# Moltbook Phase 1 Operating Plan

## Goal
Run Moltbook Phase 1 as a lightweight, repeatable passive research workflow.

The purpose is to determine whether Moltbook produces enough technical signal to justify continued monitoring or later public participation.

## Mode
Phase 1 is passive in public behavior and deterministic in execution.

Allowed:
- reading public content
- calling the Moltbook API through a local script
- extracting signals
- storing findings as JSON artifacts
- weekly summaries
- ROI evaluation
- tracking source risk and platform defensibility

Not allowed:
- posting
- commenting
- messaging
- ad hoc manual public interaction as part of the recurring scan loop

## Platform Risk Constraint
Moltbook is no longer treated as an open, low-risk platform source.

Because of the updated Terms of Service:
- Moltbook should be treated as one input source, not the sole foundation of a future product
- publication or commercial reuse of Moltbook-derived structured intelligence requires separate review
- weekly review should consider both signal quality and platform/TOS risk

## Research Questions
During Phase 1, focus on answering these questions:

1. Are real autonomous agent operators active on Moltbook?
2. Which frameworks, tools, and architectures appear repeatedly?
3. Are there recurring multi-agent coordination patterns?
4. Are people sharing real operational failures, not just success stories?
5. Is the signal distinct enough to justify monitoring time?

## Monitoring Scope
Primary scope:
- `/m/general`

Secondary scope:
- any other public Moltbook threads that contain relevant discussion about AI agents, toolchains, architectures, failures, evaluation, safety, memory, or coordination

## Canonical Workflow
### Morning and evening scan
1. Run `moltbook_scan.py`
2. Save canonical JSON artifact under `artifacts/scans/`
3. Capture richer per-post metadata: source section, tags, tools, reply count, discussion depth, topic cluster, first seen date
4. Update `signals-log.md` only for newly captured relevant posts
5. Produce a short Telegram summary derived from the artifact

### Weekly review
1. Read recent scan artifacts
2. Run the trend aggregator to compute recurring tags, tools, topic clusters, repeated posts, and signal-to-noise ratio
3. Write weekly summary markdown
4. Send a short Telegram summary

### Trend aggregation
- run `moltbook_trend_aggregator.py`
- store deterministic trend artifacts under `artifacts/trends/`
- aggregate top tools and top topic clusters in addition to tags/authors
- keep platform-native findings separate from the Meta ownership context layer

## Relevance Criteria
Capture a post only if it contains at least one of the following:
- a named framework or stack
- a named tool or MCP/toolchain detail
- a concrete architecture pattern
- a deployment or integration pattern
- a multi-agent coordination method
- a real failure mode
- an operational lesson

Do not capture:
- vague hype
- generic inspiration
- shallow showcase posts with no technical substance
- repetitive low-value noise

## Deterministic Scoring
The script should use rule-based scoring.

Suggested weighting:
- named tool or framework: +0.25
- concrete failure mode: +0.25
- architecture or coordination pattern: +0.20
- operational lesson / governance detail: +0.20
- notable quote or dense technical content: +0.10

Confidence should be derived from score bands, not free-form intuition.

## Storage Rules
### Canonical storage
- `artifacts/scans/*.json`
- schema: `moltbook.scan.v1`

### Rolling log
- `signals-log.md`
- append only newly captured relevant findings
- human-readable derivative, not source of truth

### Weekly outputs
- weekly summary markdown document
- derived from artifacts and the rolling log

## Error Rules
If scan fails:
- still write a JSON artifact
- set `status: error`
- populate `errors[]`
- send a short Telegram error summary

This keeps every scheduled run auditable.

## Capture Frequency
Cadence:
- morning scan: daily
- evening scan: daily
- weekly summary: weekly

If the platform proves low-signal, reduce scan frequency instead of forcing activity.

## Output Set
Phase 1 should produce:
- deterministic JSON scan artifacts
- derived `signals-log.md` entries
- one weekly summary per 7-day block
- one ROI recommendation at each review point

## Decision Rule
After the first weekly review:
- continue Phase 1 if signal is promising
- reduce frequency if signal is weak but non-zero
- stop monitoring if signal is consistently low
- propose Phase 2 only if the separate decision note criteria are met
