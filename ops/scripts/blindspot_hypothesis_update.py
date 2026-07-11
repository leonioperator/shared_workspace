#!/usr/bin/env python3
import os, re, subprocess, sys, tempfile
from datetime import date
from pathlib import Path

ROOT = Path('/home/leoni/shared_workspace')
RESEARCH = ROOT / 'research'
RADAR = RESEARCH / 'blindspot-radar-hypotheses.md'
SCRIPT = Path('/home/leoni/.openclaw/scripts/blindspot_hypothesis_update.py')
TODAY = date.today().isoformat()
SIGNAL = RESEARCH / f'blindspot-signals-{TODAY}.md'
HEADER = f'## Daily Radar Delta - {TODAY}'

HYPOTHESIS_RULES = [
    ('H62', 'Proof Chain', ['auditable', 'traceable', 'verification', 'benchmark', 'proof', 'self-verification', 'quality control']),
    ('H63', 'Legal Entity / Human-Centered Governance', ['human-centered', 'values', 'culture', 'governance', 'human-agent', 'social norms']),
    ('H66', 'Oversight Incentive / Delay Risk', ['delayed', 'repression', 'instability', 'approval', 'intervention', 'oversight', 'delay']),
    ('H71', 'Rubric-Guided Policy', ['rubric', 'criteria', 'policy decomposition']),
    ('H72', 'High-Stakes Integrity', ['physical sciences', 'biomedical', 'healthcare', 'scientific', 'integrity', 'domain']),
    ('H87', 'Agent Trust & Collaboration', ['trust between ai agents', 'trust formation', 'verification game', 'trust disposition']),
    ('H90', 'Multi-Agent Debate / Research Agents', ['deep research', 'delveagent', 'research agent', 'multi-agent framework']),
    ('H100', 'Latent Communication Security', ['latent', 'kv-cache', 'communication framework']),
    ('H101', 'Misinformation / Ensemble Resilience', ['misinformation', 'trust recovery', 'ensemble', 'breakage', 'recovery']),
    ('H102', 'Semantic Drift', ['semantic', 'drift', 'knowledge transfer', 'grounded reflection']),
    ('H103', 'Policy Tree Audit', ['tree', 'branch', 'planning strategy', 'dynamic planning']),
    ('H104', 'Meta-Agent Decomposition', ['benchmark construction', 'pipeline', 'planning, construction', 'meta-agent', 'decomposition']),
    ('H105', 'Decentralized Governance', ['decentralized', 'relation-aware memory', 'coordination', 'memory graph', 'conmem']),
    ('H106', 'Policy Tree Transparency', ['policy tree', 'interpretable', 'transparency']),
    ('H107', 'Runtime Autonomy Control', ['adaptive', 'runtime', 'autonomous', 'self-update']),
]


def fail(msg, code=1):
    print(f'⚠️ Blindspot hypothesis frissítés failed: {msg}', file=sys.stderr)
    sys.exit(code)


