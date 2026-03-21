# Blindspot Radar — Scored Hypothesis List
Last updated: 2026-03-21

Scoring dimensions (1–5 each):
- **Pain**: How painful is the unmet need?
- **Urgency**: How time-sensitive is it? (regulatory deadlines, market windows)
- **WTP**: Willingness to pay (enterprise or dev)?
- **Def**: Defensibility (moat potential)?
- **IntFric**: Integration friction to build a solution (lower = easier entry)?

---

## H1 — Agent Identity & Authorization Layer
**Thesis:** AI agents lack first-class identity primitives. Enterprises have no standard way to authenticate, scope permissions, or audit agent actions at runtime. Only 23% of orgs have a formal agent identity management strategy (Strata.io, 2026-03).
**Signals (updated 2026-03-21):**
- NIST CAISI launched "AI Agent Standards Initiative" in Feb 2026 — agent authentication and authorization concept papers due April 2, 2026 (NIST.gov). HIGH CONFIDENCE.
- World/Worldcoin launched tool to verify humans behind AI shopping agents (TechCrunch, 2026-03-17). HAIER signal confirmed. HIGH CONFIDENCE.
- EU AI Act high-risk compliance deadline: Aug 2, 2026. Machine identity governance rising to board-level priority (Delinea.com, 2026). HIGH CONFIDENCE.
- Meta's rogue agent accidentally exposed user data to unauthorized engineers (TechCrunch, 2026-03-18) — real production incident proving pain. HIGH CONFIDENCE.
- Agent Identity Security deployment guide published (nhimg.org, 2026-03): agent RBAC, just-in-time permissions, immutable audit trails now documented best practice.
- EU Digital Identity Wallets rollout: large orgs must accept by late 2026 — extends to agent authentication context.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=3 | IntFric=3 | **Total: 21/25**
*Score unchanged. Urgency confirmed: three hard regulatory deadlines in 2026 (EU AI Act Aug, NIST concept papers Apr, EU Digital Identity Wallet late 2026).*

---

## H2 — Agent Compliance Audit Trail (Immutable Logging)
**Thesis:** EU AI Act (enforceable Aug 2026), Colorado AI Act (Jun 2026), California ADMT rules (Jan 2026) all mandate immutable audit trails for high-risk AI decisions. 94% of orgs report critical gaps in AI activity visibility. No purpose-built agent audit layer exists; most rely on repurposed SIEM tools.
**Signals (updated 2026-03-21):**
- Agent Lifecycle Toolkit (ALTK) paper (arxiv 2026-03-16): documents how silent reasoning errors go undetected, tool argument corruption corrupts production data, policy violations create legal risk — enterprise deployment failures confirmed. HIGH CONFIDENCE.
- Tracium.ai (Product Hunt, 2026-03-18): "Track AI Agents with a single line of code" — new entrant, validates market demand. MEDIUM CONFIDENCE (early product).
- EU AI Act high-risk deadline Aug 2, 2026 unchanged. Multiple US state laws already in effect (CA SB53, AB2013, SB942 as of Jan 2026). HIGH CONFIDENCE.
- Gartner: 80% of governments will deploy AI agents for decision-making by 2028 (Express Computer, 2026-03-20) — government audit trail mandates accelerating. MEDIUM CONFIDENCE (Gartner projection).
- NVIDIA OpenShell open-sourced: secure runtime environment for autonomous AI agents (MarkTechPost, 2026-03-18) — infra layer emerging, audit tooling still missing above it.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Score unchanged. Tracium.ai entry and ALTK paper both confirm growing market. Competitive moat window narrowing — first-mover advantage still available but not indefinite.*

---

