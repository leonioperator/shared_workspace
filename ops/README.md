# ops/ — Operatív konfiguráció és dokumentáció

## Tartalom

### Szolgáltatások
| Szolgáltatás | Port | Service | Config |
|---|---|---|---|
| OpenClaw gateway | 18789 (localhost) | systemd user | ~/.openclaw/openclaw.json |
| ClawGuard | 3847 | systemd user | clawguard install |
| Kanban Board | 3848 | systemd system | /etc/systemd/system/kanban.service |

### Email
- Fiók: leoni.operator@vinczetamas.hu
- Kliens: himalaya
- Config: ~/.config/himalaya/config.toml
- IMAP: thsixtyfour.tarhely.eu:993 TLS
- SMTP: thsixtyfour.tarhely.eu:587 STARTTLS
- Folder aliases: INBOX.Sent, INBOX.Drafts, INBOX.Trash

### WordPress
- URL: vinczetamas.hu
- API user: leoni (admin)
- Auth: Application Password + CGIPassAuth On (.htaccess)
- Téma: GeneratePress + Custom CSS

### TTS/STT
- STT: faster-whisper (small modell, lokális, ingyenes)
- TTS operatív: sherpa-onnx Berta hang (lokális, ingyenes)
- TTS személyes: ElevenLabs turbo v2.5, custom voice
- CLI: `speak "szöveg"` (berta) vagy `speak "szöveg" leoni`
- CLI: `transcribe <fájl> hu`

### Cron jobok (OpenClaw)
| Job | Schedule (CET) | Leírás |
|---|---|---|
| Email/GitHub check | 30p, 06:30-21:30 | Email inbox + shared_workspace pull |
| Reggeli brief | 06:30 | Journal, review, brief Tominak |
| Heti összefoglaló | Hétfő 08:00 | Heti report, recovery check, verzió check |
| Workspace git push | 22:00 | Napi auto-commit + push |

### GitHub repók
| Repo | Hely | Cél |
|---|---|---|
| leonioperator/workspace | ~/.openclaw/workspace | Identity, memória, recovery |
| leonioperator/shared_workspace | /root/shared_workspace | Közös munkaterület |
