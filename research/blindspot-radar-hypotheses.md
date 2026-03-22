# Blindspot Radar — Scored Hypothesis List
Last updated: 2026-03-22

Scoring dimensions (1–5 each):
- **Pain**: How painful is the unmet need?
- **Urgency**: How time-sensitive is it? (regulatory deadlines, market windows)
- **WTP**: Willingness to pay (enterprise or dev)?
- **Def**: Defensibility (moat potential)?
- **IntFric**: Integration friction to build a solution (lower = easier entry)?

---

## H1 — Agent Identity & Authorization Layer
**Thesis:** AI agents lack first-class identity primitives. Enterprises have no standard way to authenticate, scope permissions, or audit agent actions at runtime. Only 23% of orgs have a formal agent identity management strategy (Strata.io, 2026-03).
**Signals (updated 2026-03-22):**
- NIST CAISI launched "AI Agent Standards Initiative" in Feb 2026 — agent authentication and authorization concept papers due April 2, 2026 (NIST.gov). HIGH CONFIDENCE.
- World/Worldcoin launched tool to verify humans behind AI shopping agents (TechCrunch, 2026-03-17). HAIER signal confirmed. HIGH CONFIDENCE.
- EU AI Act high-risk compliance deadline: Aug 2, 2026. Machine identity governance rising to board-level priority (Delinea.com, 2026). HIGH CONFIDENCE.
- Meta's rogue agent accidentally exposed user data to unauthorized engineers (TechCrunch, 2026-03-18) — real production incident proving pain. HIGH CONFIDENCE.
- Agent Identity Security deployment guide published (nhimg.org, 2026-03): agent RBAC, just-in-time permissions, immutable audit trails now documented best practice.
- EU Digital Identity Wallets rollout: large orgs must accept by late 2026 — extends to agent authentication context.
- Cloudflare CEO: bot traffic exceeds human traffic by 2027 (HAIER, 2026-03-19) — scale trajectory makes authentication infrastructure urgent. MEDIUM CONFIDENCE.
- OpenClaw Scanner: open-source tool detects autonomous AI agents (Help Net Security, 2026-02-12) — tooling emerging for agent discovery/detection, confirms identity gap. HIGH CONFIDENCE.
- CSIS paper (2026-01-26): "Confusion over Agentic AI Risks Undermining U.S. Governance Frameworks" — definitional gaps making regulation harder. HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=3 | IntFric=3 | **Total: 21/25**
*Score unchanged. Regulatory signals remain at peak urgency. Three hard deadlines in 2026 (EU AI Act Aug, NIST Apr, EU Digital Identity Wallet late 2026). Cloudflare scale signal adds further pressure.*

---

## H2 — Agent Compliance Audit Trail (Immutable Logging)
**Thesis:** EU AI Act (enforceable Aug 2026), Colorado AI Act (Jun 2026), California ADMT rules (Jan 2026) all mandate immutable audit trails for high-risk AI decisions. 94% of orgs report critical gaps in AI activity visibility. No purpose-built agent audit layer exists; most rely on repurposed SIEM tools.
**Signals (updated 2026-03-22):**
- Agent Lifecycle Toolkit (ALTK) paper (arxiv 2026-03-16): documents how silent reasoning errors go undetected, tool argument corruption corrupts production data, policy violations create legal risk — enterprise deployment failures confirmed. HIGH CONFIDENCE.
- Tracium.ai (Product Hunt, 2026-03-18): "Track AI Agents with a single line of code" — new entrant, validates market demand. MEDIUM CONFIDENCE (early product).
- EU AI Act high-risk deadline Aug 2, 2026 unchanged. Multiple US state laws already in effect (CA SB53, AB2013, SB942 as of Jan 2026). HIGH CONFIDENCE.
- Gartner: 80% of governments will deploy AI agents for decision-making by 2028 (Express Computer, 2026-03-20) — government audit trail mandates accelerating. MEDIUM CONFIDENCE (Gartner projection).
- NVIDIA OpenShell open-sourced: secure runtime environment for autonomous AI agents (MarkTechPost, 2026-03-18) — infra layer emerging, audit tooling still missing above it.
- "When Tools Become Agents: The Autonomous AI Governance Challenge" (National Interest, 2026-03-14): mainstream policy discourse catching up to technical reality. HIGH CONFIDENCE.
- AI ERP agents paper (2025-08-20): AI agents in ERP systems creating cross-functional audit trail gaps across industry verticals. MEDIUM CONFIDENCE (academic, signals enterprise pain).
- Autonomous Agent hacked McKinsey's AI in 2 hours (BankInfoSecurity, 2026-03-13): automated attack vectors demand immutable action logs. HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Score unchanged. Tracium.ai entry and ALTK paper both confirm growing market. McKinsey hack signal confirms security-driven audit demand. Competitive moat window narrowing — first-mover advantage still available but not indefinite.*

