# 9. Output

Send the avatar image to your streaming software or call apps.

| Destination | Method |
|---|---|
| OBS (transparent background) | Spout2 |
| Camera in Discord · Zoom · Teams | Virtual camera |
| Streaming a game on Discord | Screen share |
| Photos | Save PNG |

## Stream

<div class="shot" markdown="1">

![Output › Stream](img/stream.png)

- **Output image** — Choose the size of the image you send.
- **Spout2** — Turn it on and add a **Spout2 Capture** source in OBS, and the avatar appears. Set the background to **Transparent** to send it without a background.
- **Virtual camera** — The first time only, click **Install the virtual camera…**, then choose **Avatar Live Camera** as the camera in the other app.
- **Photo** — **Save PNG** saves the view. Choose from **No UI · With UI · Clear background**, and turn on **Eyes on the camera** to have the avatar look at the camera. Available in both Basic and Pro.

</div>

> 💡 Discord looks for cameras only when it starts. If the camera isn't in the list, please quit Discord completely and open it again.

## Discord screen share

<div class="shot" markdown="1">

![Output › Screen share](img/share.png)

1. Under **Share target**, choose a game or a display.
2. Turn on **Screen share**.
3. In Discord, choose **Screen Share → Applications → Avatar Live Share Output** and turn on sound.

</div>

- Your friends see the game and the avatar together, while you see only the game.
- Drag the avatar in the preview to set its position and size.
- Turn on **Game audio** to send only the game's sound to your friends.

### No game sound in Discord — virtual audio driver

> ⚠️ **Discord screen-share sound needs an available virtual audio playback device.** Without one, video may still be shared, but game audio will not be transmitted. If a warning appears under **Output › Screen share**, click **Install virtual audio driver**. Windows will request administrator permission, and you must restart your PC after installation.

Avatar Live's install option uses **VB-CABLE Virtual Audio Device** by **VB-Audio Software**. If another compatible virtual audio device is already available, you do not need to install it. We recommend **Automatic** for the shared audio device.

- **Developer · official download:** [VB-Audio Software — VB-CABLE (www.vb-cable.com)](https://vb-cable.com/)
- **Donations · licensing:** [VB-Audio's official Donationware and licensing information](https://vb-audio.com/Services/licensing.htm)

**VB-CABLE is third-party Donationware made by VB-Audio Software, not by Avatar Live.** All contributions are welcome. If you find it useful, please support its developer through a donation or license purchase on the official site. **Professional, business, or institutional use requires a separate VB-CABLE license.**

> 💡 If the game shows up black, try switching the game to **borderless window** or **windowed mode**. We recommend running Avatar Live without administrator rights.

> 💡 Screen sharing may not work with games that run only in exclusive full screen. In that case, please stream through OBS.

## External output (VMC)

Turn on **VMC output** to send the avatar's movement to another app. This is an experimental feature. To **receive** movement over VMC, please see [Devices › Receiving over VMC](06-devices.md#receiving-over-vmc-full-body-trackers--gloves--other-apps).
