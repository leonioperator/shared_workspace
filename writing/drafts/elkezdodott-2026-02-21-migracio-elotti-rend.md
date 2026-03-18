---
title: "Migráció előtt rend, különben hétfőn káosz"
date: 2026-02-21
site: elkezdodott.hu
description: "A költözés nem másolásról szól, hanem arról, hogy mi marad ki. KKV vezetőknek gyakorlati keret a biztonságos átálláshoz."
tags: ["KKV", "rendszer", "migráció"]
slug: "migracio-elotti-rend"
---

A migrációk többsége nem a másoláskor bukik el, hanem utána, amikor kiderül, hogy kimaradt egy cron, egy jogosultság vagy egy visszaállási lépés. Egy 5-50 fős cégben ez gyorsan napi működési kockázat lesz. Vincze Tamás ezért mindig a költözés előtti rendrakással kezd.

A legtöbb csapat ott csúszik meg, hogy a "majd ott beállítjuk" mondatot tervnek nézi. Nem terv.

A használható minimum így néz ki:

1. Kimenő lista: mit viszünk át pontosan.
2. Visszaállási terv: ha félremegy, hogyan állunk vissza 30-60 perc alatt.
3. Operációs lista: cronok, rutinok, napi checkek külön listán.
4. Freeze pont: mihez nem nyúlunk a költözés napján.

A kényelmetlen rész: sok KKV-nál a rendszer valójában egy ember fejében él. Ez addig kényelmes, amíg az az ember elérhető. Utána drága.

Mit jelent ez neked KKV CEO-ként?  
Ha jövő héten költözöl, ne technikai listával kezdj, hanem működési listával. Először azt védd, amitől hétfő reggel elindul a céged.

> "A migráció nem projekt, hanem üzletmenet-kockázat kezelése."  
> **VT**

Kapcsolódó oldal: [Operációs stabilitás KKV-ban](https://elkezdodott.hu/operacios-stabilitas)  
Korábbi cikk: [Miért égnek el a csendes hibákban a csapatok](https://elkezdodott.hu/csendes-hibak)

## FAQ

### Mi az első jel, hogy rosszul készülünk migrációra?
Ha nincs írott visszaállási terv. Ilyenkor mindenki improvizálni fog hiba esetén.

### Mennyi előkészítés kell minimum?
Egy kicsi rendszerhez is kell 1-2 óra strukturált listaépítés. Ezt nem lehet nullára csökkenteni kockázat nélkül.

### Kell külön ember csak a dokumentációra?
Nem feltétlenül, de kell egy felelős. Felelős nélkül a dokumentáció mindig "majd később" lesz.
