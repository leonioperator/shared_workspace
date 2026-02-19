# Elkezdődött.hu – Hírlevél rendszer dokumentáció

## ⚠️ FRISSÍTVE: 2026-02-19 — WordPress → Astro migráció

**Előző megoldás:** Newsletter plugin (WordPress) — **TÖRÖLVE**  
**Új megoldás:** Külső hírlevél szolgáltató integráció (MailerLite / Brevo)

---

## Választott megoldás: MailerLite / Brevo (TBD)

### Indoklás
- **Ingyenes**, korlátlan feliratkozó, WP-ből kezelhető
- Nincs külső szolgáltató dependency (MailerLite, Brevo stb.)
- WP PHP mail-en vagy SMTP-n keresztül küld (hosting biztosítja)
- GDPR-kompatibilis beépítetten
- Shortcode-alapú űrlap, könnyen beágyazható bárhová
- Admin: `https://elkezdodott.hu/wp-admin/admin.php?page=newsletter_main_index`

## Komponensek

### 1. Lista
- **Név:** Elkezdődött – AI Insight
- **ID:** List 1 (Newsletter plugin belső rendszer)
- **Típus:** forced (minden feliratkozó automatikusan erre a listára kerül)

### 2. Feliratkozási űrlap
- **Shortcode:** `[newsletter_form]`
- **Elhelyezések:**
  - ✅ Hírlevél oldal (ID: 17, slug: /hirlevel/)
  - ✅ Blogposztok alja (automatikusan, functions.php filter)
  - ✅ Widget area regisztrálva: "Hírlevél Sidebar" (kézzel hozzáadható WP admin → Megjelenés → Widgetek)
- **Mezők:** Név + Email + GDPR checkbox
- **Opt-in:** Double opt-in (megerősítő email)

### 3. GDPR
- Privacy checkbox: BEKAPCSOLVA
- Privacy URL: `https://elkezdodott.hu/adatkezelesi-tajekoztato`
- ⚠️ **TOMI TEENDŐ:** Az adatkezelési tájékoztató oldalt létre kell hozni!

### 4. Emailek (magyar nyelvű)
- **Megerősítő email tárgya:** "Erősítsd meg a feliratkozásodat!"
- **Sikeres feliratkozás tárgya:** "Sikeresen feliratkoztál!"
- **Feladó:** Elkezdődött.hu <info@elkezdodott.hu>

### 5. Stílus
- A blogposzt alatti CTA: sötét gradient háttér (#1a1a2e → #16213e)
- Gomb: kék gradient (#00d4ff → #0099cc)
- Illeszkedik az elkezdodott.hu design nyelvéhez

## Heti hírlevél sablon

Lásd: `newsletter-template.md`

## Heti automatizálás

### Jelenlegi megoldás
A Newsletter plugin ingyenes verziója **nem tartalmaz automatikus digest funkciót**.

### Javasolt workflow (heti, hétfő reggel):
1. Leoni (agent) összegyűjti a heti blogcikkeket + trend insightokat
2. Kitölti a sablon alapján a hírlevél szövegét
3. Newsletter plugin admin → Newsletters → New → beilleszti a tartalmat
4. Tomi jóváhagyja → Küldés

### Alternatíva (ha automatizálás kell):
- **Newsletter plugin Automated addon** (fizetős, ~€29/év) - automatikus digest
- **Vagy:** Leoni cron-alapú draft készítés + WP REST API-val newsletter létrehozás

## Fájlok módosítva
- `wp-content/themes/elkezdodott-theme/functions.php` — newsletter widget area + blog post footer CTA
- `wp-content/themes/elkezdodott-theme/custom.css` — newsletter form stílus
- Post ID 17 (Hírlevél oldal) — `[newsletter_form]` shortcode hozzáadva
- `newsletter_main` WP option — feladó beállítások
- `newsletter_subscription` WP option — űrlap + GDPR + magyar szövegek
- `newsletter_lists` WP option — lista konfiguráció

## Admin URL-ek
- Newsletter dashboard: `/wp-admin/admin.php?page=newsletter_main_index`
- Feliratkozók: `/wp-admin/admin.php?page=newsletter_users_index`
- Új hírlevél: `/wp-admin/admin.php?page=newsletter_emails_new`
- Beállítások: `/wp-admin/admin.php?page=newsletter_main_main`
- Feliratkozási űrlap: `/wp-admin/admin.php?page=newsletter_subscription_forms`

---

## Új megoldás (2026-02-19 után)

### Szolgáltató opciók
1. **MailerLite** (javasolt)
   - Ingyenes: 1000 feliratkozó, 12k email/hó
   - Magyar UI, GDPR OK
   - Embed form generálás
   
2. **Brevo** (Sendinblue)
   - Ingyenes: korlátlan feliratkozó, 300 email/nap
   - SMTP is használható
   - API integráció

3. **Saját megoldás**
   - Cloudflare Workers + Supabase
   - Teljes kontroll
   - Több fejlesztési idő

### Integráció (példa MailerLite)
1. Tomi létrehozza a fiókot (mailerlite.com)
2. Feliratkozási űrlap embed kód generálás
3. Astro `/hirlevel/` oldalon embed HTML beillesztése
4. GDPR checkbox + adatvédelmi tájékoztató link
5. Double opt-in beállítás

### Heti workflow
1. Leoni (agent) hétfő reggel draft hírlevél készítés
2. Draft → `shared_workspace/outbound/newsletter-YYYYMMDD.md`
3. Tomi review + szerkesztés
4. MailerLite/Brevo admin → campaign létrehozás + küldés

### Részletek
Lásd: `shared_workspace/outbound/20260219-elkezdodott-terv.md`

---

## Előző WordPress megoldás (ELAVULT, 2026-02-19 előtt)

<details>
<summary>Kattints a korábbi dokumentációért (archív)</summary>

### Indoklás
- **Ingyenes**, korlátlan feliratkozó, WP-ből kezelhető
- Nincs külső szolgáltató dependency (MailerLite, Brevo stb.)
- WP PHP mail-en vagy SMTP-n keresztül küld (hosting biztosítja)
- GDPR-kompatibilis beépítetten
- Shortcode-alapú űrlap, könnyen beágyazható bárhová
- Admin: `https://elkezdodott.hu/wp-admin/admin.php?page=newsletter_main_index`

[... korábbi dokumentáció ...]

</details>
