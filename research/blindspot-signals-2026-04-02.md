# Agent Platform Blindspot Radar — 2026-04-02

> Forrás: HAIER export (evolution_signals_20260402_020659.json)
> Szurt: focus_area = 'AI agents' | 'AI decision delegation'
> Relevans signalok: 232 (ebből első 30 feldolgozva)

---

## TOP 5-10 — Legerosebb signalok

### 1. Google DeepMind: 6 "csapda" autonóm agenteknek
**Bizonyíték:** DeepMind tanulmány dokumentálja, hogy az élő (wild) körülmények között futó autonóm AI agenteket 6 jól ismerheto mechanizmus segítségével lehet eltéríteni / manipulálni (prompt injection, kontextus manipuláció stb.).
**Relevancia:** KRITIKUS — Leoni és hasonló produkciós agentek közvetlen biztonsági kockázata.
- Dátum: 2026-04-01
- Forrás: google_news (the-decoder.com)
- URL: https://news.google.com/rss/articles/CBMivAFBVV95cUxPNVk0SThWaUI5d3M5N3RZX0lnRFhsZlUwZmo1RjBPc19uM0hiZ3dmZGREcEVzZHZ6VXJHYkt6X2EyaXV0Y2EyTWg2c1FVOGwyOFUxRm8xdUJOdHJzcHJZakM5bktRNXAxdUdoZFB4b0hlQnQ1UFhhZVZRTWJKNTEyUVNHbTl1SGU2TUlRVlJSTjhjV1dnQVFSSzE1UVZCLVpGaTdmMmZmQkp4aVFSZWpPMXRiMFFBMF9Ccl93Vg?oc=5

---

### 2. AI Agents Become Governance Infrastructure
**Bizonyíték:** Cikk elemzi, hogy AI agentek infrastrukturális szerepbe kerülnek szervezetekben, és ez súlyos kontroll-kérdéseket vet fel — ki felügyeli az agentet, ha az agent maga az infrastruktúra?
**Relevancia:** MAGAS — Agent identity, audit trail, oversight gap. Navibase-modellben ez most hiányzik.
- Dátum: 2026-03-29
- Forrás: google_news (National Today)
- URL: https://news.google.com/rss/articles/CBMiywFBVV95cUxQWXgwUVBGMXVMV2JoeDZ2c19BV0JUSXJwbjNKdnZTV0NLTTZFSVVOR0lXN3p1SklxY0xBRzF1Nk1Yci1mNXB0OFNZUE40UHp0WTdnSGFGcFdVRTFNaTJtYlE2UFRZUDQ5d2lrYmV4MFpYUUp4U2xJemQyWjE1Ni11M1JrdFdyNzFLeW9kM0YxbGg5ZWV0T0ZieTRPX0o0dFY3djQxeF9ucVBuajVGNGlfN084QmV4ZUpmSGgtMEVuY212XzJtTVUtd0VWVQ?oc=5

---

### 3. A Revealed Preference Framework for AI Alignment (arxiv)
**Bizonyíték:** Formális modell: mikor implementálja az AI agent a human principal preferenciáit vs. a sajátját? "Luce Alignment Model" — levezetés arra, mikor divergál az agent a delegált szándéktól. Egyszerre lab és field setting.
**Relevancia:** MAGAS — AI decision delegation blindspot: ha az agent "saját" döntési mintát tanul, hogyan detektálod?
- Dátum: 2026-03-29
- Forrás: arxiv
- URL: https://arxiv.org/abs/2603.27868v1

---

### 4. Anthropic: Claude kód szivárgás (WSJ)
**Bizonyíték:** Anthropic versenyt futott az ellen, hogy a Claude AI agent belso kódbázisa kiszivárogjon. Jelzi: az agent-infrastruktúra IP-je és biztonsági modellje egyre értékesebb célpont.
**Relevancia:** MAGAS — Produkciós agent rendszer IP-védelme, zárt vs. nyílt architektúra tradeoff.
- Dátum: 2026-04-01
- Forrás: hackernews (WSJ)
- URL: https://www.wsj.com/tech/ai/anthropic-races-to-contain-leak-of-code-behind-claude-ai-agent-4bc5acc7

---

### 5. Terminal Agents Suffice for Enterprise Automation (HuggingFace/paper)
**Bizonyíték:** Kutatás bizonyítja: terminál + filesystem hozzáféréssel rendelkezo egyszerú coding agent JOBB eredményt ér el, mint komplex MCP/web-UI alapú architektúrák. Direkt API interakció elegendő.
**Relevancia:** STRATÉGIAI — Navibase agent design döntés: ne túlbonyolítsuk. Ez a mi jelenlegi megközelítésünket igazolja.
- Dátum: 2026-03-31
- Forrás: huggingface
- URL: https://huggingface.co/papers/2604.00073

---

