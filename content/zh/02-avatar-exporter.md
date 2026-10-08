# 2. 导出角色

Avatar Live 使用的角色文件（`.vavatar`），需要在角色的 Unity 项目中安装 **Curious Bobby - Avatar Exporter** 来制作。

## 准备

- Unity **2022.3.22f1** 的角色项目
- 能够正常上传到 VRChat 的角色
- 使用 NDMF · Modular Avatar · VRCFury 等工具的角色也可以直接导出。

## 安装

在 **VCC / ALCOM** 中添加仓库后，将 **Curious Bobby - Avatar Exporter** 添加到角色项目中。

```text
https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json
```

如果下载的是 `.unitypackage`，在 Unity 中通过 **Assets → Import Package → Custom Package…** 导入即可。

## 导出

1. 在 Unity 菜单中打开 **Curious Bobby → Avatar Exporter**。
2. 在 **角色** 栏中放入要导出的角色。
3. 点击 **导出 .vavatar**。
4. 完成后，点击 **显示文件** 查看生成的文件。

| 项目 | 作用 |
|---|---|
| **在 Avatar Live 中显示的名称** | 在 Avatar Live 中看到的名称 |
| **表情剪辑（可选）** | 加入额外的表情动画，用于 [自动表情](11-pro-features.md#自动表情) |
| **输出文件夹** | 文件的保存位置 |

> 💡 如果导出不顺利，请先确认角色能否正常上传到 VRChat。

## 修改角色后

在 Unity 中修改后，只需重新导出即可。灯光、相机、面部调整、服装状态等每个角色各自的设置会继续保留。

- 原始角色和场景不会被更改。
- 生成的文件只保存在你的电脑中，不会上传到任何地方。
