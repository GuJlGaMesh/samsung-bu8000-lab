# Nettoyer Tizen OS sur Samsung BU8000 : applications préinstallées, suivi et recommandations

Désactivez les applications préinstallées superflues et la reconnaissance automatique de contenu (ACR) de votre Smart TV Samsung, ou masquez les recommandations de Smart Hub. Ces changements ont été testés séparément sur un **UE55BU8000UCCE** équipé de **T-KSU2EBDEUC-1720.7** (Tizen 6.5). Pour les recommandations seules, suivez la première section.

[Русский](README.md) · [English](README.en.md) · [Español](README.es.md) · **Français** · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

## Masquer les recommandations des experts dans l’accueil Samsung

1. Vérifiez le modèle et le micrologiciel dans **À propos de ce téléviseur**. Sauvegardez les originaux `AppsCommon.dll` et `AppsCommon.ni.dll`, puis comparez leurs deux empreintes SHA-256 avec le tableau. La modification nécessite des droits d’administration sur le téléviseur. [Masquer les recommandations dans Applications](docs/fr/smart-hub.md)
2. Si les deux empreintes correspondent, appliquez le correctif qui affiche les applications installées dans **Accueil → Applications**. L’opération redémarre l’accueil. Attendez la fin du visionnage.
3. Rouvrez l’onglet, lancez une application et envoyez une commande depuis votre système domotique. Les recommandations ont disparu et les deux vérifications ont réussi. Pour annuler, restaurez **les deux** fichiers d’origine.

## Désactiver des applications Samsung préinstallées

1. Consultez le profil avant de l’appliquer. Les 37 composants comprennent les fonctions vocales, TV Plus, Gaming Hub et l’assistance à distance. Si vous utilisez ces fonctions, évitez le profil complet. [Applications désactivées et protégées](profiles/bu8000-1720.7.json)
2. Lancez `python tools/generate_cleanup.py` sur l’ordinateur. Les scripts d’application, de vérification et de restauration sont créés dans `build/cleanup/`. L’application du profil nécessite des droits d’administration sur le téléviseur. Conservez le fichier `baseline.tsv` créé à la première application. Il contient l’état initial de chaque application. [Désactiver des composants et restaurer leur état initial](docs/fr/cleanup.md)
3. Exécutez `verify.sh`, ouvrez une application installée et commandez le téléviseur depuis votre système domotique. Pour revenir en arrière, utilisez `restore.sh` avec l’état initial sauvegardé, puis redémarrez le téléviseur.

Lors d’un démarrage à froid enregistré, les sept services sélectionnés, dont celui de reconnaissance du contenu, indiquaient `inactive` et `MainPID=0` après 85 secondes. Le réglage était `Host PC IP = 127.0.0.1`. Les outils publiés ont été vérifiés sur PC. [Relevé du téléviseur](evidence/cold-boot-sanitized.json) · [Résultats des vérifications](docs/fr/validation.md)
