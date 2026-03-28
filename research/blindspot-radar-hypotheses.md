# Blindspot Radar — Scored Hypothesis List
Last updated: 2026-03-23

Scoring dimensions (1–5 each):
- **Pain**: How painful is the unmet need?
- **Urgency**: How time-sensitive is it? (regulatory deadlines, market windows)
- **WTP**: Willingness to pay (enterprise or dev)?
- **Def**: Defensibility (moat potential)?
- **IntFric**: Integration friction to build a solution (lower = easier entry)?

---

## H1 — Agent Identity & Authorization Layer
**Thesis:** AI agents lack first-class identity primitives. Enterprises have no standard way to authenticate, scope permissions, or audit agent actions at runtime. Only 23% of orgs have a formal agent identity management strategy (Strata.io, 2026-03).
**Signals (updated 2026-03-23):**
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
*Score unchanged. No new signals today. Regulatory deadlines remain at peak urgency (NIST Apr 2, EU AI Act Aug 2, EU Digital Identity Wallet late 2026). Stable.*

---

## H2 — Agent Compliance Audit Trail (Immutable Logging)
**Thesis:** EU AI Act (enforceable Aug 2026), Colorado AI Act (Jun 2026), California ADMT rules (Jan 2026) all mandate immutable audit trails for high-risk AI decisions. 94% of orgs report critical gaps in AI activity visibility. No purpose-built agent audit layer exists; most rely on repurposed SIEM tools.
**Signals (updated 2026-03-23):**
- Agent Lifecycle Toolkit (ALTK) paper (arxiv 2026-03-16): documents how silent reasoning errors go undetected, tool argument corruption corrupts production data, policy violations create legal risk — enterprise deployment failures confirmed. HIGH CONFIDENCE.
- Tracium.ai (Product Hunt, 2026-03-18): "Track AI Agents with a single line of code" — new entrant, validates market demand. MEDIUM CONFIDENCE (early product).
- EU AI Act high-risk deadline Aug 2, 2026 unchanged. Multiple US state laws already in effect (CA SB53, AB2013, SB942 as of Jan 2026). HIGH CONFIDENCE.
- Gartner: 80% of governments will deploy AI agents for decision-making by 2028 (Express Computer, 2026-03-20) — government audit trail mandates accelerating. MEDIUM CONFIDENCE (Gartner projection).
- NVIDIA OpenShell open-sourced: secure runtime environment for autonomous AI agents (MarkTechPost, 2026-03-18) — infra layer emerging, audit tooling still missing above it.
- "When Tools Become Agents: The Autonomous AI Governance Challenge" (National Interest, 2026-03-14): mainstream policy discourse catching up to technical reality. HIGH CONFIDENCE.
- Autonomous Agent hacked McKinsey's AI in 2 hours (BankInfoSecurity, 2026-03-13): automated attack vectors demand immutable action logs. HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Score unchanged. No new signals today. Tracium.ai entry and ALTK paper both confirm growing market. McKinsey hack signal confirms security-driven audit demand. Competitive moat window narrowing — first-mover advantage still available but not indefinite.*

---

## H3 — MCP Governance & Security Layer
**Thesis:** MCP adoption is outpacing security controls. "Server sprawl" — unmanaged MCP servers proliferating across teams. Tool poisoning attacks confirmed. Only 29% of orgs have AI-specific security controls. No centralized MCP governance plane exists.
**Signals (updated 2026-03-23):**
- 2026 MCP roadmap confirmed: agent-to-agent communication requiring governance across identity, transport, policy, and observability layers (elegantsoftwaresolutions.com). HIGH CONFIDENCE.
- Operant AI MCP gateway: real-time visibility, inline redaction, dynamic control — first commercial entrant confirmed. MEDIUM CONFIDENCE (competitor).
- Forbes (2026-03-19): MCP adoption "transitioning from pilots to full-scale enterprise deployment" in finance, healthcare, manufacturing. HIGH CONFIDENCE.
- OAuth 2.1 now mandated in official MCP spec for servers handling sensitive data. Compliance complexity rising. HIGH CONFIDENCE.
- HN sandbox thread (2026-03-19): practitioners debating sandbox/security tradeoffs in production. Confirmed practitioner pain. HIGH CONFIDENCE.
- Open-source red-team playground for AI agent security (HN, 2026-03-15): "We kept finding the same types of vulnerabilities." HIGH CONFIDENCE.
- Autonomous pentest agent (vxcontrol/pentagi, 2026-03-21): fully autonomous attack capability using agent toolchains — confirms MCP/tool pipeline as attack surface. HIGH CONFIDENCE.
- browser-use GitHub trending (2026-03-23): browser automation as standard agent primitive — adds browser tool calls as unaudited attack surface. MEDIUM CONFIDENCE (new today).
- Autonomous Agent hacked McKinsey's AI in 2 hours (BankInfoSecurity, 2026-03-13). HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=4 | Def=3 | IntFric=3 | **Total: 20/25**
*Score unchanged. browser-use trending (Mar 23) confirms browser tool calls becoming standard — expands MCP/tool attack surface. Insufficient to change scores.*

