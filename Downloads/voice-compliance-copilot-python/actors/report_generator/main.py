import json
from jinja2 import Template
with open('outputs/pairs_scored.json') as f: d=json.load(f)
t=Template('<h1>Report</h1>{% for i in d %}<p>{{i.id}} {{i.score}}</p>{% endfor %}')
with open('outputs/report.html','w') as o:o.write(t.render(d=d))
print('Report generated')