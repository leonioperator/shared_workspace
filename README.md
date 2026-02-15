# shared_workspace — Tomi ↔ Leoni közös munkaterület

Ez a repo a közös asztalunk. Minden verziókövetett, minden visszanézhető.

## Mappák

### `inbox/`
**Tomi → Leoni irány.** Tomi ide tesz fájlokat (feladatok, utasítások, anyagok), és pusholja a repóba. Leoni minden heartbeat-kor (30 percenként) pullolja és feldolgozza a tartalmát.

**Fájl formátum:** `YYYYMMDD-slug.md` vagy bármilyen fájl
**Feldolgozás után:** Leoni áthelyezi a fájlt a `processed/` mappába.

### `processed/`
Feldolgozott inbox fájlok archívuma. Nem törlünk, visszakereshető marad.

### `outbound/`
**Leoni → külvilág irány.** Reportok, emailek, tartalmak, amiket Leoni készített és Tomi review-zza. Ami kész és jóváhagyott, innen megy tovább.

### `projects/`
Projekt fájlok, forráskódok, technikai anyagok. Pl. kanban board source.

### `writing/`
Blog tartalmak. Almappák:
- `drafts/` — készülő cikkek
- `published/` — publikált cikkek archívuma
- `archived/` — visszavont/elavult tartalmak

### `project_ideas/`
Közös brainstorm, ötletek, tervek. Bármelyikünk írhat ide.

### `recovery/`
Redirect a workspace repo recovery kitjéhez (elkerüli a duplikációt).

### `ops/`
Operatív fájlok, scriptek, konfig sablonok.

### `personal/`
Tomi személyes fájljai, amiket Leonival oszt meg.

## Workflow

```
1. Tomi feladatot ad:
   → Fájlt tesz az inbox/ mappába
   → git add + commit + push

2. Leoni feldolgozza (30 percenként check):
   → git pull
   → Elolvassa az inbox/ tartalmát
   → Végrehajtja a feladatot
   → Áthelyezi: inbox/fájl → processed/fájl
   → git add + commit + push

3. Leoni outputot készít:
   → outbound/ mappába teszi (report, draft, stb.)
   → git push
   → Telegramon jelzi Tominak

4. Tomi review-zza:
   → outbound/ vagy writing/drafts/ tartalmát nézi
   → Jóváhagyás vagy visszajelzés Telegramon
```

## Szabályok

- **SOHA nem kerül secret (API kulcs, jelszó) ebbe a repóba**
- Commit nyelv: angol
- Fájlnevek: dátum prefix ahol releváns (YYYYMMDD)
- Ha kérdés van: Telegram, nem commit message
