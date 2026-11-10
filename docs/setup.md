# Подготовка и доступ

Проверенная конфигурация: UE55BU8000UCCE / 22_KANTSU2E_UB2, T-KSU2EBDEUC-1720.7, Tizen 6.5, .NET Core 3.1. Компьютер: Windows / PowerShell, Python 3.12+, Git, Node.js, .NET SDK. Использовался Samsung SDB 4.2.36.

## Developer Mode

На ТВ: Apps → `12345` → Developer Mode = ON → Host PC IP = адрес вашего ПК в LAN. Подтвердите и выполните холодный перезапуск. В опыте отключали питание на 15 секунд; не делайте этого во время обновления или записи системных файлов.

```powershell
$tvIp = 'TV_LAN_IP'
$pcIp = 'PC_LAN_IP'
$sdbPath = 'PATH_TO_SDB_EXE'
& $sdbPath connect "${tvIp}:26101"
& $sdbPath devices
```

Замените текстовые значения своими. При VPN выбирайте LAN-адрес компьютера. Отказ первого соединения не доказывает несовместимость: проверьте режим, применённый после перезапуска адрес и сеть.

**Обычный `sdb shell` может быть недоступен.** Исследование использовало публичный transport из [samsung-tv-root](https://github.com/chris-ritsen/samsung-tv-root), а root — отдельную archive-launcher цепочку. Это не штатная функция Samsung. Успешный SDB connect не доказывает наличие root.

## Точная версия транспорта

```powershell
git clone https://github.com/chris-ritsen/samsung-tv-root.git private/samsung-tv-root
git -C private/samsung-tv-root checkout 3b97edf3762db7670585d73e29623dc56195bf98
git -C private/samsung-tv-root apply ../../patches/sdb-windows.patch
python tools/build_guard.py
```

Нужен OpenSSL; в Windows к `PATH` может понадобиться добавить `usr/bin` установленного Git. Патч сохраняет LF в staging shell-файле и раньше отправляет длинную команду отдельным файлом. Он не добавляет новую root-цепочку.

Создайте `private/identity.sh` с LF:

```sh
id
cat /etc/os-release
```

```powershell
python tools/run_tv_script.py --tv $tvIp --pc $pcIp --upstream private/samsung-tv-root --sdb $sdbPath --script private/identity.sh --output private/identity.json
```

Для отдельной проверки root выполните тот же скрипт с `--root`. Сначала прочитайте документацию upstream: временно получаются привилегии и исполняется переданный shell-код. При неуспехе к изменениям не переходите. JSON-результаты могут содержать личные данные.

## Подписание приложений

Нужен собственный Samsung author/distributor certificate, разрешающий ваш ТВ. Сертификаты другого человека не подходят и не должны публиковаться. Использовался [Apps2Samsung](https://github.com/Apps2Samsung), CLI 3.0.0 и Partner certificate; актуальные параметры сверяйте через `--help`.

```powershell
apps2samsung-cli install dist/tv-privacy-guard-unsigned.wgt --tv $tvIp --local-ip $pcIp --partner --json
```

Не устанавливайте helper до подготовки [профиля очистки](cleanup.md). Ни один инструмент этого репозитория не меняет Host PC IP автоматически.
