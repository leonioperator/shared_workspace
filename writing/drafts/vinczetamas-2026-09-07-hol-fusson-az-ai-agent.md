---
id: vinczetamas-2026-09-07-hol-fusson-az-ai-agent
title: "Hol fusson az AI agent a cégben?"
slug: hol-fusson-az-ai-agent
site: vinczetamas
content_type: article
created_at: "2026-09-07T07:45:00+02:00"
status: draft
quality_score: 4
source: "Cursor: Run cloud agents on machines you manage, https://cursor.com/blog/self-hosted-machines"
meta_description: "Az AI agent helye vezetői döntés: saját gép, privát hálózat, kontrollpont és adatvédelmi szabály kell a KKV működéséhez."
og_image: "vinczetamas-2026-09-07-hol-fusson-az-ai-agent.png"
tags:
  - AI agent
  - KKV
  - workflow
  - governance
---

# Hol fusson az AI agent a cégben?

Az AI agent helye nem technikai apróság, hanem vezetői kontrollkérdés. Egy 5-50 fős cégnél nem elég azt nézni, mit tud az agent. Azt is ki kell mondani, hol fut, milyen adatokhoz fér hozzá, ki látja a munkáját, és mikor kell emberi jóváhagyás.

Egy cégvezető nem úgy szokott erről kérdezni, hogy "milyen infrastruktúrán futtassuk az agentet?"

Inkább így:

"Be tudjuk ezt engedni a belső rendszerbe?"

Ez a mondat sokkal pontosabb, mint elsőre látszik. Nem a szoftverről szól. Arról szól, hogy a cégnek van-e elég rendje ahhoz, hogy egy önállóan dolgozó rendszer ne csak gyors legyen, hanem kezelhető is.

A Cursor friss bejelentése szerint a cloud agentek már a cég által kezelt gépeken is futhatnak, dinamikusan ütemezett géppoolokban, akár privát hálózaton belül. A Cursor leírása szerint ez akkor hasznos, ha az agentnek belső szolgáltatásokat, saját build-környezetet, verziókezelést vagy nehezen csomagolható rendszereket kell elérnie.