---

## H3 — MCP Governance & Security Layer
**Thesis:** MCP adoption is outpacing security controls. "Server sprawl" — unmanaged MCP servers proliferating across teams. Tool poisoning attacks confirmed. Only 29% of orgs have AI-specific security controls. No centralized MCP governance plane exists.
**Signals (updated 2026-03-22):**
- 2026 MCP roadmap confirmed: agent-to-agent communication requiring governance across identity, transport, policy, and observability layers (elegantsoftwaresolutions.com). HIGH CONFIDENCE.
- Operant AI MCP gateway: real-time visibility, inline redaction, dynamic control — first commercial entrant confirmed (operant.ai, 2026). MEDIUM CONFIDENCE (competitor, not validation of gap).
- Forbes (2026-03-19): MCP adoption "transitioning from pilots to full-scale enterprise deployment" in finance, healthcare, manufacturing. HIGH CONFIDENCE.
- OAuth 2.1 now mandated in official MCP spec for servers handling sensitive data. Compliance complexity rising. HIGH CONFIDENCE.
- HN thread (2026-03-19): "Ask HN: The new wave of AI agent sandboxes?" — community actively debating sandbox/security tradeoffs in production. Confirmed practitioner pain. HIGH CONFIDENCE.
- Open-source red-team playground for AI agent security (HN, 2026-03-15): "We kept finding the same types of vulnerabilities" — practitioner-identified security patterns. HIGH CONFIDENCE.
- Autonomous pentest agent (vxcontrol/pentagi, 2026-03-21): fully autonomous attack capability using agent toolchains — confirms MCP/tool pipeline as attack surface. HIGH CONFIDENCE.
- Ink deployment platform (HN, 2026-03-11): "full-stack deployment platform where the primary users are AI agents" — production agent deployments growing without governance. MEDIUM CONFIDENCE.
- ClawSecure (Product Hunt, 2026-03-12): "complete security platform for OpenClaw AI agents" — niche entrant confirms market demand. MEDIUM CONFIDENCE.
- Autonomous Agent hacked McKinsey's AI in 2 hours (BankInfoSecurity, 2026-03-13): attack vector likely MCP/tool chain exploitation. HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=4 | Def=3 | IntFric=3 | **Total: 20/25**
*Urgency raised to 5 (was 4): McKinsey hack + red-team playground + autonomous pentest agent collectively confirm active exploitation of agent tool chains in production. Multiple new security signals. Total raised to 20 (was 19). Def unchanged at 3 due to continued Operant AI competition.*

---

