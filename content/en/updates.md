# Update History

Changes in each Avatar Live release, starting with the latest update.

## 2026/10/23 — v2.1.2

- Fixed a one-frame flash in the Orbit camera mode: right after switching views or moving the camera, the avatar was shown from the wrong place for a single frame.

## 2026/10/22 — v2.1.1

- **Grab a studio camera:** Turning on Grab for a studio camera shows the camera and what it frames in the scene view, and you can move and turn it with arrows and rings, just like a prop. While you hold it, that camera's picture shows small in a corner. The camera's outline never appears on air, in recordings or in photos; press Esc to let go.

## 2026/10/22 — v2.1.0

**New**

- **More lighting:** Added photo light placements and approximate soft lights such as softboxes, beam quality, gobos (cookies), volumetric light and local fog, decorative and ambient lights such as neon, RGB, LED strips, candles, monitors, the sun and the moon, plus moving heads and lasers. Lights can also pulse, flicker, cycle colours, pan and tilt, or react to sound.
- **Add-light picker and lighting presets:** A new add-light picker with search, favourites and recent items, and 18 lighting presets.
- **Photosensitivity protection:** Fast-flashing lights are limited to 3 flashes per second across the whole screen, counting all effects together. The limit is lifted only after you confirm it on this PC.
- **Light timeline:** Key each light in the sequencer to animate your lighting. Light keys can be imported from VMD files, and keys can be copied and pasted, with editable influence curves.
- **Game light sync:** The colour and brightness of the game you share are reflected in the avatar's lighting in real time. Off by default.
- **Ambient projection:** A soft, blurred glow of the game screen falls gently on the avatar so it blends into the scene's mood. Only the avatar receives it, and transparent backgrounds stay transparent. Off by default.
- **Sky, fog and light:** Added 4 sky backgrounds, fog, light that bounces off walls, and softer shadows.
- **Room editing:** Hide, move or reset a room's walls, floors, doors, windows and furniture piece by piece. Switch whole kinds on or off at once, bring hidden pieces back, control the room's lamps and their brightness, and choose where the avatar stands. Only your changes are saved in the scene. Walls, what hangs on them and props that block the camera on air drop out of the picture only, keeping their shadows and light.
- **New interiors:** Added 4 rooms and a whole house, including the view outside the windows. Choosing a room also applies its own mood (bounced light, corner shading, reflections). The existing interiors can now be used as a whole building too.
- **Sequencer:** Blender-like editing with keys, a dope sheet, graphs, pose copy, pins, clip mixing and baking. Import .vrma, .bvh and .vmd motions; the arm angle and movement scale are remembered per file.
- **Free posing:** Dragging a hand, foot or the hips now moves the whole body naturally. Lowering the hips keeps the feet on the floor.
- **Breathing in held poses:** Breathing continues while a pose is held, so the avatar no longer looks frozen.
- **Start screen:** Reorganised so your avatar, devices and lists are easy to take in at a glance.


**Fixes and improvements**

- Fixed hair or clothing on some avatars sticking up and staying there.
- Fixed particle effects coming from the body appearing where the avatar had been standing after changing pose, such as sitting or lying down.
- Fixed see-through hair appearing to show the background where it overlapped screen effects.
- Soft shadow settings are now shared in remote sessions.
- **Better scene saving:** Each scene now keeps the avatar's own position and pose, and opening the scene brings them back. Switching to another avatar in a scene saves that avatar with the scene. Going back to the avatar list with unsaved changes asks whether to save them.
- Fixed the whole room moving along when the avatar was moved up or down.
- Lighting, effect and ambient presets are folded by kind, with your own saved presets at the top.
- Background choices are now Color, Green, Transparent, Image and Sky. An existing blue background stays as a Color background of the same blue.
- The studio camera list has fewer buttons so camera names are easier to read. Grab and Put on the current view are in each camera's settings.
- The add-light picker always opens below its button.
- Existing .vavatar files work without re-exporting.

