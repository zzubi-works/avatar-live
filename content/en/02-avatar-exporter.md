# 2. Exporting an avatar (Avatar Exporter)

Avatar Live opens avatars as **`.vavatar`** files. You make this file by installing **Curious Bobby - Avatar Exporter** in the Unity project of your VRChat avatar.

- Your original avatar, scenes and materials are not changed.
- The Exporter does not upload anything to the internet.
- The `.vavatar` files you make belong to you. However, the rights to the avatar and outfits inside them belong to their respective creators.

## Requirements

| Item | Details |
|---|---|
| Unity | **2022.3** |
| Avatar | **An avatar project that uploads to VRChat normally** |
| Creation tools | Avatars made with NDMF, Modular Avatar, VRCFury and similar tools can also be exported (these tools are not included in the Exporter; the ones installed in your project are used) |

## Installation

### VCC / ALCOM (recommended)

1. Add the repository to VCC or ALCOM.
   - `vcc://vpm/addRepo?url=https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json`
   - Or add the URL directly: `https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json`
2. Add **Curious Bobby - Avatar Exporter** to your avatar project.

### .unitypackage

In Unity, import it with **Assets → Import Package → Custom Package…**.

Once installed, **Curious Bobby** appears in Unity's top menu.

## Exporting

1. Open **Curious Bobby → Avatar Exporter**.
2. Put the avatar to export in the **Avatar** field.
3. Check **Name in Avatar Live**.
4. Change the **Output folder** if needed.
5. Click **Export .vavatar**.
6. When the file name appears under **Result**, you are done. **Show file** opens it in Explorer.

| Item | What it does |
|---|---|
| **Avatar** | The avatar to export |
| **Avatars in the open scenes** | Choose one when the scene has several avatars |
| **Name in Avatar Live** | The name shown in Avatar Live |
| **Expression clips (optional)** | Add extra expression animations for use in [Automatic expressions](11-pro-features.md#automatic-expressions) |
| **Output folder** | Where the `.vavatar` is saved |
| **Export .vavatar** | Create the file |

> If an export fails, first check that the avatar uploads to VRChat normally.

## Opening it in Avatar Live

- **Open Avatar…** on the start screen, or **drag and drop** the file onto the window
- Put it in the **Avatar folder** (by default `Documents\Avatar Live\Avatars`) and it appears on the start screen automatically
- While running, click the avatar name at the top left → **Add an avatar file…**

## When you change the avatar

After editing it in Unity, just **export again**. Per-avatar settings (lighting, camera, face adjustment, outfit state and so on) are kept.

- "It was made by a newer exporter" → update Avatar Live.
- If it says the format is old → export again with the latest Exporter.
- Non-humanoid avatars can use the menu and expressions, but not body tracking.
