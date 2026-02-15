# Heti összefoglalók

Hétfő reggelente (08:00 CET) automatikusan generált heti review reportok.

## Formátum

- **Fájlnév:** `YYYY-MM-DD.md` (hétfő dátuma)
- **Email:** részletes összefoglaló küldve vt@vinczetamas.hu címre
- **Telegram:** csak rövid értesítés: "Heti összefoglaló elküldve emailben"

## Tartalom

- Elvégzett feladatok (részletezve)
- Nyitott itemek (státusz, blokkolók)
- Problémák és megoldások
- Tanulságok
- Költség/token használat összesítés
- Javaslat a következő hétre
- Recovery kit ellenőrzés
- GitHub repo karbantartás
- Dependency audit
- Verzió check (OpenClaw, ClawGuard)

## Cron job

- **Név:** "Heti összefoglaló (hétfő)"
- **ID:** d8092308-d3fb-4e4a-bf6f-4b9c5636aa24
- **Schedule:** hétfő 08:00 CET (`0 7 * * 1`)
- **Forrás:** HEARTBEAT.md "Heti (hétfő reggel 08:00 CET)" szakasz
