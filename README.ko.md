# 삼성 BU8000 Tizen OS 정리하기: 기본 앱, 시청 데이터 추적, Smart Hub 추천

삼성 스마트 TV에서 불필요한 기본 앱과 자동 콘텐츠 인식(ACR)을 끄거나 Smart Hub 추천 목록을 숨길 수 있습니다. 두 변경 사항은 **UE55BU8000UCCE**, 펌웨어 **T-KSU2EBDEUC-1720.7**(Tizen 6.5)에서 각각 확인했습니다. 추천만 숨기려면 첫 번째 항목을 따르세요.

[Русский](README.md) · [English](README.en.md) · [Español](README.es.md) · [Français](README.fr.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · **한국어**

## 삼성 기본 메뉴에서 전문가 추천 숨기기

1. ‘이 TV의 정보’에서 모델 코드와 펌웨어를 확인하세요. 원본 `AppsCommon.dll`과 `AppsCommon.ni.dll`을 백업한 뒤 두 파일의 SHA-256 값을 각각 표와 대조하세요. TV 관리자 권한이 필요합니다. [앱 탭에서 추천 숨기기](docs/ko/smart-hub.md)
2. 두 값이 모두 일치하면 **홈 → 앱**에서 설치된 앱만 표시하도록 패치를 적용하세요. 적용 중 홈 화면이 다시 시작되므로 시청을 마친 뒤 작업하세요.
3. 앱 탭을 다시 열어 설치된 앱을 실행하고 스마트홈에서 TV를 조작해 보세요. 시험한 TV에서는 추천 목록이 사라졌고 두 기능 모두 작동했습니다. 되돌리려면 백업한 **원본 파일 두 개**를 모두 복원하세요.

## 삼성 기본 앱 비활성화하기

1. 먼저 37개 구성 요소의 목록을 살펴보세요. 전체 프로필을 적용하면 음성 기능, TV Plus, Gaming Hub, 원격 지원도 꺼집니다. 이 기능을 사용한다면 전체 프로필 적용을 건너뛰세요. [비활성화 대상 및 보호할 앱 목록](profiles/bu8000-1720.7.json)
2. PC에서 `python tools/generate_cleanup.py`를 실행하세요. 적용, 확인, 복원용 스크립트가 `build/cleanup/`에 생성됩니다. TV에서 적용하려면 관리자 권한이 필요합니다. 처음 적용할 때 생성되는 `baseline.tsv`에 각 앱의 원래 상태가 기록되므로 보관하세요. [구성 요소 비활성화 및 원래 상태 복원](docs/ko/cleanup.md)
3. `verify.sh`를 실행한 뒤 설치된 앱을 열고 스마트홈에서 TV를 조작해 보세요. 되돌리려면 저장한 원래 상태와 함께 `restore.sh`를 실행하고 TV를 다시 시작하세요.

전원을 분리했다가 다시 켠 시험에서 부팅 85초 뒤 콘텐츠 인식을 포함한 7개 서비스가 모두 `inactive`, `MainPID=0`이었습니다. 시험 당시 설정은 `Host PC IP = 127.0.0.1`이었습니다. 공개 버전 도구는 PC에서 확인했습니다. [TV 부팅 기록](evidence/cold-boot-sanitized.json) · [검증 결과](docs/ko/validation.md)