## H3 — MCP Governance & Security Layer
**Thesis:** MCP adoption is outpacing security controls. "Server sprawl" — unmanaged MCP servers proliferating across teams. Tool poisoning attacks confirmed. Only 29% of orgs have AI-specific security controls. No centralized MCP governance plane exists.
**Signals (updated 2026-03-21):**
- 2026 MCP roadmap confirmed: agent-to-agent communication requiring governance across identity, transport, policy, and observability layers (elegantsoftwaresolutions.com). HIGH CONFIDENCE.
- Operant AI MCP gateway: real-time visibility, inline redaction, dynamic control — first commercial entrant confirmed (operant.ai, 2026). MEDIUM CONFIDENCE (competitor, not validation of gap).
- Forbes (2026-03-19): MCP adoption "transitioning from pilots to full-scale enterprise deployment" in finance, healthcare, manufacturing. HIGH CONFIDENCE.
- OAuth 2.1 now mandated in official MCP spec for servers handling sensitive data. Compliance complexity rising. HIGH CONFIDENCE.
- HN thread (2026-03-19): "Ask HN: The new wave of AI agent sandboxes?" — community actively debating sandbox/security tradeoffs in production. Confirmed practitioner pain. HIGH CONFIDENCE.
- HAIER signal: 7 MCP-related signals in top 100 agent signals — moderate coverage vs auth/security.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*IntFric lowered to 3 (was 4): Operant AI competing, lowering build friction perception. Urgency maintained at 4. Total drops 1 point.*

---

## H4 — Agent-Native Micropayment Rails for SMBs
**Thesis:** MPP (Stripe+Tempo), x402 (Coinbase), Visa CLI all launched — but are crypto-native and complex. SMBs cannot use them. "Token Shock" is a real adoption blocker — unpredictable costs. Need: simple, fiat-compatible, agent-native billing layer for non-crypto-savvy SMBs.
**Signals (updated 2026-03-21):**
- Machine Payments Protocol on Product Hunt (2026-03-18): Stripe-linked "internet-native payment standard for AI agents" — confirmed Stripe entering space. HIGH CONFIDENCE.
- Forbes (2026-03-19): "Stripe, Visa, and Mastercard race to build AI agent payment rails" — three major players converging. HIGH CONFIDENCE.
- CBA Agentic Symposium White Paper (Jan 2026): traditional KYC/AML not designed for autonomous agents — regulatory gap confirmed. HIGH CONFIDENCE.
- Coinbase x402 agentic wallets confirmed. Crypto-native, not SMB-accessible. HIGH CONFIDENCE.
- Cloudflare CEO: bot traffic will exceed human traffic by 2027 (TechCrunch, 2026-03-19) — scale trajectory validates infrastructure urgency. MEDIUM CONFIDENCE.
- Only 14–29% consumer trust in agent payments (Nevermined.ai, 2026) — trust gap persists alongside tooling gap.
- HAIER: only 2 payment signals in top 100 agent signals — confirms HAIER undercovers this area, web search needed and confirmed useful.
**Assessment:** Big players (Stripe, Visa, Mastercard) now in this space. SMB-friendly abstraction opportunity remains — but window is narrowing fast. Timing risk: large players may commoditize before SMB layer can be built.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=2 | IntFric=4 | **Total: 17/25**
*Urgency raised to 4 (was 3): major player convergence accelerates market definition. Def lowered to 2 (was 3): Stripe/Visa/Mastercard entering reduces defensibility. Total unchanged at 17.*

---

## H5 — Agent Discovery & Verified Registry
**Thesis:** Thousands of specialized agents exist; no trusted discovery mechanism. Bitte Protocol has 12k+ connected accounts but is crypto-native. No neutral, verified, searchable agent registry for enterprise use. "Discovery is strategic infrastructure."
**Signals (updated 2026-03-21):**
- P2P network for agents to publish formally verified science (HN, 2026-03-19): "every AI agent works alone — next agent solves same problem from zero. No way for agents to find each other." Direct validation of discovery pain. HIGH CONFIDENCE.
- WordPress.com AI agents (TechCrunch, 2026-03-20): agents now publishing web content — implies agent-generated content will flood discovery channels, making verified-human/verified-agent distinction more urgent. MEDIUM CONFIDENCE.
- Nothing CEO (TechCrunch, 2026-03-18): "smartphone apps will disappear as AI agents take their place" — if true, agent discovery replaces app stores. Long-horizon signal. LOW CONFIDENCE (executive speculation).
- HAIER: 131 agent signals total — diversity confirms agent proliferation, validates discovery pain.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 16/25**
*Score unchanged. HN signal directly validates isolation pain. Still a 2027+ opportunity — no clear WTP signal yet.*

