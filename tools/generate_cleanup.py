"""Generate reviewable TV-side shell scripts; no connection or execution."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def generate(profile):
    apps = sum(profile['groups'].values(), [])
    protected = profile['protected_apps']
    units = profile['runtime_units']
    markers = profile['stop_markers']
    if len(set(apps)) != len(apps) or set(apps) & set(protected):
        raise ValueError('Duplicate or protected app in disable list')
    if not all(re.fullmatch(r'[A-Za-z0-9_.-]+', item)
               for item in apps + protected + units + markers):
        raise ValueError('Invalid profile identifier')
    sql_apps = ','.join("'" + item + "'" for item in apps)
    sql_protected = ','.join("'" + item + "'" for item in protected)
    header = '''#!/bin/sh
set -eu
db=/opt/dbspace/.pkgmgr_parser.db
backup=/opt/usr/home/owner/share/bu8000-lab-backup
'''
    verify = header + f'''
test "$(sqlite3 -readonly "$db" "SELECT count(*) FROM package_app_info WHERE app_id IN ({sql_apps}) AND app_disable='true';")" = {len(apps)}
test "$(sqlite3 -readonly "$db" "SELECT count(*) FROM package_app_info WHERE app_id IN ({sql_protected}) AND app_disable='false';")" = {len(protected)}
for unit in {' '.join(units)}; do
 test "$(systemctl show "$unit" -p LoadState)" = LoadState=masked
 test "$(systemctl show "$unit" -p ActiveState)" = ActiveState=inactive
 test "$(systemctl show "$unit" -p MainPID)" = MainPID=0
done
systemctl show {' '.join(units)} -p Id -p LoadState -p ActiveState -p MainPID
echo APP_CONFIG_OK
echo 'Disabled apps: {len(apps)}; protected apps: {len(protected)}'
'''
    block = header + f'''
test -f "$backup/baseline.tsv"
for marker in {' '.join(markers)}; do test -f "/opt/usr/share/systemd/system/$marker"; done
systemctl mask --runtime {' '.join(units)}
systemctl stop --no-block {' '.join(units)}
sleep 2
for unit in {' '.join(units)}; do
 if [ "$(systemctl show "$unit" -p ActiveState)" = ActiveState=deactivating ]; then
  systemctl kill --kill-who=all --signal=SIGKILL "$unit"
 fi
done
sleep 1
systemctl reset-failed {' '.join(units)}
''' + verify[len(header):]
    apply = header + f'''
test "$(id -u)" = 0
test "$(stat -c %u /opt/usr/home/owner)" = 5001
test "${{BU8000_LAB_CONFIRMED:-}}" = 1 || {{ echo 'Read docs/cleanup.md and confirm exact model/firmware first.' >&2; exit 1; }}
test "$(sqlite3 -readonly "$db" "SELECT count(*) FROM package_app_info WHERE app_id IN ({sql_apps});")" = {len(apps)}
test "$(sqlite3 -readonly "$db" "SELECT count(*) FROM package_app_info WHERE app_id IN ({sql_protected}) AND app_disable='false';")" = {len(protected)}
# Stop before changes if baseline state cannot be faithfully restored.
if [ ! -f "$backup/baseline.tsv" ]; then
 for unit in {' '.join(units)}; do
  test "$(systemctl show "$unit" -p LoadState)" = LoadState=loaded
  test ! -e "/run/systemd/system/$unit" && test ! -L "/run/systemd/system/$unit"
 done
 mkdir -p "$backup"
 chmod 700 "$backup"
 sqlite3 -readonly -separator '|' "$db" "SELECT app_id,app_disable FROM package_app_info WHERE app_id IN ({sql_apps}) ORDER BY app_id;" > "$backup/baseline.tmp"
 test "$(wc -l < "$backup/baseline.tmp" | tr -d ' ')" = {len(apps)}
 test "$(grep -Ec '\\|(true|false)$' "$backup/baseline.tmp")" = {len(apps)}
 mv "$backup/baseline.tmp" "$backup/baseline.tsv"
fi
test "$(wc -l < "$backup/baseline.tsv" | tr -d ' ')" = {len(apps)}
test "$(cut -d '|' -f 1 "$backup/baseline.tsv" | sort -u | wc -l | tr -d ' ')" = {len(apps)}
while IFS='|' read -r app disabled; do
 case "$app" in {'|'.join(apps)}) ;; *) echo 'Invalid baseline app' >&2; exit 1;; esac
 case "$disabled" in true|false) ;; *) echo 'Invalid baseline flag' >&2; exit 1;; esac
done < "$backup/baseline.tsv"
'''
    for app in apps:
        apply += f'pkgcmd -D -t app -n {app} --uid 5001\n'
    apply += f'''
for marker in {' '.join(markers)}; do
 if [ ! -e "/opt/usr/share/systemd/system/$marker" ]; then
  touch "$backup/$marker.created"
  touch "/opt/usr/share/systemd/system/$marker"
  chmod 644 "/opt/usr/share/systemd/system/$marker"
 fi
done
''' + block[len(header):]
    restore = header + f'''
test "$(id -u)" = 0
test "$(stat -c %u /opt/usr/home/owner)" = 5001
test -f "$backup/baseline.tsv"
# Validate the entire baseline before running any package commands.
test "$(wc -l < "$backup/baseline.tsv" | tr -d ' ')" = {len(apps)}
test "$(cut -d '|' -f 1 "$backup/baseline.tsv" | sort -u | wc -l | tr -d ' ')" = {len(apps)}
while IFS='|' read -r app disabled; do
 case "$app" in {'|'.join(apps)}) ;; *) echo 'Invalid baseline app' >&2; exit 1;; esac
 case "$disabled" in true|false) ;; *) echo 'Invalid baseline flag' >&2; exit 1;; esac
done < "$backup/baseline.tsv"
# Disable boot helper before restoring packages/services.
if [ "$(sqlite3 -readonly "$db" "SELECT count(*) FROM package_app_info WHERE app_id='tvprivgrd1.svc';")" = 1 ]; then
 pkgcmd -D -t app -n tvprivgrd1.svc --uid 5001
fi
while IFS='|' read -r app disabled; do
 if [ "$disabled" = true ]; then flag=-D; else flag=-A; fi
 pkgcmd "$flag" -t app -n "$app" --uid 5001
done < "$backup/baseline.tsv"
for marker in {' '.join(markers)}; do
 if [ -f "$backup/$marker.created" ]; then
  rm -f "/opt/usr/share/systemd/system/$marker" "$backup/$marker.created"
 fi
done
systemctl unmask --runtime {' '.join(units)}
systemctl daemon-reload
echo 'Original package flags and unit loading restored. Cold reboot and test household functions.'
'''
    return {'apply.sh': apply, 'restore.sh': restore, 'verify.sh': verify,
            'block-services.sh': block}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=ROOT / 'build/cleanup')
    args = parser.parse_args()
    profile = json.loads((ROOT / 'profiles/bu8000-1720.7.json').read_text())
    args.out.mkdir(parents=True, exist_ok=True)
    for name, text in generate(profile).items():
        (args.out / name).write_text(text, encoding='utf-8', newline='\n')
    print(f'Generated {args.out}; nothing executed on a TV')


if __name__ == '__main__':
    main()
