# 20260329-idea-focus-system.md

## Feladat

Építs ki a shared_workspace repóban egy minimál, determinisztikus ötletkezelő és fókuszrendszert úgy, hogy a meglévő inbox → processed → outbound workflow-hoz illeszkedjen. Az inbox feldolgozás és az output elhelyezése már a meglévő működési modell része.

A cél nem ötletgyűjtő rendszer, hanem döntési és fókuszrendszer.

---

## Cél

Hozz létre egy olyan rendszert, amely:

- fogad új ötleteket Telegramból vagy inbox fájlból
- minden ötletet központilag eltárol
- egyszerre csak **1 aktív** ötletet enged
- automatikusan kiválasztja a következő fókuszt
- generál **1 darab konkrét sprint feladatot**
- kezeli a státuszokat: `idea`, `active`, `done`, `killed`
- nem igényel új külső szolgáltatást
- a meglévő shared_workspace struktúrába illeszkedik

---

## Helye

Használd ezt a mappát:

`/home/leoni/shared_workspace/project_ideas/`

Hozd létre benne ezeket a fájlokat:

- `ideas.jsonl`
- `state.json`
- `README.md` rövid működési leírással

---

## Adatmodell

### `ideas.jsonl`
JSONL, egy ötlet egy sor.

Minimális mezők:

- `id`
- `created_at`
- `updated_at`
- `source` (`telegram` | `inbox` | `import`)
- `text`
- `status` (`idea` | `active` | `done` | `killed`)
- `score_money`
- `score_validation`
- `score_alignment`
- `score_effort`
- `score_total`
- `sprint_task`
- `notes`

### `state.json`
Minimális mezők:

- `active_id`
- `last_selection_at`

---

## Döntési szabályok

### Alapszabály
Egyszerre csak **1** aktív ötlet létezhet.

### Új ötlet érkezése
Ha új ötlet érkezik:
- mentsd el `ideas.jsonl`-be
- kapjon új `id`-t
- `status=idea`
- ne szakítsa meg a már aktív ötletet

### Ha nincs aktív ötlet
Ha `state.json.active_id = null`, akkor:
- pontozd a `status=idea` ötleteket
- válaszd ki a legjobb `score_total` értékű ötletet
- állítsd `status=active`-ra
- írd be az `active_id`-t a `state.json`-ba
- generálj hozzá **1 konkrét sprint taskot**

### Ha aktív ötlet kész
Ha a rendszer `done` jelzést kap egy aktív ötletre:
- állítsd `status=done`-ra
- töröld az `active_id`-t
- azonnal válaszd ki a következő legjobb ötletet
- generálj új sprint taskot

### Kill
Ha egy ötletet el kell vetni:
- állítsd `status=killed`-re
- ha ez volt az aktív, válassz újat

---

## Pontozás

Használj egyszerű, determinisztikus pontozást:

- `score_money`: 0..3
- `score_validation`: 0..3
- `score_alignment`: 0..2
- `score_effort`: -2..0

Képlet:

`score_total = score_money + score_validation + score_alignment + score_effort`

### Értelmezés
- `money`: pénztermelő potenciál rövid/középtávon
- `validation`: milyen gyorsan validálható
- `alignment`: mennyire illeszkedik a fő célokhoz
- `effort`: mennyi energia/idő kell az első érdemi lépéshez

---

## Fő célok a pontozáshoz

Használd ezeket prioritási kontextusként:

1. 2026-ban kilépés a munkahelyről
2. AI/agentic/automatizációs bevétel építése
3. saját vagyont termelő rendszerek építése
4. fókusz és készre vitel, nem párhuzamos szétszóródás

---

## Sprint task szabály

Minden aktív ötlethez pontosan **1 darab** sprint task tartozhat.

A sprint task:
- legyen konkrét
- legyen végrehajtható
- legyen max. kb. 1 napos
- ne legyen lista
- ne legyen stratégiai esszé
- egyértelműen ellenőrizhető legyen a készültsége

Példa:
- jó: „Írj meg 1 validációs landing vázlatot 3 CTA-val”
- rossz: „Gondold végig a termékstratégiát”

---

## Input források

### 1. Telegram
Ha Telegram üzenetben ez a minta jön:

`Új ötlet: ...`

akkor kezeld új ötletként.

### 2. Inbox fájlok
Ha az inboxban olyan fájl jelenik meg, amely tartalmaz új ötletet vagy ötletlistát, olvasd be, és bontsd külön ötletekre, majd mentsd őket `source=inbox` értékkel. Az inbox/processed mechanizmus már a workspace működés része.

### 3. Régi ötletek importja
Készíts egyszeri import módot meglévő ötletek betöltésére, ha olyan inbox fájl érkezik, amely korábbi ChatGPT beszélgetésekből kigyűjtött ötleteket tartalmaz.

---

## Output

Minden fontos állapotváltásnál írj rövid állapotjelentést az `outbound/` mappába, mert ez a meglévő működési minta része.

Ajánlott fájlnevek:

- `YYYYMMDD-idea-system-status.md`
- `YYYYMMDD-next-focus.md`

A `next-focus` report minimálisan tartalmazza:

- aktív ötlet ID
- aktív ötlet rövid neve/leírása
- score bontás
- 1 sprint task
- miért ez lett kiválasztva

---

## Technikai megvalósítás

Valósítsd meg minimálisan, stabilan, auditálhatóan.

### Elvárás
- ne építs új külső infrastruktúrát
- ne használj Supabase-et, Notiont, n8n-t
- a megoldás a shared_workspace repón belül éljen
- a fájlok legyenek egyszerűen olvashatók és git-kompatibilisek

### Javasolt hely
A szükséges script(ek) mehetnek ide:

`/home/leoni/shared_workspace/ops/scripts/`

Ajánlott komponensek:

- egy kis script az ötlet hozzáadásához
- egy kis script a pontozáshoz és kiválasztáshoz
- egy kis script az aktív ötlet lezárásához
- opcionálisan egy wrapper, ami ezeket egységesen hívja

Ha egyszerűbb, lehet egyetlen script is.

---

## Működési sorrend

### Új ötlet esetén
1. beolvasás
2. mentés `ideas.jsonl`-be
3. ha nincs aktív ötlet: pontozás + kiválasztás
4. sprint task generálás
5. outbound státuszjelentés

### Done esetén
1. aktív ötlet lezárása
2. `state.json` frissítése
3. következő ötlet kiválasztása
4. új sprint task generálása
5. outbound státuszjelentés

---

## Fontos tiltások

- ne legyen egyszerre több aktív ötlet
- új ötlet ne írja felül a fókuszt
- ne generálj egyszerre több sprint taskot
- ne csinálj dashboardot
- ne építs túl bonyolult architektúrát
- ne bontsd szét multi-agent rendszerre, ha nem muszáj

---

## Kért eredmény

Készítsd el:

1. a szükséges fájlstruktúrát
2. a működő script(ek)et
3. a rövid README-t a `project_ideas/` alá
4. egy minta inicializálást
5. egy rövid outbound riportot arról, hogy a rendszer elkészült, hogyan kell használni, és milyen input formátumokat vár

---

## Használati parancsok / input minták

Támogatandó minták:

- `Új ötlet: ...`
- `done: IDEA_ID`
- `kill: IDEA_ID`

Ha hasznos, definiálj egy egyszerű, stabil parancsformátumot ezekre.

---

## Végső elv

A rendszer ne csak tároljon, hanem **kényszerítsen fókuszra**.

A döntési elv:
- a rendszer választ
- Tomi végrehajt
- új ötlet nem szakíthatja meg az aktuális aktívat
