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


---

## H13 - Agent Sandboxing & Isolation Layer for SMB/Enterprise
**Thesis:** Az autonomous agent adoption gyorsul, de a legtöbb szervezet shared runtime-ban futtatja az agenteket erős izoláció nélkül. Ez növeli a cross-tenant és tool-abuse kockázatot. A piacnak szüksége van egy könnyen bevezethető, auditálható sandboxing rétegre, amely minden agent run-t izolált execution környezetben kezel.
**Signals (updated 2026-03-29):**
- Cloudflare Dynamic Workers (2026-03-24): agent sandboxing 100x faster, izolált futtatás milliszekundumos indulással. HIGH CONFIDENCE.
- Meta rogue agent trust crisis (2026-03-24): enterprise bizalom sérül, ha agent viselkedés nem kontrollált izolációban fut. HIGH CONFIDENCE.
- Orloj policy-first megközelítés (2026-03-26): runtime gate + audit trail terjed, technikai irány megerősítve. HIGH CONFIDENCE.
- EU AI Act kritikák (arxiv, 2026-03-24): autonomous task execution governance hiányok, kontrollált runtime szükségessége emelkedik. MEDIUM CONFIDENCE.
- Jentic Mini managed API layer (2026-03-25): agent execution köré biztonsági middleware-ek formálódnak, platformizáció jele. MEDIUM CONFIDENCE.
**Assessment:** Ez a hypothesis a H6 (policy enforcement) technikai testvér-tere, de külön fókusz: izolációs runtime mint termék. KKV-nál a "biztonságos default" értékesítési előny, enterprise-nál compliance + incident containment.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-03-29). A Cloudflare signal közvetlen technológiai validációt ad, a Meta jellegű trust események pedig üzleti oldalról erősítenek.*

---

## Ranking Summary (2026-03-29)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 - Agent Identity & Auth | 21/25 | = |
| 4 | H3 - MCP Governance | 20/25 | = |
| 5 | H12 - Agent Accountability Framework | 20/25 | = |
| 6 | H10 - Agent Infra as Code | 19/25 | = |
| 7 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 8 | H8 - Cross-Agent Context | 18/25 | = |
| 9 | **H13 - Agent Sandboxing & Isolation** | **18/25** | **ÚJ** |
| 10 | H4 - Agent Payment Rails | 17/25 | = |
| 11 | H11 - Hallucination Self-Check | 17/25 | = |
| 12 | H5 - Discovery & Registry | 16/25 | = |
| 13 | H9 - Agent Communication Infra | 12/25 | = |

*2026-03-29 delta: 1 új hypothesis (H13). Governance és biztonsági blokkok (H2/H6/H12/H13) együtt tovább erősödnek.*

---

## Top 3 Opportunities + Suggested Experiments (2026-03-29)

### #1: H2 / H6 - Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** Compliance határidők közelítenek, a security incidensek már valós üzleti kárt mutatnak. A láthatóság + inline kontroll együtt ad vásárolható értéket.
**Javasolt kísérlet:** 10 EU cégnek 30 napos "Agent Governance Baseline" pilot (audit log + policy violations report). Mérők: pilot->paid konverzió, átlagos incidens-szám csökkenés, compliance readiness score.

### #2: H12 - Agent Accountability Framework [Score: 20/25]
**Miért most:** A felelősségi vákuum téma egyszerre jelent meg security, jogi és üzleti forrásokban. Üres kategória, gyors thought-leadership előny építhető.
**Javasolt kísérlet:** "Accountability Map" workshop 5 design partnerrel (2 hét). Deliverable: döntési owner mátrix + eszkalációs runbook + felelősségi audit sablon. Mérők: workshop utáni fizetős implementációs igény.

### #3: H13 - Agent Sandboxing & Isolation Layer [Score: 18/25 - ÚJ]
**Miért most:** A technológia elérhető, de SMB/enterprise implementáció fragmentált. A "safe-by-default" izoláció erős differenciátor lehet a Navibase ajánlatban.
**Javasolt kísérlet:** "Isolated Agent Run" MVP 1 pilot ügyfélnél: minden magas kockázatú task külön runtime-ban fut, kötelező audit exporttal. Mérők: incident rate, overhead latency, ügyfél-bizalmi visszajelzés (NPS security kérdéssel).

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-03-28.md + delta synthesis | 2026-03-29 09:32 CET*


---

