# 验证结果

[README](../../README.zh-CN.md) · [准备电视和电脑](setup.md) · [隐藏“应用”页签中的推荐](smart-hub.md) · [停用组件并恢复原始状态](cleanup.md) · [读取 Privacy Guard 开机报告](guard.md) · **验证结果**

2026 年 11 月 10 日，电脑上的三项 Python 测试通过。应用或还原补丁时均拒绝未知二进制文件；停用列表中的受保护应用和 ID 中的 shell 元字符也会被拒绝。应用补丁再还原后，DLL 与原件逐字节一致。

Windows 传输补丁与固定版本的源码一致。两个 .NET 组件均编译成功，未签名的软件包通过 ZIP 和 XML 检查。.NET Core 3.1 的支持期限警告来自电视使用的运行时。

持续集成会运行 Python 测试、生成脚本、检查 shell 和 JavaScript 语法，并扫描发布文件。还检查了本地链接，人工核对了发布内容中的隐私信息。电视记录来自早先的冷启动测试。公开版工具在电脑上进行了检查。

[cold-boot-sanitized.json](../../evidence/cold-boot-sanitized.json)
