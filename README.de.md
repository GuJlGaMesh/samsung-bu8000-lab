# Samsung BU8000 mit Tizen OS aufräumen: vorinstallierte Apps, Nutzungsanalyse und Empfehlungen

Auf einem Samsung Smart TV lassen sich überflüssige vorinstallierte Apps und die automatische Inhaltserkennung (ACR) abschalten oder die Empfehlungen im Smart Hub ausblenden. Beide Änderungen wurden unabhängig voneinander auf einem **UE55BU8000UCCE** mit **T-KSU2EBDEUC-1720.7** (Tizen 6.5) erprobt. Wenn nur die Empfehlungen stören, genügt der erste Abschnitt.

[Русский](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · **Deutsch** · [Português](README.pt.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

## Expertenempfehlungen im Samsung-Menü ausblenden

1. Unter „Info zu diesem TV“ Modellcode und Firmware prüfen. Die Originaldateien `AppsCommon.dll` und `AppsCommon.ni.dll` sichern und beide SHA-256-Prüfsummen mit der Tabelle vergleichen. Die Änderung erfordert Administratorrechte auf dem Fernseher. [Prüfsummen und Anleitung auf Russisch](docs/smart-hub.md)
2. Stimmen beide Prüfsummen überein, den Patch für die Ansicht der installierten Apps unter **Home → Apps** anwenden. Dabei startet die Bedienoberfläche neu. Den laufenden Film vorher zu Ende schauen.
3. Den Reiter erneut öffnen, eine installierte App starten und einen Befehl aus dem Smart-Home-System senden. Beim Test verschwanden die Empfehlungen und beide Funktionen blieben nutzbar. Zum Zurücksetzen **beide** Originaldateien wiederherstellen.

## Vorinstallierte Samsung-Apps deaktivieren

1. Zuerst die Liste der 37 Komponenten prüfen. Das vollständige Profil deaktiviert auch Sprachfunktionen, TV Plus, Gaming Hub und Fernwartung. Wer eine dieser Funktionen nutzt, sollte das vollständige Profil überspringen. [Deaktivierte und geschützte Apps](profiles/bu8000-1720.7.json)
2. Auf dem PC `python tools/generate_cleanup.py` ausführen. Die Skripte zum Anwenden, Prüfen und Wiederherstellen liegen danach in `build/cleanup/`. Zum Anwenden sind Administratorrechte auf dem Fernseher erforderlich. Die beim ersten Anwenden erstellte `baseline.tsv` enthält den ursprünglichen Zustand jeder App. Diese Datei aufbewahren. [Anwenden und Wiederherstellen (Russisch)](docs/cleanup.md)
3. `verify.sh` ausführen, eine installierte App öffnen und die Smart-Home-Steuerung testen. Zum Zurücksetzen `restore.sh` mit dem gesicherten Ausgangszustand verwenden und den Fernseher neu starten.

Beim aufgezeichneten Kaltstart meldeten alle sieben ausgewählten Dienste einschließlich der Inhaltserkennung nach 85 Sekunden `inactive` und `MainPID=0`. Dabei war `Host PC IP = 127.0.0.1` eingestellt. Die veröffentlichten Werkzeuge wurden am PC geprüft. [Protokoll des Fernsehers](evidence/cold-boot-sanitized.json) · [Prüfbericht auf Russisch](docs/validation.md)
