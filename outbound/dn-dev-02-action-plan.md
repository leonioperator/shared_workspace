# dn-dev-02 (46.224.176.95) — Akcióterv

**Készült:** 2026-02-15
**Alapja:** Claude Sonnet 4.5 rendszer audit (2026-02-13)
**Készítette:** Leoni (dn-leoni-01 agent)

---

## 1. Mi az aktuális helyzet a dn-dev-02 szerveren?

A dn-dev-02-n egy **félig kész, de működőképes** Navibase/OpenClaw stack fut. Ez egy executive operations rendszer, ahol egy "Főnök" nevű AI agent custom skillekkel dolgozik (budget tracking, audit log, approval gate, metrics, stb.).

### Ami működik:
- **OpenClaw gateway** (navibase-oc instance, 127.0.0.1:28789) — 1 agent, GPT-5.1-codex modellel
- **10 custom skill** — budget_tracker, audit_log, approval_gate, metrics_engine, kanban_state, health_state, executive_summary, mission_control, ers_calc, reh_calc
- **4 SQLite adatbázis** — approval_gate.db, audit_log.db, budget_state.db, token_usage_offsets.db
- **Mission Control dashboard** — vanilla JS, Caddy-n futó real-time WebSocket dashboard (127.0.0.1:28080)
- **Snapshot Writer** — Python konténer, 10 másodpercenként aggregálja a DB-ket → snapshot.json
- **Kanban service** — külön Docker konténer (127.0.0.1:3180)
- **ClawGuard monitoring** — Node.js alapú (127.0.0.1:3847)
- **Docker Compose deployment** — összesen 6 konténer fut

### Ami hiányzik:
- Cloudflare Tunnel (nincs publikus hozzáférés)
- deploy.sh, backup.sh szkriptek (doku van, kód nincs)
- Telegram értesítések (konfig üres)
- Email értesítések
- Secrets rotation

### Számok:
- Implementálási arány: **7/10**
- Security posture: **5/10**
- Production readiness: **4/10**
- Dokumentáció minőség: **8/10** (13 fájl a docs/ mappában)

---

## 2. Milyen problémák vannak?

### 🔴 KRITIKUS — azonnali beavatkozás kell

1. **Dev gateway PUBLIKUSAN elérhető (0.0.0.0:18789-18790)**
   - Az `openclaw-openclaw-gateway-1` konténer az internetre néz
   - Token auth van, de ez önmagában nem elég
   - **Fix:** `.env` → `OPENCLAW_GATEWAY_HOST=127.0.0.1`, konténer restart

2. **API kulcsok plaintext az .env fájlokban**
   - OpenAI API key, gateway token mind plaintext
   - Dev-ben elfogadható, de ha publikus a gateway → közvetlen kockázat

3. **Nincs backup rendszer**
   - 4 SQLite DB, semmi automatikus mentés
   - Egy disk hiba = teljes adatvesztés

### 🟠 KÖZEPES — architekturális zavar

4. **Duplikált architektúra**
   - Két OpenClaw instance fut: dev (`/opt/openclaw`) + navibase (`/opt/navibase-oc`)
   - Dupla karbantartás, zavaros, melyik mit csinál

5. **Kanban külön service vs. skill**
   - Az architektúra szerint skill-ben kellene lennie
   - Ehelyett külön Docker konténer fut → sync problémák, `kanban_state.db` hiányzik

6. **ClawGuard nem dokumentált**
   - Nem szerepelt a tervezett architektúrában
   - Valószínűleg debug/monitoring célra lett hozzáadva, de nincs leírva miért/hogyan

### 🟡 ALACSONY — hiányzó funkciók

7. **Telegram bot nincs bekötve** (token üres)
8. **Deploy script nincs** (DEPLOY.md létezik, de script nem)
9. **GDPR törlési script nincs**

### 🧠 "Mentális zavar" — mi történhetett

Az audit alapján a fejlesztés **iteratív volt, de az iterációk nem lettek takarítva**:
- A dev stack (`/opt/openclaw`) maradt futva, miközben a navibase stack (`/opt/navibase-oc`) lett a "production"
- A Kanban és a ClawGuard ad-hoc lett hozzáadva, nem az eredeti terv szerint
- A dokumentáció megelőzte az implementációt (ami jó szándék, de hamis biztonságérzetet ad)
- Összességében: **a rendszer közelebb van a célhoz, mint amennyire kaotikusnak tűnik**

