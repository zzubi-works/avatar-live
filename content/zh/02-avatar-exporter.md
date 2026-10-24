# 导出角色

将 Unity 项目中的角色制作成可以在 Avatar Live 中打开的 `.vavatar` 文件。如果已经有 `.vavatar` 或 `.vrm` 文件，请前往 [打开角色](03-launcher-and-library.md)。

## 安装 Exporter

1. 点击下方按钮，将存储库添加到 VCC 或 ALCOM。在打开的窗口中确认添加。
2. 在角色项目中添加 Curious Bobby - Avatar Exporter。
3. 在 Unity 中打开该项目。

<p><a class="btn btn-primary" href="vcc://vpm/addRepo?url=https%3A%2F%2Fraw.githubusercontent.com%2Fzzubi-works%2Favatar-exporter%2Fmain%2Findex.json">添加到 VCC · ALCOM</a></p>

如果按钮无法打开，请复制下方地址，粘贴到 Settings → Packages → Add Repository。

```text
https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json
```

如果是以 `.unitypackage` 接收的话，可以在 Unity 的 Assets → Import Package → Custom Package… 中导入。

## 创建角色文件

1. 在 Unity 顶部打开 Curious Bobby → Avatar Exporter。
2. 将 Hierarchy 的角色拖入角色栏。
3. 设置显示名称和保存文件夹。
4. 点击导出 .vavatar。
5. 完成后，点击查看文件以确认结果文件。
6. 在 Avatar Live 的打开角色中加载该文件。

| 项目 | 如果更改会怎么样？ |
|---|---|
| 角色 | 请选择要导出的角色。 |
| 显示名称 | 将显示在 Avatar Live 列表中的名称。 |
| 表情剪辑 | 一起加入所选的表情动画。即使没有也可以导出。 |
| 保存文件夹 | 放置已完成的 `.vavatar` 文件的文件夹。 |
| .vavatar 导出 | 使用所选角色创建文件。 |
| 查看文件 | 打开包含已完成文件的文件夹。 |

## 修改角色时

在Unity中修改服装或头发等之后，再次导出相同的角色。在Avatar Live中加载新文件后，修改过的外观将会被反映出来。

## 导出失败时

- 在 Unity 中检查角色本身是否没有错误。
- 请确认正在使用的制作工具和导出器，然后重新导出。
- 文件已经生成，但如果部分是粉色的或消失了，请检查原始项目的材质、着色器以及该部件的开启状态。

角色、服装、道具的播放及分享许可范围遵循各制作者的条款。请确认 [内容使用条件](13-license.md#角色与道具)。
