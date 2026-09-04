from pathlib import Path
import csv,json,hashlib,re,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]

def rows(p):
    with open(p,newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
controls=rows(ROOT/'02-assessment/article32-control-matrix.csv'); findings=rows(ROOT/'05-findings/findings-register.csv'); exc=rows(ROOT/'04-fieldwork/exception-register.csv'); rems=rows(ROOT/'06-remediation/remediation-tracker.csv'); elog=rows(ROOT/'03-evidence/evidence-log.csv')
manifest=json.loads((ROOT/'03-evidence/evidence-manifest.json').read_text())
if len(controls)!=12: errors.append(f'Expected 12 controls, got {len(controls)}')
if len(findings)!=5: errors.append(f'Expected 5 findings, got {len(findings)}')
if sum(1 for f in findings if f['rating']=='High')!=4 or sum(1 for f in findings if f['rating']=='Moderate')!=1: errors.append('Severity reconciliation failed')
# deterministic rating
def rating(score): return 'Low' if score<=4 else 'Moderate' if score<=9 else 'High' if score<=16 else 'Critical'
for f in findings:
    score=int(f['likelihood'])*int(f['impact'])
    if score!=int(f['score']) or rating(score)!=f['rating']: errors.append(f"Rating mismatch {f['finding_id']}")
# finding -> exception -> test/wp/evidence -> remediation
exc_by={e['finding_id']:e for e in exc}; rem_by={r['finding_id']:r for r in rems}; ev_ids={e['evidence_id'] for e in elog}
for f in findings:
    if f['finding_id'] not in exc_by: errors.append(f"Missing exception for {f['finding_id']}")
    if f['finding_id'] not in rem_by: errors.append(f"Missing remediation for {f['finding_id']}")
    for eid in f['evidence_refs'].split(';'):
        if eid not in ev_ids: errors.append(f"Unknown evidence {eid} in {f['finding_id']}")
# evidence hashes and manifest
man={e['evidence_id']:e for e in manifest['entries']}
if len(man)!=len(elog): errors.append('Evidence manifest/log count mismatch')
for e in elog:
    p=ROOT/'03-evidence'/e['file_name']
    if not p.exists(): errors.append(f"Missing evidence file {p}"); continue
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    if h!=e['sha256']: errors.append(f"Evidence hash mismatch {e['evidence_id']}")
    if e['evidence_id'] not in man or man[e['evidence_id']]['sha256']!=h: errors.append(f"Manifest mismatch {e['evidence_id']}")
# markdown relative links
for md in ROOT.rglob('*.md'):
    text=md.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
        if target.startswith(('http://','https://','#')): continue
        t=(md.parent/target.split('#')[0]).resolve()
        if not t.exists(): errors.append(f'Broken link {md.relative_to(ROOT)} -> {target}')
# required files
for rel in ['README.md','DISCLAIMER.md','LICENSE','CHANGELOG.md','07-reporting/uk-gdpr-executive-report.pdf','07-reporting/uk-gdpr-technical-report.docx','07-reporting/uk-gdpr-technical-report.pdf','02-assessment/uk-gdpr-assessment-workbook.xlsx']:
    if not (ROOT/rel).exists(): errors.append('Missing required '+rel)
if errors:
    print('FAIL'); [print('-',e) for e in errors]; sys.exit(1)
print(f'PASS: {len(controls)} controls, {len(findings)} findings, {len(elog)} evidence files; hashes, ratings, traceability and links reconcile.')
