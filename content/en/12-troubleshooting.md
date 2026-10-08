# 12. Troubleshooting

> First check **Settings › Diagnostics**, and if that does not solve it, let us know with **Send an error report**.
> If a device problem stops Avatar Live from starting, try **launching while holding Shift** (Safe Start).

## Start-up and installation

| Symptom | Solution |
|---|---|
| "Windows protected your PC" window | **More info → Run anyway** |
| "Avatar Live's files have been changed" | Reinstall from the original you downloaded from BOOTH (avatars and settings are kept) |
| Activation does not work | Check your internet connection and try again |
| Launching only brings the window to the front | It is already running (check the tray) |

## Avatar

| Symptom | Solution |
|---|---|
| Some parts are pink | Check that the avatar uploads normally, then export again |
| "It was made by a newer exporter" | Update Avatar Live |
| The head and hands do not move | Check that it is a humanoid avatar |
| Avatar sound effects do not play | Avatar sound effects are not played |
| The avatar is not visible | Double-click an empty area of the view, or use the **⌂** scene tool |
| The pose is frozen, the hair is tangled | **⟲ Reset** at the top |

## Webcam and face

| Symptom | Solution |
|---|---|
| Camera "Failed" | Check whether another app is using the camera |
| The camera image is black | Check the lens cover and the Windows camera privacy settings |
| Expressions are too small / too large | Run **Automatic face setup** again, use **Face adjustment** |
| The avatar looks to the side | **Recenter** |
| Winks do not work | Set the blink mode to **Independent** or **Smart** |
| Left and right are swapped | **Mirror** |
| High CPU usage | Set tracking quality to **Balanced** or **Eco** |

## Microphone

| Symptom | Solution |
|---|---|
| "No signal" | In Windows Settings › Privacy › Microphone, allow desktop apps |
| "Nearly silent" | If you use a mixer app, choose that app's virtual microphone |
| Noise moves the mouth | **Detect background noise** |
| The mouth moves too little | **Voice calibration**, **Sensitivity** |

## Output

| Symptom | Solution |
|---|---|
| No Spout2 source in OBS | Install the Spout2 plugin in OBS |
| The background is black in OBS | Background **Transparent** + OBS **Composite with alpha** |
| The virtual camera is not in Discord | Install the virtual camera, then quit Discord completely and open it again |
| 4K goes out as 1080p | You are using the Basic edition (Pro supports 4K) |
| "Avatar Live Basic" text | The Basic watermark (Pro has none) |

## Discord screen share

| Symptom | Solution |
|---|---|
| Not in the Discord list | Turn on **Screen share** and check Discord's **Applications** tab |
| Black screen | Run Avatar Live without administrator rights, put the game in windowed mode |
| No sound | Turn on sound in Discord, install a virtual playback device |
| Sound is heard twice | Set **Discord audio device** to a device you do not listen to |
| Video is black | Protected video (DRM) cannot be captured |

## Supported features

| | Details |
|---|---|
| ✅ VRChat avatar features | Expressions menu and parameters, animators such as FX, PhysBones, Contacts, Constraints, Eye Look, LipSync |
| ✅ Creation tools | Avatars made with NDMF, Modular Avatar, VRCFury and similar tools |
| ✅ Shaders | Poiyomi, lilToon and others |
| ✅ Face | VRCFaceTracking, ARKit (Perfect Sync), MMD eye morphs |
| ⚠️ Does not work | Avatar sound effects, AudioLink, mirror and camera detection, Light Volumes, custom scripts |
| 🧪 Experimental features | Ultraleap, iFacialMocap, OSC / VMC, camera detection of tongue and cheeks — expected to work, but the devices and apps involved have not yet been tested in the developer's environment |
| ❌ Not supported | VRM files, Live2D, macOS, Linux |

## Frequently asked questions

**Q. Do I need a VRChat account?**
No. Avatar Live does not communicate with VRChat.

**Q. Can I use it for streaming?**
Streaming, publishing videos and commercial use require **Pro**.

**Q. Is my keyboard input recorded?**
No. Desk hand motion never saves, records or sends the characters you type.

**Q. Can I give my avatar file to other people?**
Follow the terms of use of the avatar and outfit creators.

**Q. Can I show several avatars at once?**
One at a time. Switch avatars from the avatar name at the top left.
