---
id: elkezdodott-2026-09-24-agent-onjavitas-release-gate
title: "Agent onjavitas release gate-tel: mire figyeljen egy KKV CEO?"
site: elkezdodott
content_type: article
created_at: '2026-09-24T07:45:00+02:00'
status: draft
slug: agent-onjavitas-release-gate
quality_score: 4
source_signal: /writing/research/candidates-2026-09-24.md
sources:
  - https://arxiv.org/abs/2609.24972
---

Az RRSI kutatas azt mutatja, hogy az AI agentek nem csak a valaszt, hanem a sajat futtatasi keretuket is javithatjak, merheto korlatok mellett. KKV-kent ez nem onjaro AI-t jelent, hanem release gate-et: valtoztatni csak teszten, naploval, kulon jovahagyassal es uzleti kockazati hatarral szabad.

# Agent onjavitas release gate-tel: mire figyeljen egy KKV CEO?

Az RRSI, vagyis Regularized Recursive Self-Improvement of Agent Harnesses, egy friss kutatas az agentek onjavitasarol. A lenyeg nem az, hogy a modell "okosabb lesz" altalaban, hanem hogy az agent futtatasi kerete, peldaul a prompt, az eszkozhasznalat es a dontesi szabalyok, kontrollalt modon valtozhatnak.

A tanulmany nyolc benchmarkon vizsgalta ezt a megkozelitest. A leiras szerint az RRSI azokon a feladatokon is javitott, amelyekre kozvetlenul nem optimalizaltak, mikozben kevesebb policy tokent hasznalt, mint az osszehasonlitott onjavito baseline.

KKV-szemmel ez azert fontos, mert a legtobb ceg nem sajat modellt tanit. Viszont egyre tobben epitenek olyan agentet, amely CRM-ben keres, ajanlatot keszit, hibajegyet osztalyoz, szallitasi allapotot ellenoriz vagy riportot ir. Ezeknel a kerdes mar nem csak az, hogy mit tud az agent ma, hanem az is, hogyan valtozik holnap.

## Mit jelent ez egy KKV CEO-nak?

Egy KKV CEO-nak az agent onjavitas nem technologiai latvanyossag. Operacios kockazatkezelesi kerdes.

Ha egy munkatars modosithat egy folyamatot, altalaban van felettesi jovahagyas, teszteles vagy legalabb visszakeresheto dontesi ut. Ugyanez kell az agenteknel is. Ha az agent sajat promptot, szabalylistat vagy eszkozhasznalati sorrendet javasol, azt nem szabad kozvetlenul eles mukodesbe engedni.

A jo kerdes igy hangzik: melyik agent-valtoztatas mehet at automatikusan tesztkornyezetbe, es melyikhez kell emberi release dontes?

## Konkret mukodesi pelda

Tegyük fel, hogy egy 40 fos B2B szolgaltato ceg AI agentet hasznal bejovo erdeklodesek eloszuresere. Az agent megnezi az emailt, kikeresi a cegmeretet, iparagat, varhato igenyt, majd javasol egy kovetkezo lepest az ertekesitonek.

Egy honap utan latszik, hogy az agent tul sok jo leadet sorol "kesobb kovetendo" kategoriaba. A csapat nem azonnal atirja elesben a promptot, hanem release gate-et hasznal:

1. Osszegyujtik az elmult 100 leadet es az emberi dontest.
2. Az agent javasol egy uj szabalyverziot, peldaul nagyobb sulyt ad a konkret hataridonek es a budget emlitesenek.
3. Az uj verzio csak tesztkornyezetben fut le ugyanazon a 100 eseten.
4. A csapat meri, hany jo lead kerul jobb kategoriaba, es hany gyenge lead csuszik feljebb.
5. Elesites csak akkor tortenik, ha a javulas eleri az elore megadott kuszobot, es nincs kritikus romlas.

Itt az onjavitas nem azt jelenti, hogy az agent szabadon atirja magat. Azt jelenti, hogy javaslatot tesz, a ceg pedig merheto gate-en engedi at vagy utasitja el.

## Korlát és kockázat

Az RRSI jellegu kutatasok fo tanulsaga, hogy az onjavitas konnyen tuloptimalizalhat arra, amit merunk. Ha rossz a tesztkeszlet, az agent latszolag javul, kozben a valos ugyfelekre rosszabb donteseket hoz.

KKV-nal ez kulonosen veszelyes, mert keves adatbol gyakran tul gyors kovetkeztetes szuletik. Tiz sikeres teszteset nem bizonyitja, hogy a folyamat stabil. Egy szezonalis kampany, egy uj termeknev vagy egy szokatlan ugyfeltipus eleg lehet ahhoz, hogy a korabbi szabaly rosszul viselkedjen.

A masik kockazat a felelosseg elkenodese. Ha az agent modositas utan hibazik, tudni kell, ki hagyta jova a valtoztatast, milyen teszten ment at, mi volt a vart hatas, es hogyan lehet visszaallitani az elozo verziot.

## Gyakorlati kovetkezo lepes

Ne azzal kezdj, hogy az agent onalloan javitsa magat. Kezdd egy egyszeru agent release naploval.

Minden agent-valtoztatasnal rogzitsetek:

- mi valtozott a promptban, szabalyban vagy eszkozhasznalatban,
- milyen tesztkeszleten futott,
- milyen metrika javult,
- milyen metrika romlott,
- ki hagyta jova,
- hogyan lehet visszagorgetni.

Ezutan valassz ki egy alacsony kockazatu folyamatot, peldaul belso ticket cimkezest vagy ertekesitesi lead priorizalast. Allits be egy minimum gate-et: az uj agent-verzio csak akkor mehet elesbe, ha legalabb ugyanannyi valos hibat fog meg, mint az elozo, es nem novel kritikus hibakategoriat.

Ha ez mukodik, kesobb lehet finomitani automatizaltabb onjavito ciklussal. A sorrend fontos: elobb meres, naplozas es rollback, utana onjavitas.

## FAQ

### Mi az RRSI roviden?

Az RRSI egy kutatasi megkozelites, amely az AI agent futtatasi keretet javitja rekurziv modon, de regularizacioval probalja csokkenteni a tulillesztest es a toredekeny javulasokat.

### Kell egy KKV-nak ilyen rendszert epitenie?

Altalaban nem kutatasi szinten. A hasznos lepes az, hogy minden agent-valtoztatasnak legyen tesztje, naploja, jovahagyasa es visszaallitasi pontja.

### Mi a legnagyobb uzleti kockazat?

Az, hogy az agent egy szuk teszten javul, de valos ugyfeleknel rosszabb dontest hoz. Ezert kell valos mintakon tesztelni, es kulon figyelni a kritikus hibakategoriakra.

### Mikor engedheto automatikus elesites?

Csak alacsony kockazatu folyamatnal, jol definialt metrikakkal, verziozott szabalyokkal es azonnali rollback lehetoseggel. Penzugyi, jogi vagy ugyfelertesitesi dontesnel maradjon emberi jovahagyas.
