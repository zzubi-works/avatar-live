# 2. 导出角色

## v2.0.0：Exporter 1.0.6 与 VRM 直接导入

**Unity 角色（.vavatar）**与 **VRM 模型（.vrm）**的导入方法不同。VRChat 的 Unity 角色需要使用 **Curious Bobby - Avatar Exporter 1.0.6**导出；支持的 **VRM 0.x / 1.0**则可在 Avatar Live 中直接导入，无须 Exporter。

- **Unity 项目**：从 Unity **2022.3.22f1** 的原项目和兼容 VRChat SDK 开始，选中角色并执行**导出 .vavatar**。Exporter 1.0.6 针对 VRChat SDK 3.10.5 改进 PhysBone、碰撞体，并修复部分服装合并导致发丝和装饰骨骼被关闭的问题。
- **显示名称、表情片段、保存位置**：分别决定程序里显示的名字、附带的表情动画和 Windows 中实际生成文件的位置。导出成功并不代表已经加入程序角色库，仍需打开该文件。
- **修改后重新导出**：服装、骨架、材质改变后必须重新导出，并在直播前检查原来保存的动作、镜头与表情是否仍符合新的模型。
- **VRM 导入**：部分 VRM 0.x 模型含不受支持的着色器，可能无法加载；简单改扩展名不能转换着色器。
- **资源授权**：拥有或制作文件，不代表可以把它分发给别人。使用[远程会话](09-output.md)的数据分享前，应确认角色、服装、贴图和道具的原作者许可。

如出现粉色材质或部分模型消失，请检查 Unity 项目的材质/着色器、PhysBone 和碰撞体，再导出并重新加载最新模型。

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
