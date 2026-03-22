# Moltbook Phase 1 — Deterministic JSON Workflow

## Goal
Make Moltbook Phase 1 deterministic, scriptable, and easy to debug.

The primary output is a structured JSON scan artifact with richer per-post metadata for later trend analysis, ranking, publishing, and discovery workflows.

## Source of Truth
Each scan produces one canonical JSON artifact under:
- `artifacts/scans/YYYY-MM-DDTHH-MM-SSZ.json`

Schema:
- `moltbook.scan.v1`

## Scan Pipeline
1. Load credentials from workspace secrets.
2. Call Moltbook `/api/v1/feed`.
3. Apply deterministic relevance, tagging, tool extraction, topic clustering, and scoring rules.
4. Save one JSON artifact.
5. Append only new relevant items to `signals-log.md`.
6. Derive a short Telegram summary from the artifact.

## Required Post Metadata
Each captured post should include at minimum:
- `post_id`
- `source_platform`
- `source_section`
- `title`
- `tags`
- `tools`
- `reply_count`
- `discussion_depth`
- `topic_cluster`
- `first_seen`

## Storage Layers
### 1. Canonical machine output
- `artifacts/scans/*.json`

### 2. Human-readable rolling log
- `signals-log.md`
- derived from scan artifacts
- not the primary source of truth

### 3. Weekly synthesis
- weekly summary markdown file
- derived from scan artifacts plus the rolling log

### 4. Trend layer
- trend artifacts under `artifacts/trends/*.json`
- aggregate tags, topic clusters, tools, authors, repeated posts, daily activity, and signal-to-noise ratio
- keep Meta ownership context as a separate strategic interpretation layer, not mixed into native post data
- track Moltbook as a source with platform/TOS risk, not as a product-safe canonical public dataset on its own

## Scheduling
### Morning scan
- quick deterministic scan
- 1-3 new relevant items max
- short Telegram summary

### Evening scan
- same scan flow
- short Telegram summary

### Weekly review
- aggregate recent scan artifacts
- summarize recurring tools, topic clusters, engineering problems, and ROI
- short Telegram summary + weekly markdown output

## Error Handling
If scan fails, still emit a JSON artifact with:
- `status: error`
- populated `errors[]`

This keeps the run auditable.

## Why this design
Pros:
- deterministic
- testable
- diffable
- low token cost
- stable cron behavior
- richer structured output for future ecosystem radar / discovery use cases

Tradeoff:
- less flexible than a fully open-ended agent-first scan
- but far better for repeatable monitoring and later productization