---

## H4 — Agent-Native Micropayment Rails for SMBs
**Thesis:** MPP (Stripe+Tempo), x402 (Coinbase), Visa CLI all launched — but are crypto-native and complex. SMBs cannot use them. Need: simple, fiat-compatible, agent-native billing layer for non-crypto-savvy SMBs.
**Signals (updated 2026-03-23):**
- Machine Payments Protocol on Product Hunt (2026-03-18): Stripe-linked "internet-native payment standard for AI agents." HIGH CONFIDENCE.
- Forbes (2026-03-19): "Stripe, Visa, and Mastercard race to build AI agent payment rails." HIGH CONFIDENCE.
- CBA Agentic Symposium White Paper (Jan 2026): traditional KYC/AML not designed for autonomous agents — regulatory gap confirmed. HIGH CONFIDENCE.
- AgentPay SDK guides autonomous payments in USD1 via EVM (Cryptonews.net, 2026-03-20): crypto-native, not SMB-accessible. HIGH CONFIDENCE.
- Coinbase x402 agentic wallets confirmed. Crypto-native, not SMB-accessible. HIGH CONFIDENCE.
- TradingAgents (GitHub, 2026-03-21): Multi-Agents LLM Financial Trading Framework — financial domain agents proliferating, payment rail demand confirmed. MEDIUM CONFIDENCE (new this run).
- Only 14-29% consumer trust in agent payments (Nevermined.ai, 2026) — trust gap persists.
**Assessment:** Big players (Stripe, Visa, Mastercard) now in this space. SMB-friendly fiat abstraction opportunity remains — but window is narrowing.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=2 | IntFric=4 | **Total: 17/25**
*Score unchanged. TradingAgents (Mar 21) confirms financial domain agent proliferation. Crypto-native entrants still not solving fiat SMB gap.*

---

## H5 — Agent Discovery & Verified Registry
**Thesis:** Thousands of specialized agents exist; no trusted discovery mechanism. No neutral, verified, searchable agent registry for enterprise use.
**Signals (updated 2026-03-23):**
- P2P network for agent science (HN, 2026-03-19): "No way for agents to find each other." Direct validation. HIGH CONFIDENCE.
- AgentDiscuss (Product Hunt + HN, 2026-03-16): "Product Hunt for AI agents." MEDIUM CONFIDENCE.
- GitAgent (HN, 2026-03-14): "open standard that turns any Git repo into an AI agent" — discovery layer needed above it. MEDIUM CONFIDENCE.
- Picsart AI agent marketplace (2026-03-17): first commercial agent marketplace with consumer access. MEDIUM CONFIDENCE.
- ClawRun (2026-03-21): "Deploy and manage AI agents in seconds" — implies catalog/registry component. MEDIUM CONFIDENCE (new this run).
- HAIER: 143 agent signals — ecosystem diversity confirms proliferation, validates discovery pain.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 16/25**
*Score unchanged. ClawRun minor new signal. Still a 2027+ opportunity — no clear enterprise WTP signal yet.*

---

