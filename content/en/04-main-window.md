# 4. Main window

![Main window](img/main.png)

## Left menu

| Menu | What it does | Guide |
|---|---|---|
| Logo | **Restart** (to the start screen) | [Chapter 3](03-launcher-and-library.md#returning-to-the-start-screen) |
| **Menu** | The avatar's Expressions menu, gestures, Quick Actions | [Chapter 5](05-avatar-menu.md) |
| **Devices** | Webcam, microphone, tracking sources, external trackers | [Chapter 6](06-devices.md) |
| **Motion** | Face, body, hands and desk | [Chapter 7](07-motion.md) |
| **Scene** | Background, lighting, effects, posing, objects | [Chapter 8](08-scene.md) |
| **Output** | Spout2, virtual camera, screen share | [Chapter 9](09-output.md) |
| **Settings** | Window, performance, language, hotkeys, license, updates | [Chapter 10](10-settings.md) |

When an update is available, a green dot appears on **Settings**.

The **pin** at the top right of the panel keeps the panel open while you click or drag in the scene. Close it with its menu button on the left or **F1**.

## Top

| Item | What it does |
|---|---|
| **Avatar name** (left) | Switch or add avatars ([Chapter 3](03-launcher-and-library.md#switching-avatars-while-running)) |
| **FPS** (right) | Current frame rate. Click to change the frame rate |
| Status | The trackers, microphone, outputs and screen share currently in use |
| **⟲ Reset** | Return tracking, hands, PhysBones and more to their initial state ([Chapter 5](05-avatar-menu.md#reset-and-reset-everything)). Right-click for recenter, camera start view or PhysBone reset on their own |
| Quick Action buttons | Buttons you have added ([Chapter 5](05-avatar-menu.md#quick-actions)) |

## Bottom toolbar

| Button | What it does |
|---|---|
| **Face / upper body / full body** | Change the camera framing |
| Saved views | Move to a saved camera position (right-click: rename, order, hide, start view, delete) |
| **+** | Save the current camera as a view |
| Quick Action buttons | Buttons you have added |
| View gizmo | View from the front, side, top and other directions; switch perspective / orthographic |
| **Lock the camera** | Stop the mouse from moving the camera |
| **Camera** | Camera settings (below) |

You can drag the toolbar to move it, and right-click it to change its opacity.

### Camera settings

| Item | What it does |
|---|---|
| **Save PNG / Open folder** | Save the view as a picture without the UI |
| **Lock the camera** | Fix the camera in place |
| **Lens** | Perspective / orthographic, **Field of view**, **View** |
| **Saved views** | Manage the view list, **Save the current camera**, **Start with** |
| **Mouse** | Orbit, pan and zoom speed; invert vertical orbit |
| **Grab PhysBones with the left mouse button** | Grab hair, tails and so on with the mouse (below) |

## Mouse and keyboard

| Input | What it does |
|---|---|
| Right drag | Orbit the camera |
| Wheel drag / Shift + right drag | Pan the camera |
| Wheel | Zoom |
| Double-click an empty area | Fit the whole avatar in view again |

These keys work while the Avatar Live window is in front. Keys that also work in games are set separately as [global hotkeys](10-settings.md#hotkeys--quick-actions).

| Key | What it does |
|---|---|
| **F1** | Clean view (hide / show the UI) |
| **Ctrl + 1 / 2 / 3** | Face / upper body / full body |
| **Ctrl + 4 … 9** | Saved views |
| **F** | Set the orbit center to the avatar |
| **Ctrl + = / −** | UI size |
| **Alt + Enter** | Fullscreen / window |
| **Esc** | Close menus, leave fullscreen |
| **Ctrl + Z / Ctrl + Y** | Undo / redo avatar and object placement |

## Clean view

Press **F1** to hide all UI, leaving only the background and avatar. Tracking and output continue. Press **F1** again to bring it back.

## Scene tools (left icons)

| Tool | What it does |
|---|---|
| **Camera** | Default mode |
| **Move / Rotate / Scale** | Change the avatar's position, direction and size in the view (right-click: reset only that value) |
| **Posing** (Pro) | Pick bones to create a pose ([Chapter 11](11-pro-features.md#posing)) |
| **⌂** | Move the avatar to the center |

## Grabbing PhysBones

You can grab swinging parts such as hair, ears and tails in the view with the mouse.

| Input | What it does |
|---|---|
| Left drag | Pull |
| Wheel while holding | Nearer / farther |
| Right-click while holding | **Pose** the bone in place |
| **Release posed bones** | Free the bones you posed |

A posed part stays posed until you grab that same part again.

Only parts whose PhysBone settings on the avatar allow grabbing can be grabbed.

## Window and tray

| Action | Result |
|---|---|
| Window **X** | Hide to the tray (the avatar and outputs keep running) |
| Double-click the tray icon | Open again |
| Right-click the tray icon | **Open Avatar Live** / **Open in clean view** / **Quit** |

## Screen size and theme

Change the UI size, light / dark theme and panel position in [Settings › UI](10-settings.md#ui).
