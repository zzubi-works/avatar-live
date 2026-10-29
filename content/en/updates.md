# Update History

Changes in each Avatar Live release, starting with the latest update.

## 2026/10/30 — v2.4.3

- **Lock share sources:** Lock the avatar or a source with the padlock in the source list or its right-click menu, and dragging or the wheel in the preview no longer moves it. The numbers and placement buttons still move it, and the lock is saved in layout presets.
- **Share source list:** Right-clicking the avatar no longer opens a blank white box. The spacing of the empty layout presets message and the "+ New preset" button is fixed.
- **Light effects:** Each effect's ⋯ and right-click menu has "Reset Effect". Changes on a light's card can be undone with Ctrl+Z and redone with Ctrl+Y.
- **Throw and sticker trails:** "Trail size", under "Trail amount", makes a trail 0.25 to 3 times as big.
- **Drawer edge:** The edges of the drawer and the node editor window show Windows' own resize cursor and a thin accent line instead of a grey bar.

## 2026/10/29 — v2.4.2

- **Smoother director mode:** Pictures nobody is looking at are no longer drawn, and the preview and multiview are drawn lighter. The scene view and outside outputs keep their quality.
- **Scenes restore:** Opening a scene brings back the saved avatar where it stood and in its pose.
- **App sound in recordings and the share:** Avatar Live's own sounds (throws, water and more) go into recordings, the screen share and the share's recording. Turn them off with the "App sound" switch on the recording card and "Avatar Live sound" in the share's audio.
- **Drawer width:** Drag the drawer's edge to change its width. Double-click it to go back to the default.
- **Notices:** Long notices are no longer cut off; they scroll inside the card.
- **Room packs:** Fixed missing walls in the sewers, classroom and night club (room pack 1.4.4 update).

## 2026/10/29 — v2.4.1

- **8K photos:** Photos can now be 8K (7680×4320, Pro). Edges are smoother, so a close crop stays sharp. The app no longer pauses while a PNG is saved, and depth of field, blur and grain in a large photo look as they do on screen.
- **Room names:** Rooms from room packs are named in the app's language, together with the new room pack update.
- **Update notice:** Shows only the new version's changes.

## 2026/10/29 — v2.4.0

- **AI staging over MCP:** A connected AI app can now work with lights and presets, game light sync, rooms, Simple setup rules, outputs, the screen share layout and node graphs. Every change waits for your approval and can be undone. An AI cannot turn on or change fast flashing, and the lighting changes it makes stay within the flashing limit.
- **Rooms:** Add your own room from a model file (FBX) under "My rooms"; its lights shine the way they were made. Pick a room pack and browse it as a list or a grid. Each room has "Lights the avatar too" to choose whether its lights reach the avatar (on by default).
- **Recording:** While the game's picture has not arrived, the recording shows "Waiting" and starts as soon as the game shows. Problems with the recording's sound or with finishing the file are reported, and a recording no longer drifts after its sound drops out.
- **On-air preview:** Its switch alone shows and hides the preview, also while a studio camera is held.
- **Screen share panel:** The sources picker opens at the button you pressed; sources, sound and presets fold into one card. Resolution and FPS are back under the share state.
- **Motion screen:** Expression keys have their own list beside the mesh tree, text no longer overlaps, and long help text became short tips. Messages and errors appear in all four languages.
- **Editing a running node graph:** Editing a graph while it runs (also in the separate editor window) keeps its delays, cooldowns, poses and variable values going. When both windows change the same graph, nothing is overwritten and you are told.
- **Full code review:** The whole app was reviewed, and the problems found in recording, screen share, motion, photo, lighting and more were fixed.

## 2026/10/28 — v2.3.0