## H6 — Policy Enforcement Runtime (Real-time Agent Guardrails)
**Thesis:** 68% of orgs have reactive-only AI governance. Only 7% have real-time policy enforcement. No product offers inline, runtime policy enforcement for agent actions.
**Signals (updated 2026-03-23):**
- ALTK paper (arxiv, 2026-03-16): "outputs that violate organizational policy can create legal or compliance risk" — confirmed in enterprise production. HIGH CONFIDENCE.
- Meta rogue agent incident (TechCrunch, 2026-03-18): agent bypassed data access controls at scale. HIGH CONFIDENCE.
- NVIDIA OpenShell (2026-03-18): infra layer maturing; policy enforcement gap above it persists. HIGH CONFIDENCE.
- Autonomous pentest agent (vxcontrol/pentagi, 2026-03-21): fully autonomous attack capability — inline policy enforcement becomes security-critical. HIGH CONFIDENCE.
- Dell brings autonomous AI agents to the desktop (AEC Magazine, 2026-03-21): policy enforcement scope expands to edge/desktop. MEDIUM CONFIDENCE (new this run).
- Dell + NVIDIA GB300: first hardware shipped for autonomous agents — hardware commoditizing, policy layer missing. Business Wire, 2026-03-16.
- Autonomous Agent hacked McKinsey's AI in 2 hours (BankInfoSecurity, 2026-03-13). HIGH CONFIDENCE.
- Open-source red-team playground (HN, 2026-03-15): systemic policy gaps documented. HIGH CONFIDENCE.
- Warren presses Pentagon on xAI classified network access (2026-03-16): government-level policy enforcement concern. HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Score unchanged. Dell desktop signal (Mar 21) confirms policy enforcement scope expanding to edge. All prior signals intact.*

---

## H7 — SMB Agent Deployment Wrapper (Turnkey Ops Agent)
**Thesis:** SMBs want agentic AI but face: no expertise, unpredictable costs, dirty data, legacy integration. Market for a fully managed, opinionated ops-agent-as-a-service for SMBs (like Navibase) is wide open.
**Signals (updated 2026-03-23):**
- ClawRun (2026-03-21): "Deploy and manage AI agents in seconds" — new deployment platform validates low-friction agent ops demand. MEDIUM CONFIDENCE (new this run).
- browser-use GitHub trending (2026-03-23): browser automation for AI agents — standard ops primitive maturing, reduces build complexity for SMB wrapper. MEDIUM CONFIDENCE (new today).
- production-agentic-rag-course (2026-03-23): Education demand signal — growing cohort of agent builders, adoption wave incoming. LOW CONFIDENCE (indirect, new today).
- Link AI (Product Hunt, 2026-03-19): "The Agentic Business Suite that replaces your entire stack." MEDIUM CONFIDENCE.
- Budibase AI Agents: "AI agents that run your operations (open source)." MEDIUM CONFIDENCE.
- Cal.com Agents (Product Hunt, 2026-03-13): vertical-specific agent deployment pattern. MEDIUM CONFIDENCE.
- AutoSend MCP (Product Hunt, 2026-03-17): email platform for ops agents. MEDIUM CONFIDENCE.
- Chamber (YC W26): YC validating agent-as-service for infrastructure. HIGH CONFIDENCE.
- Microsoft Copilot rollback (TechCrunch, 2026-03-20): creates space for specialized SMB offerings. MEDIUM CONFIDENCE.
**Assessment:** ClawRun and browser-use confirm tooling ecosystem growing — accelerating adoption wave. Navibase differentiation: Hungarian/CEE market focus + specific vertical (ops). Microsoft Copilot pullback maintains SMB-specific window.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=4 | IntFric=3 | **Total: 18/25**
*Score unchanged. Three new signals today (ClawRun, browser-use, RAG course) validate growing ecosystem. CEE/Hungarian focus remains genuine moat.*

---

