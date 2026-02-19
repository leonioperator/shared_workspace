# Elkezdodott.hu — Teljes működési terv (Astro-alapú)

**Dátum:** 2026-02-19  
**Állapot:** WordPress → Astro migráció sikeres, hiányzó funkciók pótlása szükséges

---

## 1. Jelenlegi állapot (2026-02-19 20:10 UTC)

### ✅ Működő részek
- **Főoldal (/):** Gradient hero + blog lista, WordPress design reprodukálva
- **Blog lista (/blog/):** Blogcikkek kártyás megjelenítéssel
- **Blog poszt (/blog/elso-poszt/):** Egyedi poszt oldal
- **RSS feed (/rss.xml):** Valid XML, működik
- **Design:** Montserrat + Open Sans, gradient (#5568FF → #9A63FF), blog cards, footer

### ❌ Hiányzó oldalak (404)
- **/hirlevel/** — Hírlevél feliratkozás oldal
- **/kapcsolat/** — Kapcsolat oldal
- **/adatvedelem/** — Adatvédelem / GDPR oldal
- **/feed/** — RSS feed (jelenleg /rss.xml-en működik, /feed/ redirect hiányzik)

### 🔄 Átállítandó rendszerek
- **Hírlevél:** WordPress Newsletter plugin → külső szolgáltató vagy saját megoldás
- **Dokumentáció:** ops/ és recovery/ mappák még WordPress-t említenek

---

## 2. Hiányzó oldalak létrehozása (prioritási sorrend)

### 2.1. `/hirlevel/` — Hírlevél feliratkozás oldal

**Cél:** Feliratkozási űrlap AI insight hírlevélre

**Tartalom:**
- Hero szekció: "Iratkozz fel heti AI insightre"
- Alcím: "Trendek, tanulságok, üzleti hatás – minden hétfőn az inboxodban."
- Feliratkozási űrlap (külső szolgáltató embed VAGY saját)
- GDPR checkbox + Adatvédelmi tájékoztató link
- Példa hírlevél tartalom preview (opcionális)

**Technikai megoldás:**
- Astro oldal: `src/pages/hirlevel.astro`
- BaseLayout használata
- Hero + form szekció

---

### 2.2. `/kapcsolat/` — Kapcsolat oldal

**Cél:** Kapcsolatfelvétel

**Tartalom:**
- Cím: "Kapcsolat"
- Rövid intro: "Kérdésed van az AI stratégiáról vagy a Navibase szolgáltatásról?"
- Email cím: info@elkezdodott.hu (vagy Tomi döntése)
- Opcionális: kontakt űrlap (egyszerű email küldés PHP/FormSubmit/Formspree)
- Social media linkek (ha vannak)

**Technikai megoldás:**
- Astro oldal: `src/pages/kapcsolat.astro`
- BaseLayout használata
- Egyszerű szöveges tartalom VAGY embedded form

---

### 2.3. `/adatvedelem/` — Adatvédelmi tájékoztató

**Cél:** GDPR-kompatibilis adatkezelési tájékoztató

**Tartalom:**
- Adatkezelő neve, címe
- Kezelt adatok típusa (név, email, hírlevél feliratkozás)
- Adatkezelés célja
- Adatkezelés jogalapja
- Adatok törlése
- Jogok (hozzáférés, törlés, tiltakozás)
- Cookie-k (ha vannak)

**Technikai megoldás:**
- Astro oldal: `src/pages/adatvedelem.astro`
- BaseLayout használata
- Markdown vagy HTML tartalom (Tomi írja meg a szöveget)

---

### 2.4. `/feed/` → `/rss.xml` redirect

**Cél:** WordPress RSS feed URL kompatibilitás

**Technikai megoldás:**
- `.htaccess` redirect szabály:
  ```apache
  RewriteRule ^feed/?$ /rss.xml [R=301,L]
  ```
- VAGY: Astro `src/pages/feed.astro` redirect oldal

---

## 3. Hírlevél rendszer (WordPress Newsletter plugin → új megoldás)

### 3.1. Jelenlegi állapot
- WordPress Newsletter plugin törölve (WordPress teljes törlése miatt)
- Feliratkozók listája: **KRITIKUS** — ha volt, mentés szükséges!
- Hírlevél sablon: `shared_workspace/ops/newsletter/newsletter-template.md`

### 3.2. Javasolt hírlevél szolgáltatók (ingyenes szint)

| Szolgáltató | Ingyenes limit | Előnyök | Hátrányok |
|---|---|---|---|
| **MailerLite** | 1000 feliratkozó, 12k email/hó | Magyar UI, egyszerű, GDPR OK | Branding footer (ingyenes) |
| **Brevo** (Sendinblue) | Korlátlan feliratkozó, 300 email/nap | Teljes körű, SMTP is | 300 email/nap limit |
| **EmailOctopus** | 2500 feliratkozó, 10k email/hó | Tiszta UI, AWS SES alapú | Branding footer |
| **ConvertKit** | 1000 feliratkozó, korlátlan email | Creator-friendly, landing pages | Összetettebb UI |
| **Buttondown** | 100 feliratkozó, korlátlan email | Markdown alapú, egyszerű | Feliratkozó limit alacsony |

**Ajánlás:** **MailerLite** vagy **Brevo** (Sendinblue)

**Indoklás:**
- MailerLite: egyszerű, magyar UI, 1000 feliratkozó elegendő kezdésnek
- Brevo: ha SMTP-t is akarod használni (nem csak hírlevél, hanem tranzakcionális email is)

---

### 3.3. Hírlevél integráció lépései

#### A) MailerLite példa

1. **Fiók létrehozás:** mailerlite.com (Tomi csinálja)
2. **Feliratkozási űrlap embed kód generálás:**
   - MailerLite admin → Forms → Create embedded form
   - Inline form vagy Popup
   - Embed kód másolása
3. **Astro integráció:**
   - `/hirlevel/` oldalon: embed HTML beillesztése
   - Hero CTA gomb: link `/hirlevel/`-re VAGY direkt popup trigger
4. **GDPR:**
   - MailerLite-ban beállítás: GDPR checkbox enabled
   - Adatvédelmi tájékoztató URL: `https://elkezdodott.hu/adatvedelem/`
5. **Double opt-in:** MailerLite-ban bekapcsolva (ajánlott)

#### B) Brevo (Sendinblue) példa

1. **Fiók létrehozás:** brevo.com (Tomi csinálja)
2. **Feliratkozási űrlap:**
   - Brevo admin → Contacts → Forms → Create a form
   - Embed kód másolása
3. **Astro integráció:** ugyanaz, mint MailerLite
4. **SMTP (opcionális):**
   - Brevo SMTP credentials → WordPress/PHP mail() helyettesítés

#### C) Saját megoldás (haladó, ha függetlenség fontos)

**Komponensek:**
- **Frontend:** Astro form (HTML)
- **Backend:** API endpoint (Cloudflare Workers / Vercel Edge / PHP script)
- **Tárolás:** PostgreSQL / Supabase / Google Sheets (!)
- **Küldés:** SMTP (SendGrid, Mailgun, AWS SES) vagy Brevo API
- **Double opt-in:** saját token generálás + megerősítő email

**Előnyök:**
- Teljes kontroll, nincs vendor lock-in
- Költséghatékony (Cloudflare Workers + Supabase ingyenes tier)

**Hátrányok:**
- Több fejlesztési idő
- GDPR compliance saját felelősség
- Email deliverability (SPF, DKIM, DMARC setup)

**Ajánlás:** Csak ha későbbi scaling vagy API automatizálás prioritás.

---

## 4. Heti hírlevél workflow (automatizálás)

### 4.1. Jelenlegi sablon
`shared_workspace/ops/newsletter/newsletter-template.md` — heti AI insight sablon

### 4.2. Javasolt workflow

**Hétfő reggel:**
1. Leoni (agent) összegyűjti:
   - Előző hét blogcikkek
   - Bejövő AI hírlevelek kivonatai (TLDR AI, Mindstream, stb.)
   - Releváns KKV/AI trendek
2. Sablon alapján draft hírlevél készítés
3. Draft → `shared_workspace/outbound/newsletter-YYYYMMDD.md`
4. Tomi review + szerkesztés
5. Tomi jóváhagyás után:
   - MailerLite/Brevo admin → Create campaign
   - Copy-paste tartalom
   - Send (vagy schedule)

### 4.3. Későbbi automatizálás (opcionális)

**MailerLite API integráció:**
- Leoni draft-ot közvetlenül MailerLite API-val feltölti campaign draft-ként
- Tomi csak jóváhagyja a MailerLite UI-ban

**Brevo API integráció:** ugyanaz

**Megvalósítás:** Python script vagy Node.js Astro API route

---

## 5. Dokumentáció frissítése

### 5.1. Frissítendő fájlok

| Fájl | Frissítés |
|---|---|
| `shared_workspace/ops/README.md` | WordPress → Astro, ninjalab.hu VPS build workflow |
| `shared_workspace/ops/newsletter/README.md` | Newsletter plugin → MailerLite/Brevo integráció |
| `shared_workspace/recovery/RECOVERY-CHECKLIST.md` | Astro projekt rebuild lépések |
| `TOOLS.md` (workspace) | Astro build + deploy, ninjalab.hu SSH |

### 5.2. Új dokumentáció

**`shared_workspace/ops/elkezdodott/README.md`** — Elkezdodott.hu deployment guide
- Astro projekt helye: `/srv/elkezdodott` (ninjalab.hu)
- Build parancs: `npm run build`
- Deploy: `./scripts/deploy.sh`
- SSH kulcs: ninjalab.hu → shared hosting (jelszómentes)
- Deploy útvonal: `/home/hogyanvi/addond/elkezdodott.hu/`

---

## 6. Implementációs terv (lépések prioritás szerint)

### Fázis 1: Kritikus linkek javítása (azonnal)
1. ✅ **WordPress törlés + Astro gyökérbe helyezés** — KÉSZ (2026-02-19)
2. 🔄 **Hiányzó oldalak létrehozása:**
   - `/hirlevel/` — placeholder oldal (form nélkül, "Hamarosan" üzenet)
   - `/kapcsolat/` — egyszerű szöveges oldal (email cím)
   - `/adatvedelem/` — placeholder (Tomi írja meg a szöveget)
3. 🔄 **RSS redirect:** /feed/ → /rss.xml (.htaccess vagy Astro redirect)
4. 🔄 **Deploy:** build + push

**Várható idő:** 30-60 perc  
**Felelős:** Leoni (agent)

---

### Fázis 2: Hírlevél rendszer kiválasztása és integráció (1-2 nap)
1. 🔄 **Tomi döntés:** MailerLite vagy Brevo? (vagy saját?)
2. 🔄 **Fiók létrehozás:** Tomi csinálja (API key mentése .env-be)
3. 🔄 **Feliratkozási űrlap embed:**
   - Szolgáltató admin → form generálás
   - Embed kód másolása
4. 🔄 **Astro integráció:**
   - `/hirlevel/` oldal frissítése embed form-mal
   - GDPR checkbox + adatvédelmi tájékoztató link
5. 🔄 **Teszt feliratkozás:** működik-e a double opt-in?
6. 🔄 **Deploy**

**Várható idő:** 1-2 óra (Tomi fiók setup) + 1 óra (Leoni integráció)  
**Felelős:** Tomi (döntés + fiók) + Leoni (kód)

---

### Fázis 3: Heti hírlevél workflow beállítása (1-2 nap)
1. 🔄 **Sablon finalizálás:**
   - `newsletter-template.md` review
   - Tomi jóváhagyás
2. 🔄 **Első draft készítés:** Leoni (agent) generálja a következő hétfőre
3. 🔄 **Tomi review + szerkesztés**
4. 🔄 **Küldés teszt:** MailerLite/Brevo campaign létrehozás, teszt email
5. 🔄 **Cron job (opcionális):** hétfő reggel auto-draft készítés

**Várható idő:** 2-3 óra (első draft + review ciklus)  
**Felelős:** Leoni (draft) + Tomi (review + küldés)

---

### Fázis 4: Dokumentáció frissítése (1 nap)
1. 🔄 **ops/README.md** frissítése
2. 🔄 **ops/newsletter/README.md** átírása (MailerLite/Brevo)
3. 🔄 **recovery/** frissítése (Astro rebuild lépések)
4. 🔄 **TOOLS.md** frissítése (Astro workflow)
5. 🔄 **Git commit + push**

**Várható idő:** 1-2 óra  
**Felelős:** Leoni (agent)

---

### Fázis 5: Továbbfejlesztések (opcionális, később)
- Blog kategóriák / tag szűrők
- Kapcsolódó cikkek (related posts)
- SEO meta adatok (OpenGraph, Twitter Card)
- Google Analytics / Plausible integráció
- Hírlevél API automatizálás (draft → MailerLite API)
- Featured image támogatás blog posztokhoz
- Mid-content CTA blogposztokban (Astro komponens)

---

## 7. Költség becslés

| Tétel | Havi költség |
|---|---|
| **Hosting (shared)** | Meglévő, nincs extra költség |
| **Domain (elkezdodott.hu)** | Meglévő |
| **Hírlevél (MailerLite ingyenes)** | €0 (max 1000 feliratkozó) |
| **Hírlevél (MailerLite fizetős)** | €9-15/hó (>1000 feliratkozó) |
| **Brevo (ingyenes)** | €0 (300 email/nap) |
| **Saját megoldás (Cloudflare Workers + Supabase)** | €0 (ingyenes tierek) |

**Összesen:** €0/hó (kezdetben)

---

## 8. Kockázatok és mitigálás

| Kockázat | Hatás | Mitigálás |
|---|---|---|
| **WordPress feliratkozók elvesztése** | Adatvesztés | WordPress adatbázis export (már késő?), újrafeliratkozás kérés |
| **Email deliverability rossz** | Spam folderbe kerülnek emailek | SPF/DKIM/DMARC setup, MailerLite/Brevo használata (saját infrastruktúra helyett) |
| **Hírlevél szolgáltató váltás** | Vendor lock-in | Export funkcionalitás ellenőrzése (MailerLite CSV export OK) |
| **GDPR compliance hiány** | Jogi kockázat | Adatvédelmi tájékoztató + GDPR checkbox + double opt-in |

---

## 9. Döntési pontok Tominak

1. **Hírlevél szolgáltató:** MailerLite, Brevo, vagy saját megoldás?
2. **Adatvédelmi tájékoztató szöveg:** Tomi írja meg, vagy sablon alapján Leoni?
3. **Kapcsolat email:** info@elkezdodott.hu vagy másik?
4. **WordPress feliratkozók:** volt-e adat, mentés szükséges-e?
5. **Blog további fejlesztések prioritása:** SEO meta, kategóriák, kapcsolódó cikkek?

---

## 10. Következő lépések (AZONNAL)

### Leoni (agent) feladatok:
1. `/hirlevel/`, `/kapcsolat/`, `/adatvedelem/` placeholder oldalak létrehozása
2. `/feed/` → `/rss.xml` redirect beállítása
3. Build + deploy
4. Dokumentáció frissítés (ops/, recovery/)
5. Git commit + push

### Tomi feladatok:
1. Hírlevél szolgáltató döntés (MailerLite / Brevo?)
2. Adatvédelmi tájékoztató szöveg megírása
3. Hírlevél fiók létrehozás (ha döntött)
4. API key megosztása Leonival (ha szükséges)

---

**Várható teljes megvalósítási idő:** 2-3 munkanap  
**Becsült token költség:** ~50-80k tokens (draft generálás + review)

---

**TERV VÉGE**
