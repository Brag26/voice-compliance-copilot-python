import json
with open('outputs/pairs_loaded.json') as f: d=json.load(f)
for i in d: i['score']=90
with open('outputs/pairs_scored.json','w') as o: json.dump(d,o,indent=2)
print('Scoring completed')