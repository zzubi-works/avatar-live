"""Makes the share images (assets/brand/og-<lang>.jpg, 1200x630) and the header icon (assets/brand/icon-64.png).

    uv run --no-project --with pillow python make_og.py

The headline comes from content/<lang>/home.json (hero.title, hero.eyebrow); the picture is the key visual,
shots/common/keyvisual.png (the fox in the night alley, 2000x1125), cropped so the avatar stands right of the headline.
Fonts are the Windows system fonts for each script.
"""
import json
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
BRAND = os.path.join(ROOT, "assets", "brand")
FONTS = {
    "ko": (r"C:\Windows\Fonts\malgunbd.ttf", r"C:\Windows\Fonts\malgun.ttf"),
    "en": (r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\segoeui.ttf"),
    "ja": (r"C:\Windows\Fonts\YuGothB.ttc", r"C:\Windows\Fonts\YuGothM.ttc"),
    "zh": (r"C:\Windows\Fonts\msyhbd.ttc", r"C:\Windows\Fonts\msyh.ttc"),
}
W, H = 1200, 630
BG, TEXT, TEXT2, ACCENT = (11, 11, 15), (237, 237, 242), (163, 163, 178), (180, 168, 255)


def fit(path, text, size, width):
    while size > 20:
        font = ImageFont.truetype(path, size)
        if font.getlength(text) <= width:
            return font
        size -= 2
    return ImageFont.truetype(path, size)


def og(lang, visual, icon):
    home = json.load(open(os.path.join(ROOT, "content", lang, "home.json"), encoding="utf-8"))
    bold, regular = FONTS[lang]
    # a 1500x787 window of the key visual: the avatar (x 880-1240 of 2000) lands at 700-990 of 1200
    im = visual.crop((10, 0, 1510, 788)).resize((W, H), Image.LANCZOS)
    # the alley's left side darkens under the headline
    shade = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(shade)
    for x in range(W):
        t = x / W
        d.line((x, 0, x, H), fill=round(255 * (0.9 if t < 0.3 else max(0.0, 0.9 - (t - 0.3) * 4.5))))
    im.paste(Image.new("RGB", (W, H), BG), (0, 0), shade)
    x0 = 640
    draw = ImageDraw.Draw(im)
    # brand
    ic = icon.resize((52, 52), Image.LANCZOS)
    mask = Image.new("L", ic.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 51, 51), radius=13, fill=255)
    im.paste(ic, (72, 66), mask)
    draw.text((140, 92), "AVATAR LIVE", font=ImageFont.truetype(FONTS["en"][0], 26), fill=TEXT, anchor="lm")
    # headline
    t1, t2 = home["hero"]["title"]
    width = x0 - 72
    f1 = fit(bold, t1, 66, width)
    f2 = fit(bold, t2, 66, width)
    size = min(f1.size, f2.size)
    f = ImageFont.truetype(bold, size)
    y = 250
    draw.text((72, y), t1, font=f, fill=TEXT, anchor="ls")
    draw.text((72, y + round(size * 1.25)), t2, font=f, fill=ACCENT, anchor="ls")
    draw.text((72, y + round(size * 1.25) + 70), home["hero"]["eyebrow"], font=fit(regular, home["hero"]["eyebrow"], 26, width), fill=TEXT2, anchor="ls")
    draw.text((72, H - 64), "Windows 10 / 11  ·  BOOTH", font=ImageFont.truetype(FONTS["en"][1], 22), fill=(112, 112, 126), anchor="ls")
    im.save(os.path.join(BRAND, "og-%s.jpg" % lang), "JPEG", quality=88, optimize=True, progressive=True)
    print("og-%s.jpg" % lang, size)


def main():
    icon = Image.open(os.path.join(BRAND, "icon-256.png")).convert("RGBA")
    icon.resize((64, 64), Image.LANCZOS).save(os.path.join(BRAND, "icon-64.png"), optimize=True)
    visual = Image.open(os.path.join(ROOT, "shots", "common", "keyvisual.png")).convert("RGB")
    for lang in FONTS:
        if os.path.exists(os.path.join(ROOT, "content", lang, "home.json")):
            og(lang, visual, icon.convert("RGB"))


if __name__ == "__main__":
    main()
