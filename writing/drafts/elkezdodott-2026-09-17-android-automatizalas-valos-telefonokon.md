---
id: elkezdodott-2026-09-17-android-automatizalas-valos-telefonokon
title: "Android automatizalas valos telefonokon: mire jo ez egy KKV-nak?"
site: elkezdodott
content_type: article
created_at: '2026-09-17T07:45:00+02:00'
status: draft
slug: android-automatizalas-valos-telefonokon
quality_score: 4
source_signal: /writing/research/candidates-2026-09-17.md
sources:
  - https://github.com/google/artemis
---

Az ARTEMIS nyilt forrasu Google projekt termeszetes nyelvu utasitasokbol futtat Android automatizalast valos telefonokon. Egy KKV-nak ez nem csak tesztelesi tema: ugyanaz a gondolkodas segit biztonsagosan automatizalni mobilos ellenorzeseket, terepi munkafolyamatokat es ugyfeloldali app-lepeseket, ha megmarad az emberi kontroll es a naplozhatosag.

# Android automatizalas valos telefonokon: mire jo ez egy KKV-nak?

A Google ARTEMIS projektje azt igeri, hogy AI asszisztensek es tesztcsomagok valos Android telefonokat hasznalhatnak termeszetes nyelvu utasitasok alapjan. A GitHub leiras szerint end-to-end workflow-kat automatizal, logokat gyujt, es AI coding assistantokkal is osszekotheto.

Ez azert erdekes KKV szemmel, mert sok cegnel a mobilos folyamat nem kulon appfejlesztesi kerdes. A futar, szervizes, raktaros, ertekesito vagy ugyfelszolgalatos gyakran ugyanazt a nehany kepernyot nyomkodja naponta: statuszfrissites, foto feltoltes, QR-kod ellenorzes, uzenetkuldes, megrendeles visszaigazolasa.

Ha egy AI agent mar nem csak bongeszoben, hanem valos telefonon is vegig tud menni ezeken a lepeseken, akkor a mobilos folyamatok tesztelese es reszleges automatizalasa sokkal kozelebb kerul a napi mukodeshez.

## Mit jelent ez egy KKV CEO-nak?

Egy KKV CEO-nak nem az a fo kerdes, hogy a mobilos AI automatizalas mennyire latvanyos. Az a kerdes, hogy melyik ismert, ismétlődő mobilos lepes okoz ma idoveszteseget, hibas adatot vagy ugyfelpanaszt.

Peldaul egy szervizcegnel a technikus minden munka utan mobilon rogzit:

- erkezesi es tavozasi idot,
- munkaallapotot,
- felhasznalt alkatreszt,
- fotot a javitasrol,
- ugyfel-alairast vagy visszaigazolast.

Egy ilyen folyamatnal az ARTEMIS jellegu megkozelites eloszor nem eles automatikus dontesre valo. Sokkal jobb elso hasznalat, ha a ceg a sajat mobilos appjat vagy kulso rendszeret teszteli vele: vegigmegy a tipikus es a problemas eseteken, naplozza, hol akad el, es megmutatja, melyik kepernyon hibaznak gyakran az emberek.

## Konkret mukodesi pelda

Tegyük fel, hogy egy KKV sajat Android appot ad a terepi munkatarsaknak. A vezeto azt latja, hogy a munka lezárása sokszor hianyos, ezert a szamlazas kesik.

Egy minimalis automatizalt mobilteszt igy nezhet ki:

1. A tesztutasitas termeszetes nyelven leirja: nyisd meg a munkalapot, add meg a felhasznalt alkatreszt, csatolj fotot, allitsd "kesz" statuszra.
2. Az automatizalas valos vagy teszttelefonon vegigkattintja a folyamatot.
3. A rendszer logot es kepernyoallapotokat ment, hogy latszodjon, hol akadt el.
4. A fejleszto vagy operacios vezeto visszanezi az elakadast, es javitja a mezot, validaciot vagy uzenetet.
5. Csak akkor jon barmilyen eles automatizalas, ha a tesztelt folyamat stabil, visszakeresheto es van emberi jovahagyasi pont.

Ez nem helyettesiti az appfejlesztot vagy az operacios vezetot. Inkabb gyorsabban felszinre hozza, hol torik meg a napi mobilos folyamat.

## Korlát és kockázat

A valos telefonon futo AI automatizalas kockazata, hogy a kepernyo latszolag ugyanaz, de a mogotte levo uzleti helyzet nem. Egy hibas statuszfrissites szamlazast indithat, rossz ugyfelet ertesithet, vagy felulirhat egy fontos megjegyzest.

Kulon figyelni kell a jogosultsagokra is. Egy tesztagent ne kapjon ugyanazt a hozzaferest, mint egy emberi admin, ha nincs ra szukseg. A mobilos automatizalasnal legyen kulon tesztfiok, tesztadat, korlatozott jogosultsag es visszakeresheto futasnaplo.

A masik korlat a robusztussag. Egy appfrissites, uj engedelykeres, lassu halozat vagy modal ablak eleg lehet ahhoz, hogy az agent rossz helyre kattintson. Ezert magas kockazatu lepeseknel kotelezo a megerosites vagy az emberi jovahagyas.

## Gyakorlati kovetkezo lepes

Valassz ki egy mobilos munkafolyamatot, amely gyakori, de nem penzugyi vagy jogi dontes az elso korben. Ird ossze a 10 legtipikusabb utat es a 3 leggyakoribb hibaesetet.

Ezutan hozz letre egy tesztfiokot, amely nem er el eles ugyfeladatot. Futtass rajta automatizalt vegigjarast, es csak azt merd, hogy:

- hol akad el a folyamat,
- melyik mezok hianyoznak,
- melyik hiba nem ertheto a munkatarsnak,
- milyen log kellene egy vitas eset visszanezeséhez.

Ha ez mar stabil, akkor lehet kovetkezo lepeskent reszleges segedautomatizalast tervezni. Eles statuszvaltas, ugyfelertesites vagy szamlazasi trigger csak kulon release gate utan menjen.

## FAQ

### Mi az ARTEMIS roviden?

Az ARTEMIS egy nyilt forrasu Android automatizalasi projekt, amely termeszetes nyelvu utasitasokbol futtat mobilos workflow-kat, es naplozza a vegrehajtast.

### Egy KKV-nak ez inkabb teszteles vagy automatizalas?

Első lepesben inkabb teszteles. A legnagyobb gyors nyereseg az, hogy a ceg latja, hol akad el egy mobilos folyamat, mielott eles automatizalast adna ra.

### Mikor nem szabad elesben hasznalni?

Ha az agent penzt mozgat, szerzodest modosit, ugyfelet ertesit vagy vegleges statuszt allit be emberi kontroll nelkul. Ezekhez kulon jogosultsag, naplozas es jovahagyasi szabaly kell.

### Mi a legegyszerubb pilot?

Egy belso tesztfiokkal futtatott mobilos regresszios teszt: ugyanazt a gyakori munkafolyamatot minden appfrissites utan vegigjaratni, majd az elakadasokat javitasi listava alakitani.
