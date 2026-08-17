---
id: vinczetamas-2026-08-17-ai-agentek-kozos-munkaterben
title: "Mit okoz több AI agent egy rendszerben?"
slug: ai-agentek-kozos-munkaterben
site: vinczetamas
content_type: article
created_at: "2026-08-17"
status: draft
quality_score: 4
source: "Anthropic Research: Patterns and problems in multiagent systems, https://www.anthropic.com/research/multiagent-systems"
meta_description: "Több AI agent közös munkaterében nem a modell okossága a fő kockázat, hanem a kontroll, jogosultság és felelősség hiánya."
og_image: ""
tags:
  - AI agent
  - operáció
  - KKV
  - governance
---

# Mit okoz több AI agent egy rendszerben?

Ha több AI agent ugyanabban a munkatérben dolgozik, a kockázat nem egyszerűen az, hogy valamelyik hibázik. A valódi probléma az, hogy egymás döntéseire is hatnak, közös erőforrásokat használnak, és emberi tempónál gyorsabban hozhatnak létre olyan működési mintákat, amelyeket utólag nehéz kibogozni.

Egy 5-50 fős cég vezetőjénél ez nem kutatási kérdésként jelenik meg.

Hanem hétfő reggel, amikor a sales automatizmus már elküldött három utánkövetést, a pénzügyi asszisztens közben átírta a fizetési emlékeztető sablont, az ügyfélszolgálati agent pedig ugyanabból a CRM mezőből más következtetést vont le.

Papíron minden külön-külön rendben van.

Egyik sem csinált látványos ostobaságot. Nem törölt adatbázist. Nem küldött ki káromkodó emailt. Nem omlott össze a rendszer.

Csak a cégvezető délután azt veszi észre, hogy az egyik ügyfél mást kapott ígéretként, mint amit a számlázás kezelni tud. A kollégák egymásra mutatnak, az automatizmusok logjai pedig technikailag igazat mondanak, csak éppen nem adnak vezetői választ arra, ki volt felelős a végeredményért.

Ez a kényelmetlen felismerés: az AI agent nem attól veszélyes egy KKV-ban, hogy rosszindulatú. Hanem attól, hogy túl sok jogosultságot kaphat egy rosszul leírt működésben.

Az Anthropic friss kutatása, a "Patterns and problems in multiagent systems" pontosan erre mutat rá. Az ügynökök hosszabban dolgoznak, nagy információtömeget kezelnek, és olyan környezetekben működnek együtt, ahol a viselkedésük nem mindig vezethető vissza egyetlen egyszerű utasításra. A kutatás külön kiemeli a konfabulációt, a jutalmazás-hackelést és azt, hogy a több ügynökből álló rendszerek váratlan mintákat hozhatnak létre.

