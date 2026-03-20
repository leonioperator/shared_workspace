# Blindspot Radar — Scored Hypothesis List
Last updated: 2026-03-20

Scoring dimensions (1–5 each):
- **Pain**: How painful is the unmet need?
- **Urgency**: How time-sensitive is it? (regulatory deadlines, market windows)
- **WTP**: Willingness to pay (enterprise or dev)?
- **Def**: Defensibility (moat potential)?
- **IntFric**: Integration friction to build a solution (lower = easier entry)?

---

## H1 — Agent Identity & Authorization Layer
**Thesis:** AI agents lack first-class identity primitives. Enterprises have no standard way to authenticate, scope permissions, or audit agent actions at runtime. Only 23% of orgs have a formal agent identity management strategy (Strata.io, 2026-03).
**Signals:** Google A2A, Anthropic MCP, IBM ACP all launched but none includes native identity binding. CyberArk and Okta writing about "agent sprawl" as critical risk. eIDAS 2.0 mandating digital identity wallets (EU deadline: end 2026).
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=3 | IntFric=3 | **Total: 21/25**

## H2 — Agent Compliance Audit Trail (Immutable Logging)
**Thesis:** EU AI Act (enforceable Aug 2026), Colorado AI Act (Jun 2026), California ADMT rules (Jan 2026) all mandate immutable audit trails for high-risk AI decisions. 94% of orgs report critical gaps in AI activity visibility. No purpose-built agent audit layer exists; most rely on repurposed SIEM tools.
**Signals:** EU AI Act full enforcement Aug 2, 2026. Multiple US state deadlines Q1-Q2 2026. Enterprise demand for "audit-ready AI" accelerating.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**

## H3 — MCP Governance & Security Layer
**Thesis:** MCP adoption is outpacing security controls. "Server sprawl" — unmanaged MCP servers proliferating across teams. Tool poisoning attacks confirmed. Only 29% of orgs have AI-specific security controls. No centralized MCP governance plane exists.
**Signals:** VentureBeat (2026): "Enterprise MCP adoption is outpacing security controls." Portkey.ai, Solo.io writing guides on MCP governance gaps. Splx.ai selling MCP security tooling (early market).
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=4 | **Total: 20/25**

## H4 — Agent-Native Micropayment Rails for SMBs
**Thesis:** MPP (Stripe+Tempo), x402 (Coinbase), Visa CLI all launched — but are crypto-native and complex. SMBs cannot use them. "Token Shock" is a real adoption blocker — unpredictable costs. Need: simple, fiat-compatible, agent-native billing layer for non-crypto-savvy SMBs.
**Signals:** Tempo mainnet launched March 2026. Forbes (March 19, 2026): "Stripe, Visa, Mastercard race to build AI agent payment rails." Only 14–29% consumer trust in agent payments (Nevermined.ai, 2026). SMB-targeted tooling absent.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=3 | IntFric=4 | **Total: 17/25**

## H5 — Agent Discovery & Verified Registry
**Thesis:** Thousands of specialized agents exist; no trusted discovery mechanism. Bitte Protocol has 12k+ connected accounts but is crypto-native. No neutral, verified, searchable agent registry for enterprise use. "Discovery is strategic infrastructure" (HackMD, 2026).
**Signals:** AI agent market $12–15B projected for 2026. Agent Conference 2026 lists hundreds of agents with no quality signal. Bitte, Rivalz, Sahara all targeting this — all crypto-native.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 16/25**

## H6 — Policy Enforcement Runtime (Real-time Agent Guardrails)
**Thesis:** 68% of orgs have reactive-only AI governance. Only 7% have real-time policy enforcement. No product offers inline, runtime policy enforcement for agent actions — most scan post-event.
**Signals:** Gravitee.io State of AI Agent Security 2026. Accelirate "agentic AI governance crisis" report. Microsoft Entra 2026 report on AI access control gaps. Beam.ai security article (2026).
**Scores:** Pain=5 | Urgency=4 | WTP=5 | Def=4 | IntFric=3 | **Total: 21/25**

## H7 — SMB Agent Deployment Wrapper (Turnkey Ops Agent)
**Thesis:** SMBs want agentic AI but face: no expertise, unpredictable costs, dirty data, legacy integration. "Implementation gap" is huge — hype vs. reality. Market for a fully managed, opinionated ops-agent-as-a-service for SMBs (like Navibase) is wide open.
**Signals:** ChannelE2E (2026): "AI agents will filter down to SMBs in 2026." Techaisle SMB top-10 priorities 2026 list agents #1. Forbes Feb 2026: "Overcoming barriers to AI adoption."
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=4 | IntFric=3 | **Total: 17/25**

## H8 — Cross-Agent Context Persistence (Stateless Problem)
**Thesis:** MCP sessions are stateless. Multi-agent workflows break when agents can't share context across sessions. No neutral, secure, cross-agent memory/context store exists. Sahara is building one but crypto-native.
**Signals:** MCP documentation (2026): stateless sessions explicitly noted as limitation. Multiple enterprise MCP guides mention this as top operational gap.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=3 | IntFric=4 | **Total: 17/25**
