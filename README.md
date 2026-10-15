# AVATAR LIVE — Website

Product site and user guide for **AVATAR LIVE** by Curious Bobby Co.

**→ https://zzubi-works.github.io/avatar-live/**

한국어 · English · 日本語 · 简体中文

- Purchase: https://curiousbobby.booth.pm/items/8953441
- This repository contains only the website. AVATAR LIVE itself is proprietary software.

## Build

```
uv run --no-project --with markdown --with pillow python build.py
```

- `content/<lang>/home.json` → `docs/<lang>/index.html` (homepage)
- `content/<lang>/*.md` → `docs/<lang>/*.html` (guide and legal pages)
- `assets/` → `docs/assets/` (styles, script, brand images, videos)
- `python check_links.py <lang>` checks the guide's links and anchors.
- `python check_site_images.py` verifies matching screenshot coverage, each
  language's own UI photos, and referenced image files. It rejects Korean UI
  copied into a translated guide.
- `python check_guide_parity.py` verifies that all 15 English, Japanese and
  Simplified Chinese guide chapters match the **Korean canonical guide** in
  heading structure, tables, screenshots and navigational links. It also checks
  all four homepages for VRM import support, Unity requirements and .vrca
  incompatibility. Run it whenever guides or supported features change.
- `make_og.py` redraws the share images (`assets/brand/og-<lang>.jpg`).

GitHub Pages serves `main:/docs`.

Homepage and guide UI screenshots use the corresponding app language and are
served from `docs/assets/shots/<lang>/`. All languages use the reviewed Main
avatar/studio and ordinary standing poses. Text-free renders, including the ten
effect comparisons, can be shared; UI photos must be captured in each language.

When refreshing screenshots from a working directory with older local PNGs,
use `python build.py --shots-prefix guide-` to convert only the new guide
captures and preserve the other committed WebP images.

## Guide capture and review

- `tools/capture_guide.py`: asks a development player's local control channel
  to open real UI sections and save screenshots. It does not activate a window
  or send desktop mouse/keyboard input. Always use an isolated copy of the
  chosen avatar/studio profile. PNG sources stay in the ignored `shots/` folder.
- `tools/capture_effect_examples.py --studio-file <isolated.studio.json>`:
  renders effect comparisons and restores the serialized effect settings.
- `tools/capture_localized_guides.py --profile <capture-profile> --worktree
  <runtime-worktree> --player <frozen-development-player.exe>`: photographs
  English, Japanese and Chinese menus in minimized players, using isolated
  profile copies. It disables automatic download and installation on quit.
  Use a frozen development-player copy so the source build stays intact.
- `tools/verify_site.cjs <output-directory>`: checks all four languages
  at desktop, tablet and mobile sizes in headless Edge. It requires Playwright
  and writes its screenshots and JSON results outside the published site.

See [the guide refresh record](reports/guide-refresh-20261015.md) for scope,
capture provenance and validation.