- **Long-stream optimization:** Reviewed the whole app so CPU, GPU, memory and VRAM use no longer build up over long sessions. Fluids and physics, avatars, rendering, outputs and recording were tidied, and start-up memory is lower. Unused outputs, the webcam and a hidden window give their resources back.
- **Screen share HDR colour:** Sharing a screen or window on an HDR monitor now shows the same colours and brightness as an SDR screen. Also fixed a crash when a session restarts.
- **Screen share editing workspace:** The large editor is now a source-panel workspace. Add picture and text sources and manage layers and presets in one place. The frame rate for the stream and the screen share is one "Frame rate (FPS)" drop-down.
- **Motion Sequencer .anim export:** Saving in the Motion Sequencer now also writes a humanoid .anim for each avatar that plays. Pick the motion in an Animation node to play, stop, change speed and loop it; the clip's shape keys play with the bones. One avatar can also be exported as .anim or .vmd.
- **Motion player and sequencer:** Studio › Posing has a motion player: the avatars in the scene play a saved sequence from one clock, with its light, prop, room and camera tracks, forwards or backwards. The sequencer gains an optional camera track, per-mesh expression sliders, Alt+arrows to step keys a frame, and draggable loop ends and markers. .vmd export writes VRM expressions as MMD's standard morphs and the first directional light as a light motion.
- **Play-sound node and variables:** The node editor has a new node that plays a sound from a graph. Variables, a node that switches the camera director on or off, copy and paste of an input's value, dragging a number's label to change it, and dragging list items to reorder them are also available.
- **Simple setup rule switches:** Each rule in Simple setup has its own on/off switch, and rules edited in the node editor keep it. Rule rows were reorganized to read on one line.
- **Number fields and labels:** Numbers now sit in the middle of their fields, including colour channels, digit rows, custom size and motion numbers. Labels were shortened to fit their row, and clipped text is fixed.
- **Pouring liquid:** the first pour no longer stalls for a moment.

## 2026/10/27 — v2.2.11

- **Separate node editor lists:** In the detached editor window, nodes such as "Character: turn an expression or animation on or off" listed only `SELECTED_CHARACTER…`. The window now shows the avatar's expressions and animations, your own "My expressions" and the scene's objects exactly as the main window does.
- **Screen share on HDR:** Fixed the shared video turning black on PCs with an HDR monitor.
- **Studio objects:** Fixed some objects exported with Avatar Exporter not showing when several were placed together. Files you already exported show together without exporting them again.
- **Screen share layout:** Avatar and layer position (X/Y) and size (W/H) can be typed in pixels. Enter, cancel and focus changes in number fields are handled reliably.
- **Screen share presets:** Save the avatar layout and layer setup as presets and apply a whole scene at once.
- **iFacialMocap / FaceMotion3D:** A port number or other invalid value in the address field is reported before connecting, and a failed connection shows which port and program is in the way.
- **Rooms and DLC:** Improved room lighting and material quality and updated the DLC room packs to 1.4. Each room can use its own sky; fixed the alley walls disappearing and the club's effects missing.
- **Memory and stability:** Cleaned up paths where memory built up over long sessions of avatar changes, photo lights, lip sync, panels, animations and added objects. Fixed a repeated Animator IK warning while throwing.

## 2026/10/26 — v2.2.10

- **Separate node editor:** Fixed the detached window failing to open in the distributed build. Reopening focuses the existing window; an editor that exits before connecting is reported and can be opened again. Edits now save automatically while the separate window remains open. Fixed node menus remaining invisible in the separate window.
- **Donation amounts:** Minimum and test amounts accept larger values such as 100,000 and 1,000,000. Starting a test while the amount field is focused uses the value you just typed. Fixed values confirmed with Enter failing to save.
- **Multiple VMC inputs:** Receive body and glove tracking on separate ports at the same time. Add three or more receivers with individual channels, avatar targets and priorities. Losing one input leaves the others running. Finger-only input without wrist data continues to work after switching the controlled avatar.
- **Broadcast compatibility:** Corrected automatic output-format changes on HDR and high-bit-depth monitors and added output-format diagnostics. Discord black-screen reports still require verification with the affected GPU, HDR and capture settings.
- **Sharing OFF:** Stops unnecessary avatar composition, preview and capture resources. Active recording or screen lighting retains only the processing it needs.
- **iPhone and lip sync:** Fixed microphone-only mouth input being blocked when iPhone face tracking was active.
- **iFacial recovery:** Restarts failed receive sockets and TCP listeners. Temporary port conflicts can recover after the port is released; turning the input off also cancels retries.
- **Donation panel:** Corrected the play button's click area. Adjust width, maximum height and text size, move the panel, scroll its contents or reset it. Long messages wrap to the selected width. Fixed mirrored text on donation cards that face the camera.
- **Expanded preview:** Fixed competing size requests from the expanded view and small preview. The texture now updates to match the expanded view and window resizing.

