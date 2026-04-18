# OpenClaw Agent fejlesztési terv – Teljes bookmark elemzés

## Célok

- **A:** KKV (kis- és középvállalkozás) automatizáció
- **B:** Agentic code fejlesztések
- **C:** Forex MT4/MT5 automata trading robot – forex tanfolyami videókból kinyert stratégiák alapján

---

## Az összes "Agents" bookmark elemzése

| # | Repo / URL | Mit csinál | A | B | C | Komp. | Aktív? | Javaslat |
|---|-----------|-----------|:--:|:--:|:--:|-------|:------:|----------|
| 1 | `besoeasy/open-skills` | 39 kész skill, 95-98% token megtakarítás, nem kell trial-and-error | 4 | 5 | 4 | Alacsony | ✅ | **TELEPÍTENI 1.** |
| 2 | `EmpusaAI` | API error-loop védelem, cost tracking dashboard, reset + recovery | 4 | 4 | 5 | Alacsony | ✅ | **TELEPÍTENI 2.** |
| 3 | `coolmanns/openclaw-memory-architecture` | 4 rétegű memória (SQLite+FTS5, szemantikus keresés, facts DB) v2.4 | 4 | 5 | 3 | Közepes | ✅ | **TELEPÍTENI 3.** |
| 4 | `avisual/memories-plugin` | Hebbian memória, terjedő aktiváció, ingyenes Mem0-alternatíva | 4 | 5 | 3 | Közepes | ✅ | **TELEPÍTENI 4.** |
| 5 | `Lior-Leonetwork/LLM-MicroAgents` | Izolált sub-agentek feladatonként, 78% token csökkentés | 4 | 4 | 3 | Alacsony | ✅ | **TELEPÍTENI 5.** |
| 6 | `shadow-mcp/shadow-mcp` | Staging env: Gmail/Slack/Stripe szimulálás, prompt injection, PII detektálás | 3 | 5 | 5 | Közepes | ✅ | **TELEPÍTENI 6. (KRITIKUS trading-hoz!)** |
| 7 | `openclaw-trade/openclaw-trading-assistant` | Crypto trading bot, Hyperliquid API, sentiment, risk mgmt, human-in-loop | 2 | 3 | 4 | Magas | ✅ | **REFERENCIA** – forex-ra adaptálni |
| 8 | `caprihan/openclaw-n8n-stack` | OpenClaw + n8n Docker Compose, 400+ integráció | 4 | 5 | 2 | Alacsony | ✅ | **OPCIONÁLIS** – ha KKV workflow kell |
| 9 | `freddy-schuetz/n8n-claw` | n8n-alapú agent, RAG memória, MCP skills, Telegram, proaktív feladat | 4 | 5 | 2 | Alacsony | ✅ | **OPCIONÁLIS** – n8n alternatíva |
| 10 | `karmaniverous/n8n-nodes-openclaw` | 20 n8n node az OpenClaw Gateway API-hoz | 4 | 5 | 2 | Alacsony | ✅ | **OPCIONÁLIS** – ha n8n-t használsz |
| 11 | `JIGGAI/ClawRecipes` | 1 paranccsal agent csapatot indít, fájl-alapú workflow | 3 | 4 | 2 | Közepes | ✅ | **OPCIONÁLIS** |
| 12 | `BlockRunAI/ClawRouter` | 41+ modell közötti okos routing, 92% megtakarítás | 4 | 5 | 3 | Nagyon alacsony | ✅ | **⏸️ HALASZTVA** (USDC wallet kell) |
| 13 | `luckyPipewrench/pipelock` | DLP, SSRF, prompt injection, 9 rétegű security scan | 3 | 5 | 3 | Alacsony | ✅ | **OPCIONÁLIS** – production biztonsági réteg |
| 14 | `SeyZ/clawbands` | Human-in-the-loop: ASK/ALLOW/DENY policy, audit log | 3 | 4 | 2 | Alacsony | ✅ | **OPCIONÁLIS** |
| 15 | `youngkent/clawtime` | Chat UI 3D avatarral, voice, WebAuthn, E2E titkosítás | 3 | 4 | 2 | Közepes | ✅ | **OPCIONÁLIS** – UI fejlesztéshez |
| 16 | `freakyflow/garminskill` | Garmin Connect egészségadatok → markdown napi összefoglaló | 2 | 3 | 2 | Alacsony | ✅ | **OPCIONÁLIS** – ha van Garmin |
| 17 | `adridder/moltron` | Önfejlesztő agent, SmythOS dependency, 49 csillag | 2 | 2 | 1 | Alacsony | Részben | ❌ SKIP – SmythOS függőség |
| 18 | `ainakwalamonk/durableclaw` | Mastra+Trigger.dev pipeline, 1 commit | 1 | 2 | 1 | Magas | ❌ | ❌ SKIP – elhagyott |
| 19 | `linuxhsj/realtime-translate` | Valós idejű audio fordítás, NVIDIA Riva, 10 nyelv | 2 | 2 | 1 | Magas | ✅ | ❌ SKIP – nem releváns |
| 20 | `own-ai/own-ai` | AI asszisztens platform | — | — | — | — | ❌ | ❌ SKIP – deprecated |
| 21 | `voxyz.space` | 1 ember + 5 AI agent cég: Nexus, Scout, Quill, Forge, Guide | 5 | 4 | 1 | — | ✅ | 📖 REFERENCIA – business model |
| 22 | `madebynathan.com` blog | Valós OpenClaw használati esetek: K8s, Git, email, CI/CD | 5 | 5 | 3 | — | — | 📖 OLVASNI |
| 23 | `openclaw/openclaw #26110` | Feature request: macOS-in-Docker Linux/Windows-on | — | — | — | — | — | 👀 FIGYELNI |
| 24 | `openclaw-trade/x.com post` | "Mission Control: AI Agent Squad" útmutató | 3 | 4 | 3 | — | — | 📖 OLVASNI |

