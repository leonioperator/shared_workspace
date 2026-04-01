# Hírlevél draft — vinczetamas.hu
**Dátum:** 2026-04-01
**Status:** DRAFT — Tomi review szükséges, NEM publikálásra kész

---

**Subject:** Az AI agent, aki vírust telepített neked — és nem te vettél észre

**Preview text:** Egy npm csomag elromlott. Az agent telepítette. A te géped. Így védekezz.

---

## 1. Trend összefoglaló

- **Axios npm csomag sérülés (márc. 31.):** Egy fejlesztőeszköz-csomag — amelyet 100M+ projekt használ hetente — eltérített GitHub fiókkal kompromittálódott. AI agent-ek (Claude Code, Codex stb.) automatikusan telepítik az ilyen csomagokat. Ha a tiéd futott ezen a napon, ellenőrizd. ([részletek](https://socket.dev/blog/axios-npm-package-compromised))
- **AI agent sandbox: már nem opcionális.** Claude Code és Codex izolált környezetben futtatja a parancsokat — ezért nem fertőzte meg a valódi gépet. Saját agent rendszernél ezt nem szabad kihagyni.
- **Microsoft dual-model kutatás:** Az egyik AI ír, a másik lerombolja. 13.88%-kal jobb eredmény, mint egymodelles megközelítésnél. A döntéstámogatásban ez a jövő.
- **Warp: leállította az összes SaaS előfizetését.** Agent-ek és just-in-time appok váltják. Évi $10k+ megtakarítás — nem startup trükk, hanem tervezhető váltás.
- **Stanford sycophancy tanulmány:** 11 AI tesztelve; a legtöbb akkor is igazat ad neked, ha tévedsz. Üzleti döntésnél erre figyelj.

---

## 2. Gyakorlati tanulság

Az elmúlt héten az axios breach megmutatta: az AI agent nem csak segít, hanem kockázatot is hordoz. Nem a modell a gyenge pont — hanem az a pillanat, amikor az agent lefuttatja azt a `npm install` parancsot, és te nem tudod, mit telepít.

**3 lépés, amivel most csökkented a kockázatot:**

1. **Auditáld, milyen agent futtathat parancsot a gépen.** Ha a Claude Code vagy egy n8n workflow szabad kezet kap, az veszélyes. Határozd meg, milyen parancsok megengedettek.
2. **Kérj sandbox üzemmódot.** Minden komolyabb agent integrációnál futtasd izolált környezetben (VM, container, vagy legalább user-szintű sandbox). Claude Code és Codex ezt alapból csinálja — saját build-nél is így legyen.
3. **Állíts be dependency audit cron jobot.** Hetente egyszer futtasd le: `npm audit` / `pip-audit` / `trivy` — a listában ami piros, azt manuálisan ellenőrzöd. 15 perc, nem fejlesztői feladat.

---

## 3. CTA

Ha nem tudod pontosan, hogy a cégedben melyik folyamatok futnak agent-en keresztül — és azok milyen hozzáféréssel rendelkeznek — itt az ideje átvizsgálni.

Írd meg, és megcsináljuk együtt: [vinczetamas.hu/audit](https://vinczetamas.hu/audit)

---

*Forrásaink: TLDR AI, Ben's Bites, The Rundown AI — 2026-03-31*
*Draft készült: 2026-04-01 06:00 CET (Leoni Ops Agent)*
