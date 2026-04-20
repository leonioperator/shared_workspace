# Blindspot Radar — Scored Hypothesis List
Last updated: 2026-04-13

## H59 - Agent Credential Brokerage (Secretless access for coding agents)
**Thesis:** A coding agenteknek egyre több külső rendszerhez kell hozzáférés (GitHub, DB, billing, infra), de a long-lived API keyk .env-ben vagy chatben való kezelése tarthatatlan. A piac egy "credential broker" mintázat felé tolódik: OIDC/token exchange, rövid életu, scope-olt cred, audit stream, és egyértelmu delegation chain.
**Signals (updated 2026-04-15):**
- Kontext CLI (GitHub, 2026-04-14): credential broker AI coding agentekhez (OIDC + token exchange, short-lived scoped creds, audit streaming). https://github.com/kontext-dev/kontext-cli
- Cred (Product Hunt, 2026-04-09): OAuth credential delegation AI agenteknek. https://www.producthunt.com/products/cred-3
**Assessment:** Ez a H37/H53 irány gyakorlati termékesedése. A buyer nyelv egyszeru: "nem adom oda a kulcsaimat". Navibase: drop-in JIT token issuance + audit korreláció, plusz consent receipt (H44) a high-risk műveletekhez.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-15). A Kontext a cred-delegation mintát konkrét eszközzé teszi, ami felgyorsítja a table stakes szintet.*

## H60 - Agent Identity Platform (Lifecycle, authZ, audit as primitives)
**Thesis:** Az agent identity nem csak "token scope", hanem teljes lifecycle: agent principal típus, provisioning/deprovisioning, policy, attestation, audit export, és ownership. Ahogy az agentek autonómabbá válnak, külön identity platform jelenik meg kifejezetten agentekre.
**Signals (updated 2026-04-15):**
- ZeroID (Help Net Security, 2026-04-13): open-source identity platform autonomous agentekhez. https://news.google.com/rss/articles/CBMiowFBVV95cUxNQ0tqVkFiZV9IbjR1R1ZMVVZVdHpMZjcta0VTV3hxSllhNkpmaUFWYzdSZmFZQjd3SlZ5UzNlU083Ql9pa0E1ajF4alBYRktpdEVFYnFlTVprNHBQTXNwWWFFNVFhVVdlVmRKdkNHVjdCTFFFSnIwSmgzdDdMOTJKTThjbURYOU9LOUFTcGotQ1NqVmhraFA2OGswMGhxQWlfamZv?oc=5
**Assessment:** Ez a H1/H40 kiegészítő, de termék-szinten: identity control plane agenteknek. Navibase: nem feltétlen saját IDP, inkább kompatibilitás, evidence export és "agent principal" best practice csomag.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-15). A ZeroID jelzi, hogy az agent identity külön platformrétegként kezd kristályosodni.*

## H61 - Agent Failure Investigation Automation (RCA for LLM apps)
**Thesis:** A production agentek nem "crash-elnek", hanem csendben rossz kimenetet adnak. A trace-ek kézi elemzése skálázhatatlan. Kell egy RCA réteg, ami automatikusan klaszterez, root cause hipotéziseket javasol, és a hibákhoz javítási útvonalat ad.
**Signals (updated 2026-04-15):**
- Kelet (2026-04-14): root cause analysis agent LLM appokhoz, trace scroll helyett mintázat felismerés. https://kelet.ai/
**Assessment:** Rokona a H32 trace-to-patch-nek, de ops fókuszú: "mi romlott el" és "hol". Navibase: Leoni reliability javítás gyors ROI, plusz enterprise audit story (H41).
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-04-15). A Kelet azt jelzi, hogy a hibakeresés önálló termékkategória lesz agent rendszereknél.*

## Top 3 Opportunities + Suggested Experiments (2026-04-15)

### #1: H59 - Credential broker demo (secretless-by-default gyors proof)
**Miért most:** Kontext + Cred együtt jelzi, hogy a buyer elvárás a rövid életu, scope-olt credential. Ez az egyik leggyorsabban értékesíthető bizalmi wedge.
**Kísérlet:** 3 napos demo: OIDC token exchange + JIT token issuance + audit correlation id (run id). Deliverable: 1 oldalas evidence export + 2 perces képernyőfelvétel.

### #2: H61 - RCA pilot Leoni trace-eken (belső gyors ROI)
**Miért most:** A trace-ek már megvannak, a kézi elemzés drága. A buyer nyelv: "miért nem azt csinálta".
**Kísérlet:** 1 hét: utolsó 30 nap hibás run klaszterezése, top 10 failure pattern + javasolt guardrail/prompt/policy fix. Mérők: human intervention rate csökkenés, regressziók száma.

### #3: H60 - Agent identity platform scan (ZeroID fit + gap list)
**Miért most:** Identity lifecycle most fordul át "nice"-ból "compliance kérdés"-sé.
**Kísérlet:** 2 nap: ZeroID áttekintés + "agent principal" checklist (provisioning, rotation, deprovision, audit export). Output: gap lista Navibase/Leoni-hoz és 1 integrációs útvonal.

## H46 — Cloud Sandbox Delegation Harness (PR-returning cloud agents)
**Thesis:** A coding agentek következő hulláma nem IDE plugin, hanem *delegációs harness*: chat/Slack/GitHub felől leírsz egy feladatot, és a rendszer izolált cloud sandboxban futtatja a lab-native CLI agentet (Claude Code/Codex), majd PR-t/review-t/diagnózist ad vissza. A buyer pain: párhuzamosíthatóság, per-task izoláció, perzisztencia (éjszaka is fut), és a „local machine trust gap”.
**Signals (updated 2026-04-12):**
- Twill.ai (Launch HN, 2026-04-10): „delegate to cloud agents, get back PRs”, explicit izolált sandbox + PR output + crons/event triggers. HIGH CONFIDENCE.
**Assessment:** Ez devtool kategória, de közvetlenül erősíti a Navibase platform narratívát: a harness engineering (izoláció, policy hook, audit trail, persistence) lesz a differenciáló, nem a modell. Navibase irány: nem feltétlen competing harness, hanem compliance/governance layer partner-stratégia ilyen harness-ek fölé.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-04-12). A Twill nagyon tisztán megfogalmazza a „delegációs harness” kategóriát és a buyer nyelvet.*

## H47 — Secure Agent Gateway Layer (Threat models + batteries-included switching)
**Thesis:** A platform blindspot, hogy a csapatok több agent/harness/toolchain között váltanak, de nincs egységes, security-first gateway: identitás, policy, secrets, allowlist, audit export, és „channel ownership” kezelés egy helyen. A gateway lehet tool-agnosztikus, és „batteries included” módon ad baseline védelmet mind external támadó (prompt injection/tool poisoning) mind internal agentic failure ellen.
**Signals (updated 2026-04-12):**
- Zeroclawed (Show HN, 2026-04-10): „Secure Agent Gateway”, kifejezetten több agent toolchain köré épített gateway, threat model fókusz. HIGH CONFIDENCE.
**Assessment:** Erős összhang H22/H24/H2/H6 vonallal. A gateway wedge buyer-friendly, mert gyorsan ad „control plane” érzést. Navibase alkalmazás: gateway-pozicionálás (vagy kompatibilitás) és exportálható evidence pack.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-12). A Zeroclawed jelzi, hogy a „gateway-first” security gondolkodás termékké válik.*

## H48 — Agent Runtime Embedding into Reactive Compute (Notebook-as-harness)
**Thesis:** Az agentek egy része nem „beszélget”, hanem *fut a compute mellett*: notebook/REPL session mint working memory + execution runtime, ahol a human és az agent közösen iterál. A reactive notebook mint harness csökkenti a hallucination kockázatot (run-to-verify), és auditálható, reprodukálható munkát ad (a notebook fájl maga a trace).
**Signals (updated 2026-04-12):**
- marimo pair (Show HN, 2026-04-07): agent skill, ami futó notebook sessionbe „beleülteti” az agentet, code-mode, cell edit/insert/delete, install packages, reprodukálható programként rögzít. HIGH CONFIDENCE.
**Assessment:** Ez nem enterprise governance wedge első körben, inkább R&D/data csapatok adoption mintázata. Navibase-nél: „evidence-by-default” gondolkodás erősítése, mert a munkavégzés artifact-ja automatikusan keletkezik (H41).
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=3 | **Total: 14/25**
*Új hypothesis (2026-04-12). A notebook-as-harness minta egyre inkább standardizálja a „run, then trust” workflow-t.*

## H49 — OSS Local-First Agent Framework Convergence (install, execute, test)
**Thesis:** Több open-source agent keretrendszer (goose stb.) a „beyond suggestions” irányba megy: install, execute, edit, test. A risk: framework-sprawl és inconsistent governance. A lehetőség: standard policy/audit hooks és conformance layer, ami több OSS framework felett működik.
**Signals (updated 2026-04-12):**
- goose (GitHub, 2026-04-12): „install, execute, edit, and test with any LLM”, explicit local-first execution. HIGH CONFIDENCE.
**Assessment:** Önmagában nem top wedge, de erősíti a H3/H42 irányt: standard security profiles és audit hooks kellenek a toolchain sprawl miatt. Navibase: conformance scan + evidence export.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=3 | **Total: 14/25**
*Új hypothesis (2026-04-12). A goose jelzi, hogy a local-first agent runtime mainstream open-source mintává válik.*

## H50 — Trustworthy Agent Benchmarks & Evidence (Benchmark-driven procurement)
**Thesis:** A buyer (procurement/security) elkezdi „bizonyítékhoz” kötni az agent adoptiont: nem csak vendor claim, hanem benchmark eredmény, attack-resilience, és audit evidence. A benchmarkok megtörése és a benchmarkok hiányosságainak nyilvános elemzése egyaránt jelzi, hogy a benchmark mint procurement eszköz erősödik.
**Signals (updated 2026-04-12):**
- Berkeley RDI: “How We Broke Top AI Agent Benchmarks: And What Comes Next” (2026-04-11). HIGH CONFIDENCE.
**Assessment:** Ez a H41/H22/H23 metszete: evidence pack + robustness + QA. Navibase alkalmazás: benchmark-alapú „readiness score” és dokumentálható test suite, amit sales/procurement nyelven lehet eladni.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-12). A benchmark diskurzus a procurement nyelv felé tolja az agent governance kategóriát.*

## H51 — Autonomous Loop Runners for PRD Completion (Agent Task Closure Engine)
**Thesis:** A következő dev-agent wedge nem csak ‘generate code’, hanem egy zárt hurkú végrehajtó: a PRD (vagy issue checklist) tételein iterál, futtat, ellenőriz, és addig ismétel, amíg minden tétel teljesül, majd bizonyítékot ad (diff/test output). Ez csökkenti a ‘félkész PR’ és ‘human shepherding’ terhet.
**Signals (updated 2026-04-13):**
- snarktank/ralph (GitHub, 2026-04-13): ‘autonomous AI agent loop that runs repeatedly until all PRD items are complete’ — explicit loop-runner kategória. https://github.com/snarktank/ralph
**Assessment:** A Twill-féle delegációs harness (H46) és a trace-to-patch (H32) mellett ez egy konkrét execution primitive: ‘task closure loop’. Navibase szempont: nem feltétlen termék, de a reliability és evidence-by-default narratívát erősíti (H41).
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=2 | **Total: 15/25**
*Új hypothesis (2026-04-13). A ‘loop until complete’ framing buyer-nyelv: outcome, nem output.*

## H52 — Inline Review Loops for Agents (Diff/Plan Annotation → Agent Patch)
**Thesis:** A coding agenteknél a legnagyobb friction a review roundtrip. Egy agent-native review UI (TUI overlay) ami diffet vagy tervet mutat, inline annotációt vesz fel, majd visszatolja az agentnek, gyorsítja a iterációs ciklust és csökkenti a félreértéseket. A review maga ‘tool’ lesz.
**Signals (updated 2026-04-13):**
- umputun/revdiff (GitHub, 2026-04-12): TUI diff reviewer inline annotációval, Claude Code plugin, plan-review hook (revdiff-planning). https://github.com/umputun/revdiff
**Assessment:** Ez nagyon jól illeszkedik a H25 (multi-agent workspace orchestration) és H19 (operational reliability) köré: a review a legdrágább emberi idő, a visszacsatolás strukturálása a ROI. Navibase: ha fejlesztői ügynököket futtatunk, ez a human-in-the-loop UX minta exportálható.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=2 | IntFric=2 | **Total: 15/25**
*Új hypothesis (2026-04-13). A revdiff azt jelzi, hogy a ‘review loop tooling’ külön termékkategória lesz.*

## H53 — Agent Secret Handling & Key Trust Boundary (Secretless-by-default Patterns)
**Thesis:** A produkciós agent adoption egyik legkeményebb bizalmi határa: ‘odaadhatom-e a kulcsaimat’. A piac a long-lived .env kulcsok felől a scoped, rövid életű, delegált credential minták felé tolódik. A wedge: secret minimization, JIT tokenek, approval gates, és auditált secret access.
**Signals (updated 2026-04-13):**
- Ask HN: ‘Do you trust AI agents with API keys / private keys?’ (HN, 2026-04-12): explicit practitioner pain a secret megosztásról. https://news.ycombinator.com/item?id=47736831
**Assessment:** Ez közvetlenül erősíti a H37 (OAuth credential delegation) és H40 (workload attestation) vonalat, de buyer-szinten a ‘kulcsok odaadhatósága’ a döntő kérdés. Navibase: egyszerű kommunikációs és termék-packaging lehetőség: ‘secretless by default’ + consent receipts (H44).
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-13). A HN thread jelzi, hogy ez már nem elméleti compliance kérdés, hanem napi dev/ops dilemma.*

## H54 — Long-Term Collaboration Memory as Shared Infrastructure (Episodic + World Model)
**Thesis:** Hosszú távú human-AI együttműködésnél a legnagyobb teljesítmény-limit nem a modell, hanem a közös memória és a ‘project world model’. A memory rendszer nem chat log, hanem strukturált, indexelt, karbantartott tudás (episodic + reality), explicit műveletekkel (read/update/maintain).
**Signals (updated 2026-04-13):**
- visionscaper/collabmem (GitHub, 2026-04-11): long-term collaboration memory system sentinel tokenekkel, világmodell + történet index. https://github.com/visionscaper/collabmem
**Assessment:** A kategória zsúfolt (H8), de a collabmem explicit ‘maintenance protocol’ mintája fontos: a memory rendszer nem csak store, hanem workflow. Navibase: a Leoni jellegű ops agentnél ez közvetlen érték, mert a döntések és kontextus auditálhatóbbá válik.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=3 | **Total: 16/25**
*Új hypothesis (2026-04-13). A ‘sentinel token + maintenance’ minta a memory operációsítását jelzi.*

## H55 — Interactive Terminal Program Control Layer (TUI Automation as Primitive)
**Thesis:** Az agentek egyre több legacy/interactive CLI-t kell vezéreljenek (git TUI, db console, infra TUI). Ehhez kell egy TUI automation primitive: képernyő-állapot felismerés, input események, transcript, és permission/intervention. Ez az ‘agent ops surface’ új attack és governance felület.
**Signals (updated 2026-04-13):**
- onesuper/tui-use (GitHub, 2026-04-08): AI agents control interactive terminal programs. https://github.com/onesuper/tui-use
**Assessment:** Ez a H39/H34 (ops monitoring) fejlesztői megfelelője: nem remote desktop, hanem terminal-level control. Navibase: belső eszköztárban hasznos, de enterprise-ben governance nélkül kockázatos, ezért összeér H22/H6-tal.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=3 | **Total: 14/25**
*Új hypothesis (2026-04-13). A TUI control az agent capability-k standardizálódó alsó rétege.*