### 6. Phantom – AI agent on its own VM that rewrites its config (Show HN)
**Bizonyíték:** Open-source agent, amely saját VM-en fut és önmaga újraírja a konfigurációját. Önmodifikáló agent prototípus — megjelenik a "self-configuring agent" pattern.
**Relevancia:** KÖZEPES/MAGAS — Self-configuration edge case; governance és audit szempontból kockázati minta.
- Dátum: 2026-03-30
- Forrás: hackernews
- URL: https://github.com/ghostwright/phantom

---

### 7. AWS Deploys AI Agents for DevOps and Security Teams (Forbes)
**Bizonyíték:** AWS bejelenti, hogy AI agenteket telepít DevOps és Security csapatok munkájának elvégzésére — nem csak segítségként, hanem "végzik a munkát."
**Relevancia:** PIACI — Az enterprise szegmens elkezdett valódi operational delegation-t végrehajtani. KKV belépési pont hamarosan.
- Dátum: 2026-04-01
- Forrás: google_news (Forbes)
- URL: https://news.google.com/rss/articles/CBMiuwFBVV95cUxPN0xmX2VycExqMzRJc3BKd0RYb3Jzc3kxQ1NSa1RkRXJwNjN0VE55ZnBmUy05cmVwYXhTQWlYbFlEb0JKN0l2NUNhVmt0Z3pjemlGcGVXWFJTaWkzWHdfY0JkenpDSjVielNBSEM4T0I0Q3p4VHZnYlJTeEc3Wl91TnZPSGVqR3pKMHdWbkJQeF9pbm4ycm9NeGFOaW9mOHpiaFdVQUQtWFJ1WW5tME1BZGZiQWlTa2ZNLVJ3?oc=5

---

### 8. $65M seed — enterprise AI agent startup (TechCrunch)
**Bizonyíték:** Ex-Coatue partner $65M seed-et zárt enterprise AI agent startupba. Befektetoi alap igazolás: az enterprise agent piac komoly pénzeket von be.
**Relevancia:** PIACI — Versenynyomás jelzés. A Navibase-nek differenciálnia kell mielőtt ez a piac telítodik.
- Dátum: 2026-03-30
- Forrás: techcrunch
- URL: https://techcrunch.com/2026/03/30/former-coatue-partner-raises-huge-65m-seed-for-enterprise-ai-agent-startup/

---

### 9. Q1 startup funding record (TechCrunch) — AI decision delegation kategória
**Bizonyíték:** Q1 2026 rekord tőkebevonás, 4 mega-deal: OpenAI, Anthropic, xAI, Waymo. Az AI-ba áramló toke nem lassul — a piac az agentek üzleti alkalmazásába fektet.
**Relevancia:** HÁTTÉR — Ecosystema-szintu gyorsulás. Az agent piac nem korrigál, csak nő.
- Dátum: 2026-04-01
- Forrás: techcrunch
- URL: https://techcrunch.com/2026/04/01/startup-funding-shatters-all-records-in-q1/

---

### 10. Autonomous AI agents in business organizations (Jerusalem Post)
**Bizonyíték:** Elemzés arról, hogyan integrálódnak autonóm AI agentek üzleti szervezetekbe — fókusz: döntési jogkörök, felelősségi láncok, emberi oversight.
**Relevancia:** KKV KONTEXTUS — Pontosan a Navibase célpiac (KKV CEO-k) problématere. Referencia cikk ügyfél-edukációhoz.
- Dátum: 2026-03-27
- Forrás: google_news (Jerusalem Post)
- URL: https://news.google.com/rss/articles/CBMiXEFVX3lxTFBBLUJRVDhqUkc2dEVBUFhKbFhZLUNwMHlwNDFxazVhVUpnb1VhMlN3Mk1NcHNzbVg0Q1hpNGhWV2QxckdNRHVBSWpWWEpIUTltOVRmUlVILUNHRVBU?oc=5

---

## Teljes signal lista (1-30)

