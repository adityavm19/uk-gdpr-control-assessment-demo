from pathlib import Path
import csv
from collections import Counter
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]

def read_csv(p):
    with open(p,newline='',encoding='utf-8') as f: return list(csv.DictReader(f))

controls=read_csv(ROOT/'02-assessment/article32-control-matrix.csv')
findings=read_csv(ROOT/'05-findings/findings-register.csv')
rems=read_csv(ROOT/'06-remediation/remediation-tracker.csv')
out=ROOT/'08-analytics'; out.mkdir(exist_ok=True)

coverage=Counter(r['conclusion'].split(' - ')[0] if ' - ' in r['conclusion'] else r['conclusion'] for r in controls)
# Use explicit effectiveness fields for stable labels
coverage=Counter('Effective' if r['operating_effectiveness']=='Effective' else 'Partially Effective' for r in controls)
fig,ax=plt.subplots(figsize=(7,4.2)); ax.bar(list(coverage.keys()), list(coverage.values())); ax.set_title('Article 32 control outcomes'); ax.set_ylabel('Controls'); ax.set_ylim(0,max(coverage.values())+2); fig.tight_layout(); fig.savefig(out/'article32-control-coverage.png',dpi=180); plt.close(fig)
sev=Counter(r['rating'] for r in findings); order=['Critical','High','Moderate','Low']; vals=[sev.get(k,0) for k in order]
fig,ax=plt.subplots(figsize=(7,4.2)); ax.bar(order,vals); ax.set_title('Findings by severity'); ax.set_ylabel('Findings'); ax.set_ylim(0,max(vals)+1); fig.tight_layout(); fig.savefig(out/'findings-by-severity.png',dpi=180); plt.close(fig)
stat=Counter(r['status'] for r in rems); fig,ax=plt.subplots(figsize=(7,4.2)); ax.bar(list(stat.keys()), list(stat.values())); ax.set_title('Remediation status'); ax.set_ylabel('Actions'); ax.set_ylim(0,max(stat.values())+1); fig.tight_layout(); fig.savefig(out/'remediation-status.png',dpi=180); plt.close(fig)
print({'controls':len(controls),'effective':coverage['Effective'],'partially_effective':coverage['Partially Effective'],'findings':len(findings),'severity':dict(sev),'remediation_status':dict(stat)})
