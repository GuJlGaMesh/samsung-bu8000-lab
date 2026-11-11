# Préparer le téléviseur et le PC

[README](../../README.fr.md) · **Préparer le téléviseur et le PC** · [Masquer les recommandations dans Applications](smart-hub.md) · [Désactiver des composants et restaurer leur état initial](cleanup.md) · [Lire le rapport de démarrage de Privacy Guard](guard.md) · [Résultats des vérifications](validation.md)

Dans « À propos de ce téléviseur », vérifiez le modèle UE55BU8000UCCE (22_KANTSU2E_UB2) et le micrologiciel T-KSU2EBDEUC-1720.7. Les essais utilisaient Tizen 6.5 et .NET Core 3.1, avec Windows PowerShell, Python 3.12+, Git, Node.js, le SDK .NET et Samsung SDB 4.2.36 sur le PC.

Dans Applications, saisissez `12345`, activez le mode développeur et renseignez l’adresse locale du PC dans Host PC IP. Confirmez et redémarrez à froid. Lors des essais, le téléviseur est resté débranché 15 secondes. Attendez la fin des mises à jour et des écritures. Adaptez les adresses et le chemin de SDB.

```powershell
$tvIp = 'TV_LAN_IP'
$pcIp = 'PC_LAN_IP'
$sdbPath = 'PATH_TO_SDB_EXE'
& $sdbPath connect "${tvIp}:26101"
& $sdbPath devices
```

Vérifiez que le téléviseur figure dans la liste. Avec un VPN, choisissez l’adresse du réseau local physique. Les changements système exigent un accès administrateur déjà configuré. Pour signer une application, utilisez vos propres certificats Samsung d’auteur et de distributeur autorisés pour ce téléviseur. Les essais utilisaient Apps2Samsung CLI 3.0.0 et un certificat Partner. Gardez certificats et journaux confidentiels.
