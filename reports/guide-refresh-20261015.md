# Guide refresh — 2026-10-15

The Korean guide was rewritten around the controls a new user sees, replacing
duplicated release-prefixed introductions, long paragraphs and development
details. Camera effects and remote sessions now have their own pages. The 2.0
release notes link to those instructions instead of duplicating them.

## Screenshots

- Source application: the user's existing v45 Windows build.
- Avatar: Main. Studio: Main.
- 83 distinct new photographs are referenced from the Korean pages. They show
  the actual open application controls, cropped at native resolution for
  legibility. Five effects have matching on/off render examples.
- The startup screen and camera settings use their actual dialogs, not a crop
  of a closed card. The session address is a documentation example and the
  pictured port matches the documented default, 47700.
- Following the user's request, capture ran through the development player's
  local control channel in a minimized, isolated instance, without moving the
  desktop pointer or repeatedly bringing windows to the front.
- Avatar bundles, personal profiles, credentials, camera video and model source
  files are not included in the website repository. The committed images are
  raster screenshots; PNG working sources remain local under `shots/`.

## Content and layout

- Removed literal Markdown emphasis markers from site content and rendering.
- Kept setting names intact in desktop tables. Two-column explanations stack
  as label-and-description rows on mobile; Basic/Pro comparisons show both
  editions together.
- Displayed control screenshots at their native size, on their own rows. Each
  screenshot links to its full image.
- Shortened Studio and Output page titles. Removed internal build names from
  user-facing guide captions and repeated version prefixes from guide copy.
- Corrected the AFK timing location to Menu → Default & AFK pose, verified in
  the actual build and the corresponding UI source.
- Remote sessions begin with hosting and joining. Port forwarding and firewall
  instructions appear under troubleshooting, collapsed until needed.
- Separated NDI, Spout2, VB-CABLE and third-party avatar/prop permissions.
  Third-party software terms and content permissions are distinct from the
  Avatar Live edition license. Updated the Korean content terms and privacy
  explanation to match optional session transfers.
- Kept the existing other-language guide material, with shared readability
  changes, simpler titles and separate third-party notices. The full rewrite
  and new Camera Effects / Remote Collaboration pages are Korean; language
  switching falls back to the corresponding existing chapter elsewhere.

## Validation

- Website build completes; new screenshot sources do not overwrite unrelated
  existing image assets.
- Markdown page links and heading anchors checked for Korean, English,
  Japanese and Simplified Chinese: no problems.
- Headless Edge checks all 21 Korean pages at 1440, 900 and 390 pixels wide:
  63 layout checks, no missing images, broken in-page anchors, raw emphasis
  markers, clipped setting names, page overflow or JavaScript errors.
- Desktop/mobile screenshots visually reviewed, including antialiasing,
  remote-session instructions and edition comparisons.
- Effect comparison captures verified to contain changed rendered pixels.
- Production publication is verified after pushing the committed site.

Primary third-party references checked on 2026-10-15:

- [NDI SDK licensing](https://docs.ndi.video/all/developing-with-ndi/sdk/licensing)
- [VB-CABLE](https://vb-audio.com/Cable/) and [VB-Audio licensing](https://vb-audio.com/Services/licensing.htm)
- [KlakSpout](https://github.com/keijiro/KlakSpout), [OBS Spout2 plugin](https://github.com/Off-World-Live/obs-spout2-plugin), [DistroAV](https://github.com/DistroAV/DistroAV)
