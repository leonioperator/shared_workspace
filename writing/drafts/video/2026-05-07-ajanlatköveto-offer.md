---
title: Ajánlatkövető Rendszer Beállítási Checklist — KKV tulajdonosoknak
date: '2026-05-25'
site: vinczetamas
status: draft
---

# Ajánlatkövető Rendszer Beállítási Checklist — KKV tulajdonosoknak

## Mit kapsz ezzel
Egy Gmail + Google Sheets alapú ajánlatkövető rendszer beállítási útmutatója, amivel
egyszer megszünteted az ajánlatok elveszésének kockázatát. Nem kell drága CRM.
Nem kell fejben tartani. Heti 6 óra admin visszajön.

---

## Beállítási Checklist

### 1. Alap struktúra (Google Sheets)
- [ ] Hozz létre egy "Ajánlatok" lapot ezekkel az oszlopokkal:
  - Cégnév
  - Kapcsolattartó neve
  - Ajánlat összege (Ft)
  - Ajánlat dátuma
  - Következo follow-up dátuma
  - Státusz (Kint / Tárgyalás / Nyert / Veszített / Befagyott)
  - Megjegyzés

### 2. Follow-up szabályok meghatározása
- [ ] 3 napon belül nincs válasz → emlékezteto email
- [ ] 7 napon belül nincs válasz → második follow-up
- [ ] 14 napon belül nincs válasz → "befagyott" státusz + Telegram értesítés

### 3. Gmail kapcsolat (Apps Script vagy Zapier/Make)
- [ ] Szuro létrehozása: "Ajánlat", "Árajánlat", "Proposal" tárgyszavakra
- [ ] Bejövo válaszok automatikus státuszfrissítése a Sheets-ben
- [ ] Kimenő ajánlat levelek automatikus rögzítése

### 4. Heti riport beállítása
- [ ] Minden hétfon reggel automatikus összesíto: hány ajánlat van kint, melyeknél jár le a follow-up
- [ ] Email vagy Telegram értesítés formátumban

### 5. Piszkozat generátor (opcionális, de ajánlott)
- [ ] Sablon follow-up emailek 3 verzióban: 3 napos, 7 napos, 14 napos
- [ ] Változók: cégnév, ajánlat összege, eredeti dátum, kapcsolattartó neve

---

## Mutatók, amiket hetente nézz
- Nyitott ajánlatok száma és összértéke
- Lejárt follow-upok száma
- Befagyott ajánlatok aránya (ha 20% felett: kommunikációs probléma)
- Átlagos lezárási idő (napban)

---

## Következo lépés
Ha ezt te is be akarod állítani a cégedben, és nem akarod egyedül összerakni:
vinczetamas.hu/audit

*49 000 Ft. Beállítjuk egy nap alatt. Ha nem spórol meg heti 6 órát, visszaadjuk az árát.*