## H56 — In-Browser Design Editing → Agent Code Patches (Design-to-Agent Feedback Loop)
**Thesis:** A ‘design by hand, code by agent’ workflow stabilizálódik: a user a böngészőben vizuálisan módosít, a változás strukturált eseményként megy az agenthez, aki patch-et készít a kódbázisban. Ez csökkenti a design-dev roundtripet és a félreértéseket.
**Signals (updated 2026-04-13):**
- cssstudio.ai (2026-04-09): in-browser editing, MCP-szerű event stream az agenthez, agent kódot módosít. https://cssstudio.ai
**Assessment:** Ez a H25 (workspace orchestration) és a MCP governance (H3/H42) metszete: új tool surface (UI events) plusz audit/permission igény. Navibase: KKV webes projektekben gyors revenue wedge lehet, ha van safe change wrapper.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=3 | **Total: 16/25**
*Új hypothesis (2026-04-13). A CSS Studio jelzi, hogy a UI-event alapú agent input mainstream minta.*

## H57 — Agent-Native Video Knowledge Bases (YouTube-to-Wiki, scene-aware)
**Thesis:** A „knowledge base” következő hulláma nem (csak) dokumentum-RAG, hanem **videókból** épített, kompaundáló tudás: transcript + scene change detektálás + key frame leírás → strukturált wiki oldalak, amikből az agent gyorsan visszakeres és hivatkozik. A value: a hosszú videók (talkok, belső felvételek, tréning) végre **repo-natív**, kereshető és idézhető tudásként élnek, nem „scrubolós” időrablásként.
**Signals (updated 2026-04-14):**
- mcptube / mcptube-vision (Show HN, 2026-04-13): Karpathy LLM Wiki minta YouTube-ra, ingest-time wiki page generálás, ffmpeg scene change + vision keyframe leírás, FTS5 keresés, MCP server mód. https://github.com/0xchamin/mcptube
**Assessment:** Ez egyszerre MCP-szerű tool surface (H3/H42) és ops-érték: a csapat „agent oktatóanyaga” verziózható artefakt lesz. Navibase-nél gyors belső leverage: saját runbookok, demo videók, kliens onboarding videók tudásbázissá konvertálása.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=2 | IntFric=2 | **Total: 14/25**
*Új hypothesis (2026-04-14). A videó-tudásbázis a következő „unstructured data” wedge, és a workflow (scene + multimodal) már oss eszközzel megjelent.*

## H58 — Local-First Agent Compute Kits (Vendor-Supported On-Device Agents)
**Thesis:** A privacy, latency és költség miatt egyre több agent workflow tolódik **local-first / on-device** futtatásra. Ahogy a hardvergyártók explicit „local agent” toolkit-et adnak, az edge agent futtatás mainstream lesz, és új governance mintákat kér (policy, audit, model frissítés, data boundary) a lokális környezetben is.
**Signals (updated 2026-04-14):**
- AMD Gaia docs: “Build AI Agents That Run Locally” (2026-04-13). https://amd-gaia.ai/docs
**Assessment:** Navibase/KKV kontextusban ez a „nem adom ki az adatot” buyer objection ellenszere. A kockázat: lokális sprawl és kontrollvesztés. A lehetőség: local agent deployment wrapper + evidence export ugyanúgy, mint cloudban.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=3 | **Total: 16/25**
*Új hypothesis (2026-04-14). A vendor-szintű toolkit jelzi, hogy a local-first agent futtatás nem hobby, hanem termékesedő irány.*

## Top 3 Opportunities + Suggested Experiments (2026-04-14)

### #1: H53/H37/H40 — Secretless-by-default + credential delegation (Trust boundary wedge)
**Miért most:** A „odaadhatom-e a kulcsaimat?” téma újra és újra feljön (Ask HN), miközben a credential delegation (Cred) és workload-attestation (H40) implementálható mintává konszolidálódik.
**Kísérlet:** 1 hetes „Delegated Credential Demo”: JIT token issuance + scope + expiry + audit correlation. Deliverable: 1 oldalas evidence export + rövid video demo.

### #2: H57 — Video-to-Wiki knowledge base (agent training leverage)
**Miért most:** A mcptube-vision workflow konkrét, kipróbálható: scene-aware multimodal ingest + wiki pages. A csapatoknak ez azonnal időnyereség.
**Kísérlet:** 1 nap: ingest 10 releváns agent/MCP/security YouTube videót, és mérni a keresési időt (FTS query → 1 perc alatt „idézet + summary”). 2. nap: MCP serverből agent query demo.

### #3: H58 — Local-first agents (privacy-first SMB packaging)
**Miért most:** Vendor-szintű „run locally” docs jelzi a wave-et. A buyer objection (adat) itt oldható fel leggyorsabban.
**Kísérlet:** 3 napos POC: 1 tipikus SMB workflow local futtatása (pl. e-mail draft + docs summary) úgy, hogy semmi ne menjen ki a gépről. Mérők: minőség, latency, üzemeltetési friction, update story.


## H36 — Managed Infrastructure for Autonomous Agents (Agent Hosting as a Service)
**Thesis:** Az autonóm agentek a pilot fázisból az éles üzem felé mennek, de a legtöbb csapat nem akar saját runtime-ot, sandboxot, skálázást, update-et és incident response-t építeni. Kell egy managed „agent hosting” réteg, ami elrejti az infrastruktúrát (runtime, izoláció, secrets, policy hooks, observability), és standard felületen adja a futtatást. A buyer itt nem csak enterprise security, hanem termékcsapat, aki gyorsan akar agentet élesíteni.
**Signals (updated 2026-04-10):**
- Anthropic launches managed infrastructure for autonomous AI agents (the-decoder.com, 2026-04-09) — explicit managed agent infra kategória, mainstream bejelentés. HIGH CONFIDENCE.
- Process Manager for Autonomous AI Agents (botctl.dev, 2026-04-09) — operációs réteg termékesedése, „agent process management” új kategória. MEDIUM CONFIDENCE.
**Assessment:** A managed hosting réteg a H2/H6/H13/H20 blokkal kompatibilis, de más entry point: „ne építsd meg, vedd meg”. Navibase irány: partner/adapter stratégia (compliance + reliability layer ráültetése managed runtime fölé), nem feltétlen infrastruktúra verseny.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=4 | **Total: 19/25**
*Új hypothesis (2026-04-10). A managed agent infra bejelentés azt jelzi, hogy a runtime réteg commoditizálódik, a differenciáló a governance/reliability és a vertical packaging lesz.*

## H37 — OAuth Credential Delegation for Agents (JIT tokens + least privilege)
**Thesis:** Az agentek tipikusan túl széles jogokat kapnak (API kulcsok, long-lived tokens), ami compliance és security kockázat. Kell egy credential delegation réteg: OAuth-alapú, just-in-time, scope-olt, rövid élettartamú tokenek agent run-okhoz, auditálható delegation chain-nel. Ez a H1 (identity/auth) gyakorlati implementációs wedge-je.
**Signals (updated 2026-04-10):**
- Cred (Product Hunt, 2026-04-09): „OAuth credential delegation for AI agents” — explicit termék validáció. HIGH CONFIDENCE.
**Assessment:** Erős, nagyon konkrét buyer pain: security team nem engedi a „random API keyt” agentnek. Wedge: drop-in SDK/gateway a token delegationhez, plusz audit export. Navibase: ezt integrációs best practice-ként és compliance komponensként lehet csomagolni (nem biztos, hogy saját termék).
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-10). A Cred jelzi, hogy a piac már megoldást keres. A „least privilege for agents” gyorsan table stakes lesz.*

## H38 — Agent Decision Evidence Packaging (Audit-ready, proof-first outputs)
**Thesis:** Az agent output akkor lesz vállalati szinten bevezethető, ha a döntésekhez automatikusan „evidence pack” készül: miért ezt javasolta, milyen inputokra hivatkozott, milyen policy-knek felelt meg, és milyen risk check-ek futottak. A naplózás (H2) nem elég, a döntésnek *azonnal* audit-ready bizonyítékká kell alakulnia (exportálható, prezentálható, visszakereshető). Ez különösen kritikus high-risk és pénzügyi/HR/ügyfél-kommunikációs use case-eknél.
**Signals (updated 2026-04-10):**
- Cyris (Product Hunt, 2026-04-08): „Turns every AI decision into audit-ready evidence” — explicit kategória és value proposition. HIGH CONFIDENCE.
**Assessment:** A proof-first output réteg összeköti a H2 (audit log), H6 (policy), H12 (accountability) és H20 (regulated infra) témákat egy könnyen eladható deliverable-be. Navibase: „evidence-by-default” riportok, CEO és compliance számára azonnali fogyasztásra.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=3 | IntFric=2 | **Total: 20/25**
*Új hypothesis (2026-04-10). A Cyris jel a piac felől, hogy a buyer nem raw logot akar, hanem kész bizonyítékot. Ez gyors revenue wedge lehet compliance audit szolgáltatásként is.*

## H39 — Agent Ops Monitoring for Non-Technical Teams (Process control + live intervention)
**Thesis:** Ahogy az agentek „dolgoznak” (TUI, remote desktop, browser automations), a napi fájdalom a nem-tech csapatoknál az, hogy nem látják, mi történik, és nem tudnak közbelépni biztonságosan. Kell egy könnyen használható ops layer: élő státusz, transcript, jóváhagyási pontok, rollback/undo, és „what changed” összefoglaló. Ez a H34 általánosítása: nem csak messaging-native, hanem role-based, non-technical kontroll.
**Signals (updated 2026-04-10):**
- Astropad Workbench (TechCrunch, 2026-04-08): remote desktop for AI agents — explicit agent-ops UX kategória. HIGH CONFIDENCE.
- TUI-use (GitHub, 2026-04-08): agentek TUI programokat vezérelnek — transcript + permission + intervention szükség. HIGH CONFIDENCE.
**Assessment:** A buyer itt ops lead és a team lead, nem csak security. Navibase: Telegram-first kontroll jó wedge, de bővíthető web dashboard irányba, ha a kontrolligény nő.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-10). A „agent-ops UX” külön kategóriává válik, és gyorsan terjed a devtool világon túl.*


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

## H34 — Agent Ops Monitoring & Human-in-the-Loop Control Plane (Messaging-native)
**Thesis:** Ahogy az agentek a végrehajtás felé mennek (TUI-k, remote desktop, messaging), a napi operációs fájdalom nem az, hogy “mit tud az agent”, hanem hogy **hogyan látod és irányítod futás közben**. Kell egy agent-native “ops console”, ami messagingből elérhető: run státusz, élő napló, jóváhagyási gombok, visszagörgethető audit, és gyors beavatkozás (pause/rollback). A meglévő IT remote desktop tooling rossz erre, mert nem agent művelet-szintű.
**Signals (updated 2026-04-09):**
- Astropad Workbench (TechCrunch, 2026-04-08): “remote desktop for AI agents” explicit pozicionálás, agent-ops monitoring kategória megjelenése. HIGH CONFIDENCE.
- Poke (TechCrunch, 2026-04-08): agents as easy as sending a text, messaging-native UX elterjedése, ami ops kontrollt igényel. HIGH CONFIDENCE.
- TUI-use (GitHub, 2026-04-08): agentek TUI programokat vezérelnek, amihez transcript + permission + live intervention kell. HIGH CONFIDENCE.
**Assessment:** Ez a H2/H6/H19 gyakorlati “surface area” kiegészítője, a buyer itt ops lead és IT. Navibase/Leoni irány: Telegram-first approval + run dashboard + audit export, “one glance ops” a CEO-nak.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-09). A Workbench + messaging-native agent UX együtt jelzi: agentek üzemeltetése új UI kategória, nem csak backend governance.*

---

## H35 — Agent End-User Distribution via Text, with Identity & Confirmation (Consumer-to-Enterprise Bridge)
**Thesis:** Az agentek elosztása (distribution) átrendeződik: a “külön app” helyett **SMS/WhatsApp/Telegram** jellegű csatornákon jelennek meg az agentek. Ez megnyitja a tömeges használatot, de azonnal felhozza az identity, consent, és action-confirmation problémát. A piacon hiányzik egy “messaging agent gateway”, ami vállalati szintű identity + scope + confirmation flow-val engedi a text-based agent használatot.
**Signals (updated 2026-04-09):**
- Poke (TechCrunch, 2026-04-08): agents via text, mainstream distribution shift. HIGH CONFIDENCE.
- Copilot terms “for entertainment purposes only” (TechCrunch, 2026-04-05): jogi disclaimerek erősödnek, text-based agentnél kötelező lesz a megerősítés és a felelősségi keret. HIGH CONFIDENCE.
**Assessment:** Erős wedge lehet SMB-nél: “agent a chatben”, de enterprise-ready guardrail-lel. Navibase kapcsolódás: Telegram-first ops, de identity+authorization és confirmation flow produktizálása.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=3 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-04-09). A distribution ugrás gyors, de a monetizációs buyer és compliance boundary még alakul.*

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


---

## H20 — Agent Orchestration Platform as Regulated Infrastructure
**Thesis:** Az AI agentek governance infrastrukturává válnak — a szabályozói figyelem (EU AI Act, NIST) hamarosan nemcsak az egyes AI döntéseket, hanem az agent orchestration platformokat közvetlenül érinti. Ma egyetlen platform sem pozicionálja magát compliance-ready regulated infrastructure-ként. Az "agent nem eszköz, hanem infrastruktúra" narratíva mainstream médiában jelent meg. Aki elsőként pozicionálja a platformját erre a keretre, az standarddá válhat — különösen a KKV szegmensben, ahol a compliance követelmény hamarabb válik belépési feltétellé, mint megkülönböztető előnnyé.
**Signals (updated 2026-04-01):**
- "AI Agents Become Governance Infrastructure" (National Today, 2026-03-29): Az "agent nem eszköz, hanem infrastruktúra" narratíva mainstream médiában jelent meg — az EU AI Act és NIST szabályozás következő célpontja az agent orchestration platform réteg. HIGH CONFIDENCE.
- NIST CAISI "AI Agent Standards Initiative" (2026-02, deadline April 2, 2026): Az agent authentication és authorization concept paper deadline elérte a határidőt — a szabályozás már platform szintre érkezett. HIGH CONFIDENCE.
- EU AI Act Aug 2026 compliance deadline: 4 hónap — a platform szintű compliance-ready pozicionálásra nyitott ablak zárul. HIGH CONFIDENCE.
- $65M seed enterprise agent startup (TechCrunch, 2026-03-30): A VC pénz enterprise szegmensbe áramlik, KKV-fókuszú compliance-ready platform differenciálhat. MEDIUM CONFIDENCE.
- iProov "accountability vacuum" (2026-03-26): A platformszintű felelősség kérdése nyitott — az orchestration layer az első hely, ahol ez kezelhető. HIGH CONFIDENCE.
**Assessment:** Ez nem egy termék feature — ez pozicionálási és go-to-market döntés. A Navibase/Leoni ma már implementálja az audit trail, policy engine, identity scope komponenseket. A kérdés: mikor kommunikálják ezt együtt, mint "compliance-ready platform infrastruktúra"? Az EU AI Act deadline közeledtével ez az üzenet hónapok múlva lesz a legértékesebb — nem évek múlva. Navibase alkalmazás: "Agent Platform Compliance Badge" — egységes EU AI Act readiness kommunikáció, amely H1 + H2 + H6 + H12 signalokat összefogja.
**Scores:** Pain=4 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 21/25**
*Új hypothesis (2026-04-01). A governance infrastruktúra narratíva mainstream megjelenése közvetlen go-to-market trigger. Az urgency 5 mert az EU AI Act deadline 4 hónapon belül van — a compliance positioning window most nyitva van, de zárul.*

