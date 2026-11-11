# TV와 PC 준비하기

[README](../../README.ko.md) · **TV와 PC 준비하기** · [앱 탭에서 추천 숨기기](smart-hub.md) · [구성 요소 비활성화 및 원래 상태 복원](cleanup.md) · [Privacy Guard 부팅 보고서 읽기](guard.md) · [검증 결과](validation.md)

‘이 TV의 정보’에서 모델과 펌웨어를 확인하세요. 시험한 기기는 UE55BU8000UCCE(22_KANTSU2E_UB2), 펌웨어 T-KSU2EBDEUC-1720.7, Tizen 6.5, .NET Core 3.1입니다. PC에서는 Windows PowerShell, Python 3.12 이상, Git, Node.js, .NET SDK, Samsung SDB 4.2.36을 사용했습니다.

앱 화면에서 `12345`를 입력해 개발자 모드를 켜고 Host PC IP에 PC의 LAN 주소를 입력하세요. 확인 후 전원을 완전히 껐다가 켜세요. 시험에서는 전원 플러그를 15초간 뽑았습니다. 업데이트와 파일 쓰기가 끝날 때까지 기다린 뒤 진행하세요. 아래 주소와 SDB 경로를 실제 값으로 바꾸세요.

```powershell
$tvIp = 'TV_LAN_IP'
$pcIp = 'PC_LAN_IP'
$sdbPath = 'PATH_TO_SDB_EXE'
& $sdbPath connect "${tvIp}:26101"
& $sdbPath devices
```

기기 목록에 TV가 있는지 확인하세요. VPN 사용 시 실제 LAN 주소를 선택하세요. 시스템 변경에는 이미 설정된 관리자 권한이 필요합니다. 앱 서명에는 본인의 삼성 작성자 인증서와 이 TV에서 유효한 배포자 인증서가 필요합니다. 시험에서는 Apps2Samsung CLI 3.0.0과 Partner 인증서를 사용했습니다. 인증서와 진단 로그는 비공개로 보관하세요.