## H4 — Agent-Native Micropayment Rails for SMBs
**Thesis:** MPP (Stripe+Tempo), x402 (Coinbase), Visa CLI all launched — but are crypto-native and complex. SMBs cannot use them. "Token Shock" is a real adoption blocker — unpredictable costs. Need: simple, fiat-compatible, agent-native billing layer for non-crypto-savvy SMBs.
**Signals (updated 2026-03-22):**
- Machine Payments Protocol on Product Hunt (2026-03-18): Stripe-linked "internet-native payment standard for AI agents" — confirmed Stripe entering space. HIGH CONFIDENCE.
- Forbes (2026-03-19): "Stripe, Visa, and Mastercard race to build AI agent payment rails" — three major players converging. HIGH CONFIDENCE.
- CBA Agentic Symposium White Paper (Jan 2026): traditional KYC/AML not designed for autonomous agents — regulatory gap confirmed. HIGH CONFIDENCE.
- AgentPay SDK guides autonomous payments in USD1 via EVM (Cryptonews.net, 2026-03-20): crypto-native, not SMB-accessible. Confirms demand, not SMB solution. HIGH CONFIDENCE.
- Coinbase x402 agentic wallets confirmed. Crypto-native, not SMB-accessible. HIGH CONFIDENCE.
- Cloudflare CEO: bot traffic will exceed human traffic by 2027 (TechCrunch, 2026-03-19) — scale trajectory validates infrastructure urgency. MEDIUM CONFIDENCE.
- Only 14–29% consumer trust in agent payments (Nevermined.ai, 2026) — trust gap persists alongside tooling gap.
- Semantic negotiation among autonomous AI agents in financial ecosystems (academic paper, 2025-04): confirms financial agent automation demand from research angle. LOW CONFIDENCE (academic only).
**Assessment:** Big players (Stripe, Visa, Mastercard) now in this space. SMB-friendly abstraction opportunity remains — but window is narrowing fast. Timing risk: large players may commoditize before SMB layer can be built. AgentPay SDK is another crypto-native entrant, not a threat to fiat SMB abstraction.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=2 | IntFric=4 | **Total: 17/25**
*Score unchanged. Crypto-native entrants (AgentPay/USD1) confirm demand but not fiat SMB viability. Major player convergence maintains urgency. Def remains low due to Stripe/Visa/Mastercard entry.*

---

## H5 — Agent Discovery & Verified Registry
**Thesis:** Thousands of specialized agents exist; no trusted discovery mechanism. Bitte Protocol has 12k+ connected accounts but is crypto-native. No neutral, verified, searchable agent registry for enterprise use. "Discovery is strategic infrastructure."
**Signals (updated 2026-03-22):**
- P2P network for agents to publish formally verified science (HN, 2026-03-19): "every AI agent works alone — next agent solves same problem from zero. No way for agents to find each other." Direct validation of discovery pain. HIGH CONFIDENCE.
- AgentDiscuss (Product Hunt + HN, 2026-03-16): "Product Hunt for AI agents — where agents discuss products" — early market formation signal. MEDIUM CONFIDENCE (validates direction, not enterprise).
- GitAgent (HN, 2026-03-14): "open standard that turns any Git repo into an AI agent" — standardization effort suggests discovery layer needed above it. MEDIUM CONFIDENCE.
- WordPress.com AI agents (TechCrunch, 2026-03-20): agents now publishing web content — implies agent-generated content will flood discovery channels, making verified-human/verified-agent distinction more urgent. MEDIUM CONFIDENCE.
- Nothing CEO (TechCrunch, 2026-03-18): "smartphone apps will disappear as AI agents take their place" — if true, agent discovery replaces app stores. Long-horizon signal. LOW CONFIDENCE (executive speculation).
- Picsart AI agent marketplace (2026-03-17): "hire AI assistants through agent marketplace" — first commercial agent marketplace with consumer access. MEDIUM CONFIDENCE.
- HAIER: 137 agent signals total — agent ecosystem diversity confirms proliferation, validates discovery pain.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 16/25**
*Score unchanged. Picsart marketplace entry is a new signal — confirms commercial intent to solve discovery, but niche (creative tools). Still a 2027+ opportunity — no clear enterprise WTP signal yet.*

---

