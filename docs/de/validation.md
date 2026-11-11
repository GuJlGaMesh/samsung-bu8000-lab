# Prüfergebnisse

[README](../../README.de.md) · [Fernseher und PC vorbereiten](setup.md) · [Empfehlungen im Apps-Reiter ausblenden](smart-hub.md) · [Komponenten deaktivieren und wiederherstellen](cleanup.md) · [Startbericht von Privacy Guard lesen](guard.md) · **Prüfergebnisse**

Am 10. November 2026 bestanden drei Python-Tests auf dem PC. Unbekannte Binärdateien wurden in beiden Richtungen abgewiesen, geschützte Apps in der Deaktivierungsliste und Shell-Metazeichen in IDs zurückgewiesen. Patch und Rückwandlung ergaben bytegenau die ursprüngliche DLL.

Der Windows-Transportpatch entsprach der festgelegten Quellversion. Beide .NET-Komponenten ließen sich bauen. Das unsignierte Paket bestand die ZIP- und XML-Prüfungen. Die Supportwarnung für .NET Core 3.1 betrifft die Laufzeitumgebung dieses Geräts.

CI führt die Python-Tests aus, erzeugt Skripte, prüft Shell- und JavaScript-Syntax und durchsucht die veröffentlichten Dateien. Lokale Links und der Dateibestand wurden auf Fehler und private Daten geprüft. Das Geräteprotokoll stammt vom früheren Kaltstart. Die öffentlichen Werkzeuge wurden am PC geprüft.

[cold-boot-sanitized.json](../../evidence/cold-boot-sanitized.json)
