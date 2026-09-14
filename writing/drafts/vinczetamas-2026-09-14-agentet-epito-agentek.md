---
id: vinczetamas-2026-09-14-agentet-epito-agentek
title: "Mikor engedjünk agentet építeni?"
slug: agentet-epito-agentek
site: vinczetamas
content_type: article
created_at: "2026-09-14"
status: draft
quality_score: 4
source_signal: /writing/research/candidates-2026-09-11.md
source: https://sierra.ai/blog/hyper-t-bench-evaluating-agents-that-build-agents
meta_description: "AI agent építés KKV-knak: mikor kell emberi kontroll, milyen kockázatot mutat a Hyper-t-bench, és mi legyen az első gyakorlatias lépés."
og_image: ""
tags:
  - AI agent
  - KKV automatizálás
  - operációs governance
  - vezetői kontroll
---

# Mikor engedjünk agentet építeni?

Egy AI agent akkor építhet másik agentet egy 5-50 fős cégnél, ha az üzleti szabály, a jóváhagyási pont és a visszamérés előbb készen van, mint maga az automatizmus. A Sierra Hyper-t-bench eredménye szerint a legerősebb önálló konfiguráció 23,9%-ot ért el, mérnöki kontextussal 82,2%-ot.

Kedden egy vezető azt kérdezte tőlem: ha már az AI meg tud írni egy ügyfélszolgálati folyamatot, akkor minek várjunk vele?

Nem türelmetlenség volt benne. Inkább fáradtság.

A cégnél három ember kezelte az ajánlatkéréseket, a szállítási módosításokat és a garanciális leveleket. Mindenki tudta, hogy sok a kézi munka. Mindenki tudta, hogy az ismétlődő válaszok idegesítőek. A vezető fejében ott volt a logikus következő lépés: építsünk egy agentet, amelyik értelmezi az ügyet, megnézi a rendelést, megfogalmazza a választ, és ha lehet, lezárja.

A kellemetlen felismerés ott kezdődött, amikor nem az volt a kérdés, hogy az AI képes-e erre.

Hanem az, hogy a cég képes-e megmondani, mikor csinálja jól.

A Sierra 2026 szeptemberében publikált Hyper-t-bench benchmarkja pontosan ezt a feszültséget teszi láthatóvá. A feladat nem egyszerű válaszadás volt. Az agentnek egy sandbox környezetben üzleti rekordokból, ügyfélinterakciókból és homályos specifikációból kellett működő ügyfélszolgálati agentet építenie. A legjobb önálló konfiguráció 23,9%-os eredményt ért el a visszatartott teszteken. Ugyanez a modellkategória, mély kontextussal rendelkező mérnökkel párosítva, 82,2%-ra jutott.

Ez nem azt jelenti, hogy az agentek használhatatlanok.

Azt jelenti, hogy a kontroll nélküli autonómia drága illúzió.

Egy 5-50 fős magyar cégben ez nagyon gyakorlati kérdés. Nem kutatási probléma, hanem hétfő reggeli működés. Ha az ügyfélszolgálati agent rosszul értelmezi a szállítási feltételt, nem egy benchmark romlik. Egy ügyfél kap rossz ígéretet. Egy kolléga visszabontja a folyamatot. A vezető pedig megint ott találja magát, ahol nem akart lenni: minden fontos döntés az ő asztalán landol.

Az AI agent építése ezért nem fejlesztési projektként indul jól, hanem operációs döntésként.

Először azt kell kimondani, mi számít jó működésnek. Például:

- 50 ezer forint alatti reklamációra javasolhat kompenzációt, de nem küldheti ki jóváhagyás nélkül.
- Címváltoztatást csak akkor kezelhet automatikusan, ha a csomag még nem került átadásra a futárnak.
- Visszatérő B2B ügyfélnél mindig ellenőriznie kell az egyedi szerződési feltételt.
- Ha a rendszer két adatforrás között eltérést talál, nem dönthet, csak feladatot nyithat.

Ez a munka unalmasabb, mint egy látványos demó.

De pontosan ez választja el a használható automatizálást a vezetői kockázattól. Az agent nem attól lesz értékes, hogy önállóan cselekszik. Attól lesz értékes, hogy a cég tudja, melyik döntési sávban engedheti cselekedni.

