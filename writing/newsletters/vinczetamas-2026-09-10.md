# Navibase hírlevél draft - 2026-09-10

Téma: AI agenteknél nem az autonómia a lényeg, hanem a kontroll

## Rövid verzió

Az elmúlt napi AI hírekből most nem az a legfontosabb, hogy megint kijött egy gyorsabb modell vagy jobb képgeneráló. Hanem az, hogy az agentek körül kezd felnőni a második kérdés:

**Honnan tudod, hogy élesben is rá mered bízni a munkát?**

Ez a kérdés KKV oldalon sokkal fontosabb, mint a modellnevek.

## 3 jel, amit érdemes figyelni

### 1. Az agent governance már nem nagyvállalati luxus

A TLDR AI egyik kiemelt anyaga arról szólt, hogyan lehet agent release gate-eket, trace-eket, evalokat, emberi review-t és jóváhagyási folyamatot egy auditálható rendszerbe kötni.

Magyarul: nem elég, hogy az AI agent "megcsinálja". Tudni kell:

* milyen adatok alapján dolgozott,
* ki hagyta jóvá,
* milyen hibákat mértünk,
* milyen jogosultságot kapott,
* mikor kell embernek belépnie.

Ez KKV-nál nem ISO tanúsítvánnyal kezdődik. Hanem egy egyszerű szabállyal: ne adjunk az agentnek több hozzáférést, mint amennyit muszáj.

### 2. Az ember + agent páros erősebb, mint a magára hagyott agent

Egy friss agent benchmark szerint egy fejlesztő agent önállóan 23,9%-os eredményt ért el. Ugyanez a modell egy mély kontextussal rendelkező mérnökkel együtt 82,2%-ot.

Ez nagyon fontos üzleti tanulság.

Nem az a jó első lépés, hogy "AI, vedd át a céget". Hanem az, hogy:

* kapjon jó kontextust,
* kapjon szűk feladatot,
* legyen mérhető eredmény,
* legyen emberi kontrollpont.

Ettől lesz hasznos eszköz, nem kockázatos kísérlet.

### 3. A 24/7 AI munka nem ingyen van

OpenAI kutatók ma már több agent-munkanapot tudnak felügyelni egyetlen emberi műszak alatt. Ez jól hangzik, de ugyanebben a trendben a napi inference költség is meredeken nő.

KKV-nál ezért minden agent munkához kell három szám:

* mennyi időt spórol,
* mennyibe kerül,
* milyen hibakockázatot vállalunk vele.

Ha ez nincs meg, akkor az AI nem automatizálás, hanem homályos költséghely.

## Mit érdemes ebből átültetni egy kisvállalkozásba?

Egy praktikus agent bevezetés első verziója lehet nagyon egyszerű:

1. Egyetlen ismétlődő feladat kiválasztása.
2. Input és output pontos leírása.
3. Jogosultságok minimumra vétele.
4. Emberi jóváhagyási pont beépítése.
5. Heti mérés: idő, költség, hibák.

Nem látványos. Pont ezért működik.

## Navibase szemmel

Az AI agent értéke nem ott kezdődik, hogy mindent önállóan csinál. Ott kezdődik, hogy a vállalkozó visszakap napi 30-60 percet egy olyan folyamatból, amit eddig kézzel tartott fejben.

Ehhez nem csodamodell kell. Hanem tiszta feladat, kontroll és visszamérés.

Ez lesz a különbség AI játék és működő operáció között.