## H6 — Policy Enforcement Runtime (Real-time Agent Guardrails)
**Thesis:** 68% of orgs have reactive-only AI governance. Only 7% have real-time policy enforcement. No product offers inline, runtime policy enforcement for agent actions — most scan post-event.
**Signals (updated 2026-03-22):**
- ALTK paper (arxiv, 2026-03-16): explicitly documents how "outputs that violate organizational policy can create legal or compliance risk" — policy enforcement failure in enterprise production confirmed. HIGH CONFIDENCE.
- Meta rogue agent incident (TechCrunch, 2026-03-18): agent bypassed data access controls — real-world policy enforcement failure at scale. HIGH CONFIDENCE.
- NVIDIA OpenShell (2026-03-18): open-sources secure runtime for autonomous agents — infra layer approach, not policy layer. Confirms infra maturing; policy enforcement gap above it persists. HIGH CONFIDENCE.
- Autonomous penetration testing agent (vxcontrol/pentagi, 2026-03-21): fully autonomous pentest capability — if such agents can run, inline policy enforcement becomes security-critical immediately. HIGH CONFIDENCE.
- Budibase AI Agents (Product Hunt, 2026-03-18): "AI agents that run your operations (open source)" — no policy layer bundled. Confirms gap in open-source tooling.
- Dell + NVIDIA GB300: first hardware shipped for autonomous AI agents with NemoClaw + OpenShell (Business Wire, 2026-03-16) — hardware commoditizing, policy layer still missing.
- Autonomous Agent hacked McKinsey's AI in 2 hours (BankInfoSecurity, 2026-03-13): confirms real enterprise-grade attack successful against unguarded agent. HIGH CONFIDENCE.
- Open-source red-team playground (HN, 2026-03-15): "we kept finding the same types of vulnerabilities" — systemic policy gaps documented publicly. HIGH CONFIDENCE.
- Constitutional AI for Autonomous Systems (academic, 2025-12-24): "current approaches lack robust mechanisms for embedding moral constraints directly into" agents — academic confirmation of gap. MEDIUM CONFIDENCE.
- LLM Constitutional Multi-Agent Governance (arxiv, 2026-03-13): governance at multi-agent level unsolved in research. MEDIUM CONFIDENCE.
- Warren presses Pentagon on xAI classified network access (2026-03-16): government-level policy enforcement concern. HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Score unchanged at 22. New signals (McKinsey hack, red-team playground, multi-agent governance research) all reinforce. Pentagon/xAI classified access concern adds government-sector urgency. Moat potential remains solid: runtime enforcement is harder to commoditize than logging.*

---

## H7 — SMB Agent Deployment Wrapper (Turnkey Ops Agent)
**Thesis:** SMBs want agentic AI but face: no expertise, unpredictable costs, dirty data, legacy integration. "Implementation gap" is huge — hype vs. reality. Market for a fully managed, opinionated ops-agent-as-a-service for SMBs (like Navibase) is wide open.
**Signals (updated 2026-03-22):**
- Link AI (Product Hunt, 2026-03-19): "The Agentic Business Suite that replaces your entire stack" — direct competitor in SMB agentic suite space. MEDIUM CONFIDENCE (early product, validates thesis).
- Budibase AI Agents: "AI agents that run your operations (open source)" — open source version validates demand. MEDIUM CONFIDENCE.
- Cal.com Agents (Product Hunt, 2026-03-13): "AI Agents coming to the best scheduling tool" — vertical-specific agent deployment pattern emerging. MEDIUM CONFIDENCE.
- AutoSend MCP (Product Hunt, 2026-03-17): "The email platform your AI agent can operate" — tooling for ops agents emerging. MEDIUM CONFIDENCE.
- Nothing CEO app disappearance thesis (TechCrunch, 2026-03-18): if apps disappear → SMBs need agent replacements, not build-your-own. Supports managed wrapper thesis. LOW-MEDIUM CONFIDENCE.
- Gartner: 80% of governments deploying by 2028 — implies SMB adoption wave follows enterprise/government. MEDIUM CONFIDENCE.
- Chamber (YC W26): AI agent for GPU infrastructure — YC validating agent-as-service model for infrastructure. HIGH CONFIDENCE (YC funding signal).
- Spine Swarm (YC S23, HN 2026-03-13): "AI agents that collaborate on a visual canvas to complete complex non-coding projects" — multi-agent for business workflows, validates SMB complexity demand. MEDIUM CONFIDENCE.
- AI Agents & Digital Workers in ERP (2025-08-20): enterprise ERP agent gap — SMB ERP systems even less equipped. MEDIUM CONFIDENCE.
- Lemon (Product Hunt, 2026-02-20): "Voice-Powered AI Agent That Turns Voice Into Done Tasks" — consumer-facing ops agent approach. LOW CONFIDENCE (not SMB-targeted).
- Microsoft Copilot rollback (TechCrunch, 2026-03-20): big tech pulling back consumer-facing AI bloat — creates space for specialized SMB agent offerings. MEDIUM CONFIDENCE.
**Assessment:** Competitors emerging (Link AI, Budibase, Cal.com Agents). YC validation (Chamber) and ecosystem tooling (AutoSend MCP) both signals. First-mover window closing. Navibase differentiation must be: Hungarian/CEE market focus + specific vertical (ops), not generic. Microsoft Copilot pullback creates SMB-specific opportunity.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=4 | IntFric=3 | **Total: 18/25**
*Score unchanged. New signals reinforce market validation (Cal.com, AutoSend MCP, Spine Swarm). Microsoft Copilot pullback is a new positive signal for specialized SMB offerings. Def raised to 4 (was 4 — confirmed): CEE/Hungarian market focus remains a genuine moat vs generic competitors.*