## 2026/10/19 — v2.0.15

- **Eye rendering fix for some avatars:** Fixed pupils disappearing or eye areas appearing hollow on avatars whose eye bones have a rotated forward reference. Gaze now applies only the change from each avatar's own reference pose. Existing .vavatar files work without re-exporting.
- **Restore eye pose when control ends:** Turning off eye control or switching avatars now restores eye bones to their animated pose regardless of eyelid mesh settings.

## 2026/10/19 — v2.0.14

- **Choose where settings are stored:** Settings > Settings files > Storage location > Change location copies your settings, avatar library, poses, scenes and more to the folder you pick, and Avatar Live uses it from the next start. Use default location moves back. The old folder is not deleted and the licence is not moved. If the chosen place (such as an external drive) is missing, Avatar Live starts from the default location and says so.
- **Settings file management:** Settings > Settings files now offers Back up now, Import from another folder, and a backup list with Restore and Delete. You can also back up automatically at start and choose how many backups to keep (3, 5, 10 or 20). Restores and imports apply the next time Avatar Live starts, and the settings in place just before are backed up first.
- **Tidier resolution fields:** Under the resolution of the output image, screen share, window and photo, "Custom size" now folds open its width and height fields in the same way everywhere. "Use source resolution" and "Use this monitor's size" sit inside that fold, and Enter applies a typed size.
- **Stream Deck:** The "Install plugin" button under Settings > Hotkeys · Quick Actions > Stream Deck now lines up with the other buttons.

## 2026/10/18 — v2.0.13

- **VMC tracking stability:** Fixed mixing of bone and hip pose data from multiple programs sending to the same VMC input. Old tracking and facial data are also cleared more reliably on disconnect or reconnect.
- **Independent pose and facial senders:** Devices > VMC Input now lets you choose pose and expression senders separately, including automatic selection. If the sender's port changes after restarting its app, select it again.
- **VMC feedback-loop protection:** Temporarily suspends VMC output when its destination would feed directly back into Avatar Live's own input.
- **iPhone facial tracking:** Improved sender validation for iFacialMocap and FaceMotion3D, facial rotation inversion and neutral-angle handling when changing avatars.
- **Ultraleap and SteamVR:** Reapplies desk, chest or monitor-top hand-tracking modes after reconnecting, improves tracking freshness and repeated-frame handling, and prevents calibration with untracked SteamVR devices.
- **OpenSeeFace and VRCFT:** Improved face-tracker process and receiver restart safety, stale frame rejection, and consistent application of external OSC expression bundles.

## 2026/10/18 — v2.0.12

- **Screen sharing and display resolution:** In Output > Screen Share, enter a width and height or use the shared source's resolution. The display window also supports the current monitor's size and custom dimensions, including 21:9 and other aspect ratios. Your licence's output limits still apply.
- **Desktop avatar:** Show your avatar in a transparent window over your own desktop, with clicks passing through to the app underneath. Turn it on or off in Output > Screen Share, or turn it off with `Ctrl+Alt+F12`. Requires Windows 10 version 2004 or later and a compatible graphics device.
- **Leap Motion mounting:** Choose desk, neck/chest or monitor-top placement to set both the sensor's base orientation and tracking mode. Check the position and angle, then recalibrate your hands after changing the mount. Ultraleap software must support the selected mode; an explanation appears if it cannot be applied.
- **Sequencer correction layers:** Fixed copy/paste overwriting separate correction layers on the same bone. Rotation and IK drags preserve the existing influence, with fixes for writing the IK result back into rotation keys and for rotations flipping at low influence.
- **Keyframes and editing layout:** Scale the timing of selected position, scale, expression and rotation keys together; conflicting edits leave the data unchanged. Improved key navigation, sequence duration updates, toolbar layout in narrow windows and expression searches inside collapsed meshes.
- **Ambient occlusion (AO):** Fixed hidden objects' outlines showing through foreground surfaces when AO was enabled.
- **Memory and resources:** Compressed undo history and limited how much is retained. Improved resource cleanup when motion sources are removed, effects are toggled or output resolution changes, and reduced temporary allocations during curve evaluation.


