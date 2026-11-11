# テレビと PC の準備

[README](../../README.ja.md) · **テレビと PC の準備** · [アプリ画面のおすすめを非表示にする](smart-hub.md) · [コンポーネントの無効化と復元](cleanup.md) · [Privacy Guard の起動レポートを読む](guard.md) · [検証結果](validation.md)

「このテレビについて」で型番とファームウェアを確認します。検証機は UE55BU8000UCCE（22_KANTSU2E_UB2）、T-KSU2EBDEUC-1720.7、Tizen 6.5、.NET Core 3.1 です。PC では Windows PowerShell、Python 3.12 以降、Git、Node.js、.NET SDK、Samsung SDB 4.2.36 を使用しました。

「アプリ」で `12345` と入力して開発者モードを有効にし、Host PC IP に PC の LAN アドレスを指定します。確定してコールドブートします。検証時は電源プラグを 15 秒間抜きました。更新や書き込みが終わるまで電源を切らないでください。下記のアドレスと SDB のパスを実際の値に置き換えます。

```powershell
$tvIp = 'TV_LAN_IP'
$pcIp = 'PC_LAN_IP'
$sdbPath = 'PATH_TO_SDB_EXE'
& $sdbPath connect "${tvIp}:26101"
& $sdbPath devices
```

一覧にテレビが表示されることを確認します。VPN 使用時は物理 LAN のアドレスを選びます。システム変更には設定済みの管理者権限が必要です。アプリの署名には自分の Samsung 作者証明書と、そのテレビで有効な配布者証明書を使います。検証時は Apps2Samsung CLI 3.0.0 と Partner 証明書を使用しました。証明書と診断ログは個人で保管してください。
