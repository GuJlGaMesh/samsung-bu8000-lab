# 隐藏“应用”页签中的推荐

[README](../../README.zh-CN.md) · [准备电视和电脑](setup.md) · **隐藏“应用”页签中的推荐** · [停用组件并恢复原始状态](cleanup.md) · [读取 Privacy Guard 开机报告](guard.md) · [验证结果](validation.md)

停止广告服务后，推荐栏依然可见。补丁修改 `FetchAppsHomeData` 中的 24 字节 IL 指令，切换到已有的“已安装应用”视图。请先核对两个原始文件的 SHA-256。

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

从 `/opt/usr/apps/com.samsung.tv.store/shared/res/` 将自己的原始库复制到电脑上的 `private/stock-apps/`，保留两个原件。在仓库根目录运行以下命令。逆向还原后的文件应与原件哈希一致。

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

在已具备管理员权限的电视上以 `ACTION=inspect` 模式运行脚本。两个哈希均匹配后，将生成的 DLL 复制到 `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll`。在脚本副本中设置 `ACTION=apply`，等观看结束后再运行。主界面会重新启动。脚本会备份两个原件、保留所有者和属性，并将原生映像移出工作目录。执行期间保持通电。

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

重新打开“主页 → 应用”，启动已安装的应用，并通过智能家居系统操作电视。要还原，请运行设置为 `ACTION=restore` 的脚本副本。它会恢复两个原件，遇到固件更新带来的未知文件时会停止。用户确认推荐栏已消失，应用及智能家居控制正常。公开版脚本已在电脑上检查。
