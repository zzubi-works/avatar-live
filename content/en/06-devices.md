# Devices

Connect your webcam, microphone, and trackers, and choose the input to use for your face, body, and hands.

## Camera · microphone

![Webcam and Microphone Settings](img/guide-devices.png)

| Button/Item | Function |
|---|---|
| Webcam Switch | Start or stop tracking with the selected camera. |
| Camera List | Choose the webcam to use. |
| Frontal Calibration | Align the direction you are currently facing with the front of the avatar. |
| Tracking Quality | 'Smooth' calculates movements more frequently. 'Balanced' and 'Economy' reduce the load on the PC. |
| Microphone Switch | Start or stop mouth movement tracking with the selected microphone. |
| Input Bar | Shows the volume of incoming voice. Check if it moves when you speak. |
| Noise Gate | Prevents the mouth from opening for small sounds. |
| Measure Background Noise | Measures sound when you are not speaking to set the noise threshold. |

Raising the noise gate threshold makes it less sensitive to keyboard sounds but may ignore small voices. If the mouth does not move well, try lowering the threshold.

## Tracking

### Tracking Sources

![Choosing input for each body part](img/guide-tracking-sources.png)

Choose what to use to move each of the face, mouth, head, eyes, arms, hands, fingers, and body.

| Option | When to Use |
|---|---|
| Webcam | Follows the movements of my face, body, and hands as seen by the camera. |
| iPhone | Moves expressions and head using the iPhone face app. |
| VMC | Receives movements from other motion capture apps or tracker apps. |
| Ultraleap | Moves the hands using a dedicated hand tracker. |
| SteamVR | Connects the HMD, controllers, and trackers to body parts. |
| Off | Does not use tracking input for that body part. |

Example: You can set the face to iPhone and arms and hands to webcam. Even if a device is connected, the body part will not move if its source points to a different input.

#### Mouth

The mouth's source is chosen in one place, the "Mouth" row of this list. Motion › Mouth only shows the source chosen now.

| Choice | How the mouth moves |
|---|---|
| Face | Follows the mouth the webcam or iPhone reads. |
| Face + mic | Uses the face and the voice together. Choose how they mix right below. |
| Mic | The voice only (lip sync). Without sound the mouth stays closed even if you open yours. |
| Off | Tracking does not move the mouth; it stays as the avatar's animation leaves it. |

While the face comes from an iPhone or VMC, "Face" shows as "iPhone" or "VMC".

With Face + mic, the mixing appears below it and is saved per avatar.

- Mic when speaking: while you speak the voice moves the mouth; while you are silent, the face does.
- Maximum: each mouth shape takes whichever opens it more, the face or the voice. A mouth held wide open stays open while you speak too.

The mixing only makes a difference on avatars whose mouth the face tracking moves (face tracking or Perfect Sync mouth shapes). On an avatar with only ordinary VRChat visemes the voice moves the visemes either way, so both look the same.

An iPhone measures the mouth itself, so its mouth takes the voice only with "Microphone moves the iPhone's mouth" on, in the same place. It is off by default; an avatar's settings made with an older version may have it on.

#### Full Body and Fingers with Webcam

- Full body: Tracks the torso and legs visible in the camera. Legs hidden by a desk are not tracked as if they were visible.
- Finger joint tracking: Follows the bending and spreading of finger joints.
- Hand tremor correction: Increasing this reduces minor tremors, but fast movements will follow slightly delayed.

### SteamVR Connection

![SteamVR Device Setup](img/guide-steamvr.png)

1. Check if the HMD, controllers, and trackers are recognized in SteamVR.
2. Device → Turn on SteamVR.
3. Connect the device to the corresponding part such as the head, hand, or body.
4. Run the calibration to align the avatar with the position of my device.

### iPhone Connection

![External face tracking connection setup](img/guide-phone.png)

1. Connect the iPhone and PC to the same Wi-Fi.
2. Choose iFacialMocap or FaceMotion3D in the face engine.
3. Copy this PC's address and enter it into the target address of the phone app.
4. Turn on the input switch and look straight ahead for a moment. Calibration will start about 3 seconds after the first facial input.
5. Check whether data is coming in during the connection test.

| Item | When turned on or changed |
|---|---|
| Mirror | Reflects left and right movement like a mirror. |
| Switch to webcam if disconnected | Switch to the webcam while the phone connection is disconnected. |
| iPhone Address | Used in a method where the PC address is not entered in the mobile app. In a normal connection, it can be left empty. |

### VMC Connection

![VMC Input and Connection Status](img/guide-vmc.png)

1. Turn on VMC transmission in the sending app and send it to this PC's receiving address and port.
2. Select the area to be received from the tracking source using the VMC.
3. Check whether the number of units received in the VMC settings and the input status are displayed.
4. If your body direction or arms are misaligned, adjust them to a T position or alignment.

**VMC tracking tested with:** ReboCap, HTC VIVE Tracker, and Tundra Tracker.

If the device is connected normally but the movement is unusual, check the smoothness, calibration, and tracking return settings in [Motion](07-motion.md).