## H14 — Agent-to-Agent Trust & M2M Communication Protocol
**Thesis:** Az agent ökoszisztéma következő nagy megoldatlan kérdése: hogyan kommunikálnak, hitelesítik egymást és osztanak meg kontextust az autonóm agentek egymás között? A mai rendszerekben az agent-to-agent kapcsolat nincs definiálva — sem trust, sem protokoll, sem felelősségi határ. Ez a "machine-to-machine trust" probléma a multi-agent pipeline-ok skálázásának legfőbb akadálya.
**Signals (updated 2026-03-30):**
- Enlidea (HN, 2026-03-28): autonóm agentek, amik hipotéziseket javasolnak, bounty-kat tesznek, kódot futtatnak és peer review-t végeznek egymás munkáján. Reverse-CAPTCHA: csak agent lép be, ember nem. Direkten validálja az agent-first M2M ecosystem igényt. HIGH CONFIDENCE.
- CRAFT paper (arxiv, 2026-03-26): 8 open-weight + 7 frontier modell tesztelve — erősebb reasoning nem jelent jobb multi-agent koordinációt. "Fundamentally unsolved challenge." HIGH CONFIDENCE.
- iProov "accountability vacuum" (2026-03-26): felelőssége nincs senkinek, ha agent dönt — ez M2M kontextusban kettőzve igaz. HIGH CONFIDENCE.
- H8 (Cross-Agent Context, Nyne $5.3M) és H1 (Agent Identity) már lefedi a részterületeket — H14 ezekre épít, de az "agent trust negotiation" réteget teszi hozzá.
**Assessment:** A CRAFT eredmény megmutatja: a probléma nem modellerő, hanem protokoll és koordináció. Aki ma épít agent-to-agent trust réteg szabványt (akár lightweight, akár YAML-alapú), az megteremtheti a következő MCP-szintű szabvány alapjait. A Navibase alkalmazás: multi-agent orchestrátor template-ek, ahol a trust handshake és az eskalációs protokoll definiált.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=4 | IntFric=4 | **Total: 18/25**
*Új hypothesis (2026-03-30). CRAFT + Enlidea egymást erősítő signalok. 2026 végétől urgency emelkedés várható, ahogy multi-agent pipeline-ok production-ba kerülnek.*

---

## H15 — B2B SaaS Agent Feature Injection (Meglévő termékek + agent réteg)
**Thesis:** A Granola eset ($125M, $1.5B valuáció) megmutatta: egy meglévő B2B SaaS termék agent-funkciók hozzáadásával azonnal 10x értékugrást képes elérni. A piac ma azt jutalmazza, aki a meglévő user base-jének agent képességeket ad — nem azt, aki nulláról épít agent platformot. Ez a KKV szegmensben eddig érintetlen lehetőség: meglévő magyar/CEE B2B SaaS termékek agent integrációra várnak.
**Signals (updated 2026-03-30):**
- Granola $125M / $1.5B valuáció (TechCrunch, 2026-03-25): meeting notetaker → enterprise agent platform. Felhasználók panaszolták a hiányát → azonnal beépítették → valuáció megtízszereződött. HIGH CONFIDENCE.
- AI Agents → Governance Infrastructure mainstream (National Today, 2026-03-29): az agent funkció nem differenciátor, hanem elvárás lesz — aki késik, lemarad. HIGH CONFIDENCE.
- Microsoft Copilot pullback (TechCrunch, 2026-03-20): big tech kivonul egyes SMB szegmensekből, nyitva hagyja a lokális/specializált agent integration piact. MEDIUM CONFIDENCE.
- Link AI "replace your entire stack" (2026-03-19): versenytárs próbál teljes stack-et kiváltani — de a meglévő SaaS-ba épülő agent réteg kisebb súrlódással jár. MEDIUM CONFIDENCE.
**Assessment:** Ez nem platform-build, hanem integration play. A Navibase pozicionálása: "agent layer a te meglévő rendszeredre" — CRM-be, számlázóba, projektmenedzsmentbe, ERP-be. A proof of concept a Leoni ops agent: nem új platform, hanem a meglévő Gmail/GitHub/Telegram infrastruktúrára rakott végrehajtó intelligencia. Alacsony IntFric, magas WTP a SaaS oldalán.
**Scores:** Pain=4 | Urgency=5 | WTP=5 | Def=3 | IntFric=2 | **Total: 19/25**
*Új hypothesis (2026-03-30). A Granola signal az egyik legerősebb üzleti bizonyíték az eddigi listán — valuáció szintű piacvalidáció. Az urgency magas: az ablak nyitva van, de a nagy szereplők is ébredeznek.*

