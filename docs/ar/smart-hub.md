# إخفاء التوصيات من تبويب التطبيقات

[README](../../README.ar.md) · [إعداد التلفزيون والحاسوب](setup.md) · **إخفاء التوصيات من تبويب التطبيقات** · [تعطيل المكوّنات واستعادة حالتها الأصلية](cleanup.md) · [قراءة تقرير بدء تشغيل Privacy Guard](guard.md) · [نتائج التحقق](validation.md)

بقيت التوصيات ظاهرة بعد إيقاف خدمة الإعلانات. يعدّل التصحيح 24 بايت من تعليمات IL في `FetchAppsHomeData` لاختيار عرض التطبيقات المثبّتة الموجود أصلًا. قارن بصمة SHA-256 لكل من الملفين الأصليين بالجدول.

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

انسخ المكتبتين الأصليتين من `/opt/usr/apps/com.samsung.tv.store/shared/res/` إلى `private/stock-apps/` على الحاسوب واحتفظ بهما. نفّذ الأمرين التاليين من المجلد الرئيسي للمستودع. يجب أن تعيد العملية العكسية البصمة الأصلية.

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

على تلفزيون مهيأ بصلاحيات المسؤول، شغّل السكربت في وضع `ACTION=inspect`. عند تطابق البصمتين، انسخ ملف DLL المُعدّ إلى `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll`. اختر `ACTION=apply` في نسخة منفصلة من السكربت وشغّلها بعد انتهاء المشاهدة. ستُعاد تهيئة الشاشة الرئيسية. يحفظ السكربت نسخًا من الملفين بملكيتهما وسماتهما ويزيل الصورة الأصلية المترجمة من مجلد التشغيل. أبقِ الكهرباء موصولة حتى اكتماله.

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

افتح التطبيقات مجددًا من الشاشة الرئيسية واختبر تطبيقًا مثبّتًا والتحكم من المنزل الذكي. للتراجع شغّل نسخة مضبوطة على `ACTION=restore`. تستعيد الملفين وترفض الكتابة فوق مكتبة مجهولة بعد تحديث البرنامج. أكّد المستخدم اختفاء التوصيات وعمل الوظيفتين. اختُبرت النسخة المنشورة من السكربت على الحاسوب.
