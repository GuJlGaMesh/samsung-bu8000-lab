# Désactiver des composants et restaurer leur état initial

[README](../../README.fr.md) · [Préparer le téléviseur et le PC](setup.md) · [Masquer les recommandations dans Applications](smart-hub.md) · **Désactiver des composants et restaurer leur état initial** · [Lire le rapport de démarrage de Privacy Guard](guard.md) · [Résultats des vérifications](validation.md)

Le profil couvre 37 identifiants : 4 pour la reconnaissance du contenu, l’analyse et la publicité ciblée, 28 pour des fonctions facultatives et 5 autres composants publicitaires. Il arrête et masque temporairement sept services, consigne lesquels des quatre marqueurs d’arrêt il a créés et contrôle 24 identifiants protégés, dont ceux de la domotique et du compte. Évitez le profil complet si vous utilisez la voix, TV Plus, Gaming Hub ou l’assistance à distance.

[bu8000-1720.7.json](../../profiles/bu8000-1720.7.json)

Générez les scripts sur le PC et examinez `build/cleanup/`. La désactivation conserve le paquet et ses données. La base est consultée en lecture seule.

```powershell
python tools/generate_cleanup.py
```

Après vérification manuelle du modèle et du micrologiciel, copiez `apply.sh` dans `private/apply.sh` et ajoutez `export BU8000_LAB_CONFIRMED=1` après `set -eu`. Avec les droits administrateur sur le téléviseur, lancez cette copie puis `verify.sh`. Le résultat attendu est `APP_CONFIG_OK`, avec 37 identifiants désactivés, 24 protégés et les états suivants pour les sept services.

```text
LoadState=masked
ActiveState=inactive
MainPID=0
```

Copiez `/opt/usr/home/owner/share/bu8000-lab-backup/baseline.tsv` sur le PC. L’état initial est conservé en cas de nouvel essai. Une interruption peut laisser des changements partiels. Des masques ou réglages existants peuvent bloquer la première exécution ; conservez-les. Réutilisez la sauvegarde uniquement avec le profil et le micrologiciel d’origine.

Sur le même téléviseur, `restore.sh` désactive le service de démarrage, rétablit les indicateurs initiaux, supprime ses propres marqueurs et lève les masques temporaires. Redémarrez à froid et testez l’accueil et la domotique. Si Host PC IP est l’adresse de bouclage, remettez l’adresse du PC puis redémarrez pour rétablir l’accès distant. L’ancien outil contrôlait 33 identifiants ensemble et 4 séparément. La version publique vérifie les 37.
