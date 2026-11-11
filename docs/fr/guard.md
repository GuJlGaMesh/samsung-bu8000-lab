# Lire le rapport de démarrage de Privacy Guard

[README](../../README.fr.md) · [Préparer le téléviseur et le PC](setup.md) · [Masquer les recommandations dans Applications](smart-hub.md) · [Désactiver des composants et restaurer leur état initial](cleanup.md) · **Lire le rapport de démarrage de Privacy Guard** · [Résultats des vérifications](validation.md)

Les masques temporaires disparaissent au redémarrage. L’utilitaire en rétablit sept, vérifie les services, écrit un rapport local et se termine. Il attend la sauvegarde initiale du profil public et quatre marqueurs. Les anciennes sauvegardes ont un format différent.

Avec `Host PC IP = 127.0.0.1`, le rapport est arrivé environ 85 secondes après le démarrage à froid. L’adresse du PC permettait le diagnostic à distance. Le nettoyage automatique à froid reste à vérifier avec cette adresse, retenue à la fin de l’essai.

Consultez l’horodatage de `/home/owner/share/tvprivacyguard-status.json`. `ok=true` décrit l’état à cet instant. Sauvegardez le rapport avant toute relance manuelle. Changer l’adresse pour lire le rapport depuis le PC peut nécessiter un redémarrage. La version publique vérifie les 37 applications, garde les rapports sur le téléviseur et nettoie ses propres fichiers temporaires. Elle a été contrôlée sur PC. Pour revenir en arrière, `restore.sh` désactive `tvprivgrd1.svc` et restaure les indicateurs et marqueurs.
