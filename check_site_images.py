"""Check matching guide coverage with each language's actual UI photos.

Run after building the website: python check_site_images.py

Only common renders and the text-free effect comparisons may be shared.
"""
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parent / "docs"
LANGUAGES = ("en", "ja", "zh")
SHOTS = re.compile(r"\.\./assets/shots/([a-z]+)/([\w-]+\.webp)")


def image_refs(page):
    return SHOTS.findall(page.read_text(encoding="utf-8"))


def main():
    errors = 0
    canonical_pages = {page.name: image_refs(page) for page in (ROOT / "ko").glob("*.html")}

    for lang in LANGUAGES:
        pages = ROOT / lang
        for name, expected in canonical_pages.items():
            page = pages / name
            if not page.is_file():
                print(f"{lang}: missing page {name}")
                errors += 1
                continue

            actual = image_refs(page)
            localized = [(lang if folder == "ko" else folder, filename) for folder, filename in expected]
            if actual != localized:
                print(f"{lang}/{name}: wrong screenshot coverage or language folder")
                errors += 1

            for folder, filename in set(actual):
                if folder not in (lang, "common"):
                    print(f"{lang}/{name}: wrong UI language {folder}/{filename}")
                    errors += 1
                elif not (ROOT / "assets" / "shots" / folder / filename).is_file():
                    print(f"{lang}/{name}: missing image {folder}/{filename}")
                    errors += 1
                elif folder == lang and filename.startswith("guide-") and not filename.startswith("guide-example-"):
                    native = ROOT / "assets" / "shots" / folder / filename
                    korean = ROOT / "assets" / "shots" / "ko" / filename
                    if korean.is_file() and hashlib.sha256(native.read_bytes()).digest() == hashlib.sha256(korean.read_bytes()).digest():
                        print(f"{lang}/{name}: Korean UI was copied instead of captured: {filename}")
                        errors += 1

    print(f"Checked {len(canonical_pages)} pages x {len(LANGUAGES)} languages; {errors} screenshot problems.")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
