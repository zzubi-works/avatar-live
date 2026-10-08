"""Builds the AVATAR LIVE website into docs/ (GitHub Pages serves main:/docs).

    uv run --no-project --with markdown --with pillow python build.py

content/<lang>/home.json      -> docs/<lang>/index.html          (the product homepage)
content/<lang>/<page>.md      -> docs/<lang>/<page>.html         (the guide and the legal pages)
shots/<shots>/<name>.png      -> docs/assets/shots/<lang>/<name>[-960].webp
shots/common/<name>.png       -> docs/assets/shots/common/<name>[-960].webp
assets/                       -> docs/assets/ (styles, script, brand, video)
"""
import html
import json
import os
import re
import shutil

import markdown
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")
SHOTS = os.path.join(ROOT, "shots")
BASE = "https://zzubi-works.github.io/avatar-live"
BOOTH = "https://curiousbobby.booth.pm/items/8953441"
X_URL = "https://x.com/User_Not_Online"
UPDATED = "2026-10-09"

LANGS = {
    "ko": {"name": "한국어", "html": "ko", "shots": "ko", "locale": "ko_KR", "preconnect": ["https://cdn.jsdelivr.net"], "font": "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css"},
    "en": {"name": "English", "html": "en", "shots": "en", "locale": "en_US", "preconnect": ["https://cdn.jsdelivr.net"], "font": "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css"},
    "ja": {"name": "日本語", "html": "ja", "shots": "ja", "locale": "ja_JP", "preconnect": ["https://cdn.jsdelivr.net"], "font": "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/packages/pretendard-jp/dist/web/variable/pretendardvariable-jp-dynamic-subset.min.css"},
    "zh": {"name": "简体中文", "html": "zh-Hans", "shots": "zh-Hans", "locale": "zh_CN", "preconnect": ["https://fonts.googleapis.com", "https://fonts.gstatic.com"], "font": "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&display=swap"},
}
GUIDE = ["01-getting-started", "02-avatar-exporter", "03-launcher-and-library", "04-main-window", "05-avatar-menu",
         "06-devices", "07-motion", "08-scene", "09-output", "10-settings", "11-pro-features", "12-troubleshooting",
         "13-license"]
LEGAL = ["legal-terms", "legal-privacy", "legal-refund", "legal-seller"]

CHROME = {
    "ko": {"guide": "가이드", "legal": "약관 · 정책", "toc": "이 페이지", "prev": "이전", "next": "다음", "updated": "최종 업데이트",
           "docsmenu": "가이드 목차", "home": "홈", "skip": "본문으로 건너뛰기", "booth": "BOOTH", "x": "X (Twitter)",
           "rights": "© 2026 Curious Bobby Co. All rights reserved.",
           "disclaimer": "AVATAR LIVE는 VRChat Inc.의 공식 제품이 아니며, VRChat Inc.와 제휴 관계가 없습니다. VRChat은 VRChat Inc.의 상표입니다.",
           "pick": "언어를 선택하세요"},
    "en": {"guide": "Guide", "legal": "Legal", "toc": "On this page", "prev": "Previous", "next": "Next", "updated": "Last updated",
           "docsmenu": "Guide contents", "home": "Home", "skip": "Skip to content", "booth": "BOOTH", "x": "X (Twitter)",
           "rights": "© 2026 Curious Bobby Co. All rights reserved.",
           "disclaimer": "AVATAR LIVE is not an official product of VRChat Inc. and is not affiliated with VRChat Inc. VRChat is a trademark of VRChat Inc.",
           "pick": "Choose a language"},
    "ja": {"guide": "ガイド", "legal": "規約・ポリシー", "toc": "このページ", "prev": "前へ", "next": "次へ", "updated": "最終更新",
           "docsmenu": "ガイド目次", "home": "ホーム", "skip": "本文へスキップ", "booth": "BOOTH", "x": "X (Twitter)",
           "rights": "© 2026 Curious Bobby Co. All rights reserved.",
           "disclaimer": "AVATAR LIVE は VRChat Inc. の公式製品ではなく、VRChat Inc. とは提携していません。VRChat は VRChat Inc. の商標です。",
           "pick": "言語を選択"},
    "zh": {"guide": "指南", "legal": "条款与政策", "toc": "本页内容", "prev": "上一页", "next": "下一页", "updated": "最后更新",
           "docsmenu": "指南目录", "home": "首页", "skip": "跳到正文", "booth": "BOOTH", "x": "X (Twitter)",
           "rights": "© 2026 Curious Bobby Co. All rights reserved.",
           "disclaimer": "AVATAR LIVE 不是 VRChat Inc. 的官方产品，与 VRChat Inc. 无关联。VRChat 是 VRChat Inc. 的商标。",
           "pick": "选择语言"},
}

