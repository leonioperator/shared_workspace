# Vincze Tamás - Napi Hírlevél Feldolgozás (2026-08-06)

Sziasztok,

A tegnapi AI hírekből most nem egy nagy modellbejelentés a legfontosabb, hanem az, hogy az agentek köré elkezd kiépülni a kontrollréteg.

**AI agentek pénzügyi korlátokkal:** A Cloudflare Wallets olyan rendszert mutatott be, amely AI agenteknek adhat stabil identitást és korlátozott fizetési jogosultságot API-khoz, MCP eszközökhöz és online tartalmakhoz. Ez KKV szemmel kulcskérdés. Egy agent akkor lesz valóban hasznos, ha nemcsak javasol, hanem műveleteket is elvégez. De ehhez nem szabad korlátlan hozzáférést kapnia. Kell limit, engedélyezett szolgáltatói lista, tranzakciós plafon és naplózás.

**Nem minden AI feladathoz kell ugyanaz a modell:** A Google Cloud API Gateway új model routing preview-ja azt mutatja, hogy a modellválasztás lassan infrastruktúra-szintű kérdés lesz. Egy cég választhat olcsóbb modellt egyszerű osztályozásra, erősebbet döntés-előkészítésre, és külön modellt kódolásra vagy elemzésre. A lényeg: az AI költséget nem csak a prompttal lehet kontrollálni, hanem azzal is, hogy melyik feladat melyik modellhez kerül.

**Az agent nem chatablak, hanem munkakörnyezet:** A Kiro Crew és a computer-use verification iránya ugyanarra mutat. A jó agent állapotot tart, visszatérő feladatokat végez, és bizonyítékot ad arról, hogy mit csinált. Például reprodukál egy hibát, lefuttatja az ellenőrzést, képernyőképet vagy videót csatol. Ez azért fontos, mert a CEO-nak nem plusz beszélgetés kell, hanem kevesebb ellenőrizetlen munka.

**Mit jelent ez egy KKV-nak?** Az AI bevezetés következő lépése nem az, hogy "legyen chatbot". Hanem az, hogy legyenek kontrollált agent-folyamatok: ki mit tehet, mennyiért, milyen jóváhagyással, milyen bizonyítékkal. Ez a különbség a látványos demó és a valóban működő operáció között.

Mai javasolt téma a Navibase hírlevélhez:

**Mikor engedheted meg egy AI agentnek, hogy pénzt költsön?**

Rövid váz:
- ne kapjon korlátlan hozzáférést
- legyen szolgáltatói allow list
- legyen napi és tranzakciós limit
- bizonyos összeg felett kérjen emberi jóváhagyást
- minden műveletről legyen napló és visszanézhető bizonyíték

Ez jó edukációs téma, mert egyszerre üzleti, biztonsági és operatív. Pont az a szint, ahol a KKV vezető már érzi a hasznot, de még nem akar technikai mélységbe menni.

Üdv,
Leoni
