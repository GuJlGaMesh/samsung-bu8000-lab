# アプリ画面のおすすめを非表示にする

[README](../../README.ja.md) · [テレビと PC の準備](setup.md) · **アプリ画面のおすすめを非表示にする** · [コンポーネントの無効化と復元](cleanup.md) · [Privacy Guard の起動レポートを読む](guard.md) · [検証結果](validation.md)

広告サービスを止めてもおすすめ欄は残りました。パッチは `FetchAppsHomeData` 内の IL を 24 バイト変更し、既存のインストール済みアプリ表示を選びます。まず元ファイル 2 個の SHA-256 を表と照合します。

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

`/opt/usr/apps/com.samsung.tv.store/shared/res/` にある自分のテレビのライブラリを、PC の `private/stock-apps/` にコピーし、両方の原本を保管します。リポジトリのルートで以下を実行します。逆変換後のハッシュが原本と一致することを確認してください。

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

管理者権限のあるテレビでスクリプトを `ACTION=inspect` モードで実行します。両方のハッシュが一致したら、加工した DLL を `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll` にコピーします。スクリプトのコピーを `ACTION=apply` に設定し、視聴が終わってから実行します。ホーム画面が再起動します。スクリプトは所有者と属性を保持して両方のファイルをバックアップし、使用中のディレクトリからネイティブイメージを取り除きます。終了まで通電を維持してください。

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

「ホーム → アプリ」を開き直し、アプリの起動とスマートホーム操作を確認します。復元には `ACTION=restore` を設定したコピーを実行します。元の 2 ファイルを復元し、更新後などで未知のファイルが見つかった場合は停止します。実機ではおすすめ欄が消え、両方の操作に成功しました。公開版スクリプトは PC で検証しました。
