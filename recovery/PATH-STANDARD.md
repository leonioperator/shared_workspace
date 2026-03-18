# Recovery Path Standard

Kötelező szabály minden recovery fájlban:

- Ne használj hardcoded `/root/...` útvonalat.
- Home-relatív formát használj: `~/.openclaw/...`, `~/shared_workspace/...`.
- Scriptben mindig változókat használj:

```bash
BASE_HOME="${BASE_HOME:-$HOME}"
WORKSPACE_DIR="${WORKSPACE_DIR:-$BASE_HOME/.openclaw/workspace}"
SHARED_DIR="${SHARED_DIR:-$BASE_HOME/shared_workspace}"
```

Ha ettől eltérés kell, azt külön indokolni kell a fájl elején.
