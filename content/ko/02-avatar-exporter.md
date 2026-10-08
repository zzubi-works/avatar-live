# 2. 아바타 내보내기

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
