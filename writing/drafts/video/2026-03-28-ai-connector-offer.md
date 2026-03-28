# AI App Connector Felterkepezesi Lap — vinczetamas.hu szamara

## Mit kapsz ezzel
Egy 20 perces auditot arról, hol vész el a legtöbb idő az appjaid között. Ez lesz a beállítás alapja.

---

## Checklist

### 1. App térkép (te csinálod, 10 perc)
- [ ] Sorold fel a 3-5 legfontosabb szoftvert, amit napi szinten használ a csapat
  (pl. számlázó, CRM, email, naptár, projektmenedzsment, táblázat)
- [ ] Melyik appból melyikbe kell rendszeresen adatot vinni?
- [ ] Ki csinálja ezt ma manuálisan, és mennyi ideje megy el rá hetente?

### 2. Kézi bridge-ek azonosítása (mi segítünk)
Minden kézi adatmozgatásnál 3 kérdés:
- Ugyanaz az adat, ugyanolyan formában kerül át? (ha igen: azonnal automatizálható)
- Van-e kivétel vagy döntési pont az átvitelnél? (ha igen: jóváhagyási kapu kell)
- Milyen gyakran fut? (napi / heti / eseményalapú)

### 3. Prioritizálás
- [ ] Top 3 folyamat, ami a legtöbb időt viszi
- [ ] Ezekre beállítjuk az AI connectort (Composio / n8n / natív integráció)
- [ ] A többit a second wave-be tervezzük (ha az első sikeres)

### 4. Implementáció (mi csináljuk)
- [ ] Connector beállítás a 3 fő flow-ra
- [ ] Tesztelés: 2 hétig együtt figyeljük az outputot
- [ ] Kalibráció után: teljesen automatikus futás, napi log neked

---

## Következo lepes
"Ha be akarod állítani a cégedben: vinczetamas.hu/audit"