ICON = {
    "sun": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    "moon": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a7 7 0 1 0 10.5 10.5z"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "close": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    "x": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7l10 10M17 7L7 17"/></svg>',
    "chev": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    "book": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5zM4 5.5v16"/></svg>',
}


def esc(s):
    return html.escape(str(s), quote=True)


def slug(text):
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


# ---------------------------------------------------------------- images ----

IMAGES = {}  # "<folder>/<name>" -> (width, height)


def build_images():
    for lang, L in LANGS.items():
        convert(os.path.join(SHOTS, L["shots"]), lang)
    convert(os.path.join(SHOTS, "common"), "common")


def convert(src, folder):
    dst = os.path.join(OUT, "assets", "shots", folder)
    os.makedirs(dst, exist_ok=True)
    if not os.path.isdir(src):
        return
    for f in sorted(os.listdir(src)):
        if not f.endswith(".png"):
            continue
        name = f[:-4]
        im = Image.open(os.path.join(src, f)).convert("RGB")
        im.save(os.path.join(dst, name + ".webp"), "WEBP", quality=84, method=6)
        if im.width > 1000:
            small = im.resize((960, round(im.height * 960 / im.width)), Image.LANCZOS)
            small.save(os.path.join(dst, name + "-960.webp"), "WEBP", quality=82, method=6)
        IMAGES[folder + "/" + name] = im.size


def img_tag(folder, name, alt, cls="", eager=False, sizes="(max-width: 900px) 100vw, 860px"):
    key = folder + "/" + name
    if key not in IMAGES:
        raise SystemExit("missing image " + key)
    w, h = IMAGES[key]
    src = "../assets/shots/%s/%s.webp" % (folder, name)
    srcset = ""
    if w > 1000:
        srcset = ' srcset="../assets/shots/%s/%s-960.webp 960w, %s %dw" sizes="%s"' % (folder, name, src, w, sizes)
    return '<img%s src="%s"%s width="%d" height="%d" alt="%s" %s decoding="async">' % (
        ' class="%s"' % cls if cls else "", src, srcset, w, h, esc(alt), 'fetchpriority="high"' if eager else 'loading="lazy"')


def poster_size(name):
    with Image.open(os.path.join(ROOT, "assets", "video", name + ".jpg")) as im:
        return im.size


def media(spec, lang, alt="", eager=False, sizes="(max-width: 900px) 100vw, 640px"):
    kind, _, value = spec.partition(":")
    if kind == "img":
        return img_tag(lang, value, alt, eager=eager, sizes=sizes)
    if kind == "common":
        return img_tag("common", value, alt, eager=eager, sizes=sizes)
    if kind == "video":
        w, h = poster_size(value)
        return ('<video class="lazyvideo" muted loop playsinline preload="none" controls poster="../assets/video/%s.jpg" width="%d" height="%d" aria-label="%s">'
                '<source src="../assets/video/%s.mp4" type="video/mp4"></video>') % (value, w, h, esc(alt), value)
    if kind == "gallery":
        cells = "".join('<div class="cell">%s</div>' % img_tag("common", n, alt, sizes="(max-width: 900px) 50vw, 320px") for n in value.split(","))
        return '<div class="mosaic">%s</div>' % cells
    raise SystemExit("unknown media " + spec)


# ----------------------------------------------------------------- pages ----

def read_md(lang, name):
    path = os.path.join(ROOT, "content", lang, name + ".md")
    if not os.path.exists(path):
        return None
    text = open(path, encoding="utf-8").read()
    h = re.search(r"^# (.+)$", text, re.M)
    return (h.group(1).strip() if h else name), text


def nav_title(title):
    return re.sub(r"^\d+\.\s*", "", title)