---

## H21 — Deterministic Agent Behavior as SMB/Enterprise Trust Signal
**Thesis:** Az önmódosító és önfejlesztő agentek (Phantom, intelligence explosion narratíva) megjelenésével az enterprise és KKV piac kettéválik: "instabil/kísérletező" és "stabil/auditálható" platformok. Az üzleti adopció gátja nem az AI képesség hiánya, hanem a kiszámíthatatlanságtól való félelem. Aki a "determinisztikus, auditálható, stabil agent viselkedés" értékajánlatát a legegyértelműbben kommunikálja, az nyeri el a konzervatívabb — de fizető — enterprise és KKV ügyfelet. A Navibase/Leoni architektúra ezt már implementálja (SOUL.md + AGENTS.md + policy engine), a piac azonban nem tud róla.
**Signals (updated 2026-04-01):**
- "Agentic AI and the next intelligence explosion" (arxiv, 2026-03-30): A self-evolving agent narratíva erősödik — a counternarrative (stabil/auditálható behavior) lesz az enterprise differenciáló. HIGH CONFIDENCE.
- Phantom open-source agent (GitHub ghostwright/phantom, 2026-03-30): Első nyilvános open-source önmódosító agent — megjelent a félelem, és megjelent az igény a kontrollált alternatívára. HIGH CONFIDENCE.
- ALTK paper (arxiv, 2026-03-16): "silent reasoning errors, tool argument corruption" — a kiszámíthatatlanság termelési kockázat, auditable behavior az ellenlábasa. HIGH CONFIDENCE.
- CRAFT paper (arxiv, 2026-03-26): Erősebb modell nem jelent jobb multi-agent koordinációt — a stabilitás protokoll és architektúra kérdése. HIGH CONFIDENCE.
- "Autonomous AI agents in business organizations" (Jerusalem Post, 2026-03-27): KKV döntéshozók is olvassák az autonóm agent témát — a bizalom és a kiszámíthatóság kérdése mainstream. MEDIUM CONFIDENCE.
**Assessment:** Ez elsősorban kommunikációs és pozicionálási lehetőség — a build work már megtörtént. Az IntFric szándékosan alacsony: a Navibase már implementálja a deterministic scope-ot (SOUL.md, AGENTS.md, policy engine, explicit scope boundaries). A piac most kezdi megérteni, miért számít ez. Az "intelligence explosion" narratívára adott válasz a Navibase pitch centereleme lehet: "míg mások az agent képességét mérik, mi az agent megbízhatóságát garantáljuk." Navibase alkalmazás: "Stable Agent Architecture" white paper + KKV pilot pitch deck.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=4 | IntFric=2 | **Total: 18/25**
*Új hypothesis (2026-04-01). A Phantom + intelligence explosion signalok egyszerre nyitják meg a "counternarrative" lehetőséget. A Navibase architektúra az egyetlen eddig látott implementáció, amelynél a scope-hardening production-szinten dokumentált.*

---

## Ranking Summary (2026-04-01)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 — Agent Identity & Auth | 21/25 | = |
| 4 | **H20 — Agent Platform as Regulated Infrastructure** | **21/25** | **ÚJ** |
| 5 | H3 — MCP Governance | 20/25 | = |
| 6 | H12 — Agent Accountability Framework | 20/25 | = |
| 7 | H10 — Agent Infra as Code | 19/25 | = |
| 8 | H15 — B2B SaaS Agent Feature Injection | 19/25 | = |
| 9 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 10 | H8 — Cross-Agent Context | 18/25 | = |
| 11 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 12 | H14 — Agent-to-Agent Trust & M2M | 18/25 | = |
| 13 | H16 — AI Alignment Measurement as a Service | 18/25 | = |
| 14 | H17 — Controlled Self-Configuration Boundary | 18/25 | = |
| 15 | H18 — Organizationally-Aligned AI | 18/25 | = |
| 16 | H19 — Operational Reliability Layer | 18/25 | = |
| 17 | **H21 — Deterministic Agent Behavior as Trust Signal** | **18/25** | **ÚJ** |
| 18 | H4 — Agent Payment Rails | 17/25 | = |
| 19 | H11 — Hallucination Self-Check | 17/25 | = |
| 20 | H5 — Discovery & Registry | 16/25 | = |
| 21 | H9 — Agent Communication Infra | 12/25 | = |

*2026-04-01 delta: 2 új hypothesis (H20, H21). H20 azonnal a top 4-be kerül 21/25-tel — az "agent platform mint regulated infrastructure" narratíva mainstream megjelenése közvetlen go-to-market trigger. H21 a 18/25 blokkba kerül, de IntFric=2 miatt Navibase-nél a legkisebb build investmenttel megvalósítható új lehetőség.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-01)

### #1: H20 — Agent Platform as Regulated Infrastructure [Score: 21/25 — ÚJ]
**Miért most:** Az "AI agents become governance infrastructure" narratíva (National Today, 2026-03-29) mainstream megjelenése és az EU AI Act Aug 2026 deadline együtt kinyit egy 4 hónapos compliance positioning ablakot. A Navibase ma már implementálja az ehhez szükséges komponenseket (H1+H2+H6+H12). A go-to-market lépés: ezeket egységes "Agent Platform Compliance" narratívába összefogni, mielőtt a $65M-es enterprise szereplők megelőzik a piacot.
**Javasolt kísérlet:** "EU AI Act Agent Compliance Checklist" — 1 oldalas, szabad letöltésű sablon, amely a Navibase komponenseit (audit trail, policy engine, identity, accountability) EU AI Act cikkelyekhez rendeli. Mérők: letöltések, inbound megkeresések, LinkedIn impressions 2 héten belül. Ha 300+ letöltés: fizetős compliance assessment pilot indítás.
**Befektetés:** ~2 nap. Erős thought leadership pozicionálás, közvetlen EU AI Act deadline-ra időzített lead gen.

### #2: H2 / H6 (tied) — Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** Változatlanul a lista legmagasabb score-ú lehetőségei. EU AI Act Aug 2026 deadline 4 hónap. McKinsey hack + Meta rogue agent + iProov accountability vacuum egymást erősítő signalok. A compliance + security kettős pitch ma a legerősebb belépési szög — a H20-val kombinálva platform-szintű narratíva.
**Javasolt kísérlet:** 10 EU-based Claude/GPT production-user enterprise hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit. Mérők: pilot-paid konverzió, árszenzitvitás, compliance framework hivatkozás.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai proof-of-concept a pitchben.

### #3: H21 — Deterministic Agent Behavior as SMB/Enterprise Trust Signal [Score: 18/25 — ÚJ]
**Miért most:** A Phantom önmódosító agent (2026-03-30) megjelenése és az "intelligence explosion" narratíva KKV és mainstream sajtóban (Jerusalem Post) egyaránt megjelent. A félelem és a bizalomigény most formálódik. A Navibase build cost nulla — az architektúra létezik. A cost: a kommunikáció megírása. Ez a legmagasabb ROI lehetőség a listán belső erőforrás szempontjából.
**Javasolt kísérlet:** "Stable Agent Architecture" egy oldalas white paper — Navibase/Leoni scope-hardening architektúra bemutatása, összehasonlítás a Phantom-típusú "wild" megközelítéssel. Mérők: elkezdodott.hu blog traffic, LinkedIn engagement, inbound kérdések a "hogyan kontrolláljuk az agent viselkedését" témában. Ha 5 inbound megkeresés: ez a pitch fő differenciálója.
**Befektetés:** ~1 nap tartalom. Azonnali differenciáló kommunikáció. A Leoni belső implementáció maga a proof-of-concept.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-01.md (223 signal, HAIER export) | 2026-04-01 09:30 CET*


---

## H22 — Adversarial Robustness Layer (Production Agent Attack Surface)
**Thesis:** DeepMind 6 dokumentált "csapda" (prompt injection, kontextus manipuláció, tool poisoning stb.) és az Anthropic kódbázis szivárgás egyszerre jelzik: a produkciós agentek ellen már aktív, szervezett támadások futnak. Az eddigi biztonsági fókusz passzív volt (naplózás, audit, izoláció) — nincs olyan réteg, amely aktívan detektálja és blokkolja az adversarial bemeneteket valós időben, KKV-ba is bevezethető formában. A "6 csapda" paper az első széles körben hivatkozott taxonómia, amely konkrét, mérhető attack pattern-eket nevesít. Erre lehet védelmi terméket építeni.
**Signals (updated 2026-04-02):**
- Google DeepMind: "6 csapda autonóm agenteknek" (the-decoder.com, 2026-04-01): prompt injection, kontextus manipuláció, tool poisoning, identity spoofing stb. — első publikus, hivatkozott taxonómia produkciós agent attack pattern-ekre. HIGH CONFIDENCE.
- Anthropic Claude kódbázis szivárgás (WSJ, 2026-04-01): az agent-infrastruktúra IP-je aktív célpont — a támadási motiváció bizonyított. HIGH CONFIDENCE.
- Mutation Testing for the Agentic Era (Trail of Bits, 2026-04-01): a hagyományos szoftvertesztelés nem alkalmas agent robustness mérésére — új mérési keretrendszer szükséges. HIGH CONFIDENCE.
- Autonomous pentest agent (vxcontrol/pentagi): teljesen autonóm támadóeszközök elérhetők — a védelem reaktívból proaktívvá kell váljon. HIGH CONFIDENCE.
- Open-source red-team playground (HN, 2026-03-15): "We kept finding the same types of vulnerabilities" — a 6 DeepMind attack type nem elméleti, production-ban dokumentált. HIGH CONFIDENCE.
**Assessment:** A DeepMind taxonómia kinyitja a "robustness layer" termékpozíciót: nem generic biztonsági eszköz, hanem kimondottan az ismert agent-specifikus attack pattern-ekre tervezett valós idejű shield. A KKV pitch: "a legjobb agented is becsapható 6 ismert módszerrel — mi blokkoljuk mind a hatot." A Trail of Bits mutation testing paper az auditálási metrikát adja hozzá. Navibase alkalmazás: Leoni bemeneti validáció + kontextus-integritás ellenőrzés a 6 DeepMind pattern alapján.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Új hypothesis (2026-04-02). DeepMind taxonómia + Anthropic szivárgás egymást erősítő, magas bizalmú signalok. A score 22/25 — azonnal a lista csúcsára kerül H2 és H6 mellé. Az adversarial attack téma a 2026 Q2 leggyorsabban növekvő agent security szegmense.*

---

## H23 — Agentic QA & Mutation Testing as a Service
**Thesis:** A hagyományos szoftvertesztelési módszerek (unit test, integration test) nem alkalmasak autonóm agent viselkedés ellenőrzésére. Trail of Bits paper (2026-04-01) megmutatja: mutation testing szükséges — az agent döntési logikájának szándékos mutálásával mérhető, hogy mennyire robusztus és kiszámítható a viselkedés. Ez ma nincs termékkénnt elérhetően — sem önállóan, sem CI/CD pipeline-ba integrálva. Az "agentic QA" kategória még nem létezik, de az igény (audit, compliance, production reliability) már megvan.
**Signals (updated 2026-04-02):**
- Mutation Testing for the Agentic Era (Trail of Bits blog, 2026-04-01): hagyományos tesztelés elégtelen, mutation testing szükséges agent robustness méréshez — közvetlen kategória-definíciós paper egy high-credibility biztonsági cégtől. HIGH CONFIDENCE.
- ALTK paper (arxiv, 2026-03-16): "silent reasoning errors go undetected" — a QA gap production-ban dokumentált. HIGH CONFIDENCE.
- AWS DevOps/Security agentek deployment (Forbes, 2026-04-01): enterprise szinten megjelenik az agent-alapú DevOps — a CI/CD pipeline-ba integrált agentic QA természetes következő lépés. MEDIUM CONFIDENCE.
- Claude Code (GitHub trending, 2026-04-02): a coding agent tooling mainstream — minden coding agent deploymentnél felvetődik a "hogyan tesztelünk" kérdés. MEDIUM CONFIDENCE.
- ChatDev 2.0 (GitHub trending, 2026-04-01): multi-agent szoftverfejlesztés terjedése — az agentic QA igénye skálázódik. MEDIUM CONFIDENCE.
**Assessment:** Ez a H2 (audit trail) és H17 (controlled self-configuration) metszéspontja, de specifikusan a szoftverfejlesztési és CI/CD pipeline-ra fókuszál. A Trail of Bits mint high-credibility forrás maga validálja a kategoriat — ami nem mainstream biztonsági fórumon jelent meg, az tudományos/ipari referencia szinten érkezik. Navibase alkalmazás: Leoni agent deployment pipeline-jában agentic mutation test checkpoint — minden konfiguráció változás előtt automatikus robustness check.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-02). Trail of Bits paper közvetlen kategória-definíció. Az "agentic QA" tér ma üres — az első szereplőnek thought leadership és tooling előnye van. 2026 Q3-ra várható a CI/CD integrációs igény felfutása.*

---

## Ranking Summary (2026-04-02)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | **H22 — Adversarial Robustness Layer** | **22/25** | **ÚJ** |
| 4 | H1 — Agent Identity & Auth | 21/25 | = |
| 5 | H20 — Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H3 — MCP Governance | 20/25 | = |
| 7 | H12 — Agent Accountability Framework | 20/25 | = |
| 8 | H10 — Agent Infra as Code | 19/25 | = |
| 9 | H15 — B2B SaaS Agent Feature Injection | 19/25 | = |
| 10 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 11 | H8 — Cross-Agent Context | 18/25 | = |
| 12 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 13 | H14 — Agent-to-Agent Trust & M2M | 18/25 | = |
| 14 | H16 — AI Alignment Measurement as a Service | 18/25 | = |
| 15 | H17 — Controlled Self-Configuration Boundary | 18/25 | = |
| 16 | H18 — Organizationally-Aligned AI | 18/25 | = |
| 17 | H19 — Operational Reliability Layer | 18/25 | = |
| 18 | H21 — Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 19 | **H23 — Agentic QA & Mutation Testing as a Service** | **18/25** | **ÚJ** |
| 20 | H4 — Agent Payment Rails | 17/25 | = |
| 21 | H11 — Hallucination Self-Check | 17/25 | = |
| 22 | H5 — Discovery & Registry | 16/25 | = |
| 23 | H9 — Agent Communication Infra | 12/25 | = |

