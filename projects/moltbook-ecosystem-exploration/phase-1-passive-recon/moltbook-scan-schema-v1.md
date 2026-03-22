# Moltbook Scan Schema v1

Schema name:
- `moltbook.scan.v1`

Purpose:
- define the canonical machine-readable output of a Moltbook deterministic scan
- provide a stable contract for cron jobs, weekly review, trend aggregation, dashboards, and future publishing

## Design Rules
- one JSON artifact per scan run
- artifact is append-only historical output
- human-readable summaries are derived from this artifact
- post objects should carry enough metadata for later clustering, ranking, and discovery use cases
- `status` must always be present
- `errors` must always be present, even when empty

## Top-Level Object

```json
{
  "schema_version": "moltbook.scan.v1",
  "scan_id": "2026-03-15T22:20:00Z",
  "scanned_at": "2026-03-15T22:20:00Z",
  "source": {
    "platform": "moltbook",
    "endpoint": "/api/v1/feed",
    "scope": ["general"]
  },
  "status": "ok",
  "summary": {
    "posts_seen": 20,
    "posts_matched": 3,
    "signal_strength": "high",
    "top_tags": ["framework", "multi-agent", "memory"]
  },
  "posts": [],
  "errors": []
}
```

## Required Top-Level Fields
- `schema_version`: string, fixed `moltbook.scan.v1`
- `scan_id`: string, unique scan id
- `scanned_at`: string, ISO-8601 UTC timestamp
- `source`: object
- `status`: string
- `summary`: object
- `posts`: array
- `errors`: array

## Post Object

```json
{
  "post_id": "123",
  "source_platform": "moltbook",
  "source_section": "/m/general",
  "title": "...",
  "tags": ["framework", "multi-agent"],
  "tools": ["LangGraph", "Redis"],
  "reply_count": 12,
  "discussion_depth": 3,
  "topic_cluster": "agent-coordination",
  "first_seen": "2026-03-15"
}
```

## Required Post Fields

### `post_id`
- Type: string
- Stable source identifier

### `source_platform`
- Type: string
- Fixed value for this pipeline: `moltbook`

### `source_section`
- Type: string
- Example: `/m/general`

### `title`
- Type: string
- Normalized post title

### `tags`
- Type: string[]
- Normalized topical tags

Suggested values include:
- `framework`
- `multi-agent`
- `memory`
- `governance`
- `reliability`
- `evaluation`
- `tooling`
- `failure-mode`
- `deployment`
- `economics`
- `identity`

### `tools`
- Type: string[]
- Concrete software, frameworks, infra, or technical components mentioned or clearly implied in the agent system

Examples:
- `LangGraph`
- `Redis`
- `Docker`
- `OpenClaw`
- `MCP`
- `Postgres`
- `FastAPI`

### `reply_count`
- Type: integer
- Number of replies/comments if available
- Default `0` when unavailable

### `discussion_depth`
- Type: integer
- Heuristic depth score for the discussion tree or technical thread depth
- Default `1` when unavailable

### `topic_cluster`
- Type: string
- Normalized cluster label for downstream trend analysis

Examples:
- `agent-coordination`
- `memory-systems`
- `governance-and-control`
- `toolchain-and-infra`
- `evaluation-and-safety`
- `agent-economics`

### `first_seen`
- Type: string
- Date in `YYYY-MM-DD`
- First date the system captured this post

## Optional Post Fields
These can remain in v1 and are useful downstream:
- `author`
- `url`
- `created_at`
- `score`
- `signals`
- `confidence`
- `notable_quote`

## Error Object
```json
{
  "code": "network_error",
  "message": "Connection timed out while calling /api/v1/feed"
}
```

## Scoring Guidance
Recommended deterministic weighting:
- named tool/framework/component: `+0.25`
- concrete failure mode: `+0.25`
- architecture/coordination pattern: `+0.20`
- operational lesson/governance detail: `+0.20`
- dense technical quote/content: `+0.10`

Clamp score to `1.0`.

## Downstream Uses
This schema is intended to support:
- daily Telegram summaries
- weekly aggregation
- trend detection
- ecosystem radar dashboards
- AI ecosystem intelligence publishing
- future discovery/ranking pages
- later agent registration and profile enrichment workflows

## Versioning Rule
If a breaking field change is introduced:
- create a new schema version
- example: `moltbook.scan.v2`
- do not silently redefine `v1`
