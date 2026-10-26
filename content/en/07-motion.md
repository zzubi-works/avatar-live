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

- Mouth: how far the voice opens the mouth now, and the current mouth shape (vowel).
- Auto Level: learns the room's noise and your speaking volume by itself and fits how far the mouth opens. While on, it shows the learned noise floor and speech peak (dB).
- Sensitivity: appears with Auto Level off. 0–100 %, more sensitive to the right: 100 % reacts to a whisper, 0 % only to a loud voice; the tooltip shows the level (dB) where the mouth starts to open. A value set in an older version carries over.
- What moves the mouth: shows the mouth's source now. It is changed in [Devices](06-devices.md) › Tracking Sources, "Mouth".
- Mic → face: whether the voice also goes into the face tracking's mouth shapes. Auto sends it only when the avatar's mouth is moved by its face tracking. It appears only while the microphone moves the mouth.
- Voice correction: Pronounce the guided vowels to match your voice.
- Tongue and cheek puffing: Apply the expression using a button or shortcut key. It will be visible only if the model has the required expression.

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
