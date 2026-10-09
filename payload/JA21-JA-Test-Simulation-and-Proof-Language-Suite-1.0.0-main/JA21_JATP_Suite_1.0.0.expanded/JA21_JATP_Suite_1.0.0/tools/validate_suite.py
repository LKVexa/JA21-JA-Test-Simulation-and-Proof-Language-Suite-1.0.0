#!/usr/bin/env python3
import csv,gzip,hashlib,json,sys,re
from collections import Counter
from pathlib import Path
root=Path(sys.argv[1] if len(sys.argv)>1 else '.')
def sh(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
corpus=root/'corpus/technical/JA21_JATP_TECHNICAL_CORPUS_10000.jsonl.gz'
rows=[]
with gzip.open(corpus,'rt',encoding='utf-8') as f:
 for line in f: rows.append(json.loads(line))
assert len(rows)==10000 and len({r['record_id'] for r in rows})==10000
assert [r['sequence'] for r in rows]==list(range(1,10001))
assert all(sh(r['source'])==r['ast']['origin_hash'] for r in rows)
scripts=list((root/'scripts').rglob('*.jap')); assert len(scripts)==1000
with (root/'catalogs/SCRIPT_CATALOG.csv').open(encoding='utf-8',newline='') as f: cat=list(csv.DictReader(f))
assert len(cat)==1000
assert Counter(x['level'] for x in cat)==Counter({x:100 for x in ['beginner','intermediate','advanced','expert','compiler','runtime','optimization','validation','certification','deployment']})
assert Counter(x['validation_class'] for x in cat)==Counter({'positive':400,'negative':150,'boundary':100,'integration':100,'security':75,'performance':50,'determinism':50,'interoperability':25,'recovery':25,'certification':25})
assert len({x['feature'] for x in cat})==32
for x in cat:
 p=root/x['file']; assert p.exists(); text=p.read_text(encoding='utf-8')
 assert sh(text)==x['source_sha256']
 assert 'ja source 0.3' in text and '\nmodule ' in text and '\nuse Proof' in text and '\npolicy ' in text and '\nemit mcrt ' in text
 assert text.count('{')==text.count('}')
book=(root/'textbook/JA21_JA_TEST_SIMULATION_PROOF_LANGUAGE_TEXTBOOK.md').read_text(encoding='utf-8')
chap=len(re.findall(r'^# Chapter \d+:',book,re.M)); assert chap==22
mx=max(len(p.relative_to(root).as_posix()) for p in root.rglob('*'))
print(json.dumps({'records':len(rows),'scripts':len(scripts),'catalog_rows':len(cat),'features':len({x['feature'] for x in cat}),'textbook_chapters':chap,'max_relative_path':mx},indent=2))
