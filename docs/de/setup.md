# Fernseher und PC vorbereiten

[README](../../README.de.md) · **Fernseher und PC vorbereiten** · [Empfehlungen im Apps-Reiter ausblenden](smart-hub.md) · [Komponenten deaktivieren und wiederherstellen](cleanup.md) · [Startbericht von Privacy Guard lesen](guard.md) · [Prüfergebnisse](validation.md)

Unter „Info zu diesem TV“ Modell und Firmware prüfen. Getestet wurden UE55BU8000UCCE (22_KANTSU2E_UB2), T-KSU2EBDEUC-1720.7, Tizen 6.5 und .NET Core 3.1. Auf dem PC kamen Windows PowerShell, Python 3.12+, Git, Node.js, das .NET SDK und Samsung SDB 4.2.36 zum Einsatz.

Unter Apps `12345` eingeben, den Entwicklermodus einschalten und unter Host PC IP die LAN-Adresse des PCs eintragen. Bestätigen und kalt starten. Beim Test war das Gerät 15 Sekunden vom Strom getrennt. Updates und Schreibvorgänge vorher abschließen lassen. Adressen und SDB-Pfad anpassen.

```powershell
$tvIp = 'TV_LAN_IP'
$pcIp = 'PC_LAN_IP'
$sdbPath = 'PATH_TO_SDB_EXE'
& $sdbPath connect "${tvIp}:26101"
& $sdbPath devices
```

Der Fernseher sollte in der Geräteliste erscheinen. Bei VPN die Adresse der physischen LAN-Verbindung verwenden. Änderungen am System setzen einen bereits eingerichteten administrativen Zugang voraus. Zum Signieren sind eigene Samsung-Autoren- und Distributionszertifikate für diesen Fernseher erforderlich. Getestet wurden Apps2Samsung CLI 3.0.0 und ein Partner-Zertifikat. Zertifikate und Diagnoseprotokolle privat aufbewahren.
