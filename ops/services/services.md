# Szolgáltatások

| Service | Port | Type | Leírás |
|---------|------|------|--------|
| openclaw-gateway | 18789 (loopback) | systemd user | OpenClaw gateway |
| clawguard | 3847 | systemd user | ClawGuard monitoring UI |
| kanban | 3848 | systemd system | Kanban board |
| tokenctl | 3849 | systemd system | Token usage dashboard |

## Systemd service fájlok
- `/etc/systemd/system/kanban.service`
- `/etc/systemd/system/tokenctl.service`
- `~/.config/systemd/user/clawguard.service`
- `~/.config/systemd/user/openclaw-gateway.service`
