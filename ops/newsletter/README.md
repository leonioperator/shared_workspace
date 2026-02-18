# Elkezdődött.hu – Hírlevél rendszer dokumentáció

## Választott megoldás: Newsletter plugin (WordPress)

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
