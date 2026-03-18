#!/usr/bin/env python3
from pathlib import Path
from datetime import date, datetime, timedelta
import re

MEMORY_DIR = Path('/home/leoni/.openclaw/workspace/memory')
SHARED = Path('/home/leoni/shared_workspace')
WEEKLY_DIR = SHARED / 'reports' / 'weekly'
DIARY_DIR = SHARED / 'writing' / 'diary'
DRAFTS_DIR = SHARED / 'writing' / 'drafts'
OUT_DIR = SHARED / 'reports' / 'qa'

START = date(2026,2,17)
END = date(2026,3,15)

DATE_RE = re.compile(r'^(\d{4}-\d{2}-\d{2})\.md$')

# Memory daily files (strict daily only)
memory_days = []
for p in sorted(MEMORY_DIR.glob('2026-*.md')):
    m = DATE_RE.match(p.name)
    if not m:
        continue
    d = datetime.strptime(m.group(1), '%Y-%m-%d').date()
    if START <= d <= END:
        memory_days.append(d)

# Expected weekly files: Mondays covering interval
cur = START
while cur.weekday() != 0:
    cur += timedelta(days=1)
expected_weeks = []
while cur <= END + timedelta(days=(6-END.weekday())):
    expected_weeks.append(cur)
    cur += timedelta(days=7)

missing_weekly = [d for d in expected_weeks if not (WEEKLY_DIR / f'{d.isoformat()}.md').exists()]

# Diary checks for memory days
diary_missing = []
for d in memory_days:
    p = DIARY_DIR / f'{d.year}' / f'{d.month:02d}' / f'{d.day:02d}.md'
    if not p.exists():
        diary_missing.append(d)

# Draft checks in range
drafts = [p.name for p in DRAFTS_DIR.glob('*.md')]
range_prefix = [f'-{d.isoformat()}-' for d in [START, END]]
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

out = OUT_DIR / f'{date.today().isoformat()}-memory-output-qc.md'

lines = []
lines.append(f'# Memory Output QC - {date.today().isoformat()}')
lines.append('')
lines.append(f'Window: {START.isoformat()} .. {END.isoformat()}')
lines.append(f'Status: **{status}**')
lines.append('')
lines.append('## Weekly reports')
lines.append(f'- Expected: {len(expected_weeks)}')
lines.append(f'- Missing: {len(missing_weekly)}')
for d in missing_weekly:
    lines.append(f'  - {d.isoformat()}')
lines.append('')
lines.append('## Diary coverage from daily memory files')
lines.append(f'- Daily memory files in window: {len(memory_days)}')
lines.append(f'- Missing diary files: {len(diary_missing)}')
for d in diary_missing:
    lines.append(f'  - {d.isoformat()}')
lines.append('')
lines.append('## Blog draft coverage')
lines.append(f'- Drafts in window: {len(in_range)}')
lines.append(f'- vinczetamas-* count: {vt_count}')
lines.append(f'- elkezdodott-* count: {ek_count}')
lines.append('')
lines.append('## Draft files in window')
for n in sorted(in_range):
    lines.append(f'- {n}')

out.write_text('\n'.join(lines) + '\n')
print(out)
print(status)
