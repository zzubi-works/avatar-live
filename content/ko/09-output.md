# 출력

완성한 아바타 화면을 OBS·Discord·Zoom으로 보내거나 사진·영상으로 저장합니다.

## 어떤 방식을 쓰면 되나요?

| 원하는 것 | 사용할 기능 |
|---|---|
| 이 PC의 OBS에 투명 아바타 넣기 | Spout2 |
| 다른 PC로 영상 보내기 | NDI® |
| 화상 통화의 카메라로 표시하기 | 가상 카메라 |
| 게임과 아바타를 함께 공유하기 | 화면 공유 |
| 친구의 아바타와 함께 방송하기 | [원격 합방](09-session.md) |
| 사진·동영상 파일 만들기 | 사진·녹화 |

NDI®는 Vizrt NDI AB의 등록 상표입니다. [NDI 공식 안내](https://ndi.video/)

## 출력 이미지

![출력 크기와 프레임 설정](img/guide-output-image.png)

| 항목 | 바꾸면 |
|---|---|
| 해상도 | 높이면 더 선명하고 PC 부담이 커집니다. |
| FPS | 높이면 움직임이 더 매끄럽고 PC·네트워크 부담이 커집니다. |
| 화면 비율 | 가로·세로 등 송출 화면의 모양을 바꿉니다. |
| 송출 대상 | 작업용 씬 뷰 또는 선택한 스튜디오 카메라의 영상을 보냅니다. |

Basic은 최대 1080p와 워터마크, Pro는 최대 4K와 워터마크 없는 출력을 지원합니다.

## Spout2

같은 Windows PC에서 Avatar Live의 영상을 OBS로 전달합니다.

![Spout2 송출 설정](img/guide-spout.png)

1. OBS를 종료하고 [OBS Spout2 플러그인](https://github.com/Off-World-Live/obs-spout2-plugin/releases)을 설치합니다.
2. OBS를 다시 실행합니다.
3. Avatar Live의 출력 → 송출 → Spout2를 켭니다.
4. OBS의 소스 → + → Spout2 Capture에서 Avatar Live를 선택합니다.
5. 투명 배경을 쓰려면 스튜디오 → 배경 → 투명을 고르고, OBS에서 Composite with alpha를 켭니다.

| 항목 | 하는 일 |
|---|---|
| Spout2 스위치 | 영상을 보내거나 멈춥니다. |
| 송신 이름 | OBS 소스 목록에 보이는 이름입니다. |
| 적용 | 바꾼 송신 이름을 확정합니다. OBS에서도 새 이름을 다시 고르세요. |
| 알파 보내기 | 배경 투명도를 함께 보냅니다. |

Spout2와 OBS 수신 플러그인의 이용 조건은 [Spout2 고지](13-license.md#spout2)를 따릅니다.

## NDI

네트워크로 다른 PC의 OBS 등에 영상을 보냅니다. Basic과 Pro 모두 지원합니다.

![NDI 송출 설정](img/guide-ndi.png)

1. 수신 PC의 OBS를 종료합니다.
2. [DistroAV](https://github.com/DistroAV/DistroAV/releases)와 해당 버전에서 요구하는 NDI Runtime을 설치합니다.
3. Avatar Live에서 출력 → 송출 → NDI를 켭니다.
4. 수신 OBS의 소스 → + → NDI Source에서 Avatar Live를 선택합니다.

OBS 없이 확인하려면 [NDI Tools의 Studio Monitor](https://ndi.video/tools/)를 사용할 수 있습니다. 송신 PC와 수신 PC가 서로 통신할 수 있는 네트워크여야 합니다.

NDI Runtime·NDI Tools·DistroAV의 이용 조건은 [NDI 고지](13-license.md#ndi)에서 각각 확인하세요.

## 가상 카메라

Discord·Zoom 등의 카메라 목록에서 아바타를 고르는 방식입니다.

![가상 카메라 설치와 송출 설정](img/guide-virtual-camera.png)

1. 가상 카메라 설치로 장치를 등록합니다. Windows 관리자 승인이 필요합니다.
2. 가상 카메라 스위치를 켭니다.
3. 사용할 앱의 카메라 목록에서 Avatar Live Camera를 고릅니다.

최대 1920×1080, 30fps이며 투명 배경은 전달하지 않습니다. 새 장치가 목록에 없으면 받는 앱을 다시 실행하세요.

## 화면 공유

게임이나 프로그램 위에 아바타를 겹쳐 Discord 등으로 보냅니다.

![화면 공유의 대상·오디오·아바타 배치](img/guide-share.png)

1. 출력 → 화면 공유를 엽니다.
2. 게임 또는 디스플레이를 고르고 공유할 대상을 선택합니다.
3. 아바타의 위치와 크기를 맞춘 뒤 화면 공유를 켭니다.
4. Discord의 화면 공유 → 애플리케이션에서 Avatar Live Share Output을 선택합니다.

| 조절 | 달라지는 것 |
|---|---|
| 아바타 위치·크기 | 게임 위에 놓이는 아바타의 자리와 크기를 바꿉니다. |
| 오디오 대상 | 게임·데스크톱·선택한 앱 중 공유할 소리를 고릅니다. |
| 앱 볼륨 | 공유받는 쪽의 소리 크기를 바꿉니다. 0%는 음소거, 100%는 원래 크기입니다. |
| 추가 소스 (Pro) | 다른 창이나 모니터를 더 겹칩니다. 목록 위쪽 소스가 앞에 표시됩니다. |

### 공유 소리가 안 나올 때

가상 오디오 장치가 없다는 안내가 나오면 가상 오디오 드라이버 설치를 사용할 수 있습니다. 이 버튼은 VB-Audio의 VB-CABLE을 설치하는 경로입니다. 설치 후 Windows 기본 재생 장치가 평소 쓰는 헤드폰·스피커인지 확인하세요.

VB-CABLE은 별도 제작사의 Donationware입니다. 사용 조건과 후원·라이선스 안내는 [VB-CABLE 고지](13-license.md#vb-cable)에서 확인하세요.

## 사진과 녹화

![사진 저장과 녹화 설정](img/guide-photo-record.png)

- 사진: 현재 출력 화면을 PNG로 저장합니다.
- 크롭: 사진에 담을 영역을 자릅니다.
- 비율: 가로·세로·정사각형 등 사진 모양을 고릅니다.
- 해상도: 저장 파일의 픽셀 수를 정합니다.
- 녹화 (Pro): 영상을 MP4로 저장합니다. 시작 후 정지를 눌러 파일을 마무리합니다.

## 문제가 있을 때

- [OBS에 소스가 없거나 영상이 검게 나옴](12-troubleshooting.md#obs와-영상-출력)
- [게임 공유가 검거나 소리가 안 나옴](12-troubleshooting.md#화면-공유)
- [원격 합방에 접속되지 않음](09-session.md#연결이-안-될-때)
