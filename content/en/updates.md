# Update History

Changes in each Avatar Live release, starting with the latest update.

## 2026/10/12 — v1.1.5

- Fixed **Eyes on the camera** so it works even when facial tracking is disabled for a pose.
- Moved per-avatar AFK wait, transition and recovery timing from Settings to **Motion › Body**, preserving saved values.
- Expanded settings search to include AFK, tracking loss, gaze, desk mode, lighting effects, output options and hotkeys.
- Avatar Live now checks for updates once on every launch and displays the update indicator when a newer version is available, even if automatic downloading is disabled.
- Removed the duplicate version from About and shortened pose and AFK explanations, including repetitive card fold-and-drag tips.

## 2026/10/12 — v1.1.4

- Corrected left/right expression channels, including blinking, in iFacialMocap mirror mode.
- Improved AFK/waiting pose entry when the iPhone reports face tracking loss through trackingStatus.
- Fixed desk-mode arm fallback with iPhone-only face tracking when webcam body data is unavailable.
- Added per-avatar settings for AFK entry delay, blend-in and return durations.
- Prepared menu layouts during avatar loading to reduce first-open lag. Initial loading may take slightly longer.
- Added top-bar settings search to find controls such as Mirror and Language.

- Existing avatars, saved poses, settings and menu-card order are preserved. Keep experimental hand-depth tracking OFF for regular use.

## 2026/10/12 — v1.1.3

- Fixed an input error that could stop menu buttons and switches from responding.
- Reorder menu cards by dropping anywhere in an expanded card's body or between cards. Added a full-card preview, insertion guide, automatic scrolling and Escape cancellation.
- Split pose tracking into facial, head, arms, fingers and torso controls. Facial tracking can remain active while head tracking is disabled.
- The default sitting pose now allows tracking while holding the hips and legs. All five controls start enabled for new settings. On upgrade, tracking permission for the existing built-in sitting pose is enabled once; individual controls and custom poses are preserved. Turning it off afterwards remains saved.
- Shortened saved-pose descriptions with full-text tooltips, camera on/off icons and expand arrows. Tracking settings now form a connected card with the pose row, with improved spacing in narrow windows.

- Existing avatars, menu order, poses and settings are preserved. Basic/Pro feature access is unchanged.

## 2026/10/11 — v1.1.2

- My expressions in Scene and Menu: Added Import .anim next to New expression in both places, using the same import feature already available under Motion › Automatic expressions.
- You can import supported Unity .anim face/shape-key clips, including still expressions and multi-frame animations. Animation looping follows the clip's original settings.
- The v1.1.1 hand-depth default-OFF behavior is unchanged. Hand-depth estimation remains experimental and may cause unnatural or twisted arm motion when enabled.

## 2026/10/11 — v1.1.1

- Experimental webcam hand-depth estimation is now OFF by default, including a one-time reset of previously enabled settings on upgrade. Camera calibration and unrelated settings are preserved.
- You may turn it on manually afterwards, but keep it OFF if normal arm movement becomes distorted.

## 2026/10/11 — v1.1.0

- MediaPipe webcam receiving: Improved UDP packet reception and tracking loss/restart handling. Duplicate or stale detections no longer count as fresh movement observations.
- Arm and wrist stability: Adjusted tracking timestamps, shoulder references, elbow directions, and wrist processing to reduce severe webcam arm jitter. Results may vary by camera and setup.
- Separate default and waiting poses: Choose one pose for normal use and another for when tracking is lost. Tracking recovery returns to the active movement; explicitly applied manual poses take priority.
- Waiting facial expressions: Assign an expression saved under My expressions to the tracking-lost waiting state. You can also use a waiting expression without a waiting pose.
- Webcam hand reach (experimental): Added estimated hand depth using camera field of view (FOV) and body measurements, plus camera- and resolution-specific calibration settings.
- Settings and update reliability: Improved profile save ordering, failure recovery, and restoration when an update is interrupted.
- Discord screen-share audio: A missing virtual audio device now shows a warning and Install virtual audio driver button. With your consent, Avatar Live can install VB-CABLE by VB-Audio; no installation is needed if a compatible device is already present. See the [installation, licensing, and donation guide](09-output.md).

- ⚠️ Hand depth estimation is experimental and may be unstable. It can reduce arm jitter but may also make normal arm movement unnatural or twist the arm/wrist. If affected, turn Estimate depth off under Motion › Hands › Webcam reach. Testing and improvements with real cameras are ongoing.

## 2026/10/11 — v1.0.10

- Improved some excessive PhysBone movement. This is a temporary improvement, with further improvements planned.
- Closing the window while broadcasting now sends the app to the tray even when the normal close action is Quit.
- Photos match the preview framing, and vignette preserves transparency in broadcast output.
- Hotkeys support F13–F24 and modifiers. Right-click custom expressions or poses to add or remove Quick Actions.
- Camera preview first shows MediaPipe tracking after confirmation. Showing the raw camera image requires a separate confirmation to reduce accidental face exposure.
- Reset Everything also resets mesh changes. The top-left icon returns directly to avatar selection.
- Enter avatar scale on the X/Y/Z axes and unlink proportions to edit axes independently.
- Poses save separate tracking permissions for face, arms, fingers and torso, and can be duplicated from their context menu.
- Group lights and adjust group position, rotation and brightness. Scene and lighting-panel selections are synchronized, with right-click deletion.
- Drag the main collapsible section headers on each page to reorder them; the order is saved per page.
- Background colors apply immediately, duplicate hand-gesture guidance was removed, and the existing scene save behavior is retained.

