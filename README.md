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
- `make_og.py` redraws the share images (`assets/brand/og-<lang>.jpg`).

GitHub Pages serves `main:/docs`.

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
- `tools/verify_site.cjs <output-directory>`: checks generated Korean pages
  at desktop, tablet and mobile sizes in headless Edge. It requires Playwright
  and writes its screenshots and JSON results outside the published site.

See [the guide refresh record](reports/guide-refresh-20261015.md) for scope,
capture provenance and validation.