def run(cmd, cwd=ROOT, check=True):
    p = subprocess.run(cmd, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if check and p.returncode != 0:
        fail(f'parancs hiba ({p.returncode}): {" ".join(cmd)}\n{p.stdout[-1200:]}')
    return p.stdout.strip(), p.returncode


def clean(s):
    return re.sub(r'\s+', ' ', (s or '').strip())


def parse_signals(md):
    chunks = re.split(r'^###\s+(\d+)\.\s+', md, flags=re.M)
    out = []
    for i in range(1, len(chunks), 2):
        rank = int(chunks[i])
        body = chunks[i+1]
        lines = body.splitlines()
        title = clean(lines[0]) if lines else f'Signal {rank}'
        def field(name):
            m = re.search(rf'^- {re.escape(name)}:\s*(.*)$', body, flags=re.M)
            return clean(m.group(1)) if m else ''
        out.append({
            'rank': rank,
            'title': title,
            'score': field('Deep score'),
            'date': field('Date'),
            'source': field('Source'),
            'focus': field('Focus/tech'),
            'url': field('URL'),
            'summary': field('Summary'),
        })
    return out


def classify(sig):
    hay = ' '.join([sig['title'], sig['summary'], sig['focus']]).lower()
    hits = []
    for hid, label, words in HYPOTHESIS_RULES:
        if any(w in hay for w in words):
            hits.append((hid, label))
    # stable unique order
    seen, uniq = set(), []
    for x in hits:
        if x[0] not in seen:
            seen.add(x[0]); uniq.append(x)
    return uniq[:4]


def bullet_signal(sig, idx):
    cls = classify(sig)
    hyp = ', '.join(f'{h} ({label})' for h, label in cls) if cls else 'H62/H72 általános auditability validation'
    score = f"{sig['score']}" if sig['score'] else 'n/a'
    url = f" — {sig['url']}" if sig['url'] else ''
    thesis = sig['summary'][:520].rstrip()
    if len(sig['summary']) > 520:
        thesis += '…'
    return (
        f"{idx}. **{sig['title']}** ({score})\n"
        f"   - **Forrás:** {sig['source'] or 'n/a'} {sig['date'] or ''}{url}\n"
        f"   - **Thesis:** {thesis}\n"
        f"   - **Hypothesis-ek:** {hyp}\n"
        f"   - **Megerősítés:** {confirmation_sentence(sig, cls)}"
    )


def confirmation_sentence(sig, cls):
    ids = {h for h, _ in cls}
    title = sig['title'].lower()
    if 'human-centered' in title:
        return 'A governance fókusz nem puszta tool-control, hanem cognition/culture/values/social behavior integráció; ez H63 és H72 vevői nyelvét erősíti.'
    if 'deep research' in title or 'dumat' in title or 'delveagent' in title:
        return 'A deep-research agenteknél az auditálhatóság, self-verification és domain-grounded reasoning már architektúra-követelmény; H62/H72/H90 erős validáció.'
    if 'delayed' in title:
        return 'A delayed oversight önmagában instabilitást okozhat; H66 nem UX-probléma, hanem rendszerstabilitási kockázat.'
    if 'trust between ai agents' in title:
        return 'Az agent-agent trust mérhető deployment előtti tulajdonság; H87/H101 ensemble governance irány erősödik.'
    if 'bench' in title or 'benchmark' in title:
        return 'A benchmark-konstrukció maga is verifikálható multi-agent pipeline lesz; H104 és H62 közvetlenül erősödik.'
    if 'sheaf' in title or 'nash' in title:
        return 'A stratégiai konzisztencia formális ellenőrzése governance/audit felületté válhat; H101/H105 irány.'
    if 'darrms' in title or 'attention radius' in title:
        return 'A resource-constrained coordination a runtime autonomy kontrollját és observation-policy governance-t teszi fontossá; H107/H105 irány.'
    if ids:
        return 'A signal meglévő governance hypothesis-t erősít, új önálló hypothesis nélkül.'
    return 'Általános agent-platform relevancia, de önálló új hypothesis nincs.'


def build_block(signals):
    top = signals[:10]
    all_cls = []
    for s in top:
        all_cls.extend(classify(s))
    unique = []
    seen = set()
    for h, label in all_cls:
        if h not in seen:
            seen.add(h); unique.append((h, label))

    top_score = top[0]['score'] if top else 'n/a'
    low_score = top[-1]['score'] if top else 'n/a'
    lines = [
        '', HEADER, '',
        f'**Forrás:** Blindspot Signals Report {TODAY} ({len(signals)} megjelenített signal, AI agents / AI decision delegation fókusz)',
        f'**Top Deep Score Range:** {top_score} – {low_score}',
        f'**Assessment Date:** {TODAY}', '',
        '### Összefoglaló: Human-centered governance + deep research auditability + ensemble stability', '',
        'A mai signal report a meglévő agent-governance hypothesis poolt erősíti. Új önálló blindspot nem indokolt: a legerősebb jelek ugyanarra a konvergenciára mutatnak, mint az előző radar delta: human-centered governance, deep-research agent auditability, selective oversight, ensemble trust és verifikálható multi-agent pipeline.', '',
        '### Key Signals', '',
    ]
    for idx, sig in enumerate(top, 1):
        lines.append(bullet_signal(sig, idx))
        lines.append('')

    lines.extend([
        '### Nincs Új Hypothesis (Mai Signal Kontextus)', '',
        'A mai jelek a meglévő hypothesis poolt validálják. Nem kell új H-számot nyitni; a piac/technológia ugyanazokat a vevői problémákat teszi konkrétabbá: audit proof chain, human-centered mandate, selective oversight, ensemble trust, semantic/representation integrity.', '',
        '**Megerősített Hypothesis Pool:**',
    ])
    if not unique:
        unique = [('H62','Proof Chain'), ('H63','Legal Entity / Human-Centered Governance'), ('H72','High-Stakes Integrity')]
    for h, label in unique:
        lines.append(f'- **{h}** ({label}): mai signalok által megerősítve')

    lines.extend([
        '', '### Top 3 Opportunity', '',
        '**1. Human-Centered Agent Governance Evidence Pack (H63 + H72 + H62)**',
        '- **Szövegkörnyezet:** Human cognition/culture/values + auditable deep-research workflows + domain verification.',
        '- **Opportunity:** governance evidence pack: mandate, value/rubric snapshot, decision transcript, source proof chain, domain self-check.',
        '- **Kísérlet:** Navibase/Leoni high-risk run proof receipt: input hash, tool trace, policy/rubric snapshot, human approval point.', '',
        '**2. Selective Oversight & Delay-Stability Monitor (H66 + H107)**',
        '- **Szövegkörnyezet:** Delay-induced instability + runtime adaptation/resource constraints.',
        '- **Opportunity:** approval-point optimizer: high-leverage gate detection, delay budget, routine auto-approve, regression alert.',
        '- **Kísérlet:** mérni approval latency-t és override rate-et Leoni cron/agent workflowkon; jelölni a késleltetésre érzékeny döntési pontokat.', '',
        '**3. Ensemble Trust / Research-Agent Audit Service (H87 + H101 + H104)**',
        '- **Szövegkörnyezet:** agent-agent trust mérhetőség + benchmark construction + deep research multi-agent audit.',
        '- **Opportunity:** ensemble trust profile és DRA audit template: pairwise verification cost, trust recovery SLA, planning DAG proof.',
        '- **Kísérlet:** 3-4 agent decision DAG stress-test: hamis jel injektálás, verification-cost mérés, recovery idő.', '',
        '### Conclusion', '',
        f'**{TODAY} radar delta:**',
        '- **Nincs új hypothesis:** consolidated pool validáció folytatódik',
        '- **Kritikus konvergencia:** human-centered governance + auditable deep-research + ensemble trust + delay-aware oversight',
        '- **Next radar checkpoint:** következő napi signal report után',
    ])
    return '\n'.join(lines).rstrip() + '\n'

if not SIGNAL.exists() or SIGNAL.stat().st_size == 0:
    print(f'NO_REPLY: mai signal fájl hiányzik: {SIGNAL}')
    sys.exit(0)
if not RADAR.exists() or RADAR.stat().st_size == 0:
    fail(f'radar fájl hiányzik vagy üres: {RADAR}')

radar_text = RADAR.read_text(encoding='utf-8')
if HEADER in radar_text:
    print(f'NO_REPLY: Daily Radar Delta {TODAY} már létezik')
    sys.exit(0)

signal_text = SIGNAL.read_text(encoding='utf-8')
novel_m = re.search(r'^- Novel vs previous reports:\s*([0-9]+)\s*$', signal_text, flags=re.M)
if novel_m and int(novel_m.group(1)) == 0:
    print(f'NO_REPLY: nincs új blindspot signal, hypothesis frissítés kihagyva: {SIGNAL}')
    sys.exit(0)
# Prefer the novelty section. The stable deep-score section repeats old evergreen papers and used to spam identical deltas.
new_section = signal_text
m = re.search(r'## New Signals Since Previous Reports\n(?P<body>.*?)(?:\n## Top Signals By Deep Score|\Z)', signal_text, flags=re.S)
if m:
    new_section = m.group('body')
signals = parse_signals(new_section)
if len(signals) < 5:
    fail(f'a signal fájl új szekciójában kevesebb mint 5 ### cím van: {len(signals)}')

block = build_block(signals)
fd, tmp = tempfile.mkstemp(prefix='blindspot-radar-', suffix='.tmp', dir=str(RESEARCH), text=True)
try:
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(radar_text.rstrip() + '\n\n' + block)
    os.replace(tmp, RADAR)
finally:
    if os.path.exists(tmp):
        os.unlink(tmp)

new_text = RADAR.read_text(encoding='utf-8')
if HEADER not in new_text:
    fail('append verification failed: header nincs a radar fájlban')
if len(re.findall(rf'^{re.escape(HEADER)}$', new_text, flags=re.M)) != 1:
    fail('append verification failed: duplikált napi blokk')
if len(re.findall(r'^\d+\. \*\*', block, flags=re.M)) < 5:
    fail('append verification failed: kevesebb mint 5 key signal')

# Only stage intended files; leave unrelated dirty workspace alone.
run(['git', 'add', str(RADAR.relative_to(ROOT)), str(SIGNAL.relative_to(ROOT))])
staged, _ = run(['git', 'diff', '--cached', '--name-only'], check=False)
if 'research/blindspot-radar-hypotheses.md' not in staged:
    fail('git staging failed: radar nincs staged állapotban')
commit_msg = f'Update blindspot radar hypotheses {TODAY}'
commit_out, commit_code = run(['git', 'commit', '-m', commit_msg], check=False)
if commit_code != 0:
    fail(f'git commit failed:\n{commit_out[-1200:]}')
push_out, push_code = run(['git', 'push'], check=False)
if push_code != 0:
    fail(f'git push failed:\n{push_out[-1200:]}')

# Verify clean for intended files only.
post, _ = run(['git', 'status', '--short', 'research/blindspot-radar-hypotheses.md', str(SIGNAL.relative_to(ROOT))], check=False)
if post.strip():
    fail(f'intended files dirty after commit/push:\n{post}')

top5 = [s['title'] for s in signals[:5]]
print('✅ Blindspot radar hypothesis frissítés sikeres')
print(f'Radar fájl: {RADAR}')
print(f'Signal fájl: {SIGNAL}')
print(f'Commit: {commit_msg}')
print('Git push: OK')
print('Email: skipped (command cron Telegram státusz, nincs külön email sink ebben a scriptben)')
print('Top 5 signal:')
for i, t in enumerate(top5, 1):
    print(f'- {i}. {t}')