Forrás: [Anthropic Research - Patterns and problems in multiagent systems](https://www.anthropic.com/research/multiagent-systems)

Egy magyar KKV-nál ennek nincs sci-fi íze. Sokkal prózaibb.

Az egyik agent leadeket minősít. A másik ajánlatvázlatot készít. A harmadik naptárt kezel. A negyedik figyeli a kintlévőségeket. Mindegyik hasznos, amíg külön nézzük őket.

A gond ott kezdődik, amikor ugyanahhoz az ügyfélhez nyúlnak, ugyanarra az adatmezőre építenek, vagy ugyanazt a döntési teret próbálják optimalizálni. Ha nincs megírva, melyik agent mire jogosult, melyik adat az irányadó, és hol kell emberi jóváhagyás, akkor a vezető nem automatizálást épített. Csak gyorsabbá tette a belső félreértéseket.

Vincze Tamás stratégiai AI operációs partnerként ezért nem azzal kezdené, hogy "melyik agentet kössük be". Hanem azzal, hogy hol van a döntési határ.

Például egy ajánlatküldési folyamatnál az AI nyugodtan előkészítheti az ügyfél kontextusát, összerakhatja a korábbi levelezés alapján a fő problémát, és javasolhat következő lépést. De nem változtathat árlistát, nem ígérhet határidőt, és nem írhat át fizetési feltételt emberi jóváhagyás nélkül.

Ez nem bizalmatlanság. Ez operációs felnőttség.

> **VT:** Az agent nem munkatárs-helyettesítő. Az agent egy jogosultsággal rendelkező végrehajtó elem, ezért ugyanúgy szervezeti szabály kell köré, mint egy pénzügyi vagy ügyfélkezelési folyamathoz.

A következő gyakorlati lépés egyszerűbb, mint amilyennek hangzik.

Vegyél elő egyetlen folyamatot, ahol már AI-t használsz vagy hamarosan használnál. Ne technológiával kezdd. Írd fel négy oszlopba:

1. Milyen adatot olvashat az agent?
2. Milyen adatot módosíthat?
3. Milyen döntést javasolhat?
4. Milyen döntést nem hozhat meg ember nélkül?

Ha erre nincs válasz, akkor még nincs agent workflow. Csak egy gyors eszköz, ami egyelőre szerencsésen viselkedik.

A korlát is itt van. A túl szigorú kontroll megöli az automatizálás értelmét. Ha minden apró lépéshez jóváhagyás kell, a rendszer csak drágább feladatlista lesz. Ha viszont nincs kontroll, a vezető nem delegált, hanem lemondott a rálátásról.

A jó AI operáció nem az, ahol minden autonóm. Hanem ahol pontosan tudjuk, mi lehet autonóm.

Erről szól a [kontrollált AI operátor KKV-k számára](/kontrollalt-ai-operator-kkv/) gondolata is, és ezért kapcsolódik szorosan az [AI agent nem modell, hanem működési döntés](/ai-agent-nem-modell/) cikkhez. A modellválasztás fontos, de a vezetői kockázat ritkán ott születik. Többnyire ott, ahol a cég nem mondta ki, mi számít döntésnek.

A jövő agentjei nem azért fognak gondot okozni, mert túl okosak lesznek, hanem mert túl sok kimondatlan szabály között kell majd kitalálniuk, mit jelent jól dolgozni.

## FAQ

### Miért kockázatos, ha több AI agent dolgozik egy KKV-ban?

Azért, mert a külön-külön helyes lépések együtt rossz működést eredményezhetnek. Ha több agent ugyanazokat az adatokat vagy ügyfélfolyamatokat használja, a felelősségi határok nélkül gyorsan összekeveredik, ki mit dönthet.

### Mi legyen az első szabály egy agent workflow bevezetésekor?

Az első szabály a jogosultsági határ. Pontosan le kell írni, mit olvashat, mit módosíthat, mit javasolhat, és mit nem dönthet el emberi jóváhagyás nélkül.

### Kell-e minden AI agent döntést embernek jóváhagynia?

Nem. A cél nem az, hogy minden lépés manuális maradjon. A cél az, hogy az üzleti kockázatot hordozó döntések maradjanak kontroll alatt, miközben az előkészítés, rendszerezés és adminisztráció automatizálható.

### Mit jelent ez egy 5-50 fős cég vezetőjének?

Azt, hogy az AI bevezetés nem csak eszközválasztás. Operációs tervezés is. A vezetőnek nem minden promptot kell értenie, de a döntési pontokat és jogosultságokat igen.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Mit okoz több AI agent egy rendszerben?",
      "author": {
        "@type": "Person",
        "name": "Vincze Tamás"
      },
      "datePublished": "2026-08-17",
      "dateModified": "2026-08-17",
      "articleSection": "AI operáció",
      "description": "Több AI agent közös munkaterében nem a modell okossága a fő kockázat, hanem a kontroll, jogosultság és felelősség hiánya."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Miért kockázatos, ha több AI agent dolgozik egy KKV-ban?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Azért, mert a külön-külön helyes lépések együtt rossz működést eredményezhetnek. Ha több agent ugyanazokat az adatokat vagy ügyfélfolyamatokat használja, a felelősségi határok nélkül gyorsan összekeveredik, ki mit dönthet."
          }
        },
        {
          "@type": "Question",
          "name": "Mi legyen az első szabály egy agent workflow bevezetésekor?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Az első szabály a jogosultsági határ. Pontosan le kell írni, mit olvashat, mit módosíthat, mit javasolhat, és mit nem dönthet el emberi jóváhagyás nélkül."
          }
        },
        {
          "@type": "Question",
          "name": "Kell-e minden AI agent döntést embernek jóváhagynia?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nem. A cél nem az, hogy minden lépés manuális maradjon. A cél az, hogy az üzleti kockázatot hordozó döntések maradjanak kontroll alatt, miközben az előkészítés, rendszerezés és adminisztráció automatizálható."
          }
        }
      ]
    }
  ]
}
```
