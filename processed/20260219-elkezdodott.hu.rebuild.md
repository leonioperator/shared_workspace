MISSION: ELKEZDODOTT.HU REBUILD – ASTRO STATIC

KONTEXTUS:
- Domain: elkezdodott.hu
- Jelenleg WordPress fut → manuálisan törlésre kerül
- Cél: minimal static Astro blog
- Build environment: ninjalab.hu VPS (Node v20.20.0)
- Static build only
- No SSR
- No Docker
- Blog = főoldal
- Minimal design (korábbi design vizuális struktúráját reprodukáld – te tudod milyen volt)
- RSS működjön
- SSH-based management
- Deploy: local build ninjalab.hu-n → dist → deploy.sh → shared hosting

FELADAT:

1. SSH-n keresztül lépj be ninjalab VPS-re.
2. Hozd létre /srv/elkezdodott mappát tiszta környezetben.
3. Inicializálj új Astro projektet:
   - static
   - minimal starter
4. Konfiguráció:
   - site: https://elkezdodott.hu
   - trailingSlash: "always"
   - output: "static"
5. Content structure:
   - src/content/blog
   - blog legyen a főoldal (index.astro getCollection)
   - RSS feed generálás
6. Minimal design (feleljen meg az eddigi WP oldal desig-nak):
   - fehér háttér
   - tipográfia clean
   - javasold, hogy érdemes-e framework CSS?
   - egyszerű lista layout
7. Content schema stabil date parse-szal
8. Teszt post generálása ISO date-tel
9. Build:
   - npm install
   - npx astro content sync
   - npm run build
10. Dist ellenőrzés
11. Vizsgáld meg a meglévő /srv/elkezdodott.hu/scripts/deploy.sh scriptet, és futtasd, de jelszót előtte beszéljük meg
12. Fontos, hogy a shared tarhely hoston SSH után a /home/hogyanvi mappába kerülsz. Az elkezdodott.hu weboldal utvonala: /home/hogyanvi/addond/elkezdodott.hu
13. Jelentés:
    - build sikeresség
    - deploy sikeresség
    - RSS elérhetőség
    - főoldal státusz

KÖVETELMÉNYEK:
- Ne használj WordPress-t
- Ne használj Docker-t
- Ne használj SSR-t
- Ne telepíts felesleges dependency-ket
- Tartsd a projektet agent-manageable struktúrában
- Minden lépést logolj és tartsd frissen a shared_workspace megfelelő mappáját, ahogy eddig!

OUTPUT:
Rövid, strukturált státuszjelentés.
Ha hiba van → konkrét error + javasolt fix.

PRIORITÁS:
Stabil, minimal Astro blogmotor.
