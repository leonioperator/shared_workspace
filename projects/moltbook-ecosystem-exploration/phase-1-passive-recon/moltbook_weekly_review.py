#!/usr/bin/env python3
import argparse
import datetime as dt
import json
from pathlib import Path
from collections import Counter

BASE = Path('/home/leoni/.openclaw/workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon')
ARTIFACTS_DIR = BASE / 'artifacts' / 'scans'
WEEKLY_DIR = BASE / 'artifacts' / 'weekly'
TEMPLATE = BASE / 'weekly-summary-template.md'


def parse_ts(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00'))


def load_artifacts(path: Path, since: dt.datetime):
    items = []
    if not path.exists():
        return items
    for file in sorted(path.glob('*.json')):
        data = json.loads(file.read_text())
        scanned_at = parse_ts(data['scanned_at'])
        if scanned_at >= since:
            items.append(data)
    return items


def top(counter: Counter, n: int = 3):
    return [k for k, _ in counter.most_common(n)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', type=int, default=7)
    parser.add_argument('--artifacts-dir', type=Path, default=ARTIFACTS_DIR)
    parser.add_argument('--out-dir', type=Path, default=WEEKLY_DIR)
    parser.add_argument('--emit-summary', action='store_true')
    args = parser.parse_args()

    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    since = now - dt.timedelta(days=args.days)
    artifacts = load_artifacts(args.artifacts_dir, since)

    tag_counter = Counter()
    tool_counter = Counter()
    problem_counter = Counter()
    posts_reviewed = 0
    relevant = 0
    success = 0
    errors = 0
    key_quotes = []

    for artifact in artifacts:
        posts_reviewed += artifact.get('summary', {}).get('posts_seen', 0)
        if artifact.get('status') == 'error':
            errors += 1
            continue
        success += 1
        relevant += artifact.get('summary', {}).get('posts_matched', 0)
        for post in artifact.get('posts', []):
            for tag in post.get('tags', []):
                tag_counter[tag] += 1
            quote = post.get('notable_quote')
            if quote:
                key_quotes.append(quote)
        for post in artifact.get('posts', []):
            if 'OpenClaw' in (post.get('title') or ''):
                tool_counter['OpenClaw'] += 1
            for sig in post.get('signals', []):
                problem_counter[sig] += 1

    signal_to_noise = 'low'
    if relevant >= 6:
        signal_to_noise = 'high'
    elif relevant >= 2:
        signal_to_noise = 'medium'

    top_tags = top(tag_counter)
    top_tools = top(tool_counter) or ['OpenClaw']
    top_problems = top(problem_counter)
    roi = 'low'
    if relevant >= 6:
        roi = 'high'
    elif relevant >= 2:
        roi = 'medium'

    out = [
        '# Moltbook Weekly Summary',
        '',
        '## Summary Period',
        f'- Start: {since.date().isoformat()}',
        f'- End: {now.date().isoformat()}',
        '',
        '## Artifact Coverage',
        f'- Scan artifacts reviewed: {len(artifacts)}',
        f'- Successful scans: {success}',
        f'- Error scans: {errors}',
        '',
        '## Activity Level',
        f'- Posts reviewed: {posts_reviewed}',
        f'- Relevant discussions captured: {relevant}',
        f'- Signal-to-noise: {signal_to_noise}',
        '',
        '## Top Tags',
    ]
    out += [f'- {x}' for x in (top_tags or ['none'])]
    out += ['', '## Most Mentioned Tools']
    out += [f'- {x}' for x in (top_tools or ['none'])]
    out += ['', '## Recurring Engineering Problems']
    out += [f'- {x}' for x in (top_problems or ['none'])]
    out += ['', '## Notable Insights']
    out += [f'- {x}' for x in (key_quotes[:3] or ['No notable insights this week.'])]
    out += ['', '## ROI Assessment', '### Time spent vs insight gained', f'- {roi}', '', '### Should monitoring continue?']
    out += ['- yes' if roi != 'low' else '- reduce frequency']
    out += ['', '### Should Phase 2 be considered?', '- not yet', '', '## Recommendation']
    if roi == 'high':
        out += ['Continue Phase 1. Signal is strong enough to justify ongoing monitoring, but Phase 2 is not justified yet.']
    elif roi == 'medium':
        out += ['Continue Phase 1 at current cadence. There is useful signal, but still not enough evidence for public participation.']
    else:
        out += ['Reduce scan frequency unless signal quality improves. Current output does not yet justify higher effort.']

    args.out_dir.mkdir(parents=True, exist_ok=True)
    path = args.out_dir / f'{now.date().isoformat()}.md'
    path.write_text('\n'.join(out) + '\n')

    if args.emit_summary:
        print(f'- Heti Moltbook review kész: {len(artifacts)} artifact, {relevant} releváns találat, ROI: {roi}.')
        print(f'- Fő címkék: {", ".join(top_tags[:2]) if top_tags else "nincs"}. File: {path.name}')
    else:
        print(path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
