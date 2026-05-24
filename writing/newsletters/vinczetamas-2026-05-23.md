# Vinczetamas Newsletter — 2026-05-23

## Subject
"Agentek terminálban — hogyan építik a Google és az xAI 2026-ban?"

## Preview
Grok Build, Genkit, Sentry Seer. Az agent framework trend. Mire vigyázz, ha saját agentet építesz?

---

## 📈 Trend: Terminal-First Agent Frameworks (2026)

Az AI agent infrastruktúra 2025-ben webből indult (Discord, Slack botok), 2026-ban viszont **terminálba költözik**.

**Miért?** Mert a dev toolok már ott vannak. A kód. Az infrastructure. Az obsessing. Pont azt csinálja az agent, amit egy developer is: nézi a repo-t, módosítja a fájlokat, futtat parancsokat.

Az xAI **Grok Build**, Google **Genkit**, Sentry **Seer Agent** — mind azt mondják: agent IDE legyen, ne messenger bot.

---

## 🔴 Tanulságok & 3 Lépés

### 1. **Sandbox = Trust Boundary**
Ha multi-agent renderesz (mik az OpenClaw subagents-ek), minden agent stateless kell legyen. Nem szabad memória között információ — se jelszavak, se konfig. Az agent egy docker konténer: spinnelni, kilni, szkalázni. Pont.

**Lépés:** Auditáld az OpenClaw agent izolációt. Van-e context leakage?

### 2. **Hooks > Direct Calls**
Genkit pattern: composable middleware. Ne a végpontot csatornázz, hanem a loop-ot.

Gyakorlat: ha most N integráció van (GitHub, Slack, Gmail), egy új tool hozzáadása = N+1 pont módosítás. Hooks-cal: egy pont.

**Lépés:** Refactor: GenKit-szerű middleware layer az OpenClaw felé.

### 3. **Observability szint = Agent szint**
Sentry Seer: az agent miért lassú? Miért rossz döntést hozott? Miért bugos az integráció? Te is tudnod kell azt válaszolni.

**Lépés:** Minden agent run = trace. Trace = inspect. Inspect = tanulás.

---

## 🎯 CTA

Szükséged van egy **agent OS**, nem ügyfélalkalmazásra.

Tudj meg többet: **[vinczetamas.hu/audit](https://vinczetamas.hu/audit)**

---

**Nap:** 2026-05-23  
**Forrás:** TLDR AI, Superhuman, Ben's Bites  
**Status:** DRAFT — Tomi review szükséges
