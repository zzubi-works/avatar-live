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
- Published website commit: `3c7ca20`. GitHub Pages reports `built` for that
  commit. Live Getting Started, Studio, Camera Effects, Remote Collaboration
  and Licensing pages returned HTTP 200 with the revised content. Five
  representative screenshot URLs also returned HTTP 200.
- Site-wide local page and asset references: 5,067 checked, none missing.

Primary third-party references checked on 2026-10-15:

- [NDI SDK licensing](https://docs.ndi.video/all/developing-with-ndi/sdk/licensing)
- [VB-CABLE](https://vb-audio.com/Cable/) and [VB-Audio licensing](https://vb-audio.com/Services/licensing.htm)
- [KlakSpout](https://github.com/keijiro/KlakSpout), [OBS Spout2 plugin](https://github.com/Off-World-Live/obs-spout2-plugin), [DistroAV](https://github.com/DistroAV/DistroAV)

## Screenshot correction after visual feedback

- Retook 17 existing screenshots and added a dedicated pose-tracking screenshot.
  The Main avatar and Main studio remain the source. Captures came from the
  exact development player, started minimized without activating its window;
  the capture player was closed after shooting.
- Removed the blown-out face and hair highlights by adjusting the isolated
  capture studio: exposure 1; fill light intensity 0.8 with neutral RGB 0.8;
  camera spot intensity 0.35 with its volumetric beam off; additional spot and
  back lights off. General screenshots have bloom, grading, DOF and the
  additional Beautify/HBAO effects off. The user's actual profile is untouched.
- Replaced the root avatar menu in all revised menu/overview captures with
  Expressions → Expression → Default (ordinary eye/face expression toggles).
  The root R18 tile no longer appears in these screenshots.
- Captured the entire real right-click popup, including Quick Action, shortcut,
  favorite, parameter information and order reset. The previous crop cut the
  popup off. The new frame includes its top-left location and the underlying
  expression buttons.
- Retook every effect comparison with the corrected lighting. Bloom example
  uses intensity 0.5, threshold 0.9 and diffusion 5, preserving face/hair detail.
- Cropped the pose menu to its complete pose/expression cards. The Pro guide
  now uses a separate photo showing the actual expanded per-part tracking
  switches in Studio → Posing.
- Rebuilt the site and visually reviewed the replacement frames. All 63
  headless layout/image checks (21 Korean pages at 1440/900/390 px) pass;
  Korean link/anchor checking reports zero problems. Local evidence is in
  `.local/verify/guide-clarity-20261015/site-review-retake` in the runtime workspace.