*2026-04-02 delta: 2 új hypothesis (H22, H23). H22 azonnal a top 3-ba kerül 22/25-tel — a DeepMind 6 trap taxonómia + Anthropic szivárgás együttesen az adversarial robustness témát az audit/policy mellé emeli. H23 a 18/25 blokkba kerül mint üres kategória-definíció. Az EU AI Act Aug 2026 deadline közeledtével a teljes governance/security blokk (H1/H2/H6/H12/H20/H22) egyre szorosabb.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-02)

### #1: H22 — Adversarial Robustness Layer [Score: 22/25 — ÚJ]
**Miért most:** A DeepMind 6 csapda paper az első széles körben hivatkozott, konkrét attack taxonómia produkciós agentekre. Az Anthropic kódszivárgás igazolja: az agent infrastruktúra aktív célpont. Ez nem jövőbeli kockázat — ez ma már aktív fenyegetés. A piac még nem rendelkezik termékkel, amely kifejezetten ezt a 6 attack pattern-t blokkolja KKV-ba is bevezethető formában. Az ablak szűk: a következő 2-3 hónapban security-fókuszú startupok fognak erre belépni.
**Javasolt kísérlet:** Leoni-ban a bemeneti pipeline elé egy "adversarial check" réteg prototípusa: a 6 DeepMind attack típust ellenőrző validációs logika (prompt injection detektor, kontextus-integritás check, tool call anomaly). Mérők: false positive arány (helyes bemenetet blokkol), true positive arány (valódi attack-ot megfog), latency overhead. 2 hetes prototípus. Ha működik: "Leoni Security Shield" KKV pitch elem.
**Befektetés:** ~1 hét build. DeepMind paper maga a spec — szabad felhasználású, magas hitelességű forrás.

### #2: H2 / H6 (tied) — Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** Változatlanul a lista legmagasabb score-ú lehetőségei. EU AI Act Aug 2026 deadline most már 4 hónap. Az új H22 signal (DeepMind + Anthropic) tovább erősíti a biztonsági narratívát — a compliance + security + adversarial robustness hármas pitch az erősebb belépési szög mint korábban. H20-val kombinálva platform-szintű narratíva.
**Javasolt kísérlet:** 10 EU-based Claude/GPT production-user enterprise hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit + adversarial exposure scan (6 DeepMind pattern-re). Mérők: pilot-paid konverzió, compliance framework hivatkozás, security-driven vs. compliance-driven inbound arány.
**Befektetés:** ~2 hét fejlesztés. A H22 prototípus + meglévő ALTK proof-of-concept együtt erős demo.

### #3: H20 — Agent Platform as Regulated Infrastructure [Score: 21/25]
**Miért most:** Az EU AI Act Aug 2026 deadline most 4 hónap — a compliance positioning window gyorsan zárul. A DeepMind/Anthropic adversarial signalok (H22) tovább erősítik a "platform-szintű compliance" narratívát: nem elég az audit log, a platform maga legyen hardened és deklaráltan compliance-ready. A Navibase ma implementálja az összes szükséges komponenst — a kommunikáció hiányzik.
**Javasolt kísérlet:** "EU AI Act Agent Compliance Checklist" 1 oldalas sablon — Navibase komponensek (H1+H2+H6+H12+H22) EU AI Act cikkelyekhez rendelve + DeepMind 6 attack pattern-re vonatkozó védelmi intézkedések listája. Mérők: letöltések, inbound megkeresések, LinkedIn impressions 2 héten belül. Ha 300+ letöltés: fizetős compliance assessment pilot.
**Befektetés:** ~2 nap. A H22 friss paper thought leadership momentum-mal tölti meg a checklist-et.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-02.md (232 signal, HAIER export) | 2026-04-02 09:30 CET*


---

## H24 — Shadow AI / Unmanaged Agent Governance Plane
**Thesis:** Ahogy a nagy szervezetekben megjelennek az első, „munkát végző” autonóm agentek (DevOps, SecOps, support, procurement), megjelenik a következő probléma: a nem jóváhagyott, csapatok által „sunny side” módon bevezetett agentek (shadow AI) gyorsabban szaporodnak, mint ahogy a central governance reagálni tudna. Kell egy dedikált governance plane, ami felderíti, inventory-zza és folyamatosan kontrollálja a nem menedzselt agenteket (policy, audit, kill switch, ownership, escalation). Ez nem MCP governance (H3) és nem csak audit trail (H2), hanem kifejezetten a shadow AI „operatív” problémájára épített termékkategória.
**Signals (updated 2026-04-03):**
- KiloClaw: shadow AI + autonomous agent governance (AI News, 2026-04-02) - explicit kategória-nevesítés ("shadow AI") + termékpozíció. HIGH CONFIDENCE.
- AWS: AI agentek DevOps és Security csapatok munkájára (Forbes, 2026-04-01) - a „working agents” enterprise-be kerülnek, ezzel a shadow deployment valószínűsége nő. HIGH CONFIDENCE (vendor signal).
- EU AI Act Aug 2026 (korábbi) - ha az agent döntést hoz vagy adatot mozgat, a governance hiánya audit/compliance kockázat. HIGH CONFIDENCE (regulatory).
**Assessment:** A "shadow AI" az a wedge, ami a governance piacot az IT/security buyerhez köti: inventory + risk scoring + containment. Moat lehetőség: agent-felderítés (network + API + identity graph), folyamatos policy enforcement, és audit-ready jelentések.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=3 | IntFric=3 | **Total: 21/25**
*Új hypothesis (2026-04-03). A KiloClaw explicit shadow AI pozicionálása erős validáció, az AWS vendor signal pedig azt jelzi: ez nem kutatás, hanem deploy.*

---

## H25 — Developer Multi-Agent Workspace Orchestration (Worktrees, Sessions, Review)
**Thesis:** A terminal-native coding agentek (Claude Code, stb.) és a multi-agent dev flow-k gyorsan terjednek, de a fejlesztők operatív fájdalma nem a modell-képesség, hanem a "túl sok agent, túl sok worktree" kezelése: state, státusz, párhuzamos futások, review, és a hibák visszakövetése. A piacnak szüksége van egy "agent workspace orchestrator" rétegre: agent/session dashboard, worktree lifecycle, run log + diff review, policies (mit csinálhat egy agent), és költség/limit menedzsment.
**Signals (updated 2026-04-03):**
- Anthropic Claude Code (GitHub, 2026-04-02) - első-party, terminal-native agent eszköz -> tömeges elterjedés. HIGH CONFIDENCE.
- Show HN: Baton - desktop app multi-agent worktree managementhez (2026-04-01) - közvetlen practitioner pain: "messy" agent/worktree kezelés. HIGH CONFIDENCE.
- ChatDev 2.0 (GitHub, 2026-04-01) - multi-agent collaboration mainstream open-source mintázat. MEDIUM CONFIDENCE.
**Assessment:** Ez devtool kategória, gyors adoption, de moatozás nehezebb. A value: "agent fleet control plane" a fejlesztő gépen, enterprise security hookkal (policy, audit).
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=2 | **Total: 16/25**
*Új hypothesis (2026-04-03). Baton és Claude Code együtt jelzi: a multi-agent dev már operációs probléma, nem novelty.*

---

## H26 — Vertical Agent Copilots in Legacy Plugin Ecosystems (WordPress wedge)
**Thesis:** A legacy, plugin-alapú ökoszisztémákban (WordPress) az "agentic" réteg egy gyors terjesztési wedge: a felhasználói bázis hatalmas, a workflow-k jól definiáltak, és a value azonnali. A kulcs: agent actions auditálása + permissioning + rollback, mert a CMS-ekben az agent hibája közvetlen üzleti kár. A platform blindspot itt a "secure action wrapper" a legacy app körül.
**Signals (updated 2026-04-03):**
- WP Copilot (Product Hunt, 2026-04-02) - agentic copilot kifejezetten WordPress-hez. HIGH CONFIDENCE.
- (Korábbi) WordPress.com AI agents (TechCrunch, 2026-03-20) - mainstream platformok belépnek a WP agentic irányba. MEDIUM CONFIDENCE.
**Assessment:** Nem általános agent platform, hanem distribution play. Navibase szempont: gyors KKV entry point, de a hard part a biztonságos, auditálható változtatáskezelés.
**Scores:** Pain=3 | Urgency=3 | WTP=4 | Def=2 | IntFric=2 | **Total: 14/25**
*Új hypothesis (2026-04-03). A WP Copilot egyértelmű validáció: a legnagyobb plugin ökoszisztémák agent-esednek.*

---

## Ranking Summary (2026-04-03)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 — Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 — Agent Identity & Auth | 21/25 | = |
| 5 | H20 — Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | **H24 — Shadow AI Governance Plane** | **21/25** | **ÚJ** |
| 7 | H3 — MCP Governance | 20/25 | = |
| 8 | H12 — Agent Accountability Framework | 20/25 | = |
| 9 | H10 — Agent Infra as Code | 19/25 | = |
| 10 | H15 — B2B SaaS Agent Feature Injection | 19/25 | = |
| 11 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 12 | H8 — Cross-Agent Context | 18/25 | = |
| 13 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 14 | H14 — Agent-to-Agent Trust & M2M | 18/25 | = |
| 15 | H16 — AI Alignment Measurement as a Service | 18/25 | = |
| 16 | H17 — Controlled Self-Configuration Boundary | 18/25 | = |
| 17 | H18 — Organizationally-Aligned AI | 18/25 | = |
| 18 | H19 — Operational Reliability Layer | 18/25 | = |
| 19 | H21 — Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 20 | H23 — Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 21 | H4 — Agent Payment Rails | 17/25 | = |
| 22 | H11 — Hallucination Self-Check | 17/25 | = |
| 23 | H5 — Discovery & Registry | 16/25 | = |
| 24 | **H25 — Developer Multi-Agent Workspace Orchestration** | **16/25** | **ÚJ** |
| 25 | H9 — Agent Communication Infra | 12/25 | = |
| 26 | **H26 — WordPress/Plugin Ecosystem Vertical Copilots** | **14/25** | **ÚJ** |

---

## Top 3 Opportunities + Suggested Experiments (2026-04-03)

### #1: H22 (tied with H2/H6) + H24 combo - Security governance for the real enterprise problem
**Miért most:** A DeepMind 6 trap + Anthropic leak (H22) mellett most megjelent a "shadow AI" explicit termékkategória (H24). A buyer itt tipikusan IT/security, és a fájdalom azonnali: felderítés + kockázat + containment.
**Javasolt kísérlet:** "Shadow Agent Exposure Scan" 10 EU enterprise-nek: 2 hetes audit, deliverable: (1) agent inventory, (2) top 10 policy gap, (3) 6 DeepMind attack exposure score, (4) quick fixes. Mérők: audit->pilot konverzió, budget range, leggyakoribb control request.
**Befektetés:** ~1 hét a scan automationra + 1 hét pilot futtatás. A kimenetből termék spec épül.

### #2: H2 / H6 - Audit Trail + Policy Enforcement Runtime
**Miért most:** EU AI Act Aug 2026. A compliance ablak zárul, és az agentek egyre több operatív folyamatba kerülnek (AWS vendor signal). Ez a legérettebb, legmagasabb WTP-vel rendelkező kategória.
**Javasolt kísérlet:** 30 napos "Agent Governance Baseline" pilot 3 design partnernél: audit trail + policy violations report + basic remediation. Mérők: (1) hány policy violation/hét, (2) remediation time, (3) pilot->paid.
**Befektetés:** ~2 hét build, az alap már létezik.

### #3: H20 - Agent Platform as Regulated Infrastructure (packaging/positioning)
**Miért most:** A compliance-ready platform narratíva most fog standarddá válni. A különbség nem implementáció, hanem hogy ki csomagolja és kommunikálja először.
**Javasolt kísérlet:** 1 oldalas "Agent Platform Compliance" oldal + checklist (EU AI Act mapping) + 10 célzott LinkedIn outreach. Mérők: letöltések, inbound meeting, 2 hetes pipeline.
**Befektetés:** 2 nap tartalom + 1 nap outreach.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-03.md (240 relevant, HAIER export) | 2026-04-03 09:30 CET*


---

## H27 — Agent Packaging & Portability Standard (Repo-as-Agent Spec)
**Thesis:** Ahogy az agent-ek eszköztár- és runtime-ökoszisztémája szétágazik (OpenAI/Anthropic tooling, MCP, GitOps runtimes, IDE agentek), a legnagyobb friction a *portabilitás*: ugyanazt az agentet új framework-be vinni ma szinte újraírás. Kell egy framework-agnosztikus, fájl-alapú “agent manifest/spec” (policy, tool-permission, runbook, audit hook, teszt checkpoint), ami bármely runtime-ba importálható. Aki ezt standardizálja, az “agent packaging layer” kategóriát birtokolhatja.
**Signals (updated 2026-04-04):**
- GitAgent (HN, 2026-03-14): „open standard that turns any Git repo into an AI agent” — explicit igény a repo-as-agent definícióra és interoperabilitásra. HIGH CONFIDENCE.
- Orloj (2026-03-26): YAML/GitOps policy-first agent infra — a spec-alapú agent lifecycle mintázat már megjelent. HIGH CONFIDENCE.
- Claude Code + több terminal agent (2026-04 eleje): agent definíciók és workflow-k „szétszóródnak” IDE/CLI között — portability pain nő. MEDIUM CONFIDENCE.
**Assessment:** Ez a H10 (Infra as Code) és H5 (Discovery) közé ékelődő, de külön kategória: nem csak policy deklarálás, hanem *agent csomagolás + import/export*. Navibase alkalmazás: egy „Navibase Agent Pack” formátum, ami a SOUL/AGENTS/policy + skill manifesteket standardizálja, és később külső partnereknek is átadható.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-04). A GitAgent explicit standard jelzés. A moat a specifikáció + referencia implementáció + template library kombinációja.*

---

## H28 — Bias/Fairness Governance for Agentic Decision Delegation
**Thesis:** A decision delegation (agent ajánl, rangsorol, döntéstámogat) gyorsan beleütközik a fairness/transparency/compliance falba: a szervezetnek bizonyítania kell, hogy a rendszer nem diszkriminál, és hogy a döntési logika auditálható. A mai governance eszközök főleg naplóznak (H2) és policy-t enforce-olnak (H6), de ritkán adnak *fairness/bias* metrikát és „explainability-ready” dokumentációt agent workflow szinten. Ez külön wedge lehet compliance buyer felé.
**Signals (updated 2026-04-04):**
- „Algorithmic bias, data ethics, and governance…” (Semantic Scholar, 2025-02-28) — fairness + governance + compliance fókusz ADM környezetben. HIGH CONFIDENCE.
- „Ethics of Using Data in Automated Decision-Making…” (Semantic Scholar, 2025-09-01) — transparency + institutional accountability mint mainstream research téma. HIGH CONFIDENCE.
- „Ethics and Fairness in Conversational AI…” (Semantic Scholar, 2025-11-01) — LLM-alapú conversational rendszerekben bias framework-ek formálódnak. MEDIUM CONFIDENCE.
- EU AI Act Aug 2026: high-risk AI decisions dokumentálása és megfelelősége kötelező (korábbi signal) — fairness dokumentáció várhatóan besorolási kérdéssé válik. HIGH CONFIDENCE.
**Assessment:** Ez nem újraírja a H2/H6-ot, hanem *ráépül*: audit trail + policy enforcement mellé „fairness evidence pack” kell. Navibase alkalmazás: „Decision Delegation Fairness Report” modul (agent run sample-set, drift check, bias checklist, audit-ready export), amit enterprise-nél compliance csapat tud használni, KKV-nél pedig bizalomépítő dokumentum.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-04). Research jellegű signalok, de compliance-ablakkal (EU AI Act) kombinálva gyorsan termék- és szolgáltatás-wedge lehet.*

