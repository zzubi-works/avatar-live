# 5. Avatar menu

## what each avatar menu control really changes

![The avatar menu](img/v45-menu.png)

| Control | Effect and how to use it |
|---|---|
| Toggle | First press enables a parameter, second disables it. Typical outfit and accessory visibility depends on the avatar creator's Animator wiring. |
| Button (while pressed) | Activates only while held and returns after release. This is intentionally different from a toggle. |
| Radial | Adjusts a continuous 0–100% value. It could control expression weight, clothing movement or another parameter defined by the avatar creator; halfway sends an intermediate value. |
| Two/Four-Axis Puppet | Moves two or four parameter directions together. The centre is the neutral value; the extremes and axes depend on the avatar's original configuration. |
| Sub Menu | Opens more controls belonging to the same avatar, not another actor. |
| Favorite / Quick Action | Another way to trigger an existing action without navigating nested menus; it does not create a new parameter. |
| Hold / Toggle hotkey | Hold works only while the key is down; Toggle remains active until the next press. Global hotkeys can work over another app, so avoid game conflicts. |

Hand gestures can be different for each hand. Automatic finger input from a webcam, VMC gloves or SteamVR controllers can override a manually selected gesture. If it keeps switching back, check [finger tracking sources](06-devices.md) and [automatic expressions](07-motion.md).

My Expressions and Pose library are saved per avatar. A static .anim applies fixed shape-key values; a multi-frame .anim changes them over time according to its animation/loop settings. Saved poses can independently allow or block Face, Head, Arms, Fingers and Torso tracking, enabling a fixed body pose with a moving face.

You use your avatar's Expressions menu from VRChat just as it is. Outfit and hair toggles, expression buttons, Radials and Puppets all work exactly as they do in VRChat.

## Expressions menu

<div class="shot" markdown="1">

![Avatar menu](img/menu.png)

- Toggle — Switches on and off each time you press it.
- Button — Stays on while you hold it.
- Sub Menu — Opens a submenu. Use Back to return.
- Radial · Puppet — Set a value with a slider or a pad.

</div>

## Right-clicking an item

<div class="shot" markdown="1">

![Item right-click menu](img/menu-ctx.png)

- Add to Quick Actions — Places it as a button on the bottom toolbar.
- Set hotkey… — Lets you turn it on with a single key, even while you're in a game.
- Favorite — Use it right away from the top of the menu.

</div>

## Hand gestures

<div class="shot" markdown="1">

![Hand gestures](img/gestures.png)

- Choose left-hand and right-hand gestures to show the avatar's gesture expressions.
- Turn on Gestures from the webcam's hands, and your own hand shapes become the gestures.

</div>

## Card order, saved poses and My expressions

![Saved poses in the Avatar Menu](img/menu-poses.png)

Click headings for Poses, My expressions and Hand gestures to expand their cards. Drag card headings to reorder the cards, and drag individual saved pose or expression tiles to rearrange them.

![My expressions in the Avatar Menu](img/menu-myexpr.png)

- Click a pose to apply or remove it. The camera icon beside it expands its per-pose tracking switches.
- Facial, head, arms, fingers and body tracking can be enabled independently. For example, you can hold the head still while tracking facial expressions.
- The built-in Sitting pose holds the hips and legs while initially allowing all five tracking parts.
- Right-click tiles for available actions such as hotkeys, duplication or Quick Actions.
- Create expression and Import .anim are available in both Studio and Avatar Menu. Multi-frame clips follow their original loop setting.

## Reset to defaults

Click Avatar parameters › Reset to defaults to return the menu values to the avatar's defaults. Values that are saved, such as outfit state, carry over to the next launch.

## Quick Actions

Turn actions you use often into buttons or keys. You can add menu items, gestures, camera views, lighting presets and more, and right-click a button to change its name and position.

## Hierarchy · Meshes · Shape keys

View your avatar's objects as a tree, just like in Unity, and change them right there.

- Hierarchy — Shows the avatar's objects as a tree. Use the checkboxes to turn them on and off. The eye icon hides an object from view while leaving it on.
- Meshes — Shows every mesh in one list. Use search to find one quickly.
- Click a mesh to adjust its shape keys one by one in the side panel. Values you set yourself take priority over face tracking and avatar animations.
- Reset all at the top returns every mesh to the avatar's original state, and Collapse all closes the tree.

## Reset

| | Reset | Reset everything |
|---|---|---|
| What it does | Returns tracking, hand poses and PhysBones to their initial state | All of that, plus outfits · position · camera, back to their initial state |
| How | ⟲ at the top | Right-click ⟲, or Settings › General |