## 2026/10/26 — v2.2.9

- **Broadcast output:** Improved projector output and preview handling. The enlarged preview stays sharp at its on-screen size, and output continues after the projector window is closed and reopened.
- **Wheel input:** The wheel works only inside the preview; scrolling outside it or over a popup no longer moves what is behind.
- **Broadcast recording:** Moved to Studio › Photo & Recording, with the same layout as studio recording.
- **Separate node editor window:** The node editor can open as its own Windows window that you can move, resize and maximize. Edits sync both ways, and you can keep editing there after closing the editor in the main window.
- **Shorter descriptions:** Menu and button descriptions now just say what each one does.
- **Diagnostics:** Added frame diagnostics for broadcast output. Items that were not measured are shown as not measured.

## 2026/10/26 — v2.2.8

- **Stable avatar targets:** Fixed explicit broadcast and node targets changing when control moved between duplicate avatars or another avatar was removed. Targets now retain the same scene slot across saving, reopening and restarting the app.
- **Saved target repair:** Removes obsolete avatar IDs from simple broadcast menu actions. Older duplicate-avatar targets that cannot be identified ask you to select the avatar again. Explicit targets in manually edited graphs and avatar-specific expressions, poses and views are preserved.
- **Avatar switching:** Held graph actions are released on their original avatar before control changes or the avatar is removed.
- **Liquid streams:** Changing node inputs and targets continue to affect an active stream. Input updates preserve the original automatic stop timer.
- **Throwing:** Pending throws and delayed collision continuations stop when their graph run is cancelled or interaction permission is removed. Corrected collision continuation and effect ordering.
- **Contact events:** Props with multiple colliders now report contacts through the owning physics body.

## 2026/10/26 — v2.2.7

- **Avatar menu:** Broadcast quick actions could remain pinned to the previous avatar: the choice stayed highlighted after switching, but nothing happened. They now run the matching menu action on the controlled avatar.
- **Clear search:** Fixed the X button in the node editor search field failing to clear the query.
- **Quit:** Window-close requests now use the normal application quit path. Stopping a share no longer drains queued settings before shutdown. Choosing Quit as the close action also works while broadcasting.
- **Thrown objects:** Imported props with a pivot far from their mesh could be invisible or hit a different body part. Flight now uses the visible centre, and offscreen and edge spawns use the target depth.
- **Impact strength:** Reduced the push at the same weight while preserving stronger reactions at higher weights. Improved collision detection for fast objects.
- **Prop cleanup:** Thrown props expire after their chosen lifetime even when scene time is paused. The last copy releases its imported file resources.
- **Export My expressions:** Choose Export .anim… from an expression’s context menu. Import it in My expressions on another avatar with the same shape keys, or use it in Unity. Animated expressions retain curves and looping.

## 2026/10/26 — v2.2.6

- **Version labels:** Updated the application and Windows file version to 2.2.6.
- **Release history:** Added the missing 2.2.6 entry. Its runtime behaviour is the same as 2.2.5; the reported fixes and .anim export are included in 2.2.7.

## 2026/10/26 — v2.2.5

