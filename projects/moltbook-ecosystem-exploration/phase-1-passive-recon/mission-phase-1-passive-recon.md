# MISSION: Moltbook Passive Recon

Agent name: Leoni  
Role: Passive ecosystem research agent

## OBJECTIVE
Observe Moltbook.com to determine whether it is a high-value signal source for the emerging AI agent ecosystem.

The goal of Phase 1 is not public participation. The goal is to assess signal quality, identify recurring technical patterns, and determine whether later active participation would have meaningful ROI.

## PHASE 1 BOUNDARY
Phase 1 remains strictly passive in public behavior.

Do not:
- publish posts
- comment publicly
- message users
- create a public identity footprint beyond what already exists

If meaningful ROI becomes visible, active participation can be proposed later as a separate mission.

## OPERATING PRINCIPLE: DETERMINISTIC FIRST
Phase 1 is now **JSON-first and deterministic**.

The primary output of each scan is not a free-form narrative. The primary output is a structured JSON artifact that can be:
- diffed
- aggregated
- tested
- summarized later
- reused by cron, weekly review, and Telegram reporting

Human summaries are derived outputs.
The canonical scan result is the JSON artifact.

## PLATFORM / TOS RISK LAYER
Moltbook must now be treated as a **high platform-risk source** due to the updated Terms of Service.

Operational implication:
- Moltbook is a research input source, not the product itself.
- Moltbook-derived intelligence should be treated as internal research unless and until publication risk is re-evaluated.
- Future ecosystem intelligence products should be multi-source, with Moltbook as one input among others.

This mission therefore tracks two things in parallel:
1. signal quality
2. source defensibility / TOS risk

## STEP 1 — DETERMINISTIC SCAN
Run a local scan script against Moltbook.

The script is responsible for:
- loading credentials from workspace secrets
- calling the Moltbook API
- applying deterministic relevance rules
- scoring posts using rule-based logic
- storing one canonical JSON artifact
- appending only new relevant items to the rolling signal log

## STEP 2 — RELEVANCE FILTER
Only keep discussions that contain at least one of the following:
- a concrete tool, framework, or stack
- a real implementation detail
- an architecture pattern
- a reported failure mode
- a coordination pattern between multiple agents
- a practical deployment or operations lesson

Ignore:
- hype-only posts
- generic motivational content
- shallow demos with no technical detail
- repetitive noise

## STEP 3 — STRUCTURED OUTPUT CONTRACT
Each scan must emit a deterministic JSON document under the schema:
- `moltbook.scan.v1`

Required top-level fields:
- `schema_version`
- `scan_id`
- `scanned_at`
- `source`
- `status`
- `summary`
- `posts`
- `errors`

Required per-post fields:
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

Recommended enrichment fields:
- `author`
- `url`
- `created_at`
- `score`
- `signals`
- `confidence`
- `notable_quote`

## STEP 4 — STORAGE LAYERS
### Canonical machine-readable storage
- `artifacts/scans/*.json`

### Human-readable rolling log
- `signals-log.md`
- derived from scan artifacts
- should remain compact and append-only for new signal

### Weekly synthesis
- weekly summary markdown output
- derived from scan artifacts and the rolling log

## STEP 5 — TELEGRAM REPORTING
Telegram reports should be short and derived from the JSON artifact.

Daily scan report should say only:
- whether there was meaningful new signal
- 1-2 top themes
- or that there was no meaningful new signal

No long narrative unless there is an actual anomaly.

## STEP 6 — WEEKLY SUMMARY
Every 7 days produce a short summary covering:
- most mentioned tools
- most discussed frameworks
- recurring engineering problems
- emerging coordination patterns
- signal-to-noise assessment
- whether Moltbook appears worth deeper monitoring

## STEP 7 — ROI DECISION GATE
At the end of each weekly summary, answer this explicitly:

1. Is Moltbook producing real technical signal?
2. Is it different from what can already be learned from GitHub, X, blogs, and docs?
3. Would public participation likely create additional value?
4. Is there enough ROI to justify Phase 2?

## PHASE 2 CRITERIA
Only propose Phase 2 if at least one of the following becomes true:
- repeated high-quality technical discussions appear
- operators of real autonomous agents share implementation details
- the platform shows unique coordination patterns not easily found elsewhere
- direct participation would likely generate better information than passive observation

## POSSIBLE PHASE 2
If Phase 1 proves high ROI, a later mission may include:
- minimal profile hygiene if needed
- one restrained intro post
- selective technical commenting

That would require a separate go/no-go decision.

## END OF MISSION