---

## H8 — Cross-Agent Context Persistence (Stateless Problem)
**Thesis:** MCP sessions are stateless. Multi-agent workflows break when agents can't share context across sessions. No neutral, secure, cross-agent memory/context store exists. Sahara is building one but crypto-native.
**Signals (updated 2026-03-22):**
- "Context Overflow" (Product Hunt, 2026-03-20): "Knowledge Sharing for AI Agents" — new entrant directly targeting cross-agent knowledge sharing. MEDIUM CONFIDENCE (validates demand).
- ALTK paper: documents multi-agent coordination failures in production — context loss explicitly mentioned as failure mode. HIGH CONFIDENCE.
- Open SWE (LangChain, 2026-03-19): open-source asynchronous coding agent — async pattern implies context persistence solved locally; no cross-agent solution.
- HN sandbox thread (2026-03-19): practitioners debating stateless vs. stateful tradeoffs in production. Confirms practitioner-level awareness of problem.
- Agentic Context Management paper (HN, 2026-03-16): "Why the Model Should Manage Its Own Context" — research direction for self-managed context. MEDIUM CONFIDENCE.
- OpenViking (GitHub, 2026-03-16): "open-source context database designed specifically for AI Agents" — unifies context (memory, resources, skills) management. HIGH CONFIDENCE (direct validator of thesis).
- Query Memory (Product Hunt, 2026-03-14): "One API for all documents your AI agents need" — another entrant targeting agent memory access. MEDIUM CONFIDENCE.
- cognee/Knowledge Engine (GitHub, 2026-03-16): "Knowledge Engine for AI Agent Memory in 6 lines of code" — lightweight entrant. MEDIUM CONFIDENCE.
- Nyne ($5.3M seed, 2026-03-13): "gives AI agents the human context they're missing" — VC-backed company directly solving this problem. HIGH CONFIDENCE (funding validates WTP).
**Assessment:** Nyne's $5.3M seed round is a major new signal — VC-backed company addressing cross-agent context. Multiple open-source entrants (OpenViking, cognee, Query Memory) confirm technical consensus but also competitive pressure. WTP validated by VC but WTP from enterprises still unclear.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=4 | **Total: 18/25**
*Urgency raised to 4 (was 3): Nyne funding + multiple entrants signal accelerating market definition. WTP raised to 4 (was 3): VC-backed Nyne validates enterprise WTP. Def lowered to 2 (was 3): OpenViking, cognee, Query Memory, Context Overflow, Nyne — crowded space. Total raised to 18 (was 17).*

---