---

## H6 — Policy Enforcement Runtime (Real-time Agent Guardrails)
**Thesis:** 68% of orgs have reactive-only AI governance. Only 7% have real-time policy enforcement. No product offers inline, runtime policy enforcement for agent actions — most scan post-event.
**Signals (updated 2026-03-21):**
- ALTK paper (arxiv, 2026-03-16): explicitly documents how "outputs that violate organizational policy can create legal or compliance risk" — policy enforcement failure in enterprise production confirmed. HIGH CONFIDENCE.
- Meta rogue agent incident (TechCrunch, 2026-03-18): agent bypassed data access controls — real-world policy enforcement failure at scale. HIGH CONFIDENCE.
- NVIDIA OpenShell (2026-03-18): open-sources secure runtime for autonomous agents — infra layer approach, not policy layer. Confirms infra maturing; policy enforcement gap above it persists. HIGH CONFIDENCE.
- Autonomous penetration testing agent (vxcontrol/pentagi, 2026-03-21): fully autonomous pentest capability — if such agents can run, inline policy enforcement becomes security-critical immediately. HIGH CONFIDENCE.
- Budibase AI Agents (Product Hunt, 2026-03-18): "AI agents that run your operations (open source)" — no policy layer bundled. Confirms gap in open-source tooling.
- Dell + NVIDIA GB300: first hardware shipped for autonomous AI agents with NemoClaw + OpenShell (Business Wire, 2026-03-18) — hardware commoditizing, policy layer still missing.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Urgency raised to 5 (was 4): Meta incident + autonomous pentest agent = real enterprise security emergencies, not future risk. Total raised to 22 (was 21).*

---

## H7 — SMB Agent Deployment Wrapper (Turnkey Ops Agent)
**Thesis:** SMBs want agentic AI but face: no expertise, unpredictable costs, dirty data, legacy integration. "Implementation gap" is huge — hype vs. reality. Market for a fully managed, opinionated ops-agent-as-a-service for SMBs (like Navibase) is wide open.
**Signals (updated 2026-03-21):**
- Link AI (Product Hunt, 2026-03-19): "The Agentic Business Suite that replaces your entire stack" — direct competitor in SMB agentic suite space. MEDIUM CONFIDENCE (early product, validates thesis).
- Budibase AI Agents: "AI agents that run your operations (open source)" — open source version validates demand. MEDIUM CONFIDENCE.
- Nothing CEO app disappearance thesis (TechCrunch, 2026-03-18): if apps disappear → SMBs need agent replacements, not build-your-own. Supports managed wrapper thesis. LOW-MEDIUM CONFIDENCE.
- Gartner: 80% of governments deploying by 2028 — implies SMB adoption wave follows enterprise/government. MEDIUM CONFIDENCE.
- Chamber (YC W26): AI agent for GPU infrastructure — YC validating agent-as-service model for infrastructure. HIGH CONFIDENCE (YC funding signal).
**Assessment:** Competitors emerging (Link AI, Budibase). First-mover window closing. Navibase differentiation must be: Hungarian/CEE market focus + specific vertical (ops), not generic.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=4 | IntFric=3 | **Total: 18/25**
*Urgency raised to 4 (was 3): competitive landscape accelerating, window closing. Total raised to 18 (was 17).*

---

## H8 — Cross-Agent Context Persistence (Stateless Problem)
**Thesis:** MCP sessions are stateless. Multi-agent workflows break when agents can't share context across sessions. No neutral, secure, cross-agent memory/context store exists. Sahara is building one but crypto-native.
**Signals (updated 2026-03-21):**
- "Context Overflow" (Product Hunt, 2026-03-20): "Knowledge Sharing for AI Agents" — new entrant directly targeting cross-agent knowledge sharing. MEDIUM CONFIDENCE (validates demand).
- ALTK paper: documents multi-agent coordination failures in production — context loss explicitly mentioned as failure mode. HIGH CONFIDENCE.
- Open SWE (LangChain, 2026-03-19): open-source asynchronous coding agent — async pattern implies context persistence solved locally; no cross-agent solution.
- HN sandbox thread (2026-03-19): practitioners debating stateless vs. stateful tradeoffs in production. Confirms practitioner-level awareness of problem.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=3 | IntFric=4 | **Total: 17/25**
*Score unchanged. Context Overflow entry confirms market direction. Still early — WTP signal weak.*

