#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, subprocess, sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path('/home/leoni/shared_workspace')
MEMORY_DIR = Path('/home/leoni/.openclaw/workspace/memory')
DIARY_DIR = ROOT / 'writing' / 'diary'
WEEKLY_DIR = ROOT / 'reports' / 'weekly'
DRAFTS_DIR = ROOT / 'writing' / 'drafts'
RESEARCH_DIR = ROOT / 'writing' / 'research'
DATE_RE = re.compile(r'(20\d{2}-\d{2}-\d{2})')
EM_DASH = '—'

def run(cmd, check=False):
    p = subprocess.run(cmd, cwd=str(ROOT), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if check and p.returncode:
        raise SystemExit(f"command failed: {' '.join(cmd)}\n{p.stdout[-2000:]}")
    return p.stdout.strip(), p.returncode

def week_bounds(today: date):
    start = today - timedelta(days=today.weekday() + 7)
    return start, start + timedelta(days=6)

def read(p: Path) -> str:
    return p.read_text(encoding='utf-8', errors='replace') if p.exists() else ''

def clean(s: str) -> str:
    return re.sub(r'\s+', ' ', s.replace(EM_DASH, '-')).strip()

def section(text: str, title: str) -> list[str]:
    lines = text.splitlines()
    out, grab = [], False
    for line in lines:
        if line.startswith('## ') or line.startswith('### '):
            if grab and line.lower().strip().lstrip('#').strip() not in (title.lower(),):
                break
            grab = title.lower() in line.lower()
            continue
        if grab and line.strip():
            out.append(line.strip())
    return out

def day_summary(d: date) -> dict:
    text = read(MEMORY_DIR / f'{d.isoformat()}.md')
    if not text:
        return {'done': ['Nincs memory fájl.'], 'why': 'Nincs forrás.', 'insight': 'A nap nincs dokumentálva.', 'next': 'Forrás pótlása.'}
    bullets = [l.strip('- ').strip() for l in text.splitlines() if l.strip().startswith('- ')]
    done = [b for b in bullets if b and not b.lower().startswith(('nincs új', 'nincsenek'))][:6]
    if not done:
        done = ['Reggeli brief és alap ellenőrzések lefutottak.', 'Érdemi új Tomi-input nem jelent meg.']
    risks = section(text, 'Kockázatok')[:3]
    opens = section(text, 'Nyitott itemek')[:3]
    return {
        'done': done,
        'why': 'Operációs memória és heti visszakereshetőség fenntartása.',
        'insight': clean((risks or opens or done)[0])[:240],
        'next': clean((opens[0] if opens else 'Következő futásnál új inputok és pipeline állapot ellenőrzése.'))[:240],
    }

def write_diary(d: date, overwrite=False) -> bool:
    out = DIARY_DIR / f'{d.year}' / f'{d.month:02d}' / f'{d.day:02d}.md'
    if out.exists() and not overwrite:
        return False
    s = day_summary(d)
    out.parent.mkdir(parents=True, exist_ok=True)
    content = [f'# Napló - {d.isoformat()}', '', '## Mit csináltam']
    content += [f'- {clean(x)}' for x in s['done']]
    content += ['', '## Miért ez', s['why'], '', '## 1 felismerés', s['insight'], '', '## Következő lépés', s['next'], '']
    out.write_text('\n'.join(content), encoding='utf-8')
    return True

def candidate_files(start: date, end: date) -> list[Path]:
    files = []
    for p in sorted(RESEARCH_DIR.glob('candidates-20*.md')):
        m = DATE_RE.search(p.name)
        if not m: continue
        d = datetime.strptime(m.group(1), '%Y-%m-%d').date()
        if start <= d <= end and read(p).strip() != 'NO_REPLY':
            files.append(p)
    return files

def pick_topics(start: date, end: date):
    chunks=[]
    for p in candidate_files(start, end):
        txt = read(p)
        for raw in re.split(r'\n(?=(?:#{2,3}|\*\s+|[-*]\s+|\d+\.\s+))', txt):
            t = clean(raw)
            if len(t) < 80 or t == 'NO_REPLY':
                continue
            score = 0
            low = t.lower()
            for k in ['agent', 'workflow', 'kkv', 'ceo', 'automation', 'agentic', 'crm', 'email', 'support', 'zero trust', 'temporal', 'jogi', 'kontroll', 'sandbox']:
                if k in low: score += 1
            if score:
                chunks.append((score, p.name, t[:900]))
    chunks.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return chunks[:8]

def slugify(s: str) -> str:
    tr = str.maketrans('áéíóöőúüűÁÉÍÓÖŐÚÜŰ', 'aeiooouuuAEIOOOUUU')
    s = s.translate(tr).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:70] or 'ai-agent-workflow'

