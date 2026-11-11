# 停用组件并恢复原始状态

[README](../../README.zh-CN.md) · [准备电视和电脑](setup.md) · [隐藏“应用”页签中的推荐](smart-hub.md) · **停用组件并恢复原始状态** · [读取 Privacy Guard 开机报告](guard.md) · [验证结果](validation.md)

配置包含 37 个应用 ID，其中 4 个用于内容识别、分析和定向广告，28 个属于可选功能，另有 5 个广告组件。脚本停止并临时屏蔽 7 个服务，记录 4 个停止标记中哪些是本次创建的，并检查 24 个受保护的 ID，包括智能家居和账号组件。如果需要语音功能、TV Plus、Gaming Hub 或远程支持，请跳过完整配置。

[bu8000-1720.7.json](../../profiles/bu8000-1720.7.json)

在电脑上生成脚本并检查 `build/cleanup/`。停用应用会保留安装包和数据。数据库仅供读取。

```powershell
python tools/generate_cleanup.py
```

手动确认型号和固件，将 `apply.sh` 复制到 `private/apply.sh`，在 `set -eu` 后添加 `export BU8000_LAB_CONFIRMED=1`。在电视上以管理员权限运行该副本，然后运行 `verify.sh`。预期输出为 `APP_CONFIG_OK`，37 个 ID 已停用，24 个 ID 受保护，七项服务均处于以下状态。

```text
LoadState=masked
ActiveState=inactive
MainPID=0
```

将 `/opt/usr/home/owner/share/bu8000-lab-backup/baseline.tsv` 另存到电脑上。重试时会保留这一初始状态。中断时可能已有部分更改生效。已有的屏蔽或覆盖配置可能阻止首次应用，应予保留。备份只适用于原配置与原固件。

在同一台电视运行 `restore.sh`。它会停用开机助手，恢复原始应用标志，仅移除自己创建的停止标记，并解除临时屏蔽。冷启动后测试主页和智能家居。如果 Host PC IP 是回环地址，请先改回电脑地址并重启以恢复远程访问。旧助手将 33 个 ID 一起检查，另查 4 个。公开版统一检查 37 个。
