"""Checks content/<lang>/*.md: every relative link points at an existing page and an existing heading anchor.

    python check_links.py ko
"""
import glob
import os
import re
import sys

lang = sys.argv[1]
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", lang)


def slug(h):
    h = re.sub(r"<[^>]+>", "", h).strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


anchors = {}
for f in glob.glob(d + "/*.md"):
    s = re.sub(r"```.*?```", "", open(f, encoding="utf-8").read(), flags=re.S)
    anchors[os.path.basename(f)] = {slug(m.group(1)) for m in re.finditer(r"^#{1,6} (.+)$", s, re.M)}
bad = 0
for f in glob.glob(d + "/*.md"):
    for m in re.finditer(r"\]\(([^)\s]+)\)", open(f, encoding="utf-8").read()):
        t = m.group(1)
        if t.startswith("http") or t.startswith("img/"):
            continue
        path, _, anc = t.partition("#")
        tgt = path or os.path.basename(f)
        if path and not os.path.exists(os.path.join(d, path)):
            print("MISSING PAGE", os.path.basename(f), t)
            bad += 1
        elif anc and anc not in anchors.get(tgt, set()):
            print("BAD ANCHOR", os.path.basename(f), t)
            bad += 1
print("problems:", bad)