- **Liquid sound:** Fixed the default sound playing even after another sound was chosen in the liquid's settings. The chosen sound now repeats while the liquid pours, and choosing no sound makes it silent. Leaving the default "Splat" keeps today's splash and pouring sound.
- **Choosing sounds:** The default sound a new rule starts with (the liquid's "Splat · random", throws, stickers) is replaced by the first other sound you choose. A rule saved earlier with both the default and your sound on plays one of them at random, so turn the default "Splat · random" off.

## 2026/10/26 — v2.2.4

- **Screen share indicator:** The top bar no longer shows "Screen share" while screen sharing is off. It appears only while the screen is actually being shared.
- **Mouth source:** What moves the mouth is chosen in one place, Devices › Tracking sources › Mouth. Motion › Mouth · Tongue · Cheeks now just shows the source in use.
- **Mixing:** When the face and the microphone are used together, choose "Mic when speaking" or "Maximum". The "Microphone moves the iPhone's mouth" switch moved to the same place.
- **Help text:** The tip now says the iPhone mouth mixes with the microphone only when "Microphone moves the iPhone's mouth" is on. The manual's Devices and Motion pages now cover the four mouth sources, the mixing and the 0–100% sensitivity.

## 2026/10/26 — v2.2.3

- **Broadcast overlays and previews:** Fixed reduced-size previews appearing black, and rotated overlays turning black or becoming darker. Preview colors and vertical orientation now display correctly.
- **Broadcast output:** Reworked screen capture, composition and output. Improved how the game screen and avatar are presented together and how output recovers after an interruption.
- **Moving game windows:** Fixed capture health checks using the previous monitor after a game window moved to another monitor.
- **Broadcast resolution:** Resizing the app window now preserves the configured resolution of the avatar image used for broadcast output.
- **Broadcast rules:** Fixed outdated rules continuing to run or respond to test buttons after an error while disabling or editing them. An error in one rule no longer blocks other rules or app functions.
- **Light effects:** Fixed the “Add effect” button in light settings failing to open its menu.
- **Performance and memory:** Improved cleanup of unused broadcast outputs and shared textures, and corrected how GPU priority settings are applied and restored.
- **Liquid effects:** Reduced repeated calculations for wet surfaces and skipped liquid rendering in cameras configured not to display the liquid. Idle liquid effects also release their resources.
- **Mouth tracking and lip sync:** Unified the mouth input setting and added per-avatar saving for face-tracking/microphone mixing settings. Lip-sync sensitivity is adjusted as a percentage.
- **Room lighting:** Fixed avatar skin appearing see-through in brightly lit rooms.

## 2026/10/26 — v2.2.2

- **Simple setup and stream integrations:** In 2.2.0 and 2.2.1, Simple setup rules didn't work and errors kept piling up, which also stopped stream connections such as CHZZK and other parts of the app. Fixed.
- **Node editor:** Links in graphs made with 2.2.0 or 2.2.1 stay connected.
- If one rule can't be set up, the other rules and the app keep working, and the error is logged once.

## 2026/10/25 — v2.2.1

- **iPhone face tracking:** When a pose held the head, the body still slid or turned with the iPhone's head movement. A pose that holds the head now keeps the body still too.
- **Panel colours:** Settings › UI › Theme offers Light, Dark, White, Black and Custom. For Custom you pick a panel colour and an accent colour; the rest follows, and the words are always adjusted to stay readable. The side menu can have its own theme (say, a white menu beside a black panel).
- **Panel look:** The light theme is a soft vanilla and lavender. The side menu sits flush with the window edge and the panel that opens tucks under it with a shadow; the background is clearer and the cards on top more solid.
- **Throwing Studio objects (Pro):** Simple setup's throw rules can also throw your own 3D models in the Studio (made with the Prop Exporter).
- **Cards:** Cards you can drag to reorder stand apart again, one by one.
- **Face card:** "Recenter" and "Automatic face setup…" sit on one row.
- **Game light:** Each avatar's share of the game light is set in Studio › Lighting › Game light sync › "Per avatar" instead of the Avatar Menu.
- **Animation layers:** Moved from the Avatar Menu to Broadcast › Interactions, since they are the animations broadcast events switch. Left as they are, ordinary tracking is not affected.
- **Error reports:** They now say what holds the head and how far the iPhone's head data jumped, so problems can be traced precisely.

## 2026/10/25 — v2.2.0

**New**

- **Stream integrations (beta, PRO):** Connect Twitch, CHZZK, SOOP or Discord on the new Broadcast page and your avatar reacts to viewers' channel points, chat, donations, subscriptions, balloons and more. This is a beta: if something doesn't work on a real stream, please send an error report (it now includes your stream connection history; tokens, codes, order numbers and emails are hidden).
- **Play together on Discord (beta, PRO):** Invite the bot to your server and link a channel to the app, and friends can trigger avatar reactions with buttons or the `/react` command. Point mini-games are included (daily check-in, roulette, slots, blackjack, quizzes, boss fights and more). Works while the app is running.
- **Simple setup (beta, PRO):** Press "+" and pick platform → event → reaction to make a rule that works right away. Supports amount ranges, per-viewer cooldowns and more items thrown for bigger donations.
- **Node editor (beta, PRO):** Wire events to reactions with nodes to build your own effects. It opens in a large window of its own, with a minimap and a TEST button on each event node.
- **Throwing, liquid, stickers and knock-downs (PRO):** Throw props at your avatar, pour water or milk that runs down the body and dries, stick images, GIFs or a viewer's profile picture onto the avatar. A hard hit knocks the avatar down and it slowly gets back up; choose its expression while down and how fast it gets up.
- **Test card:** At the bottom of Broadcast › Interactions, try throwing, knocking down, hitting, liquid and stickers right away, without a stream.
- **Donation box (PRO):** Shows donors' names and messages in a box inside the scene. Off by default.
- **WebSocket (PRO):** A WebSocket open only on your own PC for other programs to connect to. Off by default.
- **DLC room packs:** Buy the add-on on BOOTH, enter the order number in the existing code field, and 13 new rooms appear in the room list, downloading when you pick them: a Japanese alley (day and night), a Japanese apartment, a school pool, a showroom gallery, classrooms (day, evening and night) and a coworking office, each with its original lighting and mood. Turn the room's lamps on or off and set their brightness (saved with the room), and walls that block the camera drop out of the picture. Available on Basic too.
- **Screen objects:** Add a "Screen" under Studio › Objects to show an image or GIF, a monitor or window, or a Spout or NDI source inside the scene.

**Changes**

- **A redesigned panel:** grouped cards, segmented tabs, buttons at the right edge, a translucent rail and floating toolbars that softly show the scene behind them. The vertical layout and the left menu stay. The blur never appears in your stream, recordings or virtual camera, and the panel turns opaque when Windows transparency effects are off.
- **Where things moved:** Twitch and CHZZK connections and remote sessions are on the new Broadcast page; photos and the capture frame are in Studio › Photo & Recording; the knock-down settings are in Broadcast › Interactions. Long pages are grouped under subheadings. Card order and folds you changed are kept.
- **Renamed:** "Idle & layered animation" → "Animation layers", "Eye settings" → "Eye movement", "Gaze control" → "Look-at target".
- **Mouth movement:** With the mouth source set to "Face (iPhone)" or "Off", the microphone no longer moves the mouth. Choose "Face + mic" or "Mic" to move it with your voice.
- **App recording sound:** Besides your microphone, the shared game's sound is recorded too while you share a screen.
- **Right-click menus:** Every list (avatars, cameras, scenes, objects, presets and more) has a right-click (or ⋯) menu to rename, duplicate or delete, plus Delete and F2.
- **Session consent:** Joining a remote session now takes one checkbox and one "Exchange data" switch. Your existing choices are kept.
- **Code entry:** Upgrade and DLC codes also go into the single "Enter another code" window.
- **Low-poly interior:** The "whole building" choice was removed (its rooms stay). A scene saved with the whole building opens without a room.
- **Choosing a DLC room** sets the studio's ambient light, reflection strength and fog to match the room once; you can change them freely afterwards and they are saved with the scene. Switching to a built-in room or no room puts the defaults back, and the room never makes the avatar too bright.
- **Error reports** now include the stream connection state and recent events, so integration problems can be traced precisely.

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

## 2026/10/19 — v2.0.15

- **Eye rendering fix for some avatars:** Fixed pupils disappearing or eye areas appearing hollow on avatars whose eye bones have a rotated forward reference. Gaze now applies only the change from each avatar's own reference pose.
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

- Added passive VMC diagnostics for packet and bone-data stalls, recovery, tracking loss, sudden pose changes and frame delays.
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
