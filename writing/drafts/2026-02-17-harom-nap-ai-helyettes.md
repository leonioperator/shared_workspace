---
title: Három nap alatt felépítettünk egy AI helyettest. Ez történt valójában.
date: 2026-02-17
description: Hogyan épül fel egy AI operatív asszisztens a nulláról, egy valós VPS-en,
  valós feladatokkal? Három nap krónikája, hibákkal együtt.
tags:
- AI asszisztens
- operáció
- automatizálás
- KKV
- Navibase
category: AI az operációban
status: draft
site: vinczetamas
id: 2026-02-
content_type: article
created_at: '2026-05-25'
updated_at: '2026-05-25T11:25:40.403146+00:00'
---

Képzelje el, hogy három nap alatt egy működő mesterséges intelligencia asszisztenst épít fel, méghozzá a nulláról. Nem elméletben, hanem egy valós szerveren, valós üzleti kihívásokra optimalizálva. Pontosan ez történt, és most megosztom Önnel a kulcsfontosságú tanulságokat.

## Vasárnap: A Leoni Projekt indulása

Február 15-én egy üres VPS-sel indultunk. Csupán egy friss Ubuntu rendszer várt ránk. Estére azonban az AI asszisztensünk, Leoni – ahogy elneveztük – már képes volt e-maileket kezelni, GitHub repókat menedzselni, feladatokat követni egy Kanban táblán, sőt, három különböző hangon kommunikálni.  

Egyetlen nap alatt beüzemeltük az e-mail klienst (himalaya), a GitHub alapú kollaborációs felületet, egy Kanban táblát, egy token-költség elemző felületet, és három hangklónt (Tomi, Évi, Leoni hangjával). Ezen felül a teljes WordPress menedzsmentet is kiépítettük WP-CLI és MainWP segítségével.

Ez mind leírva egyszerűnek tűnik, de korántsem volt az.

Az első stratégiai döntés rögtön a projekt elején született: melyik AI modellt válasszuk. Az Opus, bár kiválóan teljesített a komplex feladatokban, token költségei fenntarthatatlanok lettek volna napi szinten. Átváltottunk a költséghatékonyabb Sonnet modellre, amely a legtöbb operatív feladathoz tökéletesen elegendő. Ez nem technikai, hanem egyértelműen üzleti döntés volt, már az első napon.

## Hétfő: Az első nehézségek és tanulságok

Hétfőn jöttek az igazi üzleti kihívások. A hanghívás integráció (Twilio) beállítása során kiderült, hogy Leoni automatikus „szívverés” jelzése, amely a működőképességet ellenőrzi, túlzottan agresszív volt. Ez nemcsak zavarta a munkát, hanem feleslegesen égette a tokeneket, ami közvetlen költséget jelentett.

A hírlevél rendszerünk (elkezdodott.hu) sem úgy teljesített, ahogy elvártuk. Az előfizetési folyamatban apró, ám bosszantó hibák merültek fel. Ezek nem rendszerösszeomlást okozó problémák voltak, hanem olyan finom részletek, amelyeket egy ember ösztönösen kezelne, de egy AI-nak pontosan meg kell határozni.

Ez a pont kristálytisztán megmutatta a munkamegosztás lényegét: az ember – ez esetben Tomi – a stratégiát és a miérteket határozza meg. Leoni végrehajtja, jelzi, ha elakad, és dokumentálja a tanultakat. Az AI nem hoz stratégiai döntéseket. Az ember dönt, az AI pedig gyorsan és precízen végrehajtja, miközben a hibák is azonnal kiderülnek.

## Kedd: Optimalizálás és költséghatékonyság

A harmadik napon már nem az volt a kérdés, hogy „működik-e a rendszer”, hanem hogy „mennyibe kerül, és mennyire hatékony az üzleti folyamatokban”. A token költségek optimalizálása vált a fő prioritássá. Cache konfigurációval és intelligensebb lekérdezésekkel jelentősen csökkenteni tudtuk a napi üzemeltetési költségeket.