---

## Telepítési terv – Prioritás szerint

### Előfeltétel ellenőrzés (szerveren)

```bash
ssh root@dn-platform-01
su - leoni
openclaw --version
openclaw plugins list
node --version       # kell: ≥18
sqlite3 --version    # kell: FTS5-tel
docker --version
```

---

### PRIORITÁS 1 — `besoeasy/open-skills` (5 perc, AZONNALI)

**Miért:** 39 battle-tested skill egyből csökkenti a trial-and-error API hívásokat – $0.15 → $0.003/feladat. Legjobb ROI, nulla kockázat.

```bash
git clone https://github.com/besoeasy/open-skills ~/open-skills
# System prompt végéhez fűzni az openclaw.json-ban:
cat ~/open-skills/prompt.txt
# → ~/.openclaw/openclaw.json "systemPrompt" mezőjébe illeszteni
```

**Forex relevancia:** Web search, PDF parse, data fetch skilleket azonnal használja a strategy-kinyerő pipeline.

---

### PRIORITÁS 2 — `EmpusaAI` (10 perc)

**Miért:** Trading bot-hoz KRITIKUS – megakadályozza az API error loop-okat (pl. MT4/MT5 kapcsolat elvesztésekor ne pörögjön drága API hívásokba). Cost tracking dashboard.

```bash
git clone https://github.com/justin55afdfdsf5ds45f4ds5f45ds4/EmpusaAI ~/empusa
cd ~/empusa && ./install.sh
# OpenClaw API proxy-n keresztül → openclaw.json endpoint frissítése
```

**Forex relevancia:** Ha a Metatrader bridge/kapcsolat megszakad, EmpusaAI leállítja a loop-ot és alertet küld.

---

### PRIORITÁS 3 — `coolmanns/openclaw-memory-architecture` (30-45 perc)

**Miért:** Tartós memória a stratégiákhoz, kereskedési mintákhoz, user preferenciákhoz. SQLite+FTS5 (lokális, nincs külső API). v2.4, aktívan fejlesztett.

```bash
git clone https://github.com/coolmanns/openclaw-memory-architecture ~/openclaw-mem
docker run -d --name nomic-embed -p 8080:8080 nomic-ai/nomic-embed-text-v2-moe
cp -r ~/openclaw-mem/plugins/* ~/.openclaw/extensions/
# ~/.openclaw/openclaw.json: slots.contextEngine = LCM
```

**⚠️ Nyitott feladat:** LCM secrets scrubbing (trading API kulcsok ne kerüljenek a memory-ba).

