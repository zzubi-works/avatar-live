# 3. Start screen and avatar library

## v2.0.0 avatar library: what selecting each option changes

![v45 avatar interface after loading](img/v45-menu.png)

- **Import .vavatar** registers a file exported using Exporter 1.0.6; it does not read your Unity project directly. **Import .vrm** opens supported VRM 0.x/1.0 files, although some unsupported shaders will not render.
- **Recent / Folder / Imported** change which library group is shown. They do not activate a camera or change tracking.
- **Default / Last used / Ask every time** decide which avatar loads automatically at startup. Ask every time is useful if different streams use different characters.
- **Start webcam/microphone automatically** can occupy devices immediately. If another app needs the camera, turn this startup behavior off and enable the device only when needed.
- Switching avatars restores **that avatar's** saved faces, poses and editor-camera presets; it does not silently copy every previous avatar profile to the new one.
- **Multi avatar (Pro)** adds multiple characters in the same studio rather than replacing the only character. Select the actor you intend to edit or drive.

**Important session distinction:** Your library's source avatars stay on your PC. The [remote session's](09-output.md) **Send my avatar data** switch requires separate consent and uses session-only encrypted temporary caching on participating PCs. It does not automatically install the other participant's original model into your permanent library.

## Start screen

![Start screen](img/launcher.png)

| Item | What it does |
|---|---|
| **Open Avatar…** | Opens a `.vavatar` file. You can also drag and drop it onto the window. |
| **Recent · Folder · Imported** | Shows avatars you opened recently, avatars in your avatar folder, and avatars you've imported. |
| **Set as default** | Makes Avatar Live start right away with this avatar. |
| **Camera · Microphone** | Choose the devices to turn on at start. |
| **Face · Hands** | Choose how tracking works. |
| **Startup** | Choose from Ask every time · Last used · Default avatar. |
| **▶ Start Avatar Live** | Starts with the avatar you chose. |

> 💡 Hold **Shift** while launching to start safely without the webcam and microphone. Try this when a device problem keeps Avatar Live from starting smoothly.

## Switching avatars while running

<div class="shot" markdown="1">

![Avatar library](img/avatar-pop.png)

- Click the **avatar name** at the top left to open the library.
- Click an avatar in the list to switch to it.
- Use **Add an avatar file…** to bring in a new avatar.
- A webcam and microphone you had turned on stay on after you switch.

</div>

## Opening a menu for the first time

Menus are prepared while the avatar loads, reducing the delay when opening each menu for the first time. Initial loading may take a little longer. The top-left logo returns to avatar selection without restarting the program.

## Returning to the start screen

Click the **logo** at the top left and choose **Restart**.
