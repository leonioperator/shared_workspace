---
id: vinczeta
title: ai-agent-nem-modell
site: vinczetamas
content_type: article
created_at: '2026-08-03'
status: draft
updated_at: '2026-08-03T07:45:00+02:00'
meta_description: 'Miért nem a modellválasztás dönti el egy KKV AI agent sikerét, hanem a memória, jogosultság, naplózás és jóváhagyási rend.'
og_image: ''
---

# Az AI agent nem a modell

Egy KKV AI agent sikere ritkán azon múlik, hogy melyik nagy modell fut mögötte. A döntő különbség a körítésben van: mit jegyez meg, mihez fér hozzá, mikor kér jóváhagyást, és hogyan lehet utólag visszanézni a döntéseit egy valós üzleti folyamatban.

Kedden egy cégvezető azt mondta: "Tomi, én már nem akarok több AI demót látni. Azt akarom tudni, hogy ezt rá lehet-e engedni a napi működésre úgy, hogy nem csinál kárt."

Ez volt a pontos mondat, ahol a beszélgetés végre jó irányba fordult.

Nem az volt a kérdés, hogy GPT, Claude, Gemini vagy nyílt súlyú modell legyen a háttérben. Az sem, hogy melyik válaszol szebben egy tesztkérdésre. A valódi kérdés az volt, hogy egy 5-50 fős cégben ki vállalja a felelősséget, amikor az AI már nem csak szöveget ír, hanem adatot olvas, ügyfélnek válaszol, számlát ellenőriz, feladatot oszt ki vagy CRM-be nyúl.

Itt kezdődik az a rész, amit a legtöbb látványos AI bemutató elhallgat.

## A modell csak egy alkatrész

Az elmúlt napok hírlevelei ugyanarra mutattak rá több oldalról. A TLDR AI 2026. július 30-i anyaga szerint a megőrzött gondolkodási állapot és a kontextus tömörítése egy benchmarkon háromszoros eredményjavulást és hatszoros tokenmegtakarítást hozott. Ugyanezen a napon a Ben's Bites agentekről, memóriáról, biztonsági incidensekről és belső mini-toolokról írt.

Ezek nem laborérdekességek.

Egy kis cégben ez így néz ki: az ügyfélszolgálati agent látja az előző levelezést, de nem látja a teljes pénzügyi mappát. Tud választ javasolni, de 100 ezer forint feletti kompenzációt nem ígérhet jóváhagyás nélkül. Ha bizonytalan, nem improvizál, hanem kérdez. Ha hibázik, van napló, amiből kiderül, mit látott, mire hivatkozott és miért döntött úgy.

Ez nem modellkérdés. Ez működési rendszer kérdése.

> **VT:** Az AI akkor válik üzleti eszközzé, amikor nem csak okos, hanem számon kérhető.

## A kényelmetlen felismerés

Sok vezető azért fél az AI bevezetéstől, mert azt érzi, hogy vagy teljesen kézben tartja, vagy kockázatos játékba kezd. Közben a valóság középen van.

Nem az a cél, hogy az agent mindent megcsináljon ember nélkül. Az a cél, hogy pontosan le legyen írva, mit csinálhat egyedül, mit készíthet elő, és hol kell megállnia.

Ez kényelmetlen, mert ugyanazt kéri a cégtől, amit egy jó kolléga betanítása is kérne: tiszta folyamatot, döntési határokat, felelősségi rendet. Ha ezek nincsenek meg, az AI nem rendet teremt. Csak gyorsabban mozgatja a meglévő káoszt.

Vincze Tamás stratégiai AI operációs partnerként pont ezt keresi egy bevezetés elején: nem azt, melyik modell hangzik a legjobban, hanem azt, hol vannak a döntési pontok, a visszakérdezési helyzetek és a kockázatos jogosultságok.

## Egy konkrét működési példa

Vegyünk egy számlafeldolgozó agentet egy szolgáltató KKV-ban.

Rossz bevezetés esetén az agent megkapja a bejövő számlákat, kiolvassa az adatokat, és automatikusan betolja őket a könyvelési rendszerbe. A vezető örül, mert eltűnt napi húsz perc kézi munka. Aztán két hét múlva kiderül, hogy egy visszatérő beszállító megváltoztatta a bankszámlaszámát, az agent pedig nem jelzett, mert a számla formailag rendben volt.

Jobb bevezetés esetén az agent máshogy működik.

Először ellenőrzi az összeget, a partneradatot, a bankszámlaszámot és a korábbi mintát. Ismert partnernél, változatlan adattal és alacsony összeggel előkészíti a könyvelési tételt. Új bankszámlaszámnál vagy szokatlan összegnél megáll, és jóváhagyást kér. Minden lépést naplóz. A vezető nem mikromenedzsel, de a kockázatos pontoknál továbbra is ő dönt.

