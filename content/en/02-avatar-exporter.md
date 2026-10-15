# 2. Exporting your avatar

## v2.0.0 · Exporter 1.0.6 versus direct VRM import

The steps differ for **Unity avatars (.vavatar)** and **VRM models (.vrm)**. Export an avatar from its Unity/VRChat project using **Curious Bobby - Avatar Exporter 1.0.6**; supported **VRM 0.x and 1.0** files can instead be opened directly in Avatar Live.

- **Unity setup:** Start from the avatar's Unity **2022.3.22f1** project with a compatible VRChat SDK. Select the model and choose **Export .vavatar**. Exporter 1.0.6 improves PhysBone/collider handling with VRChat SDK 3.10.5 and addresses some hair/accessory bones disabled by outfit merges.
- **Display name / expression clips / destination:** Name controls what appears in the app library, clips supply optional facial animations, and destination is where Windows writes the result. Exporting a file is not the same as registering it: open the new file in the app.
- **Re-exporting a model:** Changes to clothes, bones or materials require another export. The new geometry may affect previously saved pose, camera or expression positioning; verify it before broadcasting.
- **VRM models:** Direct import does not require the exporter. Some VRM 0.x models with unsupported shaders cannot load; renaming a file extension will not convert shaders.
- **Permission:** Making or possessing an avatar file never automatically grants distribution rights. Check every avatar, outfit, texture and prop license before enabling [remote avatar-data transfer](09-output.md).

If a body part is pink or disappears, inspect the shader/material and PhysBone/collider state in the Unity project, export again and explicitly reload the updated avatar file.

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
