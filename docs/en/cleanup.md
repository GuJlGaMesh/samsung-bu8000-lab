# Disable components and restore their original state

[README](../../README.en.md) · [Prepare the TV and computer](setup.md) · [Hide recommendations in Samsung Apps](smart-hub.md) · **Disable components and restore their original state** · [Read the Privacy Guard boot report](guard.md) · [Validation results](validation.md)

The profile covers 37 app IDs: 4 for content recognition, analytics and targeted advertising, 28 for optional features and 5 more advertising components. It stops and temporarily masks seven services and records which of four stop markers it created. It checks 24 protected IDs, including smart-home and account components. Skip the full profile if you need voice control, TV Plus, Gaming Hub or remote support.

[bu8000-1720.7.json](../../profiles/bu8000-1720.7.json)

Generate the scripts on your computer and review the files in `build/cleanup/`. Disabling an app preserves its package and data. The database is read only.

```powershell
python tools/generate_cleanup.py
```

After manually checking the exact model and firmware, copy `apply.sh` to `private/apply.sh` and add `export BU8000_LAB_CONFIRMED=1` after `set -eu`. On the TV with administrative access, run that copy and then `verify.sh`. A successful check prints `APP_CONFIG_OK`. Expect 37 disabled IDs, 24 protected IDs and all seven services in the states below.

```text
LoadState=masked
ActiveState=inactive
MainPID=0
```

Copy `/opt/usr/home/owner/share/bu8000-lab-backup/baseline.tsv` to the PC. This first-run baseline is kept across retries. If interrupted, some changes may already have applied. Existing masks or overrides can block the first run. Preserve them. Use the baseline only with the original profile and firmware.

For rollback, run `restore.sh` on the same TV. It disables the boot helper, restores original app flags, removes only its own markers and lifts the temporary masks. Cold-start and test Home and smart-home control. If Host PC IP is loopback, first restore the PC’s LAN address and restart for remote access. The historical helper checked 33 IDs together and the first 4 separately. The public verifier checks all 37.
