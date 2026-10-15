# Export avatar

Opening an avatar in a Unity project in Avatar Live`.vavatar`Create it as a file. already`.vavatar`me`.vrm`If there is a file[Open Avatar](03-launcher-and-library.md)Please skip to .

## Install Exporter

1. Add the below repositories to VCC or ALCOM.
2. Add Curious Bobby - Avatar Exporter to your avatar project.
3. Open the project in Unity.

```text
https://raw.githubusercontent.com/zzubi-works/avatar-exporter/main/index.json
```

`.unitypackage`If you received it as Unity’s Assets → Import Package → Custom Package… Taken from

## Create an avatar file

1. Open Curious Bobby → Avatar Exporter at the top of Unity.
2. Drag the Hierarchy's avatar into the avatar box.
3. Set a display name and save folder.
4. Click Export .vavatar.
5. Once complete, click View File to view the resulting file.
6. Load that file in Open Avatar in Avatar Live.

|item|What happens if I change it?|
|---|---|
|avatar|Select the character you want to export.|
|name to display|This will be the name you see in the list in Avatar Live.|
|facial expression clip|Includes the selected facial expression animation. You can export it even if you don't have it.|
|storage folder|completed`.vavatar`The folder in which to place the files.|
|Export .vavatar|Create a file with the avatar of your choice.|
|View files|Open the folder containing the completed file.|

## When modifying the avatar

In Unity, modify the clothing, hair, etc. and then export the same avatar again. Any changes to appearance will be reflected when you load a new file in Avatar Live.

## When export does not work

- Unity checks that there are no errors in the avatar itself.
- Check which authoring tool and exporter you are using and try exporting again.
- If the file exists, but some parts are pink or disappeared, check the material/shader of the original project and the on status of the corresponding parts.

The permitted scope for broadcasting and sharing of avatars, costumes, and props follows the terms and conditions of each producer.[Content Terms of Use](13-license.md#avatars-and-props)Check out .
