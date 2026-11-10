# Отключение компонентов и восстановление

[Полный профиль](../profiles/bu8000-1720.7.json) содержит 37 app ID: 4 ACR/аналитики/targeted advertising, 28 компонентов голоса/TV Plus/Gaming Hub/remote management/preview и 5 дополнительных рекламных компонентов.

Семь служб маскируются в `/run/systemd/system` и останавливаются. Четыре vendor stop marker-файла создаются в `/opt/usr/share/systemd/system`. Отмечается, какие файлы создал именно этот набор, чтобы откат не удалил существовавшие ранее.

`pkgcmd -D` отключает приложение, **не удаляя пакет и данные**; `pkgcmd -A` включает его. SQLite используется только для чтения и проверки, не для прямого изменения флагов.

Защищённые 24 app ID включают SmartThings, Samsung account/cloud, Butler/IoT, YouTube, MSX и общие PISA/CMS/content-службы. YouTube ID зависит от установленной версии. При несовпадении количества или статуса защищённых приложений применение остановится.

Отключение голоса может нарушить голосовое управление, даже когда SmartThings через телефон работает. HDMI-CEC/PS5 после всей последовательности изменений не прошли полный итоговый тест. Если нужны голос, TV Plus, Gaming Hub или удалённая поддержка, полный профиль не подходит.

## Генерация

```powershell
python tools/generate_cleanup.py
```

Получатся `build/cleanup/{apply,restore,verify,block-services}.sh`. Прочитайте их до запуска. Публичные скрипты переработаны из исторических команд: сохранение исходных флагов и проверки усилены. **Эта новая упаковка не проходила живой цикл apply/restore на ТВ.**

После ручной проверки полного кода модели и прошивки скопируйте `apply.sh` в `private/apply.sh` и добавьте `export BU8000_LAB_CONFIRMED=1` после `set -eu`. Это подтверждение оператора, не автоматическое распознавание прошивки. Не удаляйте проверки базы.

```powershell
python tools/run_tv_script.py --tv $tvIp --pc $pcIp --upstream private/samsung-tv-root --sdb $sdbPath --root --script private/apply.sh --output private/apply-result.json
python tools/run_tv_script.py --tv $tvIp --pc $pcIp --upstream private/samsung-tv-root --sdb $sdbPath --root --script build/cleanup/verify.sh --output private/verify-result.json
```

Исходные флаги сохраняются в `/opt/usr/home/owner/share/bu8000-lab-backup/baseline.tsv`, права каталога 0700. Сохраните baseline также на ПК. При существующих runtime-масках/override первая установка откажет: простой откат не смог бы точно восстановить чужое состояние. Не удаляйте чужие маски ради обхода проверки.

Если выполнение оборвалось, часть изменений могла примениться. Повторный запуск не перезаписывает baseline. При смене профиля или прошивки старый baseline использовать нельзя.

## Откат

```powershell
python tools/run_tv_script.py --tv $tvIp --pc $pcIp --upstream private/samsung-tv-root --sdb $sdbPath --root --script build/cleanup/restore.sh --output private/restore-result.json
```

Отключается boot-service Privacy Guard, восстанавливаются **исходные app-флаги**, удаляются только собственные marker-файлы, снимаются runtime-маски. Службы не запускаются насильно в текущем сеансе: сделайте холодный перезапуск и проверьте Home, видео, умный дом, звук и нужные входы.

При Host PC IP = `127.0.0.1` для доступа с ПК сначала вручную верните адрес ПК и перезапустите ТВ.

## Проверка

Нужно получить 37 отключённых app ID, 24 сохранённых, а для семи служб — `LoadState=masked`, `ActiveState=inactive`, `MainPID=0`. Затем отдельно проверяется поведение пользователем.

Исторический поздний helper проверял 33 app ID фаз 2/3 и 24 защищённых; первые 4 ACR/analytics проверялись отдельно. Публичный verifier объединяет 37, поэтому числа отличаются.

Один холодный запуск не доказывает отсутствие всей телеметрии. OpenWrt-блокировки в этом опыте не применялись; проверенного списка доменов нет.
