---
title: Az AI agented nem buta, csak nincs kontrollja
site: elkezdodott.hu
status: draft
created: '2026-06-18'
source: backfill-2026-06-13-18
id: elkezdod
content_type: article
created_at: '2026-06-18'
updated_at: '2026-06-18T13:30:01.939468+00:00'
---

# Az AI agented nem buta, csak nincs kontrollja

Az AI agentekkel nem az a fő baj, hogy hibáznak. Az a baj, ha nincs leírva, mit szabad nekik megtenni.

Egy kis cégben ez gyorsan káosz lesz. Először csak emailt fogalmaz. Aztán már fájlt ír. Aztán taskot hoz létre. Aztán értesítést küld. Aztán valaki azt hiszi, hogy publikált vagy jóváhagyott valamit, pedig nem kellett volna.

## A kontroll nélküli agent tünetei

- sikerüzenetet küld ellenőrzés nélkül,
- drága modellt használ cronra,
- ugyanazt a taskot újra és újra létrehozza,
- nem különíti el a draftot és a publikálást,
- nem tudod, melyik automatizmus mikor futott le.

## A mini-audit lényege

Nem kell 40 oldalas policy. Kell egy oldal, amit a csapat megért:

1. Mit csinálhat automatikusan?
2. Mihez kell emberi jóváhagyás?
3. Hol van rollback?
4. Mi számít sikernek?
5. Mi történik hiba esetén?

## A jó AI agent működési kerete

A jó agent nem szabadon improvizál. Keretben dolgozik.

- Draftolhat, de nem publikál.
- Javasolhat, de nem hagy jóvá.
- Fájlt írhat, de ellenőrzi, hogy létrejött.
- Értesíthet, de nem spameli szét a csatornát.
- Ha hibázik, nem takargatja: álljon meg és szóljon.

## Miért üzleti téma ez?

Mert az AI agent nem csak technológia. Operációs munkatárs. Ha nincs munkaköri leírása, jogosultsági kerete és ellenőrzése, akkor nem automatizációt építesz, hanem kockázatot.

## Következő lépés

Válassz ki három AI workflow-t. Írd melléjük:

- input,
- output,
- jogosultság,
- emberi döntési pont,
- hiba esetén teendő.

Ha ez nincs meg, még nincs rendszered. Csak egy lelkes robotod van.

