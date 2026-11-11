# 검증 결과

[README](../../README.ko.md) · [TV와 PC 준비하기](setup.md) · [앱 탭에서 추천 숨기기](smart-hub.md) · [구성 요소 비활성화 및 원래 상태 복원](cleanup.md) · [Privacy Guard 부팅 보고서 읽기](guard.md) · **검증 결과**

2026년 11월 10일 PC에서 Python 테스트 3개가 통과했습니다. 적용과 역변환 모두 알 수 없는 바이너리를 거부했고, 비활성화 목록의 보호 앱과 ID에 포함된 셸 메타 문자도 거부했습니다. 앱 패치를 적용한 뒤 되돌린 DLL은 원본과 바이트 단위로 일치했습니다.

Windows 전송 패치는 고정된 소스 버전과 일치했습니다. .NET 구성 요소 2개가 빌드됐고 서명되지 않은 패키지가 ZIP 및 XML 검사를 통과했습니다. .NET Core 3.1 지원 종료 경고는 TV에서 사용하는 런타임에 해당합니다.

CI는 Python 테스트, 스크립트 생성, 셸 및 JavaScript 구문 검사, 공개 파일 검사를 수행합니다. 로컬 링크를 확인하고 공개 대상에 개인 정보가 있는지도 점검했습니다. TV 기록은 이전 콜드 부팅 시험에서 얻었습니다. 공개 도구는 PC에서 검증했습니다.

[cold-boot-sanitized.json](../../evidence/cold-boot-sanitized.json)
