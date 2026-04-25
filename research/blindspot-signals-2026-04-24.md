# 🕵️ Agent Platform Blindspot Radar — 2026-04-24

**Forrás:** HAIER export `evolution_signals_20260424_033140.json`  
**Szűrő:** `focus_area` → `AI agents` | `AI decision delegation`  
**Releváns találatok:** 459 / 3049  
**Vizsgált:** első 30 signal  

---

## 🔥 Top 10 Legerősebb Signal

---

### 1. 🔐 GAAP — Garantált Agent Privacy Execution Environment
**[An AI Agent Execution Environment to Safeguard User Data](https://arxiv.org/abs/2604.19657)**  
📅 2026-04-21 | focus: AI agents

**Bizonyíték:** GAAP (Guaranteed Accounting for Agent Privacy) — determinisztikus Information Flow Control, amely megakadályozza, hogy az AI agent privát adatokat szivárogtathasson el, _beleértve az AI modell providerét is_. Prompt injection ellen is véd. Cross-task tracking.  
**Blindspot:** Az agent identity réteg és a data permission layer szétválasztása — a user engedélyezi a flow-t, nem bízik az agentben. Ez az architektúra paradigmaváltás az agent trust modelben.

---

### 2. 🚨 Cross-Session Threat Detection — Új Benchmark (CSTM-Bench)
**[Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms](https://arxiv.org/abs/2604.21131)**  
📅 2026-04-22 | focus: AI agents

**Bizonyíték:** 26 attack taxonomia, amely _session-határokat átlép_ — session-bound guardrail-ok vakok rá. A payload több session-re van elosztva. Csak a Coreset Memory Reader (K=50) tartja meg a recall-t mindkét tesztkörnyezetben.  
**Blindspot:** Jelenlegi agent guardrail-ok memóriátlanok — cross-session kompozit támadásokra teljesen vakok. Kritikus gap enterprise deploymentnél.

---

### 3. 🔑 Agent Vault — Open-Source Credential Proxy Agentekhez
**[Show HN: Agent Vault – Open-source credential proxy and vault for agents](https://github.com/Infisical/agent-vault)**  
📅 2026-04-22 | focus: AI agents

**Bizonyíték:** Infisical open-source HTTP credential proxy: az agent _soha nem látja a credentialt_, csak proxylt kérést küld. Anthropic Managed Agents architektúrájával kompatibilis. Credential brokering mint iparági standard felé mozdul.  
**Blindspot:** Az agent secret management még rendezetlen iparági szinten — az Agent Vault az első open-source implementáció, ami ezt megoldja credential exfiltration ellen.

---

### 4. 📊 AGENTS.md Governance Prompts — 37% Strukturálisan Hiányos
**[Structural Quality Gaps in Practitioner AI Governance Prompts](https://arxiv.org/abs/2604.21090)**  
📅 2026-04-22 | focus: AI agents, AI decision delegation

**Bizonyíték:** 34 publikus AGENTS.md fájl elemzése: 37%-uk nem éri el a strukturális teljességi küszöböt. Leghiányosabb területek: data classification és assessment rubric. Számíthatóság-elméleti keretrendszer alapján értékelve.  
**Blindspot:** Az agent governance prompt mint "executable specification" — de gyakorlatilag senki nem írja helyesen. Automatikus static analysis eszközre van szükség.

---

### 5. 🏢 Stateless Decision Memory — Enterprise Agent Audit Trail
**[Stateless Decision Memory for Enterprise AI Agents](https://arxiv.org/abs/2604.20158)**  
📅 2026-04-22 | focus: AI agents

**Bizonyíték:** DPM (Deterministic Projection Memory) — append-only event log + egyetlen projection döntési időben. Regulated deployment (underwriting, claims, tax) esetén 7-15x gyorsabb, 2 LLM call vs. 83-97 call auditálható. Faktális precizitás +0.52 Cohen h=1.17 (p=0.0014).  
**Blindspot:** Stateful agent memória architektúrák enterprise-ban használhatatlanok — a statelessness a load-bearing tulajdonság, nem az intelligencia.

---

### 6. 👁️ Pista — Emberi Felügyelet Agent Döntési Lépésenként
**[Auditing and Controlling AI Agent Actions in Spreadsheets](https://arxiv.org/abs/2604.20070)**  
📅 2026-04-22 | focus: AI agents

**Bizonyíték:** Pista rendszer (N=16 within-subjects study): aktív beavatkozás minden agent lépésnél — felhasználók azonosítják saját szándékukat az agent döntéseiben, hibákat találnak amiket utólagos review nem fedett volna fel. Co-ownership érzet.  
**Blindspot:** Post-hoc review elégtelen — meaningful human oversight csak real-time participációval lehetséges. Ez az agent UX következő rétege.

---

### 7. 🔒 Behavioral Transfer — Agent Mint Privacy Kockázat
**[Behavioral Transfer in AI Agents: Evidence and Privacy Implications](https://arxiv.org/abs/2604.19925)**  
📅 2026-04-21 | focus: AI agents

**Bizonyíték:** 10.659 human-agent pár (Moltbook platform): az agent szisztematikusan tükrözi a tulajdonos viselkedési karakterisztikáit (topic, értékek, affekt, stílus) — _explicit konfiguráció nélkül is_. Erősebb behavioral transfer → több személyes adat szivárgás.  
**Blindspot:** Az agent nem generikus output-ot produkál — behavioral fingerprinting révén az owner azonosítható. Platform design és agent governance implikáció.

---

### 8. ⚖️ EU AI Act "Last Mile" — Compliance vs. Fejlesztői Valóság
**[Engaged AI Governance: Addressing the Last Mile Challenge](https://arxiv.org/abs/2604.21554)**  
📅 2026-04-23 | focus: AI decision delegation

**Bizonyíték:** 10 újságíró interjú + insider action research AI startupnál. Három practitioner minta: konvergencia, meglévő gyakorlat, és disconnection (regulatory overhead). Verification-oriented requirements → box-ticking. Expert collaboration pipeline EU AI Act → actionable strategy.  
**Blindspot:** A compliance governance vagy genuine, vagy performatív — az elkülönítő faktor a translation challenge: ha a fejlesztők nem értik hogyan szolgálja a compliance a product minőségét, átverésként kezelik.

---

### 9. 🏛️ AI Governance Politikai Felügyelet Alatt — Formális Modell
**[AI Governance under Political Turnover](https://arxiv.org/abs/2604.21103)**  
📅 2026-04-22 | focus: AI decision delegation

**Bizonyíték:** Formális modell: intézmények választanak automation scale, codification mértéke és safeguard között. Compliance layer mint stable approval boundary — amelyet politikai utódok megtanulnak navigálni miközben a lawful administration látszatát fenntartják. Nehéz visszavonni.  
**Blindspot:** Az AI governance rendszer egyszer felépítve path-dependent lesz — a compliance réteg maga válik a hatalmi struktúra részévé. Agent deployment politikai kockázata alábecsült.

---

### 10. 🔴 Context AI Security Incident — Compliance Startup Bukás
**[Another customer of troubled startup Delve suffered a big security incident](https://techcrunch.com/2026/04/23/another-customer-of-troubled-startup-delve-suffered-a-big-security-incident/)**  
📅 2026-04-23 | focus: AI agents

**Bizonyíték:** Delve compliance startup — aki AI agent training céget (Context AI) auditált — maga is security incidensben érintett. A compliance certifier kompromittálódott.  
**Blindspot:** Third-party AI compliance audit infrastruktúra megbízhatósága alapvetően kérdéses. A "certified compliance" nem jelent tényleges biztonságot.

---

## 📋 Összes Vizsgált Signal (30/30)

| # | Cím | Dátum | Focus |
|---|-----|-------|-------|
| 1 | marketingskills for Claude Code | 2026-04-24 | AI agents |
| 2 | Nemobot Games: Strategic AI Gaming Agents | 2026-04-23 | AI agents |
| 3 | Task-Driven Co-Design of Heterogeneous Multi-Robot | 2026-04-23 | AI agents, robotics |
| 4 | Gradual Voluntary Participation (GVP) — Journalism AI | 2026-04-23 | AI decision delegation |
| 5 | Context AI / Delve security incident | 2026-04-23 | AI agents |
| 6 | EU AI Act "Last Mile" — Engaged AI Governance | 2026-04-23 | AI decision delegation |
| 7 | Langfuse — LLM Observability platform | 2026-04-23 | AI agents |
| 8 | Cross-Session Threats Benchmark (CSTM-Bench) | 2026-04-22 | AI agents |
| 9 | AI Governance under Political Turnover | 2026-04-22 | AI decision delegation |
| 10 | AGENTS.md Governance Prompts Quality Gaps | 2026-04-22 | AI agents, AI decision delegation |
| 11 | ServiceNow + Google Cloud unite AI agents | 2026-04-22 | AI agents |
| 12 | Trainly — AI agent production trace audit | 2026-04-22 | AI agents |
| 13 | Agent Vault — credential proxy (Infisical) | 2026-04-22 | AI agents |
| 14 | Responsible AI governance in 90 days | 2026-04-22 | AI decision delegation |
| 15 | Google TPU 8th gen — agentic era chips | 2026-04-22 | AI agents |
| 16 | Google connective tissue for autonomous agents | 2026-04-22 | AI agents |
| 17 | WebGen-R1 — RL for website generation | 2026-04-22 | AI agents |
| 18 | Bimanual Robot Manipulation via Multi-Agent ICL | 2026-04-22 | AI agents, robotics |
| 19 | AI governance — new category of tech talent | 2026-04-22 | AI decision delegation |
| 20 | GPT 5.5 Released in Codex | 2026-04-22 | AI agents |
| 21 | Stateless Decision Memory for Enterprise AI Agents | 2026-04-22 | AI agents |
| 22 | TabMail — agentic email assistant | 2026-04-22 | AI agents |
| 23 | Microsoft AI Agents for Beginners (12 lessons) | 2026-04-22 | AI agents |
| 24 | Pista — Auditing AI Agent Actions in Spreadsheets | 2026-04-22 | AI agents |
| 25 | Information Aggregation with AI Agents | 2026-04-21 | AI agents |
| 26 | SpaceX + Cursor $60B option deal | 2026-04-21 | AI decision delegation |
| 27 | Meta trains AI agents via employee tracking | 2026-04-21 | AI agents |
| 28 | NeoCognition $40M seed — agents that learn like humans | 2026-04-21 | AI agents |
| 29 | Behavioral Transfer in AI Agents — Privacy Implications | 2026-04-21 | AI agents |
| 30 | GAAP — AI Agent Privacy Execution Environment | 2026-04-21 | AI agents |

---

*Generálva: 2026-04-24 | HAIER export: evolution_signals_20260424_033140.json | Releváns pool: 459 signal*
