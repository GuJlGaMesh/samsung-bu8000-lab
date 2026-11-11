# Résultats des vérifications

[README](../../README.fr.md) · [Préparer le téléviseur et le PC](setup.md) · [Masquer les recommandations dans Applications](smart-hub.md) · [Désactiver des composants et restaurer leur état initial](cleanup.md) · [Lire le rapport de démarrage de Privacy Guard](guard.md) · **Résultats des vérifications**

Le 10 novembre 2026, trois tests Python ont réussi sur PC : rejet des binaires inconnus dans les deux sens, des applications protégées dans la liste de désactivation et des métacaractères shell dans les identifiants. Après application puis inversion du correctif, la DLL était identique à l’original, octet par octet.

Le correctif de transport Windows correspondait à la révision retenue. Les deux composants .NET ont compilé et le paquet non signé a passé les contrôles ZIP et XML. L’avertissement de fin de support de .NET Core 3.1 correspond à la version utilisée par le téléviseur.

L’intégration continue lance les tests Python, génère les scripts, vérifie la syntaxe shell et JavaScript et analyse les fichiers publiés. Les liens locaux et l’absence de données privées dans la publication ont aussi été contrôlés. Le relevé du téléviseur provient de l’essai antérieur à froid. Les outils publiés ont été vérifiés sur PC.

[cold-boot-sanitized.json](../../evidence/cold-boot-sanitized.json)
