---
id: 2026-06-
title: AI agent kontroll mini-audit sablon - KKV számára
site: vinczetamas
content_type: article
created_at: '2026-06-02'
status: draft
updated_at: '2026-06-02T10:30:02.115210+00:00'
---

# AI agent kontroll mini-audit sablon - KKV számára

## Mit kapsz ezzel

Ezzel a sablonnal gyorsan le tudod írni, hol lehet önálló az AI agented, hol kell engedélyt kérnie, és hol kell naplózni vagy visszafordítani a működését.

## Mini workflow

### 1. Agent feladatkör

Írd le egy mondatban, mire használjátok az agentet.

Példák:
- Bejövő emailek előszűrése
- Ajánlatok előkészítése
- Hibajegyek összefoglalása
- Napi riport készítése
- Ügyfélkérdések első válasza

Kontroll kérdés:
- [ ] Pontosan le van írva, mi az agent dolga?
- [ ] Le van írva, mi nem az agent dolga?
- [ ] Tudja a csapat, mikor nem szabad agentet használni?

### 2. Automatikus műveletek

Ezek azok a lépések, amelyeket az agent emberi jóváhagyás nélkül is megtehet.

Példák:
- Email összefoglalása
- Feladatlista készítése
- Piszkozat generálása
- Belső státusz riport összeállítása
- Dokumentum keresése és forrás megjelölése

Kontroll kérdés:
- [ ] Ezek csak alacsony kockázatú műveletek?
- [ ] Nem küldenek ki adatot külső félnek?
- [ ] Nem módosítanak pénzügyi, ügyfél- vagy szerződéses adatot?

### 3. Jóváhagyási pontok

Ezek azok a helyzetek, ahol az agent nem dönthet egyedül.

Tipikus jóváhagyási pontok:
- Ügyfélnek kimenő email
- Árajánlat vagy szerződés módosítása
- Pénzügyi adat átírása
- Fájl törlése vagy megosztása
- Külső rendszerben művelet indítása

Kontroll kérdés:
- [ ] Van lista arról, mikor kell emberi döntés?
- [ ] Ki a jóváhagyó?
- [ ] Mennyi ideig várhat az agent válaszra?
- [ ] Mi történik, ha nincs válasz?

### 4. Tiltott műveletek

Ezek azok, amelyeket az agent soha nem végezhet önállóan.

Javasolt tiltólista:
- Jelszó, API kulcs vagy titkos adat kezelése
- Fájl törlése
- Fizetés vagy pénzügyi tranzakció indítása
- Ügyféladat továbbküldése külső címre
- Szerződés vagy ajánlat véglegesítése
- Publikus poszt vagy email kiküldése jóváhagyás nélkül

Kontroll kérdés:
- [ ] Le van írva a tiltólista?
- [ ] Az agent promptja és workflow-ja tartalmazza?
- [ ] A csapat ismeri?

### 5. Naplózás és rollback

Az agent működésének utólag ellenőrizhetőnek kell lennie.

Minimum napló:
- Mikor futott?
- Milyen inputot kapott?
- Milyen döntést készített elő?
- Milyen műveletet hajtott végre?
- Ki hagyta jóvá?
- Hogyan lehet visszavonni?

Kontroll kérdés:
- [ ] Minden fontos futás visszakereshető?
- [ ] Látszik, ki hagyott jóvá egy kimenő műveletet?
- [ ] Van visszaállítási lépés, ha az agent rossz irányba ment?

## Egyoldalas kontroll szabály

Használd ezt belső szabályként:

Az AI agent önállóan csak információt gyűjthet, összefoglalhat és piszkozatot készíthet. Ügyfélnek kimenő üzenet, adatváltoztatás, fájlmegosztás, pénzügyi művelet vagy publikus akció csak emberi jóváhagyással történhet. Minden fontos futást naplózni kell, és minden magas kockázatú művelethez legyen visszavonási lépés.

## Következő lépés

Ha ezt a cégedben gyorsan rendbe akarod tenni: AI agent kontroll mini-audit 89 ezer forintért.

Egy nap alatt összerakjuk, mit tehet az agented, mit nem, mikor kér emberi döntést, és hol kell naplózás vagy rollback.

Ha nem kapsz legalább 5 konkrét kontrollpontot a meglévő workflow-dra, visszaadom az árát.

vinczetamas.hu/audit