---

## Ranking Summary (2026-03-30)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 — Agent Identity & Auth | 21/25 | = |
| 4 | H3 — MCP Governance | 20/25 | = |
| 5 | H12 — Agent Accountability Framework | 20/25 | = |
| 6 | H10 — Agent Infra as Code | 19/25 | = |
| 7 | **H15 — B2B SaaS Agent Feature Injection** | **19/25** | **ÚJ** |
| 8 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 9 | H8 — Cross-Agent Context | 18/25 | = |
| 10 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 11 | **H14 — Agent-to-Agent Trust & M2M** | **18/25** | **ÚJ** |
| 12 | H4 — Agent Payment Rails | 17/25 | = |
| 13 | H11 — Hallucination Self-Check | 17/25 | = |
| 14 | H5 — Discovery & Registry | 16/25 | = |
| 15 | H9 — Agent Communication Infra | 12/25 | = |

*2026-03-30 delta: 2 új hypothesis (H14, H15). H15 azonnal a top 7-be kerül a Granola valuációs bizonyíték ereje miatt. Governance és compliance blokk (H2/H6/H12) dominálja a listát — EU AI Act Aug 2026 deadline közeledtével ez várható.*

---

## Top 3 Opportunities + Suggested Experiments (2026-03-30)

### #1: H15 — B2B SaaS Agent Feature Injection [Score: 19/25 — ÚJ]
**Miért most:** A Granola eset valódi, számokkal alátámasztott piacvalidáció: agent layer hozzáadása meglévő B2B termékhez = 10x valuáció. Az ablak nyitva van, de a nagy szereplők (Salesforce, HubSpot, Monday.com) is mozognak. Magyar/CEE piacon nincs versenyző, aki ezt lokálisan hirdeti. Alacsony build-fric: a meglévő Navibase/Leoni infra minta.
**Javasolt kísérlet:** Azonosítani 3 magyar B2B SaaS céget (CRM, projekt, számlázó szegmensben), akiknek van aktív user base-jük de nincs agent feature-jük. Megközelítés: "agent integration partnership" — Navibase beépít egy Leoni-típusú ops agent réteget az ő termékükbe. Mérők: partnership érdeklődés 4 héten belül, pilot ajánlat elfogadási arány, user engagement növekedés a pilotnál.
**Befektetés:** ~1 hét outreach. Ha 1/3 partner igent mond: 8-12 hetes MVP sprint.

### #2: H2 / H6 (tied) — Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** EU AI Act Aug 2026 deadline 4 hónap. Az AI agents → governance infrastructure mainstream narratíva (National Today, 2026-03-29) azt jelzi, hogy a compliance igény most terjed át a nem-tech CEO-khoz is. Ez a legmagasabb score-ú, legérettebb lehetőség a listán.
**Javasolt kísérlet:** 10 EU-based Claude/GPT production-user enterprise hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit. Mérők: pilot→paid konverzió, árszenzitvitás, compliance framework hivatkozás.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai proof-of-concept a pitchben.

### #3: H12 — Agent Accountability Framework [Score: 20/25]
**Miért most:** Az iProov "accountability vacuum" + Leaders League "Decision Architecture" + EurekAlert "Social Values" egymást erősítő, különböző szektorbeli signalok. A kategória üres. A governance infrastruktúra mainstream narratíva (2026-03-29) azt jelzi, hogy ez már nem "tech bubble téma" — CEO szinten is megjelent.
**Javasolt kísérlet:** "Agent Accountability Map" sablon — 3 nap build, szabad letöltés. Tartalom: döntési owner mátrix, eskalációs runbook, EU AI Act megfelelési checklist. Mérők: 200+ letöltés 2 héten belül → fizetős workshop pilot indítás.
**Befektetés:** ~3 nap. Thought leadership + lead gen, közvetlen bevételi utat nyit.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-03-30.md (208 signal, HAIER export) | 2026-03-30 11:36 CET*


---

