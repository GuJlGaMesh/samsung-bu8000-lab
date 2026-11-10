#!/bin/sh
# Read docs/smart-hub.md. Edit ACTION in a local copy before explicit execution.
set -eu
ACTION=inspect
res=/opt/usr/apps/com.samsung.tv.store/shared/res
backup=/opt/usr/home/owner/share/bu8000-lab-backup/stock-apps
input=/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll
original=431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0
patched=6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d
native=13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc
hash() { sha256sum "$1" | cut -d' ' -f1; }
require_hash() { test -f "$1" && test ! -L "$1" && test "$(hash "$1")" = "$2"; }
fail() { echo "$*" >&2; exit 1; }

case "$ACTION" in
 inspect)
  sha256sum "$res/AppsCommon.dll"
  if [ -f "$res/AppsCommon.ni.dll" ]; then sha256sum "$res/AppsCommon.ni.dll"; fi
  exit 0 ;;
 apply|restore) ;;
 *) fail 'Unknown action' ;;
esac
test "$(id -u)" = 0 || fail 'Root required'
test ! -L "$res/AppsCommon.dll" || fail 'Unexpected symlink'
current=$(hash "$res/AppsCommon.dll")
case "$current" in "$original"|"$patched") ;; *) fail 'Unrecognized working DLL; refusing overwrite';; esac
if [ -e "$res/AppsCommon.ni.dll" ] || [ -L "$res/AppsCommon.ni.dll" ]; then
 require_hash "$res/AppsCommon.ni.dll" "$native" || fail 'Unrecognized native image'
fi

if [ "$ACTION" = apply ]; then
 require_hash "$input" "$patched" || fail 'Unrecognized patch input'
 if [ ! -d "$backup" ]; then
  # Backup must be captured from a complete original state.
  test "$current" = "$original" || fail 'No original backup'
  require_hash "$res/AppsCommon.ni.dll" "$native" || fail 'Original native image missing'
  mkdir -p "$backup"
  chmod 700 "$backup"
  cp -a "$res/AppsCommon.dll" "$backup/AppsCommon.original.dll"
  cp -a "$res/AppsCommon.ni.dll" "$backup/AppsCommon.original.ni.dll"
 fi
fi
# Never replace a partial or stale baseline silently.
require_hash "$backup/AppsCommon.original.dll" "$original" || fail 'Original backup invalid'
require_hash "$backup/AppsCommon.original.ni.dll" "$native" || fail 'Native backup invalid'
if [ "$ACTION" = apply ] && [ "$current" = "$patched" ] && [ ! -e "$res/AppsCommon.ni.dll" ]; then
 echo ALREADY_APPLIED
 exit 0
fi

# Pre-stage all recovery files, preserving original owner, mode and labels.
managed_tmp="$res/AppsCommon.bu8000-new"
native_tmp="$res/AppsCommon.bu8000-native"
recovery_tmp="$res/AppsCommon.bu8000-recovery"
for item in "$managed_tmp" "$native_tmp" "$recovery_tmp"; do
 test ! -e "$item" && test ! -L "$item" || fail 'Staging file exists; inspect before retrying'
done
cp -a "$backup/AppsCommon.original.dll" "$managed_tmp"
cp -a "$backup/AppsCommon.original.dll" "$recovery_tmp"
cp -a "$backup/AppsCommon.original.ni.dll" "$native_tmp"
if [ "$ACTION" = apply ]; then
 cat "$input" > "$managed_tmp"
 require_hash "$managed_tmp" "$patched" || fail 'Staged patch hash mismatch'
fi
recover() {
 trap - EXIT HUP INT TERM
 set +e
 echo 'Interrupted change; attempting original-file recovery.' >&2
 mv -f "$recovery_tmp" "$res/AppsCommon.dll"
 if [ -f "$native_tmp" ]; then mv -f "$native_tmp" "$res/AppsCommon.ni.dll"; fi
 require_hash "$res/AppsCommon.dll" "$original" && require_hash "$res/AppsCommon.ni.dll" "$native"
 recovery_status=$?
 rm -f "$managed_tmp"
 app_launcher -s com.samsung.tv.csfs
 echo "Recovery verification exit code: $recovery_status" >&2
 exit 1
}
trap recover EXIT
trap 'exit 1' HUP INT TERM
app_launcher -k com.samsung.tv.home.media || true
app_launcher -k com.samsung.tv.csfs || true
if [ "$ACTION" = apply ]; then
 # Both originals are already backed up and verified.
 rm -f "$res/AppsCommon.ni.dll"
 mv -f "$managed_tmp" "$res/AppsCommon.dll"
 require_hash "$res/AppsCommon.dll" "$patched"
else
 mv -f "$managed_tmp" "$res/AppsCommon.dll"
 mv -f "$native_tmp" "$res/AppsCommon.ni.dll"
 require_hash "$res/AppsCommon.dll" "$original"
 require_hash "$res/AppsCommon.ni.dll" "$native"
fi
app_launcher -s com.samsung.tv.csfs
trap - EXIT HUP INT TERM
rm -f "$native_tmp" "$recovery_tmp"
sha256sum "$res/AppsCommon.dll"
ls -lZ "$res/AppsCommon.dll"
echo "Completed: $ACTION. Check Home, apps and smart-home control manually."
