"""Check that every localized page uses the current Korean guide screenshots.

Run after building the website: python check_site_images.py

The English, Japanese, and Chinese text is translated independently, but until
new localized captures are approved, all languages must show the same Korean
screenshots rather than older locale-specific UI screenshots.
"""
from pathlib import Path
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
            if actual != expected:
                print(f"{lang}/{name}: screenshots differ from Korean canonical page")
                errors += 1

            for folder, filename in set(actual):
                if folder not in ("ko", "common"):
                    print(f"{lang}/{name}: outdated locale image {folder}/{filename}")
                    errors += 1
                elif not (ROOT / "assets" / "shots" / folder / filename).is_file():
                    print(f"{lang}/{name}: missing image {folder}/{filename}")
                    errors += 1

    print(f"Checked {len(canonical_pages)} pages x {len(LANGUAGES)} languages; {errors} screenshot problems.")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