---

## Ranking Summary (2026-04-04)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 — Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 — Agent Identity & Auth | 21/25 | = |
| 5 | H20 — Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H24 — Shadow AI Governance Plane | 21/25 | = |
| 7 | H3 — MCP Governance | 20/25 | = |
| 8 | H12 — Agent Accountability Framework | 20/25 | = |
| 9 | H10 — Agent Infra as Code | 19/25 | = |
| 10 | H15 — B2B SaaS Agent Feature Injection | 19/25 | = |
| 11 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 12 | H8 — Cross-Agent Context | 18/25 | = |
| 13 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 14 | H14 — Agent-to-Agent Trust & M2M | 18/25 | = |
| 15 | H16 — AI Alignment Measurement as a Service | 18/25 | = |
| 16 | H17 — Controlled Self-Configuration Boundary | 18/25 | = |
| 17 | H18 — Organizationally-Aligned AI | 18/25 | = |
| 18 | H19 — Operational Reliability Layer | 18/25 | = |
| 19 | H21 — Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 20 | H23 — Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 21 | **H28 — Bias/Fairness Governance** | **18/25** | **ÚJ** |
| 22 | H4 — Agent Payment Rails | 17/25 | = |
| 23 | H11 — Hallucination Self-Check | 17/25 | = |
| 24 | **H27 — Agent Packaging & Portability Spec** | **17/25** | **ÚJ** |
| 25 | H5 — Discovery & Registry | 16/25 | = |
| 26 | H25 — Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 27 | H26 — WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 28 | H9 — Agent Communication Infra | 12/25 | = |

*2026-04-04 delta: 2 új hypothesis (H27, H28). A security/governance blokk továbbra is domináns (H2/H6/H22/H24). H27 portability/spec irány, H28 fairness/bias compliance wedge.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-04)

### #1: H22 + H24 combo — Shadow Agent Exposure + Adversarial Robustness
**Miért most:** A „shadow AI” narratíva buyer-hez köt (IT/security), a DeepMind taxonómia pedig konkrét, értékes „scan spec”-et ad. Ez a leggyorsabb út fizetős pilothoz.
**Javasolt kísérlet:** „Shadow Agent Exposure Scan” 5 EU cégnek (2 hét): inventory + 6-trap exposure score + quick fixes, audit exporttal. Mérők: meeting->pilot, pilot->paid, leggyakoribb kontrolligény.

### #2: H20 — Agent Platform as Regulated Infrastructure (Packaging)
**Miért most:** EU AI Act Aug 2026 közel. A piac nem feature-t vesz, hanem „compliance-ready” narratívát és dokumentálhatóságot. A Navibase-nél a komponensek megvannak, a csomagolás a bottleneck.
**Javasolt kísérlet:** 1 oldalas „EU AI Act Agent Compliance Mapping” + letölthető checklist. Mérők: letöltés, inbound meeting, „melyik cikkely fáj legjobban” visszajelzés.

### #3: H28 — Bias/Fairness Governance wedge (Decision Delegation)
**Miért most:** A fairness/bias governance irodalom sűrűsödik, és compliance oldalon ez hamar „kérdezni fogják” tétel. Aki tud gyors, auditálható evidence pack-et adni, az nyer.
**Javasolt kísérlet:** „Decision Delegation Fairness Pack” pilot 1 design partnerrel: 30 agent run mintavételezés + bias checklist + explainability-ready export. Mérők: compliance csapat feedback, time-to-approve csökkenés, audit readiness.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-04.md | 2026-04-04 09:30 CET*

---

# Update — 2026-04-05

## H29 — Agent Cost Governance & Token Budget Enforcement Plane
**Thesis:** A multi-agent rendszerek egyik leggyorsabban fájó production problémája a kontrollálhatatlan token költség. A provider oldali limitek (account-level cap) utólagosak: azt mutatják, mi történt, nem azt, mi történik. A csapatoknak kell egy runtime szintű költség- és token budget enforcement réteg: threshold alapú warn/degrade/block, auditálható döntésekkel, több agent és több toolchain (LangChain/CrewAI/AutoGen/MCP) felett.
**Signals (updated 2026-04-05):**
- Tokencap (HN/GitHub, 2026-04-04): token budget enforcement wrapper + threshold akciók (WARN/DEGRADE/BLOCK/WEBHOOK), SQLite/Redis backend, framework patching támogatás. HIGH CONFIDENCE.
- Egyre több agent devtool/platform jel (Microsoft agent-framework, goose, Claude Code) -> több párhuzamos agent run, a költségkockázat gyorsan skálázódik. MEDIUM CONFIDENCE.
**Assessment:** Ez a H19 (Operational Reliability) pénzügyi testvére: nem csak azt méred, hogy sikerült-e, hanem azt is, hogy mennyibe került és mikor kell beavatkozni. Buyer: engineering lead, platform team, CFO-érzékeny ops vezető. Navibase alkalmazás: “Agent Budget Guard” (per-agent / per-customer / per-workflow budget, automatikus degrade policy, audit export).
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-05). A Tokencap egy direkt, high-signal validáció: ez már nem “nice-to-have”, hanem production control gap.*


## Ranking Summary (2026-04-05)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 — Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 — Agent Identity & Auth | 21/25 | = |
| 5 | H20 — Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H24 — Shadow AI Governance Plane | 21/25 | = |
| 7 | H3 — MCP Governance | 20/25 | = |
| 8 | H12 — Agent Accountability Framework | 20/25 | = |
| 9 | H10 — Agent Infra as Code | 19/25 | = |
| 10 | H15 — B2B SaaS Agent Feature Injection | 19/25 | = |
| 11 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 12 | H8 — Cross-Agent Context | 18/25 | = |
| 13 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 14 | H14 — Agent-to-Agent Trust & M2M | 18/25 | = |
| 15 | H16 — AI Alignment Measurement as a Service | 18/25 | = |
| 16 | H17 — Controlled Self-Configuration Boundary | 18/25 | = |
| 17 | H18 — Organizationally-Aligned AI | 18/25 | = |
| 18 | H19 — Operational Reliability Layer | 18/25 | = |
| 19 | H21 — Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 20 | H23 — Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 21 | H28 — Bias/Fairness Governance | 18/25 | = |
| 22 | H4 — Agent Payment Rails | 17/25 | = |
| 23 | H11 — Hallucination Self-Check | 17/25 | = |
| 24 | H27 — Agent Packaging & Portability Spec | 17/25 | = |
| 25 | **H29 — Cost Governance & Token Budget Enforcement** | **17/25** | **ÚJ** |
| 26 | H5 — Discovery & Registry | 16/25 | = |
| 27 | H25 — Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 28 | H26 — WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 29 | H9 — Agent Communication Infra | 12/25 | = |

*2026-04-05 delta: 1 új hypothesis (H29). A napi signalok (Tokencap + agent frameworkek) azt jelzik, hogy a költség-kontroll gyorsan “table stakes” lesz a production agent üzemeltetésben.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-05)

### #1: H22 + H24 combo — Shadow Agent Exposure + Adversarial Robustness
**Miért most:** Shadow AI buyer (IT/security) + DeepMind 6 trap mint specifikáció. Gyors, mérhető audit deliverable.
**Javasolt kísérlet:** “Shadow Agent Exposure Scan” 5 EU cégnek: inventory + 6-trap exposure score + quick fixes + audit export. Mérők: meeting->pilot, pilot->paid, top 5 control request.

### #2: H20 — Agent Platform as Regulated Infrastructure (Packaging)
**Miért most:** EU AI Act Aug 2026. A piac dokumentálhatóságot vesz, nem feature listát.
**Javasolt kísérlet:** 1 oldalas “EU AI Act Agent Compliance Mapping” (H1+H2+H6+H12+H22) + checklist, 10 célzott outreach. Mérők: letöltés, inbound meeting, compliance kérdések.

### #3: H29 — Agent Cost Governance & Token Budget Enforcement
**Miért most:** A költség-szivárgás a leggyorsabban észlelt production fájdalom. A Tokencap validálja, hogy már van “új kategória”.
**Javasolt kísérlet:** Navibase/Leoni “Budget Guard” MVP belsőn: per-run token tracking + threshold (warn/degrade/block) + heti cost report. Mérők: költség-variancia csökkenés, run-fail arány változás, user elégedettség (nem zavaró throttle).

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-05.md | 2026-04-05 09:30 CET*


---

# Update — 2026-04-06

## H30 — MCP-based Agent Trading Protocol & Risk Governance Layer
**Thesis:** Ahogy a trading (forex/crypto/equities) domain-ben megjelennek az autonóm agentek, a legnagyobb hiány nem a stratégiákban, hanem a **standardizált, auditálható és kockázat-korlátozott execution layer-ben** van. Ma mindenki ad-hoc köt broker API-ra, nincs deklaratív risk-limit (position sizing, max drawdown, kill switch), nincs egységes audit trail a tool call-okhoz, és nincs “compliance-ready” agent trading protokoll. Egy MCP-alapú standard/protokoll a trading agentekhez (order intents, approval gates, risk policy, audit export) a következő “infrastructure layer” lehet.
**Signals (updated 2026-04-06):**
- Apex Protocol – an open MCP-based standard for AI agent trading (apexstandard.org, 2026-04-06) — explicit standardizációs kísérlet a trading agentekre. HIGH CONFIDENCE.
- TradingAgents multi-agent trading framework (GitHub, 2026-03-21) — domain agentek proliferálnak, execution + governance gap nő. MEDIUM CONFIDENCE.
- EU AI Act Aug 2026 + audit/policy trend (korábbi H1/H2/H6/H20) — high-risk döntések és pénzügyi műveletek auditálhatósága és kontrollja “table stakes” irányba megy. HIGH CONFIDENCE.
**Assessment:** A moat nem a stratégia, hanem a **risk + audit + approval** standard és a broker-connectorok. Navibase alkalmazás: “Trading Ops Agent” csak akkor skálázható, ha a risk policy és a felelősségi határok deklaratívak.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=4 | **Total: 20/25**
*Új hypothesis (2026-04-06). Az Apex Protocol konkrét jel, hogy a piac standardot keres. A termék-wedge: risk governance + audit export, nem “jobb trading stratégia”.*

---

## H31 — Agent-Native Knowledge Base for Complex Office Files (Local-first)
**Thesis:** Az SMB ops agentek legnehezebb inputja nem web, hanem **helyi, komplex office fájlok** (Excel, többféle PDF, szerződés verziók, e-mail exportok). A klasszikus RAG/KB rendszerek itt elbuknak: nem értik a táblázat-struktúrát, nem kezelik jól a verziókövetést, és nem adnak “repo-native” workflow-t (diff, cite, provenance). Kell egy agent-native, local-first knowledge base réteg, ami a “messy office” fájlhalmazt megbízhatóan kereshetővé és hivatkozhatóvá teszi.
**Signals (updated 2026-04-06):**
- Show HN: DocMason – Agent Knowledge Base for local complex office files (GitHub, 2026-04-04) — explicit pain + megoldási irány. HIGH CONFIDENCE.
- dmtrKovalenko/fff.nvim – fast file search toolkit for AI agents (GitHub, 2026-04-04) — a file-level retrieval agent primitive lesz. MEDIUM CONFIDENCE.
**Assessment:** KKV-nál az első kérdés: “a saját fájljaimból dolgozik-e és vissza tudom-e követni?” A differenciáló: citations + provenance + version-aware indexing.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=3 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-04-06). A DocMason közvetlen validáció: az agentek KB-ja nem csak “docs”, hanem office-file reality.*

---

## Ranking Summary (2026-04-06)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 — Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 — Agent Identity & Auth | 21/25 | = |
| 5 | H20 — Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H24 — Shadow AI Governance Plane | 21/25 | = |
| 7 | H3 — MCP Governance | 20/25 | = |
| 8 | H12 — Agent Accountability Framework | 20/25 | = |
| 9 | **H30 — Agent Trading Protocol & Risk Governance** | **20/25** | **ÚJ** |
| 10 | H10 — Agent Infra as Code | 19/25 | = |
| 11 | H15 — B2B SaaS Agent Feature Injection | 19/25 | = |
| 12 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 13 | H8 — Cross-Agent Context | 18/25 | = |
| 14 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 15 | H14 — Agent-to-Agent Trust & M2M | 18/25 | = |
| 16 | H16 — AI Alignment Measurement as a Service | 18/25 | = |
| 17 | H17 — Controlled Self-Configuration Boundary | 18/25 | = |
| 18 | H18 — Organizationally-Aligned AI | 18/25 | = |
| 19 | H19 — Operational Reliability Layer | 18/25 | = |
| 20 | H21 — Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 21 | H23 — Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 22 | H28 — Bias/Fairness Governance | 18/25 | = |
| 23 | H4 — Agent Payment Rails | 17/25 | = |
| 24 | H11 — Hallucination Self-Check | 17/25 | = |
| 25 | H27 — Agent Packaging & Portability Spec | 17/25 | = |
| 26 | H29 — Cost Governance & Token Budget Enforcement | 17/25 | = |
| 27 | **H31 — Agent-Native KB for Office Files** | **17/25** | **ÚJ** |
| 28 | H5 — Discovery & Registry | 16/25 | = |
| 29 | H25 — Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 30 | H26 — WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 31 | H9 — Agent Communication Infra | 12/25 | = |

---

## Top 3 Opportunities + Suggested Experiments (2026-04-06)

### #1: H22 + H24 combo — Shadow Agent Exposure Scan + Adversarial Shield
**Miért most:** Shadow AI buyer (IT/security) + DeepMind 6 trap mint kőkemény scan spec. Ez a leggyorsabb “audit deliverable” út fizetős pilothoz.
**Javasolt kísérlet:** 5 EU cégnek 2 hetes “Shadow Agent Exposure Scan”: inventory + 6-trap exposure score + quick fixes + audit export. Mérők: meeting->pilot, pilot->paid, top 5 control request.

### #2: H20 — Agent Platform as Regulated Infrastructure (EU AI Act packaging)
**Miért most:** EU AI Act Aug 2026 deadline közel. A compliance-ready platform narratíva most válik belépési feltétellé.
**Javasolt kísérlet:** 1 oldalas “EU AI Act Agent Compliance Mapping” (H1+H2+H6+H12+H22) + letölthető checklist + 10 célzott outreach. Mérők: letöltés, inbound meeting, “melyik cikkely fáj” visszajelzés.

### #3: H30 — Agent Trading Protocol & Risk Governance (Apex wedge)
**Miért most:** Az Apex Protocol explicit standard-signal. A trading agenteknél a WTP nem “jobb prompt”, hanem risk limit + audit + approval.
**Javasolt kísérlet:** 1 hetes prototípus: “Trading MCP Gateway” (csak paper-trading / demo): order-intent schema + risk policy (max loss/nap, max position size) + immutable audit log export. Mérők: 3 domain feedback (trader/dev), implementációs friction (broker API), és hogy mely policy-k a minimum elvárt.

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-06.md | 2026-04-06 09:30 CET*


---

