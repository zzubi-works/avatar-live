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