## H8 — Cross-Agent Context Persistence (Stateless Problem)
**Thesis:** MCP sessions are stateless. Multi-agent workflows break when agents can't share context across sessions. No neutral, secure, cross-agent memory/context store exists.
**Signals (updated 2026-03-23):**
- Nyne ($5.3M seed, 2026-03-13): VC-backed company directly solving cross-agent context. HIGH CONFIDENCE (funding validates WTP).
- OpenViking (GitHub, 2026-03-16): "open-source context database designed specifically for AI Agents." HIGH CONFIDENCE.
- "Context Overflow" (Product Hunt, 2026-03-20): "Knowledge Sharing for AI Agents." MEDIUM CONFIDENCE.
- ALTK paper: multi-agent coordination failures — context loss explicitly mentioned. HIGH CONFIDENCE.
- Query Memory (Product Hunt, 2026-03-14): "One API for all documents your AI agents need." MEDIUM CONFIDENCE.
- cognee (GitHub, 2026-03-16): "Knowledge Engine for AI Agent Memory in 6 lines of code." MEDIUM CONFIDENCE.
- production-agentic-rag-course (2026-03-23): Production RAG for agentic systems — confirms context as core production concern. LOW CONFIDENCE (indirect, new today).
**Assessment:** Nyne's $5.3M seed remains key signal. Space is crowded. GDPR-compliant EU-focused angle may differentiate.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=4 | **Total: 18/25**
*Score unchanged. RAG course (Mar 23) is weak positive. Def remains low due to crowded landscape.*

---

## H9 — Agent-Dedicated Email & Communication Infrastructure
**Thesis:** Agents need dedicated, attributable communication channels. Attribution breaks, deliverability fails, compliance impossible when agents share human accounts.
**Signals (updated 2026-03-23):**
- AgentMailr (HN, 2026-03-15): "dedicated email inboxes for AI agents" — direct practitioner validation. HIGH CONFIDENCE.
- AutoSend MCP (Product Hunt, 2026-03-17): "The email platform your AI agent can operate." MEDIUM CONFIDENCE.
- discli (Product Hunt, 2026-03-16): "Discord CLI for AI agents and humans." MEDIUM CONFIDENCE.
- WordPress.com AI agents (TechCrunch, 2026-03-20): agent content at scale, attribution urgent. MEDIUM CONFIDENCE.
**Assessment:** No new signals today. Early stage hypothesis. WTP and defensibility unclear.
**Scores:** Pain=3 | Urgency=3 | WTP=2 | Def=2 | IntFric=2 | **Total: 12/25**
*Score unchanged. Monitoring for WTP signals.*

---

## Ranking Summary (2026-03-23)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 — Agent Identity & Auth | 21/25 | = |
| 4 | H3 — MCP Governance | 20/25 | = |
| 5 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 6 | H8 — Cross-Agent Context | 18/25 | = |
| 7 | H4 — Agent Payment Rails | 17/25 | = |
| 8 | H5 — Discovery & Registry | 16/25 | = |
| 9 | H9 — Agent Communication Infra | 12/25 | = |

*Low-delta day (2026-03-23): only 2-3 genuinely new signals since Mar 22 update. No score changes. All prior signals remain intact. Next significant movement expected when EU AI Act enforcement window tightens (Q2 2026) or new VC funding signal appears.*

---

## Top 5 Signals This Run (2026-03-23)

1. **browser-use GitHub trending** (2026-03-23): Browser automation for AI agents hitting GitHub trending — confirms browser tool calls becoming a standard agent primitive. Relevant to H3 (MCP/tool governance) and H7 (SMB ops agents). MEDIUM CONFIDENCE.

2. **ClawRun "Deploy and manage AI agents in seconds"** (2026-03-21, not in previous update): New agent deployment platform targeting deployment simplicity. Validates H7 SMB demand. MEDIUM CONFIDENCE.

3. **TradingAgents: Multi-Agents LLM Financial Trading Framework** (2026-03-21, not in previous update): Domain-specific financial agent — confirms financial vertical's appetite for multi-agent systems (H4 payment rails). MEDIUM CONFIDENCE.

4. **Dell brings autonomous AI agents to the desktop** (2026-03-21): Hardware expansion to desktop environment — policy enforcement (H6) and audit trail (H2) scope expands to edge. MEDIUM CONFIDENCE.

5. **production-agentic-rag-course** (2026-03-23): Education demand for production agentic RAG — growing adoption wave (H7, H8). LOW CONFIDENCE (indirect).

**Note:** Today is a low-delta day. The most impactful signals from this week remain: McKinsey hack (H3/H6), Nyne $5.3M seed (H8), NIST April deadline (H1). No score changes warranted today.

---

## Top 3 Opportunities + Suggested Experiments

