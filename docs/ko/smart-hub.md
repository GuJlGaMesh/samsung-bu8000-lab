# 앱 탭에서 추천 숨기기

[README](../../README.ko.md) · [TV와 PC 준비하기](setup.md) · **앱 탭에서 추천 숨기기** · [구성 요소 비활성화 및 원래 상태 복원](cleanup.md) · [Privacy Guard 부팅 보고서 읽기](guard.md) · [검증 결과](validation.md)

광고 서비스를 중지해도 추천 목록은 남았습니다. 패치는 `FetchAppsHomeData`의 IL 24바이트를 변경해 기존의 설치된 앱 보기를 선택합니다. 두 원본 파일의 SHA-256 값을 표와 대조하세요.

| | SHA-256 |
|---|---|
| `AppsCommon.dll` | `431942805baf639a080300b438a6df27461dc6c1e1f013733eb9aaac0d964ec0` |
| `AppsCommon.installed-only.dll` | `6e37622457b781df5e62da697e6fba659261bf2b43647f82fb145db5aa30b05d` |
| `AppsCommon.ni.dll` | `13310b4cded98c25d95d8c17eca6093c61a02c7554dbb5d57bff610b23c3dfdc` |

TV의 `/opt/usr/apps/com.samsung.tv.store/shared/res/` 에 있는 두 원본 라이브러리를 PC의 `private/stock-apps/`로 복사해 보관하세요. 저장소 루트에서 다음 명령을 실행하세요. 역변환한 파일의 해시가 원본과 같아야 합니다.

```powershell
python tools/patch_apps_common.py private/stock-apps/AppsCommon.dll private/stock-apps/AppsCommon.installed-only.dll
python tools/patch_apps_common.py private/stock-apps/AppsCommon.installed-only.dll private/stock-apps/AppsCommon.roundtrip.dll --reverse
```

관리자 권한이 설정된 TV에서 스크립트를 `ACTION=inspect` 모드로 실행하세요. 두 해시가 일치하면 준비한 DLL을 `/home/owner/share/tmp/sdk_tools/AppsCommon.installed-only.dll` 경로로 복사하세요. 별도 스크립트 사본에 `ACTION=apply` 를 지정하고 시청을 마친 뒤 실행하세요. 홈 화면이 재시작됩니다. 스크립트는 두 파일의 소유자와 속성을 유지한 채 백업하고 네이티브 이미지를 활성 디렉터리에서 제거합니다. 종료될 때까지 전원을 유지하세요.

[stock-apps.sh](../../tv/stock-apps.sh) · [installed-only-patch.json](../../profiles/installed-only-patch.json)

홈 → 앱을 다시 열어 설치된 앱과 스마트홈 제어를 확인하세요. 되돌리려면 `ACTION=restore` 로 설정한 사본을 실행하세요. 두 원본 파일을 복원하며 업데이트 후 알 수 없는 파일이 발견되면 중단합니다. 시험에서는 추천이 사라지고 두 기능 모두 작동했습니다. 공개판 스크립트는 PC에서 확인했습니다.