# Update — 2026-04-07

## H32 — Continuous Agent Harness Improvement from Production Traces
**Thesis:** Production agenteknél a „harness” (promptok, tool policy-k, workflow lépések, retry/guardrail logika) gyorsan elavul és driftel. A mai gyakorlat: kézzel nézzük a trace-eket és kézzel javítunk. Kell egy trace-to-patch réteg: a production trace-ekből automatikusan hibamintákat azonosít, kiértékel, és javaslatot tesz prompt/workflow/policy módosításokra, auditálható módon.

**Signals (updated 2026-04-07):**
- Show HN: **meta-agent** (GitHub, 2026-04-06): „automatically and continuously improves agent harnesses from production traces”. HIGH CONFIDENCE.
- **ALTK** paper (arxiv, 2026-03-16): a production failure mode-ok (silent reasoning error, tool argument corruption, policy violation) rendszerszinten jelennek meg; improvement loop nélkül csak tűzoltás lesz. HIGH CONFIDENCE.

**Assessment:** Navibase/Leoni esetben a run log + outcome már most rendelkezésre áll (cron/task, tool-call, hiba). Egy „trace-to-patch” loop közvetlenül csökkenti a human-in-the-loop terhelést és növeli a reliability-t (H19), miközben dokumentálható (H2).

**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-07). A meta-agent jel egyértelmű: a következő réteg nem új agent framework, hanem a production trace-ekből táplált folyamatos javítási pipeline.*

---

## H33 — Multi-Agent Influence Governance (Constitutional / Anti-Manipulation Layer)
**Thesis:** Multi-agent rendszerekben az agentek nem csak eszközöket használnak, hanem egymást is befolyásolják: meggyőzés, koalíció, collusion, cél-eltolódás. Egy enterprise buyernek nem elég a tool permission (H6) és az audit log (H2) - kell egy governance réteg, ami explicit „constitutiót” ad a multi-agent populációnak (szerepkörök, szavazási szabályok, veto/override, influence detection), és ebből compliance-ready bizonyítékot gyárt.

**Signals (updated 2026-04-07):**
- **LLM Constitutional Multi-Agent Governance** (arxiv, 2026-03-13): a modellek képesek persuasív influence stratégiákra, amelyek megváltoztatják a kooperációt - kérdés, hogy ez valódi proszociális eredmény-e vagy manipuláció. HIGH CONFIDENCE.
- **Regulating AI Agents** (arxiv, 2026-03-24): mainstream szabályozói fókusz autonóm cselekvés + limitált emberi felügyelet mellett - multi-agent governance mint következő célterület. HIGH CONFIDENCE.

**Assessment:** Rövid távon nehezebb termékké tenni (komplex, kevés buyer language), de magas Def potenciál: aki először szabványosítja a „multi-agent constitution + evidence pack” gondolkodást, az előnybe kerülhet a nagy enterprise multi-agent deployment hullámban.

**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=4 | IntFric=4 | **Total: 18/25**
*Új hypothesis (2026-04-07). A constitutional governance paper explicit jelzés: a következő governance fájdalom az agent-to-agent influence kontrollja lesz, nem csak a tool hozzáférés.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-07)

### #1: H22 + H24 combo — Shadow Agent Exposure Scan + Adversarial Shield
**Miért most:** A buyer (IT/security) azonnali fájdalmat érez (shadow agent inventory + containment), a DeepMind 6 trap pedig konkrét „scan spec”-et ad.
**Javasolt kísérlet:** 5 EU cégnek 2 hetes „Shadow Agent Exposure Scan”: inventory + 6-trap exposure score + quick fixes + audit export. Mérők: meeting->pilot, pilot->paid, top 5 control request.

### #2: H32 — Trace-to-Patch Harness Improvement (belső gyors ROI)
**Miért most:** A meta-agent jelzi, hogy a „production trace-driven improvement” elkezdett standard mintává válni.
**Javasolt kísérlet:** 14 napos belső pilot Leoni-n: (1) top 20 failure pattern automatikus klaszterezése trace-ekből, (2) heti 5 „patch proposal” (prompt/policy/workflow) + A/B vagy holdout validáció. Mérők: run success rate, human intervention rate, regressziók száma.

### #3: H20 — Agent Platform as Regulated Infrastructure (packaging)
**Miért most:** EU AI Act Aug 2026 ablak zárul; a compliance-ready platform narratíva most belépési feltétellé válik.
**Javasolt kísérlet:** 1 oldalas „EU AI Act Agent Compliance Mapping” (H1+H2+H6+H12+H22) + letölthető checklist + 10 célzott outreach. Mérők: letöltés, inbound meeting, „melyik cikkely fáj” visszajelzés.

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-07.md | 2026-04-07 09:30 CET*


---

# Update — 2026-04-11

## H40 — Agent Identity & Attestation for Delegated Workloads (Workload-to-Agent)
**Thesis:** Az agent identity (H1) implementációja a „workload-to-agent” attestation mintázat felé konszolidálódik: az agent futtatási workload kap rövid életű, igazolt identitást (mTLS/JWT), ami a delegáció kontextusához kötött. Ez egyszerre ad scoped hozzáférést, audit korrelációt, és egyértelmű választ a compliance kérdésre: „ki az agent, miért és milyen jogosultsággal cselekedett?”
**Signals (updated 2026-04-11):**
- Agent Identity Standards consolidate around workload-to-agent attestation (2026-04-10) — attestation-first identity minta. HIGH CONFIDENCE.
- Identity providers add “Agent” as first-class principal type (2026-04-05) — agent principalok külön kezelése. HIGH CONFIDENCE.
- Authentication for tool servers moves toward mTLS + JWT (2026-03-28) — a technikai forma stabilizálódik. HIGH CONFIDENCE.
**Assessment:** Ez a H1 „legvalószínűbb kivitelezési formája”. Navibase alkalmazás: per-run issued tokenek + delegation chain id, ami mind auditban (H2), mind policy-ben (H6) alap primitív.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Új hypothesis (2026-04-11). A workload-attestation minta elég konkrét, hogy termék-spec legyen: runtime identity issuance + audit correlation + scope expiry.*


## H41 — Audit-First Agent Logs as Compliance Artifact (Immutable, Replayable)
**Thesis:** A buyer nem „observabilityt” kér, hanem *compliance artifactot*: immutable, exportálható action log + replay, ami procurement és SOC 2 auditban bizonyíték. Az agent run nem csak trace, hanem aláírható, megőrizhető és SIEM-be köthető bizonyítéklánc.
**Signals (updated 2026-04-11):**
- Enterprises demand agent action logs as compliance artifact (2026-04-10) — procurement checklist trend. HIGH CONFIDENCE.
- Model providers add tool-call audit hooks (2026-03-30) — natív trace export a platformokból. HIGH CONFIDENCE.
- SOC 2 auditors ask for evidence of agent guardrails (2026-04-04) — explicit audit evidence kérés. HIGH CONFIDENCE.
**Assessment:** Ez a H2 fókuszát élesíti: nem elég logolni, „audit evidence pack”-ként kell csomagolni (H38). Navibase alkalmazás: export template-ek (SOC2/EU AI Act) + replay link + immutability (hash chain).
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Új hypothesis (2026-04-11). A compliance artifact nyelv buyer-friendly, és közvetlen procurement stopper. Quick wedge lehet advisory + tool.*


## H42 — MCP Security Profiles for Tool Servers (Standardized Auth, Scopes, Audit Events)
**Thesis:** A tool server sprawl (MCP) miatt az enterprise igény a „biztonsági profil”: standard auth (mTLS/JWT/OAuth), least-privilege scope, és egységes audit event schema. Ezzel a governance nem egyedi integráció per tool server, hanem profile-based compliance.
**Signals (updated 2026-04-11):**
- MCP Security Profiles proposed for tool servers (2026-04-09) — explicit standard draft. HIGH CONFIDENCE.
- Policy-as-code gatekeepers for agent actions (2026-04-03) — inline enforcement igény. HIGH CONFIDENCE.
- Agents as integration layer: tool server market grows (2026-04-02) — tool server piac nő, standardizáció nélkül szétcsúszik. HIGH CONFIDENCE.
**Assessment:** H3 (MCP governance) konkrétítható „profiles + conformance test” irányba. Navibase alkalmazás: MCP profile lint + conformance scan, compliance reporttal.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-11). A standard draft miatt a window most nyílt: aki hamar ad lintert és reportot, a procurement nyelvét beszéli.*


## H43 — Signed A2A Delegation Claims (Ghost Delegation Prevention)
**Thesis:** Agent-to-agent kommunikációban a legnagyobb enterprise félelem a „ghost delegation”: ki adott kinek felhatalmazást, milyen policy mellett, és ezt utólag hogyan bizonyítod. A megoldás: aláírt delegation claims (intent, constraints, context) a message payloadban, ami korrelálható audit traillel.
**Signals (updated 2026-04-11):**
- Agent-to-agent (A2A) messaging gets standardized claims (2026-04-09) — signed claims schema. HIGH CONFIDENCE.
- “Delegation risk” added to enterprise AI risk registers (2026-04-08) — kockázat explicit kategória. HIGH CONFIDENCE.
- Compliance teams ask: “Who is the agent?” (2026-03-27) — identity record igény. HIGH CONFIDENCE.
**Assessment:** H14 (A2A trust) és H12 (accountability) metszete. Navibase alkalmazás: delegation receipt, chain-of-custody, és dispute/contestability támogatás.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=4 | IntFric=4 | **Total: 20/25**
*Új hypothesis (2026-04-11). A signed claims lehet a következő standard primitív, de build fric magasabb és a buyer language még alakul.*


## H44 — Consent Receipts + Preview-Then-Execute for External Actions
**Thesis:** Enterprise governance minta: külső kommunikáció és record-módosítás előtt kötelező a preview + explicit consent receipt. A consent receipt egy auditálható artefakt, ami egyértelműsíti: ki és mikor engedélyezte az agent műveletét, milyen diff alapján.
**Signals (updated 2026-04-11):**
- “Consent receipts” for delegated actions in customer ops (2026-04-05) — explicit receipt pattern. HIGH CONFIDENCE.
- Delegation UX patterns: “preview then execute” (2026-04-01) — stabilizálódó UX standard. HIGH CONFIDENCE.
- Enterprises require HITL for external communications (2026-04-03) — governance baseline. HIGH CONFIDENCE.
**Assessment:** H34/H39 ops UX + H2 audit trail gyakorlati kimenete. Navibase alkalmazás: Telegram-first diff preview + approve button + consent receipt export.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-11). Alacsony build fric, gyorsan termékesíthető feature, és erős compliance story.*


## H45 — Agent Runbooks + Incident Response Playbooks (Operationalization Layer)
**Thesis:** Ahogy agentek production-ba kerülnek, SRE-szerű üzemeltetési réteg kell: runbook (eszkaláció, rollback, approval pontok) és incident response playbook (containment, credential revoke, replay analysis). Ez a governance hiányzó „operációs” fele.
**Signals (updated 2026-04-11):**
- “Agent runbooks” adopted as operational primitive (2026-04-01) — SRE-minta adaptáció. HIGH CONFIDENCE.
- Agent incident response playbooks emerge (2026-03-29) — security ops oldal. HIGH CONFIDENCE.
- Audit-first orchestration differentiator (2026-04-08) — a platformok erre pozicionálnak. HIGH CONFIDENCE.
**Assessment:** Ez service + tooling csomag. Navibase alkalmazás: standard runbook template library, ami összeköti a H2/H6/H40 identity primitive-eket a valós üzemeltetéssel.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-11). A runbook deliverable buyer-friendly, és jól csomagolható pilot ajánlatként.*


---

## Top 3 Opportunities + Suggested Experiments (2026-04-11)

### #1: H40 + H41 combo — Identity attestation + Compliance-grade action logs
**Miért most:** A procurement és compliance nyelv most konkretizálódik: „who is the agent” + immutable evidence. Ez a leggyorsabb enterprise wedge.
**Kísérlet:** 10 EU cégnek „Agent Delegation Evidence Pack” pilot: per-run issued identity (workload attestation) + immutable action log export + replay link. Mérők: procurement blocker-ek száma, pilot->paid konverzió, audit csapat feedback.

### #2: H42 — MCP Security Profiles linter + conformance scan
**Miért most:** Standard draft ablak nyitva, a tool server piac nő. Aki ad lintert és reportot, könnyen kerül shortlistre.
**Kísérlet:** Nyílt „MCP Security Profile Linter” v0.1: auth/scope/audit event checklist + report. Mérők: GitHub csillag, enterprise inbound, partner tool server-ek száma.

### #3: H44 — Consent receipts + preview-then-execute (Navibase/Leoni quick win)
**Miért most:** HITL external comms baseline lett. Low build, high trust.
**Kísérlet:** Leoni-ban 2 hetes pilot: minden külső email és CRM update előtt diff preview + approve, automatikus consent receipt mentés. Mérők: approval latency, user trust feedback, hibák csökkenése.


---

# Update — 2026-04-16

## H62 — Vendor Agent SDK Safety Primitives (Guardrails move “up-stack”)
**Thesis:** Ahogy a nagy model provider-ek agent SDK-i érettebbé válnak, a safety és governance primitívek (policy hooks, tool call guardrails, structured auditing) "felköltöznek" a vendor SDK rétegébe. Ez csökkenti a belépési súrlódást, de új problémát nyit: a csapatok több SDK-t használnak, és kell egy cross-vendor baseline (evidence export, policy mapping, org standard) ami nem lock-in.
**Signals (updated 2026-04-16):**
- OpenAI Agents SDK update (TechCrunch, 2026-04-15): enterprise-safe agent building primitives bővülése. https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/
**Assessment:** Ez a H6/H2/H41 irányt erősíti, de a termék-szintű realitás az, hogy a buyer először vendor SDK-t fog választani. Navibase: "guardrails + evidence export" adapter réteg, ami több SDK fölött ugyanazt a compliance artifactot adja.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-16). A safety primitives vendor-szintre tolódása gyorsítja az adoptiont, és felértékeli a cross-SDK governance/evidence réteget.*


## H63 — Agent Seat Licensing & Procurement Controls (Agents as employees)
**Thesis:** Ha az agentek "digitális munkatársakként" jelennek meg, a következő kontroll nem technikai, hanem gazdasági és compliance: licenc, seat assignment, költségallokáció, és entitlement kezelés (mely agent milyen szoftvert "használhat"). A seat/licensing modellek agent principalokra való kiterjesztése új platformréteget igényel.
**Signals (updated 2026-04-16):**
- Microsoft exec suggests AI agents will need to buy licenses, just like employees (Business Insider, 2026-04-14). https://www.businessinsider.com/microsoft-executive-suggests-ai-agents-buy-software-licenses-seats-2026-4
**Assessment:** Ez a H1/H60 identity + H29 cost governance metszete. Navibase: "agent entitlement registry" (agent principal → allowed apps/licenses) + audit export, ami procurement nyelven beszél.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-16). A "seat for agents" narratíva buyer-friendly, és gyorsan procurement kérdéssé válhat.*