## 2026/10/11 — v1.0.9

- My expressions: right-click to assign a global key; hold or toggle, with keyboard expressions taking priority over automatic expressions
- Saved poses: choose a key from right-click or the more menu; press to apply, press again to release, saved per avatar
- Scene > Scenes: save background, lights, objects, pose, expression and camera together with a thumbnail; restore in one click, undo with Ctrl+Z
- Drag expression menu and My expression tiles to reorder them
- Choose an avatar: return to the avatar list and switch without restarting the app
- Allow tracking per pose, object groups and pose folders, X/Y/Z object sizing with linked proportions
- Improved upper-body movement when shoulders are visible at the desk, with its own switch and strength
- Simplified Settings > License

## 2026/10/09 — v1.0.8

- Fixed automatic face calibration making weakly captured expressions excessively sensitive. Starting a new calibration now resets previous learned values and begins from the defaults.
- Webcam full-body and finger joint tracking are no longer experimental and are enabled by default on new installations (existing disabled settings are preserved).
- Improved HDR game capture in Discord screen sharing, converting HDR content to SDR to prevent washed-out or overly bright colours.
- Reduced the size and opacity of the license watermark in Discord screen sharing to match its subtle appearance in the app.
- Prevented multiple instances of Avatar Live from running. Launching the app again now brings the existing window to the foreground.
- Changed the window's X button to quit the app by default. Minimizing to the system tray remains available in Settings.
- Added a power button to the left sidebar. The logo menu now returns directly to avatar selection without restarting the application.
- Added a per-light "Moves with the camera" toggle.
- Fixed update history text being clipped or incorrectly positioned in Settings.
- Expanded diagnostic logging with FPS, CPU/GPU activity, frame timing and screen-sharing statistics.

## 2026/10/09 — v1.0.7

- Fixed an issue where updating to v1.0.6 unexpectedly switched webcam tracking sources for arms, head, body and other parts to VMC. Affected settings are now restored to webcam tracking.
- Improved arm and elbow stability in desk poses, with smoother transitions when lowering or raising the hands.
- Improved arm and hand positioning in sitting poses so they follow the avatar's body more naturally.
- When VMC arm input becomes unavailable, the arms now return to the desk resting pose instead of stopping unnaturally.
- Improved webcam upper-body tracking so shoulder movement can drive torso leaning and rotation without requiring lower-body tracking.
- Added X/Y/Z rotation rings for editing directional lights.
- Added "Reset all" to avatar hierarchy and mesh settings, and "Collapse all" to the hierarchy.

## 2026/10/09 — v1.0.6

- VMC can now be chosen as a tracking source per body part (arms, hands, fingers, body, head, eyes). Combine gloves, full-body trackers or other apps with the webcam, iPhone or Ultraleap.
- VMC applies each finger joint's rotation, spread and thumb, fitted to the avatar's rest pose (Align, T-pose, Reset).
- Added a Body part to Tracking sources.
- Added webcam full-body tracking (experimental, off by default).
- Added finger joint tracking (experimental, off by default).

## 2026/10/09 — v1.0.5

- iPhone face input (iFacialMocap, FaceMotion3D) connects directly and uses all 52 ARKit expressions as sent. Added face style presets.
- Fixed the mouth turning pointed when smiling with the mouth open on webcam.
- Reorganized tracking sources (face apps under Face engine, Ultraleap under Hands).
- Added hand steadiness so webcam hands and fingers no longer tremble while still.
- Improved posing (bone-sized rotation gizmo, symmetry, face the camera, feet on the floor, built-in standing and sitting poses, Done saves the pose).
- Added a pose library (.anim poses as thumbnails of your avatar; apply, edit, save).
- Added hierarchy, mesh on/off/hide and a shape key panel to the Avatar Menu.
- My expressions are now edited in a side panel.
- Added a light colour editor (RGB, hex, eyedropper), light ranges in the view, and aim/move handles.
- Photo: no UI / with UI / clear background, plus "Eyes on the camera".
- Background picture zoom and position; every slider value can be typed.
- Much lower CPU use while minimized or in the tray (unchanged while an output or share is running).
- Added in-app notices and Send a suggestion.
- Simplified the license window.

## 2026/10/09 — v1.0.4

- Desk pose: the hand now stays where it was last used (mouse or keyboard). For the old behaviour, turn on "Back to the keyboard when the mouse rests".

## 2026/10/09 — v1.0.3

- Desk pose: the mouse hand now rests nearer the body, and its position can be adjusted.

## 2026/10/09 — v1.0.2

- Fixed an issue preventing webcam tracking from starting when the installation path contained non-ANSI characters, including Korean characters.

## 2026/10/09 — v1.0.1

- Fixed tracking interruptions after changing the tracking quality.
- Removed the need to manually enter the iPhone address when using iFacialMocap.
- Improved settings panel pinning.
- Fixed tracking behavior in Eco mode.
- Improved PhysBone pose retention.
- Updated the wording of the Upgrade product.
