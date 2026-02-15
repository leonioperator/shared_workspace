# dn-dev-02 Audit Review & Fejlesztési Terv

**Készítette:** Leoni (dn-optigen-01)
**Dátum:** 2026-02-15
**Forrás:** Claude Sonnet 4.5 rendszer audit (2026-02-13)
**Célrendszer:** dn-dev-02 (46.224.176.95) — Navibase/OpenClaw stack

---

## 1. Összefoglaló

A Navibase stack **működőképes állapotban van** (~70% implementáltsági szint). Az alap architektúra (OpenClaw gateway + 10 custom skill + Mission Control UI + SQLite perzisztencia) jól működik. Három területen van kritikus teendő: **biztonság, deployment automation, és kommunikáció (Telegram).**

### ✅ Ami működik
- OpenClaw gateway (Főnök agent, GPT-5.1-codex)
- 10 custom skill (budget, audit, approval, metrics, kanban, health, summary, mission_control, ers, reh)
- 4 SQLite adatbázis (approval_gate, audit_log, budget_state, token_usage_offsets)
- Mission Control dashboard (real-time WebSocket, vanilla JS, Caddy)
- Snapshot writer (10 mp-es frissítés)
- Docker Compose deployment (3 konténer + Kanban + ClawGuard)
- Kiváló dokumentáció (13 fájl)

### ❌ Ami nem működik / hiányzik
- Telegram notifications (konfig van, token üres)
- Deploy script (dokumentáció kész, kód nincs)
- Backup/rollback rendszer (nincs)
- Cloudflare Tunnel (dev-ben OK, prod-ban kell)
- GDPR deletion script
- Email értesítések

### 🔴 Kritikus problémák
1. **OpenClaw dev gateway PUBLIKUSAN elérhető** (0.0.0.0:18789) — azonnali javítás!
2. **API kulcsok plaintext** az .env fájlokban
3. **Duplikált architektúra** (dev + navibase instance párhuzamosan fut)

---

## 2. Biztonsági értékelés

| Probléma | Súlyosság | Megoldás |
|---|---|---|
| Dev gateway publikus (0.0.0.0:18789) | 🔴 CRITICAL | `.env`: `OPENCLAW_GATEWAY_HOST=127.0.0.1` |
| API key plaintext | 🟠 HIGH | Dev-ben elfogadható, prod-ban secrets manager kell |
| Gateway token plaintext | 🟡 MEDIUM | Ugyanaz mint fent |
| Nincs key rotation | 🟡 MEDIUM | 90 napos rotation policy implementálás |

**Pozitív:** Navibase stack (28789), Mission Control (28080), Kanban (3180), ClawGuard (3847) mind loopback-only. Konténerek nem root-ként futnak. Host mountok read-only.

---

## 3. Architektúra drift

Három fő eltérés a tervezett architektúrától:

1. **Kanban külön Docker service** (az architektúra szerint skill-ben kellene)
2. **Snapshot writer külön konténer** (nem volt specifikálva)
3. **ClawGuard monitoring** (nem tervezett, de hasznos)

Ezek nem kritikusak, de döntést igényelnek: elfogadjuk őket az architektúrába, vagy integráljuk vissza.

---

## 4. Priorizált fejlesztési terv

### 🔴 Fázis 1: Kritikus javítások (1-3 nap)

| # | Feladat | Részletek |
|---|---|---|
| 1.1 | **Dev gateway lezárása** | `OPENCLAW_GATEWAY_HOST=127.0.0.1` az `/opt/openclaw/.env`-ben, konténer restart |
| 1.2 | **backup.sh script** | SQLite dump + tar.gz, napi cron, legalább 7 nap retention |
| 1.3 | **deploy.sh script** | Idempotens, backup ellenőrzéssel, a meglévő DEPLOY.md alapján |

### 🟠 Fázis 2: Kommunikáció (1 hét)

| # | Feladat | Részletek |
|---|---|---|
| 2.1 | **Telegram bot token beállítás** | `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` kitöltése a Kanban service-ben |
| 2.2 | **Napi összefoglaló (Telegram)** | snapshot.json alapján, a TELEGRAM_SUMMARY.md dokumentáció szerint |
| 2.3 | **Heti executive summary küldés** | Az executive_summary skill outputját Telegram/email-be kötni |
| 2.4 | **Approval gate → Telegram** | Jóváhagyási kérések push notification-je |

### 🟡 Fázis 3: Architektúra tisztítás (2 hét)

| # | Feladat | Részletek |
|---|---|---|
| 3.1 | **Kanban döntés** | Külön service marad VAGY skill-be integráljuk — döntés kell Tomitól |
| 3.2 | **Dev stack rendezés** | Dev gateway leállítása ha nem kell, vagy tiszta szeparáció dokumentálása |
| 3.3 | **ClawGuard dokumentálás** | Beírni az architektúra dokumentumba, célja és használata |
| 3.4 | **GDPR deletion script** | Article 17 compliance — script ami törli az adott user adatait |
| 3.5 | **.db fájlok jogosultság** | `chmod 600` az összes SQLite fájlra |

### 🟢 Fázis 4: Későbbi (production-höz)

| # | Feladat |
|---|---|
| 4.1 | Cloudflare Tunnel setup |
| 4.2 | Secrets manager (Vault / encrypted .env) |
| 4.3 | Key rotation automatizálás |
| 4.4 | Postgres migration path (ha 10+ tenant) |

---

## 5. Audit minősítések (az audit alapján)

| Szempont | Érték | Megjegyzés |
|---|---|---|
| Implementáltsági arány | 7/10 | Core kész, deployment automation hiányzik |
| Architektúra drift | 6/10 | Jelentős eltérések, de indokoltak |
| Biztonság | 5/10 | Dev gateway publikus! Egyébként jó gyakorlatok |
| Dokumentáció | 8/10 | Kiváló, 13 fájl, de néhány nincs implementálva |
| Production readiness | 4/10 | Dev environment, nem production ready |

---

## 6. Javaslat Tominak

### Azonnali teendő (ma/holnap):
> **A dev gateway publikus port-ját AZONNAL le kell zárni.** Ez a legkritikusabb biztonsági kockázat. Egy sor módosítás az `.env` fájlban + konténer restart.

### Döntést igénylő kérdések:
1. **Kanban:** Külön service marad vagy skill-be integráljuk?
2. **Dev stack:** Kell-e egyáltalán a dev gateway (/opt/openclaw), vagy elég a navibase-oc?
3. **Telegram bot:** Melyik bottól menjenek az értesítések? (Leoni botja vagy külön Navibase bot?)
4. **Fázis 2-3 prioritás:** Ki csinálja? Főnök agent (dn-dev-02) vagy Leoni (dn-optigen-01) távoli hozzáféréssel?

### Leoni szerepe:
Én (Leoni, dn-optigen-01) tudok segíteni:
- Deploy/backup scriptek megírásában (átadás shared_workspace-en keresztül)
- Dokumentáció review-ban
- Monitoring/alerting tervezésben (ClawGuard tapasztalat)
- A két VPS közötti koordinációban

---

*Ez a dokumentum a 2026-02-13-as Claude audit alapján készült. Az audit scope: /opt könyvtár, dn-dev-02.*
