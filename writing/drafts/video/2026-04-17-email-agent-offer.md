# OFFER ASSET: AI Email Agent – Ügyfélszolgálat Automatizálás

**Task ID:** mo34vuemiti5
**Dátum:** 2026-04-17

---

## CHECKLIST: 3 lépés az AI email agenthez

**Mielőtt hozzákezdesz – 15 perc:**
- [ ] Gyűjtsd össze a 10 leggyakoribb ügyfélkérdést (nyitvatartás, ár, státusz, elérhetőség, stb.)
- [ ] Írj minden kérdésre egy kész választ (sablon szöveg, amit az AI használhat)
- [ ] Döntsd el: melyik email fiókra fusson az agent? (Gmail / Outlook)

**Beállítás (mi csináljuk, 3 nap):**
- [ ] n8n workflow: beérkező email → GPT osztályozás → automatikus válasz / kézbesítés
- [ ] Sablon-válaszok betöltése a rendszerbe
- [ ] Kivétel-kezelés: amit az AI nem tud megválaszolni, azt neked továbbítja
- [ ] Napi összesítő: reggel egy digest az előző nap automatikus válaszairól

**Eredmény:**
- [ ] AI 24/7 válaszol a FAQ kérdések 80%-ára
- [ ] Te csak a 20% kivételt látod
- [ ] Heti 10 óra visszajön

---

## MINI WORKFLOW

```
Ügyfél emailt küld
    ↓
n8n fogadja → GPT osztályoz
    ↓
FAQ? → Automatikus válasz (sablon alapján)
Nem FAQ? → Továbbit neked (jelöléssel)
    ↓
Reggel: összesítő digest Telegramra / emailre
```

---

## ÁRAK

| Csomag | Ár | Mit kapsz |
|--------|-----|-----------|
| Alap | 29 900 Ft | Beállítás + 5 FAQ sablon |
| Core | 89 900 Ft | Beállítás + 20 FAQ + finomhangolás 2 hét |
| Pro | 249 000 Ft | Teljes email ops átvétel + havi karbantartás |

**Garancia:** Ha nem spórol meg heti 10 órát az első hónapban, visszaadom az árát.

---

## CTA SABLON (DM / komment válasz)

> „Köszönöm az érdeklődést! A beállítás 3 napot vesz igénybe.
> Küldök egy rövid kérdőívet, hogy mik a leggyakoribb emailjeid –
> utána indulhatunk. Mikor érsz rá 20 percet egyeztetni?"
