#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import re
import urllib.request
from pathlib import Path
from typing import Any

BASE = Path('/home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon')
DEFAULT_CREDENTIALS = Path('/home/leoni/.openclaw/workspace/.secrets/moltbook/credentials.json')
ARTIFACTS_DIR = BASE / 'artifacts' / 'scans'
SIGNALS_LOG = BASE / 'signals-log.md'
SCHEMA = 'moltbook.scan.v1'
SECTION_MAP = {'general': '/m/general'}

TAG_RULES = {
    'framework': ['framework', 'langgraph', 'autogen', 'crewai', 'openclaw', 'sdk'],
    'multi-agent': ['multi-agent', 'planner', 'executor', 'supervisor', 'coordination', 'handoff'],
    'memory': ['memory', 'context', 'persistence', 'vector', 'embedding'],
    'governance': ['governance', 'policy', 'lineage', 'rollback', 'guardrail'],
    'reliability': ['reliability', 'audit', 'monitoring', 'alert', 'observability'],
    'evaluation': ['evaluation', 'benchmark', 'judge', 'score'],
    'tooling': ['tool', 'toolchain', 'mcp', 'cli', 'sdk', 'api'],
    'failure-mode': ['failure', 'timeout', 'stuck', 'incident', 'critical alert', 'zero output'],
    'deployment': ['docker', 'vps', 'cloud', 'kubernetes', 'local workstation'],
    'economics': ['roi', 'budget', 'cost', 'revenue', 'pricing'],
    'identity': ['identity', 'soul.md', 'clone', 'self'],
}
TOOL_PATTERNS = ['LangGraph', 'Redis', 'Docker', 'OpenClaw', 'MCP', 'Postgres', 'FastAPI', 'API', 'CLI', 'SDK', 'AutoGen', 'CrewAI']
TOPIC_CLUSTERS = {
    'agent-coordination': ['multi-agent', 'planner', 'executor', 'supervisor', 'coordination', 'handoff', 'queue'],
    'memory-systems': ['memory', 'context', 'persistence', 'vector', 'embedding'],
    'governance-and-control': ['governance', 'policy', 'rollback', 'guardrail', 'lineage', 'audit'],
    'toolchain-and-infra': ['toolchain', 'docker', 'mcp', 'sdk', 'api', 'cli', 'redis', 'postgres'],
    'evaluation-and-safety': ['evaluation', 'benchmark', 'judge', 'safety'],
    'agent-economics': ['roi', 'budget', 'cost', 'revenue', 'pricing'],
}
SIGNAL_RULES = {
    'named_tool_or_framework': ['langgraph', 'autogen', 'crewai', 'openclaw', 'mcp', 'redis', 'docker', 'api', 'cli', 'sdk'],
    'architecture_pattern': ['planner', 'executor', 'workflow', 'event-driven', 'supervisor'],
    'failure_mode': ['timeout', 'failure', 'stuck', 'critical alert', 'zero output', 'incident'],
    'operational_lesson': ['lesson', 'pattern', 'rule', 'contract', 'audit', 'rollback'],
}
RAW_ID_RE = re.compile(r'Raw post id: ([a-f0-9\-]+)')
QUOTE_SPLIT = re.compile(r'(?<=[.!?])\s+')


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def load_credentials(path: Path) -> dict[str, Any]:
    with path.open() as f:
        return json.load(f)


def api_get(url: str, api_key: str) -> dict[str, Any]:
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Bearer {api_key}')
    req.add_header('Accept', 'application/json')
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def normalize_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text or '').strip()


def load_existing_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return set(RAW_ID_RE.findall(path.read_text()))


def pick_tags(text: str) -> list[str]:
    lower = text.lower()
    return sorted([tag for tag, needles in TAG_RULES.items() if any(n in lower for n in needles)])


def pick_signals(text: str) -> list[str]:
    lower = text.lower()
    return [name for name, needles in SIGNAL_RULES.items() if any(n in lower for n in needles)]


def pick_tools(text: str) -> list[str]:
    lower = text.lower()
    found = []
    for tool in TOOL_PATTERNS:
        if tool.lower() in lower:
            found.append(tool)
    return sorted(set(found))


def pick_topic_cluster(text: str, tags: list[str]) -> str:
    lower = text.lower()
    for cluster, needles in TOPIC_CLUSTERS.items():
        if any(n in lower for n in needles):
            return cluster
    if 'framework' in tags:
        return 'toolchain-and-infra'
    return 'general-agent-ops'


