# Empfehlungen im Apps-Reiter ausblenden

[README](../../README.de.md) · [Fernseher und PC vorbereiten](setup.md) · **Empfehlungen im Apps-Reiter ausblenden** · [Komponenten deaktivieren und wiederherstellen](cleanup.md) · [Startbericht von Privacy Guard lesen](guard.md) · [Prüfergebnisse](validation.md)

Nach dem Stoppen des Werbedienstes blieben die Reihen sichtbar. Der Patch ändert 24 Byte IL in `FetchAppsHomeData` und wählt die vorhandene Ansicht der installierten Apps. Beide Originaldateien mit den SHA-256-Werten vergleichen.

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

Die eigenen Originalbibliotheken aus `/opt/usr/apps/com.samsung.tv.store/shared/res/` auf den PC nach `private/stock-apps/` kopieren und beide aufbewahren. Im Stammverzeichnis des Repositorys ausführen. Die Rückwandlung muss die ursprüngliche Prüfsumme ergeben.

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

Auf dem Fernseher mit administrativem Zugang das Skript im Modus `ACTION=inspect` ausführen. Stimmen beide Werte, die vorbereitete DLL nach `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll` kopieren. In einer Skriptkopie `ACTION=apply` einstellen und nach dem Fernsehen starten. Home startet neu. Das Skript sichert beide Dateien mit Eigentümer und Attributen und entfernt das native Abbild aus dem aktiven Verzeichnis. Bis zum Abschluss die Stromversorgung aufrechterhalten.

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

Home → Apps erneut öffnen, eine App starten und die Smart-Home-Steuerung prüfen. Eine Kopie mit `ACTION=restore` stellt beide Originale wieder her. Eine unbekannte Bibliothek nach einem Firmwareupdate wird nicht überschrieben. Beim Test verschwanden die Empfehlungen und beide Funktionen blieben nutzbar. Das veröffentlichte Skript wurde am PC geprüft.
