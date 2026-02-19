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

## Deploy sikeresség: ⏸️ VÁRAKOZIK

### Deploy script: `/srv/elkezdodott/scripts/deploy.sh`
```bash
#!/usr/bin/env bash
set -e

npm run build

ssh hogyanvi@185.51.191.64 "rm -rf /home/hogyanvi/addond/elkezdodott.hu/astro/*"
scp -r dist/* hogyanvi@185.51.191.64:/home/hogyanvi/addond/elkezdodott.hu/astro
```

**Cél útvonal:** `/home/hogyanvi/addond/elkezdodott.hu/astro`

### Deploy várakozás oka
- Mission szerint: "jelszót előtte beszéljük meg"
- SSH kulcs nincs beállítva ninjalab.hu → shared hosting között (jelszó kell scp-hez)
- VAGY: deploy útvonal tisztázása (astro almappa vs. gyökér)

---

## RSS elérhetőség: ✅
- URL: https://elkezdodott.hu/rss.xml (deploy után)
- Lokális teszt: `/srv/elkezdodott/dist/rss.xml` (generálva, valid XML)

---

## Főoldal státusz: ✅ (build)
- Blog lista a főoldal
- Poszt dátum: magyar formátum (2026. 02. 19.)
- Clean minimal layout

---

## Következő lépések
1. **Deploy jóváhagyás:** SSH jelszó vagy kulcs beállítás ninjalab → shared hosting
2. **Deploy útvonal megerősítés:** `/home/hogyanvi/addond/elkezdodott.hu/astro` helyes?
3. **Deploy futtatás:** `cd /srv/elkezdodott && ./scripts/deploy.sh`
4. **Teszt:** https://elkezdodott.hu ellenőrzés
5. **WordPress törlés:** ha sikeres a deploy, régi WordPress tartalom eltávolítása

---

**Státusz összefoglaló:**  
Build: ✅ Sikeres  
Deploy: ⏸️ Jóváhagyásra vár  
RSS: ✅ Működik (build output-ban)  
Főoldal: ✅ Blog lista (build output-ban)
