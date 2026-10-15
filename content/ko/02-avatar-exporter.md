# 2. 아바타 내보내기

## v2.0.0 · Exporter 1.0.6과 VRM: 실제 준비 방법

**Unity 아바타(.vavatar)**와 **VRM(.vrm)**은 가져오는 경로가 다릅니다. Unity 프로젝트에서 만든 VRChat 아바타는 **Curious Bobby - Avatar Exporter 1.0.6**으로 내보낸 뒤 Avatar Live에서 엽니다. 반면 **VRM 0.x / 1.0은 지원되는 파일을 앱에서 직접 가져올 수 있으므로** 이를 위해 Exporter를 사용하지 않아도 됩니다.

- **Unity 프로젝트**: 기존 제작 프로젝트의 Unity **2022.3.22f1**과 호환되는 VRChat SDK를 확인하고, Exporter가 있는 프로젝트에서 아바타를 선택한 뒤 **.vavatar 내보내기**를 사용합니다. Exporter 1.0.6에서는 VRChat SDK 3.10.5 기준 PhysBone·Collider 처리와 의상 병합으로 머리카락/장식 뼈가 비활성화되던 문제를 개선했습니다.
- **이름/표정 클립/저장 폴더**: 표시 이름은 아바타 라이브러리에 보이는 이름, 표정 클립은 내보낸 모델에서 불러올 표정, 저장 폴더는 실제로 결과물이 생성되는 Windows 위치입니다. **결과 파일이 생기는 것**과 **Avatar Live에 이미 등록되는 것**은 별개이므로 내보낸 파일을 앱에서 한 번 불러오세요.
- **업데이트할 때**: Unity에서 옷/머리카락/PhysBone을 바꾼 뒤 같은 아바타를 다시 내보내면 새 데이터가 반영됩니다. 모델이 달라지면 기존 포즈·카메라·표정 설정의 적용 위치가 달라질 수 있으니 방송 전에 확인하세요.
- **VRM 모델**: 별도 Exporter 없이 가져오지만 일부 VRM 0.x 모델의 미지원 셰이더는 로딩에 실패할 수 있습니다. 이 경우 단순히 이름을 바꾸거나 확장자를 변경하는 것으로 해결되지 않습니다.
- **재배포 권한**: .vavatar·.vrm 파일의 생성·보유가 다른 참가자에게 배포할 권리를 뜻하지 않습니다. 원제작자의 모델·의상·텍스처·소품 규약을 확인하고, [원격 세션](09-output.md#원격-세션-pro-서로-다른-컴퓨터에서-합동-방송)에서 데이터 전송에 동의하기 전에 허용 여부를 확인하세요.

**내보내기를 성공했지만 화면이 분홍색이거나 특정 파츠가 사라지면:** Unity에서 올바른 재질/셰이더 및 VRChat용 PhysBone·Collider 구성을 확인하고 최신 Exporter로 다시 내보낸 후 앱에서 최신 모델을 다시 불러옵니다.

Avatar Live에서 쓸 아바타 파일(`.vavatar`)은 아바타의 Unity 프로젝트에 **Curious Bobby - Avatar Exporter**를 설치해서 만듭니다.

## 준비

- Unity **2022.3.22f1** 아바타 프로젝트
- VRChat에 정상적으로 업로드되는 아바타
- NDMF · Modular Avatar · VRCFury 등을 쓴 아바타도 그대로 내보낼 수 있습니다.

## 설치

**VCC / ALCOM**에 저장소를 추가한 뒤, 아바타 프로젝트에 **Curious Bobby - Avatar Exporter**를 추가합니다.

```text
https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json
```

`.unitypackage`로 받았다면 Unity에서 **Assets → Import Package → Custom Package…** 로 가져오면 됩니다.

## 내보내기

1. Unity 메뉴에서 **Curious Bobby → Avatar Exporter**를 엽니다.
2. **아바타** 칸에 내보낼 아바타를 넣습니다.
3. **.vavatar 내보내기**를 누릅니다.
4. 완료되면 **파일 보기**로 만들어진 파일을 확인합니다.

| 항목 | 하는 일 |
|---|---|
| **Avatar Live에 표시할 이름** | Avatar Live에서 보일 이름 |
| **표정 클립 (선택)** | 추가 표정 애니메이션을 넣어 [자동 표정](11-pro-features.md#자동-표정)에서 사용 |
| **저장 폴더** | 파일을 저장할 위치 |

> 💡 내보내기가 잘 되지 않으면, 먼저 아바타가 VRChat에 정상적으로 업로드되는지 확인해 주세요.

## 아바타를 고쳤을 때

Unity에서 수정한 뒤 다시 내보내기만 하면 됩니다. 조명, 카메라, 얼굴 조정, 옷 상태 같은 아바타별 설정은 그대로 이어집니다.

- 원본 아바타와 씬은 바뀌지 않습니다.
- 만든 파일은 내 PC에만 저장되고, 어디에도 업로드되지 않습니다.
