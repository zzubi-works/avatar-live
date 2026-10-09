# 12. Troubleshooting

> 💡 For bugs or problems that aren't solved, please let us know with **Settings › Diagnostics › Send an error report**, and for features or improvements you need, with **Settings › About › Send a suggestion**.

## Start-up · Installation

| Symptom | Solution |
|---|---|
| "Windows protected your PC" window | **More info → Run anyway** |
| "Avatar Live's files have been changed" | Please reinstall from the original you downloaded from BOOTH. Your avatars and settings are kept. |
| It doesn't start smoothly | Launch while holding **Shift** for a safe start |

## Avatar

| Symptom | Solution |
|---|---|
| Some parts look pink | Check that the avatar uploads to VRChat normally, then export it again |
| The avatar isn't visible | Double-click an empty spot in the view |
| The pose is stuck or the hair is tangled | **⟲** at the top |
| Avatar sound effects aren't heard | Avatar sound effects are not played. |

## Webcam · Face

| Symptom | Solution |
|---|---|
| The camera doesn't turn on | Check whether another app is using the camera |
| Expressions come out too small or too large | Run **Automatic face setup** again, or use **Face adjustment** |
| The avatar looks to the side | **Recenter** |
| Winks don't work | Set the blink mode to **Independent** |
| The PC feels slow | Set the tracking quality to **Balanced** or **Eco** |
| Hands · fingers jitter | Raise **Devices › Tracking sources › Hand steadiness** |
| The avatar doesn't move | In **Devices › Tracking sources**, check that no part's source is set to a device you aren't using (such as VMC) |
| The pose received over VMC is off | **T-pose** or **Align** in **VMC settings** |

## Microphone

| Symptom | Solution |
|---|---|
| "No signal" | Allow desktop apps in Windows Settings › Privacy › Microphone |
| Noise moves the mouth | **Detect background noise** |
| The mouth moves too little | **Voice calibration** |

## Output · Screen share

| Symptom | Solution |
|---|---|
| No Spout2 source in OBS | Install the Spout2 plugin in OBS |
| The background looks black in OBS | Set the background to **Transparent** and choose **Composite with alpha** in OBS |
| Not in the Discord list | Turn on **Screen share**, then check the **Applications** tab |
| The game shows up black | Switch the game to windowed mode |
| "Avatar Live Basic" text | This is the Basic watermark. It isn't shown in Pro. |

## Supported features

| | Details |
|---|---|
| ✅ VRChat avatars | Expressions menu, animators, PhysBones, Contacts, Constraints, Eye Look, LipSync |
| ✅ Creation tools | Avatars that use NDMF · Modular Avatar · VRCFury |
| ✅ Shaders | Poiyomi, lilToon and others |
| ✅ Face | Follows the avatar's setup: VRCFaceTracking, 52 ARKit shape keys (Perfect Sync), MMD eye morphs |
| ✅ Tracking | Webcam (face · arms · hands · fingers), iPhone (iFacialMocap · FaceMotion3D), VMC (per part: arms · hands · fingers · body · head · eyes) |
| 🧪 Experimental features | Ultraleap, OSC, VMC output, camera detection of the tongue and cheeks |
| ⚠️ Not supported | Avatar sound effects, AudioLink, mirror detection, VRM files, Live2D, macOS · Linux |

We've confirmed webcam (including full body and finger joints), iPhone and VMC input with real equipment. We expect the experimental features to work properly, but we haven't yet been able to test them with every device and app in the developer's environment, so they're marked **experimental** in the app. If you try them and something goes wrong, please let us know with **Send an error report**.

## Planned support

- Loading VRM models (.vrm, VRM 0.x / 1.0) and playing .vrma animations
- Stronger Perfect Sync: mapping that links shape keys directly, face calibration for each webcam · iPhone, and a tool to check the 52 expressions one by one
- More phone face apps: VTube Studio (iPhone), MeowFace (Android)
- Conveniences: automatic refresh when you export the avatar again, lower FPS when there's nothing to do

※ Planned features and their timing may change.

## Frequently asked questions

**Do I need a VRChat account?**
No, you don't. Avatar Live does not communicate with VRChat.

**Can I use it for streaming?**
For streaming, publishing videos and commercial use, please use **Pro**. Private Discord sharing with friends is fine with Basic, too.

**Is my keyboard input recorded?**
No, it isn't. Desk hand motion does not save or send the characters you type.

**Can I give my avatar file to other people?**
Please follow the terms of use of the avatar and outfit creators.
