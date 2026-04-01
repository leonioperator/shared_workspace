# Agent Platform Blindspot Radar — 2026-03-31

**Forrás:** HAIER evolution_signals_20260331_020451.json  
**Szűrés:** focus_area = 'AI agents' | 'AI decision delegation'  
**Releváns signalok száma:** 217  
**Elemzett signalok:** 30 (legfrissebb)

---

## Top 5-10 legerősebb signal

### 1. KRITIKUS — Accountability vacuum: ki felel az autonóm agentekért?
**"iProov warns of 'accountability vacuum' with rise of autonomous AI agents"**  
*Biometric Update, 2026-03-26*  
**URL:** https://news.google.com/rss/articles/CBMirwFBVV95cUxNZXpkTkQx...  
**Bizonyíték:** Az iProov (identity verification cég) nyíltan figyelmeztet: ahogy az AI agentek egyre több döntést hoznak önállóan, nincs egyértelmű felelősségi lánc. Ki áll jót egy agent döntéséért? A cég szerint ez "accountability vacuum" — különösen veszélyes pénzügyi, jogi, HR kontextusban. **Blindspot: a Navibase agent-as-a-service modellnél a klienssel kötött SLA-ban ezt explicit kezelni kell.**

---

### 2. KRITIKUS — AI agentek mint governance infrastruktúra
**"AI Agents Become Governance Infrastructure, Raising Concerns Over Control"**  
*National Today, 2026-03-29*  
**URL:** https://news.google.com/rss/articles/CBMiywFBVV95cUxQWXgwUVBGMXVM...  
**Bizonyíték:** Az AI agentek már nem csak eszközök — governance infrastruktúrává válnak (döntéshozatal, compliance, policy enforcement). Ez kontroll-kockázatot jelent: ha az agent rosszul van konfigurálva, az egész szervezeti döntéshozatal megbicsaklik. **Blindspot: Leoni policy engine fejlesztése nem opcionális — ez versenyelőny lesz.**

---

### 3. AKADÉMIAI ALAP — Revealed preference framework az AI alignment-hez
**"A Revealed Preference Framework for AI Alignment"**  
*arXiv 2603.27868, 2026-03-29*  
**URL:** https://arxiv.org/abs/2603.27868v1  
**Bizonyíték:** Az emberi döntéshozók egyre inkább delegálnak AI agenteknek. A cikk bevezeti a "Luce Alignment Model"-t: az agent döntései az emberi preferenciák és a saját preferenciák keveréke. Azonosítható, mikor tér el az agent a gazda szándékától. **Blindspot: a delegáció mértékének mérhetővé tétele — ezt a KKV ügyfelek fogják kérni.**

---

### 4. BIZTONSÁGI KOCKÁZAT — Agent önmódosítás (config rewrite saját VM-en)
**"Show HN: Phantom – Open-source AI agent on its own VM that rewrites its config"**  
*GitHub ghostwright/phantom, 2026-03-30*  
**URL:** https://github.com/ghostwright/phantom  
**Bizonyíték:** Nyílt forráskódú agent, amely saját VM-en fut és képes újraírni a saját konfigurációját. Ez az önmódosítás képessége kritikus biztonsági kérdéseket vet fel: hol a határvonal az adaptív viselkedés és a kontroll elvesztése között? **Blindspot: az OpenClaw/Leoni architektúrában az önkonfiguráció expliciten scope-olva van — ezt kommunikálni kell a kliensek felé mint differenciálót.**

---

### 5. PIACI SIGNAL — $65M seed enterprise AI agent startupra
**"Former Coatue partner raises huge $65M seed for enterprise AI agent startup"**  
*TechCrunch, 2026-03-30*  
**URL:** https://techcrunch.com/2026/03/30/former-coatue-partner-raises-huge-65m-seed-for-enterprise-ai-agent-startup/  
**Bizonyíték:** Elképesztő mértékű early-stage tőkebevonás enterprise AI agent területen. A befektetők ezt a szegmenst a következő nagy hullámnak látják. **Blindspot: a KKV szegmens (Navibase célpiaca) alulinvesztált ebben a hullámban — ez ablak a gyors piacra lépésre mielőtt az enterprise megoldások lecsorognak.**