def estimate_reply_count(post: dict[str, Any], text: str) -> int:
    for key in ['reply_count', 'replies_count', 'comments_count', 'comment_count']:
        value = post.get(key)
        if isinstance(value, int):
            return value
    lower = text.lower()
    return lower.count('reply') + lower.count('comment')


def estimate_discussion_depth(text: str, reply_count: int) -> int:
    lower = text.lower()
    depth = 1
    if any(x in lower for x in ['thread', 'discussion', 'reply', 'comment']):
        depth += 1
    if any(x in lower for x in ['nested', 'back-and-forth', 'chain', 'follow-up']):
        depth += 1
    if reply_count >= 10:
        depth += 1
    return depth


def first_quote(text: str) -> str:
    parts = QUOTE_SPLIT.split(normalize_text(text))
    for part in parts:
        if 40 <= len(part) <= 220:
            return part
    return normalize_text(text)[:180]


def score_post(text: str, tags: list[str], signals: list[str], tools: list[str], reply_count: int, depth: int) -> float:
    score = 0.0
    if tools or 'framework' in tags:
        score += 0.25
    if 'failure-mode' in tags or 'failure_mode' in signals:
        score += 0.25
    if 'multi-agent' in tags or 'architecture_pattern' in signals:
        score += 0.20
    if 'governance' in tags or 'operational_lesson' in signals or 'reliability' in tags:
        score += 0.20
    if len(text) > 300 or reply_count > 0 or depth > 1:
        score += 0.10
    return round(min(score, 1.0), 2)


def confidence_from_score(score: float) -> str:
    if score >= 0.8:
        return 'high'
    if score >= 0.45:
        return 'medium'
    return 'low'


def post_url(post: dict[str, Any]) -> str | None:
    if post.get('url'):
        return post['url']
    pid = post.get('id')
    return f'https://www.moltbook.com/posts/{pid}' if pid else None


def markdown_entry(entry: dict[str, Any]) -> str:
    tools = '\n'.join([f'      - {x}' for x in entry['tools']]) or '      - none'
    quote = entry['notable_quote'].replace('"', '\\"')
    title = entry['title'].replace('"', '\\"')
    return (
        f"  - date: {entry['first_seen']}\n"
        f"    post_url: {entry['url'] or 'null'}\n"
        f"    section: {entry['source_section']}\n"
        f"    author: {entry['author'] or 'unknown'}\n"
        f"    title_or_topic: \"{title}\"\n"
        f"    tools_used:\n{tools}\n"
        f"    topic_cluster: {entry['topic_cluster']}\n"
        f"    reply_count: {entry['reply_count']}\n"
        f"    discussion_depth: {entry['discussion_depth']}\n"
        f"    notable_quote: \"{quote}\"\n"
        f"    confidence: {entry['confidence']}\n"
        f"    notes: \"tags={','.join(entry['tags'])}; Raw post id: {entry['post_id']}\"\n"
    )


def update_signals_log(path: Path, entries: list[dict[str, Any]]) -> None:
    if not entries:
        return
    if not path.exists():
        path.write_text('# Moltbook Signals Log\n\n```yaml\nentries:\n```\n')
    text = path.read_text()
    block = ''.join(markdown_entry(e) for e in entries)
    marker = '```yaml\nentries:\n'
    if marker in text:
        text = text.replace(marker, marker + block, 1)
    else:
        text += '\n```yaml\nentries:\n' + block + '```\n'
    path.write_text(text)


def classify_post(post: dict[str, Any], existing_ids: set[str]) -> dict[str, Any] | None:
    text = normalize_text((post.get('title') or '') + '. ' + (post.get('content') or ''))
    if not text:
        return None
    post_id = str(post.get('id') or '')
    if not post_id or post_id in existing_ids:
        return None
    tags = pick_tags(text)
    signals = pick_signals(text)
    tools = pick_tools(text)
    if not tags and not signals and not tools:
        return None
    reply_count = estimate_reply_count(post, text)
    discussion_depth = estimate_discussion_depth(text, reply_count)
    topic_cluster = pick_topic_cluster(text, tags)
    score = score_post(text, tags, signals, tools, reply_count, discussion_depth)
    if score < 0.45:
        return None
    return {
        'post_id': post_id,
        'source_platform': 'moltbook',
        'source_section': SECTION_MAP.get(post.get('submolt_name') or 'general', f"/m/{post.get('submolt_name') or 'general'}"),
        'title': normalize_text(post.get('title') or 'untitled'),
        'tags': tags,
        'tools': tools,
        'reply_count': reply_count,
        'discussion_depth': discussion_depth,
        'topic_cluster': topic_cluster,
        'first_seen': utc_now().date().isoformat(),
        'author': (post.get('author') or {}).get('name') or 'unknown',
        'url': post_url(post),
        'created_at': post.get('created_at'),
        'score': score,
        'signals': signals,
        'confidence': confidence_from_score(score),
        'notable_quote': first_quote(text),
    }


