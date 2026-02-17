# Incident Report: cp failed - directory not found

**Dátum:** 2026-02-17 14:02 UTC
**Súlyosság:** alacsony (nem volt adatvesztés, második futtatás sikeres)

## Mi történt

Blog draft másolása a shared_workspace-be sikertelen volt:
```
cp ~/.openclaw/workspace/artifacts/blog-elkezd-01.md ~/shared_workspace/writing/drafts/2026-02-17-harom-nap-ai-helyettes.md
```
Hiba: `No such file or directory` - a `writing/drafts/` mappa nem létezett.

## Root cause

A parancsok sorrendje hibás volt. A `cp` megelőzte a `mkdir -p`-t az `&&` láncban:
```bash
# HIBÁS (így futtattam):
cp source target && cd ~/shared_workspace && mkdir -p writing/drafts && git add...

# HELYES (ez kellett volna):
mkdir -p ~/shared_workspace/writing/drafts && cp source target && git add...
```

## Hatás

- Telegram-on hibaüzenet jelent meg Tominak
- Adatvesztés: nincs
- Második futtatás sikeres volt (javított sorrenddel)

## Megelőzés

1. `mkdir -p` mindig a `cp` ELŐTT
2. Alternatíva: `install -D source target` (automatikusan létrehozza a könyvtárat)
3. Shared_workspace repóban a szükséges mappák (`writing/drafts/`, `writing/published/`) előre létrehozva

## Azonnali javítás

A hiányzó mappákat most előre létrehozom a repóban, hogy ez többé ne fordulhasson elő.

---
*Készítette: Leoni, 2026-02-17*
