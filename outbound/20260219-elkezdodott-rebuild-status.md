# Elkezdődött.hu Rebuild — Státusz

**Dátum:** 2026-02-19 18:50 UTC  
**Feladat:** elkezdodott.hu minimal static Astro blog építés  
**VPS:** ninjalab.hu (46.224.88.202)  
**Build környezet:** Node v20.20.0

---

## Build sikeresség: ✅

### Konfiguráció
- **Site:** https://elkezdodott.hu
- **Output:** static
- **Trailing slash:** always
- **RSS feed:** működik (/rss.xml)

### Struktúra
```
/srv/elkezdodott/
├── astro.config.mjs (frissítve: output static, trailingSlash always)
├── src/
│   ├── content/
│   │   ├── blog/ (teszt poszt: elso-poszt.md)
│   │   └── config.ts (date schema, ISO parse)
│   ├── pages/
│   │   ├── index.astro (blog lista főoldal)
│   │   ├── [slug].astro (egyedi poszt oldal)
│   │   ├── blog/index.astro (blog lista)
│   │   ├── blog/[slug].astro (blog poszt)
│   │   └── rss.xml.ts (RSS feed generálás)
│   └── layouts/BaseLayout.astro
├── dist/ (build output)
└── scripts/deploy.sh
```

### Build output (dist/)
- `index.html` — főoldal (blog lista)
- `blog/index.html` — blog lista
- `blog/elso-poszt/index.html` — teszt poszt
- `rss.xml` — RSS feed (működik)
- favicon.ico, favicon.svg

### Javítások a build során
1. **astro.config.mjs:** hozzáadva `output: "static"`, `trailingSlash: "always"`
2. **content schema konzisztencia:** pubDate → date (minden fájlban egységesítve)
3. **elso-poszt.md:** frontmatter date formátum ISO stringre javítva
4. **blog/[slug].astro, blog/index.astro:** pubDate → date
5. **rss.xml.ts:** pubDate → date (post.data.date)

### Design
- Minimal, clean, fehér háttér
- Tipográfia: system-ui, sans-serif
- Post kártyák hover effekttel
- Responsive

---

## Deploy sikeresség: ✅

### Deploy lépések
1. **SSH kulcs beállítás:** ninjalab.hu (root) → shared hosting (hogyanvi@185.51.191.64)
   - Ed25519 kulcspár generálva ninjalab.hu-n
   - Public key hozzáadva shared hosting authorized_keys-hez
   - Jelszómentes SSH működik
2. **Deploy script futtatás:** `/srv/elkezdodott/scripts/deploy.sh`
   - Build: sikeres (dist/ regenerálva)
   - SSH rm: astro almappa tisztítva
   - SCP: dist/* → `/home/hogyanvi/addond/elkezdodott.hu/astro/`
3. **Cél útvonal:** `/home/hogyanvi/addond/elkezdodott.hu/astro/`
   - index.html, blog/, rss.xml, favicon stb. feltöltve

### Élő teszt
- **Astro oldal:** https://elkezdodott.hu/astro/ ✅ (működik, blog lista látható)
- **Blog poszt:** https://elkezdodott.hu/astro/elso-poszt/ ✅
- **RSS feed:** https://elkezdodott.hu/astro/rss.xml ✅ (valid XML, 1 item)

---

## RSS elérhetőség: ✅
- **URL:** https://elkezdodott.hu/astro/rss.xml
- **Státusz:** működik, valid XML
- **Tartalom:** 1 poszt ("Első poszt", 2026-02-19)

---

## Főoldal státusz: ⚠️ WordPress még fut

### Jelenlegi állapot
- **https://elkezdodott.hu** → WordPress oldal (régi)
- **https://elkezdodott.hu/astro/** → Astro static blog (új) ✅

### WordPress fájlok a gyökérben
- `/home/hogyanvi/addond/elkezdodott.hu/` még tartalmaz WordPress fájlokat:
  - index.php, wp-admin/, wp-content/, wp-config.php stb.
- `.htaccess` WordPress RewriteRule-okat tartalmaz

### Következő lépés (manuális)
1. **WordPress fájlok törlése** a gyökérből (VAGY backup mentése)
2. **Astro tartalom áthelyezése** gyökérbe:
   ```bash
   cd /home/hogyanvi/addond/elkezdodott.hu
   rm -rf wp-* index.php .htaccess (backup után!)
   mv astro/* .
   rmdir astro
   ```
3. **VAGY:** `.htaccess` módosítása, hogy az astro almappából szolgáljon ki mindent

---

## Következő lépések
1. ✅ **SSH kulcs beállítás:** kész
2. ✅ **Deploy futtatás:** kész
3. ✅ **Teszt:** https://elkezdodott.hu/astro/ működik
4. ⏸️ **WordPress törlés:** manuális lépés, jóváhagyásra vár
5. ⏸️ **Astro tartalom gyökérbe helyezése:** manuális lépés

---

**Státusz összefoglaló:**  
Build: ✅ Sikeres  
Deploy: ✅ Sikeres (astro almappába)  
RSS: ✅ Működik (https://elkezdodott.hu/astro/rss.xml)  
Főoldal: ⚠️ WordPress még fut, Astro elérhető /astro/ útvonalon
