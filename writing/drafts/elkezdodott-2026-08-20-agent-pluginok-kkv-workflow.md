---
id: elkezdod
title: elkezdodott-2026-08-20-agent-pluginok-kkv-workflow
site: elkezdodott
content_type: article
created_at: '2026-08-20'
status: draft
updated_at: '2026-08-20T07:45:00+02:00'
---

Az agent plugin lényege, hogy az AI agenthez tartozó utasítások, eszközkapcsolatok és konfigurációk ne szétszórt beállításokban éljenek. Egy KKV-nál ez nem fejlesztői kényelmi kérdés: így lehet kontrollálni, melyik workflow mit tud, milyen eszközt ér el, és hol kell megállnia egy jóváhagyási pontnál.

## Mi történt?

A Google Developers Blog 2026 augusztusában bemutatta az Agent Plugins megközelítést: egy hordozható csomagformátumot, amely agent készségeket, MCP szerver konfigurációt és kapcsolódó komponenseket fog össze egy mappában. A cél az, hogy a kliens ne kézzel összerakott, törékeny beállításokból találja ki, mit tud egy agent, hanem manifest és rögzített mappastruktúra alapján töltse be a képességeket.

Az Agent Plugins dokumentáció szerint a formátum nem próbál mindent egyetlen szabványba kényszeríteni. A manifest validálása, a komponensek felfedezése és a hibahatárok a fontos részek. Ha például egy MCP szerver hibásan van konfigurálva, az ne feltétlenül vigye magával az összes többi készséget.

Források:

- Google Developers Blog: "Agent Plugins package your skills, tools, and more"  
  https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/
- Agent Plugins dokumentáció: "MCP servers"  
  https://agent-plugins.org/plugin-authors/mcp-servers
- Agent Plugins áttekintő oldal: "Agent Plugins: The Portable Agent Plugin Standard"  
  https://agentplugins.codes/

## Mit jelent ez egy KKV CEO-nak?

Egy KKV-ban az AI agent akkor válik üzleti eszközzé, amikor nem csak beszélgetni tud, hanem konkrét folyamatban dolgozik: ajánlatot előkészít, számlaadatot ellenőriz, ügyféligényt osztályoz, belső tudást keres, vagy státuszt frissít egy rendszerben.

Ilyenkor a kulcskérdés nem az, hogy az agent "okos-e", hanem az, hogy a képességei körülhatárolhatók-e.

CEO szemmel az agent plugin három dolgot tehet átláthatóbbá:

- milyen utasításkészlet alapján dolgozik az agent,
- milyen eszközökhöz vagy adatokhoz fér hozzá,
- mi történik, ha egy komponens hibázik vagy hiányzik.

Ez különösen akkor számít, amikor több belső workflow indul el párhuzamosan. Egy értékesítési agentnek nem kell pénzügyi jóváhagyási eszköz. Egy pénzügyi ellenőrző agentnek nem kell ügyfélnek e-mailt küldenie. A csomagolt készségek és eszközkapcsolatok segíthetnek abban, hogy ezek ne keveredjenek össze.

## Konkrét működési példa

Egy 25 fős B2B szolgáltató cég bevezet egy "ajánlat-előkészítő" agentet.

Az agent plugin tartalmazhatja:

- az ajánlatkérő e-mailek feldolgozási utasításait,
- a CRM kereséshez szükséges MCP kapcsolat konfigurációját,
- egy készséget az ügyféltípus és sürgősség besorolására,
- egy sablont a belső értékesítői összefoglalóhoz,
- egy korlátot: külső e-mailt nem küldhet, csak piszkozatot készíthet.

Ha később ugyanennek a cégnek kell egy "panasz-előkészítő" agent, nem ugyanazt az agentet kell tovább bővíteni mindenféle szabállyal. Kaphat külön plugint, külön utasítást, külön eszközhozzáférést és más jóváhagyási pontot.

Ez operatív szempontból fontos. A cég nem egy nagy, nehezen érthető AI asszisztenst épít, hanem kisebb, feladathoz kötött agent képességeket.

## Hol a korlát?

Az agent plugin nem oldja meg automatikusan a jogosultságkezelést, az auditot vagy a felelősségi rendet. A dokumentáció is jelzi, hogy az autentikáció és a hitelesítési adatok kezelése kliensoldali kérdés marad. Vagyis attól, hogy egy képesség szépen be van csomagolva, még nem biztos, hogy üzletileg biztonságos.

Tipikus kockázatok:

- túl sok eszköz kerül egy pluginba,
- nincs külön fejlesztői és éles környezet,
- nincs naplózva, melyik agent melyik eszközt hívta,
- a plugin neve üzleti célt mond, de a tartalma túl széles hozzáférést ad,
- nincs emberi jóváhagyás a külső hatású lépések előtt.

KKV környezetben az első szabály egyszerű: egy plugin egy jól körülírt workflow-t szolgáljon. Ne legyen általános "cég mindentudó agent" csomag, mert azt nehéz ellenőrizni.

## Gyakorlati következő lépés

Válassz ki egyetlen ismétlődő folyamatot, ahol az agent már most is hasznos lehetne. Például ajánlatkérés előszűrés, számlaeltérés ellenőrzés, support jegyek priorizálása vagy heti vezetői riport előkészítése.

Írj hozzá egy egyszerű agent plugin térképet:

1. Mi a workflow neve?
2. Milyen bemenetből dolgozik?
3. Milyen kimenetet készít?
4. Milyen belső rendszerhez férhet hozzá?
5. Mit nem tehet meg?
6. Hol kell emberi jóváhagyás?
7. Mi történik, ha az eszközkapcsolat hibázik?

Ez még nem technikai implementáció. Ez a kontrollterv. Ha ezt a hét kérdést nem lehet tisztán megválaszolni, akkor a plugin csomagolás csak rendezettebbé teszi a bizonytalanságot.

## FAQ

### Kell-e agent plugin egy KKV-nak az első AI bevezetéshez?

Nem feltétlenül. Ha csak egy egyszerű asszisztensről van szó, korai lehet. Akkor válik fontossá, amikor az agent már eszközöket használ, több workflow-ban dolgozik, vagy másokkal meg kell osztani a képességeit.

### Mi a különbség egy prompt és egy agent plugin között?

A prompt csak utasítás. Egy agent plugin ennél szélesebb csomag lehet: utasítás, készség, eszközkapcsolat, konfiguráció és betöltési szabály együtt.

### Milyen workflow-val érdemes kezdeni?

Olyannal, ahol a bemenet ismétlődő, a kimenet jól ellenőrizhető, és van természetes emberi jóváhagyási pont. Például ajánlat-előkészítés, dokumentum-összefoglalás vagy CRM frissítési javaslat.

### Mi legyen tiltva az első verzióban?

Külső e-mail küldése, pénzköltés, szerződésmódosítás, ügyféladat törlése és minden olyan művelet, amelyet nehéz visszafordítani.