## 2026/10/18 — v2.0.11

- **iPhone face tracking:** Improved reception of fractional expression values, face-only frames, and TCP frame delimiters used by iFacialMocap and FaceMotion3D compatibility modes. Invalid numbers can no longer overwrite the last valid face frame.
- **Repeated pairing:** Streaming requests are no longer repeated while a TCP connection or incoming traffic is active. Retries back off when the phone is silent. Diagnostics now distinguish the connection, incoming traffic and decoding failures.
- **Perfect Sync recognition:** Added support for ARKit BlendShape names ending in `.L` and `.R`. Reports include unrecognized names and scanned mesh/shape counts, and clarify when an avatar only provides MMD blink morphs. Perfect Sync requires compatible avatar expression shapes.
- **Attached lights and shadows:** Fixed imported avatars losing the target layers of their attached lights or cameras. Shadow distance now covers all active avatars, including when the controlled avatar changes or another avatar is farther away.
- **Spine posing:** In pose editing and the motion sequencer, move Spine to lean the upper body while maintaining the leg pose. Rotation editing, global/timed corrections, save/load and undo remain available.

## 2026/10/17 — v2.0.10

- **Motion sequencer editing:** Improved marquee and multi-key selection, Select All, copy/paste/cut/duplicate/delete, undo/redo, and clearly highlighted selected keys. The Summary row now selects and moves keys at the same time together.
- **Timeline navigation:** Resize the visible time range by dragging the ends of the bottom navigator, pan by dragging its center, and frame selected keys.
- **Whole-avatar transforms:** Animate both the entire avatar's position and rotation with sequence keys. Use `G` for root movement and `Shift+G` for root rotation.
- **Global and local corrections:** Apply IK position, bone rotation, and scale corrections to the entire sequence or to a selected time span on separate layers. Stack global and local corrections; adjust the time range and fade-in/out with timeline handles.
- **Smoother correction authoring:** New edits no longer insert automatic zero-correction boundary keys. A configurable nearby-key radius helps spread an edit across neighboring keys; existing saved sequences are preserved.
- **Expressions by mesh:** Fold and expand individual meshes, search all BlendShapes in a vertically scrollable, resizable list, and edit values and keys directly.
- **Multi-avatar sequencer:** Add avatars, select their tracks, link their timeline timing, copy motion clips between avatars, and operate each avatar's outfit/item menu. Multi-avatar availability still follows the product edition.
- **Pose-attached particles:** Improved spawn positions for bone-attached ParticleSystem effects and linked subemitters when a pose changes.
- **Limitations:** Time synchronization and clip copying do not live-link corrections between avatars; avatar menu toggles are not yet recorded as animation keys.

## 2026/10/16 — v2.0.6

- **Shared studio in remote sessions:** Guests can follow the host's room, background, floor, props, lighting, environment and post-processing. This is enabled by default but each guest can turn it off. Personal cameras, director controls, avatar toggles and saved scene files are preserved.
- **External asset sharing:** With session consent, background images, prop files and content packs explicitly permitted for sharing can be transferred. Received assets stay in a temporary session folder.
- **Camera shortcuts:** New cameras no longer receive number keys automatically. Right-click a camera row to assign a shortcut or add it to the bottom toolbar. Assignments remain tied to camera IDs when cameras are reordered.
- **Stream Deck:** Connect Stream Deck buttons through the same shortcut assignment dialog.
- **Scene saving:** Scenes are no longer overwritten automatically. On exit, choose Save, Don't Save or Cancel. Explicitly overwriting a scene creates a `.bak` backup; automatic saving of general settings, including devices, is unchanged.
- **Editable poses:** Save poses as Unity `.anim` files and open the actual save folder. Imported `.anim` poses can be edited and saved as new poses.
- **Avatar load recovery:** Unnamed Animator parameters are skipped with a warning, and failed initialization releases the loading state so you can retry.
- **Japanese UI:** Explicit Noto Sans JP font selection and shorter button labels improve Japanese text rendering.

