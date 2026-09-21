---
id: vinczetamas-2026-09-21-agent-futtatasi-fegyelem
title: "Hol dolgozzon az AI agent?"
site: vinczetamas
content_type: article
status: draft
created_at: "2026-09-21"
updated_at: "2026-09-21T07:45:00+02:00"
slug: agent-futtatasi-fegyelem
quality_score: 4
source_signal: /writing/research/candidates-2026-09-18.md
source: https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke
meta_description: "Az AI agent értéke nem ott dől el, hogy milyen okos, hanem ott, hogy kontrollált környezetben dolgozik-e a cég folyamataiban."
og_image: ""
tags:
  - AI agent
  - KKV automatizalas
  - governance
  - workflow
---

# Hol dolgozzon az AI agent?

Az AI agent akkor válik üzleti eszközzé, amikor nem csak feladatot kap, hanem ellenőrzött munkateret is. Egy 5-50 fős cégben nem az a fő kérdés, hogy az agent tud-e levelet írni vagy adatot rendezni. Hanem az, hogy hol fut, mit érhet el, és ki látja, ha elakad.

Kedden egy vezetővel arról beszéltünk, miért nem mer még több operációs feladatot átadni az AI-nak.

Nem az ötlettel volt baja. Pontosan látta, hogy a heti riportok, ügyfélválasz-vázlatok, ajánlat-előkészítések és CRM-frissítések jelentős része nem igényelne vezetői figyelmet. A baj azzal volt, ami a mondat végén jött.

"De ha ezt tényleg rábízom, hol fog ez dolgozni?"

Ez elsőre technikai kérdésnek hangzik. Szerver, böngésző, API, felhő, jogosultság. Valójában vezetői kérdés.

Mert amikor egy AI agent belép a cég működésébe, nem egy új szoftvert veszünk fel a listára. Egy új végrehajtó szereplőt engedünk be az operációba. Olyat, amelyik olvas, döntési javaslatot készít, rendszerek között mozog, néha hibázik, néha megáll, néha pedig túl magabiztosan halad tovább.

A Google Cloud szeptemberi bejelentése, az Agent Substrate GKE-n, pont erre a pontra mutat rá. A közlemény szerint a Substrate célja, hogy agentek izolált, gyorsan indítható környezetben fussanak, sub-500 ms resume műveletekkel és zero-trust kernel, illetve hálózati izolációval. Ez nagyvállalati infrastruktúra-nyelv, de a mögötte lévő üzleti kérdés nagyon KKV-kompatibilis.

Ha az agent dolgozik, ki védi meg a céget az agent saját hibáitól?

## A kényelmetlen felismerés

A legtöbb cég nem azért kockázatosan automatizál, mert túl bátor. Hanem azért, mert nincs különbség a kísérlet és az éles működés között.

Valaki kipróbál egy agentet egy böngészőben. Aztán ugyanazzal a lendülettel hozzáadja a Gmailt, a Drive-ot, a CRM-et, majd kéri, hogy "készítsd elő a holnapi ügyfélanyagokat". Papíron ez gyorsítás. A valóságban kontroll nélküli hozzáférési lánc.

Egy 12 fős szolgáltató cégnél ez egészen hétköznapi módon tud félremenni. Az agent kap egy feladatot: nézze át a bejövő ajánlatkéréseket, keresse ki a kapcsolódó korábbi anyagokat, és készítsen válaszvázlatot. Ez hasznos. De ha ugyanaz az agent látja a teljes ügyfélmappát, a belső árképzési jegyzeteket és a félkész szerződésmintákat is, akkor már nem automatizálásról beszélünk, hanem túl széles működési jogkörről.

A vezető ilyenkor érzi, hogy valami nem stimmel, csak gyakran rossz helyen keresi a választ. Nem jobb prompt kell először. Nem még okosabb modell. Hanem munkakörnyezet.

## Az agentnek nem bizalom kell, hanem keret

Vincze Tamás stratégiai AI operációs partnerként pont ott szokott megállni egy bevezetésben, ahol a lelkes automatizálási beszélgetések túl gyorsan továbbmennének.

Mit láthat az agent?

Mit módosíthat?

Mikor kell megállnia?

Milyen napló marad utána?

Ki tudja visszakeresni, milyen döntési úton jutott el egy javaslatig?

Ezek nem informatikai apróságok. Ezek vezetői kontrollpontok. Ha nincsenek kimondva, akkor az AI agent valójában a vezető fejében lévő határokat próbálja kitalálni. Ez nem fair a rendszerrel szemben, és nem biztonságos a céggel szemben.

Az Agent Substrate-ről szóló Google Cloud anyag azért érdekes, mert az agent futtatását nem mellékes infrastruktúra-problémaként kezeli. A futtatási környezet maga a governance része. Izoláció, gyors visszaállás, külön futási tér, hálózati kontroll. Ezek mind ugyanarra a vezetői mondatra fordíthatók le:

> VT: Ami önállóan dolgozik, annak legyen saját munkaterülete, saját határa és saját fékje.

## Egy működési példa

Vegyünk egy 20 fős B2B céget, ahol az értékesítő csapat minden pénteken összerakja a következő heti follow-up listát.

A régi működésben a vezető belenéz a CRM-be, megkérdezi az értékesítőket, átfutja az e-maileket, majd fejben rangsorol. Ami sürgősnek tűnik, előre kerül. Ami csendes, de fontos, gyakran elmarad.

Az agent erre jó jelölt lenne. Péntek reggel átnézi az elmúlt hét CRM-aktivitását, jelzi a nyitott ajánlatokat, kiemeli azokat az ügyfeleket, ahol három napja nincs válasz, és előkészít egy follow-up listát. Nem küld e-mailt. Nem módosít árat. Nem ír át státuszt. Csak javaslatot készít.

