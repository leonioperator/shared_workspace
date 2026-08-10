---
title: "Mikor van kész egy AI agent munkája?"
slug: "ai-agent-kesz-van"
site: "vinczetamas"
content_type: "article"
status: "draft"
created_at: "2026-08-10T07:45:00+02:00"
updated_at: "2026-08-10T07:45:00+02:00"
author: "Vincze Tamás"
meta_description: "KKV vezetőknek az AI agent akkor hasznos, ha pontos kész állapota, ellenőrzése és átadási szabálya van."
og_image: "vinczetamas-2026-08-10-ai-agent-kesz-van.png"
category: "AI operáció"
tags:
  - "AI agent"
  - "KKV automatizálás"
  - "operációs kontroll"
quality_score: 5
sources:
  - "TLDR AI, 2026-08-08 hírlevél, agent loop konvergencia téma"
  - "Ben's Bites, 2026-08-08 hírlevél, hosszú agent futások és stop condition példa"
---

# Mikor van kész egy AI agent munkája?

Egy AI agent nem attól hasznos, hogy sokáig dolgozik, hanem attól, hogy felismerhetően kész állapotba jut. Egy 5-50 fős cégben ezért minden agent feladathoz kell célállapot, ellenőrzési lista, stop szabály és emberi átadás. Enélkül az automatizálás csak udvariasan futó bizonytalanság.

Kedden egy cégvezető azt mondta nekem: "Azt szeretném, ha végre nem nekem kellene minden ajánlatot, emailt és riportot utánanéznem."

Teljesen érthető mondat volt. Egy 5-50 fős cégben a vezető gyakran nem azért fárad el, mert túl sok döntést hoz, hanem mert túl sok félkész dolgot kell fejben tartania. Egy ajánlat elindult, de még nincs validálva. Egy ügyfélemlékeztető elkészült, de nem tudni, elment-e. Egy heti riport megszületett, de senki nem meri kimondani, hogy használható.

Az AI agent ígérete pont itt csábító. Majd ő végigviszi. Majd dolgozik a háttérben. Majd leveszi a terhet.

A kényelmetlen felismerés az, hogy egy rosszul definiált agent nem leveszi a terhet, hanem láthatatlanná teszi.

## A legtöbb agent nem hibázik látványosan

Az agentekkel kapcsolatos vezetői félelem gyakran az, hogy "elszabadulnak". Rossz emailt küldenek, rossz adatot módosítanak, rossz döntést hoznak.

Ez létező kockázat, de a hétköznapi probléma sokkal unalmasabb. Az agent dolgozik, tokeneket használ, fájlokat nyit meg, válaszokat fogalmaz, majd visszaad valamit, ami első ránézésre majdnem jó.

És ekkor a vezető ugyanott áll, mint előtte.

Meg kell néznie, tényleg kész van-e. Ellenőriznie kell, nem maradt-e ki egy fontos feltétel. El kell döntenie, elküldhető-e, átadható-e, számlázható-e, vagy még csak vázlat.

Ilyenkor nem az AI minősége a fő kérdés. Hanem az operációs kontroll.

A TLDR AI 2026. augusztus 8-i hírlevele az agent loop konvergencia problémáját emelte ki: honnan tudjuk, hogy egy agent nem csak dolgozik, hanem közeledik a kész állapothoz. A Ben's Bites ugyanazon a napon konkrét példákon keresztül mutatta meg, hogyan tud egy agent futása időben és tokenben elnyúlni, ha nincs tervreview, teszt és stop condition.

Ez nem kutatói finomság. Ez KKV vezetői kérdés.

## A "dolgozz rajta" nem feladat

Egy embernél néha működik a laza utasítás, mert van közös múlt, rutin és kimondatlan üzleti érzék. Egy kolléga tudja, mit jelent az, hogy "Tamás ezt nem fogja kiengedni így". Egy agent nem biztos, hogy tudja.

Ha azt kapja, hogy "nézd át az ajánlatot", akkor sok mindent csinálhat.

Kijavíthatja a helyesírást. Átfogalmazhatja udvariasabbra. Ellenőrizheti, hogy szerepel-e benne minden csomag. Összevetheti a CRM-ben lévő ügyféligénnyel. Megnézheti, hiányzik-e az ár, a határidő vagy a felelős. Ezek közül több hasznos, de nem ugyanaz a munka.

Egy működő agent feladat így kezdődik:

"Az ajánlat akkor kész, ha minden tételhez tartozik ár, határidő, felelős, elfogadási feltétel és következő lépés. Ha bármelyik hiányzik, ne küldd el. Készíts hiánylistát, és add vissza emberi döntésre."

Ez nem szebb prompt. Ez vezetői kontroll.

## Konkrét működési példa

Vegyünk egy egyszerű KKV helyzetet. Egy cég hetente 15-20 érdeklődő emailt kap. A vezető szeretné, ha az AI agent előkészítené a válaszokat, és csak a fontos ügyek kerülnének elé.

Rossz feladat:

"Válaszolj az érdeklődőknek."

Működő feladat:

"Osztályozd az új érdeklődéseket három kategóriába: sürgős értékesítési lehetőség, normál válasz, nem releváns megkeresés. Sürgős, ha konkrét igény, határidő és döntéshozói jel van benne. Normál válaszhoz készíts vázlatot, de ne küldd el. Nem releváns megkeresésnél csak címkézz. Ha árkedvezményt, szerződéses feltételt vagy panaszt érint a levél, állj meg és add át embernek."

