# 2. 导出角色（Avatar Exporter）

Avatar Live 以 **`.vavatar`** 文件打开角色。该文件通过在你的 VRChat 角色 Unity 项目中安装 **Curious Bobby - Avatar Exporter** 来制作。

- 原始角色、场景和材质不会被更改。
- 导出器不会向互联网上传任何内容。
- 制作出的 `.vavatar` 文件归用户所有。但其中角色和服装的权利归各自的制作者所有。

## 要求

| 项目 | 内容 |
|---|---|
| Unity | **2022.3.22f1** |
| 角色 | **能够正常上传到 VRChat 的角色项目** |
| 制作工具 | 使用 NDMF、Modular Avatar、VRCFury 等的角色也可以导出（这些工具不包含在导出器中，使用的是项目中已安装的工具） |

## 安装

### VCC / ALCOM（推荐）

1. 在 VCC 或 ALCOM 中添加仓库。
   - `vcc://vpm/addRepo?url=https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json`
   - 或直接添加地址：`https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json`
2. 在角色项目中添加 **Curious Bobby - Avatar Exporter**。

### .unitypackage

在 Unity 中通过 **Assets → Import Package → Custom Package…** 导入。

安装后，Unity 顶部菜单中会出现 **Curious Bobby**。

## 导出

1. 打开 **Curious Bobby → Avatar Exporter**。
2. 在 **角色** 栏中放入要导出的角色。
3. 确认 **在 Avatar Live 中显示的名称**。
4. 如有需要，更改 **输出文件夹**。
5. 点击 **导出 .vavatar**。
6. **结果** 中显示文件名即完成。点击 **显示文件** 可在资源管理器中打开。

| 项目 | 作用 |
|---|---|
| **角色** | 要导出的角色 |
| **已打开场景中的角色** | 场景中有多个角色时进行选择 |
| **在 Avatar Live 中显示的名称** | 在 Avatar Live 中显示的名称 |
| **表情剪辑（可选）** | 加入额外的表情动画，用于 [自动表情](11-pro-features.md#自动表情) |
| **输出文件夹** | `.vavatar` 的保存位置 |
| **导出 .vavatar** | 生成文件 |

> 如果导出失败，请先确认角色能否正常上传到 VRChat。

## 在 Avatar Live 中打开

- 在开始界面点击 **打开角色…**，或将文件 **拖放** 到窗口中
- 放入 **角色文件夹**（默认为 `文档\Avatar Live\Avatars`）后会自动显示在开始界面
- 运行中点击左上角的角色名称 → **添加角色文件…**

## 修改角色后

在 Unity 中修改后，只需 **重新导出** 即可。每个角色的设置（灯光、相机、面部调整、服装状态等）会保留。

- “它由更新版本的导出器制作” → 请更新 Avatar Live。
- 提示格式过旧时 → 请用最新的导出器重新导出。
- 非人形（Humanoid）角色可以使用菜单和表情，但无法使用身体追踪。
