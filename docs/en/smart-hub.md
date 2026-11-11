# Hide recommendations in Samsung Apps

[README](../../README.en.md) · [Prepare the TV and computer](setup.md) · **Hide recommendations in Samsung Apps** · [Disable components and restore their original state](cleanup.md) · [Read the Privacy Guard boot report](guard.md) · [Validation results](validation.md)

Stopping the advertising service alone left the rows visible. This patch changes 24 bytes of IL in `FetchAppsHomeData` to select the existing installed-apps view. First compare the SHA-256 of both original files with the table.

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

Copy your original libraries from `/opt/usr/apps/com.samsung.tv.store/shared/res/` to `private/stock-apps/` on your computer. Keep both originals. Run the following commands from the repository root. The reverse operation must produce the original hash.

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

On a TV where you already have administrative access, run the script in `ACTION=inspect` mode. When both original hashes match, copy the prepared DLL to `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll`. Set `ACTION=apply` in a separate copy of the script and run it after viewing. Home restarts. The script backs up both files, preserves their ownership and attributes, and removes the native image from the active directory. Keep power connected until it finishes.

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

Reopen Home → Apps and test an installed app and smart-home control. For rollback run a copy with `ACTION=restore`. It restores both originals and refuses to overwrite an unknown library after a firmware update. The owner confirmed that the rows disappeared and both functions worked. The published wrapper was tested on a PC.
