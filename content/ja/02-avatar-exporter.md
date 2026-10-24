# アバターをエクスポート

UnityプロジェクトにあるアバターをAvatar Liveで開くための`.vavatar`ファイルにします。すでに`.vavatar`や`.vrm`ファイルがある場合は、[アバターを開く](03-launcher-and-library.md)に進んでください。

## Exporter のインストール

1. 下のボタンを押して、VCC または ALCOM にリポジトリを追加します。開いた画面で追加を確定します。
2. アバタープロジェクトに Curious Bobby - Avatar Exporter を追加します。
3. Unityで該当のプロジェクトを開きます。

<p><a class="btn btn-primary" href="vcc://vpm/addRepo?url=https%3A%2F%2Fraw.githubusercontent.com%2Fzzubi-works%2Favatar-exporter%2Fmain%2Findex.json">VCC・ALCOM に追加</a></p>

ボタンで開かない場合は、下のアドレスをコピーして Settings → Packages → Add Repository に貼り付けます。

```text
https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json
```

`.unitypackage`で受け取った場合は、UnityのAssets → Import Package → Custom Package…から取り込みます。

## アバターファイルを作成する

1. Unity 上部の Curious Bobby → Avatar Exporter を開きます。
2. アバター欄にHierarchyのアバターをドラッグします。
3. 表示名と保存フォルダを決めます。
4. .vavatar をエクスポートを押します。
5. 完了したら、ファイルを表示して結果ファイルを確認します。
6. Avatar Liveのアバターを開くでそのファイルを読み込みます。

| 項目 | 変えるとどうなりますか？ |
|---|---|
| アバター | エクスポートするキャラクターを選択します。 |
| 表示する名前 | Avatar Live のリストに表示される名前になります。 |
| 表情クリップ | 選択した表情アニメーションを一緒に入れます。なくても書き出すことができます。 |
| 保存フォルダー | 完成した `.vavatar` ファイルを置くフォルダーです。 |
| .vavatar をエクスポート | 選択したアバターでファイルを作成します。 |
| ファイルを見る | 完成したファイルがあるフォルダを開きます。 |

## アバターを修正したとき

Unityで衣装や髪などを修正した後、同じアバターを再度エクスポートします。Avatar Liveで新しいファイルを読み込むと、変更した外見が反映されます。

## エクスポートできないとき

- Unityでアバター自体にエラーがないか確認します。
- 使用中の制作ツールとエクスポーターを確認して、再度エクスポートします。
- ファイルは作成されたが、一部がピンク色になったり消えてしまった場合は、元のプロジェクトのマテリアル・シェーダーと該当パーツのオン状態を確認します。

アバター・衣装・小道具の放送および共有の許可範囲は、各制作者の利用規約に従います。[コンテンツ利用条件](13-license.md#アバターと小道具)を確認してください。
