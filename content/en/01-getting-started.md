# Getting Started

Start by loading an avatar, connecting your tracking devices, then setting up your broadcast video output.

## Installing and Running

1. Receive the Avatar Live ZIP file from your BOOTH purchase history.
2. Extract all files to the desired folder.
3. Run `AvatarLive.exe` inside the folder.
4. On the product activation screen, enter the information provided when you made the purchase and press Activate.

Windows 10 / 11 64-bit and a graphics card that supports DirectX 11 are required. Prepare a webcam to track face and hand movements, and a microphone to move the mouth with your voice.

## 1. Open Avatar

![Start screen for choosing the device to start with your avatar](img/guide-launcher.png)

1. Click 'Open Avatar' or drag the file into the window.
2. Select the character to use from the avatar list.
3. Click **Start** in Avatar Live. When the scene list appears, select the scene you want to use.

| File type | How to use it |
|---|---|
| `.vavatar` | Open the file directly. |
| `.vrm` | Loads as is. Supports VRM 0.x and 1.0. |
| Unity Avatar Project | After creating a `.vavatar` with [Avatar Exporter](02-avatar-exporter.md), import it. |

## 2. Connecting My Movements

![Setting up devices for webcam and microphone](img/guide-devices.png)

1. Press the device on the left.
2. Select the camera you want to use from the webcam list and turn on the switch to the right of the title.
3. Face the screen straight on and press front calibration.
4. To move your mouth with your voice, also select a microphone and turn on the switch.

If you are using an iPhone or an external tracker, check [Devices](06-devices.md) for connection methods.

## 3. Setting Background and Composition

![Main screen showing menu and avatar together](img/guide-main.png)

- Outfit & expression: Choose from the left menu.
- Face & hand movements: Adjust in Motion.
- Background & lighting: Choose in Studio.
- Composition: Select face, upper body, or full body from the camera toolbar at the bottom.

Press F1 to hide the menu and view only the avatar. Press again to bring the menu back.

## 4. Connecting to Broadcasting Software

| Purpose | Where to Open |
|---|---|
| Insert avatar into OBS on this PC | [Spout2 Connection](09-output.md#spout2) |
| Send video to OBS on another PC | [NDI Connection](09-output.md#ndi) |
| Use as camera on Discord or Zoom | [Virtual Camera](09-output.md#virtual-camera) |
| Share games and avatars together | [Screen Sharing](09-output.md#screen-share) |
| Broadcast together with a friend's avatar | [Remote Collaboration](09-session.md) |

Before starting a broadcast, check the actual video on OBS or the side receiving the shared screen. The layout of your work screen and the broadcast camera may differ.

## Editions and Exit

Basic is for personal/private use, Pro is for broadcasting, video sharing, and commercial use. Check the [features by edition](13-license.md) for the functions you need.

Close the program with the power button at the bottom left. If the window's X button is set to hide to the tray, the broadcast will continue. You can change the X button behavior in Settings → Window.
