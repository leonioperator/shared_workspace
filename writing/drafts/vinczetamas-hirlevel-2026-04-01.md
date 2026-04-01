---
date: 2026-04-01
platform: vinczetamas.hu hírlevél (MailerLite)
status: draft
author: Leoni
---

# Az AI ipar legemlékezetesebb napja — és egy véletlen tanulság

Ma egyszerre két olyan esemény történt, amit érdemes alaposan megnézni, ha az AI-t komolyan veszed az üzletben.

## 1. OpenAI: 122 milliárd dollár, 852 milliárd dolláros értékelés

A ChatGPT anyacége lezárta a magáncégek eddigi legnagyobb tőkebevonási körét. Amazon 50 milliárdot tett be, az NVIDIA és a SoftBank 30-30 milliárdot. Az összeg maga is lenyűgöző, de ami igazán érdekes, az a számok mögötti történet:

- Havi 2 milliárd dollár bevétel, 4x gyorsabb növekedés, mint az Alphabet vagy a Meta volt ugyanebben a fázisban
- 900 millió heti aktív felhasználó
- Vállalati ügyfelek adják a bevétel 40%-át, és tovább nőnek

Az OpenAI mostantól egyetlen "szuperappba" olvasztja a ChatGPT-t, a Codex-et és az agent eszközeit. A cél egyértelmű: nem chat kliens akarnak lenni, hanem az AI-val végzett munka elsődleges platformja.

**KKV szemszögből:** Ha eddig egymástól független AI eszközöket használtál, hamarosan valószínűleg egyetlen helyen fogod intézni a legtöbbet. Érdemes figyelni, mikor indul ez az egységes platform.

## 2. Az Anthropic véletlenül kiadta a Claude Code teljes forráskódját

Az Anthropic egyik npm csomagjában benne maradt egy .map fájl, ami visszafejthetővé tette az egész Claude Code forráskódot. 512 000 sor, 1900 fájl. Pár óra alatt 25 000 GitHub csillag, és valaki már újra is írta Python-ban.

A kínos incidens mögött komoly tanulságok vannak arról, hogyan épül fel egy profi AI agent rendszer:

- Kettős engedélyezési rendszer, nem csak egy egyszerű "igen/nem"
- Az emlékezet nem mindent tárol, csak 150 karakteres jelzőket arról, hol kell keresni
- Háttérben fut egy "autoDream" folyamat, ami rendszerezi és törli a felesleges memóriaelem-eket
- Agent izoláció: minden munka saját Git worktree-ben fut

A legfontosabb felismerés az architektúrából: **az AI agent jövője nem az, hogy mennyi mindent emlékezzen, hanem az, hogy mikor felejtsen el valamit.** Ne tárold, amit újra le tudsz kérdezni.

**Miért érdekel ez téged?** Mert ez egy véletlenül nyilvánosság elé kerülő tervrajz. Pontosan így kellene felépíteni egy megbízható, üzleti AI agent rendszert, legyen az ügyfélkezelés, tartalom vagy belső folyamatok. A memória, az engedélyek, az izoláció nem luxus, hanem alap.

---

Ha mindkét hírből kellene egy mondatot kiemelni: az AI 2026-ban már nem szoftver, amit megvásárolsz. Üzemi rendszerré válik, amit te (vagy az ügynököd) vezet.

Ha kérdésed van arról, hogyan illesztheted ezt a cégedbe, keress meg.

— Vincze Tamás
