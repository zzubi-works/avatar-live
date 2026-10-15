"""Check that every localized Avatar Live guide has the Korean source structure.

Run: python check_guide_parity.py
The Korean Markdown under content/ko is the canonical guide.
"""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parent/'content'
LANGS=('en','ja','zh')
DOCS=sorted(path.name for path in (ROOT/'ko').glob('[0-9][0-9]-*.md'))
HEAD=re.compile(r'^(#{1,6})\s+(.+)',re.M)
IMG=re.compile(r'!\[[^]]*\]\(([^)]+)\)')
LINK=re.compile(r'(?<!!)\[[^]]+\]\(([^)]+)\)')
def structure(value):
    headings=[len(m.group(1)) for m in HEAD.finditer(value)]
    return {
      'headings':headings,
      'image_paths':IMG.findall(value),
      'table_rows':sum(line.startswith('|') for line in value.splitlines()),
      'details_blocks':value.count('<details'),
      'effect_pairs':value.count('class="effect-pair"'),
      'external_links':sorted(u for u in LINK.findall(value) if u.startswith('http')),
      'relative_page_links':[u.split('#')[0] for u in LINK.findall(value) if u.split('#')[0].endswith('.md')],
    }
def main():
    total=0
    for language in LANGS:
        all_pages=sorted(p.name for p in (ROOT/language).glob('[0-9][0-9]-*.md'))
        if all_pages!=DOCS:
            print(f'{language}: wrong pages. Missing={sorted(set(DOCS)-set(all_pages))} Extra={sorted(set(all_pages)-set(DOCS))}')
            total+=1
        for name in DOCS:
            path=ROOT/language/name
            if not path.is_file():continue
            source=structure((ROOT/'ko'/name).read_text(encoding='utf-8'))
            local=structure(path.read_text(encoding='utf-8'))
            for key,value in source.items():
                if value!=local[key]:
                    print(f'{language}/{name} {key} mismatch: KO={str(value)[:160]} target={str(local[key])[:160]}')
                    total+=1
    print(f'Checked {len(DOCS)} canonical guide pages x {len(LANGS)} languages; {total} parity mismatches.')
    return int(bool(total))
if __name__=='__main__':sys.exit(main())
