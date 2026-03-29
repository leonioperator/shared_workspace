# Idea Focus System

Minimál, determinisztikus ötlet- és fókuszrendszer.

## Fájlok
- `ideas.jsonl` - minden ötlet egy sor JSON objektum
- `state.json` - aktuális aktív ötlet állapota

## Parancsok
A fő script: `ops/scripts/idea_system.py`

### Új ötlet
```bash
python3 ops/scripts/idea_system.py add "Új ötlet szövege" --source telegram
```

### Inbox import
```bash
python3 ops/scripts/idea_system.py import-file inbox/idea-lista.md --source inbox
```

### Aktív ötlet lezárása
```bash
python3 ops/scripts/idea_system.py done IDEA_ID
```

### Ötlet elvetése
```bash
python3 ops/scripts/idea_system.py kill IDEA_ID
```

### Következő fókusz kiválasztása kézzel
```bash
python3 ops/scripts/idea_system.py select-next
```

### Állapot
```bash
python3 ops/scripts/idea_system.py status
```

## Input minták
- `Új ötlet: ...`
- `done: IDEA_ID`
- `kill: IDEA_ID`

## Szabályok
- egyszerre csak 1 aktív ötlet lehet
- új ötlet nem szakítja meg az aktív fókuszt
- minden aktív ötlethez pontosan 1 sprint task tartozik
- a rendszer a legjobb pontszámú ötletet aktiválja, ha nincs aktív
