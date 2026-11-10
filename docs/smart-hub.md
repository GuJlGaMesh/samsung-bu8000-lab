# Подборки в штатной вкладке «Приложения»

Остановка adagent не убрала «Рекомендации экспертов». Данные вкладки загружаются через `Tizen.TV.Service.AppsCommon.AppsHomeDataManager.FetchAppsHomeData` из `AppsCommon.dll`.

В библиотеке уже была ветка вывода установленных приложений. Патч направляет выполнение в неё, не включая глобальный retail/emulator mode. Меняются 24 байта IL: короткий переход и NOP. Это изменение локального UI, не разблокировка контента.

| Файл | SHA-256 |
|---|---|
| Исходный AppsCommon.dll | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| Патченный AppsCommon.dll | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| Исходный AppsCommon.ni.dll | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

[Манифест](../profiles/installed-only-patch.json) содержит RVA, смещение и байты. Даже при том же номере прошивки проверяйте хеш. Не подставляйте другой хеш без повторного анализа IL.

## Локальная подготовка

Скопируйте собственные оригинальные DLL из `/opt/usr/apps/com.samsung.tv.store/shared/res/` в `private/stock-apps/`. Для чтения может потребоваться root. Закрытые библиотеки Samsung в репозитории не распространяются.

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

Обратное преобразование должно вернуть исходный хеш. Это пока не применение на ТВ.

## Применение и откат

Нужен root и остановка просмотра: перезапускаются компоненты Home. [tv/stock-apps.sh](../tv/stock-apps.sh) проверяет хеши обеих исходных библиотек, делает backup и сохраняет владельца/атрибуты через `cp -a`. Не заменяйте права универсальными 777.

Передайте патченную DLL в `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll`. Выполните локальную копию скрипта через `run_tv_script.py --root`, заменив `ACTION=inspect` на `ACTION=apply`. По умолчанию inspect ничего не меняет.

```powershell
& $sdbPath -s "${tvIp}:26101" push private/stock-apps/AppsCommon.installed-only.dll /home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll
Copy-Item tv/stock-apps.sh private/stock-apps-apply.sh
# Теперь вручную измените ACTION в копии, сохранив UTF-8 и переводы строк LF.
python tools/run_tv_script.py --tv $tvIp --pc $pcIp --upstream private/samsung-tv-root --sdb $sdbPath --root --script private/stock-apps-apply.sh --output private/stock-apps-apply.json
```

Native image копируется в backup и удаляется из рабочего каталога, чтобы использовался изменённый managed IL. Без этого изменение DLL могло бы не повлиять на UI. Скрипт пытается восстановить оригиналы при обнаруженной ошибке; это не защита от отключения питания во время записи. Не обесточивайте ТВ до завершения команды.

Откат: копия скрипта с `ACTION=restore`. Восстанавливаются **оба** оригинала. Если рабочая библиотека уже другая, например после обновления, скрипт откажет вместо перезаписи новой версии старой.

Пользователь подтвердил исчезновение подборок, работу приложений и умного дома. Позднее повторно проверялся патченный хеш. Полного UI-теста после всех дальнейших cold boot нет. Обновление может заменить библиотеку; автоматическое перепатчивание не предусмотрено.

Публичная обёртка `stock-apps.sh` с дополнительными проверками и восстановлением проверена локально, но повторно на телевизоре не запускалась. Исторический опыт подтверждает сам бинарный патч, а не все ветки новой обёртки.
