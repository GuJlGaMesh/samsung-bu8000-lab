# Komponenten deaktivieren und wiederherstellen

[README](../../README.de.md) · [Fernseher und PC vorbereiten](setup.md) · [Empfehlungen im Apps-Reiter ausblenden](smart-hub.md) · **Komponenten deaktivieren und wiederherstellen** · [Startbericht von Privacy Guard lesen](guard.md) · [Prüfergebnisse](validation.md)

Das Profil umfasst 37 App-IDs: 4 für Inhaltserkennung, Analyse und gezielte Werbung, 28 für optionale Funktionen und 5 weitere Werbekomponenten. Es stoppt und maskiert sieben Dienste vorübergehend und vermerkt, welche der vier Stoppmarkierungen es angelegt hat. 24 geschützte IDs einschließlich Smart Home und Samsung-Konto werden geprüft. Wer Sprache, TV Plus, Gaming Hub oder Fernwartung braucht, sollte das vollständige Profil auslassen.

[bu8000-1720.7.json](../../profiles/bu8000-1720.7.json)

Am PC die Skripte erzeugen und `build/cleanup/` prüfen. Paket und Daten bleiben beim Deaktivieren erhalten. Die Datenbank wird nur gelesen.

```powershell
python tools/generate_cleanup.py
```

Modell und Firmware manuell abgleichen, `apply.sh` nach `private/apply.sh` kopieren und hinter `set -eu` die Zeile `export BU8000_LAB_CONFIRMED=1` einfügen. Auf dem Fernseher mit Administratorrechten diese Kopie und dann `verify.sh` ausführen. Erwartet werden `APP_CONFIG_OK`, 37 deaktivierte und 24 geschützte IDs sowie folgende Zustände bei allen sieben Diensten.

```text
LoadState=masked
ActiveState=inactive
MainPID=0
```

`/opt/usr/home/owner/share/bu8000-lab-backup/baseline.tsv` auch am PC sichern. Dieser Ausgangszustand bleibt bei weiteren Versuchen erhalten. Bei einem Abbruch können einzelne Änderungen bereits aktiv sein. Vorhandene Masken oder abweichende Einstellungen können den ersten Lauf verhindern. Diese beibehalten. Die Sicherung gilt für das ursprüngliche Profil und die ursprüngliche Firmware.

Zum Zurücksetzen auf demselben Fernseher `restore.sh` ausführen. Es deaktiviert den Startdienst, stellt die ursprünglichen App-Zustände wieder her, entfernt eigene Markierungen und hebt die Laufzeitmasken auf. Kalt starten und Home sowie die Smart-Home-Steuerung testen. Bei Loopback als Host PC IP zuerst die PC-Adresse wieder eintragen und für den Fernzugriff neu starten. Früher wurden 33 IDs zusammen und 4 separat geprüft. Die öffentliche Version prüft alle 37.
