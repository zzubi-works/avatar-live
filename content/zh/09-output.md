# 9. 输出

将角色画面发送到直播软件或通话应用。

| 发送到 | 方法 |
|---|---|
| OBS（透明背景） | Spout2 |
| Discord · Zoom · Teams 的摄像头 | 虚拟摄像头 |
| Discord 游戏直播 | 屏幕共享 |
| 照片 | 保存 PNG |

## 推流输出

<div class="shot" markdown="1">

![输出 › 推流输出](img/stream.png)

- **输出画面** — 选择输出的画面尺寸。
- **Spout2** — 开启后在 OBS 中添加 **Spout2 Capture** 来源，角色就会出现。将背景设为 **透明**，即可不带背景发送。
- **虚拟摄像头** — 首次使用时点击一次 **安装虚拟摄像头…**，然后在目标应用中选择 **Avatar Live Camera** 作为摄像头。
- **照片** — 用 **保存 PNG** 保存画面。可以在 **无 UI · 含 UI · 仅背景透明** 中选择；开启 **眼睛看镜头** 后，角色会看向镜头。Basic 和 Pro 都可以使用。

</div>

> 💡 Discord 只在启动时查找摄像头。如果列表中没有，请完全退出 Discord 后重新打开。

## Discord 屏幕共享

<div class="shot" markdown="1">

![输出 › 屏幕共享](img/share.png)

1. 在 **共享对象** 中选择游戏或显示器。
2. 开启 **屏幕共享**。
3. 在 Discord 中选择 **屏幕共享 → 应用程序 → Avatar Live Share Output**，并开启声音。

</div>

- 好友看到的是游戏和角色，你自己只看到游戏。
- 在预览中拖动角色，调整位置和大小。
- 开启 **游戏声音** 后，只会把游戏的声音发送给好友。

### Discord 共享没有游戏声音时 — 虚拟音频驱动

> ⚠️ **Discord 屏幕共享要传输游戏声音，需要可用的虚拟音频播放设备。** 没有此设备时，即使画面正常共享，也无法传送声音。如果 **输出 › 屏幕共享** 显示警告，请点击 **安装虚拟音频驱动**。Windows 会请求管理员权限，安装后必须重新启动电脑。

Avatar Live 的安装功能使用 **VB-Audio Software 开发的 VB-CABLE Virtual Audio Device**。如果已有其他可用的虚拟音频设备，则无需重复安装。建议将共享音频设备设置为 **自动**。

- **开发者及官方下载：** [VB-Audio Software — VB-CABLE (www.vb-cable.com)](https://vb-cable.com/)
- **捐助与许可：** [VB-Audio 官方 Donationware 与许可说明](https://vb-audio.com/Services/licensing.htm)

**VB-CABLE 是由 VB-Audio Software 开发的第三方 Donationware（捐助型软件），并非 Avatar Live 自行开发。** 开发者欢迎大家支持；如果觉得实用，请通过官方网站捐助或购买许可。**专业、企业或机构用途必须另外购买相应的 VB-CABLE 许可。**

> 💡 如果游戏显示为黑色，请尝试将游戏切换为 **无边框窗口** 或 **窗口模式**。建议不要以管理员权限运行 Avatar Live。

> 💡 仅支持全屏的游戏可能无法使用屏幕共享。这种情况下，请通过 OBS 进行推流。

## 屏幕共享音频设置

![屏幕共享音频](img/share-audio.png)

在输出 › 屏幕共享 › 音频中查看游戏声音和播放设备。只有缺少可用的虚拟音频设备时才会显示警告及驱动安装按钮。若现有设备正常工作则无须再安装。请阅读Windows管理员权限提示，必要时重启系统。

## 外部输出（VMC）

开启 **VMC 输出** 后，会将角色的动作发送到其他应用。这是实验性功能。通过 VMC **接收** 动作的方法，请参考 [设备 › 通过 VMC 接收](06-devices.md#通过-vmc-接收全身追踪器--手套--其他应用)。
