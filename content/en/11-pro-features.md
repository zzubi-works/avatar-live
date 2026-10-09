# 11. Posing · Objects · Expressions

| Feature | Edition |
|---|---|
| [Posing](#posing) | Pro |
| [Pose library](#pose-library) | Pro |
| [Objects](#objects) | Pro |
| [More screen share sources](#more-screen-share-sources) | Pro |
| [My expressions](#my-expressions) | Basic · Pro |
| [Automatic expressions](#automatic-expressions) | Basic · Pro |

## Posing

![Posing mode](img/posing.png)

Turn on **Scene › Posing › Posing mode** to create a pose by moving the bones directly.

- Click a bone to select it, and drag a ring to rotate it. The rotation gizmo is sized to fit the bone.
- Drag a hand or foot, and the whole arm or leg follows. Use **Alt+drag** to change which way the elbow or knee points.
- **Symmetry** — Move one side, and the other side moves with it. Use **Left / right** to flip the pose or copy one side to the other.
- **Face camera** · **Feet on floor** — Turn the face toward the camera, and line the feet up with the floor.
- **Lock** — Tracking and animations don't move the bones you lock.
- Save the pose with **Done**, and turn it on right away from the **Poses** card in the avatar menu. Even after **Discard**, you can bring it back with **Ctrl+Z**.
- **Standing rest** and **Sitting** poses are included from the start. The sitting pose changes only the hips and legs, and the head and arms keep tracking.
- You can set a pose you made as **Use as the desk pose (arms and hands)** or **Rest pose (whole body)**.

> 💡 Please save your pose before you turn off posing mode.

## Pose library

In **Scene › Posing › Pose library**, choose a folder that holds `.anim` files, and every pose is shown as a **thumbnail of your current avatar**.

- Subfolders are read too, and clips are sorted into poses, hand shapes and motions. You can use search and favorites.
- Click **Apply**, and the avatar takes that pose right away. Clips that move play as animations. Use **Release** to go back.
- Use **Edit** to fix it up in posing mode, then save it as a new pose.
- You can also load humanoid · bone `.anim` files made in Unity one at a time.

## Objects

![Objects](img/props.png)

Use **Scene › Objects › + Add object** to place text, images, shapes and 3D models.

- Set **Rides on** to the head or a hand, and the object moves with the avatar.
- Double-click text to edit it right there.
- For 3D models, create a `.vprop` file with **Curious Bobby → Prop Exporter** in Unity.

## More screen share sources

You can layer more windows or monitors onto your screen share. Use this when you'd like to show a chat window or a music player as well.

## My expressions

Create your own expressions from the avatar's shape keys.

1. Click **New expression**.
2. In the side panel, move the shape keys as if you were recording them to build the expression. Use **Preview** to sweep from a neutral face (0%) to the full expression (100%) and check it.
3. Click **Save**, and you can turn the expression on from the **My expressions** card in the avatar menu.

- You can also load expression animations made in Unity (`.anim` with shape keys). Clips that move play while the expression is on.

## Automatic expressions

When you smile or look surprised, an expression you've chosen appears automatically. Turn it on in **Motion › Automatic expressions**, and link an expression to show for each one, such as smile · surprise · wink.
