# 구성 요소 비활성화 및 원래 상태 복원

[README](../../README.ko.md) · [TV와 PC 준비하기](setup.md) · [앱 탭에서 추천 숨기기](smart-hub.md) · **구성 요소 비활성화 및 원래 상태 복원** · [Privacy Guard 부팅 보고서 읽기](guard.md) · [검증 결과](validation.md)

프로필에는 앱 ID 37개가 들어 있습니다. 콘텐츠 인식·분석·맞춤 광고 관련 4개, 선택 기능 28개, 추가 광고 구성 요소 5개입니다. 서비스 7개를 중지하고 임시로 마스킹하며 정지 표식 4개 중 새로 만든 항목을 기록합니다. 스마트홈과 계정을 포함해 보호 대상 ID 24개를 확인합니다. 음성 기능, TV Plus, Gaming Hub, 원격 지원을 사용한다면 전체 프로필 적용을 건너뛰세요.

[bu8000-1720.7.json](../../profiles/bu8000-1720.7.json)

PC에서 스크립트를 생성하고 `build/cleanup/` 내용을 확인하세요. 앱을 비활성화해도 패키지와 데이터는 유지되며 데이터베이스는 읽기 전용으로 사용합니다.

```powershell
python tools/generate_cleanup.py
```

모델과 펌웨어를 직접 대조한 뒤 `apply.sh`를 `private/apply.sh`로 복사하고 `set -eu` 다음에 `export BU8000_LAB_CONFIRMED=1` 을 추가하세요. TV에서 관리자 권한으로 이 사본을 실행한 후 `verify.sh`를 실행하세요. 성공하면 `APP_CONFIG_OK` 가 출력됩니다. 비활성 ID 37개, 보호 ID 24개, 서비스 7개 모두 다음 상태인지 확인하세요.

```text
LoadState=masked
ActiveState=inactive
MainPID=0
```

`/opt/usr/home/owner/share/bu8000-lab-backup/baseline.tsv` 파일을 PC에도 보관하세요. 다시 시도해도 최초 상태는 유지됩니다. 중단되면 일부 변경이 이미 적용됐을 수 있습니다. 기존 마스크나 재정의 설정이 최초 적용을 막으면 해당 설정을 보존하세요. 저장한 상태는 원래 프로필과 펌웨어에만 사용하세요.

같은 TV에서 `restore.sh`를 실행하면 부팅 서비스를 끄고 앱 플래그를 복원하며 자체 생성한 표식만 지운 뒤 임시 마스크를 해제합니다. 전원을 완전히 껐다 켜고 홈과 스마트홈을 시험하세요. Host PC IP가 루프백이면 PC 주소로 되돌리고 재부팅해야 원격 접속할 수 있습니다. 이전 버전은 33개와 나머지 4개를 따로 확인했고 공개 버전은 37개를 모두 확인합니다.