---

### PRIORITÁS 4 — `avisual/memories-plugin` (20 perc)

**Miért:** Hebbian-jellegű asszociatív memória – a trading stratégiák közti kapcsolatokat tanulja meg. Ingyenes Mem0-alternatíva, nincs külső API.

```bash
git clone https://github.com/avisual/memories-plugin ~/.openclaw/extensions/memories-plugin
# Plugin regisztrálása az openclaw.json extensions listájában
```

**Megjegyzés:** Komplementer a memory-architecture-vel (az asszociatív + a strukturált).

---

### PRIORITÁS 5 — `Lior-Leonetwork/LLM-MicroAgents` (15 perc)

**Miért:** 78% token csökkentés – a trading pipeline-ban (news fetch, strategy calc, order gen) minden lépés külön mini-agentként fut, nem halmozódik a context.

```bash
git clone https://github.com/Lior-Leonetwork/LLM-MicroAgents ~/micro-agents
# OpenClaw skill-ként regisztrálni
```

**Forex relevancia:** Párhuzamos adat-feldolgozás (több devizapár egyszerre) alacsony tokenköltséggel.

---

### PRIORITÁS 6 — `shadow-mcp/shadow-mcp` (20 perc) — ⚠️ TRADING ELŐTT KÖTELEZŐ

**Miért:** Trading robot teszteléséhez KRITIKUS. Szimulált broker API, prompt injection detektálás, PII szivárgás ellenőrzés. Élő kereskedés előtt minden módosítást itt kell tesztelni.

```bash
# MCP-ként telepíteni az ~/.openclaw/mcp.json-ba:
{
  "mcpServers": {
    "shadow": {
      "command": "npx",
      "args": ["-y", "shadow-mcp"]
    }
  }
}
```

---

### TRADING ROBOT FEJLESZTÉSI ÚT

A forex MT4/MT5 trading robot építéséhez javasolt pipeline (az `openclaw-trading-assistant` crypto logikáját adaptálva):

```
1. Videóanyag → strategy kinyerés
   - besoeasy/open-skills PDF/video skill
   - memories-plugin tárolja a stratégiákat

2. Strategy → kód generálás (MQL4/MQL5)
   - OpenClaw agent generálja a robot kódot
   - LLM-MicroAgents: külön agent a signal logikának, a risk mgmt-nek, az order kezelésnek

3. Backtesting + validáció
   - shadow-mcp: broker szimulálás
   - EmpusaAI: védi az API hívásokat

4. Live trading
   - MT4/MT5 bridge (pl. EA Bridge, MT4-Python connector)
   - EmpusaAI: error protection élesben
```

---

### OPCIONÁLIS – n8n integráció (KKV automatizáció)

Ha a KKV automatizáció a legfontosabb:

```bash
# Legegyszerűbb: caprihan/openclaw-n8n-stack
git clone https://github.com/caprihan/openclaw-n8n-stack ~/openclaw-n8n
cd ~/openclaw-n8n && docker-compose up -d
# → OpenClaw + n8n egyben, 400+ integráció azonnal
```

---

### HALASZTVA — `BlockRunAI/ClawRouter`

Ha USDC wallet elérhető: 2 perces telepítés, 92% megtakarítás. Eco tier modellekkel a routine feladatok (adatbányászat, report gen) szinte ingyen futnak.

---

## Összefoglaló – Telepítési sorrend

| Sorrend | Repo | Idő | Legfontosabb célhoz |
|---------|------|-----|-------------------|
| 1. | `besoeasy/open-skills` | 5 perc | B + C |
| 2. | `EmpusaAI` | 10 perc | C (trading kritikus) |
| 3. | `openclaw-memory-architecture` | 45 perc | A + B + C |
| 4. | `avisual/memories-plugin` | 20 perc | A + B |
| 5. | `Lior-Leonetwork/LLM-MicroAgents` | 15 perc | A + B + C |
| 6. | `shadow-mcp/shadow-mcp` | 20 perc | B + C (KÖTELEZŐ trading előtt) |
| opt. | `caprihan/openclaw-n8n-stack` | 10 perc | A |
| ⏸️ | `BlockRunAI/ClawRouter` | 2 perc | A + B + C |