A hírlevél folyamat is letisztult: előfizetési rendszer, automatikus válaszok, szegmentálás. Ezek a háttérben zajló folyamatok nem látványosak, de egy KKV számára kulcsfontosságúak. Éppen ezek azok a feladatok, amelyek gyakran a vezető asztalán landolnak.

## Munkamegosztás: Ember és AI szinergiája

**Tomi, az ember:** stratégiai döntések, architektúra tervezés, folyamatok ellenőrzése, jóváhagyás, és ügyfélkapcsolatok kezelése. Mindaz, amihez ítélőképesség, szélesebb kontextus és emberi interakció szükséges.

**Leoni, az AI:** precíz végrehajtás, folyamatos monitorozás, dokumentáció, rendszerkarbantartás és szövegvázlatok készítése. Az ismétlődő, precíz munkák, amelyek éjjel-nappal futhatnak, fáradhatatlanul.

A lényeg nem Leoni intelligenciája, hanem az, hogy az emberi idő felszabadul a stratégiai feladatokra. Az operatív terhek nagy részét egy megbízható „munkatárs” veszi át, aki nem felejt el, nem fárad el, és nem sértődik meg, ha éjfélkor kap feladatot.

## Három nap legfontosabb tanulságai

**A költség nem technikai, hanem üzleti kérdés.** A modellválasztás, a cache stratégia, a „szívverés” frekvenciája – mindez pénz. Ha az első héten nem figyelünk rá, a hónap végén kellemetlen meglepetések érhetnek bennünket.

**Az AI nem gondolkodik helyettünk.** Végrehajt. Gyorsan, megbízhatóan. De a minőség a bemeneti instrukcióktól függ. Az ember felelőssége a pontos és érthető utasítások megfogalmazása.

**A hibák aranyat érnek.** A „szívverés” túl agresszív volt? Most már tudjuk, mi az optimális beállítás. A hírlevél folyamatban volt hiba? Most már pontosan tudjuk, hol kell részletesebb instrukciókat adni. Három nap hibáiból sokkal több tanulságot vontunk le, mint három hónap tervezésből.

**Ne várjuk a tökéletességet az első naptól.** Vasárnap elindult a rendszer. Hétfőn finomítottunk rajta. Kedden optimalizáltunk. Ez a normális működési modell. Aki a tökéletes indulásra vár, az soha nem fog elindulni.

Ez a Navibase projekt kezdeti fázisa, nem a vége. Három nap után van egy működő AI asszisztensünk, amely e-maileket kezel, feladatokat követ, hírlevelet épít, és mindent dokumentál. Nem azért, mert az AI varázslatos, hanem mert lépésről lépésre, tudatosan felépítettük.

---

## Gyakran Ismételt Kérdések

**Mennyibe kerül egy ilyen AI asszisztens üzemeltetése?**
A költség nagyban függ a választott AI modelltől és a használat intenzitásától. Nálunk a Sonnet modellre váltás és a cache optimalizálás után a napi költség elfogadható szintre csökkent. A pontos összegeket a projekt előrehaladtával fogjuk megosztani.

**Szükséges hozzá programozói tudás?**
Az alaprendszer felépítéséhez technikai háttér szükséges, de a napi használathoz egyre kevésbé. A cél az, hogy a vezető természetes nyelven kommunikáljon az asszisztenssel, ne pedig kódot írjon.

**Alkalmas ez 5-50 fős cégek számára?**
Igen, sőt. Különösen az 5-50 fős cégeknek van rá a legnagyobb szükségük, ahol nincs dedikált operatív csapat, és a vezetőre hárul az adminisztratív terhek nagy része. Vincze Tamás éppen erre a szegmensre építi a Navibase szolgáltatást.

---

*Meta description:* Három nap alatt felépítettünk egy AI operatív asszisztenst a nulláról. E-mail, Kanban, hírlevél, hangklónok, valós hibákkal. Ez történt.

*Javasolt tagek:* AI asszisztens, operáció, automatizálás, KKV, Navibase, AI operáció, VPS, Leoni, Vincze Tamás