def render_md(lang, text):
    text = re.sub(r"\]\(([\w\-]+)\.md(#[^)]*)?\)", lambda m: "](" + m.group(1) + ".html" + (m.group(2) or "") + ")", text)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])
    body = md.convert(text)
    toc, seen = [], {}

    def add_id(m):
        level, inner = m.group(1), m.group(2)
        s = slug(html.unescape(inner))
        if s in seen:
            seen[s] += 1
            s = "%s-%d" % (s, seen[s])
        else:
            seen[s] = 0
        if level == "2":
            toc.append((re.sub(r"<[^>]+>", "", inner), s))
        return '<h%s id="%s">%s<a class="anchor" href="#%s" aria-hidden="true" tabindex="-1">#</a></h%s>' % (level, s, inner, s, level)

    body = re.sub(r"<h([1-4])>(.*?)</h\1>", add_id, body)

    def figure(m):
        alt, src = html.unescape(m.group(1)), m.group(2)
        mm = re.match(r"img/(common/)?([\w\-]+)\.png$", src)
        if not mm:
            raise SystemExit("bad image " + src)
        folder = "common" if mm.group(1) else lang
        return '<figure>%s<figcaption>%s</figcaption></figure>' % (img_tag(folder, mm.group(2), alt), esc(alt))

    body = re.sub(r'<p><img alt="([^"]*)" src="([^"]+)" ?/?></p>', figure, body)
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    body = re.sub(r"<blockquote>\s*<p>(💡|🔒|⚠️)\s*", lambda m: '<blockquote class="callout %s"><p>' % {"💡": "tip", "🔒": "privacy", "⚠️": "warn"}[m.group(1)], body)
    return body, toc


def head(lang, title, desc, page, og, extra=""):
    L = LANGS[lang]
    pre = "".join('<link rel="preconnect" href="%s" crossorigin>' % u for u in L["preconnect"])
    alts = "".join('<link rel="alternate" hreflang="%s" href="%s/%s/%s">' % (LANGS[k]["html"], BASE, k, page) for k in LANGS)
    alts += '<link rel="alternate" hreflang="x-default" href="%s/">' % BASE
    return """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{base}/{code}/{page}">
{alts}
<meta property="og:type" content="website">
<meta property="og:site_name" content="AVATAR LIVE">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{base}/{code}/{page}">
<meta property="og:image" content="{base}/assets/brand/{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{locale}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0b0f">
<link rel="icon" href="../assets/brand/favicon.png">
{pre}
<link rel="stylesheet" href="{font}">
<link rel="stylesheet" href="../assets/site.css">
<script>try{{var t=localStorage.getItem('al-theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
<script src="../assets/site.js" defer></script>{extra}
</head>""".format(lang=L["html"], title=esc(title), desc=esc(desc), base=BASE, code=lang, page=page, alts=alts,
                  og=og, font=L["font"], locale=L["locale"], pre=pre, extra=extra)


def header(lang, page, home, is_home):
    C = CHROME[lang]
    n = home["nav"]
    pre = "" if is_home else "index.html"
    links = [("#overview", n["overview"]), ("#features", n["features"]), ("#how", n["how"]), ("#editions", n["editions"])]
    navl = "".join('<a href="%s%s">%s</a>' % (pre, h, esc(t)) for h, t in links)
    navl += '<a href="01-getting-started.html"%s>%s</a>' % (' aria-current="page"' if not is_home else "", esc(n["docs"]))
    langs = "".join('<a href="../%s/%s" lang="%s"%s>%s</a>' % (k, page, LANGS[k]["html"], ' aria-current="true"' if k == lang else "", v["name"])
                    for k, v in LANGS.items())
    return """<a class="skip" href="#main">{skip}</a>
<header class="site-header" data-header>
  <div class="bar">
    <a class="brand" href="index.html" aria-label="AVATAR LIVE"><img src="../assets/brand/icon-64.png" width="28" height="28" alt=""><span>AVATAR LIVE</span></a>
    <nav class="primary" aria-label="Primary">{nav}</nav>
    <div class="tools">
      <details class="lang"><summary aria-label="{language}">{globe}<span>{langname}</span></summary><div class="lang-menu" role="menu">{langs}</div></details>
      <button class="icon-btn theme-toggle" type="button" aria-label="{theme}" data-theme-toggle>{sun}{moon}</button>
      <a class="btn btn-primary btn-sm get" href="{booth}">{get}</a>
      <button class="icon-btn menu-toggle" type="button" aria-label="{menu}" aria-expanded="false" aria-controls="mobile-nav" data-menu-toggle>{menuicon}{close}</button>
    </div>
  </div>
  <div class="mobile-nav" id="mobile-nav" hidden>{nav}<a class="btn btn-primary" href="{booth}">{get}</a></div>
</header>""".format(skip=esc(C["skip"]), nav=navl, language=esc(n["language"]), globe=ICON["globe"], langname=LANGS[lang]["name"],
                    langs=langs, theme=esc(n["theme"]), sun=ICON["sun"], moon=ICON["moon"], booth=BOOTH, get=esc(n["get"]),
                    menu=esc(n["menu"]), menuicon=ICON["menu"], close=ICON["close"])


