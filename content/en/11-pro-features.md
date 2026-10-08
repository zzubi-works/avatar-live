# 11. Posing · Objects · Expressions

| Feature | Edition |
|---|---|
| [Posing](#posing) | **Pro** |
| [Objects](#objects) | **Pro** |
| [Screen share extra sources](#screen-share-extra-sources) | **Pro** |
| [My expressions](#my-expressions) | Basic · Pro |
| [Automatic expressions](#automatic-expressions) | Basic · Pro |

## Posing

Move bones directly to create avatar poses and save them.

**To start**: Scene › **Posing** › **Posing mode**, or the person icon in the scene tools on the left

| Input | What it does |
|---|---|
| Click a bone (Ctrl: several) | Select bones |
| Drag a bone | Move it (dragging a hand or foot moves the whole arm or leg) |
| Drag a ring | Rotate (Ctrl: 15° steps) |
| **Ctrl + Z / Ctrl + Y** | Undo / redo |
| **Back to normal** | Return the selected bones to the avatar's own motion |
| **Left / right** | Flip left and right · copy left side to right · copy right side to left |
| **Reset all** | Back to the initial pose |
| **Show finger bones** | Show the finger bones |

> Turning off posing mode releases the pose. Save it first.

### Poses

| Item | What it does |
|---|---|
| **+ Add pose** | **Save this pose** · **Import a .anim file…** · **Save as the desk pose (arms and hands)** |
| Click a pose | Apply / release |
| **Edit pose** | Edit a saved pose |
| **Rename / Overwrite with the current pose / Delete** | Manage poses |
| **Rest pose (whole body)** | Use this pose when your face is not visible |
| **Use as the desk pose (arms and hands)** | Use it as the desk hand pose |

You can also turn poses on and off with one button on the **Poses** card in the avatar menu.

## Objects

Attach text, images, shapes and 3D models to the scene or the avatar (a hat, text above the head, a chair, a desk and so on).

| Item | What it does |
|---|---|
| **Basic environment (floor grid)** | Show the floor |
| **+ Add object** | **Text** · **Picture file…** · **3D model (.vprop)…** · **Shape** (cube, sphere, cylinder, capsule, board) |
| Visibility switch · ⋯ | Hide; rename · duplicate · back to its first place · delete |
| **Color** | Change the color |
| **Rides on** | In the scene / Head / Chest / Torso / Left hand / Right hand |
| **Follow softly** | Follow the bone with a slight delay |
| **Keep proportions / Size** | Adjust the size |
| **Always in front / Face the camera** | How it is displayed |
| Text: **Font · Bold · Italic · Edge · Plate behind** | Style the text |

In the view, move objects with the scene tools (Move, Rotate, Scale). Double-click text to edit it right away.

### Making 3D models

In Unity, use **Curious Bobby → Prop Exporter** to export a GameObject or prefab as a **.vprop**. The model's swinging bones and animations work too.

## Screen share extra sources

Under Output › Screen share › **More sources**, layer more windows or monitors on top (a chat window, a music player and so on).

| Item | What it does |
|---|---|
| **Add source** | Add a window or display |
| 👁 | Show / hide |
| ⋯ | Bring forward · send back · back to the start · remove |

## My expressions

Create expressions yourself from the avatar's shape keys.

1. **New expression**
2. **Search shape keys** → add with **+** → adjust the weight
3. **While this expression shows**: No blinking · Pause eye tracking · Pause mouth tracking
4. **Save**

- With **Import .anim** you can also use expression animations made in Unity.
- Click them on the **My expressions** card in the avatar menu or the scene to turn them on and off.

## Automatic expressions

When you smile or look surprised, the avatar shows an expression you have chosen automatically.

| Item | What it does |
|---|---|
| **Automatic expressions** | On / off |
| Detected expressions | Smile · Surprise · Angry · Sad · Wink (left / right) · Pout · Sleepy |
| **Shows** | Link to one of My expressions, a gesture, an avatar menu item or an expression clip |
| **Threshold** | How clearly you must make the expression for it to turn on |
| **Timing** | Smoothing · Start after · Show at least |

**Expression clips** are the extra expressions you added when exporting with the Exporter ([Chapter 2](02-avatar-exporter.md#exporting)).