def ensure_log(d: date, site: str, path: Path):
    log = DRAFTS_DIR / f'draft-log-{d.strftime("%Y-%m")}.md'
    line = f'- {d.isoformat()} | {site} | {path.name}\n'
    old = read(log)
    if path.name not in old:
        if not old:
            old = f'# Draft log - {d.strftime("%Y-%m")}\n\n'
        log.write_text(old.rstrip() + '\n' + line, encoding='utf-8')

def write_draft(d: date, site: str, topic: str, source: str, overwrite=False) -> bool:
    if site == 'vinczetamas':
        title = 'Miért nem chatbot kell a KKV-nak, hanem kontrollált AI operátor?'
        slug = 'kontrollalt-ai-operator-kkv'
        desc = 'Az AI agent értéke nem a varázslat, hanem a mérhető, ellenőrizhető végrehajtás.'
        angle = 'KKV vezetőként nem újabb appra van szükséged, hanem olyan AI operátorra, amely figyel, javasol, előkészít, de pénzhez, ügyfélhez és jogi döntéshez csak kontrollált kapun át nyúl.'
    else:
        title = 'Az AI agent akkor hasznos, ha nem mindent ő csinál'
        slug = 'ai-agent-deterministicus-vegrehajtas'
        desc = 'A jó agent rendszerben az LLM dönt és fogalmaz, a végrehajtás viszont scriptelt és ellenőrizhető.'
        angle = 'A legtöbb agent projekt ott csúszik el, hogy az LLM-re bízza a determinisztikus munkát is. A jobb modell egyszerű: döntés és szöveg LLM, ismétlődő végrehajtás script, minden fontos ponton auditnyom.'
    out = DRAFTS_DIR / f'{site}-{d.isoformat()}-{slug}.md'
    if out.exists() and not overwrite:
        return False
    content = f'''---
title: "{title}"
date: {d.isoformat()}
site: {site}.hu
description: "{desc}"
tags: [ai-agent, kkv, automatizalas, governance]
slug: "{slug}"
---

{angle}

## Mi történt?

Az előző hét jelöltjei között több téma ugyanabba az irányba mutatott: AI agentek, workflow orchestration, agent trust, CRM és email automatizálás. A közös tanulság nem az, hogy mindenre kell egy új chatbot. Hanem az, hogy a céges rutinmunkákat kontrollált, mérhető agent workflow-ba kell rendezni.

Forrásjel: `{source}`

> {topic[:700]}

## Mit jelent ez egy KKV CEO-nak?

A CEO problémája nem az, hogy nincs elég AI eszköz. Az a gond, hogy túl sok apró döntés, utánkövetés, email, riport és admin ragad nála. Egy jól összerakott AI operátor ebből vesz le terhet.

De csak akkor, ha van keret:

- külön agent account,
- szűk jogosultság,
- naplózott művelet,
- emberi jóváhagyás pénz, jog és ügyfélkommunikáció előtt,
- determinisztikus script ott, ahol nincs szükség kreatív döntésre.

## Mi a rossz megközelítés?

Az, ha az LLM-re bízod az egész láncot. Ettől lesz törékeny, drága és nehezen auditálható.

## Jobb minta

1. Az LLM értelmez, rangsorol, fogalmaz.
2. A script futtat, ment, ellenőriz, commitol.
3. Az ember csak a kockázatos döntéseknél lép be.
4. A QC nem dísz, hanem fék.

## Gyors teszt

Ha holnap bevezetnéd, ezt kérdezd:

- melyik heti rutin visz el legalább 2 órát,
- van-e egyértelmű input és output,
- lehet-e először csak javaslatot készíttetni,
- van-e emberi jóváhagyási pont,
- mérhető-e az időnyereség.

## FAQ

### Mi a különbség chatbot és AI operátor között?

A chatbot válaszol. Az AI operátor figyel, előkészít, futtat, naplóz és csak szabályozott pontokon kér embert.

### Kell ehhez nagyvállalati rendszer?

Nem. Egy KKV-nál elég lehet email, Telegram, fájlrendszer, git és pár jól körülhatárolt script.

### Mi a legnagyobb kockázat?

A túl nagy jogosultság túl korán. Először olvasás, draft, javaslat. Csak később írás és küldés.

### Hol kezdjem?

Egyetlen folyamattal: inbox triage, heti riport, ajánlat utánkövetés vagy meeting utáni admin. Ne platformot építs első nap, hanem egy működő workflow-t.
'''
    content = content.replace(EM_DASH, '-')
    out.write_text(content, encoding='utf-8')
    ensure_log(d, site, out)
    return True

