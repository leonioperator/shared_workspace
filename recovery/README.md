# Recovery

Recovery dokumentáció célja: új hoston gyors, reprodukálható helyreállítás.

## Útvonal szabály

A recovery leírásokban ne használj fix `/root/...` útvonalat.
Használj home-relatív formát:

- `~/.openclaw/...`
- `~/shared_workspace/...`
- `~/shared_workspace/recovery/...`

Ha scriptben kell, használd ezt a mintát:

```bash
BASE_HOME="${BASE_HOME:-$HOME}"
WORKSPACE_DIR="${WORKSPACE_DIR:-$BASE_HOME/.openclaw/workspace}"
SHARED_DIR="${SHARED_DIR:-$BASE_HOME/shared_workspace}"
```

## Forrás

A teljes recovery anyagok a shared_workspace `recovery/` mappában vannak.
