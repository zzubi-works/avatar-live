# Troubleshooting

Check the items that match your symptoms first. If it's hard to find a setting, you can search by name using the magnifying glass at the top.

## Startup and Avatar

| Symptom | First Things to Try |
|---|---|
| Startup does not work well | Hold Shift while running to use Safe Start without webcam or microphone. |
| It says the file has changed | Extract the original ZIP received from the seller into a new folder and run it. |
| Avatar is not visible | Re-adjust for face, upper body, or full body layout. |
| Some parts are pink | Check the materials and shaders in the original Unity project, then re-export. |
| Hair is tangled | Click the top Reset button. |

## Face and Hands

| Symptom | First Things to Try |
|---|---|
| Webcam does not turn on | Check if another app is using the camera. |
| Avatar does not move | In Device → Tracking Source, check whether each part is using the device you actually connected. |
| Face direction is off | Look straight ahead and click Front Calibration. |
| Wink does not work | Change the blinking method separately. |
| Expression is too big or too small | Use Auto Face Setting or adjust the sensitivity in Face Adjustment. |
| Fingers are shaking | Increase Hand Shake Correction slightly. |
| If you reach out, your arm twists | Turn off experimental hand depth estimation and compare with the previous arm method. |
| Does not switch to idle pose | Specify the idle pose and check the waiting time for default/AFK pose in the menu. |
| No response after connecting iPhone | Make sure the phone app is sending to the PC address and wait for front-facing calibration to start. |
| VMC pose is misaligned | Check input status and adjust to T-pose/alignment. |

## OBS and Video Output

| Symptom | What to try first |
|---|---|
| Spout2 Capture is missing | Install the Spout2 plugin for OBS and then restart OBS. |
| NDI Source is missing | Install DistroAV and the NDI Runtime required for that version. |
| Background appears black | Set Avatar Live background to transparent and adjust OBS source for alpha compositing. |
| Does not appear after changing transmission name | Re-select the new name in OBS source. |
| Virtual camera does not appear in the list | Register the device and completely restart the receiving app. |
| My screen and broadcast composition are different | Check whether the streaming target is the scene view or the studio camera. |

For detailed installation steps, see [Output](09-output.md).

## Screen Sharing

- Not in Discord list: Turn on screen sharing and look for Avatar Live Share Output in the application tab.
- The game screen is black: Try changing the game to borderless window mode.
- No sound is shared: Check the audio target and app volume. If there is guidance on virtual audio devices, see [VB-CABLE guide](13-license.md#vb-cable).
- Call sound heard again: Check if Discord is included in the app you want to share.

## Remote Collaboration

First, check whether the host has started the server and whether the participant address, port, and password are correct. If an external friend cannot connect, open the port forwarding and firewall guide in [When connection does not work](09-session.md#troubleshooting-connections).

If the other party appears as a substitute avatar, check the avatar view and data transfer consent. Use a substitute avatar for models that do not allow transfer.

## When the screen is slow or blurry

1. Try lowering the output resolution and FPS.
2. Reduce the refresh rate and the number of grids in the multi-view.
3. Turn off the Spout2 output for cameras that are not in use.
4. Try turning off effects one by one, such as environmental light occlusion, depth of field, and volumetric lighting.
5. If the whole image is hazy, check the bloom intensity, threshold, and blur.

## If not resolved

In Settings → Diagnostics → Send Error Report, write down the following:

- Which button you pressed or settings you changed
- What looked strange
- The device and type of avatar you are using
- The sequence of steps that reproduce the same problem

The actual transmission is performed when the user chooses to send it.

## Supported Scope

- `.vavatar` and VRM 0.x·1.0 avatars
- Supported features such as the avatar's expression menu, animator, PhysBone, etc.
- Facial tracking settings and expressions included in the avatar
- Webcam, microphone, iPhone, VMC inputs

Some special shaders in VRM 0.x may not be supported. Features shown experimentally in the app may produce different results depending on the device and environment.