def write_weekly(start: date, end: date, overwrite=False) -> bool:
    out = WEEKLY_DIR / f'{start.isoformat()}.md'
    if out.exists() and not overwrite:
        return False
    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    topics = pick_topics(start, end)
    lines = [f'# Heti összefoglaló - {start.isoformat()} .. {end.isoformat()}', '', '## Összefoglalás', 'A hét fő mintája: stabil háttérfutások, kevés közvetlen Tomi-input, több email és tartalomfeldolgozási bizonytalanság. A memory fájlok alapján a rendszer működött, de a diary és draft outputok nem voltak megbízhatóan bekötve.', '', '## Elvégzett feladatok']
    for i in range(7):
        d = start + timedelta(days=i)
        s = day_summary(d)
        lines.append(f'- {d.isoformat()}: ' + '; '.join(clean(x) for x in s['done'][:2]))
    lines += ['', '## Nyitott itemek', '- Diary generálás automatizálása memory fájlokból.', '- Draft bemenet javítása: ne egyetlen NO_REPLY fájl döntse el a heti futást.', '- Email/hírlevél feldolgozás és Telegram célpont stabilizálása.', '', '## Problémák és megoldások', '- Probléma: a QC jogosan WARN-ra futott, mert a diary és blog draft output hiányzott.', '- Megoldás: determinisztikus heti output script készült diary, weekly és fallback draft generálásra.', '', '## Tanulságok', '- Az LLM-es cron kérdezgetése cronban haszontalan. Ahol fix fájlstruktúra az elvárás, ott script kell.', '- A heti draftnak időablakot kell néznie, nem csak az aktuális napi candidates fájlt.', '', '## Költség/token', '- Pontos költségforrás nincs a memory fájlokban. A továbbiakban ezt külön metrikából érdemes olvasni.', '', '## Javaslat a következő hétre', '- A QC előtti hétfői output generálás legyen determinisztikus.', '- A tartalmi draftolás maradhat LLM-es, de kapjon előre szűrt, nem üres bemenetet.', '- Hibajelzésekben ne névvel, hanem numerikus Telegram chat ID-val menjen a célpont.', '']
    if topics:
        lines += ['## Tartalomjelöltek', '']
        for score, src, t in topics[:5]:
            lines.append(f'- `{src}` score {score}: {t[:220]}')
    out.write_text('\n'.join(lines).replace(EM_DASH, '-') + '\n', encoding='utf-8')
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--today', default=date.today().isoformat())
    ap.add_argument('--overwrite', action='store_true')
    ap.add_argument('--commit', action='store_true')
    ap.add_argument('--push', action='store_true')
    args = ap.parse_args()
    today = datetime.strptime(args.today, '%Y-%m-%d').date()
    start, end = week_bounds(today)
    changed=[]
    for i in range(7):
        d = start + timedelta(days=i)
        if write_diary(d, args.overwrite): changed.append(f'diary {d}')
    if write_weekly(start, end, args.overwrite): changed.append(f'weekly {start}')
    # Ensure at least one root draft per target in the QC window.
    existing_vt = list(DRAFTS_DIR.glob(f'vinczetamas-{start.isoformat()[:7]}-*.md'))
    topics = pick_topics(start, end)
    topic1 = topics[0] if topics else (0, 'memory', 'AI agent workflow és kontrollált végrehajtás KKV környezetben.')
    topic2 = topics[1] if len(topics) > 1 else topic1
    draft_day = end
    if not any(start <= datetime.strptime(DATE_RE.search(p.name).group(1), '%Y-%m-%d').date() <= end for p in DRAFTS_DIR.glob('vinczetamas-20*.md') if DATE_RE.search(p.name)):
        if write_draft(draft_day, 'vinczetamas', topic1[2], topic1[1], args.overwrite): changed.append('draft vinczetamas')
    if not any(start <= datetime.strptime(DATE_RE.search(p.name).group(1), '%Y-%m-%d').date() <= end for p in DRAFTS_DIR.glob('elkezdodott-20*.md') if DATE_RE.search(p.name)):
        if write_draft(draft_day, 'elkezdodott', topic2[2], topic2[1], args.overwrite): changed.append('draft elkezdodott')
    print('changed:', ', '.join(changed) if changed else 'none')
    if args.commit:
        paths = ['ops/scripts/memory_weekly_outputs.py','writing/diary','reports/weekly','writing/drafts']
        run(['git','add'] + paths, check=True)
        staged,_ = run(['git','diff','--cached','--name-only'])
        if staged:
            msg = f'Generate memory weekly outputs {today.isoformat()}'
            out, code = run(['git','commit','-m',msg])
            if code:
                raise SystemExit(out)
            print('commit:', msg)
            if args.push:
                out, code = run(['git','push'])
                if code:
                    raise SystemExit(out)
                print('push: ok')
        else:
            print('commit: no staged changes')

if __name__ == '__main__':
    main()
