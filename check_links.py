"""Checks content/<lang>/: every relative link in the Markdown, every homepage "page" and every old page's redirect target
points at an existing page and an existing heading anchor.

    python check_links.py ko
"""
import glob
import json
import os
import re
import sys

lang = sys.argv[1]
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", lang)


def slug(h):
    h = re.sub(r"<[^>]+>", "", h).strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def ids(text):
    """The heading ids build.py gives a page: a repeated heading gets -1, -2."""
    seen, out = {}, set()
    for m in re.finditer(r"^#{1,6} (.+)$", text, re.M):
        s = slug(m.group(1))
        if s in seen:
            seen[s] += 1
            s = "%s-%d" % (s, seen[s])
        else:
            seen[s] = 0
        out.add(s)
    return out


anchors = {}
for f in glob.glob(d + "/*.md"):
    anchors[os.path.basename(f)] = ids(re.sub(r"```.*?```", "", open(f, encoding="utf-8").read(), flags=re.S))
bad = 0


def check(where, page, anc):
    global bad
    if page not in anchors:
        print("MISSING PAGE", where, page)
        bad += 1
    elif anc and anc not in anchors[page]:
        print("BAD ANCHOR", where, page + "#" + anc)
        bad += 1


for f in glob.glob(d + "/*.md"):
    for m in re.finditer(r"\]\(([^)\s]+)\)", open(f, encoding="utf-8").read()):
        t = m.group(1)
        if t.startswith("http") or t.startswith("img/"):
            continue
        path, _, anc = t.partition("#")
        check(os.path.basename(f), path or os.path.basename(f), anc)
home = json.load(open(os.path.join(d, "home.json"), encoding="utf-8"))
for spec in [home["how"]["page"]] + [r["page"] for r in home["showcase"]["rows"]] + [r["page"] for r in home["broadcast"]["items"]]:
    page, _, anc = spec.partition("#")
    check("home.json", page + ".md", anc)
check("home.json discordAnchor", "09-broadcast.md", home["broadcast"]["discordAnchor"])
for old, target in json.load(open(os.path.join(d, "redirects.json"), encoding="utf-8")).items():
    if os.path.exists(os.path.join(d, old + ".md")):
        print("REDIRECT OVER A PAGE", old)
        bad += 1
    for spec in [target["to"]] + list(target["anchors"].values()):
        page, _, anc = spec.partition("#")
        check("redirects.json " + old, page + ".md", anc)
print("problems:", bad)