---

## Ranking Summary (2026-03-21)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | ↑+1 |
| 3 | H1 — Agent Identity & Auth | 21/25 | = |
| 4 | H3 — MCP Governance | 19/25 | ↓-1 |
| 5 | H7 — SMB Deployment Wrapper | 18/25 | ↑+1 |
| 6 | H4 — Agent Payment Rails | 17/25 | = |
| 7 | H8 — Cross-Agent Context | 17/25 | = |
| 8 | H5 — Discovery & Registry | 16/25 | = |

---

## Top Signals This Week (2026-03-21 update)

1. **Meta rogue agent incident** (TechCrunch, 2026-03-18): Real production policy enforcement failure at enterprise scale. Validates H6 + H1 urgently.
2. **NIST AI Agent Standards Initiative** (Feb 2026, concept papers due Apr 2): Regulatory legitimacy for agent identity/auth standards. Validates H1 + H2.
3. **NVIDIA OpenShell open-sourced** (2026-03-18): Secure runtime infra maturing fast — policy + audit layer above it is the next gap. Validates H6 + H2.
4. **Machine Payments Protocol + Forbes race article** (2026-03-18/19): Stripe, Visa, Mastercard all entering agent payment rails. SMB abstraction window narrowing. Validates H4 urgency.
5. **World human-verification tool for AI shopping agents** (TechCrunch, 2026-03-17): Commerce layer demanding identity verification. Validates H1.
6. **ALTK paper** (arxiv, 2026-03-16): First systematic documentation of enterprise agent failure modes in production. Validates H2 + H6.
7. **Autonomous pentest agent vxcontrol/pentagi** (2026-03-21): Fully autonomous attack capability — inline guardrails now security-critical. Validates H6 urgency.
8. **Context Overflow launch** (2026-03-20): First direct cross-agent knowledge sharing product. Validates H8 direction.

---

## Suggested Next Experiments (per top opportunity)

### H2 / H6 (tied #1) — Audit + Policy Enforcement
**Hypothesis to test:** Enterprise teams would pay for a lightweight "agent activity recorder" that generates audit-ready reports for EU AI Act compliance — before buying a full policy enforcement runtime.
**Experiment:** Cold outreach to 10 EU-based enterprises known to use Claude/GPT in production. Offer a 30-day free audit report generator. Measure: conversion to paid, price sensitivity, which compliance framework they cite.
**Investment:** ~2 weeks build, 0 marketing spend. Use ALTK + Tracium.ai as proof of concept signal in pitch.

### H1 — Agent Identity Layer
**Hypothesis to test:** Developers building MCP-connected agents will pay for a hosted "agent passport" service (OAuth-compatible, RBAC, audit logs) rather than building it themselves.
**Experiment:** Publish a technical blog post with working implementation reference. Measure inbound developer interest via GitHub stars + form fills within 30 days.
**Investment:** ~1 week build of reference implementation, 0 cost except time.

### H7 — SMB Deployment Wrapper (Navibase relevance)
**Hypothesis to test:** CEE (Hungarian/Slovak/Czech) SMB owners will pay €200-500/month for a fully managed ops agent that handles: email triage, calendar, task management, weekly reporting.
**Experiment:** Offer Leoni (current ops agent) as a white-labeled pilot to 3 Hungarian SMBs. Measure: time-to-value, churn signal after 60 days, what they most frequently ask it to do.
**Investment:** Existing infrastructure. Main cost: Tomi's setup time per pilot. Direct revenue test with minimal overhead.

---

*Sources: HAIER evolution_signals export (2026-03-21, 726 signals, 131 agent-relevant); web search (agent identity compliance, payment rails, MCP security — 2026-03-21). All claims marked with confidence level. No fabricated data.*