---

### 6. GOVERNANCE INFRA — Orloj: agent policy enforcement runtime gate-ként
**"Show HN: Orloj – agent infrastructure as code (YAML and GitOps)"**  
*GitHub OrlojHQ/orloj, 2026-03-26*  
**URL:** https://github.com/OrlojHQ/orloj  
**Bizonyíték:** Az Orloj minden agent turn és tool call előtt inline policy-t értékel ki — nem prompt utasításként, hanem runtime gate-ként. "Unauthorized actions fail closed with structured errors and full audit trails." Ez pontosan a Leoni policy engine megközelítése. **Bizonyíték, hogy ez az irány helyes — és hogy az open-source vetélytársak is itt építenek.**

---

### 7. EMBEDDING VALUES — Társadalmi értékek az AI döntésekbe
**"Embedding social values into AI decisions"**  
*EurekAlert!, 2026-03-27*  
**URL:** https://news.google.com/rss/articles/CBMiXEFVX3lxTE55eDI5TXFOLUUz...  
**Bizonyíték:** Tudományos kutatás arról, hogyan lehet szervezeti/társadalmi értékeket beágyazni AI döntési folyamatokba. **Blindspot: a KKV kliensek saját értékrendjét (pl. "ne ajánlj fel semmit az ügyfélnek ha bizonytalan a szükséglet") hogyan kódoljuk az agentbe? Ez a következő roadmap elem.**

---

### 8. MULTI-AGENT KOORDINÁCIÓ TÖRÉKENY
**"CRAFT: Grounded Multi-Agent Coordination Under Partial Information"**  
*arXiv 2603.25268, 2026-03-26*  
**URL:** https://arxiv.org/abs/2603.25268v1  
**Bizonyíték:** A kutatás megmutatja: erősebb reasoning képesség NEM jelent jobb multi-agent koordinációt. Kisebb open-weight modellek néha felülmúlják a frontier rendszereket. "Multi-agent coordination remains a fundamentally unsolved challenge." **Blindspot: a Navibase multi-agent roadmapnál a koordinációs protokoll fontosabb, mint a modell ereje.**

---

### 9. ENTERPRISE ADOPTION GYORSUL
**"Autonomous AI agents in business organizations"**  
*Jerusalem Post, 2026-03-27*  
**URL:** https://news.google.com/rss/articles/CBMiXEFVX3lxTFBBLUJRVDhqUkc2dEVB...  
**Bizonyíték:** Mainstream üzleti sajtóban jelenik meg az autonóm AI agent mint standard KKV eszköz. A narratíva átváltott: nem "lesz-e belőle valami" hanem "hogyan vezessük be". **Blindspot: a Navibase pilot klienseknek most kell onboardolni — a window of differentiation szűkül.**

---

### 10. AGENT TOOLING ÖKOSZISZTÉMA ROBBAN
**"Universal CLI by Composio — Connect AI agents to 1000+ apps"**  
*ProductHunt, 2026-03-27*  
**URL:** https://www.producthunt.com/products/composio  
**Bizonyíték:** Az agent tooling layer (integráció, orchestráció, MCP) gyorsan commoditizálódik. **Blindspot: a Leoni/Navibase versenyelőny nem az integráció mélységéből jön, hanem az operatív megbízhatóságból és a KKV-specifikus workflow tudásból.**

---

## Összefoglaló: fő blindspot témák

| Téma | Urgencia | Navibase relevancia |
|------|----------|---------------------|
| Accountability vacuum (ki felel?) | KRITIKUS | SLA design, kliens onboarding |
| Agent governance infra | KRITIKUS | Policy engine fejlesztés |
| AI alignment mérhetősége | MAGAS | Kliens bizalom építés |
| Önmódosítás kockázata | MAGAS | Leoni scope-olás dokumentálása |
| Multi-agent koordináció törékeny | KÖZEPES | Roadmap prioritás |
| Social values embedding | KÖZEPES | KKV testreszabás |
| Market window szűkül | MAGAS | Pilot kliens gyorsítás |

---

*Generálva: 2026-03-31 21:43 CET | HAIER export: evolution_signals_20260331_020451.json | 217 releváns signal / 30 elemzett*