def footer(lang, home, titles):
    C = CHROME[lang]
    n, f = home["nav"], home["footer"]
    col = lambda title, items: '<div class="fcol"><h2>%s</h2><ul>%s</ul></div>' % (esc(title), "".join('<li><a href="%s">%s</a></li>' % (h, esc(t)) for h, t in items))
    product = [("index.html#features", n["features"]), ("index.html#how", n["how"]), ("index.html#editions", n["editions"]), (BOOTH, C["booth"])]
    docs = [(p + ".html", nav_title(titles[p])) for p in ["01-getting-started", "02-avatar-exporter", "12-troubleshooting", "13-license"] if p in titles]
    legal = [(p + ".html", nav_title(titles[p])) for p in LEGAL if p in titles]
    links = [(BOOTH, C["booth"]), (X_URL, C["x"]), ("https://github.com/zzubi-works/avatar-live", "GitHub")]
    return """<footer class="site-footer">
  <div class="wrap">
    <div class="fbrand"><a class="brand" href="index.html"><img src="../assets/brand/icon-64.png" width="28" height="28" alt=""><span>AVATAR LIVE</span></a><p>Curious Bobby Co.</p></div>
    {cols}
  </div>
  <div class="wrap fine"><p>{disc}</p><p>{rights}</p></div>
</footer>""".format(cols=col(f["product"], product) + col(f["docs"], docs) + col(f["legal"], legal) + col(f["links"], links),
                    disc=esc(C["disclaimer"]), rights=esc(C["rights"]))


def product_data(lang, home):
    """schema.org data for the homepage: the app and its two editions at their BOOTH prices."""
    data = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "AVATAR LIVE",
            "operatingSystem": "Windows 10, Windows 11", "applicationCategory": "MultimediaApplication",
            "description": home["meta"]["description"], "url": "%s/%s/index.html" % (BASE, lang),
            "image": "%s/assets/brand/og-%s.jpg" % (BASE, lang), "inLanguage": LANGS[lang]["html"],
            "publisher": {"@type": "Organization", "name": "Curious Bobby Co."},
            "offers": [{"@type": "Offer", "name": "AVATAR LIVE " + p["name"], "price": re.sub(r"\D", "", p["price"]),
                        "priceCurrency": "JPY", "url": BOOTH} for p in home["editions"]["plans"]]}
    return '\n<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


def page_shell(lang, page, title, desc, home, titles, body, is_home, og):
    return "%s\n<body class=\"%s\">\n%s\n%s\n%s\n</body>\n</html>\n" % (
        head(lang, title, desc, page, og, product_data(lang, home) if is_home else ""), "home" if is_home else "doc",
        header(lang, page, home, is_home), body, footer(lang, home, titles))


# ------------------------------------------------------------------ home ----