## H16 — AI Alignment Measurement as a Service (Delegáció-ellenőrzés)
**Thesis:** Az AI agentek döntései egyre kevésbé átláthatóak a megbízónak. A "Revealed Preference" kutatási irány (Luce Alignment Model) megmutatja: az agent döntései mérhetően eltérhetnek a gazda szándékától. Nincs olyan termék, amely a KKV-k számára mérhetővé teszi, hogy az agent "mennyire az ővé" — vagyis a delegáció foka és minősége kontrolálható legyen. Ez nem technikai monitoring, hanem üzleti kontroll eszköz: "milyen arányban tartja be az agent a céged értékeit és döntési elveit?"
**Signals (updated 2026-03-31):**
- arxiv "Revealed Preference Framework for AI Alignment" (2026-03-29): Luce Alignment Model bevezetése — agent döntései az emberi és saját preferenciák keveréke, eltérés mérhető. HIGH CONFIDENCE.
- iProov "accountability vacuum" (2026-03-26): ki felel az agent döntéséért? — a mérhetőség hiánya jogi és szervezeti kockázat. HIGH CONFIDENCE.
- CRAFT paper: "Fundamentally unsolved challenge" a multi-agent koordináció — az alignment mérése a megbízhatóság alapfeltétele. HIGH CONFIDENCE.
- EU AI Act Aug 2026: "high-risk AI decisions" naplózása kötelező — az alignment mérhetőség természetes compliance komponens. MEDIUM CONFIDENCE.
**Assessment:** A "mennyire bízhat meg az agent döntésében a CEO" kérdés ma megválaszolatlan. Az alignment measurement egy új kategória: nem naplózás (H2), nem policy enforcement (H6), hanem a megbízhatóság kvantitatív jelzése üzleti döntéshozóknak. Navibase alkalmazás: "Leoni Alignment Score" dashboard — hetente megmutatja, hány döntés volt emberi elvárással konzisztens, hány nem, és miért.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=4 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-03-31). A Revealed Preference Framework paper közvetlen tudományos alapot ad. A KKV piac számára az "agent megbízhatóság mérőszáma" az adopciós barrier elhárításának kulcsa.*

---

## H17 — Controlled Self-Configuration Boundary (Agent Scope Hardening)
**Thesis:** Az autonóm agentek egyre több rendszerben kapnak jogot a saját konfigurációjuk módosítására (lásd: Phantom open-source agent, saját VM-en config rewrite). Ez az önmódosítás képesség kontinuumot alkot az "adaptív viselkedés" és a "kontroll elvesztése" között. Nincs standard, amely definiálná, hol a határvonal — sem termék, sem auditálható scope-definition framework. A Navibase/Leoni architektúrában ez már megoldott (explicit scope-olás), de a piac nem tud róla, és ez differenciáló kommunikációs lehetőség.
**Signals (updated 2026-03-31):**
- Phantom (GitHub ghostwright/phantom, 2026-03-30): nyílt forráskódú agent saját VM-en, config rewrite képességgel — az önmódosítás határvonal kérdése production-szintű valóság lett. HIGH CONFIDENCE.
- Orloj (2026-03-26): runtime policy-first megközelítés, tool call gate — az önmódosítás kontrolálhatósága technikai szinten megoldható. HIGH CONFIDENCE.
- Cloudflare Dynamic Workers (2026-03-24): sandbox izoláció 100x gyorsabb — az önmódosítás kontrollált keretek közt tartható. HIGH CONFIDENCE.
- ALTK paper (2026-03-16): "silent reasoning errors go undetected" — önmódosítás nélküli agentben is van drift, önmódosítással hatványozódik. HIGH CONFIDENCE.
**Assessment:** Ez nem technikai újítás — ez kommunikációs és pozicionálási lehetőség. A Navibase/Leoni már megoldotta: az önkonfiguráció explicit scope-olva van, SOUL.md + AGENTS.md definiálja a határt, policy engine enforce-olja. A "Controlled Self-Configuration" mint termék feature és pitch elem: "tudod, mit módosíthat az agent magán és mit nem." Enterprise és KKV szinten egyformán értékes.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=4 | IntFric=2 | **Total: 18/25**
*Új hypothesis (2026-03-31). A Phantom megjelenése kinyitja a "ki szabályozza az agent önmódosítását" kérdést. A Navibase architectúra erre kész választ ad — a differenciáló kommunikáció még nincs megírva.*

---