### #1: H2 / H6 (tied) — Audit Trail + Policy Enforcement Runtime
**Why now:** EU AI Act Aug 2026 deadline, McKinsey hack confirms security-driven demand, 94% orgs report gaps. Dual pitch: compliance AND security.
**Experiment:** Cold outreach to 10 EU-based enterprises using Claude/GPT in production. Offer 30-day free audit report generator for EU AI Act compliance. Measure: conversion to paid, price sensitivity, compliance framework cited.
**Investment:** ~2 weeks build. Use ALTK + Tracium.ai as proof-of-concept signals in pitch.

### #2: H1 — Agent Identity & Auth Layer
**Why now:** NIST concept papers due April 2, 2026. EU AI Act Aug 2026. 77% orgs lack formal strategy. World/Worldcoin launch confirms market formation.
**Experiment:** Publish a free "Agent Identity Audit" tool — scans enterprise MCP/agent configs for identity gaps, outputs compliance checklist. Measure: downloads, enterprise inbound, conversion to paid advisory.
**Investment:** ~1 week build. Strong SEO play into April NIST deadline.

### #3: H7 — SMB Deployment Wrapper (Navibase direct relevance)
**Why now:** ClawRun and Link AI confirm market formation but no CEE/Hungarian player exists. Microsoft Copilot pullback creates SMB-specific window.
**Experiment:** Offer Leoni (current ops agent) as white-labeled pilot to 3 Hungarian SMBs. Measure: time-to-value, churn after 60 days, top 5 most frequent tasks.
**Investment:** Existing infrastructure. Main cost: Tomi's time for pilot setup. Direct revenue test.

---

## Data Sources & Confidence Notes

- **Primary:** HAIER evolution_signals export (2026-03-23, 800 total signals, 143 agent-relevant; filtered on focus_area: 'AI agents' OR 'AI decision delegation')
- **Web search:** UNAVAILABLE this run (Gemini API key error — same as 2026-03-22 run). All signals from HAIER export only. 143 signals sufficient for quality update; no critical gaps identified.
- **Delta since last update:** 3 genuinely new signals (browser-use Mar 23, jamwithai RAG course Mar 23, Sashiko Mar 22). 3 additional reviewed but previously noted (ClawRun, TradingAgents, Dell desktop).
- **Confidence notation:** HIGH = named source + verifiable claim | MEDIUM = plausible but single source or projection | LOW = speculative or executive opinion
- All scores are editorial judgments based on signal weight, not algorithmic. Treat as directional, not precise.
- No fabricated data. All claims traceable to specific sources in HAIER export.

*Last full web search: 2026-03-21. Web search unavailable 2026-03-22 and 2026-03-23 due to Gemini API key error. If API remains unavailable Mar 24, recommend Tomi checks Gemini API key status.*

---

## H10 — Agent Infrastructure as Code (GitOps for Agents)
**Thesis:** Ahogy az agent-ek száma nő, a kézi konfigurációkezelés fenntarthatatlanná válik. Nincs standard, verziókövetett módszer agent policy-k, role-ok, tool permission-ök és deployment konfigurációk deklaratív kezelésére. A Terraform mintájára szükség van egy "agent infra as code" rétegre: YAML-alapú, GitOps workflow-val, rollback képességgel.
**Signals (updated 2026-03-27):**
- Orloj (GitHub/HN, 2026-03-26): AgentPolicy, AgentRole, ToolPermission runtime gate, teljes audit trail YAML-ból — open-source pionír, közvetlenül validálja a thesis-t. HIGH CONFIDENCE.
- NVIDIA OpenShell (2026-03-23): secure runtime for autonomous agents — infra réteg standardizálódik, policy-as-code igény nő fölötte. HIGH CONFIDENCE.
- EU AI Act (arxiv, 2026-03-24): autonóm agentek szabályozatlan zónában vannak — policy deklarálhatósága compliance-kritikussá válik Aug 2026-ra. HIGH CONFIDENCE.
- Cloudflare Dynamic Workers (2026-03-24): sandbox izolálás infrastrukturális szinten megoldva — az "above infra" policy/config réteg marad nyitott. MEDIUM CONFIDENCE.
**Assessment:** Az Orloj nyílt forráskódú — a competitive moat nem a tool maga, hanem az opinionated, KKV-kra szabott konfiguráció template-ek és managed service réteg. Navibase alkalmazás: agent konfiguráció sablonok + változáskövetés + compliance export.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=4 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-03-27). Orloj megjelenése közvetlen validáció. Az open-source megközelítés miatt a managed/opinionated réteg a differenciáló tényező.*

