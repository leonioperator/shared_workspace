---
id: vinczetamas-2026-09-28-vallalati-ai-memoria-fegyelme
title: Ki emlékezhet a cég nevében?
site: vinczetamas
content_type: article
created_at: '2026-09-28'
status: draft
quality_score: 4
slug: vallalati-ai-memoria-fegyelme
source_signal: /writing/research/signals-2026-09-25.md
source: https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/
meta_description: "Az AI memória nem kényelmi funkció, hanem vezetői kontrollkérdés. Mit érdemes rögzíteni egy 5-50 fős cégben, és mit nem?"
og_image: /writing/drafts/vinczetamas-2026-09-28-vallalati-ai-memoria-fegyelme.png
---

# Ki emlékezhet a cég nevében?

Az AI memória akkor üzleti érték, ha pontosan szabályozott, mit őrizhet meg, ki férhet hozzá, és mikor kell törölni. Egy 5-50 fős cégben ez nem adatvédelmi mellékszál, hanem operációs kontroll. A rosszul kezelt memória ugyanazt a káoszt gyorsítja fel, amit eredetileg csökkenteni kellett volna.

Kedden egy vezető nem azt kérdezte tőlem, melyik AI eszközt érdemes bevezetni.

Azt kérdezte: "Ha az asszisztens egyszer megtanulja, hogyan dolgozunk, honnan tudom, hogy nem tanul meg túl sokat?"

Ez jó kérdés volt. Nem technikai. Vezetői.

A legtöbb cégvezető ma még úgy gondol az AI memóriára, mint kényelmi funkcióra. Ne kelljen újra bemásolni a cégbemutatót. Ne kelljen minden ügyfélnél elmagyarázni, milyen hangnemben írunk. Ne kelljen a kollégának ötödször is felidézni, hogy a pénteki riportban mi számít fontos eltérésnek.

Ez tényleg hasznos.

De a memória nem csak segít. A memória hatalmat ad.

## A memória nem jegyzetfüzet

A Google DeepMind friss leírása szerint a Private AI Compute szerveroldali memóriát kap: az információ titkosított tárolóban marad, a feloldáshoz szükséges kulcsokat pedig a felhasználó eszközei őrzik. A cél az, hogy az asszisztens eszközökön átívelően tudjon segíteni úgy, hogy a szolgáltató se férjen hozzá közvetlenül a tartalomhoz.

Forrás: [Google DeepMind - Advancing Private AI Compute with secure, server-side memory](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/)

Ez fontos irány. Nem azért, mert holnaptól minden magyar KKV ezt fogja használni. Hanem azért, mert megmutatja, merre megy a piac: az AI asszisztens nem egyszeri válaszadó lesz, hanem tartós munkatárs-memóriával rendelkező rendszer.

És itt jön a kényelmetlen felismerés.

Sok cégben ma sincs tisztázva, ki mire emlékezhet.

Az értékesítő fejében van az ügyfél előzménye. A pénzügyes tudja, melyik partner szokott csúszni. Az ügyvezető emlékszik arra, melyik beszállítóval volt konfliktus. A projektvezető érzi, melyik ügyfélnek nem szabad péntek délután ígérni.

Ezek eddig emberekhez kötött emlékek voltak. Sérülékenyek, de korlátozottak.

Amikor AI memóriába kerülnek, rendszerszintűvé válnak.

## Mi történik egy kis cégben?

Képzeljünk el egy 18 fős szolgáltató céget. Van húsz aktív ügyfelük, három projektvezetőjük, egy túlterhelt ügyvezetőjük, és heti több száz apró döntésük.

Az AI asszisztens elkezdi támogatni az operációt:

- összefoglalja az ügyfélmegbeszéléseket,
- előkészíti a státuszriportokat,
- figyeli, melyik feladat csúszik,
- javaslatot tesz a következő lépésre,
- emlékszik az ügyfél preferenciáira.

Elsőre ez felszabadító.

Aztán valaki megkéri: "Írj választ ennek az ügyfélnek a szokásos stílusunkban."

Melyik stílusban?

Abban, amit a cég hivatalosan képvisel? Abban, amit az egyik projektvezető megszokott? Abban, amit egy nehéz ügyfél miatt egyszer kivételként használtak? Abban, amit már rég el kellett volna engedni?

Az AI memória nem tudja magától, mi érvényes tudás és mi csak történeti zaj.

Ezért a vezetői kérdés nem az, hogy "tud-e emlékezni az AI". Hanem az, hogy mit tekinthet a cég nevében működési szabálynak.

> **VT signature:** Amit a cég memóriába enged, abból előbb-utóbb működési norma lesz.

## A korlát nem technikai, hanem vezetői

Egy 5-50 fős cégnél az AI memória legnagyobb kockázata ritkán az, hogy valaki rosszindulatúan feltöri a rendszert. Ez is fontos, de nem ez az első operációs töréspont.

A gyakoribb baj prózaibb:

- elavult ügyfélinformáció alapján készül döntés,
- kivételes engedményből általános szabály lesz,
- belső feszültség kerül bele egy ügyfélválasz hangnemébe,
- személyes adat marad bent olyan helyen, ahol már nincs dolga,
- a vezető azt hiszi, a rendszer tudja a kontextust, pedig csak korábbi mintákat ismétel.

Ilyenkor az AI nem hibázik látványosan. Udvariasan, gyorsan és magabiztosan viszi tovább a rossz működést.

Ez a veszélyesebb forma.

