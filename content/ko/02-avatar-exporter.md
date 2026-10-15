# 아바타 내보내기

Unity 프로젝트에 있는 아바타를 Avatar Live에서 여는 `.vavatar` 파일로 만듭니다. 이미 `.vavatar`나 `.vrm` 파일이 있다면 [아바타 열기](03-launcher-and-library.md)로 넘어가세요.

## Exporter 설치

1. VCC 또는 ALCOM에 아래 저장소를 추가합니다.
2. 아바타 프로젝트에 Curious Bobby - Avatar Exporter를 추가합니다.
3. Unity에서 해당 프로젝트를 엽니다.

```text
https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json
```

`.unitypackage`로 받았다면 Unity의 Assets → Import Package → Custom Package…에서 가져옵니다.

## 아바타 파일 만들기

1. Unity 상단 Curious Bobby → Avatar Exporter를 엽니다.
2. 아바타 칸에 Hierarchy의 아바타를 끌어 넣습니다.
3. 표시 이름과 저장 폴더를 정합니다.
4. .vavatar 내보내기를 누릅니다.
5. 완료되면 파일 보기를 눌러 결과 파일을 확인합니다.
6. Avatar Live의 아바타 열기에서 그 파일을 불러옵니다.

| 항목 | 바꾸면 어떻게 되나요? |
|---|---|
| 아바타 | 내보낼 캐릭터를 선택합니다. |
| 표시할 이름 | Avatar Live의 목록에 보이는 이름이 됩니다. |
| 표정 클립 | 선택한 표정 애니메이션을 함께 넣습니다. 없어도 내보낼 수 있습니다. |
| 저장 폴더 | 완성된 `.vavatar` 파일을 둘 폴더입니다. |
| .vavatar 내보내기 | 선택한 아바타로 파일을 만듭니다. |
| 파일 보기 | 완성된 파일이 있는 폴더를 엽니다. |

## 아바타를 수정했을 때

Unity에서 의상이나 머리카락 등을 고친 뒤 같은 아바타를 다시 내보냅니다. Avatar Live에서 새 파일을 불러오면 변경한 외형이 반영됩니다.

## 내보내기가 안 될 때

- Unity에서 아바타 자체의 오류가 없는지 확인합니다.
- 사용 중인 제작 도구와 Exporter를 확인하고 다시 내보냅니다.
- 파일은 생겼지만 일부가 분홍색이거나 사라졌다면 원본 프로젝트의 재질·셰이더와 해당 파츠의 켜짐 상태를 확인합니다.

아바타·의상·소품의 방송 및 공유 허용 범위는 각 제작자의 약관을 따릅니다. [콘텐츠 이용 조건](13-license.md#아바타와-소품)을 확인하세요.
