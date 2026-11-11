# 三星 BU8000 的 Tizen OS 清理指南：停用预装应用、收视跟踪和 Smart Hub 推荐

在三星智能电视上停用多余的预装应用和自动内容识别（ACR），或隐藏 Smart Hub 的推荐栏。两项改动已分别在 **UE55BU8000UCCE** 上测试，固件为 **T-KSU2EBDEUC-1720.7**（Tizen 6.5）。如果只想隐藏推荐，请看第一节。

[Русский](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [العربية](README.ar.md) · **简体中文** · [Deutsch](README.de.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

## 隐藏三星“应用”页签中的“专家推荐”

1. 在“关于本电视”中核对型号和固件。备份原始的 `AppsCommon.dll` 和 `AppsCommon.ni.dll`，将两份文件的 SHA-256 分别与表中的值核对。修改需要电视上的管理员权限。[隐藏“应用”页签中的推荐](docs/zh-CN/smart-hub.md)
2. 仅在两个哈希值均一致时应用补丁。“主页 → 应用”将切换为已安装应用视图。应用补丁会重启主界面，请等到观看结束后再操作。
3. 重新打开页签，启动一个已安装的应用，再用智能家居系统控制电视。测试机上的推荐栏消失了，两项检查均通过。要撤销修改，请恢复**两个原始文件**。

## 停用三星内置应用

1. 先查看配置中列出的 37 个组件。完整配置还会停用语音功能、TV Plus、Gaming Hub 和远程支持。如果需要其中任何功能，请跳过完整配置。[停用及保留的应用](profiles/bu8000-1720.7.json)
2. 在电脑上运行 `python tools/generate_cleanup.py`。应用、验证和还原脚本会生成在 `build/cleanup/` 中。应用配置需要电视上的管理员权限。请保留首次应用时生成的 `baseline.tsv`，其中记录了每个应用的原始状态。 [停用组件并恢复原始状态](docs/zh-CN/cleanup.md)
3. 运行 `verify.sh`，然后打开已安装的应用，并从智能家居系统向电视发送指令。如需还原，使用 `restore.sh` 和原始状态文件，然后重启电视。

在记录的一次断电重启中，第 85 秒时，包括内容识别在内的七项服务均显示 `inactive` 和 `MainPID=0`。测试时使用 `Host PC IP = 127.0.0.1`。公开发布的工具已在电脑上检查。[电视冷启动记录](evidence/cold-boot-sanitized.json) · [验证结果](docs/zh-CN/validation.md)
