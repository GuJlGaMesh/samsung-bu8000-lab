# Startbericht von Privacy Guard lesen

[README](../../README.de.md) · [Fernseher und PC vorbereiten](setup.md) · [Empfehlungen im Apps-Reiter ausblenden](smart-hub.md) · [Komponenten deaktivieren und wiederherstellen](cleanup.md) · **Startbericht von Privacy Guard lesen** · [Prüfergebnisse](validation.md)

Laufzeitmasken gehen beim Neustart verloren. Das Hilfsprogramm setzt sieben Masken erneut, prüft die Dienste, schreibt den lokalen Bericht und beendet sich. Es benötigt die Ausgangssicherung des öffentlichen Profils und vier Stoppmarkierungen. Ältere Sicherungen haben ein anderes Format.

Beim Kaltstart mit `Host PC IP = 127.0.0.1` lag der Bericht nach ungefähr 85 Sekunden vor. Mit der PC-Adresse war die Diagnose vom Computer möglich. Der automatische Lauf nach einem Kaltstart wurde mit dieser zuletzt gewählten Einstellung nicht bestätigt.

Den Zeitstempel von `/home/owner/share/tvprivacyguard-status.json` prüfen. `ok=true` gilt für genau diesen Zeitpunkt. Vor einem manuellen Start den Bericht sichern. Zum Auslesen vom PC kann ein Adresswechsel mit Neustart erforderlich sein. Die öffentliche Version prüft 37 Apps, speichert Berichte auf dem Gerät und räumt die eigenen temporären Dateien auf. Sie wurde am PC geprüft. Für den Rückbau deaktiviert `restore.sh` den Dienst `tvprivgrd1.svc` und stellt App-Zustände und Markierungen wieder her.
