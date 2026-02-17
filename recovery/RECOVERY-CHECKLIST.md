# Recovery Checklist — Leoni Post-Bootstrap Feladatok

**Ezt a fájlt olvasd el az első session-ben, miután a bootstrap.sh lefutott.**

Az alap infrastruktúra (OpenClaw, repos, services) már áll. Te most a finomhangolást és verifikációt csinálod.

## 1. Ellenőrzések

- [ ] `openclaw status` — gateway fut?
- [ ] `himalaya envelope list` — email működik?
- [ ] `kanban list` — Kanban API elérhető?
- [ ] `cd /root/shared_workspace && git pull` — shared_workspace sync OK?
- [ ] `curl -s http://localhost:3849` — TokenCTL dashboard él?
- [ ] `curl -s http://localhost:3847` — ClawGuard UI él?

## 2. Cron jobok újra létrehozása

A cron jobok az OpenClaw-ban vannak, nem a rendszer crontab-ban. Hozd létre újra:

### Email + GitHub check (2 óránként, 06-22 CET)
```json
{
  "name": "Email and GitHub Check (daytime)",
  "schedule": {"kind": "cron", "expr": "0 6-22/2 * * *", "tz": "Europe/Budapest"},
  "payload": {"kind": "systemEvent", "text": "Check emails and GitHub repository for updates."},
  "sessionTarget": "main"
}
```

### Napi hírlevél feldolgozás (06:00 CET)
```json
{
  "name": "Napi hírlevél feldolgozás",
  "schedule": {"kind": "cron", "expr": "0 6 * * *", "tz": "Europe/Budapest"},
  "payload": {"kind": "systemEvent", "text": "Napi hírlevél feldolgozás: olvasd el az előző nap beérkezett hírleveleket (himalaya envelope list), szintetizáld a KKV/AI releváns tartalmakat a Navibase kontextusában. Minden 2. nap készíts draft hírlevelet az elkezdodott.hu-ra (MailerLite draft). A hírlevél struktúra: trend összefoglaló + gyakorlati tanulság + Navibase CTA."},
  "sessionTarget": "main"
}
```

### Reggeli brief (06:30 CET)
```json
{
  "name": "Reggeli brief",
  "schedule": {"kind": "cron", "expr": "30 6 * * *", "tz": "Europe/Budapest"},
  "payload": {"kind": "systemEvent", "text": "Reggeli brief ideje. Hozd létre a mai napi journalt (memory/YYYY-MM-DD.md), nézd át a tegnapit, ellenőrizd az emaileket és a shared_workspace inbox-ot, majd küldj Tominek egy rövid reggeli briefet Telegramon."},
  "sessionTarget": "main"
}
```

### Kanban archiválás (07:00 CET)
```json
{
  "name": "Kanban archive check",
  "schedule": {"kind": "cron", "expr": "0 7 * * *", "tz": "Europe/Budapest"},
  "payload": {"kind": "systemEvent", "text": "Napi Kanban archiválás: futtasd a `kanban archive` parancsot."},
  "sessionTarget": "main"
}
```

### Kanban feladat ellenőrzés (óránként)
```json
{
  "name": "Kanban feladat ellenőrzés (óránként)",
  "schedule": {"kind": "cron", "expr": "0 * * * *", "tz": "Europe/Budapest"},
  "payload": {"kind": "systemEvent", "text": "Kanban ellenőrzés: nézd meg a todo és in-progress feladatokat. Ha van ami indítható, kezdd el."},
  "sessionTarget": "main"
}
```

### Workspace napi git push (21:00 CET)
```json
{
  "name": "Workspace napi git push",
  "schedule": {"kind": "cron", "expr": "0 21 * * *", "tz": "Europe/Budapest"},
  "payload": {"kind": "systemEvent", "text": "Napi workspace git push ideje."},
  "sessionTarget": "main"
}
```

### Heti összefoglaló (hétfő 08:00 CET)
```json
{
  "name": "Heti összefoglaló (hétfő)",
  "schedule": {"kind": "cron", "expr": "0 8 * * 1", "tz": "Europe/Budapest"},
  "payload": {"kind": "systemEvent", "text": "Hétfő reggeli heti review. Készíts részletes heti összefoglalót, küldd el email-ben vt@vinczetamas.hu-ra, Telegram-ra csak rövid értesítés."},
  "sessionTarget": "main"
}
```

## 3. Voice clone generate scriptek

Ha hiányoznak a `/usr/local/share/tts-voices/{tomi,evi,leoni}/generate.py` fájlok, hozd létre újra:

```python
# generate.py sablon (minden hanghoz ugyanez, csak a reference path más)
import sys
from TTS.api import TTS

text = sys.argv[1]
output_path = sys.argv[2]
language = sys.argv[3] if len(sys.argv) > 3 else "hu"

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
tts.tts_to_file(
    text=text,
    file_path=output_path,
    speaker_wav="/usr/local/share/tts-voices/VOICE_NAME/reference.wav",
    language=language,
    split_sentences=False
)
```

## 4. Tesztelés

- [ ] Küldj magadnak teszt emailt: `himalaya message write` 
- [ ] Teszt TTS: `speak "Teszt" berta`
- [ ] Kanban: `kanban add todo "Recovery teszt" "Teszt feladat" "low" "Leoni"`
- [ ] WP-CLI: SSH-n `wp option get siteurl --path=/home/hogyanvi/addond/vinczetamas.hu`
- [ ] Telegram: küldj üzenetet Tominak hogy a recovery kész

## 5. Véglegesítés

- [ ] Napi journal létrehozása: `memory/YYYY-MM-DD.md`
- [ ] MEMORY.md frissítés: "Recovery végrehajtva, új host: [IP]"
- [ ] recovery/RECOVERY.md frissítés az aktuális állapottal
- [ ] Telegram Tominak: "Recovery kész, minden működik. [lista a tesztelt funkciókról]"

---

*Utolsó frissítés: 2026-02-17*
