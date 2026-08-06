---
id: elkezdod
title: elkezdodott-2026-08-06-ai-agent-penzkoltesi-korlatai
site: elkezdodott
content_type: article
created_at: '2026-08-06'
status: draft
updated_at: '2026-08-06T06:00:01.438796+00:00'
---

Egy AI agent akkor kaphat költési jogot, ha a pénzügyi keretek nem a promptban, hanem külön szabályrétegben élnek. KKV-ként ez minimum előre beállított budgetet, engedélyezett kereskedőlistát, tranzakciós plafont, naplózást és kivételes esetekben emberi jóváhagyást jelent. A cél nem bizalom, hanem mérhető, visszavonható felhatalmazás.

## Mi történt?

A Cloudflare 2026. augusztus 4-én bejelentette a Cloudflare Wallets és cloudflare.pay megoldásokat. A cél az, hogy a Cloudflare-en futó AI agentek stabil azonosítót kapjanak, és a tulajdonosuk által beállított limiteken belül tudjanak online fizetni.

A bejelentés szerint az Account Wallet a cég vagy felhasználó központi pénztárcája, ebből lehet külön Virtual Walletet adni egyes agenteknek. Ezekhez költési plafon, jóváhagyott kereskedőlista és maximális tranzakciós méret állítható be.

Források:

- Cloudflare press release, 2026. augusztus 4.: "Cloudflare Gives AI Agents an Identity and a Wallet"  
  https://www.cloudflare.com/press/press-releases/2026/cloudflare-gives-ai-agents-an-identity-and-a-wallet/
- Help Net Security, 2026. augusztus 5.: "Cloudflare gives AI agents wallets with built-in spending controls"  
  https://www.helpnetsecurity.com/2026/08/05/cloudflare-wallets-for-ai-agents/

## Mit jelent ez egy KKV CEO-nak?

Az agent pénzköltése nem azzal kezdődik, hogy "rábízzuk a bankkártyát". A jó kérdés inkább ez: melyik kis értékű, gyakori, jól körülhatárolható vásárlást érdemes automatizálni?

Például egy operációs agent hetente kipróbálhat több fizetős adatforrást, API-t vagy iparági adatlekérést egy 10 vagy 20 eurós kereten belül. Nem rendelhet új szoftverelőfizetést, nem költhet ismeretlen oldalon, és nem lépheti túl az előre beállított tranzakciós limitet.

Ez a CEO szempontjából nem AI-feature, hanem kontrollmodell:

- ki vagy mi költhet,
- mire költhet,
- mennyit költhet egyszerre,
- mikor kell emberi jóváhagyás,
- hol látszik utólag a döntés és a tranzakció.

## Konkrét működési példa

Egy 25 fős B2B szolgáltató cég piackutató agentet használ. Az agent feladata, hogy heti egyszer frissítse az értékesítési csapat célcéglistáját.

A pénzügyi szabály:

1. Az agent csak három előre jóváhagyott adatforrásnál fizethet.
2. Heti limitje 15 euró.
3. Egy tranzakció legfeljebb 3 euró lehet.
4. Ha egy forrás drágább, az agent csak jóváhagyási javaslatot készít.
5. Minden fizetés bekerül a heti operációs riportba.

Így az agent gyorsabbá teszi a munkát, de nem kap általános beszerzési jogot. Ez a különbség az automatizálás és az elszabadított költés között.

## Hol a kockázat?

A legnagyobb kockázat nem az, hogy az agent egyszer téved. Hanem az, hogy a tévedés ismételhető, skálázható és későn látszik.

Tipikus hibák:

- túl magas induló budget,
- nincs külön agentenkénti limit,
- nincs merchant allowlist,
- nincs maximum tranzakciós méret,
- nincs riasztás szokatlan költésnél,
- a költés nincs összekötve felelőssel és üzleti céllal.

Egy promptban leírt "ne költs sokat" nem kontroll. A kontroll külön jogosultság, külön limit és utólag ellenőrizhető napló.

## Gyakorlati következő lépés

Mielőtt bármilyen fizetési jogot adsz egy agentnek, írj egy egyoldalas agent költési policy-t.

Legyen benne:

- agent neve és üzleti célja,
- engedélyezett szolgáltatók listája,
- heti vagy havi limit,
- tranzakciónkénti limit,
- jóváhagyási küszöb,
- naplózás helye,
- felelős ember neve,
- első felülvizsgálat dátuma.

KKV-ként az első verzió legyen szigorú. Először 5 vagy 10 eurós tesztkeret, csak javaslatkészítés nagyobb költésnél, heti áttekintés a CEO vagy operációs vezető részéről.

## FAQ

### Kell-e AI agentnek saját pénztárca?

Nem minden agentnek. Csak annak, amelyik kis értékű, ismétlődő, jól mérhető online vásárlást vagy fizetős lekérést végez.

### Elég, ha a promptban megtiltom a túlköltést?

Nem. A pénzügyi korlátot rendszerszinten kell beállítani: budget, kereskedőlista, tranzakciós limit, napló és jóváhagyás.

### Mi legyen az első teszt?

Egy alacsony kockázatú folyamat: fizetős adatlekérés, API-próba, tartalomhozzáférés vagy kis értékű iparági kutatás. Ne szoftverbeszerzéssel kezdj.

### Ki legyen a felelős?

Minden költési joghoz legyen emberi tulajdonos. KKV-ban ez lehet a CEO, az operációs vezető vagy az a csapatvezető, akinek a folyamatát az agent támogatja.
