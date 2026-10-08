# 2. アバターの書き出し（Avatar Exporter）

Avatar Live はアバターを **`.vavatar`** ファイルとして開きます。このファイルは、自分の VRChat アバターの Unity プロジェクトに **Curious Bobby - Avatar Exporter** をインストールして作ります。

- 元のアバター・シーン・マテリアルは変更されません。
- Exporter はインターネットに何もアップロードしません。
- 作成した `.vavatar` ファイルはユーザーのものです。ただし、その中のアバター・衣装の権利は各制作者にあります。

## 必要環境

| 項目 | 内容 |
|---|---|
| Unity | **2022.3** |
| アバター | **VRChat に正常にアップロードできるアバタープロジェクト** |
| 制作ツール | NDMF · Modular Avatar · VRCFury などを使ったアバターも書き出せます（これらのツールは Exporter に含まれず、プロジェクトにインストールされているものを使用します） |

## インストール

### VCC / ALCOM（推奨）

1. VCC または ALCOM にリポジトリを追加します。
   - `vcc://vpm/addRepo?url=https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json`
   - またはアドレスを直接追加：`https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json`
2. アバタープロジェクトに **Curious Bobby - Avatar Exporter** を追加します。

### .unitypackage

Unity で **Assets → Import Package → Custom Package…** からインポートします。

インストールすると、Unity の上部メニューに **Curious Bobby** が追加されます。

## 書き出し

1. **Curious Bobby → Avatar Exporter** を開きます。
2. **アバター** 欄に書き出すアバターを入れます。
3. **Avatar Live での表示名** を確認します。
4. 必要に応じて **保存フォルダー** を変更します。
5. **.vavatar を書き出す** を押します。
6. **結果** にファイル名が表示されれば完了です。**ファイルを表示** でエクスプローラーで開けます。

| 項目 | 内容 |
|---|---|
| **アバター** | 書き出すアバター |
| **開いているシーンのアバター** | シーンにアバターが複数あるときに選ぶ |
| **Avatar Live での表示名** | Avatar Live に表示される名前 |
| **表情クリップ（任意）** | 追加の表情アニメーションを入れて[自動表情](11-pro-features.md#自動表情)で使う |
| **保存フォルダー** | `.vavatar` の保存先 |
| **.vavatar を書き出す** | ファイルを作成 |

> 書き出しに失敗する場合は、まずアバターが VRChat に正常にアップロードできるか確認してください。

## Avatar Live で開く

- スタート画面の **アバターを開く…**、またはウィンドウにファイルを **ドラッグ＆ドロップ**
- **アバターフォルダー**（標準は `ドキュメント\Avatar Live\Avatars`）に入れると、スタート画面に自動で表示
- 起動中に左上のアバター名 → **アバターファイルを追加…**

## アバターを修正したとき

Unity で修正したあと、**書き出し直す** だけです。アバターごとの設定（ライティング・カメラ・顔の調整・衣装の状態など）はそのまま保持されます。

- 「新しいエクスポーターで作られています」→ Avatar Live をアップデートしてください。
- 古い形式と表示された場合 → 最新の Exporter で書き出し直してください。
- ヒューマノイドではないアバターは、メニュー・表情は使えますが、体のトラッキングは使えません。
