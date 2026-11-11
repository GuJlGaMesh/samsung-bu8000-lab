# Prepare the TV and computer

[README](../../README.en.md) · **Prepare the TV and computer** · [Hide recommendations in Samsung Apps](smart-hub.md) · [Disable components and restore their original state](cleanup.md) · [Read the Privacy Guard boot report](guard.md) · [Validation results](validation.md)

Check **About This TV**. The tested device was a UE55BU8000UCCE (22_KANTSU2E_UB2), firmware T-KSU2EBDEUC-1720.7, Tizen 6.5 and .NET Core 3.1. The PC used Windows PowerShell, Python 3.12+, Git, Node.js, the .NET SDK and Samsung SDB 4.2.36.

In Apps, enter `12345`, enable Developer Mode and set Host PC IP to the computer’s LAN address. Confirm and cold-start the TV. The test used 15 seconds without power. Wait for updates and file writes to finish first. Replace the placeholders below with your own addresses and SDB path.

```powershell
$tvIp = 'TV_LAN_IP'
$pcIp = 'PC_LAN_IP'
$sdbPath = 'PATH_TO_SDB_EXE'
& $sdbPath connect "${tvIp}:26101"
& $sdbPath devices
```

Check that the TV appears in the device list. With a VPN, select the physical LAN address. A connection confirms device discovery. System changes require separately established administrative access. Signing an app requires your own Samsung author and distributor certificates for this TV. The test used Apps2Samsung CLI 3.0.0 and a Partner certificate. Keep certificates and diagnostic logs private.