---

## H11 — Multi-Agent Hallucination Self-Check Layer
**Thesis:** KKV agenteknél az ügyfél-kommunikáció, ajánlatok, döntések megbízhatósága üzletileg kritikus. A "hallucination" nem csak technikai zaj — egy téves email vagy hibás adat direkt üzleti kár. Jelenleg nincs beépített, cost-efficient self-check réteg multi-agent pipeline-okban. A MARCH eredmény megmutatja: 8B paraméteres modell MARL-lal eléri a closed-source szintet hallucináció-ellenőrzésben.
**Signals (updated 2026-03-27):**
- MARCH paper (arxiv, 2026-03-25): multi-agent RL-alapú hallucináció self-check, 8B modellel closed-source teljesítmény — cost-efficient megoldás production agenteknél. HIGH CONFIDENCE.
- ALTK paper (arxiv, 2026-03-16): tool argument corruption, policy violation, silent reasoning error — multi-agent pipeline failures dokumentálva. HIGH CONFIDENCE.
- Meta rogue agent (2026-03-24): az "ellenőrzés illúziója" narratíva KKV pitchben visszaütő — a megbízhatóság lesz az értékesítési battleground. HIGH CONFIDENCE.
- EU AI Act autonóm agent kompatibilitás paper (arxiv, 2026-03-24): "misuse risk, unequal access" — téves agent output felelősség kérdése nyílik. HIGH CONFIDENCE.
**Assessment:** A MARCH technikát a Navibase SMB ops agent reliability rétegébe lehet integrálni: kimenő kommunikáció (email, ajánlat, riport) előtt self-check pass. Kis modell, alacsony latency, magas üzleti érték. Versenyképes differenciátor a "megbízható agent" pitchben.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=3 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-03-27). MARCH paper közvetlen technikai validáció. KKV relevanciája magas — az "agent hibázott és az ügyfélnek ment" forgatókönyv a legnagyobb adopciós barrier.*


---

## Ranking Summary (2026-03-27)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 — Agent Identity & Auth | 21/25 | = |
| 4 | H3 — MCP Governance | 20/25 | = |
| 5 | **H10 — Agent Infra as Code** | **19/25** | **ÚJ** |
| 6 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 7 | H8 — Cross-Agent Context | 18/25 | = |
| 8 | H4 — Agent Payment Rails | 17/25 | = |
| 9 | **H11 — Hallucination Self-Check** | **17/25** | **ÚJ** |
| 10 | H5 — Discovery & Registry | 16/25 | = |
| 11 | H9 — Agent Communication Infra | 12/25 | = |

*2026-03-27 delta: 2 új hypothesis (H10, H11). Meglévő scorok változatlanok. Governance/Compliance nyomás (H1/H2/H6) és infrastrukturális standardizáció (H10) dominál. EU AI Act Aug 2026 deadline közeledtével urgency emelkedés várható Q2-ben.*

---

## Top 3 Opportunities + Suggested Experiments (2026-03-27)

### #1: H2 / H6 (tied) — Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** EU AI Act Aug 2026 deadline közeledik. McKinsey hack + Meta rogue agent megerősítik a biztonsági igényt. 94% szervezetnél kritikus hiány az AI aktivitás láthatóságában. A compliance + security kettős pitch most nyitott ablak.
**Javasolt kísérlet:** 10 EU-ban működő, Claude/GPT-t production-ben használó enterprise-nak hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit report generátor. Mérők: konverzió fizetős felé, árszenzitvitás, hivatkozott compliance framework.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai mint proof-of-concept.