Mert a vezető nem veszi észre azonnal.

## Mit érdemes tenni most?

Vincze Tamás stratégiai AI operációs partnerként nem azzal kezdené, hogy melyik eszköz memóriája a legmodernebb. Egy 5-50 fős cégnél először memóriafegyelmet kell kialakítani.

Három egyszerű döntés elég az induláshoz.

Először: szét kell választani a tényt, a preferenciát és a szabályt.

Tény: az ügyfél keddenként tart státuszt.

Preferencia: rövid, konkrét e-maileket szeret.

Szabály: árengedményt csak vezetői jóváhagyással lehet adni.

Ha ez a három összemosódik, az AI operációs zavart fog termelni.

Másodszor: minden memóriának legyen gazdája.

Nem elég, hogy "a rendszer tudja". Ki mondhatja, hogy ez még igaz? Ki törölheti? Ki írhatja felül? Ki nézi át havonta?

Harmadszor: a memória ne legyen közvetlen végrehajtási jog.

Az asszisztens emlékezhet arra, hogy egy ügyfél érzékeny az árra. De ettől még nem adhat automatikusan kedvezményt. Emlékezhet arra, hogy egy beszállító csúszott. De ettől még nem minősítheti át egyedül kockázatos partnernek.

A memória javasolhat. A döntési jogot külön kell kezelni.

Ez kapcsolódik ahhoz is, amiről korábban az [agent futtatási fegyelemről](/blog/agent-futtatasi-fegyelem) írtam: az AI akkor hasznos a vezetőnek, ha nem csak okos, hanem kontrollálható működés része. A teljesebb képhez érdemes a [stratégiai AI operációs partner](/strategiai-ai-operacios-partner) oldalt is megnézni, mert ott látszik, hogyan épül össze a technológia, a felelősség és a cégvezetői tehermentesítés.

## A vezető valódi döntése

Az AI memória nem attól lesz biztonságos, hogy minden adat el van zárva. Attól lesz használható, hogy a cég pontosan tudja, melyik emlékből lehet működés.

Ez vezetői munka.

Nem kell túlbonyolítani. Egy induló szabályzat akár egy oldal is lehet:

- milyen ügyféltényeket tárolhat az AI,
- milyen személyes adatot nem tárolhat,
- melyik memóriát kell időszakosan felülvizsgálni,
- milyen döntést nem hozhat memória alapján,
- ki felel a törlésért és javításért.

Egy ilyen oldal nem adminisztráció. Ez a különbség aközött, hogy az AI segít emlékezni, vagy elkezdi konzerválni a cég rossz beidegződéseit.

A jövőben nem az lesz az erős cég, amelyiknek mindent megjegyez az AI-ja, hanem az, amelyik tudja, mit nem szabad a rendszer memóriájára bízni.

## FAQ

### Kell AI memória egy 5-50 fős cégnek?

Igen, ha ismétlődő ügyfélmunka, riportolás vagy belső koordináció van. De csak akkor érdemes bekapcsolni, ha világos, milyen adat kerülhet bele, ki felel érte, és mire használhatja a rendszer.

### Mi a legnagyobb kockázat az AI memóriában?

Nem csak az adatvédelmi incidens. A gyakoribb kockázat az, hogy az AI elavult, kivételes vagy pontatlan mintákból kezd működési szabályt gyártani. Ez lassan torzítja a döntéseket.

### Ki legyen felelős az AI memóriáért?

Üzleti oldali gazdára van szükség, nem csak technikai felelősre. A memória tartalma működési tudás, ezért annak kell felügyelnie, aki érti az ügyfélkezelést, a döntési jogokat és a céges kockázatokat.

### Lehet teljesen automatizálni a memória alapján hozott döntéseket?

Kis cégnél óvatosan. A memória adhat kontextust és javaslatot, de árengedmény, szerződéses ígéret, ügyfélminősítés vagy személyes adatot érintő döntés ne fusson emberi kontroll nélkül.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Ki emlékezhet a cég nevében?",
      "description": "Az AI memória nem kényelmi funkció, hanem vezetői kontrollkérdés. Mit érdemes rögzíteni egy 5-50 fős cégben, és mit nem?",
      "author": {
        "@type": "Person",
        "name": "Vincze Tamás"
      },
      "datePublished": "2026-09-28",
      "dateModified": "2026-09-28",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://vinczetamas.hu/blog/vallalati-ai-memoria-fegyelme"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Kell AI memória egy 5-50 fős cégnek?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Igen, ha ismétlődő ügyfélmunka, riportolás vagy belső koordináció van. De csak akkor érdemes bekapcsolni, ha világos, milyen adat kerülhet bele, ki felel érte, és mire használhatja a rendszer."
          }
        },
        {
          "@type": "Question",
          "name": "Mi a legnagyobb kockázat az AI memóriában?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Nem csak az adatvédelmi incidens. A gyakoribb kockázat az, hogy az AI elavult, kivételes vagy pontatlan mintákból kezd működési szabályt gyártani. Ez lassan torzítja a döntéseket."
          }
        },
        {
          "@type": "Question",
          "name": "Ki legyen felelős az AI memóriáért?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Üzleti oldali gazdára van szükség, nem csak technikai felelősre. A memória tartalma működési tudás, ezért annak kell felügyelnie, aki érti az ügyfélkezelést, a döntési jogokat és a céges kockázatokat."
          }
        }
      ]
    }
  ]
}
</script>
```
