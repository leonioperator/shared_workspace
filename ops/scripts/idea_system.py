#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path('/home/leoni/shared_workspace')
IDEAS_PATH = ROOT / 'project_ideas' / 'ideas.jsonl'
STATE_PATH = ROOT / 'project_ideas' / 'state.json'
OUTBOUND_DIR = ROOT / 'outbound'

GOALS = [
    '2026-ban kilépés a munkahelyről',
    'AI/agentic/automatizációs bevétel építése',
    'saját vagyont termelő rendszerek építése',
    'fókusz és készre vitel, nem párhuzamos szétszóródás',
]


def now_iso():
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def today_compact():
    return dt.datetime.now().strftime('%Y%m%d')


def ensure_files():
    IDEAS_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTBOUND_DIR.mkdir(parents=True, exist_ok=True)
    if not STATE_PATH.exists():
        STATE_PATH.write_text(json.dumps({'active_id': None, 'last_selection_at': None}, indent=2), encoding='utf-8')
    if not IDEAS_PATH.exists():
        IDEAS_PATH.write_text('', encoding='utf-8')


def load_state():
    ensure_files()
    return json.loads(STATE_PATH.read_text(encoding='utf-8'))


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def load_ideas():
    ensure_files()
    rows = []
    raw = IDEAS_PATH.read_text(encoding='utf-8').splitlines()
    for line in raw:
        line = line.strip()
        if not line or line == '[]':
            continue
        rows.append(json.loads(line))
    return rows


def save_ideas(ideas):
    with IDEAS_PATH.open('w', encoding='utf-8') as f:
        for item in ideas:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')


def next_id(ideas):
    prefix = dt.datetime.now().strftime('IDEA-%Y%m%d-')
    existing = [x['id'] for x in ideas if x['id'].startswith(prefix)]
    return f"{prefix}{len(existing)+1:03d}"


def score_money(text):
    t = text.lower()
    if any(k in t for k in ['bevétel', 'eladás', 'sales', 'lead', 'ügyfél', 'automatizáció', 'agent']):
        return 3
    if any(k in t for k in ['validáció', 'audit', 'offer', 'workflow']):
        return 2
    if any(k in t for k in ['ötlet', 'tartalom', 'blog']):
        return 1
    return 0


def score_validation(text):
    t = text.lower()
    if any(k in t for k in ['landing', 'videó', 'pilot', 'teszt', 'validáció', 'interjú']):
        return 3
    if any(k in t for k in ['script', 'offer', 'draft', 'mvp']):
        return 2
    if any(k in t for k in ['rendszer', 'platform', 'architektúra']):
        return 1
    return 0


def score_alignment(text):
    t = text.lower()
    score = 0
    if any(k in t for k in ['ai', 'agent', 'automatizáció']):
        score += 1
    if any(k in t for k in ['bevétel', 'vagyon', 'ügyfél', 'kkv', 'fókusz']):
        score += 1
    return min(score, 2)


def score_effort(text):
    t = text.lower()
    if any(k in t for k in ['platform', 'piactér', 'ecosystem', 'komplett rendszer', 'sok integráció']):
        return -2
    if any(k in t for k in ['mvp', 'script', 'landing', 'offer', 'videó']):
        return -1
    return 0


def generate_sprint_task(text):
    t = text.strip()
    lower = t.lower()
    if 'landing' in lower:
        return 'Írj meg 1 validációs landing vázlatot 3 CTA-val.'
    if 'videó' in lower or 'video' in lower:
        return 'Készíts 1 darab felvehető videó scriptet konkrét CTA-val.'
    if 'agent' in lower or 'automatiz' in lower:
        return 'Írj egy 1 oldalas pilot workflow-t 1 konkrét use case-re és 1 ajánlattal.'
    if 'blog' in lower or 'tartalom' in lower:
        return 'Írj meg 1 publikálható draftot 1 konkrét CTA-val.'
    if 'audit' in lower:
        return 'Írj meg 1 audit offer vázlatot scope-pal, árral és garanciával.'
    return 'Írj meg 1 oldalas validációs vázlatot konkrét célpiaccal, offerrel és CTA-val.'


def rescore(item):
    text = item['text']
    item['score_money'] = score_money(text)
    item['score_validation'] = score_validation(text)
    item['score_alignment'] = score_alignment(text)
    item['score_effort'] = score_effort(text)
    item['score_total'] = item['score_money'] + item['score_validation'] + item['score_alignment'] + item['score_effort']
    if not item.get('sprint_task'):
        item['sprint_task'] = generate_sprint_task(text)
    return item