Ehhez viszont nem általános vállalati hozzáférést kap. Csak a CRM meghatározott nézeteit, csak olvasási jogot, csak a szükséges ügyfélmezőket, és egy külön naplóba írja, miből dolgozott. Ha bizonytalan, például két ellentmondó státuszt talál, nem dönt. Jelzi, hogy emberi ellenőrzés kell.

Ez a különbség a "használjunk AI-t" és az operációsan vállalható automatizálás között.

Az első demóban látványos. A második hétfőn is működik.

## A korlát, amit nem érdemes szépíteni

Az izolált futtatás nem old meg mindent. Attól, hogy egy agent kontrollált környezetben dolgozik, még lehet rossz a feladatleírás, hiányos az adat, gyenge az ellenőrzési pont, vagy túl nagy az üzleti elvárás.

Sőt, van egy kellemetlenebb kockázat is. A technikai kontroll hamis nyugalmat adhat. A vezető azt látja, hogy van sandbox, jogosultság, naplózás, limit. Ettől még az agent rossz következtetést vonhat le egy rosszul karbantartott CRM-ből.

Ezért az első érett lépés nem az, hogy minden workflow-ba agentet teszünk. Hanem az, hogy kiválasztunk egy szűk, jól mérhető, visszafordítható folyamatot.

Például:

- heti follow-up lista előkészítése,
- bejövő ajánlatkérések előszűrése,
- számlázási eltérések jelzése,
- ügyfélmeetingekből feladatlista készítése.

Ezeknél a haszon konkrét, a kár korlátozható, az ellenőrzés pedig beépíthető.

## A következő lépés

Egy 5-50 fős cégnek nem azzal érdemes kezdenie, hogy "milyen AI agent platformot vegyünk". A jobb kérdés ez:

Melyik az a heti visszatérő döntés-előkészítő munka, ahol az agent csak javasol, de nem véglegesít?

Ha ez megvan, jöhet a futtatási tér megtervezése. Milyen adatok kellenek? Mi legyen csak olvasható? Mi legyen tiltott? Hol álljon meg az agent? Ki nézi át az eredményt? Milyen napló alapján lehet visszakeresni, mi történt?

Innen már nem hit kérdése az AI. Működési kérdés.

A korábbi cikkben írtam arról, hogy [hol fusson az AI agent egy KKV-ban](/hol-fusson-az-ai-agent/). Ez a mostani téma ennek a folytatása: nem csak az számít, lokális vagy felhős-e a futás, hanem az is, mennyire van körülhatárolva az agent munkatere. A stratégiai háttérhez érdemes külön végiggondolni az [AI operációs audit](/ai-operacios-audit/) szerepét is, mert a jogosultság, a workflow és a felelősségi pont ugyanannak a rendszernek a része.

Az AI agent értéke nem abból látszik, hogy mennyi mindent tud megcsinálni, hanem abból, hogy mennyi mindent nem engedünk neki rossz helyen megcsinálni.

## FAQ

### Miért fontos az AI agent futtatási környezete egy KKV-ban?

Azért, mert az agent nem csak választ ad, hanem céges adatokkal és folyamatokkal dolgozik. Ha nincs külön munkatere, túl széles hozzáférést kaphat, és a hibája közvetlenül operációs kockázattá válhat.

### Elég, ha az agent csak jó promptot kap?

Nem. A jó prompt segít, de nem helyettesíti a jogosultsági határokat, a naplózást és az emberi ellenőrzési pontokat. Egy rosszul keretezett workflow-ban a jó prompt is túl nagy mozgásteret adhat.

### Milyen folyamattal érdemes kezdeni?

Olyannal, ahol az agent döntést készít elő, de nem dönt véglegesen. Jó első jelölt a heti follow-up lista, a bejövő ajánlatkérések előszűrése vagy meetingjegyzetből feladatlista készítése.

### Mit jelent a governance az AI agenteknél?

A governance azt jelenti, hogy előre meghatározzuk az agent szerepét, hozzáférését, megállási pontjait és ellenőrzését. Nem lassításról szól, hanem arról, hogy az automatizálás vezetői kontroll alatt maradjon.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Hol dolgozzon az AI agent?",
      "author": {
        "@type": "Person",
        "name": "Vincze Tamás"
      },
      "datePublished": "2026-09-21",
      "dateModified": "2026-09-21",
      "mainEntityOfPage": "/agent-futtatasi-fegyelem/",
      "description": "Az AI agent értéke nem ott dől el, hogy milyen okos, hanem ott, hogy kontrollált környezetben dolgozik-e a cég folyamataiban."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Miért fontos az AI agent futtatási környezete egy KKV-ban?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Azért, mert az agent nem csak választ ad, hanem céges adatokkal és folyamatokkal dolgozik. Ha nincs külön munkatere, túl széles hozzáférést kaphat, és a hibája közvetlenül operációs kockázattá válhat."
          }
        },
        {
          "@type": "Question",
          "name": "Elég, ha az agent csak jó promptot kap?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nem. A jó prompt segít, de nem helyettesíti a jogosultsági határokat, a naplózást és az emberi ellenőrzési pontokat."
          }
        },
        {
          "@type": "Question",
          "name": "Milyen folyamattal érdemes kezdeni?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Olyannal, ahol az agent döntést készít elő, de nem dönt véglegesen. Jó első jelölt a heti follow-up lista, a bejövő ajánlatkérések előszűrése vagy meetingjegyzetből feladatlista készítése."
          }
        }
      ]
    }
  ]
}
</script>
```