---

## 3. Szükséges-e újraépítés, vagy javítható?

### Válasz: **JAVÍTHATÓ.** Nem kell újraépíteni.

Az alaparchitektúra helyes és működik. A problémák többsége konfigurációs vagy hiányzó automatizáció. Konkrétan:

| Probléma | Megoldás típusa | Becsült idő |
|---|---|---|
| Publikus gateway | Config fix | 5 perc |
| Backup hiány | Script írás + cron | 1 óra |
| Deploy script hiány | Script írás | 2 óra |
| Dev stack duplikáció | Leállítás vagy eltávolítás | 30 perc |
| Telegram bekötés | Token beállítás + teszt | 1 óra |
| Kanban integráció | Döntés + migration | 4-8 óra |

**Összesen: ~1-2 munkanap rendbe hozható.**

---

## 4. Konkrét lépések a fejlesztés folytatásához

### Fázis 1 — AZONNALI (ma/holnap)

- [ ] **Dev gateway bezárása**: `/opt/openclaw/.env` → `OPENCLAW_GATEWAY_HOST=127.0.0.1`, `docker compose restart`
- [ ] **Backup script**: egyszerű `tar` a 4 SQLite DB-ről + cron (napi 1x)
- [ ] **Dev stack döntés**: le kell-e állítani az `openclaw-openclaw-gateway-1` konténert? Ha igen → `docker compose down` az `/opt/openclaw/` mappában

### Fázis 2 — RÖVID TÁVÚ (1 hét)

- [ ] **deploy.sh megírása** — idempotens, a DEPLOY.md alapján
- [ ] **Telegram bot bekötése** — `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` beállítása a Kanban service-ben és a Navibase stack-ben
- [ ] **Napi összefoglaló** implementálása (snapshot → Telegram)

### Fázis 3 — KÖZEPES TÁV (2-3 hét)

- [ ] **Kanban döntés**: skill-be integrálni VAGY a külön service-t az architektúra dokuba felvenni
- [ ] **ClawGuard dokumentálása**
- [ ] **Cloudflare Tunnel** felállítása (ha kell publikus hozzáférés)
- [ ] **Secrets management** bevezetése (legalább `.env` fájlok `chmod 600`)

### Fázis 4 — HOSSZÚ TÁV

- [ ] GDPR törlési script
- [ ] Secrets rotation (90 napos)
- [ ] Postgres migration előkészítés (ha több tenant lesz)

---

## 5. Hogyan tud Leoni (dn-leoni-01) segíteni?

### Amit Leoni MOST meg tud csinálni (SSH/távoli hozzáféréssel):

1. **Audit eredmények monitorozása** — ez a dokumentum folyamatosan frissíthető
2. **Script generálás** — `deploy.sh`, `backup.sh` megírása, Tomi jóváhagyása után feltöltés
3. **Dokumentáció karbantartás** — az akcióterv követése, állapot frissítés
4. **Konfigurációs javaslatok előkészítése** — pontos parancsok, fájl módosítások előre megírva

### Amit Leoni meg tudna csinálni SSH hozzáféréssel a dn-dev-02-höz:

1. **Gateway fix** — 5 perc, `.env` módosítás + restart
2. **Backup cron beállítás** — script + crontab
3. **Dev stack leállítás** — ha Tomi jóváhagyja
4. **Telegram konfig** — ha megkapja a bot tokent
5. **Deploy script tesztelés**

### Javaslat Tominak:

> **Adj SSH hozzáférést Leoninak a dn-dev-02-höz** (read-only vagy korlátozott sudo). Ezzel a Fázis 1-2 lépések nagy része automatizálható, és Leoni távfelügyeletet is tud végezni.

Alternatíva: Tomi manuálisan végrehajtja a lépéseket, Leoni előkészíti a pontos parancsokat.

---

## Összefoglalás

| Kérdés | Válasz |
|---|---|
| Működik a szerver? | **Igen**, a core stack fut |
| Van kritikus probléma? | **Igen**, a dev gateway publikus |
| Újra kell építeni? | **Nem**, javítható |
| Mennyi munka? | **1-2 nap** a kritikus dolgok |
| Leoni segíthet? | **Igen**, különösen SSH hozzáféréssel |

---

*Ez a dokumentum a 2026-02-13-as Claude audit alapján készült. Frissítés szükséges minden beavatkozás után.*