Vincze Tamás stratégiai AI operációs partnerként ezt a határt keresi a cégekben. Nem az a cél, hogy minél több folyamatra rákerüljön az AI címke. Az a cél, hogy a vezető ne egy újabb kiszámíthatatlan rendszert kapjon, hanem egy ellenőrizhető működési réteget.

Van egy egyszerű példa.

Egy webáruházban az agent először nem válaszolhat minden ügyféllevélre. Kezdje azzal, hogy a bejövő leveleket négy kategóriába sorolja: rendelési státusz, számlázás, reklamáció, egyéb. A következő héten csak a rendelési státusz ügyeknél készítsen válaszjavaslatot. A harmadik héten a javaslatok 20%-át ellenőrzi külön a vezető vagy az ügyfélszolgálati felelős. Csak akkor kap nagyobb mozgásteret, ha a hibák típusa ismert, és a szabályok javíthatók.

Ez lassabbnak tűnik.

Valójában gyorsabb, mert nem kell utólag bizalmat javítani.

A Hyper-t-bench egyik tanulsága pont ez: amikor az agentnek nem csak végrehajtania kell, hanem fel kell építenie a működési logikát is, a kontextus hiánya azonnal megjelenik a minőségben. Egy KKV-ban a kontextus nem dokumentációs luxus. A kontextus a cég memóriája: miért kap ez az ügyfél kivételt, melyik terméknél nem ígérünk cserét, mikor kell telefonálni email helyett, melyik döntés jogi vagy pénzügyi következményű.

A kockázat nem az, hogy az agent hibázik.

A kockázat az, hogy a hiba üzletileg értelmesnek látszik, ezért túl későn veszik észre.

Ezért a következő gyakorlati lépés nem egy nagy agent projekt. Inkább egy egyoldalas döntési térkép:

1. Melyik három ismétlődő ügytípus viszi el a legtöbb időt?
2. Ezek közül melyiknél alacsony a pénzügyi, jogi és ügyfélkapcsolati kockázat?
3. Mi az a döntés, amit az agent csak javasolhat, de nem hajthat végre?
4. Ki nézi vissza hetente a hibákat?
5. Milyen eredménynél kap nagyobb jogosultságot?

Ha erre nincs válasz, akkor az AI agent nem tehermentesíti a vezetőt. Csak gyorsabban termeli ugyanazt a bizonytalanságot.

[AI operációs rendszerek vezetőknek](/ai-operacios-rendszerek) akkor működnek jól, ha a jogosultság, a mérés és a felelősség együtt halad. Erről szólt a korábbi írás is a [helyesen megválasztott agent futtatási környezetről](/blog/hol-fusson-az-ai-agent), mert az infrastruktúra sem technikai apróság, hanem kontrollkérdés.

> VT: Az agent nem helyettesíti a vezetői ítéletet. Akkor hasznos, ha a vezetői ítélet végre rendszerként is működni kezd.

Az AI-ban nem az első önálló döntés a fordulópont, hanem az első jól körülhatárolt döntési jog.

## FAQ

### Mit jelent az, hogy agentet építő agent?

Olyan AI rendszert jelent, amely nem csak egy feladatot hajt végre, hanem egy másik működési folyamat vagy agent logikáját is megtervezi. Ez üzletileg akkor veszélyes, ha a cég szabályai, kivételei és jóváhagyási pontjai nincsenek előre tisztázva.

### Miért fontos ez egy 5-50 fős cégnek?

Ebben a méretben a legtöbb kivétel még emberek fejében él. Ha az agent ezeket nem ismeri, magabiztosan adhat rossz választ. A vezető feladata nem a teljes tiltás, hanem a döntési sávok kijelölése.

### Mi legyen az első lépés AI agent bevezetés előtt?

Érdemes egyetlen alacsony kockázatú ügytípust kiválasztani, és ott csak javaslatkészítéssel kezdeni. A heti hibavisszanézés fontosabb, mint az első automatizált válasz sebessége.

### Mikor kaphat nagyobb önállóságot egy agent?

Akkor, ha mérhetően jól teljesít egy szűk folyamatban, a hibák típusa ismert, és van emberi felelős a szabályok módosítására. Jogosultságot nem képességbemutató alapján érdemes adni, hanem visszamért működés alapján.

## Forrás

Sierra: [Hyper-t-bench: Evaluating agents that build agents](https://sierra.ai/blog/hyper-t-bench-evaluating-agents-that-build-agents), 2026. szeptember.