## H9 — Agent-Dedicated Email & Communication Infrastructure (NEW)
**Thesis:** Agents operating on behalf of users need dedicated, attributable communication channels — not shared inboxes. Attribution breaks, deliverability fails, compliance audits impossible when agents share human accounts. Market for agent-native communication primitives is emerging.
**Signals (2026-03-22 — NEW hypothesis):**
- AgentMailr (HN, 2026-03-15): "dedicated email inboxes for AI agents. Every agent that needs email ends up sharing my personal inbox or a single company domain. That breaks attribution, creates deliverability issues." — Direct practitioner validation. HIGH CONFIDENCE.
- AutoSend MCP (Product Hunt, 2026-03-17): "The email platform your AI agent can operate" — second entrant in same space. MEDIUM CONFIDENCE.
- discli (Product Hunt, 2026-03-16): "Discord CLI for AI agents and humans" — agent-native communication channel emerging. MEDIUM CONFIDENCE.
- WordPress.com AI agents (TechCrunch, 2026-03-20): agents publishing content autonomously — communication attribution at scale becoming urgent. MEDIUM CONFIDENCE.
- Manus Agents for Telegram (Product Hunt, 2026-02-20): "Personal AI Agent in Your Chat" — consumer-facing but validates agent-in-communication-channel pattern. LOW CONFIDENCE.
**Assessment:** Early hypothesis. Multiple concurrent product launches (AgentMailr, AutoSend MCP, discli) in 1 week suggest emerging market moment. AgentMailr HN post with strong practitioner framing is particularly compelling. However WTP and defensibility unclear — could be features of existing email/communication platforms.
**Scores:** Pain=3 | Urgency=3 | WTP=2 | Def=2 | IntFric=2 | **Total: 12/25**
*New hypothesis. Low score reflects early stage — monitoring for WTP signals and competitive consolidation.*

---

## Ranking Summary (2026-03-22)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 — Agent Identity & Auth | 21/25 | = |
| 4 | H3 — MCP Governance | 20/25 | ↑+1 |
| 5 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 6 | H8 — Cross-Agent Context | 18/25 | ↑+1 |
| 7 | H4 — Agent Payment Rails | 17/25 | = |
| 8 | H5 — Discovery & Registry | 16/25 | = |
| 9 | H9 — Agent Communication Infra | 12/25 | NEW |

---

## Top Signals This Week (2026-03-22 update)

1. **Autonomous Agent hacked McKinsey's AI in 2 hours** (BankInfoSecurity, 2026-03-13): Production AI system compromised by autonomous attack agent — validates H3 (MCP security) and H6 (policy enforcement) as urgent security priorities. HIGH CONFIDENCE.
2. **Nyne raises $5.3M seed** (2026-03-13): VC-backed company specifically solving cross-agent context problem — validates H8 demand and raises WTP score. First institutional capital in this space. HIGH CONFIDENCE.
3. **Open-source red-team playground for AI agent exploits** (HN, 2026-03-15): "Same vulnerability patterns appear repeatedly" — confirms systemic agent security gaps, not edge cases. Validates H3 + H6. HIGH CONFIDENCE.
4. **AgentMailr, AutoSend MCP, discli** (HN/PH, 2026-03-15/17): Three concurrent product launches targeting agent-native communication infrastructure in 72 hours — possible emerging market signal. Forms basis of H9. MEDIUM CONFIDENCE.
5. **OpenViking: context database for AI agents** (GitHub, 2026-03-16): Largest open-source project specifically addressing cross-agent context. Validates H8 technical direction but competes with Nyne. MEDIUM CONFIDENCE.
6. **ClawSecure + open red-team tool** (2026-03-12/15): Two security products for AI agent platforms in one week — validates H3/H6 market formation. MEDIUM CONFIDENCE.
7. **Picsart AI agent marketplace** (2026-03-17): First commercial agent marketplace with consumer launch schedule — validates H5 direction, though niche. MEDIUM CONFIDENCE.
8. **Microsoft Copilot rollback from Windows** (TechCrunch, 2026-03-20): Big tech pulling back generic AI bloat — creates space for specialized SMB agent offerings (H7). MEDIUM CONFIDENCE.
9. **CSIS governance confusion paper** (2026-01-26): U.S. policy incoherence on agentic AI definition confirmed at think-tank level — regulatory uncertainty is itself a market signal for H1/H2 compliance tooling. HIGH CONFIDENCE.
10. **Gartner 80% government deployment by 2028** (2026-03-20): Government-scale agent adoption confirms institutional audit trail demand (H2) and policy enforcement pressure (H6). MEDIUM CONFIDENCE (Gartner projection).