| # | Cím | Forrás | Dátum | URL |
|---|-----|--------|-------|-----|
| 1 | anthropics / claude code | github_trending | 2026-04-02 | https://github.com/anthropics/claude-code |
| 2 | Mutation Testing for the Agentic Era | hackernews | 2026-04-01 | https://blog.trailofbits.com/2026/04/01/mutation-testing-for-the-agentic-era/ |
| 3 | Startup funding shatters all records in Q1 | techcrunch | 2026-04-01 | https://techcrunch.com/2026/04/01/startup-funding-shatters-all-records-in-q1/ |
| 4 | Google Deepmind: 6 "traps" for autonomous AI agents | google_news | 2026-04-01 | (google news link) |
| 5 | Anthropic Races to Contain Leak of Code Behind Claude AI Agent | hackernews (WSJ) | 2026-04-01 | https://www.wsj.com/tech/ai/anthropic-races-to-contain-leak-of-code-behind-claude-ai-agent-4bc5acc7 |
| 6 | Show HN: Baton – desktop app for developing with AI agents | hackernews | 2026-04-01 | https://getbaton.dev/ |
| 7 | AWS Deploys AI Agents To Do The Work Of DevOps And Security Teams | google_news (Forbes) | 2026-04-01 | (google news link) |
| 8 | OpenBMB / ChatDev 2.0 | github_trending | 2026-04-01 | https://github.com/OpenBMB/ChatDev |
| 9 | microsoft / agent lightning | github_trending | 2026-04-01 | https://github.com/microsoft/agent-lightning |
| 10 | Claw4Science: OpenClaw Scientific Agent Ecosystem dataset | biorxiv | 2026-04-01 | https://www.biorxiv.org/content/10.64898/2026.03.30.715118 |
| 11 | Terminal Agents Suffice for Enterprise Automation | huggingface | 2026-03-31 | https://huggingface.co/papers/2604.00073 |
| 12 | Show HN: Pardus Browser – browser for AI agents without Chromium | hackernews | 2026-03-31 | https://github.com/JasonHonKL/PardusBrowser/tree/main |
| 13 | AgentCypher launches Joker King (autonomous AI agent card game) | google_news | 2026-03-31 | (google news link) |
| 14 | Show HN: 3D-print pegboard with AI agent (Codex) | hackernews | 2026-03-30 | https://github.com/virpo/pegboard |
| 15 | Former Coatue partner raises $65M seed for enterprise AI agent startup | techcrunch | 2026-03-30 | https://techcrunch.com/2026/03/30/former-coatue-partner-raises-huge-65m-seed-for-enterprise-ai-agent-startup/ |
| 16 | Agentic AI and the next intelligence explosion | hackernews (arxiv) | 2026-03-30 | https://arxiv.org/abs/2603.20639 |
| 17 | Show HN: Phantom – AI agent on its own VM that rewrites its config | hackernews | 2026-03-30 | https://github.com/ghostwright/phantom |
| 18 | OpenBB – financial data platform for AI agents | github_trending | 2026-03-30 | https://github.com/OpenBB-finance/OpenBB |
| 19 | A Revealed Preference Framework for AI Alignment | arxiv | 2026-03-29 | https://arxiv.org/abs/2603.27868v1 |
| 20 | Show HN: Pglens – 27 read-only PostgreSQL tools for AI agents via MCP | hackernews | 2026-03-29 | https://github.com/janbjorge/pglens |
| 21 | AT&T Data Scientist Builds Autonomous AI Agents | google_news | 2026-03-29 | (google news link) |
| 22 | AI Agents Become Governance Infrastructure | google_news (National Today) | 2026-03-29 | (google news link) |
| 23 | Show HN: A prompt that builds the most capable AI agent system | hackernews | 2026-03-28 | https://github.com/fainir/most-capable-agent-system-prompt |
| 24 | Using OpenClaw as a Force Multiplier | google_news (Towards Data Science) | 2026-03-28 | (google news link) |
| 25 | Cline Kanban – CLI-agnostic kanban for multi-agent orchestration | product_hunt | 2026-03-28 | https://www.producthunt.com/products/cline-4 |
| 26 | Elon Musk's last co-founder reportedly leaves xAI | techcrunch | 2026-03-28 | https://techcrunch.com/2026/03/28/elon-musks-last-co-founder-reportedly-leaves-xai/ |
| 27 | Show HN: Enlidea – multi-agent research hub, reverse-CAPTCHA waitlist | hackernews | 2026-03-28 | https://enlidea.com |
| 28 | SakanaAI / AI Scientist v2 (workshop-level automated scientific discovery) | github_trending | 2026-03-28 | https://github.com/SakanaAI/AI-Scientist-v2 |
| 29 | Show HN: Kagento – LeetCode for AI Agents | hackernews | 2026-03-27 | https://kagento.io |
| 30 | Autonomous AI agents in business organizations | google_news (Jerusalem Post) | 2026-03-27 | (google news link) |

---

## Összefoglalás

**Domináns témák ma:**
1. **Biztonsági / governance fenyegetések** — DeepMind 6 trap, Phantom önmódosító agent, Anthropic kód-szivárgás
2. **Enterprise delegation gyorsulás** — AWS, $65M seed, AT&T saját agentek
3. **Alignment gap** — arxiv paper az AI decision delegation divergenciáról
4. **Platform szintű gyorsulás** — Claude Code trending, agent-lightning (Microsoft), ChatDev 2.0

**Legfontosabb Navibase-relevans insight:**
- Az agent governance / audit trail hiánya már mainstream téma — ez a Navibase differenciátor lehetosége
- A "terminal agent suffices" paper igazolja az egyszerű architektúra választásunkat
- A KKV szegmens döntési delegálás cikkek pontosan a mi pitch területünk

_Generálva: 2026-04-02 09:05 CET | Forrás: HAIER export | 232 relevans signal / 1416 összesen_