Ez a különbség a látványos automatizálás és a vezetői kontroll között.

## Hol bukik el a legtöbb agent?

Nem ott, hogy nem elég okos.

Ott, hogy nincs memóriája a folyamatról. Nincs különbség egy rutinművelet és egy kivétel között. Nincs rendesen beállított jogosultsági szint. Nincs napló. Nincs emberi jóváhagyási pont. Nincs költségfigyelés, ezért egy egyszerű feladatból harminc modellhívás lesz.

Egy 5-50 fős cégnél ezek nem technikai finomságok. Ezek döntik el, hogy az AI tehermentesíti-e a vezetőt, vagy újabb ellenőrizendő dobozzá válik az asztalán.

A korlát világos: az agent nem helyettesíti a rosszul definiált felelősséget. Ha a cégben ma sem egyértelmű, ki hagyhat jóvá kedvezményt, ki módosíthat szerződési feltételt, vagy ki szólhat rá egy késő beszállítóra, akkor az AI sem fogja ezt helyesen kitalálni.

## A gyakorlati következő lépés

Nem modellválasztással érdemes kezdeni.

Érdemes kiválasztani egyetlen belső folyamatot, például számla-előkészítést, ajánlat-utánkövetést vagy ügyfélszolgálati válaszjavaslatot. Utána négy kérdést kell végigvenni:

1. Milyen adatot láthat az agent?
2. Mit tehet meg önállóan?
3. Mikor kell emberi jóváhagyást kérnie?
4. Mit kell naplózni ahhoz, hogy visszaellenőrizhető legyen?

Ha erre nincs jó válasz, akkor még nem AI projekt van. Még operációs rendrakás van.

Kapcsolódó alapozás: [AI automatizálás KKV-knak](https://vinczetamas.hu/ai-automatizalas-kkv/) és egy korábbi gondolat az [ügynöki kontextus szerepéről](https://vinczetamas.hu/ugynoki-kontextus/).

Források: TLDR AI, 2026-07-30, message ID 475. Ben's Bites, 2026-07-30, message ID 474. Kutatási jegyzet: `/home/leoni/shared_workspace/writing/research/signals-2026-07-31.md`.

A vezető nem attól kap vissza időt, hogy az AI többet csinál, hanem attól, hogy a rendszer pontosan tudja, hol kell megállnia.

## FAQ

### Miért nem elég egy erős AI modell egy KKV automatizáláshoz?

Mert a modell önmagában nem tudja, mi a cég döntési rendje, kockázati határa és jóváhagyási folyamata. Ezeket a működési szabályokat külön kell megtervezni az agent köré.

### Milyen folyamatot érdemes először agenttel támogatni?

Olyat, ahol sok az ismétlődő előkészítő munka, de a végső döntés továbbra is embernél maradhat. Jó példa a számla-előkészítés, az ajánlat-utánkövetés vagy az ügyfélszolgálati válaszjavaslat.

### Mi a legnagyobb kockázat egy KKV AI agentnél?

Az, ha túl széles jogosultságot kap túl kevés naplózással. Ilyenkor gyorsan dolgozik, de a vezető csak későn látja, hol csúszott el a folyamat.

### Hogyan lehet kontroll alatt tartani az agent működését?

Adathozzáférési szabályokkal, jóváhagyási pontokkal, naplózással és költségfigyeléssel. Ezek nélkül az agent nem operációs segítség, hanem ellenőrizetlen végrehajtó.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Az AI agent nem a modell",
      "author": {
        "@type": "Person",
        "name": "Vincze Tamás"
      },
      "datePublished": "2026-08-03",
      "dateModified": "2026-08-03",
      "mainEntityOfPage": "https://vinczetamas.hu/ai-agent-nem-modell/"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Miért nem elég egy erős AI modell egy KKV automatizáláshoz?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Mert a modell önmagában nem tudja, mi a cég döntési rendje, kockázati határa és jóváhagyási folyamata. Ezeket a működési szabályokat külön kell megtervezni az agent köré."
          }
        },
        {
          "@type": "Question",
          "name": "Milyen folyamatot érdemes először agenttel támogatni?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Olyat, ahol sok az ismétlődő előkészítő munka, de a végső döntés továbbra is embernél maradhat. Jó példa a számla-előkészítés, az ajánlat-utánkövetés vagy az ügyfélszolgálati válaszjavaslat."
          }
        },
        {
          "@type": "Question",
          "name": "Mi a legnagyobb kockázat egy KKV AI agentnél?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Az, ha túl széles jogosultságot kap túl kevés naplózással. Ilyenkor gyorsan dolgozik, de a vezető csak későn látja, hol csúszott el a folyamat."
          }
        }
      ]
    }
  ]
}
```
