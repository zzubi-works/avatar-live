# 12. Troubleshooting

> 💡 If something isn't solved, please let us know with **Settings › Diagnostics › Send an error report**.

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
| ✅ Face | VRCFaceTracking, ARKit (Perfect Sync), MMD eye morphs |
| 🧪 Experimental features | Ultraleap, OSC · VMC, camera detection of the tongue and cheeks |
| ⚠️ Not supported | Avatar sound effects, AudioLink, mirror detection, VRM files, Live2D, macOS · Linux |

We expect the experimental features to work properly, but we haven't yet been able to test them with every device and app in the developer's environment.

## Planned support

- Loading VRM models (.vrm, VRM 0.x / 1.0) and playing .vrma animations
- Stronger Perfect Sync: mapping that links shape keys directly, face calibration for each webcam · iPhone, and a tool to check the 52 expressions one by one
- More phone face apps: VTube Studio (iPhone), MeowFace (Android)
- Webcam upper body: twisting · tilting the upper body from your shoulder movement
- Better full-body tracking app support (VMC): receiving a face app and a body app at the same time, reflecting sitting · leaning — TDPT, XR Animator and more
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