## H18 — Organizationally-Aligned AI (Social Values Embedding for SMBs)
**Thesis:** Az AI agentek ma "értéksemlegesek" — a szervezet értékrendjét, kommunikációs stílusát, döntési elveit csak prompton keresztül lehet megadni, ami törékeny és nem auditálható. A kutatási irány (EurekAlert, 2026-03-27) mutatja: az emberi értékek beágyazhatók az AI döntési folyamatokba. A KKV piacnak szüksége van egy eszközre, amellyel a saját szervezeti értékeiket (pl. "nem ajánlunk semmit ha bizonytalan a szükséglet", "mindig az ügyfél érdekét prioritizáljuk") verziókövetve, auditálhatóan adják meg az agentnek — nem prompton, hanem konfigurált policy-ként.
**Signals (updated 2026-03-31):**
- EurekAlert: "Embedding Social Values into AI Decisions" (2026-03-27): tudományos validáció — az értékbeágyazás lehetséges és szükséges. HIGH CONFIDENCE.
- iProov "accountability vacuum": az agent döntése mögött ott kell lennie a szervezeti értékrendnek, hogy a felelősség visszakövethető legyen. HIGH CONFIDENCE.
- Leaders League "Decision Architecture" (2026-03-25): "az AI governance a döntési felelősség újratervezése" — az értékek explicit kódolása ennek alapja. HIGH CONFIDENCE.
- Leoni SOUL.md + USER.md struktúra: ez maga is egy "values embedding" implementáció — de nincs KKV-szintű termékké téve. MEDIUM CONFIDENCE (internal signal).
**Assessment:** Ez a H12 (accountability) és H16 (alignment measurement) természetes kiegészítője: nem csak mérjük az eltérést, hanem megadjuk, mitől kellene eltérnie. A Navibase alkalmazás: "Organization Values Kit" — strukturált, verziókövetett, auditálható értékkonfiguráció KKV-knak, amely az ops agent "lelkévé" válik. Differenciátor: a Leoni SOUL.md maga is ennek prototípusa.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=4 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-03-31). A tudományos irány és a Leoni belső implementáció egyszerre validálja a thesis-t. Navibase számára ez termék és differenciáló narratíva egyszerre.*

---

## H19 — Operational Reliability Layer (Tooling Commoditization Response)
**Thesis:** Az agent tooling ökoszisztéma gyorsan commoditizálódik: Composio (1000+ app integráció), MCP szabvány terjedése, ClawRun, browser-use — az integráció ma már nem versenyelőny. Aki az integráció rétegen versenyez, elveszíti a differenciálót. Az igazi versenyelőny az operatív megbízhatóság: mennyi agent run végez sikeresen vs. hibával, mennyi emberi beavatkozás kell, mennyi a "silent failure" (agent nem jelez de rosszat csinál). Ez mérhető, kommunikálható, és ma senki nem pozicionálja termékként.
**Signals (updated 2026-03-31):**
- Composio "Universal CLI — Connect AI agents to 1000+ apps" (ProductHunt, 2026-03-27): az integráció réteg commoditizálódik, ez már nem differenciáló. HIGH CONFIDENCE.
- ALTK paper (2026-03-16): "silent reasoning errors, tool argument corruption, policy violations" — a megbízhatóság mérhetővé tétele sürgős. HIGH CONFIDENCE.
- $65M seed enterprise agent startup (TechCrunch, 2026-03-30): az enterprise szegmensbe nagy tőke áramlik — a KKV szegmens az operatív megbízhatóságra fog versenyezni, nem az integrációra. MEDIUM CONFIDENCE.
- CRAFT paper: erősebb modell nem jelent jobb multi-agent koordinációt — a megbízhatóság protokoll és monitoring kérdése, nem modell kérdés. HIGH CONFIDENCE.
**Assessment:** A "reliability SLA" mint termék: az ops agent minden run-nak van státusza, minden hibának van eskalációs protokollja, minden sikernek van auditnyoma. Navibase alkalmazás: "Leoni Ops Reliability Score" — heti KPI dashboard KKV CEO-knak: hány feladat futott le teljesen, hány igényelt emberi beavatkozást, mennyi volt a latency. Ez nem monitoring, hanem üzleti értékjelzés.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-03-31). A tooling commoditizáció signal (Composio) kinyitja azt a kérdést: ha mindenki integrál mindenhová, mi marad a differenciáló? Válasz: az operatív megbízhatóság mérhetősége és kommunikálása.*

---

