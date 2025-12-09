import json
from pathlib import Path
with open('sample_data/pairs.json') as f: data=json.load(f)
Path('outputs').mkdir(exist_ok=True)
with open('outputs/pairs_loaded.json','w') as o: json.dump(data,o,indent=2)
print('Text demo loaded')