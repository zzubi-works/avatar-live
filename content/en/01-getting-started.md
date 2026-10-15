# 1. Getting started

## v2.0.0 quick start: from first launch to your first stream

1. **Load an avatar:** Open a **.vavatar** created with Exporter 1.0.6 or a supported **VRM 0.x/1.0** model. Some custom VRM 0.x shaders cannot load.
2. **Connect input:** Pick webcam, iPhone, mic, VMC or SteamVR per body part in [Devices](06-devices.md). Your face, arms, fingers and body can use different sources.
3. **Calibrate:** Face forward. With iPhone input, initial correction starts roughly **three seconds** after the first valid tracked face frame.
4. **Customize motion:** Select expressions and clothing in [Avatar Menu](05-avatar-menu.md), then adjust smoothing, lip sync and AFK behavior under [Motion](07-motion.md).
5. **Prepare the picture:** Select a background and lights in [Studio](08-scene.md); **Pro** also offers multiple avatars and saved broadcast cameras.
6. **Connect OBS:** Install the **OBS Spout2 receiver plugin** for same-PC output, or **DistroAV/NDI** for network output. **NDI is available in Basic**, but the third-party OBS plugin is required. Follow the [Output tutorial](09-output.md).
7. **Check the actual broadcast:** Your editing scene view can differ from the on-air studio camera. Verify the OBS program monitor before going live.

**Basic** is licensed for personal use; public/commercial broadcasts require **Pro**, regardless of which technically available output method is selected. See [Licensing](13-license.md).

## What you need

| Item | Requirement |
|---|---|
| Operating system | Windows 10 / 11 (64-bit) |
| Graphics | GPU with DirectX 11 support |
| Webcam | A regular color webcam |
| Microphone | For lip sync (optional) |
| Internet | Needed for activation and license checks |
| Avatar | The Unity project of your VRChat avatar (Unity 2022.3.22f1) |

## Editions

| | Basic | Pro |
|---|---|---|
| Scope of use | Personal use (including private Discord sharing with friends) | Streaming · publishing videos · commercial use |
| Output | Up to 1080p · watermark | Up to 4K · no watermark |
| Posing · Objects · More screen share sources | — | ✅ |

If you'll be showing it to other people, such as on a stream or in a published video, please choose **Pro**. You'll find the details in [Chapter 13](13-license.md).

## Installation

1. Download the ZIP file from your BOOTH purchase history.
2. Extract it to any folder you like.
3. Run `AvatarLive.exe`.

> 💡 If a "Windows protected your PC" window appears, click **More info → Run anyway**.

> 💡 We recommend leaving the files in the installation folder as they are. If the files change, Avatar Live may not start; in that case, simply reinstall from the original. Your avatars and settings are kept.

## Activation

The first time you run it, the **Product activation** screen appears. Enter the information you received with your purchase and click **Activate**, and you're all set.

A license is for one person on one device. You can move it to another PC yourself once. After that, we're happy to help through an inquiry when it can't be avoided, but it may not always be easy. **Please choose the PC you activate first carefully.**

## Getting to your first stream

<div class="steps" markdown="1">

1. **Export your avatar** — Create a `.vavatar` file in Unity. → [Chapter 2](02-avatar-exporter.md)
2. **Open your avatar** — Open the file on the start screen and click **▶ Start Avatar Live**. → [Chapter 3](03-launcher-and-library.md)
3. **Turn on the webcam and mic** — Turn on the switches on the **Devices** page. → [Chapter 6](06-devices.md)
4. **Fit your face** — Click **Motion › Automatic face setup** and follow the guide. → [Chapter 7](07-motion.md)
5. **Choose a background and lighting** — Pick them on the **Studio** page. → [Chapter 8](08-scene.md)
6. **Send it out** — On the **Output** page, turn on Spout2, the virtual camera or screen share. → [Chapter 9](09-output.md)

</div>

Press **F1** to hide the menus so that only the avatar is shown.

## Important locations in 1.1.5

- Use the top magnifying glass to search for AFK, Mirror, Spout2 and other settings.
- Configure the default pose and tracking-loss idle pose separately. AFK timing is now under Motion › Body, not Settings.
- Click a section heading to fold it and drag headings to reorder cards. Each pose has independent facial, head, arms, fingers and body tracking switches.

## Quitting

By default, clicking the window's **X** quits Avatar Live. You can select **Minimize to tray** under **Settings › Window**. While streaming, closing the window may keep output running in the tray. The **power** button at the lower-left quits the program completely.
