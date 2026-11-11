# ऐप टैब से सुझाव हटाएँ

[README](../../README.hi.md) · [टीवी और कंप्यूटर तैयार करें](setup.md) · **ऐप टैब से सुझाव हटाएँ** · [घटक बंद करें और मूल स्थिति बहाल करें](cleanup.md) · [Privacy Guard की बूट रिपोर्ट पढ़ें](guard.md) · [जाँच के परिणाम](validation.md)

विज्ञापन सेवा रोकने के बाद भी सुझाव दिखाई देते थे। पैच `FetchAppsHomeData` में IL के 24 बाइट बदलकर पहले से उपलब्ध इंस्टॉल किए गए ऐप का दृश्य चुनता है। दोनों मूल फ़ाइलों के SHA-256 हैश तालिका से मिलाएँ।

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

अपनी मूल लाइब्रेरी `/opt/usr/apps/com.samsung.tv.store/shared/res/` से कंप्यूटर पर `private/stock-apps/` में कॉपी करें और दोनों मूल फ़ाइलें सँभालें। रिपॉज़िटरी की मूल डायरेक्टरी से नीचे की कमांड चलाएँ। उलटी प्रक्रिया से मूल हैश मिलना चाहिए।

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

व्यवस्थापक अधिकार उपलब्ध होने पर टीवी पर स्क्रिप्ट `ACTION=inspect` मोड में चलाएँ। दोनों हैश मिलने पर तैयार DLL को `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll` पर कॉपी करें। स्क्रिप्ट की अलग कॉपी में `ACTION=apply` सेट करें और देखना समाप्त होने के बाद चलाएँ। होम स्क्रीन फिर शुरू होगी। स्क्रिप्ट दोनों फ़ाइलों का बैकअप लेती है, स्वामित्व और गुण सुरक्षित रखती है और नेटिव इमेज को सक्रिय डायरेक्टरी से हटाती है। काम पूरा होने तक बिजली चालू रखें।

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

Home → Apps फिर खोलें। इंस्टॉल किया हुआ ऐप चलाएँ और स्मार्ट होम से टीवी नियंत्रित करें। बदलाव वापस लेने के लिए `ACTION=restore` वाली कॉपी चलाएँ। यह दोनों मूल फ़ाइलें बहाल करती है और फ़र्मवेयर अपडेट के बाद अनजान लाइब्रेरी को बदलने से मना करती है। उपयोगकर्ता ने सुझाव हटने और दोनों सुविधाओं के काम करने की पुष्टि की। प्रकाशित स्क्रिप्ट कंप्यूटर पर जाँची गई।