## Ranking Summary (2026-03-31)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 — Agent Identity & Auth | 21/25 | = |
| 4 | H3 — MCP Governance | 20/25 | = |
| 5 | H12 — Agent Accountability Framework | 20/25 | = |
| 6 | H10 — Agent Infra as Code | 19/25 | = |
| 7 | H15 — B2B SaaS Agent Feature Injection | 19/25 | = |
| 8 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 9 | H8 — Cross-Agent Context | 18/25 | = |
| 10 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 11 | H14 — Agent-to-Agent Trust & M2M | 18/25 | = |
| 12 | **H16 — AI Alignment Measurement as a Service** | **18/25** | **ÚJ** |
| 13 | **H17 — Controlled Self-Configuration Boundary** | **18/25** | **ÚJ** |
| 14 | **H18 — Organizationally-Aligned AI** | **18/25** | **ÚJ** |
| 15 | **H19 — Operational Reliability Layer** | **18/25** | **ÚJ** |
| 16 | H4 — Agent Payment Rails | 17/25 | = |
| 17 | H11 — Hallucination Self-Check | 17/25 | = |
| 18 | H5 — Discovery & Registry | 16/25 | = |
| 19 | H9 — Agent Communication Infra | 12/25 | = |

*2026-03-31 delta: 4 új hypothesis (H16–H19). Mindegyik 18/25 — erős, de nem dönti el a rangsort a meglévő top 5 ellen. A tooling commoditizáció (H19) és az alignment mérhetőség (H16) a leginkább Navibase-releváns új belépők. Governance és compliance blokk (H1/H2/H6/H12) dominál.*

---

## Top 3 Opportunities + Suggested Experiments (2026-03-31)

### #1: H2 / H6 (tied) — Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** EU AI Act Aug 2026 deadline 4 hónap. Az "agent governance infrastruktura" narratíva mainstream médiában jelent meg (National Today, 2026-03-29) — a CEO-szintű figyelem most nyílt meg. 94% szervezetnél kritikus AI láthatósági hiány. A compliance + security kettős pitch ma a legerősebb nyitó.
**Javasolt kísérlet:** 10 EU-based Claude/GPT production-user enterprise hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit. Mérők: pilot→paid konverzió, árszenzitvitás, compliance framework hivatkozás.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai proof-of-concept a pitchben.

### #2: H19 — Operational Reliability Layer [Score: 18/25 — ÚJ]
**Miért most:** A Composio-féle tooling commoditizáció (2026-03-27) jelzi: aki az integráció rétegen versenyez, elveszít. A differenciáló versenyelőny az operatív megbízhatóság — és ezt ma senki nem kommunikálja termékként. A $65M enterprise seed azt mutatja, hogy az enterprise piac felfelé megy, a KKV szegmensben az "operatív SLA" lesz az értékesítési battleground.
**Javasolt kísérlet:** Leoni ops agent-nél 30 napos reliability tracking: minden run státusz, hiba, eszkaláció, latency. Összefoglalás heti KPI dashboardban Tominak. Ha az adatok jók: ez a KKV pitch centerdarabja. Mérők: run success rate, human-in-the-loop rate, average task completion time.
**Befektetés:** ~3 nap build (Leoni belső monitoring). Azonnali belső adat + KKV pitch anyag.

### #3: H16 — AI Alignment Measurement as a Service [Score: 18/25 — ÚJ]
**Miért most:** A Revealed Preference Framework paper (arxiv, 2026-03-29) tudományos alapot ad a KKV pitchhez: "mérd le, hogy az agented valóban a te értékeidet képviseli-e." Az iProov accountability vacuum narratívával kombinálva ez az adopciós barrier legfőbb elhárítója. Navibase differenciáló: "Leoni Alignment Score" — heti dashboard, hány döntés volt emberi elvárással konzisztens.
**Javasolt kísérlet:** Leoni 30 napos alignment logging pilot: minden döntésnél (email, kanban, cron, git push) rögzítés, hogy emberi utasítással konzisztens volt-e, vagy autonóm eltérés. Heti összesítő Tominak. Mérők: eltérési arány, false autonomy rate, CEO bizalmi szint változása (szubjektív visszajelzés).
**Befektetés:** ~2 nap logging. Azonnali belső érték + pitch anyag a KKV pilotra.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-03-31.md (217 signal, HAIER export) | 2026-03-31 21:50 CET*
