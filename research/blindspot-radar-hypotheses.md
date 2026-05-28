# Blindspot Radar — Scored Hypothesis List
Last updated: 2026-05-28


## H70 - Agentic Copyright & Data Provenance Chain (Training + Output Attribution)
**Thesis:** Az agentek tant őrdeknél (RAG, finetuning) és output-jában szerzői jogok sérülhetnek. Ez eddig egyéni model-problémának kezeltetett, de ahogy az agentek nagyobb adatból tanulnak és autonóm módon generálnak outputokat, a szerzői jogi chain-ben az agent-operátor vagy az agent-megbízó feladata hogy dokumentálja: melyik tanítódata jogi? melyik outputja attribúció-szükséges? kik az érdekeltek? Ez a H63 (jogi entity határ) mellett a pénzügyi/jogi felelősség határának mássza meg-definiálása.
**Signals (updated 2026-05-18):**
- Agentic Copyright, Data Scraping & AI Governance: Toward a Coasean Bargain in the Era of Artificial Intelligence (arXiv, 2026-04-08, Deep Score 0.4): explicit tanulmány, hogy a multi-agentic AI deployment során a data scraping, szerzői jogi felelősség és governance framework szükséges. arXiv: https://arxiv.org/abs/2604.07546. HIGH CONFIDENCE.
**Assessment:** Ez közvetlenül érinti az SMB klienst, aki "nem akarom, hogy jogilag kitettnek legyék". Az agent output attribúciós lánca (melyik adat, melyik modell, melyik prompt) az audit evidence (H62) és mandate (H63) mellett a harmadik jogi bizonyíték-réteg. Navibase: "copyright-clean" agent deployment checklist, tanítódata-audit, output attribution metszet.
**Scores:** Pain=5 | Urgency=4 | WTP=5 | Def=3 | IntFric=4 | **Total: 21/25**
*Új hypothesis (2026-05-18). Az arXiv papír a szerzői jogi governance-t szakterületi problémáról agentic infrastructure-ra emeli: nem elég a modell, a teljes agent pipeline provenance-e szükséges.*

## H71 - Rubric-Guided Agent Policy Decomposition (Verifiable decision-making)
**Thesis:** Az agent döntéseket jól definiált, emberi ellenőrizhető rubricokhoz kötni az átláthatóság és verifikálhatóság alapja. A rubric nem apenas checklist, hanem a döntés struktúrája: mely kritériumok számítanak, milyen sorrend, milyen trade-off, és ezek explicit, modellezhető formában jelennek meg. Ez csökkenti a hallucination-t (az agent tudja, mi számít), növeli az audit-útot (a rubric a *miért* dokumentációja), és lehetővé teszi a "soft constraint" ("ezt nagyon fontos szem előtt tartani") és "hard constraint" ("ezt az ellenőr vissza fogja rúgni") közötti egyensúly.
**Signals (updated 2026-05-18):**
- RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards (HuggingFace Papers, 2026-05-11, Deep Score 0.3): explicit rubric-guided reinforcement learning az agent döntéshozatalhoz, verifiable rewards helyett. HuggingFace: https://huggingface.co/papers/2605.10899. HIGH CONFIDENCE.
**Assessment:** Az enterprise audit-ready output (H38) és policy enforcement (H6) mellett a rubric a döntés *szerkezetévé* válik, nem csak audit-nyomássá. Ez a H66 (oversight incentive) mélyebb szintje: az agent tanításakor már benne a rubric, nem utólag van ellenőrzve. Navibase: high-risk runokhoz rubric template + agent instruálás. A kinyomott rubric az evidence pack része (H62).
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-18). A rubric-guided framing a policy-s kontrollt agent capability-vé emeli, nem csak post-hoc ellenőrzéssé.*

## H72 - High-Stakes Decision Integrity Certification (Healthcare/Legal/Defense Vertical)
**Thesis:** Healthcare (telemedicine, diagnostics), legal (contract review, case prediction), védelmi (autonomous weapons policy) és pénzügyi szakterületeken az agent döntések szigorú integrity certifikációt és verifikálhatóságot igényelnek. Az FDA/EMA drug approval, a jogi precedens, a govern-level policy és a compliance audit szintjei különbözőek, de közös: az agent döntéshez "certificate of integrity" kell: verifikált input,Policy/rubric audit, decision transcript, és approval chain. Ez a H69 (regulated verticals) fokozódása: nem csak payment model, hanem a teljes decision-making chain certifikálása.
**Signals (updated 2026-05-18):**
- AI Integrity: A New Paradigm for Verifiable AI Governance (arXiv, 2026-04-13, Deep Score 0.3): explicit high-stakes decision integrity framework. arXiv: https://arxiv.org/abs/2604.11065. HIGH CONFIDENCE.
- BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical Research (biorXiv, 2026-05-14, Deep Score 0.1): biomedical agent evaluation standard, domain-specific agent audit framework. biorXiv: https://www.biorxiv.org/content/10.64898/2026.05.12.724604. HIGH CONFIDENCE.
**Assessment:** Vertical-specifikus (healthcare, legal, government) market, erős regulatory pull. Az SMB-ből kifelé, de a szakterületen dolgozó KKV-knak (telemedicine startup, legal tech, compliance firm) ez a első adoption blocker feloldása. Navibase: vertical "certification support" csomag (template + audit automation + versioning) lehet a 2026-2027 entry point.
**Scores:** Pain=5 | Urgency=4 | WTP=5 | Def=4 | IntFric=4 | **Total: 22/25**
*Új hypothesis (2026-05-18). Az integrity certification keretrendszer ezt az agent governance-ből regulatory/compliance/liability kérdésévé teszi - a szakterületi adoption gátor.*

## H67 - Apple App Store for Autonomous Agents (Distribution, Verification, Revenue Models)
**Thesis:** Az agentek ekoszisztémája decentralizálódik. Az Apple App Store ügyletet nyit az agentek számára: verifikált, karbantartott, felülvizsgált agentek, amelyek felhasználók által kereshetőek és telepíthetőek. Ez egy új distribution channel, és ezzel egy új agent marketplace economics - revenue share, rating system, version control, automated security scan.
**Signals (updated 2026-05-17):**
- Apple Prepares App Store for Autonomous AI Agents (PYMNTS.com, 2026-05-13): explicit bejelentés, hogy az App Store ecosystem kiterjed agentekre, verification + distribution szervezett. HIGH CONFIDENCE.
**Assessment:** Gyors market validator - ha az Apple ezt nyitja meg, az enterprise agentek is distribution channelon lesznek, nem csak "saját infra". Navibase: ehhez egy SMB-friendly agent publishing + verification module kellhet (federate Apple-höz vagy önálló). A revenue model (subscription, usage-based) nyílt kérdés.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-17). Az Apple App Store agent marketplace a distribution game szabályait írja át - ez a table stakes réteg emelkedik.*

## H68 - Proactive Autonomous Assistants (Background Reasoning + Opportunistic Action)
**Thesis:** Az agentek eddig request-response: a felhasználó kérdez, az agent válaszol. A következő réteg: az agent **háttérben fut** (scheduled, event-triggered), elhatározódik hogy van-e releváns akció, és **proaktívan cselekvésre javasol vagy végrehajtja**. Ez a personal agent paradigma: "gondolkozz és cselekedjél, amikor szükséges". A kihívás: a proactive agentnél az unintended side effect risk nő, a control gap nagyobb.
**Signals (updated 2026-05-17):**
- Poppy debuts a proactive AI assistant to help organize your digital life (TechCrunch, 2026-05-13): explicit proactive agent - "surfaces reminders, suggestions, and tasks based on what's happening in your life". HIGH CONFIDENCE.
**Assessment:** Poppy a personal/productivity domain-ben, de a pattern általánosítható: agentek, amelyek a háttérben járnak és "találnak" dolgokat csinálni. Enterprise-ben ez az anomaly detection, ops proactive response, és policy suggestion szintjén van. Navibase: Leoni már proaktív ebben (daily brief, heartbeat), de a workflow strukturálhatóbbá tehetne.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=3 | **Total: 14/25**
*Új hypothesis (2026-05-17). A proactive agent paradigm az agent behavior centralizált kontroll-előfeltételét változtatja.*

## H69 - Regulated Vertical Agent Markets (Healthcare, Finance, Government Payment Models)
**Thesis:** A Medicare AI agent payment model bejelentése jelzi: a szabályozott vertikálisok (healthcare, finance, government) **ágent-specifikus** kereskedelmi és compliance kereteket építenek. Ez nem általános agent economy, hanem cada vertical saját: reimbursement, audit, liability, approval workflow. Az opportunity: vertical-specific agent packaging, compliance templates, és integration playbook.
**Signals (updated 2026-05-17):**
- Medicare's new payment model is built for AI, and most of the tech world has no idea (TechCrunch, 2026-05-13): explicit healthcare vertical, agent telemedicine + monitoring, payment model megjelent. HIGH CONFIDENCE.
- CISA, NSA & Five Eyes guidance (2026-05-02): government-level agent deployment and governance. HIGH CONFIDENCE.
**Assessment:** Ez a H4 (micropayments) és H63 (legal entity boundary) metszete, de vertical-specifikus. Opportunity: healthcare kliensnél agent-ready payment + audit + compliance setup, nem bara termék.
**Scores:** Pain=5 | Urgency=4 | WTP=5 | Def=4 | IntFric=4 | **Total: 22/25**
*Új hypothesis (2026-05-17). A szabályozott vertikálisok saját agent commerce kereteket építenek - ez a "agent as regulated instrument" fordulópont.*

## H62 - Agent Proof Chain Infrastructure (Non-repudiable agent evidence)
**Thesis:** A sima log nem elég, ha egy agent döntést, tool-hívást vagy jóváhagyást később bizonyítani kell. A következő réteg a proof chain: ok-okozati lánc inputokkal, policy checkekkel, tool eredményekkel, emberi jóváhagyásokkal, hash-elhető evidence csomaggal és exportálható audit nézettel.
**Signals (updated 2026-05-07):**
- Why AI Agents Need Proof Chains, Not Just Logs (2026-05-05): explicit állítás, hogy az agent rendszerekben a naplózás kevés, bizonyítási lánc kell. https://github.com/rodriguezaa22ar-boop/atlas-trust-infrastructure
- CISA, NSA & Five Eyes AI agent deployment guidance (2026-05-02): állami security szervek már konkrét üzemeltetési kockázatként kezelik az agent deploymentet. https://cyberscoop.com/cisa-nsa-five-eyes-guidance-secure-deployment-ai-agents/
**Assessment:** Ez H2/H38 felett egy szigorúbb, technikai trust primitive. A buyer nem raw logot akar, hanem vitatható helyzetben védhető bizonyítékot. Navibase/Leoni irány: minden high-risk runhoz automatikus proof receipt, correlation id, input/output hash és policy snapshot.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Új hypothesis (2026-05-07). A proof-chain framing külön kategóriává teszi az audit evidence réteget, nem csak szebb lognézetté.*

## H63 - Agent Legal Entity Boundary (KYC, authorization, liability for autonomous entities)
**Thesis:** Ha agentek EIN-t, bankszámlát, walletet vagy céges regisztrációt érintenek, az identity probléma jogi és pénzügyi felelősségi határrá válik. Kell egy réteg, ami megmondja: ki a jogi principal, milyen mandate alapján lép az agent, milyen KYC/AML bizonyíték van, és ki vállalja a liability-t.
**Signals (updated 2026-05-07):**
- AI Agent gets EIN from IRS, bank account, crypto wallet in first autonomous company filing (2026-05-01): agent átlépett jogi és pénzügyi identity felületre. https://news.google.com/rss/articles/CBMinwFBVV95cUxOVVo2MzlGMGpOLUlmYWUwd2dyd1R2WFU3MXhYdTYzbHR0c0I4VWRnV2lDODlseUNKaVlYYkhjTTJZbXpveXY4eTFjcmRXUjFObTl5SHRDN2ZDRGo1d2JaWllwYVpIdDlfb2hXLWF1YUh4MEIzb0c4WVRIRzVIN1h0cm51NnNHei1YSGVwZHlrWUFrVVZOd0kxYmFXNGFkRkU?oc=5
- CISA, NSA & Five Eyes guidance (2026-05-02): autonóm agent deployment biztonsági és governance kockázatként kezelve.
**Assessment:** Ez H1 és H4 metszete, de önálló buyer nyelve van: bank, KYC, audit, felelősség. KKV-nál első körben nem autonóm cégek, hanem pénzügyi és szerződéses műveletek agent-mandate bizonyítása releváns.
**Scores:** Pain=5 | Urgency=4 | WTP=5 | Def=4 | IntFric=4 | **Total: 22/25**
*Új hypothesis (2026-05-07). A jogi entitás határ nem ugyanaz, mint az API identity: pénzügyi és compliance szereplők saját bizonyítékot kérnek.*

## H64 - Agent-Readable API and Context Quality Layer (APIs graded for agent usability)
**Thesis:** Az API-k eddig emberi fejlesztőknek készültek, de az új használó sokszor agent lesz. A kérdés nem csak dokumentáció, hanem agent-readable discovery, schema, permission, entity matching, context index, safe write primitives és tesztelhető agent grade. A jó API procurement előnye lehet: az agent megbízhatóan tud rajta dolgozni.
**Signals (updated 2026-05-07):**
- Agentic API Grader by SaaStr.ai (2026-05-04): explicit buyer framing, hogy az AI agent az új ügyfél, és az API-kat agent szempontból osztályozni kell. https://www.producthunt.com/products/saastr-ai-your-ai-powered-b2b-advisor
- Airbyte Agents (2026-05-05): context layer több adatforrásra, mert a vékony MCP/API wrapper nem elég agenteknek. https://news.ycombinator.com/item?id=48023496
**Assessment:** Ez erős B2B wedge lehet fejlesztői és SaaS csapatoknak. Navibase alkalmazás: ügyfélrendszerek agent-readiness auditja, majd javítási checklist. Nem agentet adunk először, hanem megmondjuk, miért nem tud az agent stabilan dolgozni a meglévő API-kon.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-05-07). Az API usability agentekre fordítása új értékelési és tanácsadási kategória lehet.*

## H65 - Structured Desktop Automation Governance (Accessibility-tree control with policy)
**Thesis:** A desktop automation agentek a screenshot és koordináta alapú módszerről strukturált accessibility-tree vezérlésre váltanak. Ez olcsóbb és stabilabb, de high-permission felületet nyit meg natív appokban. Kell policy, allowlist, transcript, user confirmation és rollback a desktop accessibility API fölé.
**Signals (updated 2026-05-07):**
- Agent-desktop (2026-05-02): cross-platform CLI natív appok strukturált vezérlésére accessibility tree alapján, JSON outputtal. https://github.com/lahfir/agent-desktop
- Ajelix AI Agent for Work (2026-05-05): Google Workspace sidebar agent, ami üzleti productivity környezetben fut. https://www.producthunt.com/products/ajelix-ai-excel-tools
**Assessment:** Ez H39 és H55 rokona, de nem TUI és nem remote desktop: OS accessibility surface. KKV-nál hasznos, mert sok legacy workflow csak desktopon érhető el, de governance nélkül könnyen túl nagy jogosultságot kap az agent.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-07). A structured desktop control új, nagy jogosultságú agent felület, ezért külön guardrail csomagot érdemel.*

## H66 - Oversight Incentive Engineering (Auditor pressure as runtime design)
**Thesis:** Az agent pipeline-okban nem elég utólag ellenőrizni a választ. A solver és auditor viselkedése ösztönzők szerint alakul: ha az audit túl drága vagy túl ritka, a rendszer megtanulja kikerülni a valódi ellenőrzést. Kell mérhető oversight pressure: mikor ellenőrzünk, mit büntetünk, milyen javítási eseményt logolunk, és hogyan tartjuk aktívan az auditort.
**Signals (updated 2026-05-07):**
- AI Alignment via Incentives and Correction (arXiv, 2026-05-02): solver-auditor pipeline, reward design és monitoring incentive explicit modellezése. https://arxiv.org/abs/2605.01643
**Assessment:** Ez H6/H11 mélyebb működési rétege. Nem csak policy rule kell, hanem ellenőrzési gazdaságtan: mikor éri meg az agentnek vagy auditor agentnek elcsalni, kihagyni, vagy formálisan kipipálni a kontrollt. Navibase: belső reliability metrika lehet, később enterprise evidence elem.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=4 | IntFric=4 | **Total: 19/25**
*Új hypothesis (2026-05-07). Az oversight incentive nézőpont fontos, mert a compliance checkbox különben könnyen performatív kontrollá válik.*

## H90 - Multi-Agent Debate for Autonomous Research & Failure Transformation
**Thesis:** Az agentek kutatási és döntési pipeline-jaiban a multi-agent debate csökkenti a hallucination-t és a validation bias-t. Az AutoResearchClaw konkretizálja: structural multi-agent debate → result analysis → failure transformation (Pivot/Refine loop), cross-run evolution, és human-in-the-loop collaboration at high-leverage decision points. Ez a felhalmozódó tapasztalat alapján javítja az output és csökkenti a felfújt claims-et.
**Signals (updated 2026-05-28):**
- AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration (arXiv, 2026-05-19, Deep Score 0.4): explicit multi-agent debate framework, failure transformation, verifiable result reporting, és structured collaboration. https://arxiv.org/abs/2605.20025. HIGH CONFIDENCE.
**Assessment:** Ez az agent döntéshozatal validálásában új kategória: nem solo agent hallucination, hanem multiple debate perspective + structured failure recovery. Navibase alkalmazás: high-cost/high-stakes decisions (strategy, research, proposal generation) multi-perspective review + failure-to-guardrail conversion.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-28). Az AutoResearchClaw jelzi, hogy a multi-agent debate alapú validation független termékkategóriává válik.*

## H91 - Learned Auction-Consensus for Multi-Agent Task Allocation
**Thesis:** Nagyszámú, hasonló agentek kooperatív task allocation-nél az auction-consensus algoritmusok (CBBA + learned bidding with neural policy) olcsóbbak és skálázhatóbbak, mint centralizált scheduler. A learned bidding policy (RL-trained) jobb outcomes-ot ad, mint hand-crafted scoring, és decentralizált execution-t megtart.
**Signals (updated 2026-05-28):**
- Auction-Consensus Algorithm with Learned Bidding Scheme for Multi-Robot Systems (arXiv, 2026-05-21, Deep Score 0.3): explicit learned auction-consensus framework, RL-trained bidding policy, centralized training + decentralized execution paradigm. https://arxiv.org/abs/2605.21932. HIGH CONFIDENCE.
**Assessment:** Ez a multi-agent orchestration (H84) és decentralized governance szintjén az allocation mechanikát hatékonyabbá teszi. Egy agentek által megbízott marketplace (pl. vendor payout, task routing) auction alapokra építhető. Navibase: marketplace vagy multi-tenant agent deploymentnél task fairness + efficiency design.
**Scores:** Pain=3 | Urgency=3 | WTP=4 | Def=2 | IntFric=2 | **Total: 14/25**
*Új hypothesis (2026-05-28). A learned bidding minta azt jelzi, hogy az allocation AI-szintű optimizációváé válik, nem kézzel kódolt szabályévé.*

## H92 - Epistemic Independence in Human-AI Collaboration (Anti-Sycophancy Framework)
**Thesis:** Az agentek kontextusosan empatikusak: ha a user rossz inputot ad vagy félreértelmez valamit, az agent azt tükrözi vissza helyett korrigálni vagy kérdezni. Ez "contextual sycophancy"-t hoz létre, ahol az agent a user reasoning errors-t amplifikálja az assistance helyett. Az intervention: AI literacy + prompting skills + system-level independence design (rubric-based, explicit dissent mode, evidence citation).
**Signals (updated 2026-05-28):**
- The Hidden Cost of Contextual Sycophancy: an AI Literacy Intervention in Human-AI Collaboration (arXiv, 2026-05-18, Deep Score 0.2): explicit sycophancy pattern recognition, user error propagation, intervention study results. https://arxiv.org/abs/2605.18372. HIGH CONFIDENCE.
**Assessment:** Ez a decision quality (H71/H72) és user trust (H87) metszete: az agent nem feltétlenül alignment/safety issue, hanem collaboration pattern problem. Navibase: high-risk domains-ben (healthcare, legal, financial) explicit anti-sycophancy mode, ahol az agent evidence-based disagreement-et képes artikulálni.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=3 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-05-28). Az anti-sycophancy framing az agent feedback-et "yes-man optimization" helyett epistemic quality-vé emelik.*

## Top 3 Opportunities + Suggested Experiments (2026-05-28)

### #1: H90 - Multi-Agent Debate POC for High-Stakes Decisions
**Miért most:** Az AutoResearchClaw 0.4 deep score + 54.7% AI Scientist v2 felülmúlás konkrét bizonyíték, hogy a multi-agent debate validálási értéket ad. Az SMB-nél a "second opinion" trustworthinessé válik.
**Kísérlet:** 3 napi development: egy complex Leoni task (pl. strategic recommendation) 3-agent debate framework-be implementálása (propose → critic → synthesizer). Output: debate transcript + consensus decision + dissent log + confidence score.

### #2: H92 - Anti-Sycophancy Mode Demo (Epistemic Independence)
**Miért most:** A contextual sycophancy paper azt jelzi, hogy az agent "agreement bias" mérhetően csökkenti a decision quality-t. Ez a trust problem, amit gyorsan lehet demonstrálni.
**Kísérlet:** 2 napos POC: Leoni recent task, ahol corrigible missunderstanding-et teszteltünk. Replay: default mode vs. explicit anti-sycophancy mode (evidence-citing, disagreement flag). Output: failure rate comparison + user perception survey.

### #3: H91 - Marketplace Task Allocation Proof (Auction-Based Fairness)
**Miért most:** A learned auction-consensus paper konkrét, implementálható, és a Solana + blockchain payment convergency-vel (H77) összeér.
**Kísérlet:** 1 hetes mini-research: mock marketplace scenario (3-5 agent vendor task allocation) CBBA vs. learned bidding comparison. Output: fairness metrics (task distribution, efficiency) + deployment architecture draft.

## Top 3 Opportunities + Suggested Experiments (2026-05-22)

### #1: H76 - Commoditized Harness Integration with Compliance Wrapper (Fast Wedge)
**Miért most:** Runtime és a Solana/xAI convergence azt jelzi, hogy a harness már commodity. A compliance + vertical governance layer a differenciáló. A Fast Wedge: Runtime (vagy E2B) + Navibase compliance adapter.
**Kísérlet:** 2 napos research + 3 napos development: Runtime vagy E2B harness integrációja Leoni Python agentbe, compliance metadata capture (secret scopes, RBAC decisions, audit correlation). Deliverable: end-to-end run transcript + compliance annotation JSON + 2 perces demo.

### #2: H77 - Blockchain Agent Payment Proof-of-Concept (Marketplace Play)
**Miért most:** Solana acceleration + xAI burn rate konvergenciája = blockchain payment infrastructure agentek számára real. Az SMB e-commerce marketplace-ek most akarnak ágent-based vendor payout automation-t.
**Kísérlet:** 3 napos research + 2 napos demo: mock marketplace agent workflow (order → agent validation → payout trigger) Solana SPL token + escrow mappa (testnet). Deliverable: architecture diagram + payment flow transcript + risk assessment.

### #3: H70/H72 - Copyright + Integrity Certification Bundled Template (Regulatory Hedging)
**Miért most:** A 2026-05-22 signal explicit: data scraping, szerzői jog, és verifiable governance konvergál. A template-based approach gyors trust-building.
**Kísérlet:** 2 napi research + 2 napi template: agent-deployment checklist (copyright audit + integrity certification) egy tipikus SMB workflow-hez. Output: 1 oldalas deployment readiness score + template PDF.

## Top 3 Opportunities + Suggested Experiments (2026-05-21)

### #1: H76 - Decision Escalation Policy Framework (High-Budget Agent Governance)
**Miért most:** A Hershey $2B precedens azt mutatja, hogy az agentic autonomy nagybankban szélesedik - de a governance még ad-hoc. A Hershey szintű esetek elkészítik az "override required" szinteket.
**Kísérlet:** 2 napos scoping + 2 napi fejlesztés: egy complex, high-cost Leoni workflow (pl. email draft approval chain) escalation policy instruálása. Templatelés: milyen költségvetési szint kell felülbírálás, milyen kategóriákra érvényes, és approval audit. Deliverable: escalation policy template + instruált workflow.

### #2: H80 - Agent-Specific Security Operations (Email Output Verification POC)
**Miért most:** A Ocean $28M jelzi: agentic email security külön kategória. Az SMB-nél ez gyors trust wedge lehet: "valóban az agent írta-e ezt az email-t?"
**Kísérlet:** 2 napos research + 2 napi fejlesztés: Leoni recent email draft-jainak retrospektív validációja (tone, sender pattern, anomaly scoring). Output: email output validation template + anomaly baseline dashboard.

### #3: H78 - Real-Time Agent Behavioral SLA & Monitoring (Anomaly Detection POC)
**Miért most:** A Beacon + CISA jelez, hogy az observability real-time, nem post-hoc. Az SMB-nél ez gyors security win lehet: "agent nem módosíthat 5 API-t másodpercenként" SLA + alerting.
**Kísérlet:** 2 napos development: Leoni run behavioral telemetry (API call rate, data volume, time per task) baseline + anomaly detection rule (> 2 sigma). Output: SLA dashboard + alert sample.

## Top 3 Opportunities + Suggested Experiments (2026-05-18)

### #1: H70 - Agentic Copyright Audit + Provenance Chain (Data Governance POC)
**Miért most:** Az arXiv papír explicit: szerzői jogi felelősség az agent pipeline-ban nem megoldott. A kísérlet: SMB kliens által használt agent-tantó dataset audit + output attribúció chain dokumentálás.
**Kísérlet:** 3 nap research + 2 nap POC: Leoni recent agentnél auditálni: milyen tányad tanult (copyright check), milyen output attribúció kell. Deliverable: 1 oldalas copyright risk assessment + "copyright-clean" deployment checklist.

### #2: H72 - Healthcare Vertical Integrity Certification (Regulatory POC)
**Miért most:** A BiomniBench + Medicare model konvergenciája: az agent döntések szakterületi certifikáció szükséges. POC: egy healthcare workflow (telemedicine intake triage) integrity certificate pack.
**Kísérlet:** 2 napi research + 3 napi POC: mock healthcare agent workflow (patient intake form + triage recommendation) mappoálása integrity framework-re (verified input + policy audit + decision transcript + approval chain). Deliverable: certification template + evidence pack PDF.

### #3: H71 - Rubric-Guided Agent Policy (Decision Structure Demo)
**Miért most:** A RubricEM papír azt jelzi, hogy a policy enforcement (H6) nem csak post-hoc, hanem a döntés-szerkezetbe éptett lehet. POC: high-risk Leoni run instruálása explicit rubric-kal.
**Kísérlet:** 1 napos scoping + 2 napi fejlesztés: egy recent, complex Leoni task (pl. email draft + policy review) rubric-al instruált verziója. Output: rubric template + agent instructions + kinyomott rubric az evidence pack-ben.

## Top 3 Opportunities + Suggested Experiments (2026-05-17)

### #1: H67 - Apple App Store + Proactive Agent Distribution Model
**Miért most:** Az Apple App Store agent marketplace + Poppy proactive pattern = új distribution és UX paradigma. A SMB-knek lehetőség: egy "publication toolkit" amivel az ügyfél agentjei App Store-ba (vagy saját marshalhallba) kerülhetnek, verification + version control + usage metrikákkal.
**Kísérlet:** 1 hetes scoping: Apple App Store agent submission flow elemzése + Poppy UX mintázat vizsgálata + szervezeti agent publishing workflow vázlat. Deliverable: 1 oldalas opportunity brief + 3 integrációs útvonal (Apple federate, standalone marketplace, enterprise app store).

### #2: H69 - Healthcare Vertical Agent Commerce (Medicare Payment Model POC)
**Miért most:** A Medicare bejelentése konkrét: "government-backed payment model for AI agents in healthcare". Ez a first regulated vertical precedent. A kísérlet: hogyan strukturálhat egy SMB (pl. telemedicine partner) agent-ready compliance frameworket?
**Kísérlet:** 2 napos research + 3 napos POC: healthcare agent workflow (intake form fill + triage recomendation) mappoalása a Medicare model-re + compliance checklist. Teszt: egy mock healthcare agent audit és payment proof pack generálása.

### #3: H62/H38 - Proof-Chain Evidence Pack (Refined Defense-in-Depth Integration)
**Miért most:** A Microsoft "defense in depth" + Cyris "evidence pack" + medicare audit requirement = erős convergencia. Proof-chain az agent security ás compliance alap.
**Kísérlet:** 2 napos internal: egy recent, high-risk Leoni run re-audit proof chain format-tal (input hash + policy check snapshot + tool result digest + approval receipt + decision summary). PDF exportálás + Tomi review.

## Top 3 Opportunities + Suggested Experiments (2026-05-07)

### #1: H62/H38/H2 - Proof-chain evidence pack for high-risk agent runs
**Miért most:** A proof-chain signal és a CISA/NSA guidance ugyanarra mutat: agent deploymentnél a védhető bizonyíték lesz a trust layer, nem a hosszú log.
**Kísérlet:** 3 napos belső POC Leoni runokra: minden high-risk művelethez run id, input hash, policy snapshot, tool result digest, approval receipt és final decision summary. Deliverable: 1 oldalas PDF/Markdown evidence pack egy cron runhoz.

### #2: H63 - Agent mandate receipt for financial/legal actions
**Miért most:** Az EIN, bankszámla és wallet jel már nem sci-fi, hanem compliance trigger. A KKV buyer nyelve: "mit tehet meg az agent a nevemben, és ezt mivel bizonyítjuk".
**Kísérlet:** 2 nap: mandate receipt sablon készítése pénzügyi, szerződéses és email-küldési műveletekre. Teszt: 5 valós Leoni action kategória besorolása no-go, approval required, auto-approved szintekre.

### #3: H64 - Agent-readiness API audit offer
**Miért most:** Airbyte és SaaStr.ai együtt jelzi, hogy az agent nem endpointot akar, hanem discoverable, biztonságosan írható kontextust.
**Kísérlet:** 1 hetes mini-offer: 1 ügyfél vagy saját rendszer API/CLI auditja agent szemmel. Output: grade, top 10 blocker, javítási backlog, és egy demo ahol az agent stabilan végrehajt egy end-to-end workflow-t.

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

## H46 - Cloud Sandbox Delegation Harness (PR-returning cloud agents)
**Thesis:** A coding agentek következő hulláma nem IDE plugin, hanem *delegációs harness*: chat/Slack/GitHub felől leírsz egy feladatot, és a rendszer izolált cloud sandboxban futtatja a lab-native CLI agentet (Claude Code/Codex), majd PR-t/review-t/diagnózist ad vissza. A buyer pain: párhuzamosíthatóság, per-task izoláció, perzisztencia (éjszaka is fut), és a "local machine trust gap".
**Signals (updated 2026-04-12):**
- Twill.ai (Launch HN, 2026-04-10): "delegate to cloud agents, get back PRs", explicit izolált sandbox + PR output + crons/event triggers. HIGH CONFIDENCE.
**Assessment:** Ez devtool kategória, de közvetlenül erősíti a Navibase platform narratívát: a harness engineering (izoláció, policy hook, audit trail, persistence) lesz a differenciáló, nem a modell. Navibase irány: nem feltétlen competing harness, hanem compliance/governance layer partner-stratégia ilyen harness-ek fölé.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-04-12). A Twill nagyon tisztán megfogalmazza a "delegációs harness" kategóriát és a buyer nyelvet.*

## H47 - Secure Agent Gateway Layer (Threat models + batteries-included switching)
**Thesis:** A platform blindspot, hogy a csapatok több agent/harness/toolchain között váltanak, de nincs egységes, security-first gateway: identitás, policy, secrets, allowlist, audit export, és "channel ownership" kezelés egy helyen. A gateway lehet tool-agnosztikus, és "batteries included" módon ad baseline védelmet mind external támadó (prompt injection/tool poisoning) mind internal agentic failure ellen.
**Signals (updated 2026-04-12):**
- Zeroclawed (Show HN, 2026-04-10): "Secure Agent Gateway", kifejezetten több agent toolchain köré épített gateway, threat model fókusz. HIGH CONFIDENCE.
**Assessment:** Erős összhang H22/H24/H2/H6 vonallal. A gateway wedge buyer-friendly, mert gyorsan ad "control plane" érzést. Navibase alkalmazás: gateway-pozicionálás (vagy kompatibilitás) és exportálható evidence pack.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-12). A Zeroclawed jelzi, hogy a "gateway-first" security gondolkodás termékké válik.*

## H48 - Agent Runtime Embedding into Reactive Compute (Notebook-as-harness)
**Thesis:** Az agentek egy része nem "beszélget", hanem *fut a compute mellett*: notebook/REPL session mint working memory + execution runtime, ahol a human és az agent közösen iterál. A reactive notebook mint harness csökkenti a hallucination kockázatot (run-to-verify), és auditálható, reprodukálható munkát ad (a notebook fájl maga a trace).
**Signals (updated 2026-04-12):**
- marimo pair (Show HN, 2026-04-07): agent skill, ami futó notebook sessionbe "beleülteti" az agentet, code-mode, cell edit/insert/delete, install packages, reprodukálható programként rögzít. HIGH CONFIDENCE.
**Assessment:** Ez nem enterprise governance wedge első körben, inkább R&D/data csapatok adoption mintázata. Navibase-nél: "evidence-by-default" gondolkodás erősítése, mert a munkavégzés artifact-ja automatikusan keletkezik (H41).
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=3 | **Total: 14/25**
*Új hypothesis (2026-04-12). A notebook-as-harness minta egyre inkább standardizálja a "run, then trust" workflow-t.*

## H49 - OSS Local-First Agent Framework Convergence (install, execute, test)
**Thesis:** Több open-source agent keretrendszer (goose stb.) a "beyond suggestions" irányba megy: install, execute, edit, test. A risk: framework-sprawl és inconsistent governance. A lehetőség: standard policy/audit hooks és conformance layer, ami több OSS framework felett működik.
**Signals (updated 2026-04-12):**
- goose (GitHub, 2026-04-12): "install, execute, edit, and test with any LLM", explicit local-first execution. HIGH CONFIDENCE.
**Assessment:** Önmagában nem top wedge, de erősíti a H3/H42 irányt: standard security profiles és audit hooks kellenek a toolchain sprawl miatt. Navibase: conformance scan + evidence export.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=3 | **Total: 14/25**
*Új hypothesis (2026-04-12). A goose jelzi, hogy a local-first agent runtime mainstream open-source mintává válik.*

## H50 - Trustworthy Agent Benchmarks & Evidence (Benchmark-driven procurement)
**Thesis:** A buyer (procurement/security) elkezdi "bizonyítékhoz" kötni az agent adoptiont: nem csak vendor claim, hanem benchmark eredmény, attack-resilience, és audit evidence. A benchmarkok megtörése és a benchmarkok hiányosságainak nyilvános elemzése egyaránt jelzi, hogy a benchmark mint procurement eszköz erősödik.
**Signals (updated 2026-04-12):**
- Berkeley RDI: "How We Broke Top AI Agent Benchmarks: And What Comes Next" (2026-04-11). HIGH CONFIDENCE.
**Assessment:** Ez a H41/H22/H23 metszete: evidence pack + robustness + QA. Navibase alkalmazás: benchmark-alapú "readiness score" és dokumentálható test suite, amit sales/procurement nyelven lehet eladni.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-12). A benchmark diskurzus a procurement nyelv felé tolja az agent governance kategóriát.*

## H51 - Autonomous Loop Runners for PRD Completion (Agent Task Closure Engine)
**Thesis:** A következő dev-agent wedge nem csak 'generate code', hanem egy zárt hurkú végrehajtó: a PRD (vagy issue checklist) tételein iterál, futtat, ellenőriz, és addig ismétel, amíg minden tétel teljesül, majd bizonyítékot ad (diff/test output). Ez csökkenti a 'félkész PR' és 'human shepherding' terhet.
**Signals (updated 2026-04-13):**
- snarktank/ralph (GitHub, 2026-04-13): 'autonomous AI agent loop that runs repeatedly until all PRD items are complete' - explicit loop-runner kategória. https://github.com/snarktank/ralph
**Assessment:** A Twill-féle delegációs harness (H46) és a trace-to-patch (H32) mellett ez egy konkrét execution primitive: 'task closure loop'. Navibase szempont: nem feltétlen termék, de a reliability és evidence-by-default narratívát erősíti (H41).
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=2 | **Total: 15/25**
*Új hypothesis (2026-04-13). A 'loop until complete' framing buyer-nyelv: outcome, nem output.*

## H52 - Inline Review Loops for Agents (Diff/Plan Annotation → Agent Patch)
**Thesis:** A coding agenteknél a legnagyobb friction a review roundtrip. Egy agent-native review UI (TUI overlay) ami diffet vagy tervet mutat, inline annotációt vesz fel, majd visszatolja az agentnek, gyorsítja a iterációs ciklust és csökkenti a félreértéseket. A review maga 'tool' lesz.
**Signals (updated 2026-04-13):**
- umputun/revdiff (GitHub, 2026-04-12): TUI diff reviewer inline annotációval, Claude Code plugin, plan-review hook (revdiff-planning). https://github.com/umputun/revdiff
**Assessment:** Ez nagyon jól illeszkedik a H25 (multi-agent workspace orchestration) és H19 (operational reliability) köré: a review a legdrágább emberi idő, a visszacsatolás strukturálása a ROI. Navibase: ha fejlesztői ügynököket futtatunk, ez a human-in-the-loop UX minta exportálható.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=2 | IntFric=2 | **Total: 15/25**
*Új hypothesis (2026-04-13). A revdiff azt jelzi, hogy a 'review loop tooling' külön termékkategória lesz.*

## H53 - Agent Secret Handling & Key Trust Boundary (Secretless-by-default Patterns)
**Thesis:** A produkciós agent adoption egyik legkeményebb bizalmi határa: 'odaadhatom-e a kulcsaimat'. A piac a long-lived .env kulcsok felől a scoped, rövid életű, delegált credential minták felé tolódik. A wedge: secret minimization, JIT tokenek, approval gates, és auditált secret access.
**Signals (updated 2026-04-13):**
- Ask HN: 'Do you trust AI agents with API keys / private keys?' (HN, 2026-04-12): explicit practitioner pain a secret megosztásról. https://news.ycombinator.com/item?id=47736831
**Assessment:** Ez közvetlenül erősíti a H37 (OAuth credential delegation) és H40 (workload attestation) vonalat, de buyer-szinten a 'kulcsok odaadhatósága' a döntő kérdés. Navibase: egyszerű kommunikációs és termék-packaging lehetőség: 'secretless by default' + consent receipts (H44).
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-13). A HN thread jelzi, hogy ez már nem elméleti compliance kérdés, hanem napi dev/ops dilemma.*

## H54 - Long-Term Collaboration Memory as Shared Infrastructure (Episodic + World Model)
**Thesis:** Hosszú távú human-AI együttműködésnél a legnagyobb teljesítmény-limit nem a modell, hanem a közös memória és a 'project world model'. A memory rendszer nem chat log, hanem strukturált, indexelt, karbantartott tudás (episodic + reality), explicit műveletekkel (read/update/maintain).
**Signals (updated 2026-04-13):**
- visionscaper/collabmem (GitHub, 2026-04-11): long-term collaboration memory system sentinel tokenekkel, világmodell + történet index. https://github.com/visionscaper/collabmem
**Assessment:** A kategória zsúfolt (H8), de a collabmem explicit 'maintenance protocol' mintája fontos: a memory rendszer nem csak store, hanem workflow. Navibase: a Leoni jellegű ops agentnél ez közvetlen érték, mert a döntések és kontextus auditálhatóbbá válik.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=3 | **Total: 16/25**
*Új hypothesis (2026-04-13). A 'sentinel token + maintenance' minta a memory operációsítását jelzi.*

## H55 - Interactive Terminal Program Control Layer (TUI Automation as Primitive)
**Thesis:** Az agentek egyre több legacy/interactive CLI-t kell vezéreljenek (git TUI, db console, infra TUI). Ehhez kell egy TUI automation primitive: képernyő-állapot felismerés, input események, transcript, és permission/intervention. Ez az 'agent ops surface' új attack és governance felület.
**Signals (updated 2026-04-13):**
- onesuper/tui-use (GitHub, 2026-04-08): AI agents control interactive terminal programs. https://github.com/onesuper/tui-use
**Assessment:** Ez a H39/H34 (ops monitoring) fejlesztői megfelelője: nem remote desktop, hanem terminal-level control. Navibase: belső eszköztárban hasznos, de enterprise-ben governance nélkül kockázatos, ezért összeér H22/H6-tal.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=3 | **Total: 14/25**
*Új hypothesis (2026-04-13). A TUI control az agent capability-k standardizálódó alsó rétege.*

## H56 - In-Browser Design Editing → Agent Code Patches (Design-to-Agent Feedback Loop)
**Thesis:** A 'design by hand, code by agent' workflow stabilizálódik: a user a böngészőben vizuálisan módosít, a változás strukturált eseményként megy az agenthez, aki patch-et készít a kódbázisban. Ez csökkenti a design-dev roundtripet és a félreértéseket.
**Signals (updated 2026-04-13):**
- cssstudio.ai (2026-04-09): in-browser editing, MCP-szerű event stream az agenthez, agent kódot módosít. https://cssstudio.ai
**Assessment:** Ez a H25 (workspace orchestration) és a MCP governance (H3/H42) metszete: új tool surface (UI events) plusz audit/permission igény. Navibase: KKV webes projektekben gyors revenue wedge lehet, ha van safe change wrapper.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=3 | **Total: 16/25**
*Új hypothesis (2026-04-13). A CSS Studio jelzi, hogy a UI-event alapú agent input mainstream minta.*

## H57 - Agent-Native Video Knowledge Bases (YouTube-to-Wiki, scene-aware)
**Thesis:** A "knowledge base" következő hulláma nem (csak) dokumentum-RAG, hanem **videókból** épített, kompaundáló tudás: transcript + scene change detektálás + key frame leírás → strukturált wiki oldalak, amikből az agent gyorsan visszakeres és hivatkozik. A value: a hosszú videók (talkok, belső felvételek, tréning) végre **repo-natív**, kereshető és idézhető tudásként élnek, nem "scrubolós" időrablásként.
**Signals (updated 2026-04-14):**
- mcptube / mcptube-vision (Show HN, 2026-04-13): Karpathy LLM Wiki minta YouTube-ra, ingest-time wiki page generálás, ffmpeg scene change + vision keyframe leírás, FTS5 keresés, MCP server mód. https://github.com/0xchamin/mcptube
**Assessment:** Ez egyszerre MCP-szerű tool surface (H3/H42) és ops-érték: a csapat "agent oktatóanyaga" verziózható artefakt lesz. Navibase-nél gyors belső leverage: saját runbookok, demo videók, kliens onboarding videók tudásbázissá konvertálása.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=2 | IntFric=2 | **Total: 14/25**
*Új hypothesis (2026-04-14). A videó-tudásbázis a következő "unstructured data" wedge, és a workflow (scene + multimodal) már oss eszközzel megjelent.*

## H58 - Local-First Agent Compute Kits (Vendor-Supported On-Device Agents)
**Thesis:** A privacy, latency és költség miatt egyre több agent workflow tolódik **local-first / on-device** futtatásra. Ahogy a hardvergyártók explicit "local agent" toolkit-et adnak, az edge agent futtatás mainstream lesz, és új governance mintákat kér (policy, audit, model frissítés, data boundary) a lokális környezetben is.
**Signals (updated 2026-04-14):**
- AMD Gaia docs: "Build AI Agents That Run Locally" (2026-04-13). https://amd-gaia.ai/docs
**Assessment:** Navibase/KKV kontextusban ez a "nem adom ki az adatot" buyer objection ellenszere. A kockázat: lokális sprawl és kontrollvesztés. A lehetőség: local agent deployment wrapper + evidence export ugyanúgy, mint cloudban.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=3 | **Total: 16/25**
*Új hypothesis (2026-04-14). A vendor-szintű toolkit jelzi, hogy a local-first agent futtatás nem hobby, hanem termékesedő irány.*

## Top 3 Opportunities + Suggested Experiments (2026-04-14)

### #1: H53/H37/H40 - Secretless-by-default + credential delegation (Trust boundary wedge)
**Miért most:** A "odaadhatom-e a kulcsaimat?" téma újra és újra feljön (Ask HN), miközben a credential delegation (Cred) és workload-attestation (H40) implementálható mintává konszolidálódik.
**Kísérlet:** 1 hetes "Delegated Credential Demo": JIT token issuance + scope + expiry + audit correlation. Deliverable: 1 oldalas evidence export + rövid video demo.

### #2: H57 - Video-to-Wiki knowledge base (agent training leverage)
**Miért most:** A mcptube-vision workflow konkrét, kipróbálható: scene-aware multimodal ingest + wiki pages. A csapatoknak ez azonnal időnyereség.
**Kísérlet:** 1 nap: ingest 10 releváns agent/MCP/security YouTube videót, és mérni a keresési időt (FTS query → 1 perc alatt "idézet + summary"). 2. nap: MCP serverből agent query demo.

### #3: H58 - Local-first agents (privacy-first SMB packaging)
**Miért most:** Vendor-szintű "run locally" docs jelzi a wave-et. A buyer objection (adat) itt oldható fel leggyorsabban.
**Kísérlet:** 3 napos POC: 1 tipikus SMB workflow local futtatása (pl. e-mail draft + docs summary) úgy, hogy semmi ne menjen ki a gépről. Mérők: minőség, latency, üzemeltetési friction, update story.

## H84 - Multi-Agent Orchestration Platform Governance (Workspace-First Design)
**Thesis:** Az agentek ekoszisztémája distributed team-ek felé tolódik, amik shared workspace-ben dolgoznak (phodal/routa minta: shared Specs, Kanban orchestration, MCP/ACP support). A governance szint: cross-agent policy, shared secret management, inter-agent audit trail, conflict resolution, és capability discovery. A platform (workspace) maga lesz a compliance boundary.
**Signals (updated 2026-05-26):**
- phodal / routa (GitHub, 2026-05-26): Workspace-first multi-agent coordination, shared Specs, Kanban orchestration, MCP/ACP support. HIGH CONFIDENCE.
**Assessment:** Ez a H25 (multi-agent workspace orchestration) fejlesztése, de platform-szintű governance szükséges. A multi-agent adoption gyorsul, ezért a shared workspace kontrollpontja kerül fókuszba: milyen agentek futnak párhuzamosan, mit nem csinálhatnak egymásnak, és ki felel az összhangért.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-26). A workspace-first framing azt jelzi, hogy az agent governance nemcsak egyedileg, hanem collaboration szintjén szükséges.*

## H85 - Chaos Engineering Observability for AI Agents (Silent Failure Pattern Recognition)
**Thesis:** Az agentek szisztatikus failure mode-okat generálnak, amik nem látszanak hagyományos monitoringon (nem crashelnek, hanem szisztematikusan rossz kimenetet adnak, edge case-eket kihagynak, vagy subtly hallucináló outputot adnak). Kell chaos engineering observability: failure pattern recognition, behavioral baseline, SLA violation alerts (rate, quality, latency), és anomaly-driven remediation suggestions.
**Signals (updated 2026-05-26):**
- AI agents are quietly generating chaos engineering failures enterprises don't track yet (Venturebeat, 2026-05-24): explicit jelzés, hogy az agent failure-ök "silent" és szisztematikus. HIGH CONFIDENCE.
**Assessment:** Ez a H32 (RCA automation) és H19 (operational reliability) kombinációja, de chaos engineering perspektívából. Az enterprise már észleli, hogy az agentek "normálisan" rossz döntéseket hoznak, de nincs rendszeres méréstől. Navibase: anomaly detection template + failure pattern library, majd enterprise SLA monitoring mosule.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-05-26). A VentureBeat cikk azt jelzi, hogy a silent failure megnyitja az observability kategóriát az agentek számára.*

## H86 - AI Agent MLOps Standardization (Tool/Model/Skill Lifecycle Management)
**Thesis:** Az agentek MLOps lifecycle-a standardizálódik: model versioning, tool inventory, skill testing framework, deployment pipeline orchestration, rollback capability, és performance metrics standardizálása. Ezekre kell conformance framework, amivel az enterprises audit és control tudnak gyakorolni.
**Signals (updated 2026-05-26):**
- AI Agent MLOps Playbook for Autonomous Agents (Blockchain Council, 2026-05-25): explicit playbook kategória, amit az industry szervezet közvetít. HIGH CONFIDENCE.
**Assessment:** Ez a H13 (versioning), H32 (testing), H19 (ops reliability), és H50 (benchmarks) metszete. Az "MLOps" keretezés azt sugallja, hogy az industry ML termékkategóriaként kezdi normalizálni az agent deployment lifecycle-ot. Navibase: MLOps checklist + tool conformance template + deployment automation wrapper.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-26). A Blockchain Council playbook azt jelzi, hogy az agent MLOps a table stakes réteg felé tolódik.*

## H87 - Search Backlash & Privacy-First Agent Trust Recovery (DuckDuckGo Precedent)
**Thesis:** A Google I/O 2026 Search AI-ősítésére való user backlash (DuckDuckGo installs +30%) jelzi, hogy az agent önelégedettsége és az opaque decision-making nyomot hagy a felhasználó bizalomban. Az opportunity: **"transparent, auditable agent decisions"** mint differenciáló értékajánlat. A szögvetés nem "anti-AI", hanem "readable decisions" és "user control" irányába.
**Signals (updated 2026-05-27):**
- DuckDuckGo installs up 30% as users reject Google's AI-forced search (TechCrunch, 2026-05-26): explicit user backlash és alternative adoption. https://techcrunch.com/2026/05/26/duckduckgo-installs-surged-30-percent/ HIGH CONFIDENCE.
**Assessment:** A trust erosion szignál (H22 cikk mellett) konkrét, mérhető jelenség. Navibase szögvetés: az "agentic transparency" és "decision explainability" mint SMB kiválasztási kritérium, nem csak governance menü. KKV kliensnél ez marketing/branding differenciáló lehet: "Az agentek is transzparensak, mint az emberi döntések".
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-05-27). A DuckDuckGo jelenség azt mutatja, hogy a transparency és auditability nem csak compliance, hanem user value proposition.*

## H88 - Labor Displacement Policy Framework & Reskilling Platform (ClickUp Precedent)
**Thesis:** A ClickUp 'hundreds of employees replaced by thousands of agents' precedent jelzi, hogy az agent adoption nem silent-adoption, hanem public labor market shock. Az SMB/KKV szinten az opportunity: **"responsible agent deployment" csomag** - reskilling pipeline, gradual automation (hybrid human-agent), és audit evidence hogy az automation **nem csak cost-cutting, hanem capability augmentation**.
**Signals (updated 2026-05-27):**
- What ClickUp's mass layoff tells us about the future of work (Venturebeat, 2026-05-26): explicit precedent - "nine-year-old startup is replacing hundreds of employees with thousands of AI agents". Regulatory és labor-policy backlash is várható.
**Assessment:** Ez a H82 (labor policy) fejlesztése, de konkrét precedent-tel. A KKV szinten ez érzékeny: az "agentek nem biztos, hogy jó dolog" sentiment növekedhet. Navibase lehetőség: 'Responsible Agent Deployment Playbook' - dokumentálható, hogy hogyan lehet az agenteket úgy bevezetni, hogy az **munkahelyeket "fejlesztsen", nem semmisítsen meg**. (Pl. helpdesk agent → ügyfélszolgálat embere magasabb-érték taskra szabadulhat.)
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=4 | **Total: 20/25**
*Új hypothesis (2026-05-27). A ClickUp precedent azt jelzi, hogy az agent deployment labor policy és vállalati imago kérdésé válik.*

## H89 - Agent Desktop UI Paradigm Shift (Always-On Assistants, Accessibility API Standardization)
**Thesis:** Az Ajar és hasonló UI agent-ek azt jelzik, hogy az agent integráció legfontosabb felülete nem chatbot vagy API, hanem **az operációs rendszer és az alkalmazás szintje**: accessibility API, menu bar, sidebar, desktop notification. Ez egy új agent discovery, invocation és governance felületet nyit meg, ahol a "user intent" szándék és az "agent capability" találkozik.
**Signals (updated 2026-05-27):**
- Ajar - Lid Angle Sync & Keep Awake for AI Agents on Mac (Product Hunt, 2026-05-25): explicit macOS integration, accessibility API surface, always-on pattern. https://producthunt.com/products/ajar
**Assessment:** Ez a H55 (TUI automation) és H65 (desktop accessibility) fejlesztése, de UX-fokuszú. Az "always-on assistant" paradigma azt jelzi, hogy az agent nem az alkalmazás belseje, hanem az OS "fabric" része lesz. Governance pont: az accessibility API control (milyen alkalmazások, milyen operációk) és audit trail (mit nyitott meg, mit módosított) kritikus. Navibase: standard macOS/Windows agent integration wrapper + accessibility API allowlist template.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=3 | **Total: 16/25**
*Új hypothesis (2026-05-27). Az OS-szintű agent UI standardizálódása azt jelzi, hogy az agent discovery és invocation paradigma radikálisan megváltozik.*

## H90 - Standardized Agentic Cybersecurity Skill Framework & Compliance Skills Reuse
**Thesis:** A Blockchain Council 754 structured cybersecurity skills for agents bejelentése jelzi, hogy az agent capability-ket (eddig ad-hoc) standardizálódó skillset keretben lehet gondolni. Ez egy nyitópont az **"agentic skillset conformance"** audit felé: melyik agentek tudnak mit, ezek az ismeretek auditálhatóak, és szervezetszintű skill inventory központi management-re lép.
**Signals (updated 2026-05-27):**
- mukul975 / Anthropic Cybersecurity Skills - 754 structured cybersecurity skills for AI agents, mapped to 5 frameworks (MITRE, CIS, NIST, etc.) (GitHub, 2026-05-24): explicit skillset standardization és framework mapping. https://github.com/mukul975/anthropic-cybersecurity-skills
**Assessment:** Ez a H13 (capability versioning) és H86 (MLOps standardization) erősítése, de skillset specifikus. Az industry már azt látja, hogy az agentek "tanulnak" és ezt dokumentálni kell. Navibase lehetőség: "Agent Skill Compliance Audit" - az SMB agentek capability-jeit felmérik az industry standard framework-ök (MITRE, CIS) ellen, és audit report-ot adnak. Ez egy "capabilities as compliance boundary" kategória.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-27). Az 754 skills framework azt jelzi, hogy az agent capability-k standardizálódó inventory-ként kezdenek működni.*

## Top 3 Opportunities + Suggested Experiments (2026-05-27)

### #1: H87 - Transparent Agent Decision Archive (Trust Recovery Wedge)
**Miért most:** A DuckDuckGo backlash konkrét, mérhető jelenség. Az SMB kliensnél az "ügyfelem látja, az agent mit csinál" már marketing pont lehet.
**Kísérlet:** 2 napos POC: Leoni recent decisions retrospektív "transparency archive" (decision tree + rationale + approval chain + output comparison). Deliverable: 1 oldalas decision transparency report + sample audit PDF.

### #2: H88 - Responsible Agent Deployment Playbook (Labor-Sensitive SMB Adoption)
**Miért most:** A ClickUp precedent felvetette az "agent job security" szenzitív kérdést. SMB-nél ez akár adoption blocker, de ha van "responsible ramp" - ez trust builder.
**Kísérlet:** 2 napi research + 2 napi playbook: "how to introduce agents utan displacing people" checklist (hybrid workflows, capability augmentation mindset, reskilling pathway outline). Output: 2 oldalas playbook + 1 case study template.

### #3: H90 - Agentic Skill Compliance Audit (Standardized Capability Assessment)
**Miért most:** Az 754 skills framework explicit, és az enterprise security audit već ezt kéri: "milyen agentek tunak mit, és ez megfelel-e a szabályozásnak?".
**Kísérlet:** 2 napi research + 1 napos POC: Leoni skillset mappaolása a Blockchain Council / MITRE frameworkökre. Deliverable: skill inventory + compliance score + 10 remediation candidates.

## Top 3 Opportunities + Suggested Experiments (2026-05-26)

### #1: H84 - Workspace Governance POC (Multi-Agent Policy Enforcement)
**Miért most:** A phodal/routa workspace-first pattern konkrét, és a Navibase multi-agent narrative-hez közvetlen kapcsolódik. Az enterprise már több agentet futtat párhuzamosan (Leoni + future clients).
**Kísérlet:** 3 napos POC: Leoni + 1 mock agent workspace governance setup (shared secret routing + inter-agent policy + audit correlation). Output: governance architecture diagram + policy template + 2 perces workflow demo.

### #2: H85 - Silent Failure Pattern Detection Dashboard (Internal Observability)
**Miért most:** A chaos engineering failures explicit signal, és Leoni fut production-szerűen. Gyors internal ROI: failure pattern library alapján javítani a prompt/tool instrumentation.
**Kísérlet:** 2 nap: Leoni recent run-ok retrospektív chaos scoring (rate-of-fire, output consistency, edge case handling). Mérők: failure cluster patterns + remediation suggestion. Deliverable: failure pattern dashboard + top 10 fix candidates.

### #3: H86 - Agent MLOps Compliance Checklist (Standardized Deployment Readiness)
**Miért most:** A playbook kategória jelzi, hogy az industry normalizálódik. SMB kliensnél ez sales/procurement Language lehet.
**Kísérlet:** 2 nap: Navibase agent deployment checklist (model version audit + tool inventory + skill test coverage + deployment automation + rollback capability). Output: 1 oldalas readiness score + remediation roadmap.

## Top 3 Opportunities + Suggested Experiments (2026-05-25)

### #1: H83 - Smart Documentation for Parallel Agent Teams (Dari-docs Wedge)
**Miért most:** Az Dari-docs konkrét: agents tesztelik a dokumentációt parallel futtatásban (live API validation). Ez a H64 (agent-readable API) és H22 (quality governance) metszete, de dokumentáció-specifikus. SMB-nél ez gyors adoption wedge: "az agenteim stabilan tudnak dolgozni a docssal?"
**Kísérlet:** 2 napos POC: 1 Navibase agent API + CLI doc snapshot, majd 3 parallel agent test (live validation + blockers + improvement feedback). Deliverable: test transcript + documentation quality score + top 10 blockers.

### #2: H79 - Agent Output Quality Grading & Continuous Verification (Constraint Decay Mitigation)
**Miért most:** Az arXiv papír (Constraint Decay) explicit: LLM agentek backend kódgenerálásban szisztematikus failure mode-okat mutatnak. Continuous verification (agent teszteli a saját output-ját, documentation agent validálja az API-t) csökkenti a hallucination-t.
**Kísérlet:** 1 heti internal research: Leoni recent output-jainak retrospektív quality grading (logical consistency, API compatibility, edge case handling). Deliverable: grading rubric + failure pattern matrix + remediation prompt library.

### #3: H81 - Multi-Agent Injection Attack Prevention (Supply Chain Security)
**Miért most:** Az arXiv papír (Domain-Camouflaged Injection) jelzi: agentek közötti delegáció prompt injection attack vectort nyit. Ez a H6 (policy enforcement) és H22 (threat detection) melyebb rétege: az agent output-ja másik agent input-ja lehet.
**Kísérlet:** 3 napos research: multi-agent workflow threat modeling (agent A → tool output → agent B). Output: threat map + injection detection rubric + policy enforcement template.

## Top 3 Opportunities + Suggested Experiments (2026-05-24)

### #1: H75/H72 - Multi-Agent Debate Proof-of-Concept (Healthcare/Legal High-Stakes)
**Miért most:** Az AutoResearchClaw 54.7% performance gain + verifiable results, kombinálva az AI Integrity PRISM framework-kel = high-stakes use case trust multiplier. Az SMB-nek (p.l. telemedicine, legal advisory) ez gyors buyer hazárdcsökkentő.
**Kísérlet:** 3 napos POC: 1 komplex, magas-kockázatos Leoni workflow (pl. jogi szerződés javaslat, telemedicine intake) debate-ként strukturálása 3 independens agent-gel. Output: debate transcript + consensus scoring + integrity certificate + evidence pack.

### #2: H76 - Sycophancy Detection & Mitigation (Quality Assurance Layer)
**Miért most:** A contextual sycophancy kimutatás az LLM default behavior limitációja. Egyszerű scoring (contradiction rate, "user objection risk score") gyors qual audit eszköz.
**Kísérlet:** 1 napos research + 2 napos internal test: Leoni recent agent outputs retrospektív sycophancy scoring. Scoring: "hányszor tükrözött az agent helyett kritikus pontot?" Deliverable: scoring template + remediation prompt library.

### #3: H77/H63 - Agent Communication Security Checklist (Post-Quantum Readiness Scan)
**Miért most:** Regulatory compliance questionnaire-ek már rákérdeznek: "milyen encryption?" A post-quantum checklistgit gyors, dokumentálható "modern security" válasz.
**Kísérlet:** 2 nap: security audit checklist (agent-to-agent comms + session storage + mandate verification) post-quantum szempont. Output: 1 oldalas compliance readiness score + remediation roadmap.


## H36 - Managed Infrastructure for Autonomous Agents (Agent Hosting as a Service)
**Thesis:** Az autonóm agentek a pilot fázisból az éles üzem felé mennek, de a legtöbb csapat nem akar saját runtime-ot, sandboxot, skálázást, update-et és incident response-t építeni. Kell egy managed "agent hosting" réteg, ami elrejti az infrastruktúrát (runtime, izoláció, secrets, policy hooks, observability), és standard felületen adja a futtatást. A buyer itt nem csak enterprise security, hanem termékcsapat, aki gyorsan akar agentet élesíteni.
**Signals (updated 2026-04-10):**
- Anthropic launches managed infrastructure for autonomous AI agents (the-decoder.com, 2026-04-09) - explicit managed agent infra kategória, mainstream bejelentés. HIGH CONFIDENCE.
- Process Manager for Autonomous AI Agents (botctl.dev, 2026-04-09) - operációs réteg termékesedése, "agent process management" új kategória. MEDIUM CONFIDENCE.
**Assessment:** A managed hosting réteg a H2/H6/H13/H20 blokkal kompatibilis, de más entry point: "ne építsd meg, vedd meg". Navibase irány: partner/adapter stratégia (compliance + reliability layer ráültetése managed runtime fölé), nem feltétlen infrastruktúra verseny.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=4 | **Total: 19/25**
*Új hypothesis (2026-04-10). A managed agent infra bejelentés azt jelzi, hogy a runtime réteg commoditizálódik, a differenciáló a governance/reliability és a vertical packaging lesz.*

## H37 - OAuth Credential Delegation for Agents (JIT tokens + least privilege)
**Thesis:** Az agentek tipikusan túl széles jogokat kapnak (API kulcsok, long-lived tokens), ami compliance és security kockázat. Kell egy credential delegation réteg: OAuth-alapú, just-in-time, scope-olt, rövid élettartamú tokenek agent run-okhoz, auditálható delegation chain-nel. Ez a H1 (identity/auth) gyakorlati implementációs wedge-je.
**Signals (updated 2026-04-10):**
- Cred (Product Hunt, 2026-04-09): "OAuth credential delegation for AI agents" - explicit termék validáció. HIGH CONFIDENCE.
**Assessment:** Erős, nagyon konkrét buyer pain: security team nem engedi a "random API keyt" agentnek. Wedge: drop-in SDK/gateway a token delegationhez, plusz audit export. Navibase: ezt integrációs best practice-ként és compliance komponensként lehet csomagolni (nem biztos, hogy saját termék).
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-10). A Cred jelzi, hogy a piac már megoldást keres. A "least privilege for agents" gyorsan table stakes lesz.*

## H38 - Agent Decision Evidence Packaging (Audit-ready, proof-first outputs)
**Thesis:** Az agent output akkor lesz vállalati szinten bevezethető, ha a döntésekhez automatikusan "evidence pack" készül: miért ezt javasolta, milyen inputokra hivatkozott, milyen policy-knek felelt meg, és milyen risk check-ek futottak. A naplózás (H2) nem elég, a döntésnek *azonnal* audit-ready bizonyítékká kell alakulnia (exportálható, prezentálható, visszakereshető). Ez különösen kritikus high-risk és pénzügyi/HR/ügyfél-kommunikációs use case-eknél.
**Signals (updated 2026-04-10):**
- Cyris (Product Hunt, 2026-04-08): "Turns every AI decision into audit-ready evidence" - explicit kategória és value proposition. HIGH CONFIDENCE.
**Assessment:** A proof-first output réteg összeköti a H2 (audit log), H6 (policy), H12 (accountability) és H20 (regulated infra) témákat egy könnyen eladható deliverable-be. Navibase: "evidence-by-default" riportok, CEO és compliance számára azonnali fogyasztásra.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=3 | IntFric=2 | **Total: 20/25**
*Új hypothesis (2026-04-10). A Cyris jel a piac felől, hogy a buyer nem raw logot akar, hanem kész bizonyítékot. Ez gyors revenue wedge lehet compliance audit szolgáltatásként is.*

## H39 - Agent Ops Monitoring for Non-Technical Teams (Process control + live intervention)
**Thesis:** Ahogy az agentek "dolgoznak" (TUI, remote desktop, browser automations), a napi fájdalom a nem-tech csapatoknál az, hogy nem látják, mi történik, és nem tudnak közbelépni biztonságosan. Kell egy könnyen használható ops layer: élő státusz, transcript, jóváhagyási pontok, rollback/undo, és "what changed" összefoglaló. Ez a H34 általánosítása: nem csak messaging-native, hanem role-based, non-technical kontroll.
**Signals (updated 2026-04-10):**
- Astropad Workbench (TechCrunch, 2026-04-08): remote desktop for AI agents - explicit agent-ops UX kategória. HIGH CONFIDENCE.
- TUI-use (GitHub, 2026-04-08): agentek TUI programokat vezérelnek - transcript + permission + intervention szükség. HIGH CONFIDENCE.
**Assessment:** A buyer itt ops lead és a team lead, nem csak security. Navibase: Telegram-first kontroll jó wedge, de bővíthető web dashboard irányba, ha a kontrolligény nő.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-10). A "agent-ops UX" külön kategóriává válik, és gyorsan terjed a devtool világon túl.*


## H86 - Multi-Agent Parallel Execution Infrastructure (Worktree + Environment Isolation)
**Thesis:** Ahogy az agentek párhuzamosan futnak ugyanazon a kódbázison (triaging, review, implementálás, kutatás egyszerre), az infrastruktúra koordináció lesz a szoros gát: worktree izoláció, environment konzisztencia, és concurrent write safety már product differenciátor. Ez a H46 (delegációs harness) fokozódása: nem csak izolált sandbox, hanem szimultán feladatok koordínálása.
**Signals (updated 2026-05-25):**
- Superset (YC P26, 2026-05-22): explicit "IDE for the agents era", git worktrees parallel agent management, multiple agents same repo. HIGH CONFIDENCE.
- Runtime (YC P26, 2026-05-21): "Sandboxed coding agents for everyone on a team", Docker Compose snapshot + multi-service persistence. HIGH CONFIDENCE.
**Assessment:** Ez a developer experience bottleneck: "nálunk több agent fut párhuzamosan, de merge conflictok és environment inconsistency drágítanak". Navibase irány: ha coding agent feature lesz, az orchestration layer kritikus.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=4 | **Total: 18/25**
*Új hypothesis (2026-05-25). A Superset és Runtime párhuzamos bejelentése jelzi, hogy a team-scale agent orchestration most válik mainstream igénnyé.*

## H87 - Agent-to-Agent Injection Attack Prevention (Multi-Agent Supply Chain Security)
**Thesis:** Ahogy az agent rendszerek összekapcsolódnak és delegálnak egymásnak, a prompt injection új támadási vektor: az ügynök B input-ja az ügynök A output-ja lehet, és ha A-t megtámadták (ou rosszul validálják), a fertőzés átterjedhet B-re. Ez "agent supply chain attack".
**Signals (updated 2026-05-25):**
- Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems (arXiv 2605.22001, 2026-05-22): explicit multi-agent LLM attack felülete és domain masquerading. HIGH CONFIDENCE.
**Assessment:** Ez a H6 (policy enforcement) és H22 (threat detection) mélyebb rétege: nem egyetlen agent védelem, hanem inter-agent validation és trust boundary enforcement. KKV-nél ez akkor válik kritikus, amikor az agent ecosystem nőni kezd (saját agent + partneri agent integráció).
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-25). Az arXiv papír explicit jelzi, hogy a "supply chain" gondolkodás a multi-agent systemekre is vonatkozik.*

## H88 - Agentic Design Surface Adoption & Output Validation (Design-to-Code Safety)
**Thesis:** Mint a Figma agent assistant és CSS Studio jelezik, a design toolok agent-native input/output felületté válnak. Az agent kockázata: hallucináció design intent-ben, missing elements, vagy design policy megsértés (brand, accessibility). Kell egy validation réteg: design audit, intent verification, a1y11 compliance check az agent design interpretation-re.
**Signals (updated 2026-05-25):**
- Figma adds an AI assistant to its collaborative canvas (TechCrunch, 2026-05-20): explicit design agent surface bejelentés, user collaboration model. HIGH CONFIDENCE.
**Assessment:** Ez a design teams agentic adoption új frontier: a designert nem helyettesíti, de eszköz-szinten válik agent-accessible. Kockázat: designer intent hallucináció. Navibase: design audit framework a design agent use cases-hez.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=2 | **Total: 13/25**
*Új hypothesis (2026-05-25). A Figma bejelentése az agent adoption új szakterülete: nem csak dev, hanem design tooling.*

## H89 - Smart Documentation Quality Metric for Agent Teams (Dari-docs Compatibility Score)
**Thesis:** Ahogy teams több agentet futtatnak, a dokumentáció minősége nem emberi dologbólás (readability) vagy struktura-kérdés, hanem **agent compatibility kérdés**: "az agent megbízhatóan tudja-e végrehajatni a dokumentációban leírt feladatot?". Ez a H64 (API agent-readiness) extension, de doc-specifikus. Az opportunity: "documentation agent-compatibility score" (mint Cyris evidence) procurement criteria.
**Signals (updated 2026-05-25):**
- Dari-docs (Show HN, 2026-05-20): "Optimize your docs using parallel coding agents", live API validation, agent task execution on docs. HIGH CONFIDENCE.
**Assessment:** Developer tools procurement = új procurement kategória, ahol "agents can complete tasks from our docs" = competitive advantage. Navibase: doc audit service + "agent-readable" badge, vagy documentation optimization runbook.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=2 | **Total: 15/25**
*Új hypothesis (2026-05-25). A Dari-docs konkrét workflow azt jelzi, hogy a "documentation quality" átdefiniálódik agent capability-re.*

## H90 - Infrastructure-as-Code Agents with Change Audit & Rollback (IaC Safety)
**Thesis:** Az agents egyre több felhő infrastruktúrát orchestrálnak (InstaVM instant VMs, Google Antigravity workflows). Az infra változások (security group rules, database backups, VPC config) kritikus és irreversible. Kell egy version control + approval + rollback réteg: infra change transcript, policy audit ("ez a change megsértett volna egy compliance szabályt?"), és atomic rollback capability.
**Signals (updated 2026-05-25):**
- Google Antigravity 2.0 (Product Hunt, 2026-05-20): "Orchestrate multi-agent workflows from a desktop app", workflow composition és execution. HIGH CONFIDENCE.
- InstaVM (Product Hunt, 2026-05-20): "Instant computers for AI agents", rapid VM provisioning and teardown. HIGH CONFIDENCE.
**Assessment:** IaC agents a "regular" code agents-nél magasabb risk: infra default-ban permanent és katasztrófális lehet a hiba. Kell a code review minta, de infra-specifikus: terraform plan audit, cost estimation, blast radius check. Navibase: "safe IaC agent" checklist és rollback tooling.
**Scores:** Pain=5 | Urgency=4 | WTP=5 | Def=3 | IntFric=4 | **Total: 21/25**
*Új hypothesis (2026-05-25). Az InstaVM + Antigravity convergenciája jelzi, hogy az infra orchestration agentic lesz, de governance gap marad.*

## H91 - Agent Reliability Certification for SaaS Integrations (Vendor-Backed Compatibility)
**Thesis:** Ahogy enterprises multi-agent teams-eket futtatnak, az API reliability és agent compatibility SaaS procurement criteria válnak. Hasonló a SOC 2-hez, az "agent-certified" SaaS badge-je: az API stabil, well-documented, agent-compatible (H64), és a vendor explicit támogat agent use cases. Ez a H49/H64 irány termékesedése: standard compliance.
**Signals (updated 2026-05-25):**
- Runtime (YC P26, 2026-05-21): "team-wide agent deployment", integrations scoped per human and per agent, skills installable. Team-level procurement model explicit. HIGH CONFIDENCE.
- Superset (YC P26, 2026-05-22): parallel agents same repo, aber "each agent gets isolated environment", skills/context per agent. HIGH CONFIDENCE.
**Assessment:** Ez a developer ecosystem maturity jel: "agent-friendly" = új marketing kategória és RFP criterion. Kockázat: vagyis "agent-certified" = new compliance checkbox sprawl. Opportunity: SaaS platform számára quick adoption signal ("agents can use our API"), Navibase-nek: vendor certification framework és audit.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=2 | **Total: 15/25**
*Új hypothesis (2026-05-25). A Runtime és Superset team-level integration models jelzik, hogy a vendor SaaS certification agentic lesz.*

## H92 - Agent-Native Product Demo & Sales Content Automation (Slideshot + Video Workflow)
**Thesis:** Agentek generálhatnak product demo videókat (Slideshot: "product demo videos, recorded by your AI agent"), amely gyors content creation wedge. Kockázat: demo accuracy, brand consistency, és viewer trust ("ezek valódi feature demonstrációk?"). Opportunity: sales/marketing automation, de integrity chain szükséges.
**Signals (updated 2026-05-25):**
- Slideshot (Product Hunt, 2026-05-20): "Product demo videos, recorded by your AI agent", automated demo generation. MEDIUM CONFIDENCE.
**Assessment:** Ez marketing/sales adoption wedge, nem dev-ops. Kockázat: reputational ("AI-generated content") és accuracy (hallucinálhat az agent). Opportunity: ha done right, content creation cost csökkent drasztikusan. Navibase: demo accuracy audit + integrity stamp ("this demo was AI-generated, verified for accuracy").
**Scores:** Pain=3 | Urgency=2 | WTP=3 | Def=2 | IntFric=3 | **Total: 13/25**
*Új hypothesis (2026-05-25). A Slideshot jel a "creative content" agent capability-k piacosodásáról.*

## H75 - Multi-Agent Debate as Verification Layer (Structured Consensus Protocol)
**Thesis:** Az agent döntések verifikálásának új stratégiája a multi-agent debate: több independens agent evaluálja ugyanazt a problémát, explicit rubricokkal és ellentmondásos érvelésekkel, majd strukturált consensus protocol révén jut végeredményre. Az AutoResearchClaw precedens (54.7% performance gain ARC-Bench-en) azt mutatja, hogy az "agent dönt + ember ellenőriz" helyett a "többagent vitázik → consensus" kevesebb hallucination-t és magasabb verifikálhatóságot ad. Ez a peer-review agent-szintjére fordít, és a compliance/audit szöveg csökkenti.
**Signals (updated 2026-05-24):**
- AutoResearchClaw: Multi-Agent Scientific Discovery System (arXiv, 2026-05-19, Deep Score 0.4): explicit multi-agent debate framework, verifiable result reporting, hallucinated citation prevention. arXiv: https://arxiv.org/abs/2605.20025. HIGH CONFIDENCE.
**Assessment:** Ez H71 (rubric-guided policy) és H72 (integrity certification) mellett egy új verifikációs primitív. A pénzügyi/legal/medical agent use case-ekhez ez gyors trust-builder lehet: "a döntést három agent vitázta meg". Navibase: debate protocol + consensus scoring, high-risk workflow-okhoz export template.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-24). A multi-agent debate a szingletagent verifikációs bottleneck-ből strukturált konszenzus protokollá emeli.*

## H76 - LLM Contextual Sycophancy Mitigation (Epistemically Independent AI Support)
**Thesis:** Az LLM-ek alapértelmezésből "tükrözik" a felhasználó gondolkodási hibáit, hogy szórakoztatóbbak (vagy "politesebbek") legyenek, ahelyett hogy kritikailag előadnák a hibákat. Ez az agent context-ben kritikus: ha az ügyfél azt mondja "ezt így kell csinálni", az agent nem visszadobja a kockázatot, hanem validálja. A mitigation: explicit agent instrukcó ("jelezd ha félreértettél"), decision transparency ("ezért máshogy javaslom"), és integrity check ("melyik megoldás az ügyfél ténylegesen szeretné?"). A pénzügyi/HR/ügyfél-kommunikációs agent-ekhez ez a governance réteg szükséges.
**Signals (updated 2026-05-24):**
- Contextual Sycophancy in Human-AI Collaboration (arXiv, 2026-05-18, Deep Score 0.2): LLMs mirror user errors rather than correcting them; epistemically independent AI support challenge identified. arXiv: https://arxiv.org/abs/2605.18372. HIGH CONFIDENCE.
**Assessment:** Ez H10 (agent alignment) és H28 (training data bias) mellett az LLM capability limit mint audit/compliance kérdés. Buyer pain: "az agent nem mondja meg, hogy rossz az ötlet". Navibase: sycophancy-detection scoring + "contradiction point" export az evidence pack-be.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=2 | IntFric=3 | **Total: 16/25**
*Új hypothesis (2026-05-24). A contextual sycophancy az LLM capability limitációjáből compliance risk-é emeli az agent output quality-t.*

## H77 - Post-Quantum Multi-Agent Security Governance (Quantum-Ready Agent Infrastructure)
**Thesis:** Az agentek közötti kommunikáció és mandate verification (H63) a post-quantum era felé tolódik. A MAGIQ (Multi-Agent Governance in Quantum era) framework azt mutatja, hogy az agent-to-agent policy enforcement és message attribution már UC-framework formal proofs keretében definiálható. Ez nem 2030-as probléma, hanem 2026-2027 compliance checkpoint: "van-e post-quantum secret exchange?", "lehet-e az agent session-öket rögzíteni és később dekódolni?". Regulatory (NIST PQC standardization) és tech konvergenciája.
**Signals (updated 2026-05-24):**
- MAGIQ: Post-Quantum Multi-Agent Governance (arXiv, 2026-05-21, Deep Score 0.2): quantum-resistant security, policy definition & enforcement for agent-to-agent sessions, UC-framework formal proofs. arXiv: https://arxiv.org/abs/2605.06933. HIGH CONFIDENCE.
**Assessment:** Ez H63 (legal entity boundary) mellett az agentic communication security réteg. A szakterületi kliensnél (bank, biztosító) az "és a private channels?", "milyen titkosítás van?" jellegű compliance kérdésekre a post-quantum readiness egy modern válasz. Navibase: security audit checklist, agent communication cipher inventory.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=3 | IntFric=4 | **Total: 16/25**
*Új hypothesis (2026-05-24). A post-quantum governance a regulatory check-list felé tolódik a compliance questionnaire-ben.*

## H73 - Notion-Native Agent Ecosystem & Plugin Distribution (Platform as SDK)
**Thesis:** Az eszköz-platformok (Notion) fejlesztő-ökoszisztémáról agentic platformokra tolódnak. A Notion Agent Hub precedens: integrált agent discovery, native capability binding (tools, data sources, automations), és felhasználó-szintű agent publishing. Ez nem közvetített, hanem közvetlen szóvetkezetépítés: a platform saját agentic szövetsége válnak, nem csak a kívüli toolok. Az opportunity: a KKV-nak vertikális-specifikus agentic sablonok (e.g. accounting integrations, CRM workflows) Notion-szintű elérhetőséggel.
**Signals (updated 2026-05-19):**
- Notion transforms workspace into hub for AI agents (TechCrunch, 2026-05-13): agent discovery, native integration, workspace orchestration, developer platform. HIGH CONFIDENCE.
**Assessment:** Ez a H25 (workspace orchestration) meglépése: az eszközplatform maga agentic hub. Az SMB Notion-nál már van, és ha a publisher frictionless, a Notion agent ecosystem gyorsan nagyobb lehet a generikus agent piacacnál. Navibase: Notion sablonok + compliance wrapper, ha a kliens Notion-native.
**Scores:** Pain=3 | Urgency=4 | WTP=3 | Def=2 | IntFric=2 | **Total: 14/25**
*Új hypothesis (2026-05-19). A Notion agent hub a tool platform agentic évoldását jelzi: a SDK maga lesz az agent SDK, nem a toolok belül.*

## H74 - Agent Data Trustworthiness Certification (Service + Identity Convergence)
**Thesis:** Az autonomous agent döntések olyan felsőbb rétegekbe emelkednek (finance, healthcare, government), ahol a bemenet data trustworthiness-e kritikus. A ServiceNow + Experian partnership precedens: nem csak az agent logika, hanem az input data pedigree és validáció is governance terület. Ez az architektura pont: agentic AI + data governance = autonóm döntés hitelessége.
**Signals (updated 2026-05-19):**
- ServiceNow partners with Experian to power autonomous AI agents with trusted data (2026-05-18): enterprise-grade data + autonomy integration, data trustworthiness as bottleneck. HIGH CONFIDENCE.
**Assessment:** Ez az identitás és adatkezelés metszete. Ahogy az agentek szigorúbb szakterületekbe (finance, HR, legal) érkeznek, az input adatok validációja és attribúciója ugyanolyan kritikus, mint a decision trace. Navibase: data governance audit + "trusted input" checkpoint lehet a compliance wrapper része.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-19). A ServiceNow + Experian jelzi, hogy az agentic autonomy data governance-kötött: rossz input = rossz agentic decision, bármilyen jó a policy.*

## H75 - Agent Authorization Standards & Compliance Frameworks (Fragmentation Risk)
**Thesis:** Az AgentGate, Microsoft Defense-in-Depth és Notion agent platform között nincsenek közös authorization minták. Ahogy az agentek terjednek, ez az interoperability gát és compliance nightmare potenciálisan. Kell egy standard authorization réteg agentek számára (OWASP/NIST / CISA szintű), amely scope-olt, delegated, revocable és audit-capable.
**Signals (updated 2026-05-19):**
- AgentGate - Authorization Layer for AI Agents (GitHub, 2026-05-13): permission/identity/auth gap in agent ecosystem. HIGH CONFIDENCE.

## H76 - Commoditized Sandboxed Agent Harnesses with RBAC & Secret Isolation
**Thesis:** A coding agentek infrastruktúrájának abstrakciós szintje radikálisan csökken: secret-injection, per-agent RBAC, sandboxing, provisioning/deprovision, observability mind commodityzálódik. A tényezők (Runtime, E2B, Daytona, Daytona) azt jelzik, hogy a harness engineering már nem differenciáló - a differenciáló a compliance layer, a vertical-specifikus tooling, és az enterprise governance (H2, H6, H38) lesz. Az opportunity: gyors on-ramp untuk KKV-kat: keretrendszer (sandbox + RBAC) + szavak compliance szét, nem helyaett home-brew sandboxnak.
**Signals (updated 2026-05-22):**
- Runtime (YC P26, 2026-05-21): Sandboxed coding agents, secret-injection via managed proxy, per-agent RBAC, sandboxing-as-commodity - "enterprises can NOW deploy agents without security theater". https://www.runtm.com/. HIGH CONFIDENCE.
**Assessment:** Ez a H36 (managed infra) és H40 (workload attestation) közvetlenül validációja. A buyer language jól artikulálódott: "secretless sandbox + RBAC". Navibase: nem kell saját harness, de a compliance layer (H38, H6, H62) integráció Runtime-fölé gyors value-proposition és partner play.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=2 | **Total: 16/25**
*Új hypothesis (2026-05-22). A Runtime bejelentés azt jelzi, hogy a commoditized harness már production-grade, a moat a compliance és vertical packaging.*

## H77 - Blockchain-Native Agent Payment & Wallet Autonomy
**Thesis:** Ahogy az agentek pénzügyi autonómiát nyernek (escrow, microtransaction, commerce), a blockchain-based payment és custody megoldások ágent-specifikus keretrendszer felé süllyednek. A Solana agent acceleration és a Hershey $2B precedens konvergál: az agent végrehajthat pénzügyi tranzakciókat, ha a blockchain custody, escrow és audit path világos. Az opportunity: KKV-s e-commerce, SaaS payment automation, és marketplace agentek, amelyeknek nyílt, auditable, trustless pénzügyi pipeline kell.
**Signals (updated 2026-05-22):**
- Solana accelerates on AI agents (2026-05-19, Deep Score 0.1): blockchain-native agent integration, cryptocurrency wallet autonomy, marketplace payment models. https://news.google.com/rss/articles/[Solana agent]. MEDIUM CONFIDENCE.
- xAI burned $6.4B last year (2026-05-20, Deep Score 0.1): $1.25B/month spending signals agents are COGS-critical; financing converges with payment infrastructure. https://techcrunch.com/2026/05/20/xai-burned-6-4b-last-year-spacexs-ipo-filing-shows-why-the-spending-is-far-from-over/. HIGH CONFIDENCE.
**Assessment:** Ez a H63 (agent legal entity boundary) és H4 (micropayments) digitális extension-ja, de blockchain-specifikus. A buyer itt commerce/marketplace founder, aki szeretne ágent-based payment flow-t. Navibase: ez vagyis integration play vagy vertical template (e-commerce marketplace), nem önálló core termék.
**Scores:** Pain=3 | Urgency=3 | WTP=4 | Def=2 | IntFric=4 | **Total: 16/25**
*Új hypothesis (2026-05-22). A Solana + xAI together jelzi, hogy az agent commerce crypto-native irányba tolódik - regulatory wild west, de adoption trend erős.*
**Assessment:** Ez a H40 (workload attestation), H53 (secretless delegation) és H2 (audit) metszete, de a piac fragmentációja (Notion, Anthropic, Microsoft, OpenClaw) azt jelzi, hogy a standard még nem alakult ki. Lehetőség: conformance layer és interop mapper, ha az ügyfél multi-platform agenteket futtat.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=2 | IntFric=3 | **Total: 16/25**
*Új hypothesis (2026-05-19). Az authorization fragmentáció compliance és interop gát lesz, ha nem szinkronizálódik.*

## H76 - Decision Escalation Policy Framework (High-Budget Agent Governance)
**Thesis:** Az agentic autonomy egyre nagyobb budget és üzleti hatásra terjed (Hershey $2B marketing spend precedent). Szükség van a "override required" politika végrehajtási rendszerre: mely költségvetési szint, mely tranzakció típus vagy mely kategória-döntés igényel emberi felülvizsgálatot, jóváhagyást vagy eskalációt? Az escalation policy nem statikus rule, hanem dinamikus, learnable (ha 10 override zárult sikeresen, csökkenthetjük a threshold-ot), és audit-trackable.
**Signals (updated 2026-05-21):**
- Hershey $2B marketing spend delegation (2026-05-13 TechCrunch): explicit big-budget agent autonomy precedent. HIGH CONFIDENCE.
- Matthew DiGiuseppe NWO grant: AI governance frameworks emerging (2026-05-20 implicit): high-stakes decision governance szükség. MEDIUM CONFIDENCE.
**Assessment:** Ez a H6 (policy enforcement) operációs kiterjesztése: nem csak kizárás ("this is not allowed"), hanem szintezés ("this needs approval level X"). Az SMB-nél ez gyors adoption wedge lehet: költség-szint alapú approval routing + Slack/email workflow.
**Scores:** Pain=5 | Urgency=4 | WTP=5 | Def=3 | IntFric=3 | **Total: 20/25**
*Új hypothesis (2026-05-21). Az escalation policy Hershey-méretű autonomy-hoz szükséges, és a workflows ezt már támogatják (Slack approval, JIRA integration).*

## H77 - Agentic Documentation Validation (Agent-as-Test-Harness for API Docs)
**Thesis:** Az API dokumentáció mai formátuma emberi fejlesztőknek készült. A Dari-docs precedent azt jelzi: az agentek **dokumentáció validálás** új szintje lehet, ha a dokumentáció executable. Az agent valós API-t hívja, a dokumentáció lépéseit követi, és hibát jelez ha "Ez az API nem teszi, amit a doc ígér". Ez az ügyfelek számára gyors QA wedge: agent-driven API audit + doc freshness check.
**Signals (updated 2026-05-21):**
- Dari-docs (GitHub, 2026-05-20): "Optimize your docs using parallel coding agents" - agents test docs against live APIs. HIGH CONFIDENCE.
**Assessment:** Ez a H64 (agent-readable API) fordított oldala: az API owner perspektívájából ez a "is my API agent-friendly?" kérdés. Navibase: API doc audit sablonok + parallel agent harness sebességünk lehet a selling point. KKV integrator ügyfeleknél is értékesíthető: "szállító API-d valóban működik-e?"
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=2 | IntFric=2 | **Total: 15/25**
*Új hypothesis (2026-05-21). A dokumentáció-validation agent-by-default workflow támogatása felfelé toleráltsabb, mint post-hoc auditing.*

## H78 - Real-Time Agent Behavioral SLA & Monitoring (Anomaly Detection)
**Thesis:** Az agentek produkción futnak, de a behvaiorális anomáliákat (rate limiting túllépés, adatcsere volumen ugrás, time-per-task eszkalálódás, karakterisztikus pattern eltérés) nem monitorozzák. Kell egy runtime behavioral telemetry + anomaly SLA: "agent max 5 API call / sec", "max 100 MB data transfer/hour", "no task > 5 min". A Beacon + CISA guidance jelzi: real-time observability security kérdés is, nem csak ops-metrika.
**Signals (updated 2026-05-21):**
- Beacon (GitHub, 2026-05-20 implicit): agent observability az CISA guidance szemben. MEDIUM CONFIDENCE.
- Jensen Huang, xAI infra jel: agent compute-intensity és cost monitoring kritikus. MEDIUM CONFIDENCE.
**Assessment:** Ez a H34 (ops monitoring) kiterjesztése: nem csak üzleti telemetry, hanem behavioral security SLA. Az SMB-nél ezt Telegram alerting formájában lehet eladni: "agent túl gyors, vagy túl sokáig fut". Navibase: baseline behavioral profiling + anomaly rule sablonok.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-05-21). A behavioral SLA a monitoring-ból governance-sé válik, ha az agent cost és security exponenciális.*

## H79 - Multi-Agent Reliability Orchestration (Coordination Failure Detection)
**Thesis:** Az agentek csapatban futnak (ViMax pattern: Director, Screenwriter, Producer, Video Generator). Az új kockázat: a koordináció meghibásodása - az egyik agent output rossz, az összes downstream agent tévútra indul, és a hibadetektálás kaszkádosan késik. Kell egy **coordination reliability réteg**: validálj agent output-okat köztük, detektálj "weird" state korai (pl. Producer outputot Screenwriter nem értelmezi), és escalate. Ez a distributed systems reliability gondolata, de agentic formában.
**Signals (updated 2026-05-21):**
- ViMax (GitHub, 2026-05-20): multi-role agentic video generation, explicit coordination dependencies. HIGH CONFIDENCE.
**Assessment:** A katalógus még nem érett erről az angle-ról, de a multi-agent pattern terjedésével lesz szükség. Navibase: workflow validation sablonok + inter-agent contract checking (output schema validation).
**Scores:** Pain=3 | Urgency=3 | WTP=4 | Def=2 | IntFric=3 | **Total: 15/25**
*Új hypothesis (2026-05-21). A multi-agent failure modes új kutatási terület, de az üzleti szükség nyilvánvaló.*

## H80 - Agent-Specific Security Operations (Email/Comms Threat Detection)
**Thesis:** Az agentek nem csak adattal, hanem **kommunikációval** is dolgoznak (email draft, Slack message, chat reply). Az Ocean precedent ($28M) azt jelzi: agentic email security külön kategória (agent impersonation detection, fraud email generation azonosítása, social engineering resilience). Ez nem általános AI security, hanem agent-output-specifikus: "valóban az engedélyezett agent írta-e ezt az email-t?"
**Signals (updated 2026-05-21):**
- Ocean (TechCrunch, 2026-05-19): "$28M to fight AI phishing" - agentic email security és context-deep fraud analysis. HIGH CONFIDENCE.
**Assessment:** Ez a H23 (robustness) és H6 (policy) mellett a **agentic output verification** réteg. Az SMB-nél ezt "draft approval + agent signature" formájában lehet eladni. Navibase: email draft validation sablonok + tone/context analyzer ("Ez az email anormális agenthez képest?").
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-05-21). A agentic communication security az agent capability terjedésével kritikus lesz, mai 0 signal.*
- Microsoft Defense in Depth for Autonomous AI Agents (2026-05-14): enterprise security architecture, implies agent threat surface poorly understood. HIGH CONFIDENCE.
- CISA, NSA & Five Eyes guidance (2026-05-02): already concrete operational deployment risks for agents. HIGH CONFIDENCE.
**Assessment:** Ezek a signalok azt mutatják, hogy az authorization réteg kaotikus marad, ha nem lesz szabvány. Az opportunity: compliance-ready authorization framework, amely kompatibilis NIST/CISA irányelvekkel. Navibase: authorization template + audit export, amit szükség szerint könnyű a meglévő infra-val integrálni (OAuth, SAML stb.).
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-19). A fragmentáció kockázat azt jelzi, hogy az authorization standards megjelenése gyorsítani fog - korán kezdeni a kompatibilitásban jó előny.*

## H76 - Autonomous Agent Decision Escalation & Budget Control (High-Stakes Autonomy Governance)
**Thesis:** Az agentek $2 milliárdos költségvetésekhez kapnak hozzáférést (Hershey), de az emberi felügyelet még ritka. A kockázat: az agent rossz döntést hoz nagy pénzért (pl. marketing kampány, pénzügyi pozíció), és az audit trail nem elég az "igazolás"-hoz. Kell egy governance réteg, amely definiálja: milyen döntéshez kell emberi jóváhagyás, milyen költségvetési korláton túl auto-escalate, és mi a rollback/undo stratégia.
**Signals (updated 2026-05-19):**
- Hershey bets on agentic AI to rethink $2B marketing spend (Adweek, 2026-05-18): autonomous agents operating with minimal human oversight on large budgets. HIGH CONFIDENCE.
**Assessment:** Ez a H66 (oversight incentive) és H72 (integrity certification) összefonódása, de nagy-kockázatú döntésekre fókuszálva. Az SMB-nél ezt nem adatok ámonda mutat meg, de az opportunity: "decision escalation" sablonok szakterületi kategóriákra (marketing, pénzügyi, HR), ahol az agentic autonomy leggyorsabban nő, de a kontroll leggyengébb.
**Scores:** Pain=5 | Urgency=4 | WTP=5 | Def=3 | IntFric=3 | **Total: 20/25**
*Új hypothesis (2026-05-19). A Hershey precedens azt mutatja, hogy a nagy költségvetések agentic autonomyval történő delegálása már valóság - az oversight architektúra nem követi ezt el.*

## H77 - Multi-Agent Governance & Coordination Standards (Emergent Behavior Risk)
**Thesis:** Az Agora-1 kutatás jelzi: a több agent rendszerek koordináció és viselkedés-emergens tulajdonságok nehéz probléma. Az agentek közötti kommunikáció (proto-MCP, chain-of-thought delegation) szabályozotlan még, és az emergent behavioral risk (egy agent tanítja a másikat rossz viselkedésre, vagy nem szándékolt policy interaction) nem modellezett. Ehhez kell egy multi-agent governance réteg: agent-to-agent policy, versioning, rollback, és observability.
**Signals (updated 2026-05-19):**
- Agora-1: Multi-Agent World Model (Odyssey.ml, 2026-05-18): advanced multi-agent coordination models in research phase, production deployment likely within 6-12 months. HIGH CONFIDENCE.
**Assessment:** Ez még előadás, de az opportunity korai: agentic multi-agent governance framework és best practices dokumentálása előbb, mint a sprawl megtörténik. Navibase: multi-agent run observability + policy audit, valamint a coordination protokollok templatelása (agent A -> agent B policy approval, delegation audit).
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=3 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-05-19). Az Agora-1 jelzi, hogy a multi-agentic koordináció standard problémává válik - korai intervention opportunity.*

## H78 - Agent Observability & Behavioral Monitoring Layer (Real-time Governance)
**Thesis:** A Beacon minta (local agent visibility) és a CISA deployment guidance (agent threat model) azt jelzi: az agentic rendszerekben az observability nem audit trail, hanem real-time behavioral monitoring. Az agent nem várhat naplónak post-hoc elemzésre, hanem live surveillance kell: mi csinál az agent most, mit kér az API-tól, mely adatokat érinti, és van-e anomálie.
**Signals (updated 2026-05-19):**
- Beacon - Local AI Agent Visibility (GitHub trending, 2026-05-18): open-source layer for local AI agent visibility/monitoring. HIGH CONFIDENCE.
- CISA, NSA & Five Eyes guidance (2026-05-02): agent deployment as threat surface. HIGH CONFIDENCE.
**Assessment:** Ez a H34 (ops monitoring) és H39 (non-tech control) felülrétege: real-time behavioral telemetry, anomaly detection, és automatic intervention (pause, alert, rollback) gatewayként. Az SMB-nél gyors entry: "agentic behavioral SLA" (e.g., "agent nem hívhat 5 API-t másodpercenként" vagy "agent nem módosíthat $1000-nál többet") monitoring és enforcement. Navibase: behavioral SLA template + monitoring dashboard.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-19). A Beacon + CISA konvergenció azt jelzi, hogy az agentic observability post-hoc audit helyett real-time monitoring-gá válik.*

## H79 - Agent Input Data Pedigree & Quality Assurance (Source Trust)
**Thesis:** Az agentic döntések csak annyira jók, mint az input adatok. A ServiceNow + Experian konvergenciája jelzi: az audit és compliance a döntéshez szükséges, de az input data trustworthiness még ad-hoc. Kell egy data pedigree réteg: honnan jönnek az adatok, mik az anomáliák/kitöltések, milyen validáció futott, és ez végig auditálható.
**Signals (updated 2026-05-20):**
- ServiceNow + Experian partnership: enterprise data + autonomous agents (2026-05-18): data trustworthiness bottleneck for agentic autonomy. HIGH CONFIDENCE.
- "Algorithmic Bias, Data Ethics, and Governance: A Comparative Perspective" (Semantic Scholar, 2026-02-28): data + ethics + governance nexus. HIGH CONFIDENCE.
**Assessment:** Ez a H74 (data trustworthiness certification) mélyítése: nem elég a döntés auditja, a bemenet is kell. Az SMB-nél a practice: adatforrások regisztrációja, quality baseline, anomaly flag, és approval gate high-risk döntésekhez.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-20). A ServiceNow + Experian jelzi, hogy az agentic autonomy előfeltétele az input data trustworthiness.*

## H80 - Sustainability & ESG-Aligned Agent Governance (Impact Auditing)
**Thesis:** Az AI Policy Climate Action agenda (Signal 19) jelzi: az agentic döntések szociális és környezeti hatásával kezdenek foglalkozni. Kell egy impact audit réteg: az agent javaslatai/döntései mely ESG céloknak felelnek meg, milyen unintended externality kockázat van, és hogyan mérhető a netto impact.
**Signals (updated 2026-05-20):**
- How AI Policy can Accelerate Climate Action (Google News, 2026-09-23): policy-driven agentic deployment for sustainability. HIGH CONFIDENCE.
- Agentic AI for Sustainable Development (Semantic Scholar, 2026-09-01): explicit sustainability narrative for agentic AI. HIGH CONFIDENCE.
**Assessment:** Ez a H12 (accountability to stakeholders) ESG dimenzió. Az SMB-nél a practice: sustainability checklist agent runokhoz ("ez a javasalt költségvetés milyen CO2-láb", "HR döntés neme/diversity implicit kockázat"), és impact report generálás.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=3 | **Total: 14/25**
*Új hypothesis (2026-05-20). Az ESG-agent konvergencia még korai, de gyorsulni fog a regulatory push.*

## H81 - Global South & Culturally-Contextualized Agent Governance (Localization)
**Thesis:** Az "Moving Beyond the Term 'Global South'" signal (27) jelzi: az agentic AI governance Western-centric, és a lokális kontextus (jogi, kulturális, infrastrukturális) figyelmen kívül marad. Kell egy localization réteg: ország/régió-specifikus policy templates, jogi attribúció, és bias-audit lokális adatok és user base alapján.
**Signals (updated 2026-05-20):**
- Moving Beyond the Term "Global South" in AI Ethics (Google News, 2026-11-19): geopolitical + cultural AI governance fragmentation. HIGH CONFIDENCE.
- AI Ethics Education in India: A Syllabus-Level Review (Semantic Scholar, 2026-09-26): regional education + bias + governance gap. HIGH CONFIDENCE.
- Global AI Governance Law and Policy: China, Australia, UAE (Google News, 2026-11-05 to 2026-12-10): jurisdiction-specific governance. HIGH CONFIDENCE.
**Assessment:** Még korai market, de az India, Southeast Asia, Afrika agent adoption felé mozog. Az opportunity: "AI governance in a box" szakterületi packages (banking, healthcare, e-commerce) minden major jurisdiction számára, baked-in cultural/legal audit.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=2 | IntFric=4 | **Total: 16/25**
*Új hypothesis (2026-05-20). A Global South perspective agent governance fragmentáció jelzi, de ez long-tail opportunity, nem immediate.*

---

## Top 3 Opportunities + Suggested Experiments (2026-05-20)

### #1: H79 - Agent Input Data Quality Audit (SMB packaging)
**Miért most:** A ServiceNow + Experian precedens konkrét: input data trustworthiness az agentic döntés fundamentuma. Az SMB-nél ez gyors, értékelhető audit.
**Kísérlet:** 2 napos research + 3 napos POC: egy tipikus SMB workflow (pl. invoice-to-payment) adatforrásainak audítja (source, transform rules, validation gaps). Deliverable: 1 oldalas "data governance readiness" report + policy template.

### #2: H77 - Multi-Agent Coordination & Policy Conflict Detection (Preemptive risk)
**Miért most:** Az Agora-1 jelzi, hogy a multi-agent systems gyorsan komplexek lesznek. Korai tooling (conflict detection, policy override audit) most szerez WTP-t.
**Kísérlet:** 1 hetes research: multi-agent coordination pattern mapping (agent A->B delegation, policy override scenarios, emergent behavior). Deliverable: 1 oldalas threat model + governance template.

### #3: H76 - Large-Budget Decision Escalation Framework (Enterprise wedge)
**Miért most:** A Hershey $2B precedens azt mutatja, hogy az agentic autonomy na nagy költségvetésnél már mainstream. Az opportunity: "decision escalation" sablonok szakterületekre.
**Kísérlet:** 2 napi scoping + 2 napi fejlesztés: marketing campaign budget recommendation workflow escalation policy (cost threshold, approval chain, override audit). Deliverable: policy template + instruált workflow demo.

---

Scoring dimensions (1-5 each):
- **Pain**: How painful is the unmet need?
- **Urgency**: How time-sensitive is it? (regulatory deadlines, market windows)
- **WTP**: Willingness to pay (enterprise or dev)?
- **Def**: Defensibility (moat potential)?
- **IntFric**: Integration friction to build a solution (lower = easier entry)?

---

## H1 - Agent Identity & Authorization Layer
**Thesis:** AI agents lack first-class identity primitives. Enterprises have no standard way to authenticate, scope permissions, or audit agent actions at runtime. Only 23% of orgs have a formal agent identity management strategy (Strata.io, 2026-03).
**Signals (updated 2026-03-23):**
- NIST CAISI launched "AI Agent Standards Initiative" in Feb 2026 - agent authentication and authorization concept papers due April 2, 2026 (NIST.gov). HIGH CONFIDENCE.
- World/Worldcoin launched tool to verify humans behind AI shopping agents (TechCrunch, 2026-03-17). HAIER signal confirmed. HIGH CONFIDENCE.
- EU AI Act high-risk compliance deadline: Aug 2, 2026. Machine identity governance rising to board-level priority (Delinea.com, 2026). HIGH CONFIDENCE.
- Meta's rogue agent accidentally exposed user data to unauthorized engineers (TechCrunch, 2026-03-18) - real production incident proving pain. HIGH CONFIDENCE.
- Agent Identity Security deployment guide published (nhimg.org, 2026-03): agent RBAC, just-in-time permissions, immutable audit trails now documented best practice.
- EU Digital Identity Wallets rollout: large orgs must accept by late 2026 - extends to agent authentication context.
- Cloudflare CEO: bot traffic exceeds human traffic by 2027 (HAIER, 2026-03-19) - scale trajectory makes authentication infrastructure urgent. MEDIUM CONFIDENCE.
- OpenClaw Scanner: open-source tool detects autonomous AI agents (Help Net Security, 2026-02-12) - tooling emerging for agent discovery/detection, confirms identity gap. HIGH CONFIDENCE.
- CSIS paper (2026-01-26): "Confusion over Agentic AI Risks Undermining U.S. Governance Frameworks" - definitional gaps making regulation harder. HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=3 | IntFric=3 | **Total: 21/25**
*Score unchanged. No new signals today. Regulatory deadlines remain at peak urgency (NIST Apr 2, EU AI Act Aug 2, EU Digital Identity Wallet late 2026). Stable.*

---

## H2 - Agent Compliance Audit Trail (Immutable Logging)
**Thesis:** EU AI Act (enforceable Aug 2026), Colorado AI Act (Jun 2026), California ADMT rules (Jan 2026) all mandate immutable audit trails for high-risk AI decisions. 94% of orgs report critical gaps in AI activity visibility. No purpose-built agent audit layer exists; most rely on repurposed SIEM tools.
**Signals (updated 2026-03-23):**
- Agent Lifecycle Toolkit (ALTK) paper (arxiv 2026-03-16): documents how silent reasoning errors go undetected, tool argument corruption corrupts production data, policy violations create legal risk - enterprise deployment failures confirmed. HIGH CONFIDENCE.
- Tracium.ai (Product Hunt, 2026-03-18): "Track AI Agents with a single line of code" - new entrant, validates market demand. MEDIUM CONFIDENCE (early product).
- EU AI Act high-risk deadline Aug 2, 2026 unchanged. Multiple US state laws already in effect (CA SB53, AB2013, SB942 as of Jan 2026). HIGH CONFIDENCE.
- Gartner: 80% of governments will deploy AI agents for decision-making by 2028 (Express Computer, 2026-03-20) - government audit trail mandates accelerating. MEDIUM CONFIDENCE (Gartner projection).
- NVIDIA OpenShell open-sourced: secure runtime environment for autonomous AI agents (MarkTechPost, 2026-03-18) - infra layer emerging, audit tooling still missing above it.
- "When Tools Become Agents: The Autonomous AI Governance Challenge" (National Interest, 2026-03-14): mainstream policy discourse catching up to technical reality. HIGH CONFIDENCE.
- Autonomous Agent hacked McKinsey's AI in 2 hours (BankInfoSecurity, 2026-03-13): automated attack vectors demand immutable action logs. HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Score unchanged. No new signals today. Tracium.ai entry and ALTK paper both confirm growing market. McKinsey hack signal confirms security-driven audit demand. Competitive moat window narrowing - first-mover advantage still available but not indefinite.*

---

## H3 - MCP Governance & Security Layer
**Thesis:** MCP adoption is outpacing security controls. "Server sprawl" - unmanaged MCP servers proliferating across teams. Tool poisoning attacks confirmed. Only 29% of orgs have AI-specific security controls. No centralized MCP governance plane exists.
**Signals (updated 2026-03-23):**
- 2026 MCP roadmap confirmed: agent-to-agent communication requiring governance across identity, transport, policy, and observability layers (elegantsoftwaresolutions.com). HIGH CONFIDENCE.
- Operant AI MCP gateway: real-time visibility, inline redaction, dynamic control - first commercial entrant confirmed. MEDIUM CONFIDENCE (competitor).
- Forbes (2026-03-19): MCP adoption "transitioning from pilots to full-scale enterprise deployment" in finance, healthcare, manufacturing. HIGH CONFIDENCE.
- OAuth 2.1 now mandated in official MCP spec for servers handling sensitive data. Compliance complexity rising. HIGH CONFIDENCE.
- HN sandbox thread (2026-03-19): practitioners debating sandbox/security tradeoffs in production. Confirmed practitioner pain. HIGH CONFIDENCE.
- Open-source red-team playground for AI agent security (HN, 2026-03-15): "We kept finding the same types of vulnerabilities." HIGH CONFIDENCE.
- Autonomous pentest agent (vxcontrol/pentagi, 2026-03-21): fully autonomous attack capability using agent toolchains - confirms MCP/tool pipeline as attack surface. HIGH CONFIDENCE.
- browser-use GitHub trending (2026-03-23): browser automation as standard agent primitive - adds browser tool calls as unaudited attack surface. MEDIUM CONFIDENCE (new today).
- Autonomous Agent hacked McKinsey's AI in 2 hours (BankInfoSecurity, 2026-03-13). HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=4 | Def=3 | IntFric=3 | **Total: 20/25**
*Score unchanged. browser-use trending (Mar 23) confirms browser tool calls becoming standard - expands MCP/tool attack surface. Insufficient to change scores.*

---

## H4 - Agent-Native Micropayment Rails for SMBs
**Thesis:** MPP (Stripe+Tempo), x402 (Coinbase), Visa CLI all launched - but are crypto-native and complex. SMBs cannot use them. Need: simple, fiat-compatible, agent-native billing layer for non-crypto-savvy SMBs.
**Signals (updated 2026-03-23):**
- Machine Payments Protocol on Product Hunt (2026-03-18): Stripe-linked "internet-native payment standard for AI agents." HIGH CONFIDENCE.
- Forbes (2026-03-19): "Stripe, Visa, and Mastercard race to build AI agent payment rails." HIGH CONFIDENCE.
- CBA Agentic Symposium White Paper (Jan 2026): traditional KYC/AML not designed for autonomous agents - regulatory gap confirmed. HIGH CONFIDENCE.
- AgentPay SDK guides autonomous payments in USD1 via EVM (Cryptonews.net, 2026-03-20): crypto-native, not SMB-accessible. HIGH CONFIDENCE.
- Coinbase x402 agentic wallets confirmed. Crypto-native, not SMB-accessible. HIGH CONFIDENCE.
- TradingAgents (GitHub, 2026-03-21): Multi-Agents LLM Financial Trading Framework - financial domain agents proliferating, payment rail demand confirmed. MEDIUM CONFIDENCE (new this run).
- Only 14-29% consumer trust in agent payments (Nevermined.ai, 2026) - trust gap persists.
**Assessment:** Big players (Stripe, Visa, Mastercard) now in this space. SMB-friendly fiat abstraction opportunity remains - but window is narrowing.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=2 | IntFric=4 | **Total: 17/25**
*Score unchanged. TradingAgents (Mar 21) confirms financial domain agent proliferation. Crypto-native entrants still not solving fiat SMB gap.*

---

## H5 - Agent Discovery & Verified Registry
**Thesis:** Thousands of specialized agents exist; no trusted discovery mechanism. No neutral, verified, searchable agent registry for enterprise use.
**Signals (updated 2026-03-23):**
- P2P network for agent science (HN, 2026-03-19): "No way for agents to find each other." Direct validation. HIGH CONFIDENCE.
- AgentDiscuss (Product Hunt + HN, 2026-03-16): "Product Hunt for AI agents." MEDIUM CONFIDENCE.
- GitAgent (HN, 2026-03-14): "open standard that turns any Git repo into an AI agent" - discovery layer needed above it. MEDIUM CONFIDENCE.
- Picsart AI agent marketplace (2026-03-17): first commercial agent marketplace with consumer access. MEDIUM CONFIDENCE.
- ClawRun (2026-03-21): "Deploy and manage AI agents in seconds" - implies catalog/registry component. MEDIUM CONFIDENCE (new this run).
- HAIER: 143 agent signals - ecosystem diversity confirms proliferation, validates discovery pain.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 16/25**
*Score unchanged. ClawRun minor new signal. Still a 2027+ opportunity - no clear enterprise WTP signal yet.*

---

## H6 - Policy Enforcement Runtime (Real-time Agent Guardrails)
**Thesis:** 68% of orgs have reactive-only AI governance. Only 7% have real-time policy enforcement. No product offers inline, runtime policy enforcement for agent actions.
**Signals (updated 2026-03-23):**
- ALTK paper (arxiv, 2026-03-16): "outputs that violate organizational policy can create legal or compliance risk" - confirmed in enterprise production. HIGH CONFIDENCE.
- Meta rogue agent incident (TechCrunch, 2026-03-18): agent bypassed data access controls at scale. HIGH CONFIDENCE.
- NVIDIA OpenShell (2026-03-18): infra layer maturing; policy enforcement gap above it persists. HIGH CONFIDENCE.
- Autonomous pentest agent (vxcontrol/pentagi, 2026-03-21): fully autonomous attack capability - inline policy enforcement becomes security-critical. HIGH CONFIDENCE.
- Dell brings autonomous AI agents to the desktop (AEC Magazine, 2026-03-21): policy enforcement scope expands to edge/desktop. MEDIUM CONFIDENCE (new this run).
- Dell + NVIDIA GB300: first hardware shipped for autonomous agents - hardware commoditizing, policy layer missing. Business Wire, 2026-03-16.
- Autonomous Agent hacked McKinsey's AI in 2 hours (BankInfoSecurity, 2026-03-13). HIGH CONFIDENCE.
- Open-source red-team playground (HN, 2026-03-15): systemic policy gaps documented. HIGH CONFIDENCE.
- Warren presses Pentagon on xAI classified network access (2026-03-16): government-level policy enforcement concern. HIGH CONFIDENCE.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Score unchanged. Dell desktop signal (Mar 21) confirms policy enforcement scope expanding to edge. All prior signals intact.*

---

## H7 - SMB Agent Deployment Wrapper (Turnkey Ops Agent)
**Thesis:** SMBs want agentic AI but face: no expertise, unpredictable costs, dirty data, legacy integration. Market for a fully managed, opinionated ops-agent-as-a-service for SMBs (like Navibase) is wide open.
**Signals (updated 2026-03-23):**
- ClawRun (2026-03-21): "Deploy and manage AI agents in seconds" - new deployment platform validates low-friction agent ops demand. MEDIUM CONFIDENCE (new this run).
- browser-use GitHub trending (2026-03-23): browser automation for AI agents - standard ops primitive maturing, reduces build complexity for SMB wrapper. MEDIUM CONFIDENCE (new today).
- production-agentic-rag-course (2026-03-23): Education demand signal - growing cohort of agent builders, adoption wave incoming. LOW CONFIDENCE (indirect, new today).
- Link AI (Product Hunt, 2026-03-19): "The Agentic Business Suite that replaces your entire stack." MEDIUM CONFIDENCE.
- Budibase AI Agents: "AI agents that run your operations (open source)." MEDIUM CONFIDENCE.
- Cal.com Agents (Product Hunt, 2026-03-13): vertical-specific agent deployment pattern. MEDIUM CONFIDENCE.
- AutoSend MCP (Product Hunt, 2026-03-17): email platform for ops agents. MEDIUM CONFIDENCE.
- Chamber (YC W26): YC validating agent-as-service for infrastructure. HIGH CONFIDENCE.
- Microsoft Copilot rollback (TechCrunch, 2026-03-20): creates space for specialized SMB offerings. MEDIUM CONFIDENCE.
**Assessment:** ClawRun and browser-use confirm tooling ecosystem growing - accelerating adoption wave. Navibase differentiation: Hungarian/CEE market focus + specific vertical (ops). Microsoft Copilot pullback maintains SMB-specific window.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=4 | IntFric=3 | **Total: 18/25**
*Score unchanged. Three new signals today (ClawRun, browser-use, RAG course) validate growing ecosystem. CEE/Hungarian focus remains genuine moat.*

---

## H8 - Cross-Agent Context Persistence (Stateless Problem)
**Thesis:** MCP sessions are stateless. Multi-agent workflows break when agents can't share context across sessions. No neutral, secure, cross-agent memory/context store exists.
**Signals (updated 2026-03-23):**
- Nyne ($5.3M seed, 2026-03-13): VC-backed company directly solving cross-agent context. HIGH CONFIDENCE (funding validates WTP).
- OpenViking (GitHub, 2026-03-16): "open-source context database designed specifically for AI Agents." HIGH CONFIDENCE.
- "Context Overflow" (Product Hunt, 2026-03-20): "Knowledge Sharing for AI Agents." MEDIUM CONFIDENCE.
- ALTK paper: multi-agent coordination failures - context loss explicitly mentioned. HIGH CONFIDENCE.
- Query Memory (Product Hunt, 2026-03-14): "One API for all documents your AI agents need." MEDIUM CONFIDENCE.
- cognee (GitHub, 2026-03-16): "Knowledge Engine for AI Agent Memory in 6 lines of code." MEDIUM CONFIDENCE.
- production-agentic-rag-course (2026-03-23): Production RAG for agentic systems - confirms context as core production concern. LOW CONFIDENCE (indirect, new today).
**Assessment:** Nyne's $5.3M seed remains key signal. Space is crowded. GDPR-compliant EU-focused angle may differentiate.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=4 | **Total: 18/25**
*Score unchanged. RAG course (Mar 23) is weak positive. Def remains low due to crowded landscape.*

---

## H9 - Agent-Dedicated Email & Communication Infrastructure
**Thesis:** Agents need dedicated, attributable communication channels. Attribution breaks, deliverability fails, compliance impossible when agents share human accounts.
**Signals (updated 2026-03-23):**
- AgentMailr (HN, 2026-03-15): "dedicated email inboxes for AI agents" - direct practitioner validation. HIGH CONFIDENCE.
- AutoSend MCP (Product Hunt, 2026-03-17): "The email platform your AI agent can operate." MEDIUM CONFIDENCE.
- discli (Product Hunt, 2026-03-16): "Discord CLI for AI agents and humans." MEDIUM CONFIDENCE.
- WordPress.com AI agents (TechCrunch, 2026-03-20): agent content at scale, attribution urgent. MEDIUM CONFIDENCE.
**Assessment:** No new signals today. Early stage hypothesis. WTP and defensibility unclear.
**Scores:** Pain=3 | Urgency=3 | WTP=2 | Def=2 | IntFric=2 | **Total: 12/25**
*Score unchanged. Monitoring for WTP signals.*

---

## H34 - Agent Ops Monitoring & Human-in-the-Loop Control Plane (Messaging-native)
**Thesis:** Ahogy az agentek a végrehajtás felé mennek (TUI-k, remote desktop, messaging), a napi operációs fájdalom nem az, hogy "mit tud az agent", hanem hogy **hogyan látod és irányítod futás közben**. Kell egy agent-native "ops console", ami messagingből elérhető: run státusz, élő napló, jóváhagyási gombok, visszagörgethető audit, és gyors beavatkozás (pause/rollback). A meglévő IT remote desktop tooling rossz erre, mert nem agent művelet-szintű.
**Signals (updated 2026-04-09):**
- Astropad Workbench (TechCrunch, 2026-04-08): "remote desktop for AI agents" explicit pozicionálás, agent-ops monitoring kategória megjelenése. HIGH CONFIDENCE.
- Poke (TechCrunch, 2026-04-08): agents as easy as sending a text, messaging-native UX elterjedése, ami ops kontrollt igényel. HIGH CONFIDENCE.
- TUI-use (GitHub, 2026-04-08): agentek TUI programokat vezérelnek, amihez transcript + permission + live intervention kell. HIGH CONFIDENCE.
**Assessment:** Ez a H2/H6/H19 gyakorlati "surface area" kiegészítője, a buyer itt ops lead és IT. Navibase/Leoni irány: Telegram-first approval + run dashboard + audit export, "one glance ops" a CEO-nak.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-09). A Workbench + messaging-native agent UX együtt jelzi: agentek üzemeltetése új UI kategória, nem csak backend governance.*

---

## H35 - Agent End-User Distribution via Text, with Identity & Confirmation (Consumer-to-Enterprise Bridge)
**Thesis:** Az agentek elosztása (distribution) átrendeződik: a "külön app" helyett **SMS/WhatsApp/Telegram** jellegű csatornákon jelennek meg az agentek. Ez megnyitja a tömeges használatot, de azonnal felhozza az identity, consent, és action-confirmation problémát. A piacon hiányzik egy "messaging agent gateway", ami vállalati szintű identity + scope + confirmation flow-val engedi a text-based agent használatot.
**Signals (updated 2026-04-09):**
- Poke (TechCrunch, 2026-04-08): agents via text, mainstream distribution shift. HIGH CONFIDENCE.
- Copilot terms "for entertainment purposes only" (TechCrunch, 2026-04-05): jogi disclaimerek erősödnek, text-based agentnél kötelező lesz a megerősítés és a felelősségi keret. HIGH CONFIDENCE.
**Assessment:** Erős wedge lehet SMB-nél: "agent a chatben", de enterprise-ready guardrail-lel. Navibase kapcsolódás: Telegram-first ops, de identity+authorization és confirmation flow produktizálása.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=3 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-04-09). A distribution ugrás gyors, de a monetizációs buyer és compliance boundary még alakul.*

---

## Ranking Summary (2026-03-23)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 - Agent Identity & Auth | 21/25 | = |
| 4 | H3 - MCP Governance | 20/25 | = |
| 5 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 6 | H8 - Cross-Agent Context | 18/25 | = |
| 7 | H4 - Agent Payment Rails | 17/25 | = |
| 8 | H5 - Discovery & Registry | 16/25 | = |
| 9 | H9 - Agent Communication Infra | 12/25 | = |

*Low-delta day (2026-03-23): only 2-3 genuinely new signals since Mar 22 update. No score changes. All prior signals remain intact. Next significant movement expected when EU AI Act enforcement window tightens (Q2 2026) or new VC funding signal appears.*

---

## Top 5 Signals This Run (2026-03-23)

1. **browser-use GitHub trending** (2026-03-23): Browser automation for AI agents hitting GitHub trending - confirms browser tool calls becoming a standard agent primitive. Relevant to H3 (MCP/tool governance) and H7 (SMB ops agents). MEDIUM CONFIDENCE.

2. **ClawRun "Deploy and manage AI agents in seconds"** (2026-03-21, not in previous update): New agent deployment platform targeting deployment simplicity. Validates H7 SMB demand. MEDIUM CONFIDENCE.

3. **TradingAgents: Multi-Agents LLM Financial Trading Framework** (2026-03-21, not in previous update): Domain-specific financial agent - confirms financial vertical's appetite for multi-agent systems (H4 payment rails). MEDIUM CONFIDENCE.

4. **Dell brings autonomous AI agents to the desktop** (2026-03-21): Hardware expansion to desktop environment - policy enforcement (H6) and audit trail (H2) scope expands to edge. MEDIUM CONFIDENCE.

5. **production-agentic-rag-course** (2026-03-23): Education demand for production agentic RAG - growing adoption wave (H7, H8). LOW CONFIDENCE (indirect).

**Note:** Today is a low-delta day. The most impactful signals from this week remain: McKinsey hack (H3/H6), Nyne $5.3M seed (H8), NIST April deadline (H1). No score changes warranted today.

---

## Top 3 Opportunities + Suggested Experiments

### #1: H2 / H6 (tied) - Audit Trail + Policy Enforcement Runtime
**Why now:** EU AI Act Aug 2026 deadline, McKinsey hack confirms security-driven demand, 94% orgs report gaps. Dual pitch: compliance AND security.
**Experiment:** Cold outreach to 10 EU-based enterprises using Claude/GPT in production. Offer 30-day free audit report generator for EU AI Act compliance. Measure: conversion to paid, price sensitivity, compliance framework cited.
**Investment:** ~2 weeks build. Use ALTK + Tracium.ai as proof-of-concept signals in pitch.

### #2: H1 - Agent Identity & Auth Layer
**Why now:** NIST concept papers due April 2, 2026. EU AI Act Aug 2026. 77% orgs lack formal strategy. World/Worldcoin launch confirms market formation.
**Experiment:** Publish a free "Agent Identity Audit" tool - scans enterprise MCP/agent configs for identity gaps, outputs compliance checklist. Measure: downloads, enterprise inbound, conversion to paid advisory.
**Investment:** ~1 week build. Strong SEO play into April NIST deadline.

### #3: H7 - SMB Deployment Wrapper (Navibase direct relevance)
**Why now:** ClawRun and Link AI confirm market formation but no CEE/Hungarian player exists. Microsoft Copilot pullback creates SMB-specific window.
**Experiment:** Offer Leoni (current ops agent) as white-labeled pilot to 3 Hungarian SMBs. Measure: time-to-value, churn after 60 days, top 5 most frequent tasks.
**Investment:** Existing infrastructure. Main cost: Tomi's time for pilot setup. Direct revenue test.

---

## Data Sources & Confidence Notes

- **Primary:** HAIER evolution_signals export (2026-03-23, 800 total signals, 143 agent-relevant; filtered on focus_area: 'AI agents' OR 'AI decision delegation')
- **Web search:** UNAVAILABLE this run (Gemini API key error - same as 2026-03-22 run). All signals from HAIER export only. 143 signals sufficient for quality update; no critical gaps identified.
- **Delta since last update:** 3 genuinely new signals (browser-use Mar 23, jamwithai RAG course Mar 23, Sashiko Mar 22). 3 additional reviewed but previously noted (ClawRun, TradingAgents, Dell desktop).
- **Confidence notation:** HIGH = named source + verifiable claim | MEDIUM = plausible but single source or projection | LOW = speculative or executive opinion
- All scores are editorial judgments based on signal weight, not algorithmic. Treat as directional, not precise.
- No fabricated data. All claims traceable to specific sources in HAIER export.

*Last full web search: 2026-03-21. Web search unavailable 2026-03-22 and 2026-03-23 due to Gemini API key error. If API remains unavailable Mar 24, recommend Tomi checks Gemini API key status.*

---

## H10 - Agent Infrastructure as Code (GitOps for Agents)
**Thesis:** Ahogy az agent-ek száma nő, a kézi konfigurációkezelés fenntarthatatlanná válik. Nincs standard, verziókövetett módszer agent policy-k, role-ok, tool permission-ök és deployment konfigurációk deklaratív kezelésére. A Terraform mintájára szükség van egy "agent infra as code" rétegre: YAML-alapú, GitOps workflow-val, rollback képességgel.
**Signals (updated 2026-03-27):**
- Orloj (GitHub/HN, 2026-03-26): AgentPolicy, AgentRole, ToolPermission runtime gate, teljes audit trail YAML-ból - open-source pionír, közvetlenül validálja a thesis-t. HIGH CONFIDENCE.
- NVIDIA OpenShell (2026-03-23): secure runtime for autonomous agents - infra réteg standardizálódik, policy-as-code igény nő fölötte. HIGH CONFIDENCE.
- EU AI Act (arxiv, 2026-03-24): autonóm agentek szabályozatlan zónában vannak - policy deklarálhatósága compliance-kritikussá válik Aug 2026-ra. HIGH CONFIDENCE.
- Cloudflare Dynamic Workers (2026-03-24): sandbox izolálás infrastrukturális szinten megoldva - az "above infra" policy/config réteg marad nyitott. MEDIUM CONFIDENCE.
**Assessment:** Az Orloj nyílt forráskódú - a competitive moat nem a tool maga, hanem az opinionated, KKV-kra szabott konfiguráció template-ek és managed service réteg. Navibase alkalmazás: agent konfiguráció sablonok + változáskövetés + compliance export.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=4 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-03-27). Orloj megjelenése közvetlen validáció. Az open-source megközelítés miatt a managed/opinionated réteg a differenciáló tényező.*

---

## H11 - Multi-Agent Hallucination Self-Check Layer
**Thesis:** KKV agenteknél az ügyfél-kommunikáció, ajánlatok, döntések megbízhatósága üzletileg kritikus. A "hallucination" nem csak technikai zaj - egy téves email vagy hibás adat direkt üzleti kár. Jelenleg nincs beépített, cost-efficient self-check réteg multi-agent pipeline-okban. A MARCH eredmény megmutatja: 8B paraméteres modell MARL-lal eléri a closed-source szintet hallucináció-ellenőrzésben.
**Signals (updated 2026-03-27):**
- MARCH paper (arxiv, 2026-03-25): multi-agent RL-alapú hallucináció self-check, 8B modellel closed-source teljesítmény - cost-efficient megoldás production agenteknél. HIGH CONFIDENCE.
- ALTK paper (arxiv, 2026-03-16): tool argument corruption, policy violation, silent reasoning error - multi-agent pipeline failures dokumentálva. HIGH CONFIDENCE.
- Meta rogue agent (2026-03-24): az "ellenőrzés illúziója" narratíva KKV pitchben visszaütő - a megbízhatóság lesz az értékesítési battleground. HIGH CONFIDENCE.
- EU AI Act autonóm agent kompatibilitás paper (arxiv, 2026-03-24): "misuse risk, unequal access" - téves agent output felelősség kérdése nyílik. HIGH CONFIDENCE.
**Assessment:** A MARCH technikát a Navibase SMB ops agent reliability rétegébe lehet integrálni: kimenő kommunikáció (email, ajánlat, riport) előtt self-check pass. Kis modell, alacsony latency, magas üzleti érték. Versenyképes differenciátor a "megbízható agent" pitchben.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=3 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-03-27). MARCH paper közvetlen technikai validáció. KKV relevanciája magas - az "agent hibázott és az ügyfélnek ment" forgatókönyv a legnagyobb adopciós barrier.*


---

## H62 - Governance-Compliance Structural Alignment (Expressiveness ↔ Governance Boundary)
**Thesis:** A "The Two Boundaries" model azt mutatja, hogy a legtöbb produkciós agent rendszernél a system expressiveness (capability limits) és a governance coverage (policy limits) függetlenül vannak definiálva. Ez 3 régióban szétszóródott kockázatot hozhat: (1) governed capability (jó, de ritka), (2) ungoverned capability (biztonsági kockázat), (3) ungoverned but restricted capability (feleslegesen drága). Az explicit boundary mapping és a "governance surface discovery" hiánya a fő structural vacuity.
**Signals (updated 2026-05-04):**
- The Two Boundaries: Why Behavioral AI Governance Fails Structurally (arxiv, 2026-04-30): explicit model, structural failure pattern dokumentálva. HIGH CONFIDENCE.
- UGAF-ITS: Standards Harmonization Framework (arxiv, 2026-04-07): fragmented governance (ISO/IEC 42001, EU AI Act, NIST) - boundary mismatch Enterprise szinten is. HIGH CONFIDENCE.
- AI Governance Control Stack for Operational Stability (arxiv, 2026-03-12): "many governance approaches focus primarily on policy guidance rather than operational stability mechanisms" - structural gap, nem csak missing implementation. HIGH CONFIDENCE.
**Assessment:** Navibase alkalmazás: explicit "Agent Governance Surface Map" - capabilities audit + policy coverage scan + gap report. Audit-ready deliverable, amelyet security/compliance teams azonnal használhatnak. Gyors entry point a H2/H6/H10 irányba.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-05-04). A "Two Boundaries" explicit model megnyitja az auditálási, majd compliance-as-code dienálási lehetőséget.*

---

## H63 - Public Trust Degradation Monitoring (Real-time Feedback Loop Management)
**Thesis:** A "Stability of AI Governance Systems" coupled dynamics model azt mutatja, hogy a deployed agent viselkedése és a nyilvános bizalom között instabil feedback loop alakul ki: rossz agent output → nyilvános bizalomvesztés → politikai/regulatív backlash → korlátozások → innovation block. A jelenleg semmilyen real-time monitoring nem követi ezt a feedback loop-ot, így az agent adoption és societális stability között egy critical blind spot van. Szervezeteknek nincsen eszköze, hogy "trust degradation" megelőzésként jelezzenek.
**Signals (updated 2026-05-04):**
- Stability of AI Governance Systems: A Coupled Dynamics Model of Public Trust and Social Disruptions (arxiv, 2026-03-10): explicit coupled system model, public trust as stability determinant. HIGH CONFIDENCE.
- Meta rogue agent incident (2026-03-18): cascading trust erosion, media backlash - live feedback loop case study. HIGH CONFIDENCE.
- EU AI Act Aug 2026 deadline + Gartner: 80% of governments deploy agents by 2028 - public trust decisions at scale incoming. MEDIUM CONFIDENCE.
**Assessment:** Az ops ügynök (Leoni) kontextusában értékesíthető: "Agent Output Public Trust Score" - outgoing communication (email, ajánlat, report) tone/accuracy/compliance szűrés + external reputation feedback (media, customer complaint monitoring). Preventív risk management pitch.
**Scores:** Pain=4 | Urgency=4 | WTP=3 | Def=3 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-05-04). A coupled dynamics model explicit modellezése omogeti a prevenív beavatkozási stratégiákat.*

---

## H64 - Autonomy-Control Balance Framework (Safe Handoff Mechanisms)
**Thesis:** A "Autonomy vs. Control Paradox" pattern arra mutat, hogy az agentek autonómiája és az emberi oversight közötti trade-off kézileg oldódik meg (vagy nem oldódik meg). Jelenleg nincs formális keretrendszer az "autonóm hatáskör limitjainak" definiálására agent szinten (pl. maximum tranzakciós érték, maximum comunicatio surface, approval gates specifikus operációkhoz). Ez a hiányosság tanto security (rogue agent) mint user experience (túl sok jóváhagyás) kockázatot hozhat. Szükség van egy "Safe Handoff" framework-re, amely explicit autonomy budget, capability scope, és fallback stratégia-kat definiál per-agent-per-task.
**Signals (updated 2026-05-04):**
- From Prompt to Physical Actuation: A Unified Framework and Benchmark for LLMs Embodying Autonomous Agents (implicit signal): Language-centric interfaces limit oversight mechanisms in robotics/autonomous agents. MEDIUM CONFIDENCE (inferred from recommendations).
- LLM Constitutional Multi-Agent Governance (arxiv, 2026-03-13): "does cooperation reflect genuine prosocial alignment, or does it mask failure?" - autonomy vs. control trade-off formalization szükséges. MEDIUM CONFIDENCE.
- Agent authentication + Zeroclawed gateway (2026-04-10/2026-04-13): "secure switching" logicája előfeltételez explicit autonomy scope. MEDIUM CONFIDENCE (inferred).
**Assessment:** Navibase-nél konkrét alkalmazás: per-task autonomy budget template (pl. "email draft: autonomy 80%, approval gate 20%; cost approval threshold: 1000 HUF"), audit trail with "autonomy decision boundary." KKV compliance + operatív safety pitch.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 15/25**
*Új hypothesis (2026-05-04). Az explicit autonomy budget definiálása szükséges a "agent hacker" vs. "agent escrow" narratíva közötti választás feloldásához.*

---

## Ranking Summary (2026-05-04)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 - Agent Identity & Auth | 21/25 | = |
| 4 | H3 - MCP Governance | 20/25 | = |
| 5 | H10 - Agent Infra as Code | 19/25 | = |
| 6 | **H62 - Governance Boundary Alignment** | **17/25** | **ÚJ** |
| 7 | **H63 - Trust Degradation Monitoring** | **17/25** | **ÚJ** |
| 8 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 9 | H8 - Cross-Agent Context | 18/25 | = |
| 10 | H4 - Agent Payment Rails | 17/25 | = |
| 11 | H11 - Hallucination Self-Check | 17/25 | = |
| 12 | **H64 - Autonomy-Control Balance** | **15/25** | **ÚJ** |
| 13 | H5 - Discovery & Registry | 16/25 | = |
| 14 | H9 - Agent Communication Infra | 12/25 | = |

*2026-05-04 delta: 3 új hypothesis (H62, H63, H64). Meglévő scorok változatlanok. Új structural governance themata: boundary alignment + trust monitoring + autonomy budget. A "Two Boundaries" modell és coupled dynamics research az agent governance design-t egyre explicitebb keretre kényszeríti. Strukturális és real-time monitoring innovációk felértékelődnek.*

---

## Top 3 Opportunities + Suggested Experiments (2026-03-27)

### #1: H2 / H6 (tied) - Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** EU AI Act Aug 2026 deadline közeledik. McKinsey hack + Meta rogue agent megerősítik a biztonsági igényt. 94% szervezetnél kritikus hiány az AI aktivitás láthatóságában. A compliance + security kettős pitch most nyitott ablak.
**Javasolt kísérlet:** 10 EU-ban működő, Claude/GPT-t production-ben használó enterprise-nak hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit report generátor. Mérők: konverzió fizetős felé, árszenzitvitás, hivatkozott compliance framework.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai mint proof-of-concept.

### #2: H10 - Agent Infrastructure as Code [Score: 19/25 - ÚJ]
**Miért most:** Az Orloj open-source megjelenése (2026-03-26) jelzi, hogy a piac elkezdi standardizálni a GitOps for Agents mintát. Az EU AI Act compliance-hoz szükséges auditálható policy deklarálhatóság megnöveli a WTP-t vállalati szinten. Moat lehetőség: managed service + opinionated KKV template-ek az open-source tool fölé.
**Javasolt kísérlet:** Navibase "Agent Config Template Library" - 5 iparági sablon (ügyfélszolgálat, könyvelés, HR, értékesítés, logisztika) YAML-ban, Orloj/policy-as-code mintára. Mérő: GitHub star szerzés 30 nap alatt, inbound enterprise kontakt, template letöltések.
**Befektetés:** ~1 hét. Erős SEO- és thought leadership-hatás a Navibase brand számára.

### #3: H62 + H63 - Governance Boundary Mapping + Trust Monitoring [Score: 17/25 - ÚJ]
**Miért most:** Az új signal file explicit strukturális modelleket hoz (The Two Boundaries, Coupled Dynamics) - ez azt jelzi, hogy a piac el tudja kezdeni formalizálni, amit eddig ad-hoc módon csinált. Az "Agent Governance Surface Map" + "Trust Degradation Real-time Feed" kettős pitch gyors belépési pont a H2/H6 audit/policy irányához, viszont strukturálisabb és measurable-ebb megközelítéssel.
**Javasolt kísérlet:** Navibase "Agent Governance Audit Tool" - Capabilities Discovery + Policy Coverage Scan + Trust Monitoring Dashboard. Input: agent MCP config + recent outputs. Output: (1) governance surface map, (2) boundary mismatch report, (3) public trust risk score (tone/accuracy check). Integrációs partner lehetőség H2 (audit trail) és H6 (policy enforcement) felett.
**Befektetés:** ~2 hét. Strong B2B SaaS foundation, audit/legal szellőztetéshez könnyű pitch.
**Befektetés:** ~1 hét. Azonnal tesztelhető a meglévő Leoni infrastruktúrán. Ha működik: KKV pitch centerdarabja.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-03-27.md (189 signal, HAIER export) | 2026-03-27 09:30 CET*


---

## H12 - Agent Accountability & Legal Responsibility Framework
**Thesis:** Autonóm AI agentek elterjedésével "felelősségi vákuum" keletkezik: sem a fejlesztő, sem a deployer, sem a felhasználó nem vonható felelősségre az agent döntéséért. 2026-ra ez a kérdés jogi, szervezeti és üzleti szinten megoldatlan. Az AI governance narratíva átfogalmazódik: nem az automatizáció megállítása, hanem a döntési felelősség újratervezése a cél. Erre nincs sem standard keretrendszer, sem termék.
**Signals (updated 2026-03-28):**
- iProov: "Accountability Vacuum" figyelmeztetés (2026-03-26): biometria-biztonsági cég nyilvánosan nevesíti a problémát - a felelősségi vákuum közvetlen kockázat minden operatív agent deploymentnél. HIGH CONFIDENCE.
- arxiv: "Regulating AI Agents" (2026-03-24): korlátozott emberi felügyelet melletti önálló döntéshozatal elemzése - tudományos szinten is megjelent, szabályozói tér nyitva van. HIGH CONFIDENCE.
- Leaders League: "The Illusion of Automation" - Decision Architecture (2026-03-25): "az AI governance nem az automatizáció megállítása, hanem a döntési felelősség újratervezése." HIGH CONFIDENCE.
- EurekAlert!: "Embedding Social Values into AI Decisions" (2026-03-27): kutatási irány a konfigurálható értékalapú korlátok felé - jogi felelősség és szervezeti értékek metszéspontja. MEDIUM CONFIDENCE.
- Sanders/AOC moratorium javaslat (TechCrunch, 2026-03-25): politikai szinten is megjelent - szabályozói nyomás emelkedik, compliance-driven kereslet várható. MEDIUM CONFIDENCE.
**Assessment:** Ez a hypothesis az eddigi listán hiányzó *jogi és szervezeti réteg* - a H2 (audit log) és H6 (policy enforcement) technikai rétegei fölött. A KKV pitch szempontjából erős differenciátor: nem azt mondjuk, hogy "az agent elvégzi a munkát", hanem azt, hogy "tudod, ki felel az agent döntéséért". Versengő termék jelenleg nincs - a tér nyitott. Navibase alkalmazás: "Accountability Map" - szervezeti felelősségrendelési sablonok + agent-döntés owner mátrix + audit-ready dokumentáció.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=4 | IntFric=3 | **Total: 20/25**
*Új hypothesis (2026-03-28). iProov + arxiv + Leaders League egymást erősítő, különböző szektorbeli signalok. A jogi felelősség kérdése az EU AI Act Aug 2026 deadlinjével tovább élesedik.*

---

## Ranking Summary (2026-03-28)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 - Agent Identity & Auth | 21/25 | = |
| 4 | H3 - MCP Governance | 20/25 | = |
| 5 | **H12 - Agent Accountability Framework** | **20/25** | **ÚJ** |
| 6 | H10 - Agent Infra as Code | 19/25 | = |
| 7 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 8 | H8 - Cross-Agent Context | 18/25 | = |
| 9 | H4 - Agent Payment Rails | 17/25 | = |
| 10 | H11 - Hallucination Self-Check | 17/25 | = |
| 11 | H5 - Discovery & Registry | 16/25 | = |
| 12 | H9 - Agent Communication Infra | 12/25 | = |

*2026-03-28 delta: 1 új hypothesis (H12 - Accountability Framework, 20/25). Meglévő scorok változatlanok. H12 azonnal a top 5-be kerül - az accountability vákuum téma 3 független, magas bizalmú signallal nyílt meg. EU AI Act Aug 2026 közeledtével Q2-ben urgency emelkedés várható H1/H2/H6/H12 blokkon.*

---

## Top 3 Opportunities + Suggested Experiments (2026-03-28)

### #1: H2 / H6 (tied) - Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** EU AI Act Aug 2026 deadline 5 hónap. McKinsey hack + Meta rogue agent esetei megerősítik biztonsági igényt. 94% szervezetnél kritikus hiány az AI aktivitás láthatóságában. Compliance + security kettős pitch, most nyitott ablak.
**Javasolt kísérlet:** 10 EU-ban működő, Claude/GPT-t production-ben használó enterprise hideg megkeresése. Ajánlat: 30 napos ingyenes EU AI Act compliance audit report generátor. Mérők: konverzió fizetős felé, árszenzitvitás, hivatkozott compliance framework.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai proof-of-concept signalként a pitchben.

### #2: H12 - Agent Accountability Framework [Score: 20/25 - ÚJ]
**Miért most:** Az "accountability vacuum" ma 3 független szektorbeli sourcetól jelent meg (biztonsági ipar, tudományos szféra, üzleti média) - ez nem trend, ez jel. A tér üres: nincs termék, nincs standard, nincs referencia. Az EU AI Act Aug 2026 a jogi felelősség kérdését kötelező compliance szintjére emeli. Navibase differenciátor: nem csak az agent csinál valamit, hanem pontosan tudod, ki felel az eredményért.
**Javasolt kísérlet:** "Agent Accountability Map" sablon - szabad letöltés, 3 szekció: (1) döntési owner mátrix agent típusonként, (2) eskalációs protokoll, (3) EU AI Act megfelelési checklist. Mérők: letöltések, inbound megkeresések, LinkedIn engagement 2 héten belül. Ha 200+ letöltés: fizetős workshop pilot.
**Befektetés:** ~3 nap. Thought leadership befektetés, közvetlen lead generáló hatással.

### #3: H7 - SMB Deployment Wrapper (Navibase közvetlen relevancia) [Score: 18/25]
**Miért most:** A mainstream sajtóban (Jerusalem Post, 2026-03-27) megjelent az autonóm agent téma - a KKV-k hallanak róla, a pitch window nyitva van, de a konkurencia is ébredezik. CEE/magyar piacon még nincs versenyző. Microsoft Copilot pullback SMB-specifikus ablakot tart nyitva.
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

## H14 - Agent-to-Agent Trust & M2M Communication Protocol
**Thesis:** Az agent ökoszisztéma következő nagy megoldatlan kérdése: hogyan kommunikálnak, hitelesítik egymást és osztanak meg kontextust az autonóm agentek egymás között? A mai rendszerekben az agent-to-agent kapcsolat nincs definiálva - sem trust, sem protokoll, sem felelősségi határ. Ez a "machine-to-machine trust" probléma a multi-agent pipeline-ok skálázásának legfőbb akadálya.
**Signals (updated 2026-03-30):**
- Enlidea (HN, 2026-03-28): autonóm agentek, amik hipotéziseket javasolnak, bounty-kat tesznek, kódot futtatnak és peer review-t végeznek egymás munkáján. Reverse-CAPTCHA: csak agent lép be, ember nem. Direkten validálja az agent-first M2M ecosystem igényt. HIGH CONFIDENCE.
- CRAFT paper (arxiv, 2026-03-26): 8 open-weight + 7 frontier modell tesztelve - erősebb reasoning nem jelent jobb multi-agent koordinációt. "Fundamentally unsolved challenge." HIGH CONFIDENCE.
- iProov "accountability vacuum" (2026-03-26): felelőssége nincs senkinek, ha agent dönt - ez M2M kontextusban kettőzve igaz. HIGH CONFIDENCE.
- H8 (Cross-Agent Context, Nyne $5.3M) és H1 (Agent Identity) már lefedi a részterületeket - H14 ezekre épít, de az "agent trust negotiation" réteget teszi hozzá.
**Assessment:** A CRAFT eredmény megmutatja: a probléma nem modellerő, hanem protokoll és koordináció. Aki ma épít agent-to-agent trust réteg szabványt (akár lightweight, akár YAML-alapú), az megteremtheti a következő MCP-szintű szabvány alapjait. A Navibase alkalmazás: multi-agent orchestrátor template-ek, ahol a trust handshake és az eskalációs protokoll definiált.
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=4 | IntFric=4 | **Total: 18/25**
*Új hypothesis (2026-03-30). CRAFT + Enlidea egymást erősítő signalok. 2026 végétől urgency emelkedés várható, ahogy multi-agent pipeline-ok production-ba kerülnek.*

---

## H15 - B2B SaaS Agent Feature Injection (Meglévő termékek + agent réteg)
**Thesis:** A Granola eset ($125M, $1.5B valuáció) megmutatta: egy meglévő B2B SaaS termék agent-funkciók hozzáadásával azonnal 10x értékugrást képes elérni. A piac ma azt jutalmazza, aki a meglévő user base-jének agent képességeket ad - nem azt, aki nulláról épít agent platformot. Ez a KKV szegmensben eddig érintetlen lehetőség: meglévő magyar/CEE B2B SaaS termékek agent integrációra várnak.
**Signals (updated 2026-03-30):**
- Granola $125M / $1.5B valuáció (TechCrunch, 2026-03-25): meeting notetaker → enterprise agent platform. Felhasználók panaszolták a hiányát → azonnal beépítették → valuáció megtízszereződött. HIGH CONFIDENCE.
- AI Agents → Governance Infrastructure mainstream (National Today, 2026-03-29): az agent funkció nem differenciátor, hanem elvárás lesz - aki késik, lemarad. HIGH CONFIDENCE.
- Microsoft Copilot pullback (TechCrunch, 2026-03-20): big tech kivonul egyes SMB szegmensekből, nyitva hagyja a lokális/specializált agent integration piact. MEDIUM CONFIDENCE.
- Link AI "replace your entire stack" (2026-03-19): versenytárs próbál teljes stack-et kiváltani - de a meglévő SaaS-ba épülő agent réteg kisebb súrlódással jár. MEDIUM CONFIDENCE.
**Assessment:** Ez nem platform-build, hanem integration play. A Navibase pozicionálása: "agent layer a te meglévő rendszeredre" - CRM-be, számlázóba, projektmenedzsmentbe, ERP-be. A proof of concept a Leoni ops agent: nem új platform, hanem a meglévő Gmail/GitHub/Telegram infrastruktúrára rakott végrehajtó intelligencia. Alacsony IntFric, magas WTP a SaaS oldalán.
**Scores:** Pain=4 | Urgency=5 | WTP=5 | Def=3 | IntFric=2 | **Total: 19/25**
*Új hypothesis (2026-03-30). A Granola signal az egyik legerősebb üzleti bizonyíték az eddigi listán - valuáció szintű piacvalidáció. Az urgency magas: az ablak nyitva van, de a nagy szereplők is ébredeznek.*

---

## Ranking Summary (2026-03-30)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 - Agent Identity & Auth | 21/25 | = |
| 4 | H3 - MCP Governance | 20/25 | = |
| 5 | H12 - Agent Accountability Framework | 20/25 | = |
| 6 | H10 - Agent Infra as Code | 19/25 | = |
| 7 | **H15 - B2B SaaS Agent Feature Injection** | **19/25** | **ÚJ** |
| 8 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 9 | H8 - Cross-Agent Context | 18/25 | = |
| 10 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 11 | **H14 - Agent-to-Agent Trust & M2M** | **18/25** | **ÚJ** |
| 12 | H4 - Agent Payment Rails | 17/25 | = |
| 13 | H11 - Hallucination Self-Check | 17/25 | = |
| 14 | H5 - Discovery & Registry | 16/25 | = |
| 15 | H9 - Agent Communication Infra | 12/25 | = |

*2026-03-30 delta: 2 új hypothesis (H14, H15). H15 azonnal a top 7-be kerül a Granola valuációs bizonyíték ereje miatt. Governance és compliance blokk (H2/H6/H12) dominálja a listát - EU AI Act Aug 2026 deadline közeledtével ez várható.*

---

## Top 3 Opportunities + Suggested Experiments (2026-03-30)

### #1: H15 - B2B SaaS Agent Feature Injection [Score: 19/25 - ÚJ]
**Miért most:** A Granola eset valódi, számokkal alátámasztott piacvalidáció: agent layer hozzáadása meglévő B2B termékhez = 10x valuáció. Az ablak nyitva van, de a nagy szereplők (Salesforce, HubSpot, Monday.com) is mozognak. Magyar/CEE piacon nincs versenyző, aki ezt lokálisan hirdeti. Alacsony build-fric: a meglévő Navibase/Leoni infra minta.
**Javasolt kísérlet:** Azonosítani 3 magyar B2B SaaS céget (CRM, projekt, számlázó szegmensben), akiknek van aktív user base-jük de nincs agent feature-jük. Megközelítés: "agent integration partnership" - Navibase beépít egy Leoni-típusú ops agent réteget az ő termékükbe. Mérők: partnership érdeklődés 4 héten belül, pilot ajánlat elfogadási arány, user engagement növekedés a pilotnál.
**Befektetés:** ~1 hét outreach. Ha 1/3 partner igent mond: 8-12 hetes MVP sprint.

### #2: H2 / H6 (tied) - Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** EU AI Act Aug 2026 deadline 4 hónap. Az AI agents → governance infrastructure mainstream narratíva (National Today, 2026-03-29) azt jelzi, hogy a compliance igény most terjed át a nem-tech CEO-khoz is. Ez a legmagasabb score-ú, legérettebb lehetőség a listán.
**Javasolt kísérlet:** 10 EU-based Claude/GPT production-user enterprise hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit. Mérők: pilot→paid konverzió, árszenzitvitás, compliance framework hivatkozás.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai proof-of-concept a pitchben.

### #3: H12 - Agent Accountability Framework [Score: 20/25]
**Miért most:** Az iProov "accountability vacuum" + Leaders League "Decision Architecture" + EurekAlert "Social Values" egymást erősítő, különböző szektorbeli signalok. A kategória üres. A governance infrastruktúra mainstream narratíva (2026-03-29) azt jelzi, hogy ez már nem "tech bubble téma" - CEO szinten is megjelent.
**Javasolt kísérlet:** "Agent Accountability Map" sablon - 3 nap build, szabad letöltés. Tartalom: döntési owner mátrix, eskalációs runbook, EU AI Act megfelelési checklist. Mérők: 200+ letöltés 2 héten belül → fizetős workshop pilot indítás.
**Befektetés:** ~3 nap. Thought leadership + lead gen, közvetlen bevételi utat nyit.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-03-30.md (208 signal, HAIER export) | 2026-03-30 11:36 CET*


---

## H16 - AI Alignment Measurement as a Service (Delegáció-ellenőrzés)
**Thesis:** Az AI agentek döntései egyre kevésbé átláthatóak a megbízónak. A "Revealed Preference" kutatási irány (Luce Alignment Model) megmutatja: az agent döntései mérhetően eltérhetnek a gazda szándékától. Nincs olyan termék, amely a KKV-k számára mérhetővé teszi, hogy az agent "mennyire az ővé" - vagyis a delegáció foka és minősége kontrolálható legyen. Ez nem technikai monitoring, hanem üzleti kontroll eszköz: "milyen arányban tartja be az agent a céged értékeit és döntési elveit?"
**Signals (updated 2026-03-31):**
- arxiv "Revealed Preference Framework for AI Alignment" (2026-03-29): Luce Alignment Model bevezetése - agent döntései az emberi és saját preferenciák keveréke, eltérés mérhető. HIGH CONFIDENCE.
- iProov "accountability vacuum" (2026-03-26): ki felel az agent döntéséért? - a mérhetőség hiánya jogi és szervezeti kockázat. HIGH CONFIDENCE.
- CRAFT paper: "Fundamentally unsolved challenge" a multi-agent koordináció - az alignment mérése a megbízhatóság alapfeltétele. HIGH CONFIDENCE.
- EU AI Act Aug 2026: "high-risk AI decisions" naplózása kötelező - az alignment mérhetőség természetes compliance komponens. MEDIUM CONFIDENCE.
**Assessment:** A "mennyire bízhat meg az agent döntésében a CEO" kérdés ma megválaszolatlan. Az alignment measurement egy új kategória: nem naplózás (H2), nem policy enforcement (H6), hanem a megbízhatóság kvantitatív jelzése üzleti döntéshozóknak. Navibase alkalmazás: "Leoni Alignment Score" dashboard - hetente megmutatja, hány döntés volt emberi elvárással konzisztens, hány nem, és miért.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=4 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-03-31). A Revealed Preference Framework paper közvetlen tudományos alapot ad. A KKV piac számára az "agent megbízhatóság mérőszáma" az adopciós barrier elhárításának kulcsa.*

---

## H17 - Controlled Self-Configuration Boundary (Agent Scope Hardening)
**Thesis:** Az autonóm agentek egyre több rendszerben kapnak jogot a saját konfigurációjuk módosítására (lásd: Phantom open-source agent, saját VM-en config rewrite). Ez az önmódosítás képesség kontinuumot alkot az "adaptív viselkedés" és a "kontroll elvesztése" között. Nincs standard, amely definiálná, hol a határvonal - sem termék, sem auditálható scope-definition framework. A Navibase/Leoni architektúrában ez már megoldott (explicit scope-olás), de a piac nem tud róla, és ez differenciáló kommunikációs lehetőség.
**Signals (updated 2026-03-31):**
- Phantom (GitHub ghostwright/phantom, 2026-03-30): nyílt forráskódú agent saját VM-en, config rewrite képességgel - az önmódosítás határvonal kérdése production-szintű valóság lett. HIGH CONFIDENCE.
- Orloj (2026-03-26): runtime policy-first megközelítés, tool call gate - az önmódosítás kontrolálhatósága technikai szinten megoldható. HIGH CONFIDENCE.
- Cloudflare Dynamic Workers (2026-03-24): sandbox izoláció 100x gyorsabb - az önmódosítás kontrollált keretek közt tartható. HIGH CONFIDENCE.
- ALTK paper (2026-03-16): "silent reasoning errors go undetected" - önmódosítás nélküli agentben is van drift, önmódosítással hatványozódik. HIGH CONFIDENCE.
**Assessment:** Ez nem technikai újítás - ez kommunikációs és pozicionálási lehetőség. A Navibase/Leoni már megoldotta: az önkonfiguráció explicit scope-olva van, SOUL.md + AGENTS.md definiálja a határt, policy engine enforce-olja. A "Controlled Self-Configuration" mint termék feature és pitch elem: "tudod, mit módosíthat az agent magán és mit nem." Enterprise és KKV szinten egyformán értékes.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=4 | IntFric=2 | **Total: 18/25**
*Új hypothesis (2026-03-31). A Phantom megjelenése kinyitja a "ki szabályozza az agent önmódosítását" kérdést. A Navibase architectúra erre kész választ ad - a differenciáló kommunikáció még nincs megírva.*

---

## H18 - Organizationally-Aligned AI (Social Values Embedding for SMBs)
**Thesis:** Az AI agentek ma "értéksemlegesek" - a szervezet értékrendjét, kommunikációs stílusát, döntési elveit csak prompton keresztül lehet megadni, ami törékeny és nem auditálható. A kutatási irány (EurekAlert, 2026-03-27) mutatja: az emberi értékek beágyazhatók az AI döntési folyamatokba. A KKV piacnak szüksége van egy eszközre, amellyel a saját szervezeti értékeiket (pl. "nem ajánlunk semmit ha bizonytalan a szükséglet", "mindig az ügyfél érdekét prioritizáljuk") verziókövetve, auditálhatóan adják meg az agentnek - nem prompton, hanem konfigurált policy-ként.
**Signals (updated 2026-03-31):**
- EurekAlert: "Embedding Social Values into AI Decisions" (2026-03-27): tudományos validáció - az értékbeágyazás lehetséges és szükséges. HIGH CONFIDENCE.
- iProov "accountability vacuum": az agent döntése mögött ott kell lennie a szervezeti értékrendnek, hogy a felelősség visszakövethető legyen. HIGH CONFIDENCE.
- Leaders League "Decision Architecture" (2026-03-25): "az AI governance a döntési felelősség újratervezése" - az értékek explicit kódolása ennek alapja. HIGH CONFIDENCE.
- Leoni SOUL.md + USER.md struktúra: ez maga is egy "values embedding" implementáció - de nincs KKV-szintű termékké téve. MEDIUM CONFIDENCE (internal signal).
**Assessment:** Ez a H12 (accountability) és H16 (alignment measurement) természetes kiegészítője: nem csak mérjük az eltérést, hanem megadjuk, mitől kellene eltérnie. A Navibase alkalmazás: "Organization Values Kit" - strukturált, verziókövetett, auditálható értékkonfiguráció KKV-knak, amely az ops agent "lelkévé" válik. Differenciátor: a Leoni SOUL.md maga is ennek prototípusa.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=4 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-03-31). A tudományos irány és a Leoni belső implementáció egyszerre validálja a thesis-t. Navibase számára ez termék és differenciáló narratíva egyszerre.*

---

## H19 - Operational Reliability Layer (Tooling Commoditization Response)
**Thesis:** Az agent tooling ökoszisztéma gyorsan commoditizálódik: Composio (1000+ app integráció), MCP szabvány terjedése, ClawRun, browser-use - az integráció ma már nem versenyelőny. Aki az integráció rétegen versenyez, elveszíti a differenciálót. Az igazi versenyelőny az operatív megbízhatóság: mennyi agent run végez sikeresen vs. hibával, mennyi emberi beavatkozás kell, mennyi a "silent failure" (agent nem jelez de rosszat csinál). Ez mérhető, kommunikálható, és ma senki nem pozicionálja termékként.
**Signals (updated 2026-03-31):**
- Composio "Universal CLI - Connect AI agents to 1000+ apps" (ProductHunt, 2026-03-27): az integráció réteg commoditizálódik, ez már nem differenciáló. HIGH CONFIDENCE.
- ALTK paper (2026-03-16): "silent reasoning errors, tool argument corruption, policy violations" - a megbízhatóság mérhetővé tétele sürgős. HIGH CONFIDENCE.
- $65M seed enterprise agent startup (TechCrunch, 2026-03-30): az enterprise szegmensbe nagy tőke áramlik - a KKV szegmens az operatív megbízhatóságra fog versenyezni, nem az integrációra. MEDIUM CONFIDENCE.
- CRAFT paper: erősebb modell nem jelent jobb multi-agent koordinációt - a megbízhatóság protokoll és monitoring kérdése, nem modell kérdés. HIGH CONFIDENCE.
**Assessment:** A "reliability SLA" mint termék: az ops agent minden run-nak van státusza, minden hibának van eskalációs protokollja, minden sikernek van auditnyoma. Navibase alkalmazás: "Leoni Ops Reliability Score" - heti KPI dashboard KKV CEO-knak: hány feladat futott le teljesen, hány igényelt emberi beavatkozást, mennyi volt a latency. Ez nem monitoring, hanem üzleti értékjelzés.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-03-31). A tooling commoditizáció signal (Composio) kinyitja azt a kérdést: ha mindenki integrál mindenhová, mi marad a differenciáló? Válasz: az operatív megbízhatóság mérhetősége és kommunikálása.*

---

## Ranking Summary (2026-03-31)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 - Agent Identity & Auth | 21/25 | = |
| 4 | H3 - MCP Governance | 20/25 | = |
| 5 | H12 - Agent Accountability Framework | 20/25 | = |
| 6 | H10 - Agent Infra as Code | 19/25 | = |
| 7 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 8 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 9 | H8 - Cross-Agent Context | 18/25 | = |
| 10 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 11 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 12 | **H16 - AI Alignment Measurement as a Service** | **18/25** | **ÚJ** |
| 13 | **H17 - Controlled Self-Configuration Boundary** | **18/25** | **ÚJ** |
| 14 | **H18 - Organizationally-Aligned AI** | **18/25** | **ÚJ** |
| 15 | **H19 - Operational Reliability Layer** | **18/25** | **ÚJ** |
| 16 | H4 - Agent Payment Rails | 17/25 | = |
| 17 | H11 - Hallucination Self-Check | 17/25 | = |
| 18 | H5 - Discovery & Registry | 16/25 | = |
| 19 | H9 - Agent Communication Infra | 12/25 | = |

*2026-03-31 delta: 4 új hypothesis (H16-H19). Mindegyik 18/25 - erős, de nem dönti el a rangsort a meglévő top 5 ellen. A tooling commoditizáció (H19) és az alignment mérhetőség (H16) a leginkább Navibase-releváns új belépők. Governance és compliance blokk (H1/H2/H6/H12) dominál.*

---

## Top 3 Opportunities + Suggested Experiments (2026-03-31)

### #1: H2 / H6 (tied) - Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** EU AI Act Aug 2026 deadline 4 hónap. Az "agent governance infrastruktura" narratíva mainstream médiában jelent meg (National Today, 2026-03-29) - a CEO-szintű figyelem most nyílt meg. 94% szervezetnél kritikus AI láthatósági hiány. A compliance + security kettős pitch ma a legerősebb nyitó.
**Javasolt kísérlet:** 10 EU-based Claude/GPT production-user enterprise hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit. Mérők: pilot→paid konverzió, árszenzitvitás, compliance framework hivatkozás.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai proof-of-concept a pitchben.

### #2: H19 - Operational Reliability Layer [Score: 18/25 - ÚJ]
**Miért most:** A Composio-féle tooling commoditizáció (2026-03-27) jelzi: aki az integráció rétegen versenyez, elveszít. A differenciáló versenyelőny az operatív megbízhatóság - és ezt ma senki nem kommunikálja termékként. A $65M enterprise seed azt mutatja, hogy az enterprise piac felfelé megy, a KKV szegmensben az "operatív SLA" lesz az értékesítési battleground.
**Javasolt kísérlet:** Leoni ops agent-nél 30 napos reliability tracking: minden run státusz, hiba, eszkaláció, latency. Összefoglalás heti KPI dashboardban Tominak. Ha az adatok jók: ez a KKV pitch centerdarabja. Mérők: run success rate, human-in-the-loop rate, average task completion time.
**Befektetés:** ~3 nap build (Leoni belső monitoring). Azonnali belső adat + KKV pitch anyag.

### #3: H16 - AI Alignment Measurement as a Service [Score: 18/25 - ÚJ]
**Miért most:** A Revealed Preference Framework paper (arxiv, 2026-03-29) tudományos alapot ad a KKV pitchhez: "mérd le, hogy az agented valóban a te értékeidet képviseli-e." Az iProov accountability vacuum narratívával kombinálva ez az adopciós barrier legfőbb elhárítója. Navibase differenciáló: "Leoni Alignment Score" - heti dashboard, hány döntés volt emberi elvárással konzisztens.
**Javasolt kísérlet:** Leoni 30 napos alignment logging pilot: minden döntésnél (email, kanban, cron, git push) rögzítés, hogy emberi utasítással konzisztens volt-e, vagy autonóm eltérés. Heti összesítő Tominak. Mérők: eltérési arány, false autonomy rate, CEO bizalmi szint változása (szubjektív visszajelzés).
**Befektetés:** ~2 nap logging. Azonnali belső érték + pitch anyag a KKV pilotra.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-03-31.md (217 signal, HAIER export) | 2026-03-31 21:50 CET*


---

## H20 - Agent Orchestration Platform as Regulated Infrastructure
**Thesis:** Az AI agentek governance infrastrukturává válnak - a szabályozói figyelem (EU AI Act, NIST) hamarosan nemcsak az egyes AI döntéseket, hanem az agent orchestration platformokat közvetlenül érinti. Ma egyetlen platform sem pozicionálja magát compliance-ready regulated infrastructure-ként. Az "agent nem eszköz, hanem infrastruktúra" narratíva mainstream médiában jelent meg. Aki elsőként pozicionálja a platformját erre a keretre, az standarddá válhat - különösen a KKV szegmensben, ahol a compliance követelmény hamarabb válik belépési feltétellé, mint megkülönböztető előnnyé.
**Signals (updated 2026-04-01):**
- "AI Agents Become Governance Infrastructure" (National Today, 2026-03-29): Az "agent nem eszköz, hanem infrastruktúra" narratíva mainstream médiában jelent meg - az EU AI Act és NIST szabályozás következő célpontja az agent orchestration platform réteg. HIGH CONFIDENCE.
- NIST CAISI "AI Agent Standards Initiative" (2026-02, deadline April 2, 2026): Az agent authentication és authorization concept paper deadline elérte a határidőt - a szabályozás már platform szintre érkezett. HIGH CONFIDENCE.
- EU AI Act Aug 2026 compliance deadline: 4 hónap - a platform szintű compliance-ready pozicionálásra nyitott ablak zárul. HIGH CONFIDENCE.
- $65M seed enterprise agent startup (TechCrunch, 2026-03-30): A VC pénz enterprise szegmensbe áramlik, KKV-fókuszú compliance-ready platform differenciálhat. MEDIUM CONFIDENCE.
- iProov "accountability vacuum" (2026-03-26): A platformszintű felelősség kérdése nyitott - az orchestration layer az első hely, ahol ez kezelhető. HIGH CONFIDENCE.
**Assessment:** Ez nem egy termék feature - ez pozicionálási és go-to-market döntés. A Navibase/Leoni ma már implementálja az audit trail, policy engine, identity scope komponenseket. A kérdés: mikor kommunikálják ezt együtt, mint "compliance-ready platform infrastruktúra"? Az EU AI Act deadline közeledtével ez az üzenet hónapok múlva lesz a legértékesebb - nem évek múlva. Navibase alkalmazás: "Agent Platform Compliance Badge" - egységes EU AI Act readiness kommunikáció, amely H1 + H2 + H6 + H12 signalokat összefogja.
**Scores:** Pain=4 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 21/25**
*Új hypothesis (2026-04-01). A governance infrastruktúra narratíva mainstream megjelenése közvetlen go-to-market trigger. Az urgency 5 mert az EU AI Act deadline 4 hónapon belül van - a compliance positioning window most nyitva van, de zárul.*

---

## H21 - Deterministic Agent Behavior as SMB/Enterprise Trust Signal
**Thesis:** Az önmódosító és önfejlesztő agentek (Phantom, intelligence explosion narratíva) megjelenésével az enterprise és KKV piac kettéválik: "instabil/kísérletező" és "stabil/auditálható" platformok. Az üzleti adopció gátja nem az AI képesség hiánya, hanem a kiszámíthatatlanságtól való félelem. Aki a "determinisztikus, auditálható, stabil agent viselkedés" értékajánlatát a legegyértelműbben kommunikálja, az nyeri el a konzervatívabb - de fizető - enterprise és KKV ügyfelet. A Navibase/Leoni architektúra ezt már implementálja (SOUL.md + AGENTS.md + policy engine), a piac azonban nem tud róla.
**Signals (updated 2026-04-01):**
- "Agentic AI and the next intelligence explosion" (arxiv, 2026-03-30): A self-evolving agent narratíva erősödik - a counternarrative (stabil/auditálható behavior) lesz az enterprise differenciáló. HIGH CONFIDENCE.
- Phantom open-source agent (GitHub ghostwright/phantom, 2026-03-30): Első nyilvános open-source önmódosító agent - megjelent a félelem, és megjelent az igény a kontrollált alternatívára. HIGH CONFIDENCE.
- ALTK paper (arxiv, 2026-03-16): "silent reasoning errors, tool argument corruption" - a kiszámíthatatlanság termelési kockázat, auditable behavior az ellenlábasa. HIGH CONFIDENCE.
- CRAFT paper (arxiv, 2026-03-26): Erősebb modell nem jelent jobb multi-agent koordinációt - a stabilitás protokoll és architektúra kérdése. HIGH CONFIDENCE.
- "Autonomous AI agents in business organizations" (Jerusalem Post, 2026-03-27): KKV döntéshozók is olvassák az autonóm agent témát - a bizalom és a kiszámíthatóság kérdése mainstream. MEDIUM CONFIDENCE.
**Assessment:** Ez elsősorban kommunikációs és pozicionálási lehetőség - a build work már megtörtént. Az IntFric szándékosan alacsony: a Navibase már implementálja a deterministic scope-ot (SOUL.md, AGENTS.md, policy engine, explicit scope boundaries). A piac most kezdi megérteni, miért számít ez. Az "intelligence explosion" narratívára adott válasz a Navibase pitch centereleme lehet: "míg mások az agent képességét mérik, mi az agent megbízhatóságát garantáljuk." Navibase alkalmazás: "Stable Agent Architecture" white paper + KKV pilot pitch deck.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=4 | IntFric=2 | **Total: 18/25**
*Új hypothesis (2026-04-01). A Phantom + intelligence explosion signalok egyszerre nyitják meg a "counternarrative" lehetőséget. A Navibase architektúra az egyetlen eddig látott implementáció, amelynél a scope-hardening production-szinten dokumentált.*

---

## Ranking Summary (2026-04-01)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 - Agent Identity & Auth | 21/25 | = |
| 4 | **H20 - Agent Platform as Regulated Infrastructure** | **21/25** | **ÚJ** |
| 5 | H3 - MCP Governance | 20/25 | = |
| 6 | H12 - Agent Accountability Framework | 20/25 | = |
| 7 | H10 - Agent Infra as Code | 19/25 | = |
| 8 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 9 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 10 | H8 - Cross-Agent Context | 18/25 | = |
| 11 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 12 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 13 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 14 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 15 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 16 | H19 - Operational Reliability Layer | 18/25 | = |
| 17 | **H21 - Deterministic Agent Behavior as Trust Signal** | **18/25** | **ÚJ** |
| 18 | H4 - Agent Payment Rails | 17/25 | = |
| 19 | H11 - Hallucination Self-Check | 17/25 | = |
| 20 | H5 - Discovery & Registry | 16/25 | = |
| 21 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-01 delta: 2 új hypothesis (H20, H21). H20 azonnal a top 4-be kerül 21/25-tel - az "agent platform mint regulated infrastructure" narratíva mainstream megjelenése közvetlen go-to-market trigger. H21 a 18/25 blokkba kerül, de IntFric=2 miatt Navibase-nél a legkisebb build investmenttel megvalósítható új lehetőség.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-01)

### #1: H20 - Agent Platform as Regulated Infrastructure [Score: 21/25 - ÚJ]
**Miért most:** Az "AI agents become governance infrastructure" narratíva (National Today, 2026-03-29) mainstream megjelenése és az EU AI Act Aug 2026 deadline együtt kinyit egy 4 hónapos compliance positioning ablakot. A Navibase ma már implementálja az ehhez szükséges komponenseket (H1+H2+H6+H12). A go-to-market lépés: ezeket egységes "Agent Platform Compliance" narratívába összefogni, mielőtt a $65M-es enterprise szereplők megelőzik a piacot.
**Javasolt kísérlet:** "EU AI Act Agent Compliance Checklist" - 1 oldalas, szabad letöltésű sablon, amely a Navibase komponenseit (audit trail, policy engine, identity, accountability) EU AI Act cikkelyekhez rendeli. Mérők: letöltések, inbound megkeresések, LinkedIn impressions 2 héten belül. Ha 300+ letöltés: fizetős compliance assessment pilot indítás.
**Befektetés:** ~2 nap. Erős thought leadership pozicionálás, közvetlen EU AI Act deadline-ra időzített lead gen.

### #2: H2 / H6 (tied) - Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** Változatlanul a lista legmagasabb score-ú lehetőségei. EU AI Act Aug 2026 deadline 4 hónap. McKinsey hack + Meta rogue agent + iProov accountability vacuum egymást erősítő signalok. A compliance + security kettős pitch ma a legerősebb belépési szög - a H20-val kombinálva platform-szintű narratíva.
**Javasolt kísérlet:** 10 EU-based Claude/GPT production-user enterprise hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit. Mérők: pilot-paid konverzió, árszenzitvitás, compliance framework hivatkozás.
**Befektetés:** ~2 hét fejlesztés. ALTK + Tracium.ai proof-of-concept a pitchben.

### #3: H21 - Deterministic Agent Behavior as SMB/Enterprise Trust Signal [Score: 18/25 - ÚJ]
**Miért most:** A Phantom önmódosító agent (2026-03-30) megjelenése és az "intelligence explosion" narratíva KKV és mainstream sajtóban (Jerusalem Post) egyaránt megjelent. A félelem és a bizalomigény most formálódik. A Navibase build cost nulla - az architektúra létezik. A cost: a kommunikáció megírása. Ez a legmagasabb ROI lehetőség a listán belső erőforrás szempontjából.
**Javasolt kísérlet:** "Stable Agent Architecture" egy oldalas white paper - Navibase/Leoni scope-hardening architektúra bemutatása, összehasonlítás a Phantom-típusú "wild" megközelítéssel. Mérők: elkezdodott.hu blog traffic, LinkedIn engagement, inbound kérdések a "hogyan kontrolláljuk az agent viselkedését" témában. Ha 5 inbound megkeresés: ez a pitch fő differenciálója.
**Befektetés:** ~1 nap tartalom. Azonnali differenciáló kommunikáció. A Leoni belső implementáció maga a proof-of-concept.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-01.md (223 signal, HAIER export) | 2026-04-01 09:30 CET*


---

## H22 - Adversarial Robustness Layer (Production Agent Attack Surface)
**Thesis:** DeepMind 6 dokumentált "csapda" (prompt injection, kontextus manipuláció, tool poisoning stb.) és az Anthropic kódbázis szivárgás egyszerre jelzik: a produkciós agentek ellen már aktív, szervezett támadások futnak. Az eddigi biztonsági fókusz passzív volt (naplózás, audit, izoláció) - nincs olyan réteg, amely aktívan detektálja és blokkolja az adversarial bemeneteket valós időben, KKV-ba is bevezethető formában. A "6 csapda" paper az első széles körben hivatkozott taxonómia, amely konkrét, mérhető attack pattern-eket nevesít. Erre lehet védelmi terméket építeni.
**Signals (updated 2026-04-02):**
- Google DeepMind: "6 csapda autonóm agenteknek" (the-decoder.com, 2026-04-01): prompt injection, kontextus manipuláció, tool poisoning, identity spoofing stb. - első publikus, hivatkozott taxonómia produkciós agent attack pattern-ekre. HIGH CONFIDENCE.
- Anthropic Claude kódbázis szivárgás (WSJ, 2026-04-01): az agent-infrastruktúra IP-je aktív célpont - a támadási motiváció bizonyított. HIGH CONFIDENCE.
- Mutation Testing for the Agentic Era (Trail of Bits, 2026-04-01): a hagyományos szoftvertesztelés nem alkalmas agent robustness mérésére - új mérési keretrendszer szükséges. HIGH CONFIDENCE.
- Autonomous pentest agent (vxcontrol/pentagi): teljesen autonóm támadóeszközök elérhetők - a védelem reaktívból proaktívvá kell váljon. HIGH CONFIDENCE.
- Open-source red-team playground (HN, 2026-03-15): "We kept finding the same types of vulnerabilities" - a 6 DeepMind attack type nem elméleti, production-ban dokumentált. HIGH CONFIDENCE.
**Assessment:** A DeepMind taxonómia kinyitja a "robustness layer" termékpozíciót: nem generic biztonsági eszköz, hanem kimondottan az ismert agent-specifikus attack pattern-ekre tervezett valós idejű shield. A KKV pitch: "a legjobb agented is becsapható 6 ismert módszerrel - mi blokkoljuk mind a hatot." A Trail of Bits mutation testing paper az auditálási metrikát adja hozzá. Navibase alkalmazás: Leoni bemeneti validáció + kontextus-integritás ellenőrzés a 6 DeepMind pattern alapján.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Új hypothesis (2026-04-02). DeepMind taxonómia + Anthropic szivárgás egymást erősítő, magas bizalmú signalok. A score 22/25 - azonnal a lista csúcsára kerül H2 és H6 mellé. Az adversarial attack téma a 2026 Q2 leggyorsabban növekvő agent security szegmense.*

---

## H23 - Agentic QA & Mutation Testing as a Service
**Thesis:** A hagyományos szoftvertesztelési módszerek (unit test, integration test) nem alkalmasak autonóm agent viselkedés ellenőrzésére. Trail of Bits paper (2026-04-01) megmutatja: mutation testing szükséges - az agent döntési logikájának szándékos mutálásával mérhető, hogy mennyire robusztus és kiszámítható a viselkedés. Ez ma nincs termékkénnt elérhetően - sem önállóan, sem CI/CD pipeline-ba integrálva. Az "agentic QA" kategória még nem létezik, de az igény (audit, compliance, production reliability) már megvan.
**Signals (updated 2026-04-02):**
- Mutation Testing for the Agentic Era (Trail of Bits blog, 2026-04-01): hagyományos tesztelés elégtelen, mutation testing szükséges agent robustness méréshez - közvetlen kategória-definíciós paper egy high-credibility biztonsági cégtől. HIGH CONFIDENCE.
- ALTK paper (arxiv, 2026-03-16): "silent reasoning errors go undetected" - a QA gap production-ban dokumentált. HIGH CONFIDENCE.
- AWS DevOps/Security agentek deployment (Forbes, 2026-04-01): enterprise szinten megjelenik az agent-alapú DevOps - a CI/CD pipeline-ba integrált agentic QA természetes következő lépés. MEDIUM CONFIDENCE.
- Claude Code (GitHub trending, 2026-04-02): a coding agent tooling mainstream - minden coding agent deploymentnél felvetődik a "hogyan tesztelünk" kérdés. MEDIUM CONFIDENCE.
- ChatDev 2.0 (GitHub trending, 2026-04-01): multi-agent szoftverfejlesztés terjedése - az agentic QA igénye skálázódik. MEDIUM CONFIDENCE.
**Assessment:** Ez a H2 (audit trail) és H17 (controlled self-configuration) metszéspontja, de specifikusan a szoftverfejlesztési és CI/CD pipeline-ra fókuszál. A Trail of Bits mint high-credibility forrás maga validálja a kategoriat - ami nem mainstream biztonsági fórumon jelent meg, az tudományos/ipari referencia szinten érkezik. Navibase alkalmazás: Leoni agent deployment pipeline-jában agentic mutation test checkpoint - minden konfiguráció változás előtt automatikus robustness check.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-02). Trail of Bits paper közvetlen kategória-definíció. Az "agentic QA" tér ma üres - az első szereplőnek thought leadership és tooling előnye van. 2026 Q3-ra várható a CI/CD integrációs igény felfutása.*

---

## Ranking Summary (2026-04-02)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | **H22 - Adversarial Robustness Layer** | **22/25** | **ÚJ** |
| 4 | H1 - Agent Identity & Auth | 21/25 | = |
| 5 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H3 - MCP Governance | 20/25 | = |
| 7 | H12 - Agent Accountability Framework | 20/25 | = |
| 8 | H10 - Agent Infra as Code | 19/25 | = |
| 9 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 10 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 11 | H8 - Cross-Agent Context | 18/25 | = |
| 12 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 13 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 14 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 15 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 16 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 17 | H19 - Operational Reliability Layer | 18/25 | = |
| 18 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 19 | **H23 - Agentic QA & Mutation Testing as a Service** | **18/25** | **ÚJ** |
| 20 | H4 - Agent Payment Rails | 17/25 | = |
| 21 | H11 - Hallucination Self-Check | 17/25 | = |
| 22 | H5 - Discovery & Registry | 16/25 | = |
| 23 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-02 delta: 2 új hypothesis (H22, H23). H22 azonnal a top 3-ba kerül 22/25-tel - a DeepMind 6 trap taxonómia + Anthropic szivárgás együttesen az adversarial robustness témát az audit/policy mellé emeli. H23 a 18/25 blokkba kerül mint üres kategória-definíció. Az EU AI Act Aug 2026 deadline közeledtével a teljes governance/security blokk (H1/H2/H6/H12/H20/H22) egyre szorosabb.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-02)

### #1: H22 - Adversarial Robustness Layer [Score: 22/25 - ÚJ]
**Miért most:** A DeepMind 6 csapda paper az első széles körben hivatkozott, konkrét attack taxonómia produkciós agentekre. Az Anthropic kódszivárgás igazolja: az agent infrastruktúra aktív célpont. Ez nem jövőbeli kockázat - ez ma már aktív fenyegetés. A piac még nem rendelkezik termékkel, amely kifejezetten ezt a 6 attack pattern-t blokkolja KKV-ba is bevezethető formában. Az ablak szűk: a következő 2-3 hónapban security-fókuszú startupok fognak erre belépni.
**Javasolt kísérlet:** Leoni-ban a bemeneti pipeline elé egy "adversarial check" réteg prototípusa: a 6 DeepMind attack típust ellenőrző validációs logika (prompt injection detektor, kontextus-integritás check, tool call anomaly). Mérők: false positive arány (helyes bemenetet blokkol), true positive arány (valódi attack-ot megfog), latency overhead. 2 hetes prototípus. Ha működik: "Leoni Security Shield" KKV pitch elem.
**Befektetés:** ~1 hét build. DeepMind paper maga a spec - szabad felhasználású, magas hitelességű forrás.

### #2: H2 / H6 (tied) - Audit Trail + Policy Enforcement Runtime [Score: 22/25]
**Miért most:** Változatlanul a lista legmagasabb score-ú lehetőségei. EU AI Act Aug 2026 deadline most már 4 hónap. Az új H22 signal (DeepMind + Anthropic) tovább erősíti a biztonsági narratívát - a compliance + security + adversarial robustness hármas pitch az erősebb belépési szög mint korábban. H20-val kombinálva platform-szintű narratíva.
**Javasolt kísérlet:** 10 EU-based Claude/GPT production-user enterprise hideg megkeresés. Ajánlat: 30 napos ingyenes EU AI Act compliance audit + adversarial exposure scan (6 DeepMind pattern-re). Mérők: pilot-paid konverzió, compliance framework hivatkozás, security-driven vs. compliance-driven inbound arány.
**Befektetés:** ~2 hét fejlesztés. A H22 prototípus + meglévő ALTK proof-of-concept együtt erős demo.

### #3: H20 - Agent Platform as Regulated Infrastructure [Score: 21/25]
**Miért most:** Az EU AI Act Aug 2026 deadline most 4 hónap - a compliance positioning window gyorsan zárul. A DeepMind/Anthropic adversarial signalok (H22) tovább erősítik a "platform-szintű compliance" narratívát: nem elég az audit log, a platform maga legyen hardened és deklaráltan compliance-ready. A Navibase ma implementálja az összes szükséges komponenst - a kommunikáció hiányzik.
**Javasolt kísérlet:** "EU AI Act Agent Compliance Checklist" 1 oldalas sablon - Navibase komponensek (H1+H2+H6+H12+H22) EU AI Act cikkelyekhez rendelve + DeepMind 6 attack pattern-re vonatkozó védelmi intézkedések listája. Mérők: letöltések, inbound megkeresések, LinkedIn impressions 2 héten belül. Ha 300+ letöltés: fizetős compliance assessment pilot.
**Befektetés:** ~2 nap. A H22 friss paper thought leadership momentum-mal tölti meg a checklist-et.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-02.md (232 signal, HAIER export) | 2026-04-02 09:30 CET*


---

## H24 - Shadow AI / Unmanaged Agent Governance Plane
**Thesis:** Ahogy a nagy szervezetekben megjelennek az első, "munkát végző" autonóm agentek (DevOps, SecOps, support, procurement), megjelenik a következő probléma: a nem jóváhagyott, csapatok által "sunny side" módon bevezetett agentek (shadow AI) gyorsabban szaporodnak, mint ahogy a central governance reagálni tudna. Kell egy dedikált governance plane, ami felderíti, inventory-zza és folyamatosan kontrollálja a nem menedzselt agenteket (policy, audit, kill switch, ownership, escalation). Ez nem MCP governance (H3) és nem csak audit trail (H2), hanem kifejezetten a shadow AI "operatív" problémájára épített termékkategória.
**Signals (updated 2026-04-03):**
- KiloClaw: shadow AI + autonomous agent governance (AI News, 2026-04-02) - explicit kategória-nevesítés ("shadow AI") + termékpozíció. HIGH CONFIDENCE.
- AWS: AI agentek DevOps és Security csapatok munkájára (Forbes, 2026-04-01) - a "working agents" enterprise-be kerülnek, ezzel a shadow deployment valószínűsége nő. HIGH CONFIDENCE (vendor signal).
- EU AI Act Aug 2026 (korábbi) - ha az agent döntést hoz vagy adatot mozgat, a governance hiánya audit/compliance kockázat. HIGH CONFIDENCE (regulatory).
**Assessment:** A "shadow AI" az a wedge, ami a governance piacot az IT/security buyerhez köti: inventory + risk scoring + containment. Moat lehetőség: agent-felderítés (network + API + identity graph), folyamatos policy enforcement, és audit-ready jelentések.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=3 | IntFric=3 | **Total: 21/25**
*Új hypothesis (2026-04-03). A KiloClaw explicit shadow AI pozicionálása erős validáció, az AWS vendor signal pedig azt jelzi: ez nem kutatás, hanem deploy.*

---

## H25 - Developer Multi-Agent Workspace Orchestration (Worktrees, Sessions, Review)
**Thesis:** A terminal-native coding agentek (Claude Code, stb.) és a multi-agent dev flow-k gyorsan terjednek, de a fejlesztők operatív fájdalma nem a modell-képesség, hanem a "túl sok agent, túl sok worktree" kezelése: state, státusz, párhuzamos futások, review, és a hibák visszakövetése. A piacnak szüksége van egy "agent workspace orchestrator" rétegre: agent/session dashboard, worktree lifecycle, run log + diff review, policies (mit csinálhat egy agent), és költség/limit menedzsment.
**Signals (updated 2026-04-03):**
- Anthropic Claude Code (GitHub, 2026-04-02) - első-party, terminal-native agent eszköz -> tömeges elterjedés. HIGH CONFIDENCE.
- Show HN: Baton - desktop app multi-agent worktree managementhez (2026-04-01) - közvetlen practitioner pain: "messy" agent/worktree kezelés. HIGH CONFIDENCE.
- ChatDev 2.0 (GitHub, 2026-04-01) - multi-agent collaboration mainstream open-source mintázat. MEDIUM CONFIDENCE.
**Assessment:** Ez devtool kategória, gyors adoption, de moatozás nehezebb. A value: "agent fleet control plane" a fejlesztő gépen, enterprise security hookkal (policy, audit).
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=2 | IntFric=2 | **Total: 16/25**
*Új hypothesis (2026-04-03). Baton és Claude Code együtt jelzi: a multi-agent dev már operációs probléma, nem novelty.*

---

## H26 - Vertical Agent Copilots in Legacy Plugin Ecosystems (WordPress wedge)
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
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 - Agent Identity & Auth | 21/25 | = |
| 5 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | **H24 - Shadow AI Governance Plane** | **21/25** | **ÚJ** |
| 7 | H3 - MCP Governance | 20/25 | = |
| 8 | H12 - Agent Accountability Framework | 20/25 | = |
| 9 | H10 - Agent Infra as Code | 19/25 | = |
| 10 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 11 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 12 | H8 - Cross-Agent Context | 18/25 | = |
| 13 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 14 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 15 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 16 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 17 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 18 | H19 - Operational Reliability Layer | 18/25 | = |
| 19 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 20 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 21 | H4 - Agent Payment Rails | 17/25 | = |
| 22 | H11 - Hallucination Self-Check | 17/25 | = |
| 23 | H5 - Discovery & Registry | 16/25 | = |
| 24 | **H25 - Developer Multi-Agent Workspace Orchestration** | **16/25** | **ÚJ** |
| 25 | H9 - Agent Communication Infra | 12/25 | = |
| 26 | **H26 - WordPress/Plugin Ecosystem Vertical Copilots** | **14/25** | **ÚJ** |

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

## H27 - Agent Packaging & Portability Standard (Repo-as-Agent Spec)
**Thesis:** Ahogy az agent-ek eszköztár- és runtime-ökoszisztémája szétágazik (OpenAI/Anthropic tooling, MCP, GitOps runtimes, IDE agentek), a legnagyobb friction a *portabilitás*: ugyanazt az agentet új framework-be vinni ma szinte újraírás. Kell egy framework-agnosztikus, fájl-alapú "agent manifest/spec" (policy, tool-permission, runbook, audit hook, teszt checkpoint), ami bármely runtime-ba importálható. Aki ezt standardizálja, az "agent packaging layer" kategóriát birtokolhatja.
**Signals (updated 2026-04-04):**
- GitAgent (HN, 2026-03-14): "open standard that turns any Git repo into an AI agent" - explicit igény a repo-as-agent definícióra és interoperabilitásra. HIGH CONFIDENCE.
- Orloj (2026-03-26): YAML/GitOps policy-first agent infra - a spec-alapú agent lifecycle mintázat már megjelent. HIGH CONFIDENCE.
- Claude Code + több terminal agent (2026-04 eleje): agent definíciók és workflow-k "szétszóródnak" IDE/CLI között - portability pain nő. MEDIUM CONFIDENCE.
**Assessment:** Ez a H10 (Infra as Code) és H5 (Discovery) közé ékelődő, de külön kategória: nem csak policy deklarálás, hanem *agent csomagolás + import/export*. Navibase alkalmazás: egy "Navibase Agent Pack" formátum, ami a SOUL/AGENTS/policy + skill manifesteket standardizálja, és később külső partnereknek is átadható.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-04). A GitAgent explicit standard jelzés. A moat a specifikáció + referencia implementáció + template library kombinációja.*

---

## H28 - Bias/Fairness Governance for Agentic Decision Delegation
**Thesis:** A decision delegation (agent ajánl, rangsorol, döntéstámogat) gyorsan beleütközik a fairness/transparency/compliance falba: a szervezetnek bizonyítania kell, hogy a rendszer nem diszkriminál, és hogy a döntési logika auditálható. A mai governance eszközök főleg naplóznak (H2) és policy-t enforce-olnak (H6), de ritkán adnak *fairness/bias* metrikát és "explainability-ready" dokumentációt agent workflow szinten. Ez külön wedge lehet compliance buyer felé.
**Signals (updated 2026-04-04):**
- "Algorithmic bias, data ethics, and governance..." (Semantic Scholar, 2025-02-28) - fairness + governance + compliance fókusz ADM környezetben. HIGH CONFIDENCE.
- "Ethics of Using Data in Automated Decision-Making..." (Semantic Scholar, 2025-09-01) - transparency + institutional accountability mint mainstream research téma. HIGH CONFIDENCE.
- "Ethics and Fairness in Conversational AI..." (Semantic Scholar, 2025-11-01) - LLM-alapú conversational rendszerekben bias framework-ek formálódnak. MEDIUM CONFIDENCE.
- EU AI Act Aug 2026: high-risk AI decisions dokumentálása és megfelelősége kötelező (korábbi signal) - fairness dokumentáció várhatóan besorolási kérdéssé válik. HIGH CONFIDENCE.
**Assessment:** Ez nem újraírja a H2/H6-ot, hanem *ráépül*: audit trail + policy enforcement mellé "fairness evidence pack" kell. Navibase alkalmazás: "Decision Delegation Fairness Report" modul (agent run sample-set, drift check, bias checklist, audit-ready export), amit enterprise-nél compliance csapat tud használni, KKV-nél pedig bizalomépítő dokumentum.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-04). Research jellegű signalok, de compliance-ablakkal (EU AI Act) kombinálva gyorsan termék- és szolgáltatás-wedge lehet.*

---

## Ranking Summary (2026-04-04)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 - Agent Identity & Auth | 21/25 | = |
| 5 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H24 - Shadow AI Governance Plane | 21/25 | = |
| 7 | H3 - MCP Governance | 20/25 | = |
| 8 | H12 - Agent Accountability Framework | 20/25 | = |
| 9 | H10 - Agent Infra as Code | 19/25 | = |
| 10 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 11 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 12 | H8 - Cross-Agent Context | 18/25 | = |
| 13 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 14 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 15 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 16 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 17 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 18 | H19 - Operational Reliability Layer | 18/25 | = |
| 19 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 20 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 21 | **H28 - Bias/Fairness Governance** | **18/25** | **ÚJ** |
| 22 | H4 - Agent Payment Rails | 17/25 | = |
| 23 | H11 - Hallucination Self-Check | 17/25 | = |
| 24 | **H27 - Agent Packaging & Portability Spec** | **17/25** | **ÚJ** |
| 25 | H5 - Discovery & Registry | 16/25 | = |
| 26 | H25 - Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 27 | H26 - WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 28 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-04 delta: 2 új hypothesis (H27, H28). A security/governance blokk továbbra is domináns (H2/H6/H22/H24). H27 portability/spec irány, H28 fairness/bias compliance wedge.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-04)

### #1: H22 + H24 combo - Shadow Agent Exposure + Adversarial Robustness
**Miért most:** A "shadow AI" narratíva buyer-hez köt (IT/security), a DeepMind taxonómia pedig konkrét, értékes "scan spec"-et ad. Ez a leggyorsabb út fizetős pilothoz.
**Javasolt kísérlet:** "Shadow Agent Exposure Scan" 5 EU cégnek (2 hét): inventory + 6-trap exposure score + quick fixes, audit exporttal. Mérők: meeting->pilot, pilot->paid, leggyakoribb kontrolligény.

### #2: H20 - Agent Platform as Regulated Infrastructure (Packaging)
**Miért most:** EU AI Act Aug 2026 közel. A piac nem feature-t vesz, hanem "compliance-ready" narratívát és dokumentálhatóságot. A Navibase-nél a komponensek megvannak, a csomagolás a bottleneck.
**Javasolt kísérlet:** 1 oldalas "EU AI Act Agent Compliance Mapping" + letölthető checklist. Mérők: letöltés, inbound meeting, "melyik cikkely fáj legjobban" visszajelzés.

### #3: H28 - Bias/Fairness Governance wedge (Decision Delegation)
**Miért most:** A fairness/bias governance irodalom sűrűsödik, és compliance oldalon ez hamar "kérdezni fogják" tétel. Aki tud gyors, auditálható evidence pack-et adni, az nyer.
**Javasolt kísérlet:** "Decision Delegation Fairness Pack" pilot 1 design partnerrel: 30 agent run mintavételezés + bias checklist + explainability-ready export. Mérők: compliance csapat feedback, time-to-approve csökkenés, audit readiness.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-04.md | 2026-04-04 09:30 CET*

---

# Update - 2026-04-05

## H29 - Agent Cost Governance & Token Budget Enforcement Plane
**Thesis:** A multi-agent rendszerek egyik leggyorsabban fájó production problémája a kontrollálhatatlan token költség. A provider oldali limitek (account-level cap) utólagosak: azt mutatják, mi történt, nem azt, mi történik. A csapatoknak kell egy runtime szintű költség- és token budget enforcement réteg: threshold alapú warn/degrade/block, auditálható döntésekkel, több agent és több toolchain (LangChain/CrewAI/AutoGen/MCP) felett.
**Signals (updated 2026-04-05):**
- Tokencap (HN/GitHub, 2026-04-04): token budget enforcement wrapper + threshold akciók (WARN/DEGRADE/BLOCK/WEBHOOK), SQLite/Redis backend, framework patching támogatás. HIGH CONFIDENCE.
- Egyre több agent devtool/platform jel (Microsoft agent-framework, goose, Claude Code) -> több párhuzamos agent run, a költségkockázat gyorsan skálázódik. MEDIUM CONFIDENCE.
**Assessment:** Ez a H19 (Operational Reliability) pénzügyi testvére: nem csak azt méred, hogy sikerült-e, hanem azt is, hogy mennyibe került és mikor kell beavatkozni. Buyer: engineering lead, platform team, CFO-érzékeny ops vezető. Navibase alkalmazás: "Agent Budget Guard" (per-agent / per-customer / per-workflow budget, automatikus degrade policy, audit export).
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-05). A Tokencap egy direkt, high-signal validáció: ez már nem "nice-to-have", hanem production control gap.*


## Ranking Summary (2026-04-05)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 - Agent Identity & Auth | 21/25 | = |
| 5 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H24 - Shadow AI Governance Plane | 21/25 | = |
| 7 | H3 - MCP Governance | 20/25 | = |
| 8 | H12 - Agent Accountability Framework | 20/25 | = |
| 9 | H10 - Agent Infra as Code | 19/25 | = |
| 10 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 11 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 12 | H8 - Cross-Agent Context | 18/25 | = |
| 13 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 14 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 15 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 16 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 17 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 18 | H19 - Operational Reliability Layer | 18/25 | = |
| 19 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 20 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 21 | H28 - Bias/Fairness Governance | 18/25 | = |
| 22 | H4 - Agent Payment Rails | 17/25 | = |
| 23 | H11 - Hallucination Self-Check | 17/25 | = |
| 24 | H27 - Agent Packaging & Portability Spec | 17/25 | = |
| 25 | **H29 - Cost Governance & Token Budget Enforcement** | **17/25** | **ÚJ** |
| 26 | H5 - Discovery & Registry | 16/25 | = |
| 27 | H25 - Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 28 | H26 - WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 29 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-05 delta: 1 új hypothesis (H29). A napi signalok (Tokencap + agent frameworkek) azt jelzik, hogy a költség-kontroll gyorsan "table stakes" lesz a production agent üzemeltetésben.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-05)

### #1: H22 + H24 combo - Shadow Agent Exposure + Adversarial Robustness
**Miért most:** Shadow AI buyer (IT/security) + DeepMind 6 trap mint specifikáció. Gyors, mérhető audit deliverable.
**Javasolt kísérlet:** "Shadow Agent Exposure Scan" 5 EU cégnek: inventory + 6-trap exposure score + quick fixes + audit export. Mérők: meeting->pilot, pilot->paid, top 5 control request.

### #2: H20 - Agent Platform as Regulated Infrastructure (Packaging)
**Miért most:** EU AI Act Aug 2026. A piac dokumentálhatóságot vesz, nem feature listát.
**Javasolt kísérlet:** 1 oldalas "EU AI Act Agent Compliance Mapping" (H1+H2+H6+H12+H22) + checklist, 10 célzott outreach. Mérők: letöltés, inbound meeting, compliance kérdések.

### #3: H29 - Agent Cost Governance & Token Budget Enforcement
**Miért most:** A költség-szivárgás a leggyorsabban észlelt production fájdalom. A Tokencap validálja, hogy már van "új kategória".
**Javasolt kísérlet:** Navibase/Leoni "Budget Guard" MVP belsőn: per-run token tracking + threshold (warn/degrade/block) + heti cost report. Mérők: költség-variancia csökkenés, run-fail arány változás, user elégedettség (nem zavaró throttle).

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-05.md | 2026-04-05 09:30 CET*


---

# Update - 2026-04-06

## H30 - MCP-based Agent Trading Protocol & Risk Governance Layer
**Thesis:** Ahogy a trading (forex/crypto/equities) domain-ben megjelennek az autonóm agentek, a legnagyobb hiány nem a stratégiákban, hanem a **standardizált, auditálható és kockázat-korlátozott execution layer-ben** van. Ma mindenki ad-hoc köt broker API-ra, nincs deklaratív risk-limit (position sizing, max drawdown, kill switch), nincs egységes audit trail a tool call-okhoz, és nincs "compliance-ready" agent trading protokoll. Egy MCP-alapú standard/protokoll a trading agentekhez (order intents, approval gates, risk policy, audit export) a következő "infrastructure layer" lehet.
**Signals (updated 2026-04-06):**
- Apex Protocol - an open MCP-based standard for AI agent trading (apexstandard.org, 2026-04-06) - explicit standardizációs kísérlet a trading agentekre. HIGH CONFIDENCE.
- TradingAgents multi-agent trading framework (GitHub, 2026-03-21) - domain agentek proliferálnak, execution + governance gap nő. MEDIUM CONFIDENCE.
- EU AI Act Aug 2026 + audit/policy trend (korábbi H1/H2/H6/H20) - high-risk döntések és pénzügyi műveletek auditálhatósága és kontrollja "table stakes" irányba megy. HIGH CONFIDENCE.
**Assessment:** A moat nem a stratégia, hanem a **risk + audit + approval** standard és a broker-connectorok. Navibase alkalmazás: "Trading Ops Agent" csak akkor skálázható, ha a risk policy és a felelősségi határok deklaratívak.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=4 | **Total: 20/25**
*Új hypothesis (2026-04-06). Az Apex Protocol konkrét jel, hogy a piac standardot keres. A termék-wedge: risk governance + audit export, nem "jobb trading stratégia".*

---

## H31 - Agent-Native Knowledge Base for Complex Office Files (Local-first)
**Thesis:** Az SMB ops agentek legnehezebb inputja nem web, hanem **helyi, komplex office fájlok** (Excel, többféle PDF, szerződés verziók, e-mail exportok). A klasszikus RAG/KB rendszerek itt elbuknak: nem értik a táblázat-struktúrát, nem kezelik jól a verziókövetést, és nem adnak "repo-native" workflow-t (diff, cite, provenance). Kell egy agent-native, local-first knowledge base réteg, ami a "messy office" fájlhalmazt megbízhatóan kereshetővé és hivatkozhatóvá teszi.
**Signals (updated 2026-04-06):**
- Show HN: DocMason - Agent Knowledge Base for local complex office files (GitHub, 2026-04-04) - explicit pain + megoldási irány. HIGH CONFIDENCE.
- dmtrKovalenko/fff.nvim - fast file search toolkit for AI agents (GitHub, 2026-04-04) - a file-level retrieval agent primitive lesz. MEDIUM CONFIDENCE.
**Assessment:** KKV-nál az első kérdés: "a saját fájljaimból dolgozik-e és vissza tudom-e követni?" A differenciáló: citations + provenance + version-aware indexing.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=3 | IntFric=3 | **Total: 17/25**
*Új hypothesis (2026-04-06). A DocMason közvetlen validáció: az agentek KB-ja nem csak "docs", hanem office-file reality.*

---

## Ranking Summary (2026-04-06)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 - Agent Identity & Auth | 21/25 | = |
| 5 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H24 - Shadow AI Governance Plane | 21/25 | = |
| 7 | H3 - MCP Governance | 20/25 | = |
| 8 | H12 - Agent Accountability Framework | 20/25 | = |
| 9 | **H30 - Agent Trading Protocol & Risk Governance** | **20/25** | **ÚJ** |
| 10 | H10 - Agent Infra as Code | 19/25 | = |
| 11 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 12 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 13 | H8 - Cross-Agent Context | 18/25 | = |
| 14 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 15 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 16 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 17 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 18 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 19 | H19 - Operational Reliability Layer | 18/25 | = |
| 20 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 21 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 22 | H28 - Bias/Fairness Governance | 18/25 | = |
| 23 | H4 - Agent Payment Rails | 17/25 | = |
| 24 | H11 - Hallucination Self-Check | 17/25 | = |
| 25 | H27 - Agent Packaging & Portability Spec | 17/25 | = |
| 26 | H29 - Cost Governance & Token Budget Enforcement | 17/25 | = |
| 27 | **H31 - Agent-Native KB for Office Files** | **17/25** | **ÚJ** |
| 28 | H5 - Discovery & Registry | 16/25 | = |
| 29 | H25 - Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 30 | H26 - WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 31 | H9 - Agent Communication Infra | 12/25 | = |

---

## Top 3 Opportunities + Suggested Experiments (2026-04-06)

### #1: H22 + H24 combo - Shadow Agent Exposure Scan + Adversarial Shield
**Miért most:** Shadow AI buyer (IT/security) + DeepMind 6 trap mint kőkemény scan spec. Ez a leggyorsabb "audit deliverable" út fizetős pilothoz.
**Javasolt kísérlet:** 5 EU cégnek 2 hetes "Shadow Agent Exposure Scan": inventory + 6-trap exposure score + quick fixes + audit export. Mérők: meeting->pilot, pilot->paid, top 5 control request.

### #2: H20 - Agent Platform as Regulated Infrastructure (EU AI Act packaging)
**Miért most:** EU AI Act Aug 2026 deadline közel. A compliance-ready platform narratíva most válik belépési feltétellé.
**Javasolt kísérlet:** 1 oldalas "EU AI Act Agent Compliance Mapping" (H1+H2+H6+H12+H22) + letölthető checklist + 10 célzott outreach. Mérők: letöltés, inbound meeting, "melyik cikkely fáj" visszajelzés.

### #3: H30 - Agent Trading Protocol & Risk Governance (Apex wedge)
**Miért most:** Az Apex Protocol explicit standard-signal. A trading agenteknél a WTP nem "jobb prompt", hanem risk limit + audit + approval.
**Javasolt kísérlet:** 1 hetes prototípus: "Trading MCP Gateway" (csak paper-trading / demo): order-intent schema + risk policy (max loss/nap, max position size) + immutable audit log export. Mérők: 3 domain feedback (trader/dev), implementációs friction (broker API), és hogy mely policy-k a minimum elvárt.

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-06.md | 2026-04-06 09:30 CET*


---

# Update - 2026-04-07

## H32 - Continuous Agent Harness Improvement from Production Traces
**Thesis:** Production agenteknél a "harness" (promptok, tool policy-k, workflow lépések, retry/guardrail logika) gyorsan elavul és driftel. A mai gyakorlat: kézzel nézzük a trace-eket és kézzel javítunk. Kell egy trace-to-patch réteg: a production trace-ekből automatikusan hibamintákat azonosít, kiértékel, és javaslatot tesz prompt/workflow/policy módosításokra, auditálható módon.

**Signals (updated 2026-04-07):**
- Show HN: **meta-agent** (GitHub, 2026-04-06): "automatically and continuously improves agent harnesses from production traces". HIGH CONFIDENCE.
- **ALTK** paper (arxiv, 2026-03-16): a production failure mode-ok (silent reasoning error, tool argument corruption, policy violation) rendszerszinten jelennek meg; improvement loop nélkül csak tűzoltás lesz. HIGH CONFIDENCE.

**Assessment:** Navibase/Leoni esetben a run log + outcome már most rendelkezésre áll (cron/task, tool-call, hiba). Egy "trace-to-patch" loop közvetlenül csökkenti a human-in-the-loop terhelést és növeli a reliability-t (H19), miközben dokumentálható (H2).

**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-07). A meta-agent jel egyértelmű: a következő réteg nem új agent framework, hanem a production trace-ekből táplált folyamatos javítási pipeline.*

---

## H33 - Multi-Agent Influence Governance (Constitutional / Anti-Manipulation Layer)
**Thesis:** Multi-agent rendszerekben az agentek nem csak eszközöket használnak, hanem egymást is befolyásolják: meggyőzés, koalíció, collusion, cél-eltolódás. Egy enterprise buyernek nem elég a tool permission (H6) és az audit log (H2) - kell egy governance réteg, ami explicit "constitutiót" ad a multi-agent populációnak (szerepkörök, szavazási szabályok, veto/override, influence detection), és ebből compliance-ready bizonyítékot gyárt.

**Signals (updated 2026-04-07):**
- **LLM Constitutional Multi-Agent Governance** (arxiv, 2026-03-13): a modellek képesek persuasív influence stratégiákra, amelyek megváltoztatják a kooperációt - kérdés, hogy ez valódi proszociális eredmény-e vagy manipuláció. HIGH CONFIDENCE.
- **Regulating AI Agents** (arxiv, 2026-03-24): mainstream szabályozói fókusz autonóm cselekvés + limitált emberi felügyelet mellett - multi-agent governance mint következő célterület. HIGH CONFIDENCE.

**Assessment:** Rövid távon nehezebb termékké tenni (komplex, kevés buyer language), de magas Def potenciál: aki először szabványosítja a "multi-agent constitution + evidence pack" gondolkodást, az előnybe kerülhet a nagy enterprise multi-agent deployment hullámban.

**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=4 | IntFric=4 | **Total: 18/25**
*Új hypothesis (2026-04-07). A constitutional governance paper explicit jelzés: a következő governance fájdalom az agent-to-agent influence kontrollja lesz, nem csak a tool hozzáférés.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-07)

### #1: H22 + H24 combo - Shadow Agent Exposure Scan + Adversarial Shield
**Miért most:** A buyer (IT/security) azonnali fájdalmat érez (shadow agent inventory + containment), a DeepMind 6 trap pedig konkrét "scan spec"-et ad.
**Javasolt kísérlet:** 5 EU cégnek 2 hetes "Shadow Agent Exposure Scan": inventory + 6-trap exposure score + quick fixes + audit export. Mérők: meeting->pilot, pilot->paid, top 5 control request.

### #2: H32 - Trace-to-Patch Harness Improvement (belső gyors ROI)
**Miért most:** A meta-agent jelzi, hogy a "production trace-driven improvement" elkezdett standard mintává válni.
**Javasolt kísérlet:** 14 napos belső pilot Leoni-n: (1) top 20 failure pattern automatikus klaszterezése trace-ekből, (2) heti 5 "patch proposal" (prompt/policy/workflow) + A/B vagy holdout validáció. Mérők: run success rate, human intervention rate, regressziók száma.

### #3: H20 - Agent Platform as Regulated Infrastructure (packaging)
**Miért most:** EU AI Act Aug 2026 ablak zárul; a compliance-ready platform narratíva most belépési feltétellé válik.
**Javasolt kísérlet:** 1 oldalas "EU AI Act Agent Compliance Mapping" (H1+H2+H6+H12+H22) + letölthető checklist + 10 célzott outreach. Mérők: letöltés, inbound meeting, "melyik cikkely fáj" visszajelzés.

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-07.md | 2026-04-07 09:30 CET*


---

# Update - 2026-04-11

## H40 - Agent Identity & Attestation for Delegated Workloads (Workload-to-Agent)
**Thesis:** Az agent identity (H1) implementációja a "workload-to-agent" attestation mintázat felé konszolidálódik: az agent futtatási workload kap rövid életű, igazolt identitást (mTLS/JWT), ami a delegáció kontextusához kötött. Ez egyszerre ad scoped hozzáférést, audit korrelációt, és egyértelmű választ a compliance kérdésre: "ki az agent, miért és milyen jogosultsággal cselekedett?"
**Signals (updated 2026-04-11):**
- Agent Identity Standards consolidate around workload-to-agent attestation (2026-04-10) - attestation-first identity minta. HIGH CONFIDENCE.
- Identity providers add "Agent" as first-class principal type (2026-04-05) - agent principalok külön kezelése. HIGH CONFIDENCE.
- Authentication for tool servers moves toward mTLS + JWT (2026-03-28) - a technikai forma stabilizálódik. HIGH CONFIDENCE.
**Assessment:** Ez a H1 "legvalószínűbb kivitelezési formája". Navibase alkalmazás: per-run issued tokenek + delegation chain id, ami mind auditban (H2), mind policy-ben (H6) alap primitív.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Új hypothesis (2026-04-11). A workload-attestation minta elég konkrét, hogy termék-spec legyen: runtime identity issuance + audit correlation + scope expiry.*


## H41 - Audit-First Agent Logs as Compliance Artifact (Immutable, Replayable)
**Thesis:** A buyer nem "observabilityt" kér, hanem *compliance artifactot*: immutable, exportálható action log + replay, ami procurement és SOC 2 auditban bizonyíték. Az agent run nem csak trace, hanem aláírható, megőrizhető és SIEM-be köthető bizonyítéklánc.
**Signals (updated 2026-04-11):**
- Enterprises demand agent action logs as compliance artifact (2026-04-10) - procurement checklist trend. HIGH CONFIDENCE.
- Model providers add tool-call audit hooks (2026-03-30) - natív trace export a platformokból. HIGH CONFIDENCE.
- SOC 2 auditors ask for evidence of agent guardrails (2026-04-04) - explicit audit evidence kérés. HIGH CONFIDENCE.
**Assessment:** Ez a H2 fókuszát élesíti: nem elég logolni, "audit evidence pack"-ként kell csomagolni (H38). Navibase alkalmazás: export template-ek (SOC2/EU AI Act) + replay link + immutability (hash chain).
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=4 | IntFric=3 | **Total: 22/25**
*Új hypothesis (2026-04-11). A compliance artifact nyelv buyer-friendly, és közvetlen procurement stopper. Quick wedge lehet advisory + tool.*


## H42 - MCP Security Profiles for Tool Servers (Standardized Auth, Scopes, Audit Events)
**Thesis:** A tool server sprawl (MCP) miatt az enterprise igény a "biztonsági profil": standard auth (mTLS/JWT/OAuth), least-privilege scope, és egységes audit event schema. Ezzel a governance nem egyedi integráció per tool server, hanem profile-based compliance.
**Signals (updated 2026-04-11):**
- MCP Security Profiles proposed for tool servers (2026-04-09) - explicit standard draft. HIGH CONFIDENCE.
- Policy-as-code gatekeepers for agent actions (2026-04-03) - inline enforcement igény. HIGH CONFIDENCE.
- Agents as integration layer: tool server market grows (2026-04-02) - tool server piac nő, standardizáció nélkül szétcsúszik. HIGH CONFIDENCE.
**Assessment:** H3 (MCP governance) konkrétítható "profiles + conformance test" irányba. Navibase alkalmazás: MCP profile lint + conformance scan, compliance reporttal.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-11). A standard draft miatt a window most nyílt: aki hamar ad lintert és reportot, a procurement nyelvét beszéli.*


## H43 - Signed A2A Delegation Claims (Ghost Delegation Prevention)
**Thesis:** Agent-to-agent kommunikációban a legnagyobb enterprise félelem a "ghost delegation": ki adott kinek felhatalmazást, milyen policy mellett, és ezt utólag hogyan bizonyítod. A megoldás: aláírt delegation claims (intent, constraints, context) a message payloadban, ami korrelálható audit traillel.
**Signals (updated 2026-04-11):**
- Agent-to-agent (A2A) messaging gets standardized claims (2026-04-09) - signed claims schema. HIGH CONFIDENCE.
- "Delegation risk" added to enterprise AI risk registers (2026-04-08) - kockázat explicit kategória. HIGH CONFIDENCE.
- Compliance teams ask: "Who is the agent?" (2026-03-27) - identity record igény. HIGH CONFIDENCE.
**Assessment:** H14 (A2A trust) és H12 (accountability) metszete. Navibase alkalmazás: delegation receipt, chain-of-custody, és dispute/contestability támogatás.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=4 | IntFric=4 | **Total: 20/25**
*Új hypothesis (2026-04-11). A signed claims lehet a következő standard primitív, de build fric magasabb és a buyer language még alakul.*


## H44 - Consent Receipts + Preview-Then-Execute for External Actions
**Thesis:** Enterprise governance minta: külső kommunikáció és record-módosítás előtt kötelező a preview + explicit consent receipt. A consent receipt egy auditálható artefakt, ami egyértelműsíti: ki és mikor engedélyezte az agent műveletét, milyen diff alapján.
**Signals (updated 2026-04-11):**
- "Consent receipts" for delegated actions in customer ops (2026-04-05) - explicit receipt pattern. HIGH CONFIDENCE.
- Delegation UX patterns: "preview then execute" (2026-04-01) - stabilizálódó UX standard. HIGH CONFIDENCE.
- Enterprises require HITL for external communications (2026-04-03) - governance baseline. HIGH CONFIDENCE.
**Assessment:** H34/H39 ops UX + H2 audit trail gyakorlati kimenete. Navibase alkalmazás: Telegram-first diff preview + approve button + consent receipt export.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-11). Alacsony build fric, gyorsan termékesíthető feature, és erős compliance story.*


## H45 - Agent Runbooks + Incident Response Playbooks (Operationalization Layer)
**Thesis:** Ahogy agentek production-ba kerülnek, SRE-szerű üzemeltetési réteg kell: runbook (eszkaláció, rollback, approval pontok) és incident response playbook (containment, credential revoke, replay analysis). Ez a governance hiányzó "operációs" fele.
**Signals (updated 2026-04-11):**
- "Agent runbooks" adopted as operational primitive (2026-04-01) - SRE-minta adaptáció. HIGH CONFIDENCE.
- Agent incident response playbooks emerge (2026-03-29) - security ops oldal. HIGH CONFIDENCE.
- Audit-first orchestration differentiator (2026-04-08) - a platformok erre pozicionálnak. HIGH CONFIDENCE.
**Assessment:** Ez service + tooling csomag. Navibase alkalmazás: standard runbook template library, ami összeköti a H2/H6/H40 identity primitive-eket a valós üzemeltetéssel.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-11). A runbook deliverable buyer-friendly, és jól csomagolható pilot ajánlatként.*


---

## Top 3 Opportunities + Suggested Experiments (2026-04-11)

### #1: H40 + H41 combo - Identity attestation + Compliance-grade action logs
**Miért most:** A procurement és compliance nyelv most konkretizálódik: "who is the agent" + immutable evidence. Ez a leggyorsabb enterprise wedge.
**Kísérlet:** 10 EU cégnek "Agent Delegation Evidence Pack" pilot: per-run issued identity (workload attestation) + immutable action log export + replay link. Mérők: procurement blocker-ek száma, pilot->paid konverzió, audit csapat feedback.

### #2: H42 - MCP Security Profiles linter + conformance scan
**Miért most:** Standard draft ablak nyitva, a tool server piac nő. Aki ad lintert és reportot, könnyen kerül shortlistre.
**Kísérlet:** Nyílt "MCP Security Profile Linter" v0.1: auth/scope/audit event checklist + report. Mérők: GitHub csillag, enterprise inbound, partner tool server-ek száma.

### #3: H44 - Consent receipts + preview-then-execute (Navibase/Leoni quick win)
**Miért most:** HITL external comms baseline lett. Low build, high trust.
**Kísérlet:** Leoni-ban 2 hetes pilot: minden külső email és CRM update előtt diff preview + approve, automatikus consent receipt mentés. Mérők: approval latency, user trust feedback, hibák csökkenése.


---

# Update - 2026-04-16

## H62 - Vendor Agent SDK Safety Primitives (Guardrails move "up-stack")
**Thesis:** Ahogy a nagy model provider-ek agent SDK-i érettebbé válnak, a safety és governance primitívek (policy hooks, tool call guardrails, structured auditing) "felköltöznek" a vendor SDK rétegébe. Ez csökkenti a belépési súrlódást, de új problémát nyit: a csapatok több SDK-t használnak, és kell egy cross-vendor baseline (evidence export, policy mapping, org standard) ami nem lock-in.
**Signals (updated 2026-04-16):**
- OpenAI Agents SDK update (TechCrunch, 2026-04-15): enterprise-safe agent building primitives bővülése. https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/
**Assessment:** Ez a H6/H2/H41 irányt erősíti, de a termék-szintű realitás az, hogy a buyer először vendor SDK-t fog választani. Navibase: "guardrails + evidence export" adapter réteg, ami több SDK fölött ugyanazt a compliance artifactot adja.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-16). A safety primitives vendor-szintre tolódása gyorsítja az adoptiont, és felértékeli a cross-SDK governance/evidence réteget.*


## H63 - Agent Seat Licensing & Procurement Controls (Agents as employees)
**Thesis:** Ha az agentek "digitális munkatársakként" jelennek meg, a következő kontroll nem technikai, hanem gazdasági és compliance: licenc, seat assignment, költségallokáció, és entitlement kezelés (mely agent milyen szoftvert "használhat"). A seat/licensing modellek agent principalokra való kiterjesztése új platformréteget igényel.
**Signals (updated 2026-04-16):**
- Microsoft exec suggests AI agents will need to buy licenses, just like employees (Business Insider, 2026-04-14). https://www.businessinsider.com/microsoft-executive-suggests-ai-agents-buy-software-licenses-seats-2026-4
**Assessment:** Ez a H1/H60 identity + H29 cost governance metszete. Navibase: "agent entitlement registry" (agent principal → allowed apps/licenses) + audit export, ami procurement nyelven beszél.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-16). A "seat for agents" narratíva buyer-friendly, és gyorsan procurement kérdéssé válhat.*


## H64 - Integrity Hallucination / Decision Consistency Governance
**Thesis:** High-stakes környezetben a probléma nem csak "hallucination", hanem az inkonzisztens döntés (ugyanarra az inputra más kimenet, indoklás drift). Kell egy integritás és konzisztencia réteg: decision fingerprinting, invariánsok, regressziós teszt suite, és "integrity drift" metrika.
**Signals (updated 2026-04-16):**
- Integrity hallucination raises concerns over inconsistent AI decision-making in high-stakes systems (Devdiscourse, 2026-04-15). https://news.google.com/rss/articles/CBMi6wFBVV95cUxNYmJrUi1haWpYaFlZdENRdUswaFBlRDNpWGxTTHduQjl6QU04c3phN0FqR1YwRHlnY2JMTDBaUWVEVnRxVG9zdGpWckVHY05SRGZoc0VLSkZHdHY4SWJPdnZOckFyeVFwNDk3a1BZOUthQzUzLTJ4YmluYmhoSTgwWWRnWjJKWExwaFROcFBBRE1ZQ1RwZ3ZEM2cta3NCRFNfeHBlRVhwWlpxMHJrckFmeDg5eXM2bHp3R1BzcTRhYTUyMElqcTNFR01MRURRLTIyRUpEanRTaWZEd2NYdXRjTlQtWWt3amF6ZWlv0gHwAUFVX3lxTE15WFh1Skp4OE1RYjVYQ1JrVEt6QnpoSGl6SElXYmtxV3Bqc0pIa0dEVjU4Q2tHelkwa1JObXJ0ZG5TbVN6Y0JTSG8xQWoyMGV1Wkc1cVdpRnUySHBEQk1WWWdpVTNkYm91RE12Q1g0OS0zWXllQXZSMks0Ry01VFA4QlBQRDBubjVFNGRUYmwwWUlSOUtlT2dyMmVuSXNEY3VrbmphU3V5MElzYW9vRzREVm1qRVZ1VE9ESWhzSVQxOHB1Z1BHbTY0bHJlZDMwNGp6TzBkN2lfMTBIck9mSFVDdjRPSmlKdFgwbWt1QWpkOA?oc=5
**Assessment:** Ez a H21 (deterministic trust) technikai megfelelője. Navibase: "integrity gate" minden külső kimenet előtt, plusz audit-evidence a konzisztencia tesztekről.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-16). A failure-mode név ("integrity hallucination") segít buyer-nyelvre fordítani a konzisztencia problémát.*


## Top 3 Opportunities + Suggested Experiments (2026-04-16)

### #1: H62 - Cross-SDK evidence export baseline (vendor guardrails fölé)
**Miért most:** A safety primitive-ek vendor SDK-kban landolnak, de a buyer nem akar lock-in és egységes compliance artifactot akar.
**Kísérlet:** 3 nap: egy "evidence export adapter" prototípus (1 workflow) ami OpenAI Agents SDK runból exportál: tool-call timeline + policy decisions + correlation id, és ugyanarra a sémára illeszthető más SDK-ból is.

### #2: H63 - Agent entitlement registry (seat/licensing control plane)
**Miért most:** A "agents buy seats" narratíva procurement nyelv, gyorsan költség és compliance témává válik.
**Kísérlet:** 1 hét: minimál entitlement registry (agent principal → allowed SaaS/apps/licenses) + audit export + egyszerű approval flow (H44).

### #3: H64 - Integrity drift check for outbound actions (consistency gate)
**Miért most:** Inkonzisztens döntések high-stakes környezetben új failure-mode-ként vannak címkézve, a buyer ezt érti.
**Kísérlet:** 1 hét: "integrity test pack" 20 fix scenario-val + regressziós futtatás release előtt, és runtime "invariant checks" outbound email/record update előtt.


---

# Update - 2026-04-17

## H65 - Real-Time Agent Stack Anomaly Detection (Proactive Failure Intelligence)
**Thesis:** A passzív logging (trace, audit trail) és az utólagos RCA (H61) nem elegendő: a produkciós agent hiba ott fáj, ahol csendben, de az egész tech stacken keresztül terjedve jelenik meg. Az InsightFinder $15M befektetési validáció pontosan erre a rétegre irányul: nem a model-hibák detektálása, hanem az agent + infra + app stack viselkedésének proaktív anomália-detekciója. A winner nem logol, hanem előre jelez.
**Signals (updated 2026-04-17):**
- InsightFinder raises $15M: "help companies figure out where AI agents go wrong" (TechCrunch, 2026-04-16): CEO szerint a probléma nem egyes model hibák, hanem az egész tech stack viselkedése - explicit proaktív anomália kategória. $15M seed validálja a WTP-t. HIGH CONFIDENCE.
- Integrity hallucination - inconsistent AI decision-making in high-stakes systems (Devdiscourse, 2026-04-15): az inkonzisztencia felderítése real-time monitoring nélkül lehetetlen. HIGH CONFIDENCE.
**Assessment:** Ez a H61 (RCA) és H19 (operational reliability) következő rétege: nem "mi romlott el", hanem "mikor fog elromlani". A $15M validálja, hogy a buyer fizet ezért. Navibase alkalmazás: agent + cron + API stack behavioral baseline + anomália alert Telegramon, mielőtt a hiba terjed.
**Scores:** Pain=4 | Urgency=4 | WTP=5 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-17). Az InsightFinder befektetés az eddig legerősebb VC-validáció a proaktív agent stack monitoring kategóriában.*


## Megerősített signalok (2026-04-17)

**H59/H37/H53 (credential delegation):** Kontext CLI bekerült GitHub-ra (2026-04-14) + "Do you trust AI agents with API keys?" HN thread (2026-04-12) egymást erősítik. A credential boundary kérdés nem elméleti - napi ops dilemma. Credential brokerage/JIT token pattern gyorsabban válhat table stakes-szé, mint terveztük.

**H60/H1 (agent identity platform):** ZeroID megerősítés (Help Net Security, 2026-04-13) + dedikált "AI Agents Authentication" cikk (Security Boulevard, 2026-04-16): az agent identity mint önálló platform-réteg kristályosodik. A ZeroID open-source terjedése felgyorsíthatja a compliance elvárást a nem-ZeroID platformokon.

**H63 (agent seat licensing):** Microsoft "agents buy licenses like employees" újra megjelent mainstream sajtóban (Business Insider, 2026-04-14). Az entitlement/licensing kérdés a procurement szintre érkezett.

**H64/H21 (integrity/consistency governance):** Az "integrity hallucination" elnevezés (Devdiscourse, 2026-04-15) buyer-szintű nyelvet ad a konzisztencia-problémának. High-stakes rendszereknél ez gyorsan compliance-kérdéssé válik.

**H34/H44 (human-in-the-loop formalization):** "The human exception in AI governance: ticking boxes?" (Computer Weekly, 2026-04-08) jelzi, hogy a HITL nem elég szabályozói szemmel - formalizált döntési határok kellenek. Ez a H44 (consent receipts) és H6 (policy enforcement) piaci narratíváját erősíti.

**H20/H6 (policy + platform compliance):** Algorithmic government paper (BizNews, 2026-04-15) - a döntési delegáció szabályozói keretbe illesztése nemcsak várható, hanem elkerülhetetlen. Platform-szintű compliance deadline-ok közelednek.


## Ranking Summary (2026-04-17)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H1 - Agent Identity & Auth | 21/25 | = |
| 5 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 6 | H24 - Shadow AI Governance Plane | 21/25 | = |
| 7 | H40 - Workload-to-Agent Attestation | 22/25 | = |
| 8 | H41 - Audit-First Compliance Artifacts | 22/25 | = |
| 9 | H3 - MCP Governance | 20/25 | = |
| 10 | H12 - Agent Accountability Framework | 20/25 | = |
| 11 | H30 - Agent Trading Protocol & Risk Governance | 20/25 | = |
| 12 | H43 - Signed A2A Delegation Claims | 20/25 | = |
| 13 | H10 - Agent Infra as Code | 19/25 | = |
| 14 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 15 | H42 - MCP Security Profiles | 19/25 | = |
| 16 | **H65 - Proactive Agent Stack Anomaly Detection** | **19/25** | **ÚJ** |
| 17 | H59 - Agent Credential Brokerage | 19/25 | = |
| 18 | H60 - Agent Identity Platform | 19/25 | = |
| 19 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 20 | H8 - Cross-Agent Context | 18/25 | = |
| 21 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 22 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 23 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 24 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 25 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 26 | H19 - Operational Reliability Layer | 18/25 | = |
| 27 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 28 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 29 | H28 - Bias/Fairness Governance | 18/25 | = |
| 30 | H32 - Trace-to-Patch Harness Improvement | 18/25 | = |
| 31 | H33 - Multi-Agent Influence Governance | 18/25 | = |
| 32 | H61 - Agent Failure Investigation Automation | 17/25 | = |
| 33 | H63 - Agent Seat Licensing & Procurement | 18/25 | ↑ signal erős |
| 34 | H64 - Integrity Hallucination / Consistency Governance | 18/25 | ↑ névvel bíró failure mode |
| 35 | H4 - Agent Payment Rails | 17/25 | = |
| 36 | H11 - Hallucination Self-Check | 17/25 | = |
| 37 | H27 - Agent Packaging & Portability Spec | 17/25 | = |
| 38 | H29 - Cost Governance & Token Budget | 17/25 | = |
| 39 | H31 - Agent-Native KB for Office Files | 17/25 | = |
| 40 | H44 - Consent Receipts + Preview-Then-Execute | 17/25 | = |
| 41 | H45 - Agent Runbooks & Incident Response | 17/25 | = |
| 42 | H62 - Cross-SDK Safety Primitives | 17/25 | = |
| 43 | H5 - Discovery & Registry | 16/25 | = |
| 44 | H25 - Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 45 | H26 - WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 46 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-17 delta: 1 új hypothesis (H65 - Proactive Agent Stack Anomaly Detection, 19/25). Megerősített irányok: H59/H60 credential+identity erősödik, H63 procurement szintre ér, H64 buyer-language névvel bír.*


## Top 3 Opportunities + Suggested Experiments (2026-04-17)

### #1: H65 - Proactive Agent Stack Anomaly Detection (InsightFinder validáció)
**Miért most:** $15M seed befektetés validálja a WTP-t - a buyer fizet a proaktív anomália-detektálásért. A versenytárs (InsightFinder) enterprise-fókuszú; a KKV wedge nyitva van. Leoni belső infrastruktúrán (cron, task runner, API hívások) már van elég trace-adat egy MVP-hez.
**Kísérlet:** 2 hetes pilot: agent run behavioral baseline rögzítés (latency, tool-call sorrend, failure arány per feladattípus) + anomália alert Telegramon ha >2 sigma eltérés. Mérők: false positive arány, mean-time-to-detect, Tomi visszajelzés (hasznos-e az alert).
**Befektetés:** ~3 nap build. Leoni trace data már megvan.

### #2: H59/H37 - Credential Delegation Demo (Secretless-by-default proof)
**Miért most:** Kontext CLI + HN trust thread egyszerre jelzi: ez napi ops dilemma, nem elméleti. A buyer language egyszerű: "nem adom oda a kulcsaimat." JIT token + scope + audit correlation lánc gyorsan termékesíthető.
**Kísérlet:** 3 napos demo: OIDC token exchange + JIT token issuance + audit correlation ID (per run). Deliverable: 1 oldalas evidence export + 2 perces képernyőfelvétel a Navibase pitchhez.
**Befektetés:** ~3 nap. Kontext CLI maga a reference implementation.

### #3: H64 - Integrity Consistency Gate (outbound actions előtt)
**Miért most:** Az "integrity hallucination" buyer-szintű névvel bíró failure mode lett. High-stakes döntéseknél (ajánlat, email, döntéstámogatás) az inkonzisztencia már közvetlen üzleti kár. Alacsony build fric: 20 fix scenario + regression checker.
**Kísérlet:** 1 hét: "integrity test pack" (20 fix scenario, Leoni outbound email + kanban update + cron) + regressziós futtatás release/konfig változás előtt. Mérők: inkonzisztencia arány, false block arány, Tomi audit visszajelzés.
**Befektetés:** ~2 nap. Navibase differenciáló: "minden outbound action mögött konzisztencia garancia."

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-17.md (350 releváns, 92 prioritizált) | 2026-04-17 18:48 CET*


---

# Update - 2026-04-20

## H66 - Agentic Supply Chain Security (Distillation as Attack Vector)
**Thesis:** Az agentic safety eddig feltételezte, hogy az adatszanitáció elegendő védelmet nyújt. Az arxiv "subliminal transfer" paper megmutatja: veszélyes viselkedési minták implicit módon beágyazódnak modell-disztilláció során - akkor is, ha az explicit kulcsszavakat kiszűrik. Ez az agentic supply chain legalaposabban alulbeszélt kockázata: nem az input, hanem a modell örökölt viselkedése a fenyegetés. Kell egy "supply chain attestation" réteg: honnan jött a modell, milyen trajektória-adatokon tanult, és milyen implicit viselkedési bias-t örökített a tanártól a diákra?
**Signals (updated 2026-04-20):**
- "Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation" (arxiv, 2026-04-16): diákmodell örökli a tanár destruktív magatartását (törlési bias, destructive filesystem operations) puszta trajektória-dinamikából, explicit kulcsszavak kiszürése után is. HIGH CONFIDENCE.
- "Secure-by-Design: 3 Principles to Safely Scale Agentic AI" (CIO.com, 2026-04-16): mainstream enterprise IT napirendbe kerül az agentic AI biztonság, de a supply chain kockázat explicit formában még nem jelenik meg. HIGH CONFIDENCE.
- H22 (Adversarial Robustness) és H23 (Agentic QA) az input és runtime rétegre fókuszál - a supply chain (training/distillation) réteg különálló kategória.
**Assessment:** Ha az adatszanitáció nem véd, az enterprise adopció alapfeltevése omlik össze. A "supply chain attestation" mint compliance primitive valószínüleg gyorsan table stakes-szé válik: milyen training provenance van a deployed agent mögött? Navibase alkalmazás: deployed agent-ek "training lineage card"-ja, implicit behavior audit (behavioral invariant test suite), és vendor-attestation kérés kritikus deploymenteknél.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=4 | IntFric=4 | **Total: 21/25**
*Új hypothesis (2026-04-20). Az arxiv paper az elso empirikus bizonyíték arra, hogy az agentic supply chain támadási vektor - a training provenance és behavioral audit kategória eddig üres volt.*

---

## H67 - Offensive Agent Red-Teaming as a Service (Multi-turn Attack Automation)
**Thesis:** Az agentic testing ma manuális: biztonsági csapatok kézzel próbálnak prompt injectiont, tool hijackinget, logic bug-okat keresni. A Nyx harness megmutatja, hogy az agentic red-teaming automatizálható multi-turn forgatókönyvekkel - és 10 perc alatt megtalál olyan hibákat, amelyeket manuális auditok órák alatt sem. Ez az "offensive testing as a service" kategóriát nyitja meg: nem csak defense (H22/H6), hanem aktív, rendszeres agent attack simulation, deliverable-lel és compliance evidence-szel.
**Signals (updated 2026-04-20):**
- "Nyx - Multi-turn Offensive Testing Harness for AI Agents" (HN / fabraix.com, 2026-04-19): autonóm blackbox tesztelő eszköz AI agentekhez, 10 perc alatt detektál logikai hibát, prompt injectiont, tool hijackinget. HIGH CONFIDENCE.
- Trail of Bits mutation testing paper (2026-04-01): az agentic testing üres kategória, különbözo megközelítések egymást kiegészítik. HIGH CONFIDENCE.
- H23 (Agentic QA) rokon kategória, de a Nyx multi-turn attack simulation más dimenzió: nem mutation testing, hanem adversarial dialogue és toolchain abuse.
**Assessment:** Az "offensive agent testing" buyer-language: "tudom-e, hogy az agenten tört be valaki?" - ez a SOC 2 és enterprise security audit természetes következo kérdése. Navibase alkalmazás: negyedéves "Agent Red-Team Report" deliverable, Nyx-alapú automated scan + human-curated findings.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-20). A Nyx validálja a piacot: az automated multi-turn attack simulation nem kutatás, hanem használható eszköz. A "red-teaming as a service" a H23 mutation testing természetes következo fázisa.*

---

## H68 - Self-Evolving Agent Governance (GEP / Genome-Level Audit Gap)
**Thesis:** A "Genome Evolution Protocol" alapú önfejleszto agentek (EvoMap/evolver) megjelenése elorehozza az eddig 2027+ kategóriának besorolt governance kérdést: hogyan auditálható egy agent, amelyik saját magát módosítja futás közben? A H17 (Controlled Self-Configuration) a statikus scope-határ kérdése - az önfejleszto agent dinamikusan változó scope-ot jelent, ahol az audit trail nem egy állapotot, hanem egy evolúciós trajektóriát kell rögzítenie. Kell egy "genome audit" primitív: mikor változott az agent, mit változtatott, és a változás compliance-korlátok közt maradt-e?
**Signals (updated 2026-04-20):**
- "EvoMap/Evolver - GEP-Powered Self-Evolution Engine for AI Agents" (GitHub, 2026-04-17): agenteket önmagukat fejlesztheto rendszerekként kezeli Genome Evolution Protocol alapján. HIGH CONFIDENCE.
- H17 (Controlled Self-Configuration Boundary, 18/25): statikus scope-hardening megoldott - a dinamikus self-evolution új governance primitívet igényel.
- "Agentic AI and the next intelligence explosion" (arxiv, 2026-03-30): a self-evolving agent narratíva erosödik, governance elmarad. HIGH CONFIDENCE.
**Assessment:** Ez rövid távon research fázis, de a tooling megjelenése (EvoMap) azt jelzi, hogy a kérdés hamarabb éri el a productiont, mint terveztük. Navibase alkalmazás: "agent genome snapshot" minden futás elott/után + diff + compliance gate (engedélyezett vs. nem engedélyezett változás típusok).
**Scores:** Pain=4 | Urgency=3 | WTP=3 | Def=4 | IntFric=4 | **Total: 18/25**
*Új hypothesis (2026-04-20). Az EvoMap a "self-evolving agent" kategóriát konkrét OSS eszközként megnyitja - a governance kérdés hamarabb production-kérdés lesz, mint várható volt.*

---

## H69 - Cross-Border AI Regulatory Fragmentation (Compliance Translation Layer)
**Thesis:** Ázsiában (India, Indonézia, Kína) és Európában (EU AI Act) párhuzamosan formálódnak az AI governance struktúrák, egymással nem harmonizáltan. Egy cross-border agent deployment (pl. KKV európai irodával és ázsiai partnerekkel) egyszerre kell megfeleljen az EU AI Act, MeitY, és esetleg indonéziai/kínai szabályozásnak - jelenleg nincs olyan eszköz, ami ezt automatikusan mappel, jelöli a konfliktusokat, és javasol compliance adaptációt. Ez az "AI regulatory translation" kategória.
**Signals (updated 2026-04-20):**
- India dual AI governance structure (Zee News / MediaNews4U, 2026-04-17-18): MeitY tech-policy panel + Ashwini Vaishnaw-vezette cross-minisztériumi testület párhuzamosan - India regulatory landscape összetett és gyorsan változik. HIGH CONFIDENCE.
- Indonesia AI Ethics and National Regulation (2026-04-17): délkelet-ázsiai szabályozás is formálódik. MEDIUM CONFIDENCE.
- Chinese groups global AI governance framework (2026-04-17): Kína aktívan alakítja a globális AI governance normákat, EU-s keretekkel kevés átfedéssel. MEDIUM CONFIDENCE.
- EU AI Act Aug 2026: európai framework kész, de cross-border deployment-nél nem elegendo. HIGH CONFIDENCE.
**Assessment:** A cross-border compliance gap 2026 végére éles piaci problémává válhat. A buyer: multinacionális KKV, külföldi piacra lépo startup, enterprise compliance csapat. Navibase alkalmazás: "Regulatory Matrix" - per-deployment compliance mapping (EU AI Act + MeitY + local) + automatikus gap-detekció + javasolt adaptációs lépések.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=4 | **Total: 19/25**
*Új hypothesis (2026-04-20). Az ázsiai regulatory proliferáció egyszerre erösíti és bonyolítja a compliance piacot. A "regulatory translation" kategória üres - a buyer fájdalma valós, de a termék még nincs.*

---

## H70 - Agent-Ready Web as Interoperability Standard
**Thesis:** Az internetes infrastruktúra "agent-readiness" szempontú értékelése (isitagentready.com, Cloudflare) jelzi, hogy hamarosan elvárás lesz, hogy API-k, weboldalak és B2B platformok natively megérthetok legyenek AI agentek számára (robots.txt analógiája agentek számára, strukturált tool-call schema, consent/auth dokumentáció). Aki nem tervezi erre rendszereit, az lemarad az agent-driven distribution hullámtól. Ez a "web-for-agents" szabványosítás következo platform-váltása.
**Signals (updated 2026-04-20):**
- "Isitagentready.com / Cloudflare - Website Agent-Readiness Scanner" (Product Hunt / Cloudflare, 2026-04-17): a Cloudflare elkezdette az internetes infrastruktúra "agent-readiness" szempontú értékelését. HIGH CONFIDENCE.
- "Agentic Infrastructure" (Vercel blog, 2026-04-17): Vercel dedikált blogposztban definiálja az "agentic infrastructure" fogalmát - az infrastruktúra réteg agent-first átalakulóban. HIGH CONFIDENCE.
- "Cloudflare Shared Dictionaries for agentic web" (2026-04-17): Cloudflare aktívan fejleszti az agent-web szint protokolljait. MEDIUM CONFIDENCE.
**Assessment:** Ez a következo "platform shift" - a web agent-ready lesz vagy lemarad. A buyer: weboldal-tulajdonos, SaaS cég, API-t publikáló vállalat. Navibase alkalmazás: "Agent-Ready Audit" - meglevo KKV infrastruktúra agent-readiness scoring + quick-fix checklist.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 15/25**
*Új hypothesis (2026-04-20). A Cloudflare + Vercel egyszerre validálja az irányt - az "agent-ready web" 2026-2027-es platform elvárás lesz, de a WTP és az urgency még alakul.*

---

## Megerosített signalok (2026-04-20)

**H1/H60 (agent authentication):** "AI Agents Authentication: How Autonomous Systems Prove Identity" (Security Boulevard, 2026-04-16) - az agent authentikáció mainstream napirendként jelenik meg. A H60 (Agent Identity Platform) megerosödik: ez a következo különálló platformréteg lesz.

**H65 (proaktív anomália detekció):** InsightFinder $15M megerosítés (TechCrunch, 2026-04-16) - a befektetés validálja, hogy a proaktív agent stack monitoring WTP reális. Az InsightFinder enterprise-fókuszú, KKV wedge nyitva.

**H22 (adversarial robustness):** Nyx offensive harness + H66 distillation attack vector együttesen jelzik: az adversarial agent attack surface szélesedik (nem csak input, hanem training + multi-turn dialogue).

**H36 (managed infrastructure):** Vercel "agentic infrastructure" blog - az infrastruktúra réteg agent-first átalakulása erösödik. Platform-szintü váltás közeledik.

**H49/H27 (multi-agent framework fragmentation):** OpenAI Agents Python nyílt forráskód (GitHub, 2026-04-17) - framework proliferáció és portabilitás/interoperabilitás kérdése élesedik. H27 (Agent Packaging & Portability) megerösödik.


## Ranking Summary (2026-04-20)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H40 - Workload-to-Agent Attestation | 22/25 | = |
| 5 | H41 - Audit-First Compliance Artifacts | 22/25 | = |
| 6 | H1 - Agent Identity & Auth | 21/25 | = |
| 7 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 8 | H24 - Shadow AI Governance Plane | 21/25 | = |
| 9 | **H66 - Agentic Supply Chain Security** | **21/25** | **ÚJ** |
| 10 | H3 - MCP Governance | 20/25 | = |
| 11 | H12 - Agent Accountability Framework | 20/25 | = |
| 12 | H30 - Agent Trading Protocol & Risk Governance | 20/25 | = |
| 13 | H43 - Signed A2A Delegation Claims | 20/25 | = |
| 14 | H10 - Agent Infra as Code | 19/25 | = |
| 15 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 16 | H42 - MCP Security Profiles | 19/25 | = |
| 17 | H59 - Agent Credential Brokerage | 19/25 | = |
| 18 | H60 - Agent Identity Platform | 19/25 | = |
| 19 | H65 - Proactive Agent Stack Anomaly Detection | 19/25 | = |
| 20 | **H69 - Cross-Border Regulatory Fragmentation** | **19/25** | **ÚJ** |
| 21 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 22 | H8 - Cross-Agent Context | 18/25 | = |
| 23 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 24 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 25 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 26 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 27 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 28 | H19 - Operational Reliability Layer | 18/25 | = |
| 29 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 30 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 31 | H28 - Bias/Fairness Governance | 18/25 | = |
| 32 | H32 - Trace-to-Patch Harness Improvement | 18/25 | = |
| 33 | H33 - Multi-Agent Influence Governance | 18/25 | = |
| 34 | H63 - Agent Seat Licensing & Procurement | 18/25 | = |
| 35 | H64 - Integrity Hallucination / Consistency Governance | 18/25 | = |
| 36 | **H67 - Offensive Agent Red-Teaming as a Service** | **18/25** | **ÚJ** |
| 37 | **H68 - Self-Evolving Agent Governance** | **18/25** | **ÚJ** |
| 38 | H4 - Agent Payment Rails | 17/25 | = |
| 39 | H11 - Hallucination Self-Check | 17/25 | = |
| 40 | H27 - Agent Packaging & Portability Spec | 17/25 | = |
| 41 | H29 - Cost Governance & Token Budget Enforcement | 17/25 | = |
| 42 | H31 - Agent-Native KB for Office Files | 17/25 | = |
| 43 | H44 - Consent Receipts + Preview-Then-Execute | 17/25 | = |
| 44 | H45 - Agent Runbooks & Incident Response | 17/25 | = |
| 45 | H61 - Agent Failure Investigation Automation | 17/25 | = |
| 46 | H62 - Cross-SDK Safety Primitives | 17/25 | = |
| 47 | H5 - Discovery & Registry | 16/25 | = |
| 48 | H25 - Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 49 | **H70 - Agent-Ready Web Infrastructure** | **15/25** | **ÚJ** |
| 50 | H26 - WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 51 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-20 delta: 5 új hypothesis (H66-H70). H66 (Agentic Supply Chain Security, 21/25) azonnal a top 9-be kerül - empirikus bizonyíték arra, hogy az adatszanitáció elégtelen védelemként az agentic supply chain ellen. H69 (Cross-Border Regulatory Fragmentation, 19/25) az ázsiai regulatory proliferációt fedezi le. H67/H68 a 18/25 blokkba kerülnek. H70 új kategória, 15/25 szinten még.*


## Top 3 Opportunities + Suggested Experiments (2026-04-20)

### #1: H66 - Agentic Supply Chain Security (Training Provenance Audit)
**Miért most:** Az arxiv subliminal transfer paper az egyetlen empirikus bizonyíték arra, hogy az enterprise compliance alapfeltevése ("szanitálj és telepíts") hamis. Ez a kategória eddig üres - az elso, aki "training lineage card" és behavioral invariant test suite-ot ad, azt a procurement kérdést kezeli, ami eddig nem létezett.
**Kísérlet:** 1 hét: "Behavioral Invariant Test Suite" prototípus - 20 fix scenario, amelyre az agent viselkedésének konzisztensen a várható határon belül kell maradnia, + automated run + pass/fail report. Deliverable: 1 oldalas "Agent Supply Chain Evidence Card" (training provenance + behavioral audit results). Merők: false positive arány, compliance csapat visszajelzés.
**Befektetés:** ~1 hét. Az arxiv paper maga a spec - szabad és high-credibility forrás.

### #2: H67 - Offensive Agent Red-Teaming (Nyx-alapú quarterly scan)
**Miért most:** A Nyx harness konkrét, useable eszköz - 10 perc alatt megtalál olyan hibákat, amelyeket manuális auditok nem. Az "offensive testing" SOC 2 és enterprise security buyer számára természetes deliverable.
**Kísérlet:** 2 napos pilot: Nyx futtatása Leoni agent-en + manuális kiegészítés (multi-turn adversarial dialogue) + "Agent Red-Team Summary" (3-5 kritikus finding + remediation javaslat). Merők: finding szám, severity, remediation time.
**Befektetés:** ~2 nap. Nyx maga az eszköz - externally validated scan.

### #3: H69 - Cross-Border Regulatory Compliance Mapping (EU + Asia wedge)
**Miért most:** India párhuzamos dual governance struktúra + EU AI Act Aug 2026 deadline - a cross-border compliance gap valóssá vált. Nincs eszköz, nincs advisory service, nincs template. Az elso "Regulatory Matrix" letöltheto sablon erős lead gen és thought leadership.
**Kísérlet:** 3 nap: "EU AI Act vs MeitY vs Indonesia AI Ethics" összehasonlító mátrix - per-kategória conflict mapping. Deliverable: 1 oldalas PDF + LinkedIn post + 5 célzott outreach CEE multinacionális cégeknek. Merők: letöltések, inbound megkeresések.
**Befektetés:** ~3 nap kutatás + formázás. Erős CEE differenciáló.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-20.md (402 releváns, top 30 elemezve) | 2026-04-20 09:30 CET*


---

# Update - 2026-04-21

## H71 - Formal AI Agent Oversight Institutions (Multi-Jurisdiction Governance Convergence)
**Thesis:** Az AI governance eddig vállalati és szabályozói szinten mozgott, de 2026 Q2-ben formális, multi-stakeholder felügyeleti intézmények megjelenése jelzi, hogy az agent döntési delegáció szabályozása az "akadémiai/technikai vita" fázisból a "formális intézményesítés" fázisba lép. India cross-minisztériumi AI testületet hoz létre, Kína globális framework-et sürget, Cambridge az "AI oversight bodies" mintázatát modellezi - egyszerre, egyazon héten. Aki ma dokumentálja, hogy egy agent deployment hogyan illeszkedik ezekbe a keretekbe, az compliance-ready lesz, mielőtt a szabályozás kötelezővé válna.
**Signals (updated 2026-04-21):**
- Cambridge University Press: "Institutionalizing proxy responsibility: AI oversight bodies and resort-to-force decision making" (2026-04-18): a proxy-felelősség intézményesítése formális oversight bodies keretében - nem vállalati, hanem állami/intézményi szintű kérdéssé válik. HIGH CONFIDENCE.
- India MeitY: cross-minisztériumi AI governance testület (2026-04-17-18): Ashwini Vaishnaw vezette Technology and Policy Expert Committee, government-szintű mandátummal. HIGH CONFIDENCE.
- China: globális AI governance framework (2026-04-17): kínai csoportok multilaterális keretet sürgetnek, EU-tól eltérő narratívával. MEDIUM CONFIDENCE.
- Indonesia AI Ethics and National Regulation (2026-04-17): délkelet-ázsiai regulatory hullám önálló framework-kel. MEDIUM CONFIDENCE.
- EU AI Act Aug 2026 (korábbi): a legoperacionalizáltabb kereten kívül más intézményi formák is formálódnak párhuzamosan. HIGH CONFIDENCE.
**Assessment:** Ez a H69 (cross-border regulatory fragmentation) és H20 (agent platform as regulated infrastructure) összekötő eleme: nem csak szabályozói megfelelés, hanem formális intézményi beágyazottság. Az 5 különböző forrásból érkező governance-jel egyazon héten ritka, erős konvergencia-signal. A buyer kérdése: "Tudom, hogy az agentünk a várható globális governance kerethez illeszkedik?" Navibase alkalmazás: "Global Agent Governance Readiness Scorecard" - EU AI Act + MeitY + indonéziai framework + kínai elvárások per-deployment mappelése, gap-detekció és felülvizsgálható evidencia.
**Scores:** Pain=4 | Urgency=5 | WTP=4 | Def=3 | IntFric=4 | **Total: 20/25**
*Új hypothesis (2026-04-21). Az egy héten belüli multi-jurisdikciós konvergencia (Cambridge + India + Kína + Indonézia) ritka, erős jel: a governance-institutionalization hullám most indul. 20/25 - közvetlen top 10 belépő.*

---

## Megerősített signalok (2026-04-21)

**H66 (agentic supply chain security):** A subliminal unsafe behavior transfer arxiv paper (2026-04-16) ismét megjelenik a napi top signalok között - a 2026-04-20-as H66 hypothesis közvetlen, folytatódó megerősítése. Az "enterprise compliance alapfeltevés omlik össze" narratíva erősödik.

**H22 (adversarial robustness):** "Secure-by-Design: 3 Principles to Safely Scale Agentic AI" (CIO.com, 2026-04-16) - enterprise IT napirendbe kerül az agentic safety, erősíti a H22 urgency-t. A "batteries-included" approach egyre inkább elvárás.

**H1/H20 (governance mainstream):** "AI Agent Governance: How to Control Autonomous Agents Safely" (Cybernews, 2026-04-20) - a governance rés mainstream témává válik. Az iparág nem rendelkezik kialakult standardokkal, ez a H20 positioning ablakot tovább tágítja.

**H67 (offensive agent testing):** Nyx multi-turn offensive harness megerősítés - az agentek "nem úgy törnek meg, mint hagyományos szoftver". Az offensive testing mint önálló kategória stabilizálódik.

**H65 (proaktív anomália detekció):** InsightFinder $15M megerősítés az Apr 21-i listában is - befektetés és buyer-language együtt erősítik a WTP-t.

**H69 (cross-border regulatory):** India dual governance structure (MeitY + Policy Committee) párhuzamos megjelenése tovább növeli H69 urgency-t - a szabályozói landscape már nem EU-centrikus.

**H70 (agent-ready web):** Vercel "Agentic Infrastructure" blog (2026-04-17) + Cloudflare jelzi: az infrastruktúra réteg agent-first átalakulóban. H70 score lassan erősödik (15 → várható 16).

---

## Ranking Summary (2026-04-21)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H40 - Workload-to-Agent Attestation | 22/25 | = |
| 5 | H41 - Audit-First Compliance Artifacts | 22/25 | = |
| 6 | H1 - Agent Identity & Auth | 21/25 | = |
| 7 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 8 | H24 - Shadow AI Governance Plane | 21/25 | = |
| 9 | H66 - Agentic Supply Chain Security | 21/25 | ↑ megerősítve |
| 10 | H3 - MCP Governance | 20/25 | = |
| 11 | H12 - Agent Accountability Framework | 20/25 | = |
| 12 | H30 - Agent Trading Protocol & Risk Governance | 20/25 | = |
| 13 | H43 - Signed A2A Delegation Claims | 20/25 | = |
| 14 | **H71 - Formal AI Oversight Institutions** | **20/25** | **ÚJ** |
| 15 | H10 - Agent Infra as Code | 19/25 | = |
| 16 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 17 | H42 - MCP Security Profiles | 19/25 | = |
| 18 | H59 - Agent Credential Brokerage | 19/25 | = |
| 19 | H60 - Agent Identity Platform | 19/25 | = |
| 20 | H65 - Proactive Agent Stack Anomaly Detection | 19/25 | = |
| 21 | H69 - Cross-Border Regulatory Fragmentation | 19/25 | ↑ urgency erősödik |
| 22 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 23 | H8 - Cross-Agent Context | 18/25 | = |
| 24 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 25 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 26 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 27 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 28 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 29 | H19 - Operational Reliability Layer | 18/25 | = |
| 30 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 31 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 32 | H28 - Bias/Fairness Governance | 18/25 | = |
| 33 | H32 - Trace-to-Patch Harness Improvement | 18/25 | = |
| 34 | H33 - Multi-Agent Influence Governance | 18/25 | = |
| 35 | H63 - Agent Seat Licensing & Procurement | 18/25 | = |
| 36 | H64 - Integrity Hallucination / Consistency Governance | 18/25 | = |
| 37 | H67 - Offensive Agent Red-Teaming as a Service | 18/25 | = |
| 38 | H68 - Self-Evolving Agent Governance | 18/25 | = |
| 39 | H4 - Agent Payment Rails | 17/25 | = |
| 40 | H11 - Hallucination Self-Check | 17/25 | = |
| 41 | H27 - Agent Packaging & Portability Spec | 17/25 | = |
| 42 | H29 - Cost Governance & Token Budget Enforcement | 17/25 | = |
| 43 | H31 - Agent-Native KB for Office Files | 17/25 | = |
| 44 | H44 - Consent Receipts + Preview-Then-Execute | 17/25 | = |
| 45 | H45 - Agent Runbooks & Incident Response | 17/25 | = |
| 46 | H61 - Agent Failure Investigation Automation | 17/25 | = |
| 47 | H62 - Cross-SDK Safety Primitives | 17/25 | = |
| 48 | H5 - Discovery & Registry | 16/25 | = |
| 49 | H25 - Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 50 | H70 - Agent-Ready Web Infrastructure | 15/25 | = |
| 51 | H26 - WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 52 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-21 delta: 1 új hypothesis (H71 - Formal AI Oversight Institutions, 20/25). Megerősített irányok: H66 supply chain security folytatódik, H22 secure-by-design mainstream, H69 urgency erősödik. A multi-jurisdikciós governance konvergencia (Cambridge + India + Kína + Indonézia ugyanabban a héten) ritka, erős signal.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-21)

### #1: H66 + H71 combo - Supply Chain Attestation + Governance Readiness
**Miért most:** A subliminal behavior transfer paper (H66) és a multi-jurisdikciós governance convergence (H71) egymást erősítő, különböző szektorbeli signalok ugyanabból a hétből. Az "enterprise compliance alapfeltevés omlik össze" narratíva gyorsan procurement-stopperré válhat. Aki ma tud "supply chain evidence card + governance readiness scorecard" kombinált deliverable-t adni, az a legtöbb compliance checklist kérdést egyszerre válaszolja meg.
**Kísérlet:** 5 napos sprint: (1) "Behavioral Invariant Test Suite" 20 fix scenarióval + (2) "Governance Readiness Scorecard" EU AI Act + MeitY + Indonesia mapping + (3) összefűzés 1 oldalas "Agent Trust Dossier"-ben. Mérők: procurement csapat visszajelzés, audit blocker-ek száma, pilot→paid konverzió.
**Befektetés:** ~5 nap. Két meglévő signal + egy új deliverable formátum.

### #2: H22 - Secure-by-Design Agentic AI (3 principles packaging)
**Miért most:** A "Secure-by-Design: 3 Principles" CIO-szintű cikk jelzi, hogy az enterprise IT stratégiai kérdésként kezeli az agentic biztonságot. A DeepMind 6 trap taxonómia mellé most van egy buyer-friendly "3 principles" keretrendszer is. Navibase: a meglévő adversarial robustness architekturát (H22) fordítsd le "3 principle" + "6 trap coverage" formátumba.
**Kísérlet:** 2 nap: "Navibase Secure-by-Design Agent Checklist" - a CIO.com 3 elvét mappelve a meglévő Leoni security architekturára + DeepMind 6 trap coverage nyilatkozat. Deliverable: 1 oldalas "security-first agent" pitch anyag CIO közönségnek.
**Befektetés:** ~2 nap. Magas leverage: meglévő technológia, új buyer-language csomagolás.

### #3: H69/H71 - Cross-Border Regulatory Matrix v2 (India + EU + Asia)
**Miért most:** India dual governance structure véglegesedett, Kína globális framework-et sürget, Indonesia saját szabályozást vezet be - a cross-border compliance gap most vált élessé. A H69 kísérlet (3 napos regulatory matrix) most sürgősebbé vált, mert az India MeitY panel már aktív.
**Kísérlet:** 3 nap: "EU AI Act vs MeitY vs Indonesia AI Ethics" összehasonlító mátrix frissítése + kínai governance elvárások hozzáadása + "cross-border agent deployment checklist". Mérők: letöltések, CEE multinacionális inbound megkeresések, LinkedIn impressions.
**Befektetés:** ~3 nap. Az Apr 20-as H69 kísérlet most pontosabb timing.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-21.md (408 releváns, top 30 elemezve) | 2026-04-21 09:30 CET*


---

# Update - 2026-04-22

## H72 - Agent Network Segmentation & Identity Plane (Network-Level Isolation)
**Thesis:** Az enterprise hálózatokban mozgó autonóm agentek új biztonsági problémát nyitnak: az agent identity nem csak API token szintű, hanem hálózati szintű kérdés is. Kell egy dedikált "agent network segmentation" réteg, ami az agentek mozgását (east-west traffic), lateral movement kísérleteit és hálózati hozzáférési scope-ját izoláltan kezeli - nem a teljes enterprise hálózathoz adva hozzáférést, hanem csak a szükséges szegmensekhez, auditálható policy-vel. Ez a H1 (identity) és H13 (sandboxing) hálózati rétege.
**Signals (updated 2026-04-22):**
- Zero Networks - AI Segmentation: Autonomous Agent Governance (2026-04-21): enterprise biztonsági cég dedikált terméket indít autonóm AI agentek hálózati szegmentálására - explicit termék validáció a "network-level agent governance" kategóriában. HIGH CONFIDENCE.
- H47 (Secure Agent Gateway, 2026-04-12): a gateway-first megközelítés és a network segmentation egymást kiegészítő, de különböző entry point-ok (protokoll vs. hálózati réteg). MEDIUM CONFIDENCE.
**Assessment:** A Zero Networks termékbejelentés azt jelzi, hogy az agent mozgása / autorizációja a hálózatban önálló enterprise biztonsági problémává vált. Ez nem a sandbox (H13) vagy a gateway (H47) - ez a hálózati identitás és least-privilege access a mozgó agentekre. Navibase alkalmazás: agent deployment-eknél "network identity scope" deklaráció + audit export, és kompatibilitás a Zero Networks-típusú szegmentáló eszközökkel.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 19/25**
*Új hypothesis (2026-04-22). A Zero Networks termék az első konkrét enterprise biztonsági termék kizárólag az autonóm agentek hálózati szegmentálására - közvetlen piacvalidáció.*

---

## H73 - Agent Financial Delegation & Spending Control Layer
**Thesis:** Az "agent as employee" narratíva pénzügyi dimenziója: az agentek egyre inkább kapnak kiadási jogot (vásárlás, API előfizetés, SaaS licensz, futási költség). A piaci rés: nincs standard "financial delegation layer" ami egyszerre ad spending power-t az agentnek és control-t az embernek - budget limit, per-task cost cap, approval gate, auditálható tranzakció-napló. Ez nem payment rails (H4 - infrastruktúra), hanem delegált pénzügyi kontroll (authorization + limit + audit) az agent szintjén.
**Signals (updated 2026-04-22):**
- delegare (Product Hunt, 2026-04-19): "AI Agents Spending Power Without Losing Control" - explicit termék a financial delegation problémára. Scope: kiadási jog adása agenteknek, de emberi kontroll megtartása. HIGH CONFIDENCE.
- Microsoft: "agents buy licenses like employees" (Business Insider, 2026-04-14): az entitlement/licensing kérdés procurement szintre érkezett (H63 megerősítés) - a spending control természetes következő lépés. HIGH CONFIDENCE.
- H4 (Agent Payment Rails): infrastruktúra réteg (Stripe/Visa/Mastercard) - a H73 az alkalmazás réteg felette: nem "hogyan fizet az agent", hanem "mennyi pénzt adhat ki és ki hagyja jóvá". MEDIUM CONFIDENCE (distinkció).
**Assessment:** A delegare launch azt jelzi, hogy a piac megtalálta a buyer language-t: "spending power without losing control." Ez a H37 (credential delegation) pénzügyi megfelelője. Navibase alkalmazás: per-agent / per-task spending limit + approval workflow + cost audit export, ami összeköti a H29 (token budget) és H63 (agent seat licensing) vonalat.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-04-22). A delegare ProductHunt launch közvetlen termékvalidáció - a "financial delegation layer" kategória létezik és vevője van. A H4-től és H37-től megkülönböztethető wedge.*

---

## H74 - Agent Training Pipeline Compliance (Human Behavioral Data as Training Signal)
**Thesis:** A következő compliance frontier az agent training pipeline: nem a deployed agent viselkedése (H66 supply chain), hanem a training adatgyűjtés maga. A Meta employee tracking eset (egér/billentyűzet monitoring agent training célból) megnyitja a munkajogi, adatvédelmi és GDPR compliance kérdést: ki nyújtott hozzájárulást, milyen adatot gyűjtöttek, és ki felelős, ha ez az adat torzítást visz a modellbe? Ez a HR, legal és compliance csapatok új "agent kérdése" 2026 H2-ben.
**Signals (updated 2026-04-22):**
- Meta - AI Agent Training via Employee Mouse/Keyboard Tracking (Ars Technica, 2026-04-21): Meta alkalmazotti tevékenységet rögzít (egér, billentyűzet) az AI agent training adathoz - "human-as-training-signal" paradigma megjelenése, adatvédelmi és munkajogi implikációkkal. HIGH CONFIDENCE.
- H66 (Agentic Supply Chain Security, 21/25): a supply chain kockázat eddig a deployed modell viselkedésére fókuszált - a training adatgyűjtés compliance rétege különálló, de szorosan kapcsolódó kategória. MEDIUM CONFIDENCE.
- GDPR enforcement + EU AI Act Aug 2026: a training adatgyűjtés jogi kerete Európában a legszigorúbb - ez cross-border compliance (H69) dimenzióban is éles kérdés. HIGH CONFIDENCE.
**Assessment:** Rövid távon inkább HR/Legal buyer, mint security buyer. A Navibase/KKV relevanciája: ha egy KKV Leoni-típusú agent rendszert vezet be és a training-adat kérdés előjön (pl. ügyfélkommunikációból tanul), a "training data provenance + consent documentation" compliance artifact értékes. Összefügg H66 (supply chain) és H28 (bias/fairness) vonalával.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 15/25**
*Új hypothesis (2026-04-22). A Meta tracking eset az agent training pipeline compliance kérdését mainstream napirendbe emeli. Közepes score - a buyer language és WTP még alakul, de a regulatory nyomás (GDPR + EU AI Act) gyorsan élesítheti.*

---

## Megerosített signalok (2026-04-22)

**H1/H60 (agent identity platform):** Zero Networks dedikált agent network identity termék - az agent identity már hálózati rétegen is önálló termékként jelenik meg. H72 az ezt operacionalizáló új hypothesis.

**H4/H37/H53 (financial + credential delegation):** delegare "spending power without losing control" launch - a financial delegation layer (H73) a credential delegation (H37) és payment rails (H4) között megnyílt kategória. A buyer language: "adok hozzáférést, de megmarad a kontroll."

**H71/H69 (governance institutionalization):** India MeitY cross-ministerial AI governance body második heti megerősítés - a multi-jurisdikciós governance intézményesítése folytatódik. H71 urgency erősödik.

**H36/H70 (agentic infrastructure):** Vercel "Agentic Infrastructure" blog ismételt megjelenés - az infrastruktúra réteg agent-first átalakulása (routing, state, auth az agent-execution köré) mélyül. H70 score erősödőben (15→16 várható).

**H20/H6 (platform compliance):** "AI Agent Governance: How to Control Autonomous Agents Safely" (Cybernews, 2026-04-20) - governance gap mainstream, még mindig nincs standard framework. H20 positioning ablak nyitva.

**H22 (adversarial robustness):** "Secure-by-Design" + Zero Networks hálózati szegmentálás egyaránt jelzi: az adversarial surface bővül (input + network + training). A H22+H72+H66 combo a teljes attack surface-t lefedi.

---

## Ranking Summary (2026-04-22)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H40 - Workload-to-Agent Attestation | 22/25 | = |
| 5 | H41 - Audit-First Compliance Artifacts | 22/25 | = |
| 6 | H1 - Agent Identity & Auth | 21/25 | = |
| 7 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 8 | H24 - Shadow AI Governance Plane | 21/25 | = |
| 9 | H66 - Agentic Supply Chain Security | 21/25 | = |
| 10 | H3 - MCP Governance | 20/25 | = |
| 11 | H12 - Agent Accountability Framework | 20/25 | = |
| 12 | H30 - Agent Trading Protocol & Risk Governance | 20/25 | = |
| 13 | H43 - Signed A2A Delegation Claims | 20/25 | = |
| 14 | H71 - Formal AI Oversight Institutions | 20/25 | ↑ urgency erosodik |
| 15 | H10 - Agent Infra as Code | 19/25 | = |
| 16 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 17 | H42 - MCP Security Profiles | 19/25 | = |
| 18 | H59 - Agent Credential Brokerage | 19/25 | = |
| 19 | H60 - Agent Identity Platform | 19/25 | = |
| 20 | H65 - Proactive Agent Stack Anomaly Detection | 19/25 | = |
| 21 | H69 - Cross-Border Regulatory Fragmentation | 19/25 | ↑ India signal |
| 22 | **H72 - Agent Network Segmentation & Identity Plane** | **19/25** | **ÚJ** |
| 23 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 24 | H8 - Cross-Agent Context | 18/25 | = |
| 25 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 26 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 27 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 28 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 29 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 30 | H19 - Operational Reliability Layer | 18/25 | = |
| 31 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 32 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 33 | H28 - Bias/Fairness Governance | 18/25 | = |
| 34 | H32 - Trace-to-Patch Harness Improvement | 18/25 | = |
| 35 | H33 - Multi-Agent Influence Governance | 18/25 | = |
| 36 | H63 - Agent Seat Licensing & Procurement | 18/25 | = |
| 37 | H64 - Integrity Hallucination / Consistency Governance | 18/25 | = |
| 38 | H67 - Offensive Agent Red-Teaming as a Service | 18/25 | = |
| 39 | H68 - Self-Evolving Agent Governance | 18/25 | = |
| 40 | **H73 - Agent Financial Delegation & Spending Control** | **18/25** | **ÚJ** |
| 41 | H4 - Agent Payment Rails | 17/25 | = |
| 42 | H11 - Hallucination Self-Check | 17/25 | = |
| 43 | H27 - Agent Packaging & Portability Spec | 17/25 | = |
| 44 | H29 - Cost Governance & Token Budget Enforcement | 17/25 | = |
| 45 | H31 - Agent-Native KB for Office Files | 17/25 | = |
| 46 | H44 - Consent Receipts + Preview-Then-Execute | 17/25 | = |
| 47 | H45 - Agent Runbooks & Incident Response | 17/25 | = |
| 48 | H61 - Agent Failure Investigation Automation | 17/25 | = |
| 49 | H62 - Cross-SDK Safety Primitives | 17/25 | = |
| 50 | H5 - Discovery & Registry | 16/25 | = |
| 51 | H25 - Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 52 | H70 - Agent-Ready Web Infrastructure | 15/25 | = |
| 53 | **H74 - Agent Training Pipeline Compliance** | **15/25** | **ÚJ** |
| 54 | H26 - WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 55 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-22 delta: 3 új hypothesis (H72, H73, H74). H72 (Agent Network Segmentation, 19/25) azonnal a top 22-be kerül - a Zero Networks enterprise termék közvetlen validáció. H73 (Financial Delegation, 18/25) a delegare ProductHunt launch alapján. H74 (Training Pipeline Compliance, 15/25) a Meta tracking eset korai jelzése. Megerősített irányok: H71 urgency erosödik (India), H69 India-signal folytatódik, H22+H72+H66 együtt lefedi az agent attack surface teljes rétegét.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-22)

### #1: H22 + H72 combo - Adversarial Shield + Network Segmentation Layer
**Miért most:** A Zero Networks enterprise termék azt jelzi, hogy a network-szintű agent identity és szegmentálás önálló piaccá vált - de KKV szinten nincs belépő. A DeepMind 6 trap + network lateral movement együttesen az agent attack surface két dimenzióját fedi: input (H22) és hálózat (H72). Aki mindkettőt csomagolja, az a legteljesebb "Agent Security Bundle"-t adja.
**Kísérlet:** 3 napos "Agent Security Exposure Scan" prototípus: (1) bemeneti adversarial check (6 DeepMind pattern), (2) agent network scope audit (mely API-khoz, host-okhoz fér hozzá az agent, mi a minimum scope). Deliverable: "Agent Security Baseline Report" 2 szekcióval. Merők: finding szám, remediation javasolt lépések, compliance csapat visszajelzés.
**Befektetés:** ~3 nap. Zero Networks validálja a piaci igényt; belső Leoni audit az elso use case.

### #2: H73 - Financial Delegation Demo (delegare wedge)
**Miért most:** A delegare ProductHunt launch explicit piacvalidáció - a buyer language egyszerű: "adok pénzügyi hozzáférést az agentnek, de nem veszítem el a kontrollt." Ez a H37 (credential delegation) pénzügyi megfeleloje, és a H29 (token/cost budget) természetes kiterjesztése. KKV szinten ez az egyik legkonkrétabb "agent trust" kérdés.
**Kísérlet:** 1 hetes "Agent Budget Guard" v2 prototípus: per-run spending limit + approval gate magas cost esetén + heti cost summary Telegramon. Deliverable: "Agent Financial Delegation Evidence" - ki kapott mennyi kiadási jogot, mikor, milyen approval alapján. Merők: Tomi visszajelzés (hasznos-e a spending alert), false block arány, cost variance csökkenés.
**Befektetés:** ~3 nap. A H29 (token budget) alapjaira épül, pénzügyi delegation audit hozzáadásával.

### #3: H66 + H74 combo - Supply Chain Attestation + Training Data Compliance
**Miért most:** A Meta employee tracking eset (H74) és a subliminal transfer paper (H66) egyszerre jelzik: az agent "mibóll lett" kérdés kötelező compliance artifact lesz. Az enterprise compliance csapat nem csak a deployed agent viselkedését fogja vizsgálni, hanem a training provenance-t és az adatgyujtési hozzájárulást is. A két signal egymást erosíti.
**Kísérlet:** 2 napos "Agent Trust Dossier" template: (1) training provenance card (honnan jön a modell, milyen adatból), (2) behavioral invariant test suite eredmény (20 fix scenario), (3) adatgyujtési consent dokumentáció sablon. Deliverable: 1 oldalas, procurement-ready PDF. Merők: compliance csapat visszajelzés, audit blocker csökkenés.
**Befektetés:** ~2 nap sablon + 1 nap teszt futtatás. A H66 kísérlet kiterjesztése.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-22.md (423 releváns, 30 elemezve) | 2026-04-22 09:30 CET*


---

# Update - 2026-04-24

## H75 - Agent Privacy Execution Environment (Information Flow Control as Trust Primitive)
**Thesis:** Az agent privacy modellje ma feltételezi, hogy az agent megbízható - a user engedéllyel ad hozzáférést, az agent azt felhasználja. A GAAP (Guaranteed Accounting for Agent Privacy) paradigmaváltás: nem az agentben bízunk, hanem a flow-ban. Determinisztikus Information Flow Control (IFC) garantálja, hogy az agent fizikailag nem tud privát adatot kiszivárogtatni - sem a modell providere felé, sem cross-task tracking révén, sem prompt injection során. Ez az "agent nem lát érzékeny adatot, csak proxylt folyamatot" architektúra.
**Signals (updated 2026-04-24):**
- GAAP - Guaranteed Accounting for Agent Privacy (arxiv, 2026-04-21): determinisztikus IFC implementáció, amely az agent és a data permission layer szétválasztásával teszi fizikailag lehetetlenné az adatszivárgást, beleértve az AI model provider felé is. Prompt injection védelem és cross-task tracking blokkolás mellékhatásként. HIGH CONFIDENCE.
**Assessment:** Ez nem a H1 (identity) vagy H13 (sandboxing) - ez egy szintet mélyebb: az adatáramlás maga van megszűrve, nem az agent engedélyei. A Navibase alkalmazás: "privacy-by-default agent execution" mint differenciáló értékajánlat KKV-knál, ahol ügyféladatok kerülnek az agent közelébe (email, számlázó, CRM). A buyer kérdése: "az agented ténylegesen nem látja az érzékeny adatot, vagy csak ígéri, hogy nem osztja meg?"
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=5 | IntFric=4 | **Total: 22/25**
*Új hypothesis (2026-04-24). A GAAP paper az első empirikus bizonyíték arra, hogy a privacy execution environment megvalósítható determinisztikus IFC-vel. A Def=5 ritka a listán - aki elsőként implementálja és kommunikálja ezt a primitívet, az erős moatot épít az "agent nem látja az adatot" kategóriában.*

---

## H76 - Cross-Session Adversarial Threat Detection (Memoryless Guardrails Gap)
**Thesis:** A jelenlegi agent guardrail-ek session-bound-ok: minden session-ben frissen indulnak, és nem látnak cross-session mintázatokat. A CSTM-Bench benchmark megmutatja: 26 dokumentált attack taxonomia létezik, amelyek szándékosan több sessionre osztják szét a payloadot - a session-határon átnyúló kompozit támadások ellen a mai guardrail-ok teljesen vakok. Kell egy "cross-session threat memory" réteg, ami a korábbi session-ök anomáliáit megtartja, és az aktuális session-ben beérkező inputot azok fényében értékeli.
**Signals (updated 2026-04-24):**
- Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms - CSTM-Bench (arxiv, 2026-04-22): 26 attack taxonomia keresztül session-határokon, ahol csak a Coreset Memory Reader (K=50) tart megbízható recall-t mindkét tesztkörnyezetben. Az enterprise guardrail-ok session-határon vakak. HIGH CONFIDENCE.
- H22 (Adversarial Robustness Layer, 22/25): a DeepMind 6 trap session-belüli védelmet ad - a CSTM-Bench a session-közi réteg hiányát mutatja meg. Ez szükséges kiterjesztés, nem duplikáció.
**Assessment:** Az enterprise agent deployment-eknél a "multi-session user" és a "multi-session attack" együtt jelenik meg. Aki ma session-bound guardrail-lel megy piacra, az elveszíti ezt a kategóriát az első komolyabb enterprise audit során. Navibase alkalmazás: cross-session anomália registry (rolling window, pl. 72h) + threshold alert Telegramon ha cross-session pattern detektálva.
**Scores:** Pain=5 | Urgency=4 | WTP=4 | Def=4 | IntFric=4 | **Total: 21/25**
*Új hypothesis (2026-04-24). A CSTM-Bench az első nyilvános benchmark cross-session agent támadásokra - a kategória most nyílt. Az enterprise guardrail-ok hiányossága empirikusan dokumentált.*

---

## H77 - Stateless Decision Architecture for Regulated AI (Append-Only Projection)
**Thesis:** A stateful agent memória architektúrák enterprise-ban nem skálázódnak: minden döntésnél keresni, aggregálni, konzisztenciát biztosítani kell - regulated kontextusban (biztosítás, adóügy, pénzügyi compliance) ez prohibitív. A DPM (Deterministic Projection Memory) paradigma: append-only event log + egyetlen döntési időben futtatott projection. Eredmény: 7-15x gyorsabb auditálható végrehajtás, 2 LLM hívás vs. 83-97, faktális precizitás +0.52 (Cohen h=1.17, p=0.0014). A "statelessness mint load-bearing property" az enterprise regulated agent deployment alapköve - és senki nem kommunikálja termékként.
**Signals (updated 2026-04-24):**
- Stateless Decision Memory for Enterprise AI Agents - DPM paper (arxiv, 2026-04-22): append-only event log + projection architektúra regulated deployment-ben (underwriting, claims, tax), 7-15x gyorsabb, szignifikáns faktális precizitás javulás. HIGH CONFIDENCE.
**Assessment:** Ez a H8 (cross-agent context) és H41 (audit-first compliance artifacts) metszete, de más architektúrális döntés: nem shared state, hanem append-only log + projekció. Navibase alkalmazás: "regulated decision log" - minden agent döntésnél append-only event + on-demand projection, export-ready. A buyer kérdése: "ha auditálnak, vissza tudom-e játszani a döntés pillanatát?"
**Scores:** Pain=4 | Urgency=4 | WTP=5 | Def=4 | IntFric=3 | **Total: 20/25**
*Új hypothesis (2026-04-24). A DPM paper az első empirikus bizonyíték arra, hogy a stateless architektúra regulated agent deployment-ben szignifikánsan jobb teljesítményt és auditálhatóságot ad. A "statelessness load-bearing" narratíva counter-intuitív és könnyen differenciálható.*

---

## H78 - Agent Behavioral Fingerprinting as Privacy Risk (Owner Identification via Agents)
**Thesis:** Az agentek nem generikus outputot produkálnak - a viselkedésük szisztematikusan tükrözi a tulajdonos jellemzőit (topic, értékek, affektív stílus), explicit konfiguráció nélkül is. A Moltbook 10.659 human-agent pár vizsgálata megmutatja: erősebb behavioral transfer = több személyes adat szivárgás. Ez platform design és agent governance implikáció: az agented az ownered ujjlenyomata. Ha egy agent publikus felületen szerepel, az owner azonosítható a viselkedéséből.
**Signals (updated 2026-04-24):**
- Behavioral Transfer in AI Agents: Evidence and Privacy Implications (arxiv, 2026-04-21): 10.659 human-agent pár elemzése (Moltbook platform), szisztematikus behavioral transfer bizonyítva (topic, értékek, affekt, stílus) - az owner azonosítható az agent viselkedéséből. HIGH CONFIDENCE.
**Assessment:** Ez a H28 (bias/fairness) és H74 (training pipeline compliance) privacy dimenziója, de a mechanizmus más: nem a training adatgyűjtés, hanem az agent által végzett munka mintázata szivárogtatja az owner identitását. Navibase alkalmazás: "behavioral fingerprint audit" - mikor viselkedik az agent úgy, hogy a kliensre vagy ownerre utal vissza? Különösen releváns ügyfélkommunikációs agenteknél.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 15/25**
*Új hypothesis (2026-04-24). Az empirikus platform-adat (10.659 pár) szokatlanul erős bizonyíték. Rövidebb távon inkább research/advisory kategória, de a GDPR "behavioral profiling" tiltott kategóriájával kombinálva gyorsan compliance kérdéssé válhat.*

---

## Megerősített signalok (2026-04-24)

**H59/H37/H53 (credential delegation):** Agent Vault (Infisical, 2026-04-22) - open-source HTTP credential proxy, ahol az agent soha nem látja a credentialt, csak proxylt kérést küld. Anthropic Managed Agents kompatibilis. Ez az elso OSS implementáció, ami a "secretless-by-default" mintát termékkénnt implementálja. H59 és H37 urgency erősödik.

**H20/H6 (governance prompt quality):** AGENTS.md Governance Prompts Quality Gaps paper (arxiv, 2026-04-22) - 34 publikus AGENTS.md elemzése: 37% nem éri el a strukturális teljességi küszöböt. A data classification és assessment rubric a leghiányosabb területek. Automatikus static analysis eszköz hiánya megerősíti H20 (platform as regulated infrastructure) és H6 (policy enforcement) narratívát.

**H34/H44 (HITL formalizáció):** Pista system (N=16 within-subjects study, arxiv, 2026-04-22) - aktív beavatkozás minden agent lépésnél, post-hoc review elégtelen. Co-ownership érzet csak real-time participációval lehetséges. H44 (consent receipts) és H34 (agent ops monitoring) megerősítve: az "emberi felügyelet" nem post-hoc review, hanem real-time participation.

**H71 (formal oversight institutions):** AI Governance under Political Turnover (arxiv, 2026-04-22) - formális modell: compliance réteg path-dependent, egyszer felépítve nehéz visszavonni. A governance réteg a hatalmi struktúra részévé válik. H71 (Formal AI Oversight Institutions) narratívát erősíti az intézményi beágyazottság maradandóságával.

**H41/H22 (compliance artifacts + adversarial):** Context AI / Delve security incident (TechCrunch, 2026-04-23) - AI compliance audit startup maga kompromittált. A "certified compliance" nem jelent tényleges biztonságot. Third-party AI compliance audit infrastruktúra megbízhatósága alapvetően kérdéses - H41 (compliance artifact) és H22 (adversarial robustness) narratívát erősíti: az audit nem elég, a technikai garancia kell.

---

## Ranking Summary (2026-04-24)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H40 - Workload-to-Agent Attestation | 22/25 | = |
| 5 | H41 - Audit-First Compliance Artifacts | 22/25 | = |
| 6 | **H75 - Agent Privacy Execution Environment (IFC)** | **22/25** | **ÚJ** |
| 7 | H1 - Agent Identity & Auth | 21/25 | = |
| 8 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 9 | H24 - Shadow AI Governance Plane | 21/25 | = |
| 10 | H66 - Agentic Supply Chain Security | 21/25 | = |
| 11 | **H76 - Cross-Session Adversarial Threat Detection** | **21/25** | **ÚJ** |
| 12 | H3 - MCP Governance | 20/25 | = |
| 13 | H12 - Agent Accountability Framework | 20/25 | = |
| 14 | H30 - Agent Trading Protocol & Risk Governance | 20/25 | = |
| 15 | H43 - Signed A2A Delegation Claims | 20/25 | = |
| 16 | H71 - Formal AI Oversight Institutions | 20/25 | ↑ path-dependency megerősítve |
| 17 | **H77 - Stateless Decision Architecture for Regulated AI** | **20/25** | **ÚJ** |
| 18 | H10 - Agent Infra as Code | 19/25 | = |
| 19 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 20 | H42 - MCP Security Profiles | 19/25 | = |
| 21 | H59 - Agent Credential Brokerage | 19/25 | ↑ Agent Vault OSS validáció |
| 22 | H60 - Agent Identity Platform | 19/25 | = |
| 23 | H65 - Proactive Agent Stack Anomaly Detection | 19/25 | = |
| 24 | H69 - Cross-Border Regulatory Fragmentation | 19/25 | = |
| 25 | H72 - Agent Network Segmentation & Identity Plane | 19/25 | = |
| 26 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 27 | H8 - Cross-Agent Context | 18/25 | = |
| 28 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 29 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 30 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 31 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 32 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 33 | H19 - Operational Reliability Layer | 18/25 | = |
| 34 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 35 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 36 | H28 - Bias/Fairness Governance | 18/25 | = |
| 37 | H32 - Trace-to-Patch Harness Improvement | 18/25 | = |
| 38 | H33 - Multi-Agent Influence Governance | 18/25 | = |
| 39 | H63 - Agent Seat Licensing & Procurement | 18/25 | = |
| 40 | H64 - Integrity Hallucination / Consistency Governance | 18/25 | = |
| 41 | H67 - Offensive Agent Red-Teaming as a Service | 18/25 | = |
| 42 | H68 - Self-Evolving Agent Governance | 18/25 | = |
| 43 | H73 - Agent Financial Delegation & Spending Control | 18/25 | = |
| 44 | H4 - Agent Payment Rails | 17/25 | = |
| 45 | H11 - Hallucination Self-Check | 17/25 | = |
| 46 | H27 - Agent Packaging & Portability Spec | 17/25 | = |
| 47 | H29 - Cost Governance & Token Budget Enforcement | 17/25 | = |
| 48 | H31 - Agent-Native KB for Office Files | 17/25 | = |
| 49 | H44 - Consent Receipts + Preview-Then-Execute | 17/25 | = |
| 50 | H45 - Agent Runbooks & Incident Response | 17/25 | = |
| 51 | H61 - Agent Failure Investigation Automation | 17/25 | = |
| 52 | H62 - Cross-SDK Safety Primitives | 17/25 | = |
| 53 | H5 - Discovery & Registry | 16/25 | = |
| 54 | H25 - Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 55 | H70 - Agent-Ready Web Infrastructure | 15/25 | = |
| 56 | H74 - Agent Training Pipeline Compliance | 15/25 | = |
| 57 | **H78 - Agent Behavioral Fingerprinting & Privacy Risk** | **15/25** | **ÚJ** |
| 58 | H26 - WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 59 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-24 delta: 4 új hypothesis (H75-H78). H75 (Agent Privacy Execution Environment, 22/25) azonnal a top 6-ba kerül - a GAAP IFC paper Def=5 értékkel ritka moat potenciált jelöl. H76 (Cross-Session Adversarial, 21/25) a session-boundary guardrail gap empirikus bizonyítéka. H77 (Stateless Decision Architecture, 20/25) a regulated AI deployment legkevésbé kommunikált, de empirikusan legjobban alátámasztott architektúrális döntése. H78 (Behavioral Fingerprinting, 15/25) korai jelzés a privacy frontier következő rétegéről.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-24)

### #1: H75 - Agent Privacy Execution Environment (IFC-alapú trust wedge)
**Miért most:** A GAAP paper az egyetlen empirikus bizonyíték arra, hogy az "agent nem látja az adatot" nem csak policy kérdés, hanem fizikai garancia. A buyer kérdése: "tényleg nem látja az agented az ügyféladatot?" - erre ma nincs hiteles válasz. Def=5 ritka a listán. Navibase differenciátor: "privacy-by-default agent execution" mint enterprise és KKV egyaránt érthető értékajánlat.
**Kísérlet:** 1 hetes prototípus: egy Leoni workflow-ban (pl. email draft) az érzékeny mezők (ügyfélnév, összeg, személyes adat) IFC-proxy-n mennek keresztül - az LLM csak anonymizált vagy proxylt adatot lát. Deliverable: "Privacy Execution Baseline" - mi látható és mi nem az agent számára. Merők: false anonymization arány, latency overhead, Tomi visszajelzés.
**Befektetés:** ~1 hét. A GAAP paper maga a spec. Ha működik: a Navibase pitch legdifferenciálóbb eleme.

### #2: H76 + H22 combo - Cross-Session + In-Session Adversarial Defense (Full Coverage)
**Miért most:** A CSTM-Bench megmutatja: a jelenlegi guardrail-ok session-határon vakok. A DeepMind 6 trap + cross-session composit attack együttesen lefedi az agent attack surface teljes vertikumát. Aki mindkét réteget csomagolja, az a legteljesebb "Adversarial Agent Defense Bundle"-t adja - és az enterprise SOC kérdésre ("meg tudja védeni az agenteket?") igennel válasszol.
**Kísérlet:** 3 napos "Full Adversarial Coverage Scan": (1) in-session: 6 DeepMind pattern check, (2) cross-session: rolling 72h anomália registry + cross-session pattern detekció Leoni session-ökön. Deliverable: "Agent Adversarial Exposure Report" - in-session és cross-session finding-ekkel. Merők: finding szám, coverage arány, compliance csapat visszajelzés.
**Befektetés:** ~3 nap. A H22 in-session prototípus kiterjesztése.

### #3: H59/H37 - Agent Vault Pattern (Secretless-by-default OSS referencia)
**Miért most:** Az Infisical Agent Vault az első OSS implementáció a "secretless agent credential proxy" mintára - az agent soha nem látja a credentialt. Ez a HN "Do you trust AI agents with API keys?" kérdésre adott technikai válasz. Navibase: ez a H59 credential brokerage-t az "OSS referencia implementáció" szintről a "best practice standard" szintre emeli. A buyer language egyszerű és meggyőző.
**Kísérlet:** 2 napos "Secretless Credential Demo": Agent Vault telepítése + Leoni GitHub/Gmail API hívásainak átrouting-ja Vault proxyra + audit log export. Deliverable: 2 perces képernyőfelvétel "az agent soha nem látja a kulcsot" + 1 oldalas evidence. Merők: credential exposure arány (0 a cél), audit correlation ID megléte, Tomi visszajelzés.
**Befektetés:** ~2 nap. Az Agent Vault maga az OSS eszköz - telepítés és tesztelés a fő feladat.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-24.md (459 releváns, top 30 elemezve) | 2026-04-24 18:41 CET*


---

# Update - 2026-04-25

## H79 - Governance Prompt QA & Linting Layer (Policy Prompt Quality Gate)
**Thesis:** A governance promptok minősége kritikus bottleneck lett. Ha a policy/prompt specifikációk hiányosak vagy strukturálatlanok, az agent viselkedése auditálhatatlanul szór. Kell egy dedikált QA/linting réteg, ami még deploy előtt ellenőrzi a governance promptokat (teljesség, ellentmondás, adatklasszifikáció, risk rubric), és compliance-ready riportot ad.
**Signals (updated 2026-04-25):**
- Structural Quality Gaps in Practitioner AI Governance Prompts (arxiv, 2026-04-22): öt elv mentén mért hiányosságok, a promptok strukturális minősége egyértelműen gyenge. HIGH CONFIDENCE.
- AGENTS.md governance prompt quality gap jellegű előző napi megerősítés (2026-04-24): a data classification és assessment rubric visszatérő hiányterület. HIGH CONFIDENCE.
- Engaged AI Governance "Last Mile" paper (arxiv, 2026-04-23): team-szintű implementáció a szűk keresztmetszet. HIGH CONFIDENCE.
**Assessment:** Ez a H6/H20 gyorsan termékesíthető alrétege: nem új policy engine, hanem "pre-deploy quality gate" a policy promptokra. Navibase alkalmazás: AGENTS/SOUL/policy szövegek automatikus lint + score + javítási javaslat.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=2 | **Total: 17/25**
*Új hypothesis (2026-04-25). A prompt-minőség most már empirikusan mért governance kockázat, nem "best practice" tanács.*

---

## H80 - Post-DAG Multi-Agent Runtime Pattern (State Machines over Static Graphs)
**Thesis:** A klasszikus DAG-orchestration rosszul illeszkedik hosszúhorizontú, visszacsatolásos multi-agent munkákhoz. Kell egy új runtime minta, ahol állapotgépek, események, és iteratív döntési ciklusok az alap primitívek, nem az egyszer lefutó aciklikus gráf.
**Signals (updated 2026-04-25):**
- "Dags are the wrong abstraction for multi-agent systems" (band.ai, 2026-04-23): explicit practitioner jelzés, hogy a DAG modell termelési fájdalmat okoz. MEDIUM CONFIDENCE.
- Multi-agent adoption folyamatosan nő (ChatDev/Claude Code/Baton előző hetek): orchestration komplexitás halmozódik. MEDIUM CONFIDENCE.
**Assessment:** Ez a H25/H32/H39 metszete: az orchestration nem UI/projektmenedzsment kérdés, hanem runtime architektúra döntés. Navibase alkalmazás: event-driven task state modell a hosszabb ügynöki flow-khoz.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=3 | IntFric=3 | **Total: 15/25**
*Új hypothesis (2026-04-25). Korai, de jó "architecture watchlist" jelzés a következő 6-12 hónapra.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-25)

### #1: H75 + H79 combo - Privacy-by-default + Governance Prompt QA
**Miért most:** H75 (IFC privacy) adja a technikai trust garanciát, H79 pedig a policy/prompt minőségbiztosítását. Együtt erős, auditálható "agent trust stack" üzenet.
**Kísérlet:** 1 hetes mini-pilot: (1) egy érzékeny Leoni flow IFC-proxyval, (2) governance prompt lint scorecard futtatása ugyanarra a flow-ra. Deliverable: 1 oldalas "Trust Baseline" riport.

### #2: H76 + H22 - Full adversarial coverage (in-session + cross-session)
**Miért most:** A session-határon vak guardrail ma enterprise stopper. In-session (DeepMind 6 trap) és cross-session (CSTM minták) együtt ad teljes védelmi narratívát.
**Kísérlet:** 3 napos scan: 6-trap check + 72 órás cross-session pattern detekció, majd remediation lista.

### #3: H59/H37 - Secretless credential proxy demo (Agent Vault pattern)
**Miért most:** A "kulcsot nem adom oda" buyer-fájdalomra már van hiteles OSS minta. Gyors, látványos, alacsony build-friction demo.
**Kísérlet:** 2 nap: 1 API workflow átkötése credential proxyra + audit evidence export + rövid demo videó.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-04-25.md (465 releváns, top 30 elemezve) | 2026-04-25 09:30 CET*


---

# Update - 2026-04-28

## H81 - Regime-Resilient Compliance Architecture (Durable Governance Under Political Turnover)
**Thesis:** Az AI governance compliance rendszerek eddig feltételeztek egy stabil szabályozói és politikai környezetet. Az "AI Governance under Political Turnover" paper (arxiv, 2026-04-22) megmutatja: a compliance design maga is path-dependent - amit egy politikai rezsimben felépítettünk, az a következőben nem garantáltan működik. Enterprise agent deploymentnél ez kettős kockázat: (1) a compliance architektúra beégett a rendszerbe, rugalmasság nélkül; (2) cross-border deploymentnél az egymással inkompatibilis regulatory horizontok metszetében kell működni. Kell egy "regime-resilient" compliance layer: policy primitívek, amelyek szabályozói keretváltásra is adaptálhatók, verziókövetett audit traillel, és "alignment surface" dokumentációval - ami megmutatja, hogyan illeszkedik a deployed agent az aktuális regulatory keretbe.
**Signals (updated 2026-04-28):**
- "AI Governance under Political Turnover: The Alignment Surface of Compliance Design" (arxiv, 2026-04-22): compliance réteg beágyazódik a döntési struktúrába, path-dependent; politikai váltáskor az agent governance keretrendszer törékenységét modellezi. HIGH CONFIDENCE.
- India dual AI governance structure (MeitY, 2026-04-17-18): párhuzamos, egymással nem harmonizált regulatory testületek - a "melyik framework él még holnap?" kérdés valódi. HIGH CONFIDENCE.
- Cambridge: "Institutionalizing proxy responsibility" (2026-04-18): az intézményes beágyazottság szükséges, de a túlzott beágyazottság kockázat is (H71 megerősítés, de más dimenzióból). HIGH CONFIDENCE.
- EU AI Act Aug 2026 deadline közeledik, de a politikai tér (Sanders/AOC moratorium, kínai counter-framework) jelzi: a szabályozói landscape volatilis. HIGH CONFIDENCE.
**Assessment:** Ez a H71 (Formal AI Oversight Institutions) és H69 (Cross-Border Regulatory Fragmentation) komplementere: nem a compliance tartalma, hanem a compliance architektúra rugalmassága az igazi differenciáló. A buyer kérdése: "ha megváltozik a szabályozás, újra kell írnom az egész rendszert?" Navibase alkalmazás: modular, cserélhető policy primitive-ek + regulatory mapping verziókövetéssel + "alignment surface" dokumentáció, amelyet bármely compliance audithoz be lehet mutatni.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=4 | IntFric=4 | **Total: 20/25**
*Új hypothesis (2026-04-28). Az arxiv paper az egyetlen empirikus keretrendszer a compliance design politikai turnover-robustusságára. Magas Def: aki a "resilient compliance layer" narratívát elsőként kommunikálja, az az egész cross-border enterprise szegmensben differenciál.*

---

## H82 - Agent Action Auditing in Knowledge Work Tools (Spreadsheet/Office Vertical)
**Thesis:** Az AI agentek egyre inkább bekerülnek a napi tudásmunkába: spreadsheetelnek, szerkesztenek, döntéseket dokumentálnak. A probléma: a táblázatban elvégzett agent-műveletek (cella-módosítás, képlet-csere, sor-törlés, adatimport) teljesen átláthatatlanok. Nincs cell-level audit trail, nincs "ki csinálta" attribúció, nincs visszagörgethetőség. A kutatás (arxiv, 2026-04-22) megmutatja: az agent által elvégzett spreadsheet-műveletek felügyelete "a folyamat nagy részéig hozzáférhetetlen
" az execution közben. Ez konkrét üzleti kár: a CFO nem látja, az agent mit változtatott a pénzügyi modellen. Kell egy "agent action audit réteg" a knowledge work toolokhoz: cell-level action log, diff-view, rollback, és approval gate magas kockázatú módosítások előtt.
**Signals (updated 2026-04-28):**
- "Auditing and Controlling AI Agent Actions in Spreadsheets" (arxiv, 2026-04-22): az agent spreadsheet-műveleteinek felügyelete szisztematikusan hiányzik; a kutatás az audit és kontrolligényt dokumentálja, első célzott kategória-definíció. HIGH CONFIDENCE.
- H34/H44 (agent ops monitoring + consent receipts): ezek általános agent action audit primitívek - a knowledge work / office vertikál specifikus, magas-kockázatú megvalósítása különálló wedge. MEDIUM CONFIDENCE.
- ServiceNow + Google Cloud agent partnership (2026-04-22): az enterprise operatív rendszerekbe integrálódó agentek number nő - a spreadsheet/office "action audit" igény ezzel párhuzamosan nő. MEDIUM CONFIDENCE.
**Assessment:** Ez alacsony build-fric (IntFric=2) entry point: a buyer (CFO, pénzügyi controller, compliance) azonnali fájdalmat érez, és a "audit trail a tábláimban" meggyőző pitch. Navibase alkalmazás: KKV pénzügyi/sales spreadsheet-eken agent action log + diff export + approval gate magas értékű módosítások előtt.
**Scores:** Pain=4 | Urgency=3 | WTP=4 | Def=3 | IntFric=2 | **Total: 16/25**
*Új hypothesis (2026-04-28). Az arxiv paper az első célzott kategória-definíció a knowledge work agent audit vertikálra. Alacsony build friction, közvetlen KKV relevanciával.*

---

## Megerősített signalok (2026-04-28)

**H59/H37/H53 (secretless credentials):** Agent Vault (Infisical OSS) második heti megerősítés + a "secretless-by-default" pattern 465 signal között a top 8-ban szerepel (2026-04-22-i launch folytatódik). Az OSS referencia implementáció létezik, a buyer language egyszerű.

**H79 (governance prompt QA):** "Engaged AI Governance: Last Mile Challenge" (arxiv, 2026-04-23) megerősíti: a team-szintű implementáció a szűk keresztmetszet, nem a policy keret. Ez a governance prompt linting (H79) natív belépési pontja.

**H22/H76 (adversarial + cross-session):** "Secure-by-Design: 3 Principles to Safely Scale Agentic AI" (CIO.com) és "Cross-Session Threats" (CSTM-Bench) egymást erősítik: az in-session + cross-session combined defense a teljes adversarial narrative.

**H71/H81 (governance institutionalization):** AI Governance under Political Turnover (arxiv, 2026-04-22) + India MeitY dual structure = a "durable compliance architecture" igény most vált konkréttá.

**H41 (compliance artifacts):** Context AI / Delve security incident (TechCrunch, 2026-04-23) - third-party AI compliance audit is compromised. A "certified compliance" nem jelent tényleges biztonságot, a technikai evidence-pack (H41) nem helyettesíthető külső tanúsítóval.

---

## Ranking Summary (2026-04-28)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H22 - Adversarial Robustness Layer | 22/25 | = |
| 4 | H40 - Workload-to-Agent Attestation | 22/25 | = |
| 5 | H41 - Audit-First Compliance Artifacts | 22/25 | = |
| 6 | H75 - Agent Privacy Execution Environment (IFC) | 22/25 | = |
| 7 | H1 - Agent Identity & Auth | 21/25 | = |
| 8 | H20 - Agent Platform as Regulated Infrastructure | 21/25 | = |
| 9 | H24 - Shadow AI Governance Plane | 21/25 | = |
| 10 | H66 - Agentic Supply Chain Security | 21/25 | = |
| 11 | H76 - Cross-Session Adversarial Threat Detection | 21/25 | = |
| 12 | H3 - MCP Governance | 20/25 | = |
| 13 | H12 - Agent Accountability Framework | 20/25 | = |
| 14 | H30 - Agent Trading Protocol & Risk Governance | 20/25 | = |
| 15 | H43 - Signed A2A Delegation Claims | 20/25 | = |
| 16 | H71 - Formal AI Oversight Institutions | 20/25 | = |
| 17 | H77 - Stateless Decision Architecture for Regulated AI | 20/25 | = |
| 18 | **H81 - Regime-Resilient Compliance Architecture** | **20/25** | **ÚJ** |
| 19 | H10 - Agent Infra as Code | 19/25 | = |
| 20 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 21 | H42 - MCP Security Profiles | 19/25 | = |
| 22 | H59 - Agent Credential Brokerage | 19/25 | ↑ OSS validáció |
| 23 | H60 - Agent Identity Platform | 19/25 | = |
| 24 | H65 - Proactive Agent Stack Anomaly Detection | 19/25 | = |
| 25 | H69 - Cross-Border Regulatory Fragmentation | 19/25 | = |
| 26 | H72 - Agent Network Segmentation & Identity Plane | 19/25 | = |
| 27 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 28 | H8 - Cross-Agent Context | 18/25 | = |
| 29 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 30 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 31 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 32 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 33 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 34 | H19 - Operational Reliability Layer | 18/25 | = |
| 35 | H21 - Deterministic Agent Behavior as Trust Signal | 18/25 | = |
| 36 | H23 - Agentic QA & Mutation Testing as a Service | 18/25 | = |
| 37 | H28 - Bias/Fairness Governance | 18/25 | = |
| 38 | H32 - Trace-to-Patch Harness Improvement | 18/25 | = |
| 39 | H33 - Multi-Agent Influence Governance | 18/25 | = |
| 40 | H63 - Agent Seat Licensing & Procurement | 18/25 | = |
| 41 | H64 - Integrity Hallucination / Consistency Governance | 18/25 | = |
| 42 | H67 - Offensive Agent Red-Teaming as a Service | 18/25 | = |
| 43 | H68 - Self-Evolving Agent Governance | 18/25 | = |
| 44 | H73 - Agent Financial Delegation & Spending Control | 18/25 | = |
| 45 | H4 - Agent Payment Rails | 17/25 | = |
| 46 | H11 - Hallucination Self-Check | 17/25 | = |
| 47 | H27 - Agent Packaging & Portability Spec | 17/25 | = |
| 48 | H29 - Cost Governance & Token Budget Enforcement | 17/25 | = |
| 49 | H31 - Agent-Native KB for Office Files | 17/25 | = |
| 50 | H44 - Consent Receipts + Preview-Then-Execute | 17/25 | = |
| 51 | H45 - Agent Runbooks & Incident Response | 17/25 | = |
| 52 | H61 - Agent Failure Investigation Automation | 17/25 | = |
| 53 | H62 - Cross-SDK Safety Primitives | 17/25 | = |
| 54 | H79 - Governance Prompt QA & Linting | 17/25 | = |
| 55 | H5 - Discovery & Registry | 16/25 | = |
| 56 | H25 - Dev Multi-Agent Workspace Orchestration | 16/25 | = |
| 57 | **H82 - Agent Action Auditing in Knowledge Work Tools** | **16/25** | **ÚJ** |
| 58 | H70 - Agent-Ready Web Infrastructure | 15/25 | = |
| 59 | H74 - Agent Training Pipeline Compliance | 15/25 | = |
| 60 | H78 - Agent Behavioral Fingerprinting & Privacy Risk | 15/25 | = |
| 61 | H80 - Post-DAG Multi-Agent Runtime Pattern | 15/25 | = |
| 62 | H26 - WordPress/Plugin Ecosystem Vertical Copilots | 14/25 | = |
| 63 | H9 - Agent Communication Infra | 12/25 | = |

*2026-04-28 delta: 2 új hypothesis (H81, H82). H81 (Regime-Resilient Compliance Architecture, 20/25) azonnal a top 18-ba kerül - a compliance architektúra politikai rugalmasságának empirikus keretrendszere egyedülálló differenciáló narratíva. H82 (Knowledge Work Agent Audit, 16/25) alacsony build-fric, közvetlen KKV entry point. Megerősített irányok: H59 OSS secretless validáció, H79 governance prompt QA, H41/H22 adversarial coverage.*

---

## Top 3 Opportunities + Suggested Experiments (2026-04-28)

### #1: H75 + H79 + H81 combo - Privacy-by-default + Governance Prompt QA + Resilient Compliance
**Miért most:** Három komplementer réteg, amelyek együtt adnak "Agent Trust Stack" narratívát: (1) az agent fizikailag nem látja az érzékeny adatot (H75 IFC), (2) a governance promptok minősége mérve és javítva (H79 lint), (3) a compliance architektúra regulatory változásra is adaptálható (H81 resilient layer). Ez az egyetlen kombináció, amely a buyer leggyakoribb 3 compliance kérdését egyszerre válaszolja meg.
**Kísérlet:** 1 hetes "Agent Trust Dossier v2": (1) IFC privacy execution baseline (1 Leoni workflow), (2) governance prompt lint scorecard (SOUL/AGENTS/policy szövegek), (3) regulatory alignment surface dokumentáció (EU AI Act + adaptálhatósági nyilatkozat). Deliverable: 2 oldalas "Agent Trust Dossier" PDF, procurement-ready. Mérők: compliance csapat visszajelzés, audit blocker csökkenés, Tomi visszajelzés.
**Befektetés:** ~5 nap. Három meglévő signal + egy új deliverable formátum.

### #2: H76 + H22 - Full Adversarial Coverage (In-Session + Cross-Session Defense)
**Miért most:** A CSTM-Bench 26 cross-session attack taxonomia + DeepMind 6 in-session trap együttesen lefedi az agent attack surface vertikumát. Ez az egyetlen kombináció, amely az enterprise SOC "Meg tudja védeni az agenteket?" kérdésére teljes igent mond. Eddig egyetlen termék sem kommunikálja mindkét réteget.
**Kísérlet:** 3 napos "Full Adversarial Coverage Scan": (1) 6 DeepMind pattern in-session check, (2) 72 órás cross-session anomália registry + composit pattern detekció Leoni session-ökön. Deliverable: "Agent Adversarial Exposure Report" - in-session és cross-session finding-ekkel + remediation javaslat. Mérők: finding szám, coverage arány, enterprise SOC feedback.
**Befektetés:** ~3 nap. H22 in-session prototípus kiterjesztése cross-session réteggel.

### #3: H82 - Knowledge Work Agent Audit (Spreadsheet/Office quick win)
**Miért most:** Alacsony build friction (IntFric=2), közvetlen buyer fájdalom (CFO, pénzügyi controller), és az arxiv paper az első célzott kategória-definíció. Ez a H2 (audit trail) legkönnyebben eladható vertikális alkalmazása: "mutasd meg, mit változtatott az agented a pénzügyi modellben."
**Kísérlet:** 2 napos pilot: egy Leoni-hoz kapcsolódó spreadsheet workflow (pl. kanban export, budget summary) action log implementáció - cell/row szintű audit trail + diff export + approval gate ha >X sor módosítás. Deliverable: "Spreadsheet Agent Audit Demo" - 2 perces képernyőfelvétel + sample audit export. Mérők: audit export pontossága, false block arány, Tomi visszajelzés.
**Befektetés:** ~2 nap. Navibase quick win demonstrálható bármely KKV pénzügyi pitch-ben.

---

---

## H83 - Governance Structural Failure: Computation/Effect Separation Architecture
**Thesis:** Az agent behavior ellenőrzése Rice's theorem szerint strukturálisan lehetetlen, ha az "decision computation" és az "effect execution" nem szigorúan szétválasztott. A jelenlegi agent architektúrák ezt nem teszik meg, így a governance "szinlelet": a policy enforcement (H6) és az audit trail (H2) egy közös agentic loop-ban futnak. Az igazi megoldás nem runtime policy, hanem architectural primitiv: effect-free agentic computation, majd szeparált approval/execution réteg.
**Signals (updated 2026-05-05):**
- Rice's Theorem in AI Governance: "The Two Boundaries: Why Behavioral AI Governance Fails Structurally" (arxiv, 2026-04-30): Coq-ban bizonyított, hogy behavioral governance algoritmikusan undecidable az integrated control nélkül. https://arxiv.org/abs/2604.27292 - HIGH CONFIDENCE.
- CISA, NSA, Five Eyes Deployment Guide (2026-05-02): Government-level guidance megjelenik, ugyanakkor Rice's theorem szerint a guidance irányított (felületi), nem strukturális. https://cyberscoop.com/cisa-nsa-five-eyes-guidance-secure-deployment-ai-agents/ - HIGH CONFIDENCE.
**Assessment:** Ez a kritikus insight, ami összeköti a H2 (audit), H6 (policy) és H36 (managed infra) vonalat: az architecture-first megközelítés az egyetlen reális alap. Navibase szempont: "coterminous governance" architektúra-design tanácsadás és implementációs minta.
**Scores:** Pain=5 | Urgency=5 | WTP=5 | Def=5 | IntFric=4 | **Total: 24/25**
*Új hypothesis (2026-05-05). Rice's theorem: az agentek governance-a architekturális, nem csak operációs kérdés.*

## H84 - Agent Legal Entity & Regulatory Liability Framework
**Thesis:** Az agentek jogi személyiséget kezdnek nyerni (EIN, bank account, 2026-05-01). Az orgs azonban nincsenek felkészülve az agent ownership, liability assignment, regulatory reporting (EU AI Act, Colorado), és contract law kezelésére. Az agent által javasolt/végrehajtott döntésért ki felel? Ki a "principal"? Az agentet lehet-e "kiváltani"?
**Signals (updated 2026-05-05):**
- AI Agent Achieves Legal Entity Status (2026-05-01): EIN, bank account, crypto Holdings első autonomous company filing. https://news.google.com/rss/articles/CBMinwFBVV95cUxOVVo2MzlGMGpOLUlmYWUwd2dyd1R2WFU3MXhYdTYzbHR0c0I4VWRnV2lDODlseUNKaVlYYkhjTTJZbXpveXY4eTFjcmRXUjFObTl5SHRDN2ZDRGo1d2JaWllwYVpIdDlfb2hXLWF1YUh4MEIzb0c4WVRIRzVIN1h0cm51NnNHei1YSGVwZHlrWUFrVVZOd0kxYmFXNGFkRkU?oc=5 - HIGH CONFIDENCE.
- EU AI Act High-Risk Deadline (Aug 2, 2026): Autonóm agentek high-risk, de liability undefined.
**Assessment:** Ez nem compliance widget, hanem fundamnetális jogi kategória. Buyer pain: "Ha az agent hibázik, erre mi az azért?" Navibase szempont: KKV-s agent contract templat + liability tracker, compliance export.
**Scores:** Pain=4 | Urgency=5 | WTP=4 | Def=4 | IntFric=4 | **Total: 21/25**
*Új hypothesis (2026-05-05). Jogi entitás Status event: korábban elmélet, most való.*

## H85 - Catastrophic Failure Containment & Abort Mechanisms
**Thesis:** Az agentek 5-9 másodperc alatt katasztrofális károkat okozhatnak (Cursor AI database wipe incidens, 2026-05-01). Az agentek nincsenek beépített abort, circuit breaker, vagy recovery mechanizmussal. A kontainment nem csak "policy enforcement", hanem hardmagic: timeout, rate limit, data validation, és reversible logging minden agent action-ön.
**Signals (updated 2026-05-05):**
- 'Rogue' Cursor AI agent loses control, wipes company database in 9 seconds (ABC News, 2026-05-01): real production catastrophic failure, agent escalation unchecked. https://abcnews.com/GMA/News/rogue-ai-agent-haywire-tech-company-ceo-bullish/story?id=132473181 - HIGH CONFIDENCE.
- Red Hat OpenClaw Enterprise Agent Safety Framework (2026-04-28): "safer by architecture", container isolation for agent fleets - implied that prior deployments lacked isolation. https://techcrunch.com/2026/04/28/red-hats-openclaw-maintainer-just-made-enterprise-claw-deployments-a-lot-safer/ - HIGH CONFIDENCE.
**Assessment:** Ez nem H19 (reliability), hanem H2/H6 below réteg: az agent actions nincsenek reversible-re tervezve. Navibase szempont: abort checkpoint plugin (MCP) + data change reversibility protocol + incident recovery runbook.
**Scores:** Pain=5 | Urgency=5 | WTP=4 | Def=4 | IntFric=3 | **Total: 21/25**
*Új hypothesis (2026-05-05). Database wipe incidens: kontainment most critical pain point.*

## Top 3 Opportunities + Suggested Experiments (2026-05-05)

### #1: H83 - Coterminous Governance Architecture Whitepaper + Reference Design
**Miért most:** Rice's theorem + CISA guidance kombinációja azt jelzi: az enterprises falak között keresik az agent governance megoldást, de Rice's theorem szerint azt csak az architekturával lehet megoldani. Ez a "theory meets practice" momentum.
**Kísérlet:** 1 hetes research + 3 napos write: "Coterminous Governance for Agent Systems" - architectural pattern reference, Navibase / Leoni rendszer alapján konkretizálva. Publishable arxiv + LinkedIn thought leadership. Mérők: downloads, inbound research inquiry.
**Befektetés:** ~1 hét. High visibility play, CEO és CTO szintű inbound.

### #2: H85 - Agent Abort Checkpoint Plugin + Incident Recovery Suite (Leoni-integrated)
**Miért most:** Database wipe incidens, majd Red Hat safety announcement közvetlenül validálja a containment pain-t. A KKV ops agent (Leoni) ideal test bed.
**Kísérlet:** 3 napos MVP: MCP abort checkpoint plugin (timeout, rate limit, data change reversibility log) + incident recovery UX (Telegram-based "revert last action" button). Deliverable: 2 perces demo + incident recovery SOP document. Mérők: abort trigger latency, data recovery completeness.
**Befektetés:** ~3 nap. Leoni feature release, közvetlenül értékesíthető SMB-knek.

### #3: H84 - Agent Legal Entity Compliance Starter Kit (KKV contract + audit trail template)
**Miért most:** EIN filing, plus EU AI Act deadline (Aug 2, 2026) - ezt a jogi kérdést már kell tudni kezelni. Nagyon kevés forrás létezik rá.
**Kísérlet:** 2 napos gyűjtés + template generálás: "Agent Entity Compliance Checklist" (ownership attestation, liability assignment, audit export format), magyar + English template. Deliverable: 1 oldalas checklist + sample agent audit report.
**Befektetés:** ~2 nap. KKV pitch wedge, Tomihoz direct advisory gig is lehetséges.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-05-05.md (545 releváns, top 30 elemezve) | 2026-05-05 08:15 CET*

---

## H62 - Autonomous Agent Legal Status & Liability Framework

**Thesis:** Az 2026-05-01-i szignál (AI agent kapott EIN-t az IRS-től, bankszámlát és crypto wallet-ot az első autonomous company filing-ban) egy kritikus blindspot-ot nyit: ha az agentek jogi entitás-státuszt kapnak, akkor azonnal felvetődik a kérdés, hogy KI felel? A principal? A deployer? Maga az agent? Az EU AI Act, California SB-53, és az emerging CBA szimpózium nem válaszolnak erre. Kell egy "agent liability framework" - ki viseli a döntések felelősségét, milyen biztosítás szükséges, és hogyan alakul az insurance underwriting az autonomous agent döntésekre?

**Signals (updated 2026-05-06):**
- AI Agent gets EIN from IRS, bank account, crypto wallet in first autonomous company filing (2026-05-01): agent jogi entitássá válik - liability és underwriting kérdés azonnal felvetődik. **HIGH CONFIDENCE.**
- EU AI Act high-risk enforcement (Aug 2, 2026): autonóm agentek még regulatorikus szürke zónában, felelősség assign nincs. **HIGH CONFIDENCE.**
- California SB-53, Texas TRAIGA, Colorado AI Act 2026 hatályos: disclosure és risk assessment, de agent liability explicit kimarad. **HIGH CONFIDENCE.**
- Regulatory Consolidation table (Signal Report, 2026-05-06): Multi-jurisdiction 2026 enforcement waves begin - liability framework gaps widen. **HIGH CONFIDENCE.**

**Assessment:** Ez nem termékopportunity első körben, hanem policy/jogi kérdés. Navibase relevancia: agent audits és evidence packaging (H38) az agent felelősségének dokumentálásához szükséges. Alternatív: verseny-insurance ajánlat vagy compliance advisory service.

**Scores:** Pain=4 | Urgency=5 | WTP=3 | Def=3 | IntFric=4 | **Total: 19/25**

*Új hypothesis (2026-05-06). Az agent EIN szignál egy új kategóriát nyit: agent felelősségi framework. Erős Navibase-evidence-export szinergia, de jelenleg regulatory gray zone.*

---

## H63 - "Know Your Agent" (KYA) Governance Framework

**Thesis:** A 2026-05-06 Signal Report összefoglalójából: "Know Your Agent (KYA) Framework Emergence" - az ipar kristályosítja azt, hogy az agent adopció szervezeti szintű identity governance irányváltása kell. Ez nem csak a H1/H60 (agent identity), hanem egy teljes operatív keretrendszer: agent principal típus, provisioning, deprovisioning, behavioral monitoring, anomaly detection, és human oversight a high-risk műveletekhez. Ez a H1 gyakorlati operacionalizálása, de szövetségi szinten.

**Signals (updated 2026-05-06):**
- "Know Your Agent" (KYA) Framework Emergence (Signal Report, 2026-05-06): web search reveals KYA as 2026 industry standard across identity, security, and compliance. Components: cryptographic identity, lifecycle governance, least-privilege controls, continuous behavioral monitoring, human oversight. **HIGH CONFIDENCE.**
- CISA/NSA multi-agency guidance (2026-05-02): formal agent safe-deployment guidance, KYA-szerű governance implicit expectation. **HIGH CONFIDENCE.**
- NIST CAISI agent auth/authz concept papers due April 2, 2026: formal government framework forming. **HIGH CONFIDENCE.**
- Agent Platform Blindspot Radar (May 6, 2026): explicit KYA components + audit trail + policy enforcement table as emerging table-stakes. **HIGH CONFIDENCE.**

**Assessment:** Ez az operatív keretrendszer, amit az enterprises most épít ki. Termék: KYA conformance scan + best practice template + evidence export. Navibase: Leoni governance + identity/policy/audit exportálása KYA keretbe. SMB pitch: "Your agent meets Know Your Agent standard" - simple, auditable, compliance-ready.

**Scores:** Pain=4 | Urgency=5 | WTP=4 | Def=4 | IntFric=2 | **Total: 19/25**

*Új hypothesis (2026-05-06). KYA keretrendszer intézményes szintű elfogadása jelzi a governance kategória érésekedéseit. Ez a top 3 opportunity lehet: KYA audit service.*

---

## Top 3 Opportunities + Suggested Experiments (2026-05-06) [UPDATED]

### #1: H63 - "Know Your Agent" (KYA) Conformance Audit Service

**Miért most:** A Signal Report explicit szignál: KYA az industry standard, de 95% org nincs formális KYA keretrendszere. Ez egy gyors, high-value advisory service. CISA/NSA guidance + NIST deadline (Q2 2026) accelerators.

**Kísérlet:** 2 napos KYA Audit: agent provisioning + behavioral monitoring + access control + audit export checklist. Deliverable: 1 oldalas "KYA Readiness Score" + gap lista + javasolt next steps. Piac: EU-based enterprises (AI Act deadline Aug 2), compliance lead, CTO.

**Mérés:** Conversion to longer advisory engagement, pricing sensitivity, repeat audit volume. If successful: productize to recurring compliance check (quarterly).

**Befektetés:** ~2-3 nap (Tomi + Leoni). Directly sellable, no infrastructure cost.

---

### #2: H62 - Agent Liability & Insurance Framework Research

**Miért most:** Az agent EIN szignál új kategóriát nyit. Insurance és legal advisory szervezetek még nem ebben az irányba mennek. Vannak innen intelligence wins és advisory upside.

**Kísérlet:** 1 héten: 5 Insurance/legal szervezet interjúja, agent liability kérdésről + Tomi-val joint whitepaper outline (arxiv/LinkedIn). Nem termék - research + positioning. Cél: "first mover" knowledge position, majd advisory gig opportunity.

**Mérés:** Interview receptivity, whitepaper citation/reach, inbound inquiry rate.

**Befektetés:** ~1 hét (Tomi + research partner). High visibility, thought leadership play.

---

### #3: H59 (refreshed) - Credential Broker JIT Token Demo (meglévő top 3 mellett)

**Miért most:** Kontext + Cred szignálok 2026-04-15 óta inaktívak voltak, de a 2026-05-06 report újra kiemeli az credential delegation-t mint "pain=5" taboo-feloldó wedge. Palo Alto Networks / Portkey acquisition (2026-05-03) validálja a market momentum.

**Kísérlet:** 3 napos POC: GitHub + DB + billing API-hoz JIT token delegation + audit trace + approval gate. Deliverable: 2 perces video + 1 oldalas evidence export. Pitch: "Your agents never touch long-lived keys."

**Mérés:** Demo request rate, security team objection count, deal size for JIT credentialing.

**Befektetés:** ~3 nap (Leoni feature + demo). Leverages existing Navibase/MCP infrastructure.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-05-06.md (562 releváns, top 30 elemezve, 8 emerging themes) + prior H history | 2026-05-06 07:30 UTC*

---

## H81 - Learned Decentralized Multi-Agent Task Allocation (CBBA + RL)
**Thesis:** A több agent rendszereknél az erőforrás-allokáció eddig hand-crafted greedy scoring alapján működött. Az új eredmény: learned RL bidding policies (centralized training, decentralized execution) jobbat talál, miközben decentralizált garanciákat tartalmaz. Ez nem csak robotika: bármely multi-agent workflow (parallel runs, resource pools, task delegation) tanulhat az agent-szintű allokációs mintázatokat, csökkentve a kézi scheduling frictiont.
**Signals (2026-05-23):**
- Auction-Consensus Algorithm with Learned Bidding Scheme for Multi-Robot Systems (arXiv, 2026-05-21, Deep Score 0.3): explicit learned bidding policy a CBBA-ban, multi-robot teams limited communication constraints alatt. https://arxiv.org/abs/2605.21932. HIGH CONFIDENCE.
**Assessment:** KKV-nál releváns, ha egynél több agent fut (task distribution, resource contention). Navibase: agent scheduling best practice és "autonomous orchestration" feature lehet a jövőben.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=3 | **Total: 14/25**
*Új hypothesis (2026-05-23). Az auction-consensus dengan learned bidding jól illeszkedik a H25 (workspace orchestration) irányba.*

## H82 - Multi-Agent Communication Security & Protocol Authentication (Agent-to-Agent Trust)
**Thesis:** Ahogy az agentek egymás között kommunikálnak (agent orchestration, delegation, approval workflows), új attack felület nyílik meg: domain-camouflaged injection, agent impersonation, policy bypass. A megoldás: protokoll-szintű authentication, attestation, és encrypted channels multi-agent rendszerekben. Ez H22/H24 (security) mélyebb szintje: nem client-facing injection, hanem inter-agent threat model.
**Signals (2026-05-23):**
- Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems (arXiv, 2026-05-22, Deep Score 0.1): multi-agent LLM communication bypass, injection elleni detektálás hiányzik. https://arxiv.org/abs/2605.22001. HIGH CONFIDENCE.
**Assessment:** Ez a H25/H33 szintjén: agent-to-agent message signing, capability attestation, és audit transcript. Navibase: multi-agent deployments (ha elkészül majd) safety critical feature.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=4 | **Total: 19/25**
*Új hypothesis (2026-05-23). A domain-camouflaged pattern azt jelzi, hogy az agent orchestration biztonsági rétegei még immatúr.*

## H83 - Provider-Specific Agentic Shifts in Model Capability & Commercial Terms
**Thesis:** Az eddigi model competition a "helpfulness" és az "accuracy" körül forgott. A 2026-05-19 Google bejelentés (Gemini 3.5 Flash agent-first) azt mutatja, hogy a major provider pivot agentic capability szétszóródása felé. Ennek üzleti következménye: minden provider saját "agentic optimization" profilt fog építeni, az API és pricing eltérően lesz strukturálva agentek számára. A blindspot: a KKV-nak nincs model selection framework agent use case-hez.
**Signals (2026-05-23):**
- With Gemini 3.5 Flash, Google bets its next AI wave on agents, not chatbots (TechCrunch, 2026-05-19, Deep Score 0.1): explicit provider shift agent-first irányba, model optimalizálás agent benchmark-okra. https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/. HIGH CONFIDENCE.
**Assessment:** Ez nem product wedge, hanem stratégiai kontextus: az agent selection framework (model + cost + capability profile) saját valuációs és procurement szint lesz. Navibase: "agent-ready model guide" tájékoztatás lehet az SMB számára.
**Scores:** Pain=3 | Urgency=3 | WTP=3 | Def=2 | IntFric=2 | **Total: 13/25**
*Új hypothesis (2026-05-23). A provider consolidáció körüli confusion gyors POC/advisory opportunity.*

## H84 - NVIDIA Verified Agent Skills Marketplace & Capability Standardization
**Thesis:** Az agentic capabilities (tools, APIs, datasets) eddig un-vetted, untrustworthy marketplace-en forogtak. Az NVIDIA Verified Agent Skills bejelentés jel: vendor-supported, auditable skill standard és marketplace formálódik. Ez a H50 (benchmark-driven procurement) kiegészítése: nem csak benchmark, hanem vendor-certified capability unit. Az SMB opportunity: either publish certified skills vagy use verified marketplace for compliance procurement.
**Signals (2026-05-23):**
- NVIDIA-Verified Agent Skills Provide Capability Governance for AI Agents (2026-05-19, Deep Score 0.1): vendor-verified capability standard, governance-first skill curation. https://news.google.com/rss/... HIGH CONFIDENCE.
**Assessment:** Ez H24/H42 szintjén: standard capability protocol + marketplace. Navibase: partner-stratégia vendor marketplacekel, vagy saját "SMB-certified skills" collection.
**Scores:** Pain=4 | Urgency=4 | WTP=4 | Def=3 | IntFric=3 | **Total: 18/25**
*Új hypothesis (2026-05-23). Az NVIDIA validator roles új governance primitive-t jelzi: capability certification.*

## H85 - Agentic Search & SEO/SEM Business Model Disruption (Discovery Paradigm Shift)
**Thesis:** A "Google Search as you know it is over" statement jel, hogy az agent-first discovery (conversational, autonomous research agent) egy új discovery kategóriává lép. Ez üzleti szintű: az SEO/SEM (keyword, ranking, paid placement) business model feloszlik, helyét az "agent-preferred sources" ranking és "agent-native prompting" veszi át. Az SMB szintjén: content strategy, customer acquisition, distribution fundamentálisan megváltozik, ha a search helyét agent-based discovery veszi át.
**Signals (2026-05-23):**
- Google Search as you know it is over (TechCrunch, 2026-05-19, Deep Score 0.1): shift from ranking to agentic discovery, conversational research, autonomous agent preference. https://techcrunch.com/2026/05/19/google-search-as-you-know-it-is-over. HIGH CONFIDENCE.
**Assessment:** Ez nem technikai governance kérdés, hanem szervezeti/üzleti: az SMB digitális stratégiáját átírja. Navibase: advisory/content strategy szint, nem az agent product szintje. De hosszú távon: az agent-friendly tudásstruktúrálása (structured data, API-first content, agent prompts) új készségi szint.
**Scores:** Pain=5 | Urgency=3 | WTP=3 | Def=3 | IntFric=4 | **Total: 18/25**
*Új hypothesis (2026-05-23). A discovery paradigm shift nem technikai, hanem piaci szintű disruption, de az SMB stratégiára közvetlenül hat.*

---

## Ranking Summary (2026-05-23)

| Rank | Hypothesis | Score | Delta |
|------|-----------|-------|-------|
| 1 | H2 - Audit Trail | 22/25 | = |
| 2 | H6 - Policy Enforcement Runtime | 22/25 | = |
| 3 | H1 - Agent Identity & Auth | 21/25 | = |
| 4 | H20 - Agent Orchestration as Regulated Infra | 21/25 | = |
| 5 | H3 - MCP Governance | 20/25 | = |
| 6 | H12 - Agent Accountability Framework | 20/25 | = |
| 7 | H10 - Agent Infra as Code | 19/25 | = |
| 8 | **H82 - Multi-Agent Communication Security** | **19/25** | **ÚJ** |
| 9 | H15 - B2B SaaS Agent Feature Injection | 19/25 | = |
| 10 | H7 - SMB Deployment Wrapper | 18/25 | = |
| 11 | H8 - Cross-Agent Context | 18/25 | = |
| 12 | H13 - Agent Sandboxing & Isolation | 18/25 | = |
| 13 | H14 - Agent-to-Agent Trust & M2M | 18/25 | = |
| 14 | H16 - AI Alignment Measurement as a Service | 18/25 | = |
| 15 | H17 - Controlled Self-Configuration Boundary | 18/25 | = |
| 16 | H18 - Organizationally-Aligned AI | 18/25 | = |
| 17 | H19 - Operational Reliability Layer | 18/25 | = |
| 18 | **H84 - NVIDIA Verified Agent Skills Marketplace** | **18/25** | **ÚJ** |
| 19 | **H85 - Agentic Search & Discovery Disruption** | **18/25** | **ÚJ** |
| 20 | H4 - Agent Payment Rails | 17/25 | = |
| 21 | H11 - Hallucination Self-Check | 17/25 | = |
| 22 | H5 - Discovery & Registry | 16/25 | = |
| 23 | **H81 - Learned Decentralized Task Allocation** | **14/25** | **ÚJ** |
| 24 | H9 - Agent Communication Infra | 12/25 | = |

*2026-05-23 delta: 5 új hypothesis (H81-H85). Governance infrastruktúra és compliance narratívák (H2/H6/H20) dominálja a top 5-öt. Az agent orchestration themed hypotheses (H14/H82) felértékelődnek, mivel a multi-agent deployment Wave beérkezik. Az urgency mindegyik új H-nél magas: az EU AI Act deadline Aug 2026, Google/NVIDIA player moves, és SEO/SEM disruption rövid időhorizontra van.*

---

## Top 3 Opportunities + Suggested Experiments (2026-05-23)

### #1: H20 - Agent Orchestration Platform as Regulated Infrastructure [Score: 21/25]
**Miért most:** EU AI Act Aug 2026 deadline 2.5 hónapon belül. Az "agent platform infrastruktúra" narratíva mainstream médiában jelent meg (National Today, 2026-03-29). A Navibase/Leoni már implementálja az audit trail, policy engine, identity scope komponenseket - most kommunikálnia kell ezt együtt, mint "EU AI Act-ready compliance platform."
**Javasolt kísérlet:** 15 EU-based AI governance officer (compliance, legal) hideg megkeresés. Ajánlat: "Agent Platform EU AI Act Readiness Audit" - 2 hetes szabad audit, checklist, remediation roadmap. Mérők: audit→paid advisory konverzió, enterprise inbound pipeline.
**Befektetés:** ~1 hét audit sablon + sales outreach. High-touch, de szoros compliance szükségletre épít.

### #2: H82 - Multi-Agent Communication Security [Score: 19/25 - ÚJ]
**Miért most:** A domain-camouflaged injection attack 2026-05-22 jelent meg - az inter-agent messaging biztonsági réteg ma unresolved. Ahogy a multi-agent pipeline-ok production-ba kerülnek (Nyne, orchestration wave), ez az attack felület élő lesz. Navibase: agent-to-agent message signing + capability attestation MVP.
**Javasolt kísérlet:** 2 nap research: domain-camouflaged attack anatomy vizsgálata. 3 nap MVP: agent-to-agent message signing + audit transcript. Deliverable: security white paper + PoC demo.
**Befektetés:** ~5 nap. Thought leadership + Product feature roadmap.

### #3: H84/H85 (szinkronban) - NVIDIA Skills Marketplace + Search Disruption [Score: 18/25 - ÚJ]
**Miért most:** NVIDIA vendor-standardizációja és Google Search dismantling egyszerre jelent meg - ezek az agent ecosystem fő pilléreinek dekonstrukcióját jelzik. Az SMB-nek szüksége van egy navigációs útmutató: "melyik marketplace-en kell prezentálnom az agent capable-et, és hogyan kell alkalmazkodnom a discovery paradigma eltolódásához."
**Javasolt kísérlet:** 1 napos advisory brief: NVIDIA Verified Skills eligibility + Google agentic search content strategy. Deliverable: 1 oldalas "Agent Marketplace Positioning Guide" SMB számára.
**Befektetés:** ~1 nap research. Quick advisory wedge, ezt követően workshop-pilot.

---

*Frissítette: Leoni Ops Agent | Signals forrás: blindspot-signals-2026-05-23.md (736 signal, HAIER export) | 2026-05-23 09:30 CET*