## H64 — Integrity Hallucination / Decision Consistency Governance
**Thesis:** High-stakes környezetben a probléma nem csak "hallucination", hanem az inkonzisztens döntés (ugyanarra az inputra más kimenet, indoklás drift). Kell egy integritás és konzisztencia réteg: decision fingerprinting, invariánsok, regressziós teszt suite, és "integrity drift" metrika.
**Signals (updated 2026-04-16):**
- Integrity hallucination raises concerns over inconsistent AI decision-making in high-stakes systems (Devdiscourse, 2026-04-15). https://news.google.com/rss/articles/CBMi6wFBVV95cUxNYmJrUi1haWpYaFlZdENRdUswaFBlRDNpWGxTTHduQjl6QU04c3phN0FqR1YwRHlnY2JMTDBaUWVEVnRxVG9zdGpWckVHY05SRGZoc0VLSkZHdHY4SWJPdnZOckFyeVFwNDk3a1BZOUthQzUzLTJ4YmluYmhoSTgwWWRnWjJKWExwaFROcFBBRE1ZQ1RwZ3ZEM2cta3NCRFNfeHBlRVhwWlpxMHJrckFmeDg5eXM2bHp3R1BzcTRhYTUyMElqcTNFR01MRURRLTIyRUpEanRTaWZEd2NYdXRjTlQtWWt3amF6ZWlv0gHwAUFVX3lxTE15WFh1Skp4OE1RYjVYQ1JrVEt6QnpoSGl6SElXYmtxV3Bqc0pIa0dEVjU4Q2tHelkwa1JObXJ0ZG5TbVN6Y0JTSG8xQWoyMGV1Wkc1cVdpRnUySHBEQk1WWWdpVTNkYm91RE12Q1g0OS0zWXllQXZSMks0Ry01VFA4QlBQRDBubjVFNGRUYmwwWUlSOUtlT2dyMmVuSXNEY3VrbmphU3V5MElzYW9vRzREVm1qRVZ1VE9ESWhzSVQxOHB1Z1BHbTY0bHJlZDMwNGp6TzBkN2lfMTBIck9mSFVDdjRPSmlKdFgwbWt1QWpkOA?oc=5
**Assessment:** Ez a H21 (deterministic trust) technikai megfelelője. Navibase: "integrity gate" minden külső kimenet előtt, plusz audit-evidence a konzisztencia tesztekről.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-16). A failure-mode név ("integrity hallucination") segít buyer-nyelvre fordítani a konzisztencia problémát.*


## Top 3 Opportunities + Suggested Experiments (2026-04-16)

### #1: H62 — Cross-SDK evidence export baseline (vendor guardrails fölé)
**Miért most:** A safety primitive-ek vendor SDK-kban landolnak, de a buyer nem akar lock-in és egységes compliance artifactot akar.
**Kísérlet:** 3 nap: egy "evidence export adapter" prototípus (1 workflow) ami OpenAI Agents SDK runból exportál: tool-call timeline + policy decisions + correlation id, és ugyanarra a sémára illeszthető más SDK-ból is.

### #2: H63 — Agent entitlement registry (seat/licensing control plane)
**Miért most:** A "agents buy seats" narratíva procurement nyelv, gyorsan költség és compliance témává válik.
**Kísérlet:** 1 hét: minimál entitlement registry (agent principal → allowed SaaS/apps/licenses) + audit export + egyszerű approval flow (H44).

### #3: H64 — Integrity drift check for outbound actions (consistency gate)
**Miért most:** Inkonzisztens döntések high-stakes környezetben új failure-mode-ként vannak címkézve, a buyer ezt érti.
**Kísérlet:** 1 hét: "integrity test pack" 20 fix scenario-val + regressziós futtatás release előtt, és runtime "invariant checks" outbound email/record update előtt.


---

# Update — 2026-04-17

## H65 — Real-Time Agent Stack Anomaly Detection (Proactive Failure Intelligence)
**Thesis:** A passzív logging (trace, audit trail) és az utólagos RCA (H61) nem elegendő: a produkciós agent hiba ott fáj, ahol csendben, de az egész tech stacken keresztül terjedve jelenik meg. Az InsightFinder $15M befektetési validáció pontosan erre a rétegre irányul: nem a model-hibák detektálása, hanem az agent + infra + app stack viselkedésének proaktív anomália-detekciója. A winner nem logol, hanem előre jelez.
**Signals (updated 2026-04-17):**
- InsightFinder raises $15M: "help companies figure out where AI agents go wrong" (TechCrunch, 2026-04-16): CEO szerint a probléma nem egyes model hibák, hanem az egész tech stack viselkedése — explicit proaktív anomália kategória. $15M seed validálja a WTP-t. HIGH CONFIDENCE.
- Integrity hallucination — inconsistent AI decision-making in high-stakes systems (Devdiscourse, 2026-04-15): az inkonzisztencia felderítése real-time monitoring nélkül lehetetlen. HIGH CONFIDENCE.
**Assessment:** Ez a H61 (RCA) és H19 (operational reliability) következő rétege: nem "mi romlott el", hanem "mikor fog elromlani". A $15M validálja, hogy a buyer fizet ezért. Navibase alkalmazás: agent + cron + API stack behavioral baseline + anomália alert Telegramon, mielőtt a hiba terjed.
**Scores:** Pain=4 | Urgency=4 | WTP=5 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-17). Az InsightFinder befektetés az eddig legerősebb VC-validáció a proaktív agent stack monitoring kategóriában.*


## Megerősített signalok (2026-04-17)

**H59/H37/H53 (credential delegation):** Kontext CLI bekerült GitHub-ra (2026-04-14) + "Do you trust AI agents with API keys?" HN thread (2026-04-12) egymást erősítik. A credential boundary kérdés nem elméleti — napi ops dilemma. Credential brokerage/JIT token pattern gyorsabban válhat table stakes-szé, mint terveztük.

**H60/H1 (agent identity platform):** ZeroID megerősítés (Help Net Security, 2026-04-13) + dedikált "AI Agents Authentication" cikk (Security Boulevard, 2026-04-16): az agent identity mint önálló platform-réteg kristályosodik. A ZeroID open-source terjedése felgyorsíthatja a compliance elvárást a nem-ZeroID platformokon.

**H63 (agent seat licensing):** Microsoft "agents buy licenses like employees" újra megjelent mainstream sajtóban (Business Insider, 2026-04-14). Az entitlement/licensing kérdés a procurement szintre érkezett.

**H64/H21 (integrity/consistency governance):** Az "integrity hallucination" elnevezés (Devdiscourse, 2026-04-15) buyer-szintű nyelvet ad a konzisztencia-problémának. High-stakes rendszereknél ez gyorsan compliance-kérdéssé válik.

**H34/H44 (human-in-the-loop formalization):** "The human exception in AI governance: ticking boxes?" (Computer Weekly, 2026-04-08) jelzi, hogy a HITL nem elég szabályozói szemmel — formalizált döntési határok kellenek. Ez a H44 (consent receipts) és H6 (policy enforcement) piaci narratíváját erősíti.

**H20/H6 (policy + platform compliance):** Algorithmic government paper (BizNews, 2026-04-15) — a döntési delegáció szabályozói keretbe illesztése nemcsak várható, hanem elkerülhetetlen. Platform-szintű compliance deadline-ok közelednek.


## Ranking Summary (2026-04-17)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 — Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 — Agent Identity & Auth | 21/25 | = |
| 5 | H20 — Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H24 — Shadow AI Governance Plane | 21/25 | = |
| 7 | H40 — Workload-to-Agent Attestation | 22/25 | = |
| 8 | H41 — Audit-First Compliance Artifacts | 22/25 | = |
| 9 | H3 — MCP Governance | 20/25 | = |
| 10 | H12 — Agent Accountability Framework | 20/25 | = |
| 11 | H30 — Agent Trading Protocol & Risk Governance | 20/25 | = |
| 12 | H43 — Signed A2A Delegation Claims | 20/25 | = |
| 13 | H10 — Agent Infra as Code | 19/25 | = |
| 14 | H15 — B2B SaaS Agent Feature Injection | 19/25 | = |
| 15 | H42 — MCP Security Profiles | 19/25 | = |
| 16 | **H65 — Proactive Agent Stack Anomaly Detection** | **19/25** | **ÚJ** |
| 17 | H59 — Agent Credential Brokerage | 19/25 | = |
| 18 | H60 — Agent Identity Platform | 19/25 | = |
| 19 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 20 | H8 — Cross-Agent Context | 18/25 | = |
| 21 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 22 | H14 — Agent-to-Agent Trust & M2M | 18/25 | = |
| 23 | H16 — AI Alignment Measurement as a Service | 18/25 | = |
| 24 | H17 — Controlled Self-Configuration Boundary | 18/25 | = |
| 25 | H18 — Organizationally-Aligned AI | 18/25 | = |
| 26 | H19 — Operational Reliability Layer | 18/25 | = |
| 27 | H21 — Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 28 | H23 — Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 29 | H28 — Bias/Fairness Governance | 18/25 | = |
| 30 | H32 — Trace-to-Patch Harness Improvement | 18/25 | = |
| 31 | H33 — Multi-Agent Influence Governance | 18/25 | = |
| 32 | H61 — Agent Failure Investigation Automation | 17/25 | = |
| 33 | H63 — Agent Seat Licensing & Procurement | 18/25 | ↑ signal erős |
| 34 | H64 — Integrity Hallucination / Consistency Governance | 18/25 | ↑ névvel bíró failure mode |
| 35 | H4 — Agent Payment Rails | 17/25 | = |
| 36 | H11 — Hallucination Self-Check | 17/25 | = |
| 37 | H27 — Agent Packaging & Portability Spec | 17/25 | = |
| 38 | H29 — Cost Governance & Token Budget | 17/25 | = |
| 39 | H31 — Agent-Native KB for Office Files | 17/25 | = |
| 40 | H44 — Consent Receipts + Preview-Then-Execute | 17/25 | = |
| 41 | H45 — Agent Runbooks & Incident Response | 17/25 | = |
| 42 | H62 — Cross-SDK Safety Primitives | 17/25 | = |
| 43 | H5 — Discovery & Registry | 16/25 | = |
| 44 | H25 — Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 45 | H26 — WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 46 | H9 — Agent Communication Infra | 12/25 | = |

*2026-04-17 delta: 1 új hypothesis (H65 — Proactive Agent Stack Anomaly Detection, 19/25). Megerősített irányok: H59/H60 credential+identity erősödik, H63 procurement szintre ér, H64 buyer-language névvel bír.*


## Top 3 Opportunities + Suggested Experiments (2026-04-17)

### #1: H65 — Proactive Agent Stack Anomaly Detection (InsightFinder validáció)
**Miért most:** $15M seed befektetés validálja a WTP-t — a buyer fizet a proaktív anomália-detektálásért. A versenytárs (InsightFinder) enterprise-fókuszú; a KKV wedge nyitva van. Leoni belső infrastruktúrán (cron, task runner, API hívások) már van elég trace-adat egy MVP-hez.
**Kísérlet:** 2 hetes pilot: agent run behavioral baseline rögzítés (latency, tool-call sorrend, failure arány per feladattípus) + anomália alert Telegramon ha >2 sigma eltérés. Mérők: false positive arány, mean-time-to-detect, Tomi visszajelzés (hasznos-e az alert).
**Befektetés:** ~3 nap build. Leoni trace data már megvan.

### #2: H59/H37 — Credential Delegation Demo (Secretless-by-default proof)
**Miért most:** Kontext CLI + HN trust thread egyszerre jelzi: ez napi ops dilemma, nem elméleti. A buyer language egyszerű: "nem adom oda a kulcsaimat." JIT token + scope + audit correlation lánc gyorsan termékesíthető.
**Kísérlet:** 3 napos demo: OIDC token exchange + JIT token issuance + audit correlation ID (per run). Deliverable: 1 oldalas evidence export + 2 perces képernyőfelvétel a Navibase pitchhez.
**Befektetés:** ~3 nap. Kontext CLI maga a reference implementation.

### #3: H64 — Integrity Consistency Gate (outbound actions előtt)
**Miért most:** Az "integrity hallucination" buyer-szintű névvel bíró failure mode lett. High-stakes döntéseknél (ajánlat, email, döntéstámogatás) az inkonzisztencia már közvetlen üzleti kár. Alacsony build fric: 20 fix scenario + regression checker.
**Kísérlet:** 1 hét: "integrity test pack" (20 fix scenario, Leoni outbound email + kanban update + cron) + regressziós futtatás release/konfig változás előtt. Mérők: inkonzisztencia arány, false block arány, Tomi audit visszajelzés.
**Befektetés:** ~2 nap. Navibase differenciáló: "minden outbound action mögött konzisztencia garancia."

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-17.md (350 releváns, 92 prioritizált) | 2026-04-17 18:48 CET*


---

# Update — 2026-04-20

## H66 — Agentic Supply Chain Security (Distillation as Attack Vector)
**Thesis:** Az agentic safety eddig feltételezte, hogy az adatszanitáció elegendő védelmet nyújt. Az arxiv "subliminal transfer" paper megmutatja: veszélyes viselkedési minták implicit módon beágyazódnak modell-disztilláció során — akkor is, ha az explicit kulcsszavakat kiszűrik. Ez az agentic supply chain legalaposabban alulbeszélt kockázata: nem az input, hanem a modell örökölt viselkedése a fenyegetés. Kell egy "supply chain attestation" réteg: honnan jött a modell, milyen trajektória-adatokon tanult, és milyen implicit viselkedési bias-t örökített a tanártól a diákra?
**Signals (updated 2026-04-20):**
- "Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation" (arxiv, 2026-04-16): diákmodell örökli a tanár destruktív magatartását (törlési bias, destructive filesystem operations) puszta trajektória-dinamikából, explicit kulcsszavak kiszürése után is. HIGH CONFIDENCE.
- "Secure-by-Design: 3 Principles to Safely Scale Agentic AI" (CIO.com, 2026-04-16): mainstream enterprise IT napirendbe kerül az agentic AI biztonság, de a supply chain kockázat explicit formában még nem jelenik meg. HIGH CONFIDENCE.
- H22 (Adversarial Robustness) és H23 (Agentic QA) az input és runtime rétegre fókuszál — a supply chain (training/distillation) réteg különálló kategória.
**Assessment:** Ha az adatszanitáció nem véd, az enterprise adopció alapfeltevése omlik össze. A "supply chain attestation" mint compliance primitive valószínüleg gyorsan table stakes-szé válik: milyen training provenance van a deployed agent mögött? Navibase alkalmazás: deployed agent-ek "training lineage card"-ja, implicit behavior audit (behavioral invariant test suite), és vendor-attestation kérés kritikus deploymenteknél.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=4 | IntFric=4 | **Total: 21/25**
*Új hypothesis (2026-04-20). Az arxiv paper az elso empirikus bizonyíték arra, hogy az agentic supply chain támadási vektor — a training provenance és behavioral audit kategória eddig üres volt.*

---

