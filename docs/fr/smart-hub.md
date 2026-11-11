# Masquer les recommandations dans Applications

[README](../../README.fr.md) · [Préparer le téléviseur et le PC](setup.md) · **Masquer les recommandations dans Applications** · [Désactiver des composants et restaurer leur état initial](cleanup.md) · [Lire le rapport de démarrage de Privacy Guard](guard.md) · [Résultats des vérifications](validation.md)

Arrêter le service publicitaire laissait les sélections visibles. Le correctif modifie 24 octets de code IL dans `FetchAppsHomeData` pour sélectionner la vue des applications installées. Comparez les empreintes SHA-256 des deux originaux au tableau.

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

Copiez vos bibliothèques d’origine depuis `/opt/usr/apps/com.samsung.tv.store/shared/res/` vers `private/stock-apps/` sur le PC. Conservez les deux fichiers. Exécutez les commandes à la racine du dépôt. La transformation inverse doit redonner l’empreinte initiale.

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

Avec un accès administrateur sur le téléviseur, exécutez le script en mode `ACTION=inspect`. Si les deux empreintes correspondent, copiez la DLL préparée vers `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll`. Choisissez `ACTION=apply` dans une copie du script et lancez-la après le visionnage. L’accueil redémarre. Le script sauvegarde les deux fichiers avec leurs attributs et leur propriétaire, puis retire l’image native du répertoire actif. Maintenez l’alimentation jusqu’à la fin.

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

Rouvrez Accueil → Applications, lancez une application et vérifiez la commande domotique. Pour annuler, utilisez une copie avec `ACTION=restore`. Elle restaure les deux originaux et refuse d’écraser une bibliothèque inconnue après mise à jour. L’utilisateur a confirmé la disparition des sélections et le fonctionnement des deux commandes. Le script publié a été vérifié sur PC.