### #2: H10 — Agent Infrastructure as Code [Score: 19/25 — ÚJ]
**Miért most:** Az Orloj open-source megjelenése (2026-03-26) jelzi, hogy a piac elkezdi standardizálni a GitOps for Agents mintát. Az EU AI Act compliance-hoz szükséges auditálható policy deklarálhatóság megnöveli a WTP-t vállalati szinten. Moat lehetőség: managed service + opinionated KKV template-ek az open-source tool fölé.
**Javasolt kísérlet:** Navibase "Agent Config Template Library" — 5 iparági sablon (ügyfélszolgálat, könyvelés, HR, értékesítés, logisztika) YAML-ban, Orloj/policy-as-code mintára. Mérő: GitHub star szerzés 30 nap alatt, inbound enterprise kontakt, template letöltések.
**Befektetés:** ~1 hét. Erős SEO- és thought leadership-hatás a Navibase brand számára.

### #3: H11 — Hallucination Self-Check réteg (Navibase közvetlen alkalmazás) [Score: 17/25 — ÚJ]
**Miért most:** A MARCH paper (8B MARL modell, closed-source szintű teljesítmény) megnyitja a cost-efficient in-pipeline self-check lehetőséget. KKV-knál a "agent hibás emailt küldött az ügyfélnek" forgatókönyv a legfőbb adopciós barrier — ezt megszünteti. Belső implementáció gyors ROI-t hozhat a Leoni ops agent megbízhatóságán.
**Javasolt kísérlet:** Leoni kimenő kommunikáció pipeline-jában (email, ajánlat, riport) MARCH-alapú self-check réteg prototípus. Mérő: false positive arány (nem blokkol helyes outputot), false negative arány (nem enged át hibásat), latency overhead. 2 hetes A/B: önellenőrzéssel vs. anélkül.
**Befektetés:** ~1 hét. Azonnal tesztelhető a meglévő Leoni infrastruktúrán. Ha működik: KKV pitch centerdarabja.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-03-27.md (189 signal, HAIER export) | 2026-03-27 09:30 CET*


---

## H12 — Agent Accountability & Legal Responsibility Framework
**Thesis:** Autonóm AI agentek elterjedésével "felelősségi vákuum" keletkezik: sem a fejlesztő, sem a deployer, sem a felhasználó nem vonható felelősségre az agent döntéséért. 2026-ra ez a kérdés jogi, szervezeti és üzleti szinten megoldatlan. Az AI governance narratíva átfogalmazódik: nem az automatizáció megállítása, hanem a döntési felelősség újratervezése a cél. Erre nincs sem standard keretrendszer, sem termék.
**Signals (updated 2026-03-28):**
- iProov: "Accountability Vacuum" figyelmeztetés (2026-03-26): biometria-biztonsági cég nyilvánosan nevesíti a problémát — a felelősségi vákuum közvetlen kockázat minden operatív agent deploymentnél. HIGH CONFIDENCE.
- arxiv: "Regulating AI Agents" (2026-03-24): korlátozott emberi felügyelet melletti önálló döntéshozatal elemzése — tudományos szinten is megjelent, szabályozói tér nyitva van. HIGH CONFIDENCE.
- Leaders League: "The Illusion of Automation" — Decision Architecture (2026-03-25): "az AI governance nem az automatizáció megállítása, hanem a döntési felelősség újratervezése." HIGH CONFIDENCE.
- EurekAlert!: "Embedding Social Values into AI Decisions" (2026-03-27): kutatási irány a konfigurálható értékalapú korlátok felé — jogi felelősség és szervezeti értékek metszéspontja. MEDIUM CONFIDENCE.
- Sanders/AOC moratorium javaslat (TechCrunch, 2026-03-25): politikai szinten is megjelent — szabályozói nyomás emelkedik, compliance-driven kereslet várható. MEDIUM CONFIDENCE.
**Assessment:** Ez a hypothesis az eddigi listán hiányzó *jogi és szervezeti réteg* — a H2 (audit log) és H6 (policy enforcement) technikai rétegei fölött. A KKV pitch szempontjából erős differenciátor: nem azt mondjuk, hogy "az agent elvégzi a munkát", hanem azt, hogy "tudod, ki felel az agent döntéséért". Versengő termék jelenleg nincs — a tér nyitott. Navibase alkalmazás: "Accountability Map" — szervezeti felelősségrendelési sablonok + agent-döntés owner mátrix + audit-ready dokumentáció.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=4 | IntFric=3 | **Total: 20/25**
*Új hypothesis (2026-03-28). iProov + arxiv + Leaders League egymást erősítő, különböző szektorbeli signalok. A jogi felelősség kérdése az EU AI Act Aug 2026 deadlinjével tovább élesedik.*