Forrás: [Cursor - Run cloud agents on machines you manage](https://cursor.com/blog/self-hosted-machines)

Ez első ránézésre fejlesztői hír.

Valójában vezetői hír is.

Mert amint az AI agent nem csak egy böngészőben válaszol, hanem belép a cég működésébe, megváltozik a kérdés. Onnantól nem az a fő téma, hogy milyen okos. Hanem az, hogy milyen környezetben dolgozik.

## A gyors agent nem mindig a jó agent

Képzeljünk el egy 25 fős szolgáltató céget.

Van egy belső ajánlatkészítő rendszerük, egy projektkövető táblájuk, néhány automatizált riportjuk és egy ügyfélkommunikációs sablonrendszerük. A vezető azt szeretné, hogy egy AI agent segítsen rendbe tenni a heti operációs riportot: nézze meg a nyitott ajánlatokat, gyűjtse össze a késéseket, és készítsen vezetői összefoglalót.

Ez papíron tökéletes AI feladat.

Csakhogy a valóságban az agentnek érzékeny adatokhoz kell nyúlnia. Ügyfélnevekhez. Ajánlati összegekhez. Belső megjegyzésekhez. Kollégák teljesítményével kapcsolatos információkhoz.

Ilyenkor a "használjunk AI-t" mondat már kevés.

A vezetőnek azt kell eldöntenie, hogy az agent milyen határok között dolgozhat. Elég egy külső cloud környezet? Kell privát hálózati hozzáférés? Legyen külön tesztadat? Milyen napló marad a műveletekről? Ki tudja visszanézni, mit olvasott és mit módosított?

A kényelmetlen felismerés ez: sok KKV nem az AI képességeire nincs felkészülve, hanem arra, hogy az AI végre láthatóvá teszi a saját hozzáférési káoszát.

Ha ma senki nem tudja pontosan, melyik kolléga milyen táblához fér hozzá, akkor egy agent bevezetése nem automatizálási projektként indul. Jogosultsági tükörként.

## Az infrastruktúra is döntési rend

Vincze Tamás stratégiai AI operációs partnerként ezért nem azzal kezdené egy ilyen projektet, hogy melyik agent platform a legizgalmasabb. Hanem azzal, hogy milyen adatkörbe léphet be az agent az első héten.

Egy 5-50 fős cégben az első agent környezet lehet nagyon egyszerű.

Például:

- csak olvasási jogosultság a projektlistához
- külön export az ajánlatokról, ügyféladat nélkül
- emberi jóváhagyás minden külső üzenet előtt
- naplózott futás minden heti riportkészítésnél
- tiltott hozzáférés pénzügyi döntésekhez és szerződésmódosításhoz

Ez nem lassítás. Ez munkarend.

Az agent akkor lesz vezetői eszköz, ha nem kell minden egyes használatnál újra azon gondolkodni, hogy "vajon ezt szabad-e neki?" A jó szabály nem elveszi a sebességet, hanem megteremti azt a teret, ahol a sebesség nem válik kockázattá.

> **VT:** Az AI agent nem attól válik üzleti eszközzé, hogy hozzáfér mindenhova. Hanem attól, hogy pontosan tudjuk, hova nem férhet hozzá.

## Egy konkrét működési példa

Tegyük fel, hogy a cég heti vezetői riportot akar automatizálni.

Rossz első lépés: az agent kapjon hozzáférést minden belső rendszerhez, és "rakjon össze valami hasznosat".

Jobb első lépés: az agent csak három forrást kap.

Az első a nyitott ajánlatok listája. A második a futó projektek státusza. A harmadik a lejárt belső feladatok exportja. Mindhárom olvasási joggal. Az agent feladata nem döntés, hanem előkészítés: készítsen egy heti vezetői összefoglalót arról, hol van elakadás, hol hiányzik felelős, és melyik ügyfélfolyamatnál kell vezetői figyelem.

A kimenet nem megy ki ügyfélnek. Nem módosít státuszt. Nem ír át határidőt. Nem küld automatikus figyelmeztetést kollégának.

Csak megmutatja, hol kell dönteni.

Ez már hasznos. És közben kontrollálható.

Két hét után lehet bővíteni: az agent készíthet belső feladatjavaslatot. Négy hét után előkészíthet ügyfél-email piszkozatot. De a jóváhagyási pont maradjon ott, ahol üzleti vállalás születik.

## A korlát, amit nem lehet megspórolni

A saját gépen vagy privát hálózaton futó agent sem old meg mindent.

Sőt, hamis biztonságérzetet is adhat. Attól, hogy valami "házon belül" fut, még lehet rosszul naplózott, túl széles jogosultságú vagy rosszul felügyelt. A belső infrastruktúra nem helyettesíti a döntési szabályt.

Ez különösen fontos KKV-kban, ahol sok rendszer organikusan nőtt össze. Egy közös drive, néhány táblázat, régi CRM, félhivatalos riportok, kollégák saját mappái. Ha az agent ebbe belép, akkor nem csak adatot olvas. A cég működési rendezetlenségével találkozik.

A gyakorlati következő lépés ezért nem egy nagy platformváltás.

Írj össze egyetlen agent feladatot, amely valódi vezetői terhet vesz le. Például heti elakadásriport, ajánlatkövetési összefoglaló vagy belső ticket-rendezés.

Utána válaszolj négy kérdésre:

1. Melyik három adatforrás kell hozzá tényleg?
2. Ezek közül melyik tartalmaz érzékeny üzleti vagy személyes adatot?
3. Mit tehet az agent önállóan, és mit csak piszkozatként?
4. Ki nézi vissza az első három futás eredményét?

Ha erre nincs válasz, akkor még nem agentet kell választani. Először a működési határt kell megrajzolni.

Belső összefüggésben ez ugyanoda tartozik, mint a [kontrollált AI operátor KKV-k számára](/kontrollalt-ai-operator-kkv/) gondolata: az érték nem az önállóságból jön, hanem a jól beállított önállóságból. Korábbi cikkben ugyanez jelent meg a [scope-fék AI agent projektekben](/scope-fek-ai-agent-projektekben/) kapcsán is, ahol a túl gyors építés csak akkor lett hasznos, amikor vezetői határt kapott.

Az AI agent helye végső soron nem szerveroldali kérdés, hanem bizalmi térkép: megmutatja, hol van rend a cégben, és hol csak megszokás tartja össze a működést.

## FAQ

### Miért fontos, hol fut az AI agent?

Azért, mert a futtatási hely meghatározza, milyen rendszerekhez, adatokhoz és műveletekhez fér hozzá. Egy KKV-ban ez közvetlenül érinti az ügyféladatokat, pénzügyi információkat és belső döntési folyamatokat.

### Mikor érdemes saját gépen vagy privát hálózaton futtatni az agentet?

Akkor, ha az agentnek belső rendszereket, saját fejlesztői környezetet vagy érzékeny adatokat kell elérnie. Ez csak akkor jó döntés, ha mellette világos jogosultság, naplózás és jóváhagyási rend is van.

### Mi legyen az első agent feladat egy 5-50 fős cégnél?

Olyan feladat, amely olvasási joggal is értéket ad. Például heti elakadásriport, nyitott ajánlatok összefoglalása vagy lejárt belső feladatok rendezése. Az első verzió ne módosítson ügyféladatot és ne küldjön külső üzenetet.

### Mi a legnagyobb kockázat a belső agent hozzáférésnél?

Az, hogy az agent túl széles jogosultságot kap, mert a cégben eleve nincsenek pontos hozzáférési szabályok. Ilyenkor az AI nem rendet teremt, hanem felnagyítja a meglévő rendezetlenséget.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Hol fusson az AI agent a cégben?",
      "description": "Az AI agent helye vezetői döntés: saját gép, privát hálózat, kontrollpont és adatvédelmi szabály kell a KKV működéséhez.",
      "author": {
        "@type": "Person",
        "name": "Vincze Tamás"
      },
      "datePublished": "2026-09-07",
      "dateModified": "2026-09-07",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://vinczetamas.hu/hol-fusson-az-ai-agent/"
      },
      "image": "https://vinczetamas.hu/wp-content/uploads/vinczetamas-2026-09-07-hol-fusson-az-ai-agent.png"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Miért fontos, hol fut az AI agent?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Azért, mert a futtatási hely meghatározza, milyen rendszerekhez, adatokhoz és műveletekhez fér hozzá. Egy KKV-ban ez közvetlenül érinti az ügyféladatokat, pénzügyi információkat és belső döntési folyamatokat."
          }
        },
        {
          "@type": "Question",
          "name": "Mikor érdemes saját gépen vagy privát hálózaton futtatni az agentet?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Akkor, ha az agentnek belső rendszereket, saját fejlesztői környezetet vagy érzékeny adatokat kell elérnie. Ez csak akkor jó döntés, ha mellette világos jogosultság, naplózás és jóváhagyási rend is van."
          }
        },
        {
          "@type": "Question",
          "name": "Mi legyen az első agent feladat egy 5-50 fős cégnél?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Olyan feladat, amely olvasási joggal is értéket ad. Például heti elakadásriport, nyitott ajánlatok összefoglalása vagy lejárt belső feladatok rendezése. Az első verzió ne módosítson ügyféladatot és ne küldjön külső üzenetet."
          }
        }
      ]
    }
  ]
}
```
