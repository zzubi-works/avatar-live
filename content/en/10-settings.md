# 10. Settings

## performance, interface and update settings

![Settings](img/v45-settings.png)

| Setting | What it actually changes |
|---|---|
| App FPS cap | Higher refreshes view/physics more often at a CPU/GPU cost; lower saves power but makes motion less fluid. Broadcast output has its own FPS limit. |
| Render quality/resolution | Higher improves hair and outline detail at a GPU cost. Scene-view window size and broadcast image resolution may be different. |
| Shadows/post-effects | Disabling them reduces rendering load, but depth and film effects become flatter. Studio-owned effects can vary per saved scene. |
| Window size / Always on top | Changes the Windows app window, not the pixel dimensions of the OBS Spout2/NDI sender. |
| Close-button behavior | X can quit or minimise to tray; active output may continue when minimised. |
| UI scaling | Makes labels and controls larger or smaller. At very high scaling, narrow windows need more scrolling. |
| Quick-toolbar opacity | Higher makes idle camera controls easier to see; lower leaves more of the character unobstructed. |
| Automatic update downloads | Downloads available updates for later installation. Even when off, startup can check and notify you of new versions. |
| Send diagnostics | Used after the user chooses to send a report; include the steps leading to the issue rather than assuming all logs are uploaded automatically. |

Hotkeys may work when the program is in the background. Select combinations that do not conflict with game controls. An expression can work while held or as press to toggle. F13–F24 and modifiers are supported; basic hotkeys can also be triggered by devices such as Stream Deck.

Remember the scope of each setting: pose/expressions/saved editor camera views are typically per-avatar; room/studio lights/broadcast studio cameras are saved per studio; a selected hardware microphone or webcam may need updating when Windows devices change.

## General · Window · Performance

<div class="shot" markdown="1">

![Settings page](img/settings.png)

- Open the menu at start — Turn it off to start without the menu.
- Window — Set the window size, full screen, always on top, and what the X button does.
- Performance — Set the frame rate and image quality. Lowering them puts less load on your PC.
- Shadows — The shadows that the hair and chin cast on the neck and chest. Turning them off puts less load on the GPU.
- Language — 한국어 · English · 日本語 · 简体中文
- UI — Change the theme, panel position and text size.

</div>

## Search menus and settings

![Global menu search](img/settings-search.png)

Use the magnifying glass at the top-right to search for AFK, Mirror, Language, Spout2, eye gaze, desk mode or hotkeys. A result opens the matching Menu, Devices, Motion, Studio, Output or Settings page and expands the relevant cards. AFK timing results navigate to Motion › Body rather than its old Settings location.

## Hotkeys

<div class="shot" markdown="1">

![Hotkeys](img/hotkeys.png)

- Click + Add a hotkey, then choose an action and a key.
- Hotkeys work even while you're in a game or Avatar Live is in the background.
- Your key presses still reach other programs as usual.
- For menu buttons and gestures, you can choose While held or Press to switch.

</div>

## License

Check your current edition.

| Button | What it does |
|---|---|
| Enter another code | Switches to another license. |
| Upgrade to Pro | Enter the upgrade you bought on BOOTH to switch to Pro. |
| Check now | Checks the license again. |

## Diagnostics · About · Updates

| Item | What it does |
|---|---|
| Diagnostics › Send an error report | When something goes wrong, sends a description and the logs. It is sent only when you click it. |
| About › Send a suggestion | Sends a feature you'd like to have or something you'd like us to fix. |
| Notices | New notices are shown once at start-up, and you can look at past notices again in Settings. |
| Open log folder | Lets you look at the log files. |
| Check now · Download | Checks for a new version and downloads it. |
| Restart to install | Updates right away. Your avatars and settings stay as they are. |

> Avatar Live checks for updates once at every launch and shows a green indicator when a newer version is available. Turn on Settings › Updates › Auto-download updates to download automatically. Installation follows the separate Install when quitting option or Restart to install button. You can also get the new version from BOOTH; existing avatars and settings are preserved.

## Automatic update checks and downloading

![Update settings](img/settings-updates.png)

Avatar Live checks for a newer release once whenever the app starts. Disabling automatic downloading does not disable the version check or update notification. From the Update settings, you can check or download manually and install after restarting or when quitting. Existing avatars and saved settings are preserved.

## Send an error report

![Diagnostics and error report](img/settings-diagnostics.png)

If you experience a bug, open Settings › Diagnostics › Send error report. Include what you were doing when the problem occurred; the diagnostic data and reproduction steps are much more useful than a general message.

## Sending problems and suggestions

- If you run into a bug or problem while using Avatar Live, please let us know with Settings › Diagnostics › Send an error report. A line or two about what was happening helps us a great deal in finding the cause.
- If there's a feature or improvement you need, please send it with Settings › About › Send a suggestion. We take your feedback into account when planning updates.
