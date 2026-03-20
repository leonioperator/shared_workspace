#!/usr/bin/env python3
"""
Weekly Memory Output QC Report
Checks the rolling previous 7 days (Mon-Sun of last week).
"""
from pathlib import Path
from datetime import date, datetime, timedelta
import re

MEMORY_DIR = Path('/home/leoni/.openclaw/workspace/memory')
SHARED = Path('/home/leoni/shared_workspace')
WEEKLY_DIR = SHARED / 'reports' / 'weekly'
DIARY_DIR = SHARED / 'writing' / 'diary'
DRAFTS_DIR = SHARED / 'writing' / 'drafts'
OUT_DIR = SHARED / 'reports' / 'qa'

# Rolling window: previous full week (Mon–Sun)
today = date.today()
last_monday = today - timedelta(days=today.weekday() + 7)
last_sunday = last_monday + timedelta(days=6)
START = last_monday
END = last_sunday

DATE_RE = re.compile(r'^(\d{4}-\d{2}-\d{2})\.md$')

# Memory daily files in window
memory_days = []
for p in sorted(MEMORY_DIR.glob('2026-*.md')):
    m = DATE_RE.match(p.name)
    if not m:
        continue
    d = datetime.strptime(m.group(1), '%Y-%m-%d').date()
    if START <= d <= END:
        memory_days.append(d)

# Expected weekly report: the Monday of the window
expected_weeks = [START]
missing_weekly = [d for d in expected_weeks if not (WEEKLY_DIR / f'{d.isoformat()}.md').exists()]

# Diary checks
diary_missing = []
for d in memory_days:
    p = DIARY_DIR / f'{d.year}' / f'{d.month:02d}' / f'{d.day:02d}.md'
    if not p.exists():
        diary_missing.append(d)

# Draft checks in window
drafts = [p.name for p in DRAFTS_DIR.glob('*.md')]
in_range = []
for n in drafts:
    m = re.search(r'(\d{4}-\d{2}-\d{2})', n)
    if not m:
        continue
    d = datetime.strptime(m.group(1), '%Y-%m-%d').date()
    if START <= d <= END:
        in_range.append(n)

vt_count = sum(1 for n in in_range if n.startswith('vinczetamas-'))
ek_count = sum(1 for n in in_range if n.startswith('elkezdodott-'))

status = 'PASS'
if missing_weekly or diary_missing or vt_count == 0 or ek_count == 0:
    status = 'WARN'

OUT_DIR.mkdir(parents=True, exist_ok=True)
out = OUT_DIR / f'{today.isoformat()}-memory-output-qc.md'

lines = []
lines.append(f'# Memory Output QC - {today.isoformat()}')
lines.append('')
lines.append(f'Window: {START.isoformat()} .. {END.isoformat()} (előző hét: H-V)')
lines.append(f'Status: **{status}**')
lines.append('')
lines.append('## Heti riport')
lines.append(f'- Elvárt: {len(expected_weeks)} ({START.isoformat()}.md)')
lines.append(f'- Hiányzó: {len(missing_weekly)}')
for d in missing_weekly:
    lines.append(f'  - {d.isoformat()}')
lines.append('')
lines.append('## Diary lefedettség (napi memory fájlok alapján)')
lines.append(f'- Napi memory fájlok az ablakban: {len(memory_days)}')
lines.append(f'- Hiányzó diary fájlok: {len(diary_missing)}')
for d in diary_missing:
    lines.append(f'  - {d.isoformat()}')
lines.append('')
lines.append('## Blog draft lefedettség')
lines.append(f'- Draftek az ablakban: {len(in_range)}')
lines.append(f'- vinczetamas-* : {vt_count}')
lines.append(f'- elkezdodott-* : {ek_count}')
lines.append('')
lines.append('## Draft fájlok')
for n in sorted(in_range):
    lines.append(f'- {n}')

out.write_text('\n'.join(lines) + '\n')
print(out)
print(status)
