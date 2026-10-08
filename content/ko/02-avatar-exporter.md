# 2. 아바타 내보내기 (Avatar Exporter)

Avatar Live는 아바타를 **`.vavatar`** 파일로 엽니다. 이 파일은 내 VRChat 아바타의 Unity 프로젝트에 **Curious Bobby - Avatar Exporter**를 설치해서 만듭니다.

- 원본 아바타·씬·머티리얼은 바뀌지 않습니다.
- Exporter는 아무것도 인터넷에 올리지 않습니다.
- 만든 `.vavatar` 파일은 사용자 소유입니다. 단, 그 안의 아바타·의상 권리는 각 제작자에게 있습니다.

## 요구 사항

| 항목 | 내용 |
|---|---|
| Unity | **2022.3.22f1** |
| 아바타 | **VRChat에 정상적으로 업로드되는 아바타 프로젝트** |
| 제작 도구 | NDMF · Modular Avatar · VRCFury 등을 쓴 아바타도 내보낼 수 있습니다 (이 도구들은 Exporter에 포함되지 않으며, 프로젝트에 설치된 것을 사용) |

## 설치

### VCC / ALCOM (권장)

1. VCC 또는 ALCOM에 저장소를 추가합니다.
   - `vcc://vpm/addRepo?url=https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json`
   - 또는 주소 직접 추가: `https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json`
2. 아바타 프로젝트에 **Curious Bobby - Avatar Exporter**를 추가합니다.

### .unitypackage

Unity에서 **Assets → Import Package → Custom Package…** 로 가져옵니다.

설치하면 Unity 상단 메뉴에 **Curious Bobby**가 생깁니다.

## 내보내기

1. **Curious Bobby → Avatar Exporter**를 엽니다.
2. **아바타** 칸에 내보낼 아바타를 넣습니다.
3. **Avatar Live에 표시할 이름**을 확인합니다.
4. 필요하면 **저장 폴더**를 바꿉니다.
5. **.vavatar 내보내기**를 누릅니다.
6. **결과**에 파일 이름이 나오면 완료입니다. **파일 보기**로 탐색기에서 엽니다.

| 항목 | 하는 일 |
|---|---|
| **아바타** | 내보낼 아바타 |
| **열린 장면의 아바타** | 씬에 아바타가 여럿일 때 고르기 |
| **Avatar Live에 표시할 이름** | Avatar Live에서 보일 이름 |
| **표정 클립 (선택)** | 추가 표정 애니메이션을 넣어 [자동 표정](11-pro-features.md#자동-표정)에서 쓰기 |
| **저장 폴더** | `.vavatar`를 저장할 곳 |
| **.vavatar 내보내기** | 파일 만들기 |

> 내보내기가 실패하면, 아바타가 VRChat에 정상 업로드되는지 먼저 확인해 주세요.

## Avatar Live에서 열기

- 시작 화면 **아바타 열기…**, 또는 창에 파일 **끌어다 놓기**
- **아바타 폴더**(기본 `문서\Avatar Live\Avatars`)에 넣으면 시작 화면에 자동으로 표시
- 실행 중 왼쪽 위 아바타 이름 → **아바타 파일 추가…**

## 아바타를 수정했을 때

Unity에서 고친 뒤 **다시 내보내기**만 하면 됩니다. 아바타별 설정(조명·카메라·얼굴 조정·옷 상태 등)은 그대로 유지됩니다.

- "더 새로운 익스포터로 만든 파일입니다" → Avatar Live를 업데이트하세요.
- 오래된 형식이라고 나오면 → 최신 Exporter로 다시 내보내세요.
- 휴머노이드가 아닌 아바타는 메뉴·표정은 쓸 수 있지만 몸 트래킹은 쓸 수 없습니다.