def build_summary(entries: list[dict[str, Any]], posts_seen: int) -> dict[str, Any]:
    counter = {}
    for entry in entries:
        for tag in entry['tags']:
            counter[tag] = counter.get(tag, 0) + 1
    top_tags = [k for k, _ in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:3]]
    strength = 'low'
    if len(entries) >= 3:
        strength = 'high'
    elif len(entries) >= 1:
        strength = 'medium'
    return {'posts_seen': posts_seen, 'posts_matched': len(entries), 'signal_strength': strength, 'top_tags': top_tags}


def save_artifact(doc: dict[str, Any], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = doc['scanned_at'].replace(':', '-').replace('.', '-')
    path = out_dir / f'{ts}.json'
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--credentials', type=Path, default=DEFAULT_CREDENTIALS)
    parser.add_argument('--artifacts-dir', type=Path, default=ARTIFACTS_DIR)
    parser.add_argument('--signals-log', type=Path, default=SIGNALS_LOG)
    parser.add_argument('--limit', type=int, default=3)
    parser.add_argument('--emit-summary', action='store_true')
    args = parser.parse_args()
    now = utc_now().replace(microsecond=0)
    try:
        creds = load_credentials(args.credentials)
        feed = api_get('https://www.moltbook.com/api/v1/feed', creds['api_key'])
        posts = feed.get('posts', [])
        existing_ids = load_existing_ids(args.signals_log)
        entries = []
        for post in posts:
            entry = classify_post(post, existing_ids)
            if entry:
                entries.append(entry)
        entries = sorted(entries, key=lambda e: (-e['score'], e['post_id']))[:args.limit]
        update_signals_log(args.signals_log, entries)
        summary = build_summary(entries, len(posts))
        doc = {
            'schema_version': SCHEMA,
            'scan_id': now.isoformat().replace('+00:00', 'Z'),
            'scanned_at': now.isoformat().replace('+00:00', 'Z'),
            'source': {'platform': 'moltbook', 'endpoint': '/api/v1/feed', 'scope': ['general']},
            'status': 'ok' if entries else 'no_signal',
            'summary': summary,
            'posts': entries,
            'errors': [],
        }
        artifact = save_artifact(doc, args.artifacts_dir)
        if args.emit_summary:
            if entries:
                top_topics = ', '.join(summary['top_tags'][:2]) or 'nincs'
                print(f'- Moltbook scan kész: {summary["posts_matched"]} új releváns signal / {summary["posts_seen"]} poszt.')
                print(f'- Fő témák: {top_topics}. Artifact: {artifact.name}')
            else:
                print(f'- Moltbook scan kész: nincs új releváns signal. Artifact: {artifact.name}')
        else:
            print(json.dumps(doc, ensure_ascii=False))
        return 0
    except Exception as e:
        error_doc = {
            'schema_version': SCHEMA,
            'scan_id': now.isoformat().replace('+00:00', 'Z'),
            'scanned_at': now.isoformat().replace('+00:00', 'Z'),
            'source': {'platform': 'moltbook', 'endpoint': '/api/v1/feed', 'scope': ['general']},
            'status': 'error',
            'summary': {'posts_seen': 0, 'posts_matched': 0, 'signal_strength': 'low', 'top_tags': []},
            'posts': [],
            'errors': [{'code': e.__class__.__name__, 'message': str(e)}],
        }
        save_artifact(error_doc, args.artifacts_dir)
        if args.emit_summary:
            print(f'- Moltbook scan hiba: {e.__class__.__name__}: {e}')
        else:
            print(json.dumps(error_doc, ensure_ascii=False))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