def home_page(lang, h, titles):
    C = CHROME[lang]
    hero, feat, how, sc, cmp_, ed, faq, cta = h["hero"], h["features"], h["how"], h["showcase"], h["compare"], h["editions"], h["faq"], h["cta"]
    sub = "<br>".join(esc(x) for x in hero["sub"].split("\n"))
    out = []
    out.append("""<main id="main">
<section class="hero" id="overview">
  <div class="wrap hero-copy">
    <p class="eyebrow"><span class="dot"></span>{eyebrow}</p>
    <h1><span>{t1}</span><span class="grad">{t2}</span></h1>
    <p class="lead">{sub}</p>
    <div class="cta-row"><a class="btn btn-primary btn-lg" href="{booth}">{primary}{arrow}</a><a class="btn btn-ghost btn-lg" href="#features">{secondary}</a></div>
    <p class="meta">{meta}</p>
  </div>
  <div class="wrap">
    <figure class="product">
      <div class="frame">
        <div class="frame-bar"><span></span><span></span><span></span><em>AVATAR LIVE</em></div>
        <video class="hero-video" autoplay muted loop playsinline preload="auto" poster="../assets/video/hero.jpg" width="1280" height="720" aria-label="{caption}"><source src="../assets/video/hero.mp4" type="video/mp4"></video>
      </div>
      <figcaption>{caption}</figcaption>
    </figure>
  </div>
</section>""".format(eyebrow=esc(hero["eyebrow"]), t1=esc(hero["title"][0]), t2=esc(hero["title"][1]), sub=sub, booth=BOOTH,
                     primary=esc(hero["primary"]), arrow=ICON["arrow"], secondary=esc(hero["secondary"]), meta=esc(hero["meta"]),
                     caption=esc(hero["caption"])))
    out.append('<section class="works"><div class="wrap"><p>%s</p><ul>%s</ul></div></section>' % (
        esc(h["works"]["label"]), "".join("<li>%s</li>" % esc(x) for x in h["works"]["items"])))
    cards = []
    for i, it in enumerate(feat["items"]):
        cards.append('<article class="bento-card %s reveal"><div class="bento-media">%s</div><div class="bento-text"><h3>%s</h3><p>%s</p></div></article>' % (
            esc(it.get("size", "")), media(it["media"], lang, it["title"]), esc(it["title"]), esc(it["body"])))
    out.append("""<section class="section" id="features"><div class="wrap">
  <header class="section-head reveal"><p class="kicker">{k}</p><h2>{t}</h2><p>{s}</p></header>
  <div class="bento">{cards}</div>
</div></section>""".format(k=esc(feat["kicker"]), t=esc(feat["title"]), s=esc(feat["sub"]), cards="".join(cards)))
    steps = "".join('<li class="step reveal"><span class="num">%d</span><h3>%s</h3><p>%s</p></li>' % (i + 1, esc(s["title"]), esc(s["body"])) for i, s in enumerate(how["steps"]))
    out.append("""<section class="section how" id="how"><div class="wrap">
  <header class="section-head reveal"><p class="kicker">{k}</p><h2>{t}</h2></header>
  <ol class="steps-line">{steps}</ol>
  <p class="how-note reveal">{note} <a href="02-avatar-exporter.html">{link}{arrow}</a></p>
</div></section>""".format(k=esc(how["kicker"]), t=esc(how["title"]), steps=steps, note=esc(how["note"]), link=esc(how["link"]), arrow=ICON["arrow"]))
    rows = []
    for i, r in enumerate(sc["rows"]):
        pts = "".join("<li>%s%s</li>" % (ICON["check"], esc(p)) for p in r["points"])
        rows.append("""<article class="show-row{flip} reveal">
  <div class="show-media">{media}</div>
  <div class="show-text"><h3>{t}</h3><p>{b}</p><ul class="points">{pts}</ul><a class="more" href="{page}.html">{more}{arrow}</a></div>
</article>""".format(flip=" flip" if i % 2 else "", media=media(r["media"], lang, r["title"], sizes="(max-width: 900px) 100vw, 680px"),
                     t=esc(r["title"]), b=esc(r["body"]), pts=pts, page=r["page"], more=esc(sc["more"]), arrow=ICON["arrow"]))
    out.append("""<section class="section" id="showcase"><div class="wrap">
  <header class="section-head reveal"><p class="kicker">{k}</p><h2>{t}</h2></header>
  {rows}
</div></section>""".format(k=esc(sc["kicker"]), t=esc(sc["title"]), rows="".join(rows)))
    crow = "".join('<div class="crow"><span class="clabel">%s</span><span class="cleft">%s%s</span><span class="cright">%s%s</span></div>' % (
        esc(r["label"]), ICON["x"], esc(r["left"]), ICON["check"], esc(r["right"])) for r in cmp_["rows"])
    out.append("""<section class="section compare" id="compare"><div class="wrap">
  <header class="section-head reveal"><p class="kicker">{k}</p><h2>{t}</h2></header>
  <div class="ctable reveal" role="table"><div class="chead"><span></span><span class="cleft">{l}<small>{ln}</small></span><span class="cright">{r}</span></div>{rows}</div>
  <p class="foot reveal">{foot}</p>
</div></section>""".format(k=esc(cmp_["kicker"]), t=esc(cmp_["title"]), l=esc(cmp_["left"]), ln=esc(cmp_["leftNote"]), r=esc(cmp_["right"]), rows=crow, foot=esc(cmp_["foot"])))
    plans = []
    for p in ed["plans"]:
        feats = "".join("<li>%s%s</li>" % (ICON["check"], esc(x)) for x in p["features"])
        plans.append("""<article class="plan{hl} reveal">
  <header><h3>{n}</h3>{badge}<p class="for">{f}</p></header>
  <p class="price">{price}</p>
  <ul>{feats}</ul>
  <a class="btn {btn} btn-block" href="{booth}">{cta}</a>
</article>""".format(hl=" highlight" if p.get("badge") else "", n=esc(p["name"]), badge='<span class="badge">%s</span>' % esc(p["badge"]) if p.get("badge") else "",
                     f=esc(p["for"]), price=esc(p["price"]), feats=feats, btn="btn-primary" if p.get("badge") else "btn-ghost", booth=BOOTH, cta=esc(p["cta"])))
    out.append("""<section class="section editions" id="editions"><div class="wrap">
  <header class="section-head reveal"><p class="kicker">{k}</p><h2>{t}</h2><p>{s}</p></header>
  <div class="plans">{plans}</div>
  <p class="upgrade reveal">{up}</p>
  <p class="fineprint reveal">{note} <a href="legal-refund.html">{nl}</a></p>
</div></section>""".format(k=esc(ed["kicker"]), t=esc(ed["title"]), s=esc(ed["sub"]), plans="".join(plans), up=esc(ed["upgrade"]), note=esc(ed["note"]), nl=esc(ed["noteLink"])))
    qa = "".join('<details class="qa reveal"><summary><span>%s</span>%s</summary><div class="a"><p>%s</p></div></details>' % (esc(x["q"]), ICON["chev"], esc(x["a"])) for x in faq["items"])
    out.append("""<section class="section faq" id="faq"><div class="wrap narrow">
  <header class="section-head reveal"><p class="kicker">{k}</p><h2>{t}</h2></header>
  {qa}
</div></section>""".format(k=esc(faq["kicker"]), t=esc(faq["title"]), qa=qa))
    out.append("""<section class="final-cta"><div class="wrap reveal">
  <h2>{t}</h2><p>{s}</p>
  <div class="cta-row"><a class="btn btn-primary btn-lg" href="{booth}">{p}{arrow}</a><a class="btn btn-ghost btn-lg" href="01-getting-started.html">{book}{sec}</a></div>
</div></section>
</main>""".format(t=esc(cta["title"]), s=esc(cta["sub"]), booth=BOOTH, p=esc(cta["primary"]), arrow=ICON["arrow"], book=ICON["book"], sec=esc(cta["secondary"])))
    return "\n".join(out)


