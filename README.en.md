# Samsung BU8000 Tizen OS debloat: built-in apps, viewing analytics and Smart Hub recommendations

Disable unwanted preinstalled apps and automatic content recognition (ACR) on a Samsung Smart TV, or remove recommendation rows from Smart Hub. We tested these changes independently on a **UE55BU8000UCCE** running **T-KSU2EBDEUC-1720.7** (Tizen 6.5). For recommendations alone, start with the first section.

[Русский](README.md) · **English** · [Español](README.es.md) · [Français](README.fr.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

## Hide Expert Recommendations in Samsung Home

1. Check the model and firmware under **About This TV**. Back up the original `AppsCommon.dll` and `AppsCommon.ni.dll` and compare both SHA-256 hashes with the table. The change requires administrative access on the TV. [Hide recommendations in Samsung Apps](docs/en/smart-hub.md)
2. If both hashes match, apply the patch that selects the installed-apps view under **Home → Apps**. Applying it restarts Home, so wait until you have finished watching.
3. Reopen the tab, launch an app and send a command from your smart-home system. The recommendations disappeared and both checks passed on the test TV. To undo the change, restore **both** original files.

## Disable built-in Samsung apps

1. Review the profile before applying it. The 37 components include voice features, TV Plus, Gaming Hub and remote support. Skip the full profile if you use those features. [Disabled and protected apps](profiles/bu8000-1720.7.json)
2. Run `python tools/generate_cleanup.py` on your computer. It creates the apply, verify and restore scripts in `build/cleanup/`. Applying the profile requires administrative access on the TV. Keep the `baseline.tsv` created on first application. It records each app’s original state. [Disable components and restore their original state](docs/en/cleanup.md)
3. Run `verify.sh`, open an installed app and control the TV from your smart-home system. To undo the changes, run `restore.sh` with the saved baseline and restart the TV.

In one recorded cold boot, all seven selected services, including content recognition, showed `inactive` and `MainPID=0` at 85 seconds. The test used `Host PC IP = 127.0.0.1`. The published tools were checked on a PC. [TV test record](evidence/cold-boot-sanitized.json) · [Validation results](docs/en/validation.md)