## 2026/10/16 — v2.0.5

- Fixed repeated errors in the Devices menu caused by invalid Windows `PATH` or Steam paths. Ultraleap library discovery now skips invalid candidates.
- Moved device-library discovery to a background task so the menu does not wait for the scan.

## 2026/10/16 — v2.0.4

- Added passive VMC/ReboCap diagnostics for packet and bone-data stalls, recovery, tracking loss, sudden pose changes and frame delays.
- Diagnostic details are included in error reports (`Player.log` and `diagnostics.txt`). Tracking motion and IK behavior remain unchanged.

## 2026/10/16 — v2.0.3

- Fixed a VRC Parent Constraint issue where hand-attached props could reuse an old world position after unfreezing while the constraint was inactive and then reactivating it.

## 2026/10/15 — v2.0.2

- Fixed avatar menu toggles for hair and props not syncing to session peers when restored from saved settings or reset to their defaults.
- **Important:** All session participants must update to v2.0.2 or later for this fix and the v2.0.1 fix to take effect.

## 2026/10/15 — v2.0.1

- Fixed mesh visibility synchronization that could incorrectly hide hair and other child meshes on remote avatars.

## 2026/10/15 — v2.0.0

- Studio brings scenes, avatars, cameras, backgrounds, lights and props together.
- Pro can place multiple avatars, switch the controlled avatar and drive them with shared movement.
- Pro can create multiple cameras, switch with cuts/crossfades and compare shots in multiview.
- Expanded room presets, the prop library, bone-attached props and lighting settings.
- Added additional post effects and ambient occlusion to Pro.
- Effects such as bloom, color, lenses, focus and pixelation can be enabled and adjusted individually.
- Existing post-processing remains available in Basic and Pro.
- Added NDI® output to Basic and Pro for sending video to OBS on another PC.
- Pro supports per-camera Spout2 output and MP4 recording.
- Pro remote sessions bring friends' avatars from different PCs into one scene.
- Improved photo crop, aspect ratio, resolution and screen-sharing audio.
- VRM 0.x and 1.0 avatars can be opened directly. Some custom shaders are unsupported.
- Added SteamVR device input and full-body calibration; experimental support needs checks for each device.
- Improved face/head movement, lost-tracking recovery, VMC input and arm/hand motion.
- Expanded hand poses, AFK poses, gaze and lip-sync settings.
- Improved CPU use and menu operation with multiple avatars.
- Improved Avatar Exporter physics and fixed some disappearing hair/accessory parts.

## 2026/10/12 — v1.1.6

- Completely revised PhysBone and physics calculations.
- Updated Animator logic and animation property bindings to improve coordination between fingers, gestures and physics.

## 2026/10/12 — v1.1.5

- Fixed Eyes on the camera so it works even when facial tracking is disabled for a pose.
- Moved per-avatar AFK wait, transition and recovery timing from Settings to Motion › Body, preserving saved values.
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

- Right-click a custom expression to assign a global hotkey. Hold-to-apply and press-to-toggle modes are supported, and hotkey expressions take priority over automatic expressions.
- Saved poses can be assigned hotkeys from the right-click or ⋯ menu. Press once to apply and again to release; hotkeys are saved per avatar.
- In Scene > Scenes, you can save the current background, lights, objects, pose, expression and camera with a thumbnail, then restore them together. Ctrl+Z undo is also supported.
- You can drag expression-menu items and My Expressions tiles to change their order.
- You can return to avatar selection and switch avatars without restarting the app.
- Added per-pose tracking permissions, object groups and pose folders. Object size can be entered separately for X/Y/Z with optional linked proportions.
- Improved upper-body movement when shoulders are visible in desk mode, and added a separate upper-body tracking toggle and strength control.
- Simplified the Settings > License screen.

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