# ------------------------------------------------------------------ docs ----

def doc_page(lang, name, title, body, toc, titles):
    C = CHROME[lang]
    side = ['<p class="side-h">%s</p><ul>' % esc(C["guide"])]
    for p in GUIDE:
        if p in titles:
            side.append('<li><a href="%s.html"%s>%s</a></li>' % (p, ' aria-current="page"' if p == name else "", esc(nav_title(titles[p]))))
    side.append('</ul><p class="side-h">%s</p><ul>' % esc(C["legal"]))
    for p in LEGAL:
        if p in titles:
            side.append('<li><a href="%s.html"%s>%s</a></li>' % (p, ' aria-current="page"' if p == name else "", esc(nav_title(titles[p]))))
    side.append("</ul>")
    seq = [p for p in GUIDE + LEGAL if p in titles]
    i = seq.index(name)
    prev_, next_ = (seq[i - 1] if i > 0 else None), (seq[i + 1] if i + 1 < len(seq) else None)
    pager = '<nav class="pager" aria-label="Pager">%s%s</nav>' % (
        '<a class="prev" href="%s.html"><span>%s</span>%s</a>' % (prev_, esc(C["prev"]), esc(nav_title(titles[prev_]))) if prev_ else "<span></span>",
        '<a class="next" href="%s.html"><span>%s</span>%s</a>' % (next_, esc(C["next"]), esc(nav_title(titles[next_]))) if next_ else "<span></span>")
    toc_html = ""
    if len(toc) > 1:
        toc_html = '<nav class="toc" aria-label="%s"><p class="toc-h">%s</p><ul>%s</ul></nav>' % (
            esc(C["toc"]), esc(C["toc"]), "".join('<li><a href="#%s">%s</a></li>' % (s, esc(t)) for t, s in toc))
    return """<div class="docs">
  <button class="docs-menu-btn" type="button" aria-expanded="false" aria-controls="docs-side" data-docs-toggle>{menu}{label}</button>
  <aside class="docs-side" id="docs-side"><nav aria-label="{label}">{side}</nav></aside>
  <main id="main" class="docs-main"><article class="prose">{body}</article>{pager}<p class="updated">{upd}: {date}</p></main>
  {toc}
</div>""".format(menu=ICON["menu"], label=esc(C["docsmenu"]), side="".join(side), body=body, pager=pager, upd=esc(C["updated"]),
                 date=UPDATED, toc=toc_html)


