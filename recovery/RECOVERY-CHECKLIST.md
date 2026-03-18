# Recovery Checklist — Leoni Post-Bootstrap

> Path standard: lásd `PATH-STANDARD.md` (kötelező).

Ezt a fájlt az első sessionben kövesd, miután a bootstrap lefutott.

## 0) Alapútvonalak (NE fix /root)

```bash
BASE_HOME="${BASE_HOME:-$HOME}"
WORKSPACE_DIR="${WORKSPACE_DIR:-$BASE_HOME/.openclaw/workspace}"
SHARED_DIR="${SHARED_DIR:-$BASE_HOME/shared_workspace}"
RECOVERY_DIR="${RECOVERY_DIR:-$SHARED_DIR/recovery}"
```

Minden további példa ezekre épül.

## 1) Ellenőrzések

- [ ] `openclaw status` — gateway fut
- [ ] `himalaya envelope list` — email működik
- [ ] `kanban list` — Kanban API elérhető
- [ ] `cd "$SHARED_DIR" && git pull` — shared_workspace sync OK
- [ ] `curl -s http://localhost:3849` — TokenCTL él
- [ ] `curl -s http://localhost:3847` — ClawGuard él

## 2) Cron jobok újra létrehozása

OpenClaw cronban hozd létre, nem system crontabban.

- Email + GitHub check (2 óránként, 06-22 CET)
- Napi hírlevél + tartalomjel feldolgozás (06:00 CET)
- Reggeli brief (06:30 CET)
- Kanban archive (07:00 CET)
- Kanban ellenőrzés (óránként)
- Workspace napi git push (21:00 CET)
- Heti összefoglaló (hétfő 08:00 CET)

Megjegyzés: az aktuális, éles cron-konfigot mindig a futó gatewayből exportáld (`openclaw cron list`), ne régi statikus példából indulj.

## 3) TTS / Voice

- [ ] Teszt TTS: `speak "Teszt" berta`
- [ ] Ha hiányzik Berta runtime/model, állítsd helyre a sherpa-onnx toolchain-t `~/.openclaw/tools/...` útvonalon
- [ ] Voice clone scriptek helye: `/usr/local/share/tts-voices/{tomi,evi,leoni}/generate.py`

## 4) Tesztelés

- [ ] Email teszt olvasás
- [ ] Kanban teszt task létrehozás
- [ ] Telegram üzenetküldés teszt
- [ ] OpenClaw model/auth ellenőrzés

## 5) Véglegesítés

- [ ] Napi journal: `memory/YYYY-MM-DD.md`
- [ ] `MEMORY.md` frissítés: recovery és host állapot
- [ ] `recovery/RECOVERY.md` frissítés
- [ ] Rövid készre jelentés Telegramon

---

Utolsó frissítés: 2026-03-18