Itt már van kész állapot. Van ellenőrzés. Van kockázati határ. Van emberi átadás.

Az agent nem "segít valamiben". Egy jól körülhatárolt operációs lépést végez.

## A korlát nem technikai szégyen

Sok vezető azért nem vezeti be jól az automatizálást, mert túl sokat vár az első verziótól. Azt gondolja, akkor éri meg, ha az agent elejétől végéig önállóan dolgozik.

Pedig a legtöbb cégnél az első érték nem a teljes autonómia. Hanem az, hogy a vezető elé már nem nyers káosz kerül, hanem rendezett döntési helyzet.

Egy agent első verziója nyugodtan lehet ilyen:

- összegyűjti a hiányzó adatokat,
- jelzi a bizonytalan pontokat,
- előkészíti a válaszvázlatot,
- megmutatja, mi alapján döntött,
- megáll, ha pénz, jogi kockázat vagy ügyfélpanasz kerül elő.

Ez már érdemi tehercsökkentés. Nem látványos demó, hanem jobb hétfő reggel.

Vincze Tamás stratégiai AI operációs partnerként ezért nem azzal kezdené egy 5-50 fős cégnél, hogy "melyik modell legyen". A kérdés előbb ez: melyik munkafolyamatnál tudjuk pontosan megmondani, mit jelent a kész?

> **VT signature:** Az AI agent értéke nem a futási időben van, hanem abban, hogy a vezetőnek kevesebb félkész állapotot kell fejben tartania.

## Gyakorlati következő lépés

Válassz ki egy ismétlődő, de nem életveszélyes folyamatot. Például érdeklődő emailek előszűrése, heti vezetői riport előkészítése, ajánlatok hiányellenőrzése vagy meeting jegyzetekből feladatlista készítése.

Írj hozzá négy sort:

1. Mi a kész állapot?
2. Mit kell ellenőrizni?
3. Mikor kell megállni?
4. Mikor kell embernek átadni?

Ha erre a négy kérdésre nem tudsz válaszolni, akkor még nem agent feladatod van. Csak egy reményed, hogy a rendszer majd kitalálja helyetted.

Belső háttérként érdemes összekötni ezt a [stratégiai AI operációs partner szemlélettel](/strategiai-ai-operacios-partner/) és a korábbi [AI agent nem modell, hanem működési felelősség](/ai-agent-nem-modell/) gondolattal. A technológia csak akkor lesz vezetői eszköz, ha a működésben is van helye.

A jó automatizálás nem helyetted gondolkodik, hanem megmutatja, hol kell még döntened.

## FAQ

### Mit jelent az, hogy egy AI agent kész állapotba jut?

Azt jelenti, hogy előre meghatározott feltételek alapján eldönthető: a feladat befejeződött, hiányos, hibás vagy emberi döntést igényel. Kész állapot nélkül az agent eredménye minden alkalommal újabb vezetői ellenőrzést kér.

### Miért fontos a stop szabály egy KKV automatizálásban?

Mert a KKV-ban kevés a tartalék figyelem és pénz. Ha egy agent bizonytalan helyzetben tovább dolgozik, könnyen időt, tokent és vezetői bizalmat éget el. A stop szabály azt mondja meg, mikor kell megállni és átadni a feladatot.

### Milyen folyamatot érdemes elsőként agentre bízni?

Olyat, amely gyakori, szabályai részben leírhatók, de a végső döntés még maradhat embernél. Jó első jelölt az email előszűrés, riport előkészítés, ajánlat hiányellenőrzés vagy meeting utáni feladatlista.

### Kell mindig a legerősebb modell egy agent feladathoz?

Nem. Sok operációs feladatnál a pontos folyamatleírás, a jó ellenőrzési pont és az átadási szabály többet számít, mint a legerősebb modell. A modellválasztás költségkérdés is, nem presztízskérdés.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Mikor van kész egy AI agent munkája?",
      "author": {
        "@type": "Person",
        "name": "Vincze Tamás"
      },
      "datePublished": "2026-08-10",
      "dateModified": "2026-08-10",
      "description": "KKV vezetőknek az AI agent akkor hasznos, ha pontos kész állapota, ellenőrzése és átadási szabálya van.",
      "image": "vinczetamas-2026-08-10-ai-agent-kesz-van.png"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Mit jelent az, hogy egy AI agent kész állapotba jut?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Azt jelenti, hogy előre meghatározott feltételek alapján eldönthető: a feladat befejeződött, hiányos, hibás vagy emberi döntést igényel."
          }
        },
        {
          "@type": "Question",
          "name": "Miért fontos a stop szabály egy KKV automatizálásban?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Mert bizonytalan helyzetben az agent könnyen időt, tokent és vezetői bizalmat éget el. A stop szabály azt mondja meg, mikor kell megállni és átadni a feladatot."
          }
        },
        {
          "@type": "Question",
          "name": "Milyen folyamatot érdemes elsőként agentre bízni?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Olyat, amely gyakori, szabályai részben leírhatók, de a végső döntés még maradhat embernél. Jó első jelölt az email előszűrés, riport előkészítés vagy ajánlat hiányellenőrzés."
          }
        }
      ]
    }
  ]
}
</script>
```