# ----------------------------------------------------------------- build ----

ROOT_INDEX = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>AVATAR LIVE</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" href="assets/brand/favicon.png">
<link rel="canonical" href="{base}/">
{alts}
<script>
var l=(navigator.languages&&navigator.languages[0]||navigator.language||'en').toLowerCase();
var t=l.indexOf('ko')==0?'ko':l.indexOf('ja')==0?'ja':l.indexOf('zh')==0?'zh':'en';
location.replace(t+'/index.html');
</script>
<style>body{{background:#0b0b0f;color:#ededf2;font:16px/1.6 system-ui,sans-serif;display:grid;place-items:center;min-height:100vh;margin:0}}a{{color:#a99bff;margin:0 10px}}</style>
</head><body><p><a href="ko/index.html">한국어</a><a href="en/index.html">English</a><a href="ja/index.html">日本語</a><a href="zh/index.html">简体中文</a></p></body></html>
"""


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    build_images()
    urls = []
    for lang in LANGS:
        home = json.load(open(os.path.join(ROOT, "content", lang, "home.json"), encoding="utf-8"))
        titles, pages = {}, {}
        for name in GUIDE + LEGAL:
            r = read_md(lang, name)
            if r:
                titles[name], pages[name] = r[0], r
        os.makedirs(os.path.join(OUT, lang), exist_ok=True)
        og = "og-%s.jpg" % lang
        write(os.path.join(OUT, lang, "index.html"),
              page_shell(lang, "index.html", home["meta"]["title"], home["meta"]["description"], home, titles,
                         home_page(lang, home, titles), True, og))
        urls.append("%s/%s/index.html" % (BASE, lang))
        for name, (title, text) in pages.items():
            body, toc = render_md(lang, text)
            first = re.sub(r"<[^>]+>", "", re.search(r"<p>(.*?)</p>", body, re.S).group(1)) if "<p>" in body else nav_title(title)
            desc = (first[:150] + "…") if len(first) > 150 else first
            write(os.path.join(OUT, lang, name + ".html"),
                  page_shell(lang, name + ".html", "%s — AVATAR LIVE" % nav_title(title), desc, home, titles,
                             doc_page(lang, name, title, body, toc, titles), False, og))
            urls.append("%s/%s/%s.html" % (BASE, lang, name))
    alts = "".join('<link rel="alternate" hreflang="%s" href="%s/%s/index.html">' % (LANGS[k]["html"], BASE, k) for k in LANGS)
    write(os.path.join(OUT, "index.html"), ROOT_INDEX.format(base=BASE, alts=alts))
    write(os.path.join(OUT, "404.html"), ROOT_INDEX.format(base=BASE, alts=alts).replace("location.replace(t+'/index.html');", ""))
    write(os.path.join(OUT, "sitemap.xml"), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join("<url><loc>%s</loc><lastmod>%s</lastmod></url>\n" % (u, UPDATED) for u in urls) + "</urlset>\n")
    write(os.path.join(OUT, "robots.txt"), "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % BASE)
    write(os.path.join(OUT, ".nojekyll"), "")
    print("built %d pages, %d images" % (len(urls), len(IMAGES)))


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