---

## Ranking Summary (2026-03-28)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 — Agent Identity & Auth | 21/25 | = |
| 4 | H3 — MCP Governance | 20/25 | = |
| 5 | **H12 — Agent Accountability Framework** | **20/25** | **ÚJ** |
| 6 | H10 — Agent Infra as Code | 19/25 | = |
| 7 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 8 | H8 — Cross-Agent Context | 18/25 | = |
| 9 | H4 — Agent Payment Rails | 17/25 | = |
| 10 | H11 — Hallucination Self-Check | 17/25 | = |
| 11 | H5 — Discovery & Registry | 16/25 | = |
| 12 | H9 — Agent Communication Infra | 12/25 | = |

*2026-03-28 delta: 1 új hypothesis (H12 — Accountability Framework, 20/25). Meglévő scorok változatlanok. H12 azonnal a top 5-be kerül — az accountability vákuum téma 3 független, magas bizalmú signallal nyílt meg. EU AI Act Aug 2026 közeledtével Q2-ben urgency emelkedés várható H1/H2/H6/H12 blokkon.*

---

## Top 3 Opportunities + Suggested Experiments (2026-03-28)

### #1: H2 / H6 (tied) — Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** EU AI Act Aug 2026 deadline 5 hónap. McKinsey hack + Meta rogue agent esetei megerősítik biztonsági igényt. 94% szervezetnél kritikus hiány az AI aktivitás láthatóságában. Compliance + security kettős pitch, most nyitott ablak.
**Javasolt kísérlet:** 10 EU-ban működő, Claude/GPT-t production-ben használó enterprise hideg megkeresése. Ajánlat: 30 napos ingyenes EU AI Act compliance audit report generátor. Mérők: konverzió fizetős felé, árszenzitvitás, hivatkozott compliance framework.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai proof-of-concept signalként a pitchben.

### #2: H12 — Agent Accountability Framework [Score: 20/25 — ÚJ]
**Miért most:** Az "accountability vacuum" ma 3 független szektorbeli sourcetól jelent meg (biztonsági ipar, tudományos szféra, üzleti média) — ez nem trend, ez jel. A tér üres: nincs termék, nincs standard, nincs referencia. Az EU AI Act Aug 2026 a jogi felelősség kérdését kötelező compliance szintjére emeli. Navibase differenciátor: nem csak az agent csinál valamit, hanem pontosan tudod, ki felel az eredményért.
**Javasolt kísérlet:** "Agent Accountability Map" sablon — szabad letöltés, 3 szekció: (1) döntési owner mátrix agent típusonként, (2) eskalációs protokoll, (3) EU AI Act megfelelési checklist. Mérők: letöltések, inbound megkeresések, LinkedIn engagement 2 héten belül. Ha 200+ letöltés: fizetős workshop pilot.
**Befektetés:** ~3 nap. Thought leadership befektetés, közvetlen lead generáló hatással.

### #3: H7 — SMB Deployment Wrapper (Navibase közvetlen relevancia) [Score: 18/25]
**Miért most:** A mainstream sajtóban (Jerusalem Post, 2026-03-27) megjelent az autonóm agent téma — a KKV-k hallanak róla, a pitch window nyitva van, de a konkurencia is ébredezik. CEE/magyar piacon még nincs versenyző. Microsoft Copilot pullback SMB-specifikus ablakot tart nyitva.
**Javasolt kísérlet:** Leoni ops agent white-label pilot 3 magyar KKV-nak. Mérők: time-to-value (mennyi nap alatt látnak eredményt), top 5 legtöbbet használt feladat, 60 napos churn. Ha a 3 pilot közül 2 marad: méretezési döntés.
**Befektetés:** Meglévő infrastruktúra. Fő cost: Tomi ideje a pilot setuphoz. Közvetlen bevétel-teszt.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-03-28.md (197 signal, HAIER export) | 2026-03-28 09:30 CET*
