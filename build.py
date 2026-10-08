"""Builds the Avatar Live guide site: content/<lang>/*.md -> docs/<lang>/*.html (GitHub Pages serves docs/).

    uv run --no-project --with markdown --with pillow python build.py
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
SHOTS = os.path.join(ROOT, "shots")  # shots/<lang>/<name>.png (raw captures)
UPDATED = "2026-10-09"
# not published: the activation screen names what it accepts; fps/clean are not used
SKIP_SHOTS = {"activation", "fps", "clean"}

LANGS = {
    "ko": {"name": "한국어", "html": "ko", "shots": "ko"},
    "en": {"name": "English", "html": "en", "shots": "en"},
    "ja": {"name": "日本語", "html": "ja", "shots": "ja"},
    "zh": {"name": "简体中文", "html": "zh-Hans", "shots": "zh-Hans"},
}

PAGES = ["index", "01-getting-started", "02-avatar-exporter", "03-launcher-and-library", "04-main-window",
         "05-avatar-menu", "06-devices", "07-motion", "08-scene", "09-output", "10-settings", "11-pro-features",
         "12-troubleshooting", "13-license"]
LEGAL = ["legal-terms", "legal-privacy", "legal-refund", "legal-seller"]

UI = {
    "ko": {"guide": "가이드", "legal": "약관 · 정책", "buy": "BOOTH에서 구매", "home": "홈", "toc": "이 페이지",
           "updated": "최종 업데이트", "prev": "이전", "next": "다음", "menu": "메뉴", "theme": "테마",
           "rights": "© 2026 Curious Bobby Co. All rights reserved.",
           "disclaimer": "Avatar Live는 VRChat Inc.와 제휴하거나 승인받은 제품이 아닙니다. VRChat은 VRChat Inc.의 상표입니다."},
    "en": {"guide": "Guide", "legal": "Legal", "buy": "Buy on BOOTH", "home": "Home", "toc": "On this page",
           "updated": "Last updated", "prev": "Previous", "next": "Next", "menu": "Menu", "theme": "Theme",
           "rights": "© 2026 Curious Bobby Co. All rights reserved.",
           "disclaimer": "Avatar Live is not affiliated with or endorsed by VRChat Inc. VRChat is a trademark of VRChat Inc."},
    "ja": {"guide": "ガイド", "legal": "規約・ポリシー", "buy": "BOOTHで購入", "home": "ホーム", "toc": "このページ",
           "updated": "最終更新", "prev": "前へ", "next": "次へ", "menu": "メニュー", "theme": "テーマ",
           "rights": "© 2026 Curious Bobby Co. All rights reserved.",
           "disclaimer": "Avatar Live は VRChat Inc. と提携・承認関係にある製品ではありません。VRChat は VRChat Inc. の商標です。"},
    "zh": {"guide": "指南", "legal": "条款与政策", "buy": "在 BOOTH 购买", "home": "首页", "toc": "本页内容",
           "updated": "最后更新", "prev": "上一页", "next": "下一页", "menu": "菜单", "theme": "主题",
           "rights": "© 2026 Curious Bobby Co. All rights reserved.",
           "disclaimer": "Avatar Live 与 VRChat Inc. 无关联，也未获其认可。VRChat 是 VRChat Inc. 的商标。"},
}


def slug(text):
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def read_page(lang, name):
    path = os.path.join(ROOT, "content", lang, name + ".md")
    if not os.path.exists(path):
        return None
    text = open(path, encoding="utf-8").read()
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
        text = text[m.end():]
    title = meta.get("title")
    if not title:
        h = re.search(r"^# (.+)$", text, re.M)
        title = h.group(1).strip() if h else name
    return meta, title, text


def nav_title(title):
    return re.sub(r"^\d+\.\s*", "", title)


def render_md(lang, text):
    # links: foo.md#x -> foo.html#x ; images: img/x.png -> ../assets/shots/<lang>/x.webp
    text = re.sub(r"\]\(([\w\-]+)\.md(#[^)]*)?\)", lambda m: "](" + m.group(1) + ".html" + (m.group(2) or "") + ")", text)
    text = re.sub(r"(\]\(|src=\")img/([\w\-]+)\.png", lambda m: m.group(1) + "../assets/shots/" + lang + "/" + m.group(2) + ".webp", text)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"])
    body = md.convert(text)
    toc = []
    seen = {}

    def add_id(m):
        level, inner = m.group(1), m.group(2)
        s = slug(html.unescape(inner))
        if s in seen:
            seen[s] += 1
            s = "%s-%d" % (s, seen[s])
        else:
            seen[s] = 0
        if level in ("2", "3"):
            toc.append((int(level), re.sub(r"<[^>]+>", "", inner), s))
        return '<h%s id="%s">%s<a class="anchor" href="#%s">#</a></h%s>' % (level, s, inner, s, level)

    body = re.sub(r"<h([1-4])>(.*?)</h\1>", add_id, body)
    # images become figures that open full size
    body = re.sub(r'<p><img alt="([^"]*)" src="([^"]+)" ?/?></p>',
                  r'<figure><a href="\2" target="_blank" rel="noopener"><img alt="\1" src="\2" loading="lazy"></a><figcaption>\1</figcaption></figure>', body)
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    # callouts: > ⚠️ / > 💡 blockquotes
    body = re.sub(r"<blockquote>\s*<p>(⚠️|💡|🔒)", r'<blockquote class="callout"><p>\1', body)
    return body, toc


def fill(t, d):
    return re.sub(r"\{\{(\w+)\}\}", lambda m: str(d[m.group(1)]), t)


def esc(s):
    return html.escape(s, quote=True)


def page_html(lang, name, title, body, toc, titles, is_home):
    ui = UI[lang]
    L = LANGS[lang]
    order = [p for p in PAGES if p != "index"]
    side = ['<div class="side-h">%s</div><ul>' % ui["guide"]]
    for p in order:
        if p in titles:
            side.append('<li><a href="%s.html"%s>%s</a></li>' % (p, ' class="on"' if p == name else "", esc(nav_title(titles[p]))))
    side.append('</ul><div class="side-h">%s</div><ul>' % ui["legal"])
    for p in LEGAL:
        if p in titles:
            side.append('<li><a href="%s.html"%s>%s</a></li>' % (p, ' class="on"' if p == name else "", esc(nav_title(titles[p]))))
    side.append("</ul>")
    toc_html = ""
    if toc and not is_home:
        toc_html = '<nav class="toc"><div class="toc-h">%s</div><ul>%s</ul></nav>' % (
            ui["toc"], "".join('<li class="l%d"><a href="#%s">%s</a></li>' % (lv, s, esc(t)) for lv, t, s in toc))
    pager = ""
    seq = order + LEGAL
    if name in seq:
        i = seq.index(name)
        prev_ = seq[i - 1] if i > 0 else None
        next_ = seq[i + 1] if i + 1 < len(seq) else None
        pager = '<div class="pager">%s%s</div>' % (
            '<a class="prev" href="%s.html"><span>%s</span>%s</a>' % (prev_, ui["prev"], esc(nav_title(titles[prev_]))) if prev_ in titles else "<span></span>",
            '<a class="next" href="%s.html"><span>%s</span>%s</a>' % (next_, ui["next"], esc(nav_title(titles[next_]))) if next_ in titles else "<span></span>")
    langs = "".join('<a href="../%s/%s.html"%s>%s</a>' % (k, name, ' class="on"' if k == lang else "", v["name"]) for k, v in LANGS.items())
    legal_links = " · ".join('<a href="%s.html">%s</a>' % (p, esc(nav_title(titles[p]))) for p in LEGAL if p in titles)
    full_title = "Avatar Live" if is_home else "%s — Avatar Live" % nav_title(title)
    if is_home:
        full_title = "Avatar Live — " + re.sub(r"<[^>]+>", "", title)
    return fill(TEMPLATE, dict(
        lang=L["html"], title=esc(full_title), desc=esc(DESC[lang]), side="".join(side), body=body, toc=toc_html,
        pager=pager, langs=langs, buy=ui["buy"], home=ui["home"], updated=ui["updated"], date=UPDATED,
        rights=ui["rights"], disclaimer=ui["disclaimer"], legal_links=legal_links, menu=ui["menu"],
        bodyclass="home" if is_home else "doc", langname=L["name"]))


DESC = {
    "ko": "VRChat 아바타를 VRM 변환 없이 그대로 쓰는 Windows용 VTuber 소프트웨어 Avatar Live 공식 가이드",
    "en": "Official guide for Avatar Live — Windows VTuber software that uses your VRChat avatar as is, without VRM conversion.",
    "ja": "VRChat アバターを VRM 変換なしでそのまま使える Windows 用 VTuber ソフト Avatar Live の公式ガイド",
    "zh": "Avatar Live 官方指南 —— 无需转换为 VRM，直接使用 VRChat 模型的 Windows VTuber 软件",
}

TEMPLATE = open(os.path.join(ROOT, "template.html"), encoding="utf-8").read()


def shots():
    for lang, L in LANGS.items():
        src = os.path.join(SHOTS, L["shots"])
        dst = os.path.join(OUT, "assets", "shots", lang)
        os.makedirs(dst, exist_ok=True)
        if not os.path.isdir(src):
            continue
        for f in os.listdir(src):
            if f.endswith(".png") and f[:-4] not in SKIP_SHOTS:
                im = Image.open(os.path.join(src, f)).convert("RGB")
                im.save(os.path.join(dst, f[:-4] + ".webp"), "WEBP", quality=86, method=6)


def main():
    shutil.rmtree(os.path.join(OUT, "assets"), ignore_errors=True)
    if os.path.isdir(OUT):
        for item in os.listdir(OUT):
            if item != "assets":
                p = os.path.join(OUT, item)
                shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(OUT, exist_ok=True)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)
    shots()
    for lang in LANGS:
        titles = {}
        pages = {}
        for name in PAGES + LEGAL:
            r = read_page(lang, name)
            if r:
                pages[name] = r
                titles[name] = r[1]
        os.makedirs(os.path.join(OUT, lang), exist_ok=True)
        for name, (meta, title, text) in pages.items():
            body, toc = render_md(lang, text)
            open(os.path.join(OUT, lang, name + ".html"), "w", encoding="utf-8").write(
                page_html(lang, name, title, body, toc, titles, name == "index"))
    # root: pick a language
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(ROOT_INDEX)
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    print("built", sum(len(fs) for _, _, fs in os.walk(OUT)), "files")


ROOT_INDEX = """<!doctype html><html><head><meta charset="utf-8"><title>Avatar Live</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" href="assets/brand/favicon.png">
<script>
var l=(navigator.languages&&navigator.languages[0]||navigator.language||'en').toLowerCase();
var t=l.indexOf('ko')==0?'ko':l.indexOf('ja')==0?'ja':l.indexOf('zh')==0?'zh':'en';
location.replace(t+'/index.html');
</script></head><body>
<a href="ko/index.html">한국어</a> · <a href="en/index.html">English</a> · <a href="ja/index.html">日本語</a> · <a href="zh/index.html">简体中文</a>
</body></html>"""

if __name__ == "__main__":
    main()
