---
id: 2026-05-
title: AI Ügyfélszolgálat Setup Checklist
site: vinczetamas
content_type: article
created_at: '2026-05-29'
status: draft
updated_at: '2026-05-29T06:30:02.055493+00:00'
---

# AI Ügyfélszolgálat Setup Checklist
## Sesame AI Agent Implementáció — Vincze Tamás

---

## Mit kapsz ezzel

Egy autonóm AI ügyfélszolgálati agent, amely azonnal feldolgozza az ügyféli kérdések 80 százalékát, 24/7 válaszol, és amit nem tud, automatikusan felkalapálja neked.

Az első héten működik. Az első hónapban már látod az eredményt: 25-40% kevesebb support ticket, 24 órás válaszidő, ügyfél elégedettség plusz 20%.

---

## Beállítási Checklist — 5 munkanap

### Nap 1-2: Döntéspontok és architecture

- [ ] **Döntés 1: Kommunikációs csatornák**
  Mely csatornákon válaszol az agent? (Email, Telegram, Chat, Facebook Messenger, vagy több egyszerre?)
  
- [ ] **Döntés 2: Tudásbázis forrása**
  Honnan veszi az agent a válaszokat? (FAQ dokumentum, korábbi ticket-ek, termékleírás, vagy valósidős adatok)
  
- [ ] **Döntés 3: Escalation szabály**
  Mikor nyúl be az ember? (Max 2 próbálkozás után, ha az agent confidence alatta 60%, vagy specifikus szavakra?)

### Nap 3-4: Technikai implementáció

- [ ] **Agent alapkonfiguráció**
  Az agent becsatlakozik a kommunikációs csatornáidhoz (API kulcsok, webhookok)
  
- [ ] **Tudásbázis feltöltés**
  Az agent megtanulja az FAQ, termék infó és policy dokumentumaid
  
- [ ] **Escalation pipeline**
  Ha az agent bizonytalan, automatikusan értesít téged és mellékeli az ügyfél kérdését

### Nap 5: Tesztelés és élesítés

- [ ] **Live tesztelés**
  Az agent válaszol az első valódi ügyfél kérdésekre (live monitoring)
  
- [ ] **Fine-tuning**
  Ha rossz választ adott, korrigálunk 1-2 óra alatt
  
- [ ] **24/7 monitoring bekapcsolása**
  Az agent már működik, te már nem kell kézzel válaszolj

---

## Az Első Hét Után

**Nap 8:** Az agent már feldolgozta az első 50-100 ügyfél kérdést. Átnézzük az escalation listát (azok, amiket nem tudott) és finomítunk.

**Hét 2:** Az agent már ismeri a mintázatokat. Ha az első hétben azt szűrtük, hogy mely kérdéseket nem érted el, azokra most ad jobban választ.

**Hó 2-3:** Az agent szinte önmagától fejlődik. Ami a múlt hónapban problém volt, erre most már saját magítól veszi fel a mintázatot.

---

## A Garantált Eredmény

### 30 napos Money-Back Garancia

Ezeket garantáljuk az első 30 napban:
- **25-40% support ticket csökkentés** (mérés: előző 30 nap vs. új 30 nap)
- **24/7 ügyfél válaszidő** (nincs több "majd hétfőn" üzenetek pénteken)
- **20% ügyfél elégedettség növekedés** (az escalation-ba kerülő ügyfelek visszajelzése alapján)

Ha ezek közül bármelyik nem jön össze az első 30 napban, teljes visszatérítés. Nincs feltétel, nincs magyarázat, csak visszajár az ár.

---

## Felkészítés: Mit Készítesz Elő?

Az implementáció gyors, de neked szükséged van ezekre:

1. **FAQ vagy Support Dokumentum** (ha van már)
   10-20 gyakori kérdés + válasz szövegben. Ha nincs, azt interjúzás alapján írjuk meg 1-2 óra alatt.

2. **Kommunikációs Csatorna Hozzáférés**
   Az agent integrálódik az emailedhez / Telegramhoz / Chat platformodhoz. Ehhez admin jogot ad neked.

3. **Escalation Partner**
   Ki az az ember, akire az agent felkalapálja a problémás kérdéseket? (Általában te vagy az ügyfélszolgálat vezetője.)

4. **30 napos Tesztelési Közreműködés**
   1-2 naponta 15 percet szánunk arra, hogy átnézük az escalation listát és finomítunk.

---

## Következő Lépés

Ha ezt beépíteni akarod a cégedbe, kezdjük egy 30 perces audit-tal. Megnézzük az utolsó 30 nap support ticket-eid, azonosítjuk a mintázatokat, és kiszámoljuk, hogy az agent pontosan mennyit fog spórolni az idődből.

Menj a **vinczetamas.hu/audit** oldalra és foglalj le egy audit-ot.

---

## Kérdések?

Ha bármi kérdésed van az implementáció folyamatáról, írj egy üzenetet: **vinczetamas.hu/chat**

Egyébként: az agent 1 hétig felépül. Aztán már csak működik.