def write_status_report(active, reason):
    path = OUTBOUND_DIR / f"{today_compact()}-idea-system-status.md"
    lines = [
        f"# Idea System Status — {today_compact()}",
        '',
        f"Ok: {reason}",
    ]
    if active:
        lines += [
            '',
            f"Active ID: {active['id']}",
            f"Text: {active['text']}",
            f"Score: {active['score_total']} ({active['score_money']}/{active['score_validation']}/{active['score_alignment']}/{active['score_effort']})",
            f"Sprint task: {active['sprint_task']}",
        ]
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def write_focus_report(active):
    path = OUTBOUND_DIR / f"{today_compact()}-next-focus.md"
    why = 'Ez kapta a legmagasabb score_total pontszámot a szabad ötletek közül.'
    lines = [
        f"# Next Focus — {today_compact()}",
        '',
        f"Aktív ötlet ID: {active['id']}",
        f"Aktív ötlet: {active['text']}",
        '',
        '## Score bontás',
        f"- money: {active['score_money']}",
        f"- validation: {active['score_validation']}",
        f"- alignment: {active['score_alignment']}",
        f"- effort: {active['score_effort']}",
        f"- total: {active['score_total']}",
        '',
        '## Sprint task',
        f"- {active['sprint_task']}",
        '',
        '## Miért ez lett kiválasztva',
        f"- {why}",
    ]
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def select_next(ideas, state):
    if state.get('active_id'):
        return None
    candidates = [rescore(x) for x in ideas if x['status'] == 'idea']
    if not candidates:
        return None
    candidates.sort(key=lambda x: (x['score_total'], x['score_validation'], x['score_money'], x['created_at']), reverse=True)
    winner = candidates[0]
    for item in ideas:
        if item['id'] == winner['id']:
            item['status'] = 'active'
            item['updated_at'] = now_iso()
            item['sprint_task'] = winner['sprint_task']
            item['score_money'] = winner['score_money']
            item['score_validation'] = winner['score_validation']
            item['score_alignment'] = winner['score_alignment']
            item['score_effort'] = winner['score_effort']
            item['score_total'] = winner['score_total']
            state['active_id'] = item['id']
            state['last_selection_at'] = now_iso()
            save_ideas(ideas)
            save_state(state)
            write_focus_report(item)
            write_status_report(item, 'Új aktív ötlet kiválasztva.')
            return item
    return None


def add_idea(text, source):
    ideas = load_ideas()
    state = load_state()
    item = {
        'id': next_id(ideas),
        'created_at': now_iso(),
        'updated_at': now_iso(),
        'source': source,
        'text': text.strip(),
        'status': 'idea',
        'score_money': 0,
        'score_validation': 0,
        'score_alignment': 0,
        'score_effort': 0,
        'score_total': 0,
        'sprint_task': '',
        'notes': '',
    }
    rescore(item)
    ideas.append(item)
    save_ideas(ideas)
    picked = select_next(ideas, state)
    if not picked:
        write_status_report(None, f"Új ötlet mentve: {item['id']}")
    return item


def update_status(idea_id, new_status):
    ideas = load_ideas()
    state = load_state()
    target = None
    for item in ideas:
        if item['id'] == idea_id:
            item['status'] = new_status
            item['updated_at'] = now_iso()
            target = item
            break
    if not target:
        raise SystemExit(f'Nincs ilyen ID: {idea_id}')
    if state.get('active_id') == idea_id:
        state['active_id'] = None
    save_ideas(ideas)
    save_state(state)
    picked = select_next(ideas, state)
    write_status_report(picked, f"{idea_id} -> {new_status}")
    return target, picked


def import_file(path, source):
    text = Path(path).read_text(encoding='utf-8')
    ideas = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith('#'):
            continue
        if s.lower().startswith('új ötlet:'):
            s = s.split(':', 1)[1].strip()
        if s.startswith('- ') or s.startswith('* '):
            s = s[2:].strip()
        if len(s) >= 12:
            ideas.append(s)
    added = []
    for idea in ideas:
        added.append(add_idea(idea, source))
    return added


def show_status():
    ideas = load_ideas()
    state = load_state()
    print(json.dumps({'state': state, 'ideas': ideas}, ensure_ascii=False, indent=2))


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd', required=True)

    addp = sub.add_parser('add')
    addp.add_argument('text')
    addp.add_argument('--source', default='telegram', choices=['telegram', 'inbox', 'import'])

    imp = sub.add_parser('import-file')
    imp.add_argument('path')
    imp.add_argument('--source', default='inbox', choices=['telegram', 'inbox', 'import'])

    done = sub.add_parser('done')
    done.add_argument('idea_id')

    kill = sub.add_parser('kill')
    kill.add_argument('idea_id')

    sub.add_parser('select-next')
    sub.add_parser('status')

    args = p.parse_args()
    ensure_files()

    if args.cmd == 'add':
        item = add_idea(args.text, args.source)
        print(item['id'])
    elif args.cmd == 'import-file':
        added = import_file(args.path, args.source)
        print(json.dumps([x['id'] for x in added], ensure_ascii=False))
    elif args.cmd == 'done':
        target, picked = update_status(args.idea_id, 'done')
        print(json.dumps({'done': target['id'], 'next_active': picked['id'] if picked else None}, ensure_ascii=False))
    elif args.cmd == 'kill':
        target, picked = update_status(args.idea_id, 'killed')
        print(json.dumps({'killed': target['id'], 'next_active': picked['id'] if picked else None}, ensure_ascii=False))
    elif args.cmd == 'select-next':
        ideas = load_ideas(); state = load_state(); picked = select_next(ideas, state)
        print(picked['id'] if picked else 'NO_IDEA')
    elif args.cmd == 'status':
        show_status()

if __name__ == '__main__':
    main()
