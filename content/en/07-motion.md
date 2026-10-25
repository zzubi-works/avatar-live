# Motion

It determines how much and how smoothly my facial expressions and movements are reflected in the avatar. The settings are saved for each avatar.

## Face

![Face Tracking and Expression Control](img/guide-motion-face.png)

| Item | If adjusted |
|---|---|
| Face Tracking | When turned on, it reflects my facial expressions. When turned off, facial input is not used. |
| Mirror | Reflects left and right movement like a mirror. |
| Gesture → Facial Expression | Uses avatar expressions linked to hand shapes. |
| Expression Sensitivity | Increasing it makes even small expressions look bigger, lowering it makes them look calmer. |
| Softness | Increasing it reduces vibration, and lowering it makes it respond faster. |

### Automatic Face Settings

![Automatic Face Setup Guide](img/guide-face-calibration.png)

1. Press Automatic Face Setup.
2. Follow the instructions to look straight ahead or make a facial expression.
3. Press Measure and proceed to the next step.
4. Finally, press Apply.

### Face Adjustment

![Adjusting the face by separately matching the eyes, eyebrows, and mouth](img/guide-face-adjust.png)

- Eyes, eyebrows, mouth, cheeks: Adjust the movement size of each expression separately.
- Edit left and right together: If turned on, it changes both sides to the same value.
- Smoothing: Reduces small facial tremors. If set too high, the response is slow.

### When Expressions Don't Appear

You can only move the expressions that exist on the avatar. If there is a VRCFaceTracking setting, that setting will be used, and if there are ARKit shape keys, those facial shapes will be used. Expressions that do not exist will not be created even if sensitivity is increased.

## Eyes · Gaze

![Blinking and Gaze Settings](img/guide-motion-eyes.png)

| Item | Result |
|---|---|
| Separate Blinking | Closes the left and right eyes separately. Used for winking. |
| Blink Synchronization | Close both eyes together. |
| Automatic Blinking | Blinks at a regular interval even without input. |
| Eye Gaze Tracking | Reflects the direction of my eyeballs. |
| Camera view | Make the avatar's pupils face the camera. |
| Look-at target | Choose the object to look at, such as a camera or a specific avatar. |

Head tracking and facial tracking, as well as camera view, are set separately. Even in a fixed head pose, you can make only the eyes look at the camera.

## Mouth · Expressions

![Mic Lip Sync and Mouth Settings](img/guide-motion-mouth.png)

- Lip-sync intensity: Increasing it opens the mouth wider.
- Auto Level: Adjusts mouth movements to match the volume of the voice.
- Sensitivity: Shown when Auto Level is off. The higher it is, the quieter the voice that opens the mouth. 100% reacts even to a whisper, 0% only to a loud voice; the level (dB) at which the mouth starts to open is shown with it.
- Voice correction: Pronounce the guided vowels to match your voice.
- Tongue and cheek puffing: Apply the expression using a button or shortcut key. It will be visible only if the model has the required expression.

### What Moves the Mouth

The mouth card's Source chooses what moves the avatar's mouth. It is the same setting as Mouth in the Tracking Sources on [Devices](06-devices.md).

| Option | How the mouth moves |
|---|---|
| Face | Follows the mouth your webcam or iPhone reads. |
| Face + mic | Uses both the face and the voice. Choose how they mix right below. |
| Mic | Uses the voice only (lip sync). Without sound the mouth stays shut even if you open yours. |
| Off | Tracking does not move the mouth; it stays as the avatar's animation leaves it. |

The way Face + mic mixes is saved per avatar.

- Voice when speaking: While you speak the voice moves the mouth; while you are silent, the face does.
- Wider of the two: Each mouth shape takes whichever opens it more, the face or the voice. A mouth held wide open stays open while you speak too.

The difference between the two only shows on avatars whose mouth the face tracking moves (avatars with face tracking or Perfect Sync mouth shapes). On an avatar with only ordinary VRChat visemes the voice moves the visemes either way, so both look the same. A mouth from an iPhone is not mixed with the voice.

Mic → face decides whether the voice also goes into the face tracking's mouth shapes. Auto sends it only when the avatar's mouth is moved by its face tracking. It shows only while the mic moves the mouth.

### Auto Expressions

![Auto Expression Connection Settings](img/guide-auto-expression.png)

Turn it on in Actions → Auto Expressions. Connect the expressions saved in My Expressions to each detectable expression such as smile, surprise, or wink. Then, when you actually smile or are surprised, the connected expression will automatically appear.

## Head

![Head and Body Movement Settings](img/guide-motion-body.png)

| Item | If adjusted |
|---|---|
| Head Movement | Choose the size of movement: small, natural, or large. |

## Body

| Item | If adjusted |
|---|---|
| Follow Body | The body turns along when the head turns. |
| Natural Movement | Even when still, small idle movements are added. |
| Breathing | Small body movements as if breathing are added. |
| Upper Body/Full Body | Reflects the body movements received from the device. |

## Hands

![Arm/Hand Tracking and Desk Movements](img/guide-motion-hands.png)

| Item | Effect When Adjusted |
|---|---|
| Arm/Hand Smoothness | Increasing it reduces shaking, and fast hand gestures follow more slowly. |
| Dynamic Method | Uses an arm method that reflects changes in reaching distance. |
| Previous Method | Can be compared with the existing arm movement method. |
| Hand Depth Estimation | Estimates forward and backward distance with a webcam. Experimental, turn off if the arm twists. |
| Hand Release Return | Changes the speed at which the hands return to the default pose when not visible. |

## Desk

When the hands are not visible to the camera, the avatar hands move according to keyboard and mouse use.

- Default Hand Pose: Adjust the desk height, hand spacing, and wrist angle.
- Keyboard Response: The movement size of fingers and hands when typing.
- Mouse Response: The size of hand movement following the mouse.
- When the hands are back in view of the camera, it returns to tracking.

Keyboard input is only used to create hand movements; typed characters are not saved or transmitted.
