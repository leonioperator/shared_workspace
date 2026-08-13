---
id: elkezdod
title: elkezdodott-2026-08-13-ai-agent-modell-routing
site: elkezdodott
content_type: article
created_at: '2026-08-13'
status: draft
updated_at: '2026-08-13T07:45:00+02:00'
---

Az AI agent költsége nem csak modelláron múlik. Egy KKV-nál sokkal fontosabb, hogy a rendszer felismerje: melyik lépéshez elég egy olcsóbb, gyorsabb modell, és mikor kell erősebb modellre váltani. A modell-routing így nem technikai finomság, hanem operációs kontroll.

## Mi történt?

Az NVIDIA 2026. augusztus 12-én bemutatta a NeMo Switchyard modell-routing megközelítést AI agent munkafolyamatokhoz. A technikai blog szerint a cél az, hogy az agent ne minden lépésnél ugyanazt a modellt használja, hanem a feladat típusa, a modellképesség, a költség és az infrastruktúra jelei alapján válasszon.

Ez azért érdekes, mert az agentek sok apró lépésből állnak: adatkinyerés, osztályozás, keresés, összefoglalás, döntési javaslat, ellenőrzés. Ezek közül nem mindegyik igényli a legerősebb modellt.

Források:

- NVIDIA Technical Blog, 2026. augusztus 12.: "Route AI Agent Workloads Across Models with NVIDIA NeMo Switchyard"  
  https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard/
- NVIDIA Blog, 2026. augusztus 12.: "NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver Faster, Smarter, More Efficient Agentic AI"  
  https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/

## Mit jelent ez egy KKV CEO-nak?

Egy KKV-nak nem az a legfontosabb kérdés, hogy "melyik a legjobb AI modell?". A jobb kérdés ez: melyik üzleti lépéshez milyen szintű AI döntés kell?

Ha minden feladatot a legerősebb modellel futtatunk, a költség gyorsan elszállhat. Ha minden feladatot az olcsó modellel futtatunk, a minőség és a megbízhatóság sérülhet. A modell-routing lényege, hogy ezt ne kézzel kelljen minden alkalommal eldönteni.

CEO szemmel ez három kontrollt jelent:

- milyen feladattípusoknál használhat olcsó modellt az agent,
- milyen esetben kell erősebb modell vagy emberi jóváhagyás,
- hol látszik utólag, melyik döntés mennyibe került és miért.

## Konkrét működési példa

Egy 40 fős szolgáltató cég inbound ajánlatkéréseket dolgoz fel. Az agent beolvassa az e-mailt, kinyeri az ügyfélnevet, iparágat, határidőt és becsült projektméretet, majd előkészít egy választervet az értékesítőnek.

A routing szabály lehet például:

1. Egyszerű adatkinyeréshez olcsó, gyors modell.
2. Duplikáció ellenőrzéshez kereső vagy adatbázis lekérdezés.
3. Ajánlatkérési szándék és sürgősség besorolásához közepes modell.
4. Nagy értékű vagy jogi kockázatú ügyfélnél erősebb modell.
5. Külső válasz elküldése előtt emberi jóváhagyás.

Így az agent nem "okosabbnak látszik", hanem kiszámíthatóbban működik. A drágább AI kapacitás oda megy, ahol üzleti kockázat vagy döntési érték van.

## Hol a korlát?

A modell-routing nem oldja meg önmagában a folyamat minőségét. Ha rossz a bemenet, hiányzik a célállapot, nincs ellenőrzési pont, vagy az agent nem tudja, mikor kell megállnia, akkor a routing csak olcsóbban futtat rossz munkát.

Tipikus kockázatok:

- nincs mérve a feladatonkénti költség,
- a routing szabály túl bonyolult és senki nem érti,
- nincs minőségi visszamérés,
- az agent túl későn kér emberi jóváhagyást,
- nincs napló arról, melyik modell milyen lépésben döntött.

KKV környezetben az első verzió legyen egyszerű. Nem kell tíz modell és bonyolult optimalizálás. Elég két vagy három út: olcsó rutinlépés, erősebb döntési lépés, emberi jóváhagyás.

## Gyakorlati következő lépés

Válassz ki egy agent folyamatot, amely legalább három ismétlődő lépésből áll. Írd mellé minden lépéshez:

- mi a bemenet,
- mi a kívánt kimenet,
- mennyi hibát tűr el a folyamat,
- kell-e külső hatás vagy ügyfélkommunikáció,
- mi történik bizonytalanság esetén.

Ezután jelöld a lépéseket három kategóriával: rutin, döntési, jóváhagyásos. A rutin mehet olcsóbb modellre. A döntési lépés kaphat erősebb modellt. A jóváhagyásos lépésnél az agent csak javaslatot készít.

Ez a legegyszerűbb modell-routing térkép. Nem technológiai projektként indul, hanem költség és kontroll térképként.

## FAQ

### Kell-e egy KKV-nak saját modell-routing rendszer?

Nem feltétlenül. A legtöbb KKV-nak először elég a folyamatlépések besorolása: rutin, döntési, jóváhagyásos. Erre később lehet technikai routingot építeni.

### Mikor éri meg erősebb modellt használni?

Akkor, ha a lépés üzleti döntést, magasabb pénzügyi értéket, ügyfélkommunikációt, jogi kockázatot vagy nehezen javítható hibát érint.

### Mi az első mérőszám?

Feladatonkénti költség és javítási arány. Ha egy olcsó modell kimenetét mindig embernek kell javítania, akkor valójában nem olcsó.

### Mi legyen emberi jóváhagyásos?

Külső küldés, pénzköltés, szerződéses állítás, árajánlat, panaszkezelés és minden olyan lépés, ahol egy hiba közvetlenül ügyfélhez vagy pénzhez ér.
