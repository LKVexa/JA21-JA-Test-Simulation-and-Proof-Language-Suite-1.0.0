#!/usr/bin/env python3
import argparse,gzip,json,collections
p=argparse.ArgumentParser(); p.add_argument('corpus'); p.add_argument('--feature'); p.add_argument('--level'); p.add_argument('--class-name'); a=p.parse_args()
counts=collections.Counter(); shown=0
with gzip.open(a.corpus,'rt',encoding='utf-8') as f:
 for line in f:
  r=json.loads(line); counts[(r['level'],r['validation_class'],r['feature'])]+=1
  if (not a.feature or r['feature']==a.feature) and (not a.level or r['level']==a.level) and (not a.class_name or r['validation_class']==a.class_name) and shown<10:
   print(r['record_id'],r['level'],r['validation_class'],r['feature'],r['validation_result']['expected_status']); shown+=1
print('records',sum(counts.values()),'groups',len(counts))
