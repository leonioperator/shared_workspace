# Recovery

> Path standard: lásd `PATH-STANDARD.md` (kötelező).

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


## Aktuális infra állapot (2026-03)

- **dn-platform-01**: AI/automation control plane (OpenClaw, n8n, kanban, tokenctl, TTS)
- **dn-web-01**: public web node, IP: `46.224.110.90` (Nginx + Astro)
- **dn-dev-01**: forex/trading infra (MT4, EA, trading bot), izolált rendszer

Architektúra elv:
- platform = compute/logika
- web = prezentáció
- forex = pénzügyi motor
