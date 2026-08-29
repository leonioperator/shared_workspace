# Vincze Tamás - Napi Hírlevél Feldolgozás (2026-08-29)

Szevasztok!

A mai anyag nem klasszikus AI hír, inkább egy építési napló. Ben Tossell végigment azon, hogyan épített új személyes weboldalt agentekkel: első koncepció, vizuális feedback, annotált képernyőképek, újabb iterációk, majd egy fontos döntés: a túl bonyolult irányt elengedte.

### 1. Az agent gyorsan épít, de nem dönt helyetted

Az első weboldal koncepció agent appnak nézett ki: szálak, promptok, oldalsávok, interakciók. Technikailag izgalmas volt, de pont ez lett a gond. Ha valami agentnek néz ki, akkor előbb-utóbb valódi agent funkciókat is akarunk beletenni. Ez gyorsan elviszi a fókuszt.

KKV tanulság: az AI fejlesztésben nem csak az a kérdés, mit lehet megépíteni, hanem az is, mit nem szabad most megépíteni.

### 2. A legjobb brief néha egy képernyőkép

A szerző többször képernyőképet készített, rárajzolta a változtatásokat, majd visszaadta az agentnek. Ez sokkal gyorsabb, mint hosszú specifikációkat írni. Egy vezetőnek vagy projektgazdának ez különösen hasznos: ha látod, mi nem jó, elég megmutatni és röviden megmondani, mit változtatnál.

### 3. Tartalom külön fájlban

A végső megoldásban a tartalom Markdown fájlokba került, nem közvetlenül a kódba. Ez kisvállalati környezetben is jó minta: a változó üzleti szöveg legyen egyszerűen szerkeszthető, a technikai rész pedig maradjon stabil.

### Miért érdekes ez?

Mert ez a mindennapi AI munka valósága. Nem varázslat, hanem iteráció. Megnézed, javítod, visszavágod, újra próbálod. Az igazi érték nem az, hogy az agent sok mindent tud építeni, hanem hogy gyorsan kiderül, melyik irányt érdemes megtartani.

Mai javaslat: AI projektnél legyen egy külön "később" lista. Ami nem kell az első használható verzióhoz, oda megy. Ez a legegyszerűbb scope-fék.

Üdv,
Tomi