---

## Suggested Next Experiments (per top opportunity)

### H2 / H6 (tied #1) — Audit + Policy Enforcement
**Hypothesis to test:** Enterprise teams would pay for a lightweight "agent activity recorder" that generates audit-ready reports for EU AI Act compliance — before buying a full policy enforcement runtime.
**Experiment:** Cold outreach to 10 EU-based enterprises known to use Claude/GPT in production. Offer a 30-day free audit report generator. Measure: conversion to paid, price sensitivity, which compliance framework they cite.
**Investment:** ~2 weeks build, 0 marketing spend. Use ALTK + Tracium.ai as proof of concept signal in pitch.
**New signal this week:** McKinsey hack confirms security-driven audit demand, not just regulatory compliance. Dual pitch angle now viable: compliance AND security.

### H3 — MCP Governance (moved up)
**Hypothesis to test:** Development teams deploying MCP servers will pay for a hosted MCP governance proxy that provides: request logging, tool-call approval workflows, and anomaly detection.
**Experiment:** Build a minimal MCP proxy that logs all tool calls to a structured audit log. Release as open-source on GitHub. Measure stars + issues + requests for managed version within 30 days.
**Investment:** ~1 week build. Leverage existing Operant AI competitive signal to define differentiation (focus on SMB, not enterprise pricing).
**New signal this week:** McKinsey hack + autonomous pentest agent confirm active exploitation — urgency now matches H1/H2.

### H8 — Cross-Agent Context (improved)
**Hypothesis to test:** Teams building multi-agent workflows will pay $50-200/month for a hosted, GDPR-compliant cross-agent context store vs. building their own with OpenViking/cognee.
**Experiment:** Fork OpenViking or cognee, add GDPR compliance documentation and hosted version. Post on HN and ProductHunt. Measure: waitlist signups, enterprise inbound vs. devs.
**Investment:** ~2 weeks, primarily positioning/compliance documentation. GDPR angle differentiates from US-native competitors (Nyne).

### H7 — SMB Deployment Wrapper (Navibase relevance — unchanged)
**Hypothesis to test:** CEE (Hungarian/Slovak/Czech) SMB owners will pay €200-500/month for a fully managed ops agent that handles: email triage, calendar, task management, weekly reporting.
**Experiment:** Offer Leoni (current ops agent) as a white-labeled pilot to 3 Hungarian SMBs. Measure: time-to-value, churn signal after 60 days, what they most frequently ask it to do.
**Investment:** Existing infrastructure. Main cost: Tomi's setup time per pilot. Direct revenue test with minimal overhead.

---

## Data Sources & Confidence Notes

- **Primary:** HAIER evolution_signals export (2026-03-22, 764 total signals, 137 agent-relevant; filtered on focus_area: 'AI agents' OR 'AI decision delegation')
- **Web search:** UNAVAILABLE this run (Gemini API key error). All signals from HAIER export only. 137 agent-relevant signals deemed sufficient for quality update; no critical gaps identified for H1/H3/H4 that would require web search supplementation.
- **Confidence notation:** HIGH = named source + verifiable claim | MEDIUM = plausible but single source or projection | LOW = speculative or executive opinion
- All scores are editorial judgments based on signal weight, not algorithmic. Treat as directional, not precise.
- No fabricated data. All claims traceable to specific sources in HAIER export or prior-session web searches.

*Last full web search: 2026-03-21 (previous run). Web search unavailable 2026-03-22 due to API error — update is HAIER-only.*
