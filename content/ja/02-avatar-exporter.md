# 2. アバターの書き出し

Avatar Live で使うアバターファイル（`.vavatar`）は、アバターの Unity プロジェクトに **Curious Bobby - Avatar Exporter** をインストールして作ります。

## 準備

- Unity **2022.3.22f1** のアバタープロジェクト
- VRChat に正常にアップロードできるアバター
- NDMF・Modular Avatar・VRCFury などを使ったアバターも、そのまま書き出せます。

## インストール

**VCC / ALCOM** にリポジトリを追加してから、アバタープロジェクトに **Curious Bobby - Avatar Exporter** を追加します。

```text
https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json
```

`.unitypackage` でダウンロードした場合は、Unity の **Assets → Import Package → Custom Package…** からインポートしてください。

## 書き出し

1. Unity のメニューから **Curious Bobby → Avatar Exporter** を開きます。
2. **アバター** 欄に、書き出すアバターを入れます。
3. **.vavatar を書き出す** を押します。
4. 完了したら、**ファイルを表示** で作成されたファイルを確認します。

| 項目 | 内容 |
|---|---|
| **Avatar Live での表示名** | Avatar Live に表示される名前 |
| **表情クリップ（任意）** | 追加の表情アニメーションを入れて、[自動表情](11-pro-features.md#自動表情)で使用 |
| **保存フォルダー** | ファイルの保存先 |

> 💡 書き出しがうまくいかない場合は、まずアバターが VRChat に正常にアップロードできるか確認してください。

## アバターを改変したとき

Unity で改変したあと、書き出し直すだけで大丈夫です。ライティング、カメラ、顔の調整、衣装の状態など、アバターごとの設定はそのまま引き継がれます。

- 元のアバターとシーンは変更されません。
- 作成したファイルは自分の PC にだけ保存され、どこにもアップロードされません。
