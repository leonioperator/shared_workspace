---
title: "Három nap alatt felépítettünk egy AI helyettest. Ez történt valójában."
date: 2026-02-17
description: "Hogyan épül fel egy AI operatív asszisztens a nulláról, egy valós VPS-en, valós feladatokkal? Három nap krónikája, hibákkal együtt."
tags: ["AI asszisztens", "operáció", "automatizálás", "KKV", "Navibase"]
category: "AI az operációban"
---

Hogyan épül fel egy AI operatív asszisztens a nulláról? Nem elméletben, nem demóban, hanem egy valódi szerveren, valódi feladatokkal, valódi hibákkal. Három nap története következik, amiben egy ember és egy AI együtt próbált összerakni valamit, ami működik.

## Vasárnap: Leoni megszületik

Február 15-én, egy üres VPS-sel kezdtünk. Semmi nem volt rajta, csak egy friss Ubuntu. Este, mire abbahagytuk, az AI asszisztens - akit Leoninek hívnak - már tudott emailt olvasni, GitHubon fájlokat kezelni, feladatokat nyomon követni egy Kanban boardon, és három különböző hangon beszélni.

Számokban: egyetlen nap alatt felállt az email kliens (himalaya), a GitHub shared workspace, egy Kanban board, egy token-költség dashboard, és három voice clone (Tomi, Evi, Leoni hangjával). Plusz a teljes WordPress menedzsment WP-CLI-n és MainWP-n keresztül.

Ez így leírva simán hangzik. Nem volt az.

Az első komoly döntés rögtön az elején jött: melyik AI modellt használjuk. Az Opus (a nagyobb, drágább) remekül működött a komplex feladatokra, de a token költség az egekbe szökött. Napi szinten ez fenntarthatatlan lett volna. Átváltottunk Sonnet-re, ami olcsóbb és a legtöbb operatív feladatra pont elég. Ez nem technikai döntés volt. Ez üzleti döntés volt, az első napon.

## Hétfő: az első hibák

Hétfőn jöttek az igazi kihívások. A hanghívás (Twilio integráció) felállítása közben kiderült, hogy az automatikus szívverés-jelzés (heartbeat), amivel Leoni jelzi, hogy él és dolgozik, túl agresszív volt. Túl sűrűn jelentkezett, ami zavartta a munkát és feleslegesen égette a tokeneket.

A hírlevél rendszer (elkezdodott.hu) sem úgy viselkedett, ahogy vártuk. A feliratkozási flow-ban apró, de bosszantó hibák voltak. Nem katasztrofális dolgok, inkább olyan részletek, amiket egy ember intuitíven kezel, de egy AI-nak explicit meg kell mondani.

Ez volt az a pont, ahol elkezdett kirajzolódni a munkamegosztás. Tomi mondja meg, mit kell csinálni és miért. Leoni megcsinálja, jelzi ha elakad, és dokumentálja amit tanult. Nem az AI dönt a stratégiáról. Az ember dönt. Az AI végrehajtja, gyorsan, és ha hibázik, az is gyorsan kiderül.

## Kedd: az optimalizálás napja

A harmadik napra már nem az volt a kérdés, hogy "működik-e", hanem hogy "mennyibe kerül és mennyire hatékony". A token költség optimalizálása lett a fő téma. Cache konfigurációval és okosabb lekérdezésekkel sikerült jelentősen csökkenteni a napi költséget.

A hírlevél flow is formát öltött. Feliratkozási rendszer, automatikus válaszok, szegmentálás. Ezek nem látványos dolgok, de egy KKV számára ez az a fajta háttérmunka, amit valakinek meg kell csinálnia, és ami általában a vezető asztalán landol.

## Ki mit csinál ebben a felállásban?

Tomi, az ember: architektúra döntések, stratégia, review, jóváhagyás, ügyfélkapcsolat. A dolgok, amikhez ítélőképesség, kontextus és emberi kapcsolat kell.

Leoni, az AI: végrehajtás, monitorozás, dokumentáció, rendszerkarbantartás, draft készítés. A dolgok, amik ismétlődnek, amikhez precizitás kell, és amik éjjel-nappal futhatnak.

A lényeg nem az, hogy az AI okos. A lényeg az, hogy az ember ideje felszabadul a stratégiai munkára, mert az operatív terhek nagy részét átveszi valaki (valami), aki nem felejt el, nem fárad el, és nem sértődik meg, ha éjfélkor kap feladatot.

## Amit három nap alatt megtanultunk

**A költség nem technikai kérdés.** A modellválasztás, a cache stratégia, a heartbeat frekvencia, mind pénz. Ha nem figyelsz rá az első héten, a hónap végén meglepődsz.

**Az AI nem gondolkodik helyetted.** Végrehajt. Jól, gyorsan, megbízhatóan. De ha rossz instrukciót kap, rossz eredményt ad. Az instrukció minősége az emberen múlik.

**A hibák hasznosak.** A heartbeat túl sűrű volt? Most már tudjuk, mi az optimális. A hírlevél flow bugos volt? Most már tudjuk, hol kell explicit lenni. Három nap hibáiból több tanulság jött ki, mint három hónap tervezgetésből.

**Nem kell tökéletesnek lennie az első napon.** Vasárnap felállt a rendszer. Hétfőn javítottuk. Kedden optimalizáltuk. Ez a normális. Aki arra vár, hogy minden tökéletes legyen induláskor, az soha nem indul el.

Ez a Navibase projekt eleje. Nem a vége. Három nap után van egy működő AI asszisztens, aki emailt kezel, feladatokat nyomon követ, hírlevelet épít, és dokumentál mindent. Nem azért, mert az AI varázslatos. Azért, mert valaki leült és felépítette. Lépésről lépésre.

---

## Gyakran ismételt kérdések

**Mennyibe kerül egy ilyen AI asszisztens üzemeltetése?**
A költség nagyban függ a választott modelltől és a használat intenzitásától. Nálunk a Sonnet-re váltás és a cache optimalizálás után a napi költség elfogadható szintre csökkent. A pontos összegeket a projekt előrehaladtával fogjuk megosztani.

**Kell hozzá programozói tudás?**
Igen, a felépítéshez kell technikai háttér. De a napi használathoz egyre kevésbé. A cél pont az, hogy a vezető természetes nyelven kommunikáljon az asszisztenssel, ne kódot írjon.

**Alkalmas ez 5-50 fős cégek számára?**
Igen, sőt. Éppen az 5-50 fős cégeknek van a legnagyobb szükségük rá, mert nincs dedikált ops csapatuk, és a vezető maga végzi az operatív munkát. Vincze Tamás pont erre a szegmensre építi a Navibase szolgáltatást.

---

*Meta description:* Három nap alatt felépítettünk egy AI operatív asszisztenst a nulláról. Email, Kanban, hírlevél, voice clone, valós hibákkal. Ez történt.

*Javasolt tagek:* AI asszisztens, operáció, automatizálás, KKV, Navibase, AI operáció, VPS, Leoni, Vincze Tamás
