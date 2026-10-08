# 2. Exporting your avatar

You make avatar files for Avatar Live (`.vavatar`) by installing **Curious Bobby - Avatar Exporter** in your avatar's Unity project.

## Before you start

- A Unity **2022.3.22f1** avatar project
- An avatar that uploads to VRChat normally
- Avatars that use NDMF, Modular Avatar, VRCFury and similar tools can be exported as they are, too.

## Installation

Add the repository to **VCC / ALCOM**, then add **Curious Bobby - Avatar Exporter** to your avatar project.

```text
https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json
```

If you downloaded the `.unitypackage`, import it in Unity with **Assets → Import Package → Custom Package…**.

## Exporting

1. In the Unity menu, open **Curious Bobby → Avatar Exporter**.
2. Put the avatar you want to export in the **Avatar** field.
3. Click **Export .vavatar**.
4. When it's done, click **Show file** to see the file that was created.

| Item | What it does |
|---|---|
| **Name in Avatar Live** | The name shown in Avatar Live |
| **Expression clips (optional)** | Adds extra expression animations for use in [Automatic expressions](11-pro-features.md#automatic-expressions) |
| **Output folder** | Where the file is saved |

> 💡 If exporting doesn't go well, please first check that the avatar uploads to VRChat normally.

## When you change your avatar

After making changes in Unity, just export it again. Per-avatar settings such as lighting, camera, face adjustment and outfit state carry over.

- Your original avatar and scene are not changed.
- The files you create are saved only on your PC and are not uploaded anywhere.
