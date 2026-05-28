---
title: Migráció előtt rend, különben hétfőn káosz
date: 2026-06-20
site: elkezdodott.hu
description: A költözés nem másolásról szól, hanem arról, hogy mi marad ki. KKV vezetőknek
  gyakorlati keret a biztonságos átálláshoz.
tags:
- KKV
- rendszer
- migráció
slug: migracio-elotti-rend
status: draft
id: elkezdod
content_type: article
created_at: '2026-05-25'
updated_at: '2026-05-28T09:19:03.187458+00:00'
---

A rendszer költözés nem a másoláskor megy keresztül, hanem az után. Ekkor derül ki, hogy valaki elfelejtett egy beállítást, egy jogosultság maradt el, vagy egy rutinfeladat nincs dokumentálva. Egy 5-50 fős cégnél ez egyből működési zavar. Ezért érdemes előtte tisztázni, hogy mi megy, mi marad, és hogyan állunk vissza ha baj van.

A legtöbb csapat ott csúszik meg, hogy a "majd ott beállítjuk" úgy hangzik, mint terv. De valójában nem az.

Mit működik gyakorlatban:

1. Pontos lista: mit viszünk át, mit nem. Nem lehet "szinte minden".
2. Visszaállási terv: papíron, 30-60 percre tervezett. Hogy lehet visszamászni, ha félremegy.
3. A rutin dolgok külön listán: cronok, napi checkek, ütemezett munkák. Hogy semmi ne maradjon ki.
4. Amit nem nyúlunk a költözés napján: kritikus adatok, éppen futó projektek, ügyfél interfészek.

A gyakorlat azt mutatja: sok cégnél az összes rendszer egy-két ember fejében él. Ez addig működik, amíg az illető elérhető. Nem működik, ha betegszabadság, váratlan lemondás vagy stressz történik.

Mit csinálja ebből a legjobb? Ha költöznöl, ne egy technikus listát kezdj szerkeszteni, hanem azt: milyen dolgotól függ hétfő reggel a napi működés. Azt védd meg előszőr. A többi másodlagos.

> "Költözés előtt érdemes gondolkodni rajta, mint kockázat kezelésen. Nem technikai projekten."
> (Vincze Tamás)

## Konkrét példa

Az egyik KKV, ahol ezt csináltuk, az első lépés volt: melyik 5 dolog nem működhet hétfő reggel? Ezek voltak: email jövetele, termékkatalógus, számlázó, pénztárgép adatok, ügyfél adatbázis. Erre az ötre fókuszáltunk. Minden más sokkal kevesebb volt aggodalomra okot adó.

## Ha már túl késő: a drágább út

Aki nem tervez előre, az később drágán fizet. Tipikus forgatókönyv: pénteken költöznek, szombaton kiderül, hogy az egyik rendszer nem működik, vasárnap pánikban kezdik az improvizálást, hétfőn reggel az ügyfél fél, hogy mi a helyzet. Ez pár ezer euróba kerül, és alig állítható vissza.

Az előzetes rend összerakása tart 2-3 órát. Az improvizáció miatt okozott zavar napokba, hetekbe kerülhet.

---

*Draft státusz. Publikálás Tomi jóváhagyása alapján.*

## 2026-os relevancia frissítés

Ez a cikk tartalmilag továbbra is releváns az aktuális AI-piaci helyzetben is. A fókusz ma: költségkontroll, adatminőség, workflow-governance, és vendorfüggetlen működés. A példák időközben változhatnak, de a vezetői döntési keret és a megvalósítási logika ma is érvényes.