## H67 — Offensive Agent Red-Teaming as a Service (Multi-turn Attack Automation)
**Thesis:** Az agentic testing ma manuális: biztonsági csapatok kézzel próbálnak prompt injectiont, tool hijackinget, logic bug-okat keresni. A Nyx harness megmutatja, hogy az agentic red-teaming automatizálható multi-turn forgatókönyvekkel — és 10 perc alatt megtalál olyan hibákat, amelyeket manuális auditok órák alatt sem. Ez az "offensive testing as a service" kategóriát nyitja meg: nem csak defense (H22/H6), hanem aktív, rendszeres agent attack simulation, deliverable-lel és compliance evidence-szel.
**Signals (updated 2026-04-20):**
- "Nyx – Multi-turn Offensive Testing Harness for AI Agents" (HN / fabraix.com, 2026-04-19): autonóm blackbox tesztelő eszköz AI agentekhez, 10 perc alatt detektál logikai hibát, prompt injectiont, tool hijackinget. HIGH CONFIDENCE.
- Trail of Bits mutation testing paper (2026-04-01): az agentic testing üres kategória, különbözo megközelítések egymást kiegészítik. HIGH CONFIDENCE.
- H23 (Agentic QA) rokon kategória, de a Nyx multi-turn attack simulation más dimenzió: nem mutation testing, hanem adversarial dialogue és toolchain abuse.
**Assessment:** Az "offensive agent testing" buyer-language: "tudom-e, hogy az agenten tört be valaki?" — ez a SOC 2 és enterprise security audit természetes következo kérdése. Navibase alkalmazás: negyedéves "Agent Red-Team Report" deliverable, Nyx-alapú automated scan + human-curated findings.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-20). A Nyx validálja a piacot: az automated multi-turn attack simulation nem kutatás, hanem használható eszköz. A "red-teaming as a service" a H23 mutation testing természetes következo fázisa.*

---

## H68 — Self-Evolving Agent Governance (GEP / Genome-Level Audit Gap)
**Thesis:** A "Genome Evolution Protocol" alapú önfejleszto agentek (EvoMap/evolver) megjelenése elorehozza az eddig 2027+ kategóriának besorolt governance kérdést: hogyan auditálható egy agent, amelyik saját magát módosítja futás közben? A H17 (Controlled Self-Configuration) a statikus scope-határ kérdése — az önfejleszto agent dinamikusan változó scope-ot jelent, ahol az audit trail nem egy állapotot, hanem egy evolúciós trajektóriát kell rögzítenie. Kell egy "genome audit" primitív: mikor változott az agent, mit változtatott, és a változás compliance-korlátok közt maradt-e?
**Signals (updated 2026-04-20):**
- "EvoMap/Evolver – GEP-Powered Self-Evolution Engine for AI Agents" (GitHub, 2026-04-17): agenteket önmagukat fejlesztheto rendszerekként kezeli Genome Evolution Protocol alapján. HIGH CONFIDENCE.
- H17 (Controlled Self-Configuration Boundary, 18/25): statikus scope-hardening megoldott — a dinamikus self-evolution új governance primitívet igényel.
- "Agentic AI and the next intelligence explosion" (arxiv, 2026-03-30): a self-evolving agent narratíva erosödik, governance elmarad. HIGH CONFIDENCE.
**Assessment:** Ez rövid távon research fázis, de a tooling megjelenése (EvoMap) azt jelzi, hogy a kérdés hamarabb éri el a productiont, mint terveztük. Navibase alkalmazás: "agent genome snapshot" minden futás elott/után + diff + compliance gate (engedélyezett vs. nem engedélyezett változás típusok).
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=4 | IntFric=4 | **Total: 18/25**
*Új hypothesis (2026-04-20). Az EvoMap a "self-evolving agent" kategóriát konkrét OSS eszközként megnyitja — a governance kérdés hamarabb production-kérdés lesz, mint várható volt.*

---

## H69 — Cross-Border AI Regulatory Fragmentation (Compliance Translation Layer)
**Thesis:** Ázsiában (India, Indonézia, Kína) és Európában (EU AI Act) párhuzamosan formálódnak az AI governance struktúrák, egymással nem harmonizáltan. Egy cross-border agent deployment (pl. KKV európai irodával és ázsiai partnerekkel) egyszerre kell megfeleljen az EU AI Act, MeitY, és esetleg indonéziai/kínai szabályozásnak — jelenleg nincs olyan eszköz, ami ezt automatikusan mappel, jelöli a konfliktusokat, és javasol compliance adaptációt. Ez az "AI regulatory translation" kategória.
**Signals (updated 2026-04-20):**
- India dual AI governance structure (Zee News / MediaNews4U, 2026-04-17-18): MeitY tech-policy panel + Ashwini Vaishnaw-vezette cross-minisztériumi testület párhuzamosan — India regulatory landscape összetett és gyorsan változik. HIGH CONFIDENCE.
- Indonesia AI Ethics and National Regulation (2026-04-17): délkelet-ázsiai szabályozás is formálódik. MEDIUM CONFIDENCE.
- Chinese groups global AI governance framework (2026-04-17): Kína aktívan alakítja a globális AI governance normákat, EU-s keretekkel kevés átfedéssel. MEDIUM CONFIDENCE.
- EU AI Act Aug 2026: európai framework kész, de cross-border deployment-nél nem elegendo. HIGH CONFIDENCE.
**Assessment:** A cross-border compliance gap 2026 végére éles piaci problémává válhat. A buyer: multinacionális KKV, külföldi piacra lépo startup, enterprise compliance csapat. Navibase alkalmazás: "Regulatory Matrix" — per-deployment compliance mapping (EU AI Act + MeitY + local) + automatikus gap-detekció + javasolt adaptációs lépések.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=4 | **Total: 19/25**
*Új hypothesis (2026-04-20). Az ázsiai regulatory proliferáció egyszerre erösíti és bonyolítja a compliance piacot. A "regulatory translation" kategória üres — a buyer fájdalma valós, de a termék még nincs.*

---

## H70 — Agent-Ready Web as Interoperability Standard
**Thesis:** Az internetes infrastruktúra "agent-readiness" szempontú értékelése (isitagentready.com, Cloudflare) jelzi, hogy hamarosan elvárás lesz, hogy API-k, weboldalak és B2B platformok natively megérthetok legyenek AI agentek számára (robots.txt analógiája agentek számára, strukturált tool-call schema, consent/auth dokumentáció). Aki nem tervezi erre rendszereit, az lemarad az agent-driven distribution hullámtól. Ez a "web-for-agents" szabványosítás következo platform-váltása.
**Signals (updated 2026-04-20):**
- "Isitagentready.com / Cloudflare — Website Agent-Readiness Scanner" (Product Hunt / Cloudflare, 2026-04-17): a Cloudflare elkezdette az internetes infrastruktúra "agent-readiness" szempontú értékelését. HIGH CONFIDENCE.
- "Agentic Infrastructure" (Vercel blog, 2026-04-17): Vercel dedikált blogposztban definiálja az "agentic infrastructure" fogalmát — az infrastruktúra réteg agent-first átalakulóban. HIGH CONFIDENCE.
- "Cloudflare Shared Dictionaries for agentic web" (2026-04-17): Cloudflare aktívan fejleszti az agent-web szint protokolljait. MEDIUM CONFIDENCE.
**Assessment:** Ez a következo "platform shift" — a web agent-ready lesz vagy lemarad. A buyer: weboldal-tulajdonos, SaaS cég, API-t publikáló vállalat. Navibase alkalmazás: "Agent-Ready Audit" — meglevo KKV infrastruktúra agent-readiness scoring + quick-fix checklist.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 15/25**
*Új hypothesis (2026-04-20). A Cloudflare + Vercel egyszerre validálja az irányt — az "agent-ready web" 2026-2027-es platform elvárás lesz, de a WTP és az urgency még alakul.*

---

## Megerosített signalok (2026-04-20)

**H1/H60 (agent authentication):** "AI Agents Authentication: How Autonomous Systems Prove Identity" (Security Boulevard, 2026-04-16) — az agent authentikáció mainstream napirendként jelenik meg. A H60 (Agent Identity Platform) megerosödik: ez a következo különálló platformréteg lesz.

**H65 (proaktív anomália detekció):** InsightFinder $15M megerosítés (TechCrunch, 2026-04-16) — a befektetés validálja, hogy a proaktív agent stack monitoring WTP reális. Az InsightFinder enterprise-fókuszú, KKV wedge nyitva.

**H22 (adversarial robustness):** Nyx offensive harness + H66 distillation attack vector együttesen jelzik: az adversarial agent attack surface szélesedik (nem csak input, hanem training + multi-turn dialogue).

**H36 (managed infrastructure):** Vercel "agentic infrastructure" blog — az infrastruktúra réteg agent-first átalakulása erösödik. Platform-szintü váltás közeledik.

**H49/H27 (multi-agent framework fragmentation):** OpenAI Agents Python nyílt forráskód (GitHub, 2026-04-17) — framework proliferáció és portabilitás/interoperabilitás kérdése élesedik. H27 (Agent Packaging & Portability) megerösödik.


## Ranking Summary (2026-04-20)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 — Audit Trail | 22/25 | = |
| 2 | H6 — Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 — Adversarial Robustness Layer | 22/25 | = |
| 4 | H40 — Workload-to-Agent Attestation | 22/25 | = |
| 5 | H41 — Audit-First Compliance Artifacts | 22/25 | = |
| 6 | H1 — Agent Identity & Auth | 21/25 | = |
| 7 | H20 — Agent Platform as Regulated Infrastructure | 21/25 | = |
| 8 | H24 — Shadow AI Governance Plane | 21/25 | = |
| 9 | **H66 — Agentic Supply Chain Security** | **21/25** | **ÚJ** |
| 10 | H3 — MCP Governance | 20/25 | = |
| 11 | H12 — Agent Accountability Framework | 20/25 | = |
| 12 | H30 — Agent Trading Protocol & Risk Governance | 20/25 | = |
| 13 | H43 — Signed A2A Delegation Claims | 20/25 | = |
| 14 | H10 — Agent Infra as Code | 19/25 | = |
| 15 | H15 — B2B SaaS Agent Feature Injection | 19/25 | = |
| 16 | H42 — MCP Security Profiles | 19/25 | = |
| 17 | H59 — Agent Credential Brokerage | 19/25 | = |
| 18 | H60 — Agent Identity Platform | 19/25 | = |
| 19 | H65 — Proactive Agent Stack Anomaly Detection | 19/25 | = |
| 20 | **H69 — Cross-Border Regulatory Fragmentation** | **19/25** | **ÚJ** |
| 21 | H7 — SMB Deployment Wrapper | 18/25 | = |
| 22 | H8 — Cross-Agent Context | 18/25 | = |
| 23 | H13 — Agent Sandboxing & Isolation | 18/25 | = |
| 24 | H14 — Agent-to-Agent Trust & M2M | 18/25 | = |
| 25 | H16 — AI Alignment Measurement as a Service | 18/25 | = |
| 26 | H17 — Controlled Self-Configuration Boundary | 18/25 | = |
| 27 | H18 — Organizationally-Aligned AI | 18/25 | = |
| 28 | H19 — Operational Reliability Layer | 18/25 | = |
| 29 | H21 — Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 30 | H23 — Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 31 | H28 — Bias/Fairness Governance | 18/25 | = |
| 32 | H32 — Trace-to-Patch Harness Improvement | 18/25 | = |
| 33 | H33 — Multi-Agent Influence Governance | 18/25 | = |
| 34 | H63 — Agent Seat Licensing & Procurement | 18/25 | = |
| 35 | H64 — Integrity Hallucination / Consistency Governance | 18/25 | = |
| 36 | **H67 — Offensive Agent Red-Teaming as a Service** | **18/25** | **ÚJ** |
| 37 | **H68 — Self-Evolving Agent Governance** | **18/25** | **ÚJ** |
| 38 | H4 — Agent Payment Rails | 17/25 | = |
| 39 | H11 — Hallucination Self-Check | 17/25 | = |
| 40 | H27 — Agent Packaging & Portability Spec | 17/25 | = |
| 41 | H29 — Cost Governance & Token Budget Enforcement | 17/25 | = |
| 42 | H31 — Agent-Native KB for Office Files | 17/25 | = |
| 43 | H44 — Consent Receipts + Preview-Then-Execute | 17/25 | = |
| 44 | H45 — Agent Runbooks & Incident Response | 17/25 | = |
| 45 | H61 — Agent Failure Investigation Automation | 17/25 | = |
| 46 | H62 — Cross-SDK Safety Primitives | 17/25 | = |
| 47 | H5 — Discovery & Registry | 16/25 | = |
| 48 | H25 — Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 49 | **H70 — Agent-Ready Web Infrastructure** | **15/25** | **ÚJ** |
| 50 | H26 — WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 51 | H9 — Agent Communication Infra | 12/25 | = |

*2026-04-20 delta: 5 új hypothesis (H66-H70). H66 (Agentic Supply Chain Security, 21/25) azonnal a top 9-be kerül — empirikus bizonyíték arra, hogy az adatszanitáció elégtelen védelemként az agentic supply chain ellen. H69 (Cross-Border Regulatory Fragmentation, 19/25) az ázsiai regulatory proliferációt fedezi le. H67/H68 a 18/25 blokkba kerülnek. H70 új kategória, 15/25 szinten még.*


## Top 3 Opportunities + Suggested Experiments (2026-04-20)

### #1: H66 — Agentic Supply Chain Security (Training Provenance Audit)
**Miért most:** Az arxiv subliminal transfer paper az egyetlen empirikus bizonyíték arra, hogy az enterprise compliance alapfeltevése ("szanitálj és telepíts") hamis. Ez a kategória eddig üres — az elso, aki "training lineage card" és behavioral invariant test suite-ot ad, azt a procurement kérdést kezeli, ami eddig nem létezett.
**Kísérlet:** 1 hét: "Behavioral Invariant Test Suite" prototípus — 20 fix scenario, amelyre az agent viselkedésének konzisztensen a várható határon belül kell maradnia, + automated run + pass/fail report. Deliverable: 1 oldalas "Agent Supply Chain Evidence Card" (training provenance + behavioral audit results). Merők: false positive arány, compliance csapat visszajelzés.
**Befektetés:** ~1 hét. Az arxiv paper maga a spec — szabad és high-credibility forrás.

### #2: H67 — Offensive Agent Red-Teaming (Nyx-alapú quarterly scan)
**Miért most:** A Nyx harness konkrét, useable eszköz — 10 perc alatt megtalál olyan hibákat, amelyeket manuális auditok nem. Az "offensive testing" SOC 2 és enterprise security buyer számára természetes deliverable.
**Kísérlet:** 2 napos pilot: Nyx futtatása Leoni agent-en + manuális kiegészítés (multi-turn adversarial dialogue) + "Agent Red-Team Summary" (3-5 kritikus finding + remediation javaslat). Merők: finding szám, severity, remediation time.
**Befektetés:** ~2 nap. Nyx maga az eszköz — externally validated scan.

### #3: H69 — Cross-Border Regulatory Compliance Mapping (EU + Asia wedge)
**Miért most:** India párhuzamos dual governance struktúra + EU AI Act Aug 2026 deadline — a cross-border compliance gap valóssá vált. Nincs eszköz, nincs advisory service, nincs template. Az elso "Regulatory Matrix" letöltheto sablon erős lead gen és thought leadership.
**Kísérlet:** 3 nap: "EU AI Act vs MeitY vs Indonesia AI Ethics" összehasonlító mátrix — per-kategória conflict mapping. Deliverable: 1 oldalas PDF + LinkedIn post + 5 célzott outreach CEE multinacionális cégeknek. Merők: letöltések, inbound megkeresések.
**Befektetés:** ~3 nap kutatás + formázás. Erős CEE differenciáló.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-20.md (402 releváns, top 30 elemezve) | 2026-04-20 09:30 CET*
