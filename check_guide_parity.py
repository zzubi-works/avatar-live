"""Check guide structure and the homepage's currently supported avatar formats.

Run: python check_guide_parity.py
The Korean Markdown under content/ko is the canonical guide.
"""
from pathlib import Path
import json
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
    # 홈페이지 FAQ는 가이드 본문과 별도 JSON이라 문서 구조 검사만으로는
    # VRM 지원 여부가 예전 문구로 되돌아가는 실수를 발견할 수 없다.
    for language in ('ko', *LANGS):
        home=json.loads((ROOT/language/'home.json').read_text(encoding='utf-8'))
        note=home['how']['note']
        items=home['faq']['items']
        vrm_answer=next((item['a'] for item in items if 'VRM' in item['q']), '')
        unity_answer=next((item['a'] for item in items if 'Unity' in item['q']), '')
        direct={'ko':'직접', 'en':'directly', 'ja':'直接', 'zh':'直接'}[language]
        expectations={
          'VRM FAQ':(vrm_answer, ('VRM', '0.x', '1.0', direct)),
          'Unity FAQ':(unity_answer, ('VRM', '.vavatar', 'Unity')),
          'setup note':(note, ('VRM', '0.x', '1.0', '.vavatar', '.vrca', 'Unity')),
        }
        for section,(text,required) in expectations.items():
            if not all(term in text for term in required):
                print(f'{language}/home.json {section}: stale or incomplete avatar-format information')
                total+=1
    # The pages the guide folded into others keep their old addresses in every language.
    folded=sorted(json.loads((ROOT/'ko'/'redirects.json').read_text(encoding='utf-8')))
    for language in LANGS:
        local=sorted(json.loads((ROOT/language/'redirects.json').read_text(encoding='utf-8')))
        if local!=folded:
            print(f'{language}/redirects.json: wrong old pages. Missing={sorted(set(folded)-set(local))} Extra={sorted(set(local)-set(folded))}')
            total+=1
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
    print(f'Checked {len(DOCS)} canonical guide pages x {len(LANGS)} languages and four homepages; {total} mismatches.')
    return int(bool(total))
if __name__=='__main__':sys.exit(main())
