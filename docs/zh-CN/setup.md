# 准备电视和电脑

[README](../../README.zh-CN.md) · **准备电视和电脑** · [隐藏“应用”页签中的推荐](smart-hub.md) · [停用组件并恢复原始状态](cleanup.md) · [读取 Privacy Guard 开机报告](guard.md) · [验证结果](validation.md)

打开“关于本电视”核对型号和固件。测试设备为 UE55BU8000UCCE（22_KANTSU2E_UB2），固件 T-KSU2EBDEUC-1720.7，系统 Tizen 6.5，运行时 .NET Core 3.1。电脑使用 Windows PowerShell、Python 3.12+、Git、Node.js、.NET SDK 和 Samsung SDB 4.2.36。

在“应用”页面输入 `12345`，开启开发者模式，将 Host PC IP 设为电脑的局域网地址。确认后冷启动。测试时断电 15 秒，断电前应等待系统更新和文件写入完成。将以下示例中的地址和 SDB 路径替换为实际值。

```powershell
$tvIp = 'TV_LAN_IP'
$pcIp = 'PC_LAN_IP'
$sdbPath = 'PATH_TO_SDB_EXE'
& $sdbPath connect "${tvIp}:26101"
& $sdbPath devices
```

确认设备列表中出现电视。使用 VPN 时填写物理局域网地址。修改系统需要预先配置好的管理员权限。签名应用需要自己的三星作者证书和允许在该电视上安装的分发证书。测试使用 Apps2Samsung CLI 3.0.0 和 Partner 证书。请妥善保管证书和诊断日志。
