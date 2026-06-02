# Google Sheet AI adatvédelmi audit checklist - KKV számára

## Mit kapsz ezzel

Ezzel a checklisttel gyorsan átnézheted, hol láthat AI bővítmény ügyféladatot, árlistát, ajánlati számítást vagy belső céges adatot a Google Sheetjeidben.

## Checklist

### 1. AI bővítmények listája

- [ ] Írd össze az összes Google Sheets bővítményt, amit a csapat használ.
- [ ] Jelöld, melyik bővítmény AI funkciót használ.
- [ ] Ellenőrizd, ki telepítette, és kinek a fiókjában fut.
- [ ] Töröld vagy kapcsold ki azt, amit senki nem tud megindokolni.

### 2. Hozzáférési szintek

- [ ] Nézd meg, melyik bővítmény fér hozzá a teljes Drive-hoz.
- [ ] Nézd meg, melyik bővítmény fér hozzá minden táblázathoz.
- [ ] Külön jelöld azokat, amelyek külső szolgáltatóhoz küldenek adatot.
- [ ] Amihez elég egy konkrét fájl, ne kapjon teljes fiókszintű jogot.

### 3. Érzékeny oszlopok

- [ ] Jelöld a táblázatokban az ügyfélnevet, emailt, telefonszámot és címet.
- [ ] Jelöld az árlistát, ajánlati számítást és belső margin adatokat.
- [ ] Jelöld a szerződéses, pénzügyi vagy HR adatokat.
- [ ] Ezekre legyen külön szabály: AI csak jóváhagyott mezőt dolgozhat fel.

### 4. Megosztási szabályok

- [ ] Ellenőrizd, van-e "anyone with the link" megosztás.
- [ ] Ellenőrizd, van-e külső Gmail vagy privát fiók a megosztottak között.
- [ ] Nézd meg, ki tud szerkeszteni és ki tud csak olvasni.
- [ ] Állíts be tulajdonosi felelősséget minden fontos táblázathoz.

### 5. Csapat szabály

- [ ] Írd le egy mondatban, milyen adatot tilos AI bővítménybe küldeni.
- [ ] Írd le, milyen esetben kell vezetői jóváhagyás.
- [ ] Írd le, ki dönt új AI bővítmény telepítéséről.
- [ ] Havonta egyszer nézd át a telepített bővítményeket és a megosztásokat.

## Javasolt belső szabály

AI bővítmény csak olyan táblázatban használható, ahol nincs ügyfélazonosító, árlista, belső margin, szerződéses adat vagy olyan információ, amit nem küldenénk ki külső partnernek.

Ha ilyen adat van a táblázatban, előbb másolatot kell készíteni, az érzékeny oszlopokat törölni kell, és csak ezt a tisztított verziót szabad AI-val feldolgozni.

## Következő lépés

Ha ezt a cégedben gyorsan rendbe akarod tenni: Google Sheet AI adatvédelmi audit 59 ezer forintért.

Átnézzük a bővítményeket, a jogosultságokat, az érzékeny mezőket és a megosztási szabályokat.

Ha nem találunk legalább 3 konkrét hibát vagy kockázatot, nem fizetsz.

vinczetamas.hu/audit
