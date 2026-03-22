#!/usr/bin/env python3
import argparse
import datetime as dt
import json
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path('/home/leoni/.openclaw/workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon')
ARTIFACTS_DIR = BASE / 'artifacts' / 'scans'
TRENDS_DIR = BASE / 'artifacts' / 'trends'
SCHEMA = 'moltbook.trends.v1'


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
            data['_file'] = file.name
            data['_scanned_at_dt'] = scanned_at
            items.append(data)
    return items


def top(counter: Counter, n: int = 5):
    return [{'name': k, 'count': v} for k, v in counter.most_common(n)]


def bucket_day(ts: dt.datetime) -> str:
    return ts.date().isoformat()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', type=int, default=7)
    parser.add_argument('--artifacts-dir', type=Path, default=ARTIFACTS_DIR)
    parser.add_argument('--out-dir', type=Path, default=TRENDS_DIR)
    parser.add_argument('--emit-summary', action='store_true')
    args = parser.parse_args()

    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    since = now - dt.timedelta(days=args.days)
    artifacts = load_artifacts(args.artifacts_dir, since)

    tag_counter = Counter()
    tool_counter = Counter()
    cluster_counter = Counter()
    author_counter = Counter()
    status_counter = Counter()
    post_counter = Counter()
    daily = defaultdict(lambda: {'artifacts': 0, 'posts_seen': 0, 'posts_matched': 0, 'statuses': Counter()})
    top_posts = []
    posts_seen = 0
    posts_matched = 0

    for artifact in artifacts:
        status = artifact.get('status', 'unknown')
        status_counter[status] += 1
        day = bucket_day(artifact['_scanned_at_dt'])
        daily[day]['artifacts'] += 1
        daily[day]['statuses'][status] += 1
        seen = artifact.get('summary', {}).get('posts_seen', 0)
        matched = artifact.get('summary', {}).get('posts_matched', 0)
        posts_seen += seen
        posts_matched += matched
        daily[day]['posts_seen'] += seen
        daily[day]['posts_matched'] += matched
        for post in artifact.get('posts', []):
            pid = post.get('post_id')
            if pid:
                post_counter[pid] += 1
            tags = post.get('tags', [])
            for tag in tags:
                tag_counter[tag] += 1
            tools = post.get('tools', [])
            for tool in tools:
                tool_counter[tool] += 1
            cluster = post.get('topic_cluster')
            if not cluster:
                if 'multi-agent' in tags:
                    cluster = 'agent-coordination'
                elif 'memory' in tags:
                    cluster = 'memory-systems'
                elif 'governance' in tags:
                    cluster = 'governance-and-control'
                elif 'framework' in tags or 'tooling' in tags:
                    cluster = 'toolchain-and-infra'
                elif 'evaluation' in tags:
                    cluster = 'evaluation-and-safety'
                elif 'economics' in tags:
                    cluster = 'agent-economics'
                else:
                    cluster = 'general-agent-ops'
            cluster_counter[cluster] += 1
            author = post.get('author')
            if author:
                author_counter[author] += 1
            top_posts.append({
                'post_id': pid,
                'title': post.get('title'),
                'topic_cluster': post.get('topic_cluster'),
                'tools': post.get('tools', []),
                'author': author,
                'score': post.get('score', 0),
                'artifact': artifact['_file'],
                'scanned_at': artifact.get('scanned_at'),
            })

    ratio = (posts_matched / posts_seen) if posts_seen else 0.0
    signal_band = 'low'
    if ratio >= 0.25:
        signal_band = 'high'
    elif ratio >= 0.10:
        signal_band = 'medium'

    trend_doc = {
        'schema_version': SCHEMA,
        'generated_at': now.isoformat().replace('+00:00', 'Z'),
        'window': {'days': args.days, 'start': since.isoformat().replace('+00:00', 'Z'), 'end': now.isoformat().replace('+00:00', 'Z')},
        'platform_context': {
            'platform_positioning': 'standalone ecosystem source under Meta ownership',
            'implication': 'track platform-native signal separately from owner-level strategic influence',
            'watch_items': [
                'whether Meta ownership changes audience quality or posting incentives',
                'whether platform discussion shifts toward Meta-aligned tooling or distribution patterns',
                'whether standalone community signal remains distinct from broader social noise',
            ],
        },
        'summary': {
            'artifacts_reviewed': len(artifacts),
            'posts_seen': posts_seen,
            'posts_matched': posts_matched,
            'signal_to_noise_ratio': round(ratio, 4),
            'signal_to_noise_band': signal_band,
            'status_breakdown': dict(status_counter),
        },
        'leaders': {
            'top_tags': top(tag_counter),
            'top_tools': top(tool_counter),
            'top_topic_clusters': top(cluster_counter),
            'top_authors': top(author_counter),
        },
        'daily_activity': [
            {'date': day, 'artifacts': info['artifacts'], 'posts_seen': info['posts_seen'], 'posts_matched': info['posts_matched'], 'statuses': dict(info['statuses'])}
            for day, info in sorted(daily.items())
        ],
        'repeated_posts': [{'post_id': pid, 'count': count} for pid, count in sorted(post_counter.items(), key=lambda kv: (-kv[1], kv[0])) if count > 1],
        'top_posts': sorted(top_posts, key=lambda x: (-x['score'], x['scanned_at'], x['post_id'] or ''))[:10],
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_path = args.out_dir / f'{now.date().isoformat()}.json'
    out_path.write_text(json.dumps(trend_doc, indent=2, ensure_ascii=False) + '\n')

    if args.emit_summary:
        top_clusters = ', '.join([x['name'] for x in trend_doc['leaders']['top_topic_clusters'][:2]]) or 'nincs'
        print(f'- Trend aggregátor kész: {len(artifacts)} artifact, S/N: {signal_band}, top cluster: {top_clusters}.')
        print(f'- Meta kontextus figyelve külön rétegben. File: {out_path.name}')
    else:
        print(out_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
