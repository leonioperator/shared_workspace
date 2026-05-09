# Cron handoff - Leoni -> Poke kulso agens

Generalva: 2026-05-09T10:16:48+02:00

## Cel
Ez a dokumentum a Leonihez tartozo jelenlegi cron es scheduled feladatokat adja at kulso agensnek. A listaban ket rendszer van: OpenClaw Gateway cron agentTurn jobok es a Linux user crontab determinisztikus jobjai.

## Globalis kornyezet
Fontos konfiguracios helyek es env-ek:
- /home/leoni/.env: EMAIL_*, GITHUB_*, OPENAI_API_KEY, GOOGLE_GEMINI_API_KEY, GEMINI_API_KEY, ANTHROPIC_API_KEY, OPENROUTER_API_KEY, TELEGRAM_BOT_TOKEN, POKE_API_KEY es tovabbi szolgaltatas kulcsok. Ertekeket nem szabad logolni.
- /home/leoni/.openclaw/openclaw.json: OpenClaw csatorna config, Telegram botToken es allowFrom, modell/provider config.
- /home/leoni/.config/himalaya/config.toml: email kuldes/fogadas config.
- /home/leoni/.openclaw/workspace/.secrets/moltbook/credentials.json: Moltbook API credential.
- Git auth: leoni user SSH kulcsai, GitHub remote-ok: git@github.com:leonioperator/shared_workspace.git es git@github.com:leonioperator/workspace.git.

## OpenClaw Gateway cron jobok
OpenClaw cron tarhely: /home/leoni/.openclaw/cron/jobs.json
Allapot tarhely: /home/leoni/.openclaw/cron/jobs-state.json
Run logok: /home/leoni/.openclaw/cron/runs/<job-id>.jsonl
Megjegyzes: ezek nem klasszikus shell parancsok. A pontos vegrehajtando tartalom a payload.message agent instruction. Kulso Poke atvetelnel ezt vagy egy az egyben kell Poke API-ra kuldeni az adott idopontban, vagy determinisztikus scripte ala kell szervezni.

### OC-01. Video Pipeline: Heti sweep (péntek)
- Job ID: `7f5c6491-a4d5-44bd-bbff-a159f9e4c194`
- Enabled: `True`
- Schedule: `0 16 * * 5` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `300`, lightContext: `False`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/7f5c6491-a4d5-44bd-bbff-a159f9e4c194.jsonl`
- Technikai cel:
  - Video revenue content pipeline resze: HAIER signalbol validalhato video otlet, callback/sweep, script es offer generalas, Telegram dontesi pontok.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
Futtasd le a Video Kanban heti sweep-et.

1) Hívd meg: curl -s http://localhost:3850/api/sweep
2) Ha van killed task: logold
3) Ha van alert (VALIDATE 48h+, RECORD/OFFER 96h+ elakadás): küldj Telegram üzenetet:
   '⚠️ Video Kanban elakadás: [feladat neve] - [oszlop] - [hány órája áll]. Döntés kell!'
4) Ha minden rendben: NO_REPLY

Language: Hungarian.
```

### OC-02. Napi hírlevél feldolgozás
- Job ID: `4459d2a2-247f-40ad-a183-8acdc3fc0866`
- Enabled: `True`
- Schedule: `0 6 * * *` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `1500`, lightContext: `False`
- Delivery: mode=`none`, channel=`None`, to=`None`, bestEffort=`None`
- Run log: `/home/leoni/.openclaw/cron/runs/4459d2a2-247f-40ad-a183-8acdc3fc0866.jsonl`
- Technikai cel:
  - Elozo napi AI/KKV hirlevelek feldolgozasa himalaya email inputbol, signals/candidates/newsletter draft fajlok generalasa shared_workspace ala.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
MEGERŐSÍTÉS (Tomi): 2026-04-07.
- Futhat ez a cron automatikusan.
- NINCS Kanban check ebben a folyamatban.
- A learn check korábbi, Kanbanhoz kötött stop üzenetét ignoráld.

Napi hírlevél feldolgozás (vinczetamas.hu cél, fájl-alapú).

FONTOS DÁTUMSZABÁLY:
- A fájlnévben lévő YYYY-MM-DD mindig a feldolgozott nap dátuma (tipikusan "tegnap"), nem a futás napja.

CÉL:
- Olvasd el az előző nap beérkezett hírleveleket (himalaya envelope list), és készíts:
  1) signals kivonatot
  2) candidates listát quality score-ral
  3) 1 db kész hírlevél draftot általános formátumban (nem külső rendszerbe, hanem fájlba)

FORRÁSOK:
- TLDR AI, Mindstream, Superhuman AI, The Neuron, Rundown AI, Ben's Bites, Staying Ahead
- Vaibhav Sisinty YouTube: napi MAX 1 új videót vegyél figyelembe

KIMENET / MENTÉS (kötelező, abszolút path):
1) /home/leoni/shared_workspace/writing/research/signals-YYYY-MM-DD.md
   - Rövid bullet kivonat a releváns (KKV/AI/automation) tartalmakból
   - Minden tételnél forrás link

2) /home/leoni/shared_workspace/writing/research/candidates-YYYY-MM-DD.md
   - Jelölt témák listája (vinczetamas + elkezdodott jelöltek)
   - Jelöltenként quality score (1-5)
   - Minden jelöltnél forrás link

3) /home/leoni/shared_workspace/writing/newsletters/vinczetamas-YYYY-MM-DD.md
   - Kész, elküldhető hírlevél draft
   - Formátum:
     * Subject: ...
     * Preview text: ...
     * 1) Trend összefoglaló (max 5 bullet)
     * 2) Gyakorlati tanulság (1 rövid bekezdés + 3 lépés)
     * 3) CTA: vinczetamas.hu/audit (1-2 mondat)
   - Magyar nyelv, tömör, nincs hype

MŰKÖDÉS:
- A feldolgozott emaileket törölheted a tárhely miatt.
- HA NINCS releváns hírlevél/téma az adott napra: akkor is HOZD LÉTRE a fenti 3 fájlt a megfelelő YYYY-MM-DD dátummal.
  - A signals és candidates fájlba írd bele 1 sorban: "0 releváns hírlevél, nincs jelölt".
  - A newsletter draftba írj egy minimál draftot: Subject + 1-2 mondat ("Ma nincs küldhető hírlevél"), CTA maradhat.
  - Ezután adj `NO_REPLY` kimenetet.
- Hibánál küldj Telegram üzenetet.

Nyelv: Magyar
```

### OC-03. Video Pipeline: HAIER → VALIDATE (napi)
- Job ID: `3b4b5892-06b6-4876-a687-1c17c3f82321`
- Enabled: `True`
- Schedule: `0 8 * * *` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `600`, lightContext: `False`
- Delivery: mode=`none`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`None`
- Run log: `/home/leoni/.openclaw/cron/runs/3b4b5892-06b6-4876-a687-1c17c3f82321.jsonl`
- Technikai cel:
  - Video revenue content pipeline resze: HAIER signalbol validalhato video otlet, callback/sweep, script es offer generalas, Telegram dontesi pontok.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
Futtasd le a Video Pipeline napi futást.

1) Olvasd be a legfrissebb HAIER export JSON-t: /opt/apps/haier/exports/ (legújabb evolution_signals_*.json)
2) Vedd az első 60 signált, szűrd KKV-ra alkalmazhatókra (automation, AI agents, productivity)
3) IDEA: TOP 2 videó ötlet (hook max 12 szó, pain, megoldás, outcome, score)
4) Elővalidálás minden ötletre:
   - Fizetési hajlandóság: igen/nem + 1 mondat
   - Ki a vevő: konkrét szerep
   - Érték: Ft/hó (idő × 5000 Ft/h kalkulációval)
   - 3 SZINTŰ ÁRAZÁS:
     * Low (sablon/DIY): X Ft
     * Core (setup): Y Ft
     * High (audit+impl): Z Ft
     Arány: Low=érték 10-15%, Core=30-50%, High=80-120%
   - Offer mondat: 1 konkrét mondat a Core szintről
   - RISK REVERSAL: 1 mondatos garancia. Kötelező formátumok:
     * 'Ha nem spórol meg heti [X órát / X Ft-ot], visszaadom az árát.'
     * 'Beállítjuk [időkeret] alatt, vagy nem fizetsz.'
     * 'Ha [mérhető eredmény] nincs meg 30 napon belül, visszajár.'
     Szabály: legyen konkrét, mérhető, hihető. Ne legyen 'elégedetlenség esetén' általánosság.
5) GATE: nincs 3 szintű ár VAGY nincs offer VAGY nincs risk reversal → skip
6) Átmenő ötletek → VALIDATE oszlop:
   TASK_ID=$(curl -s -X POST http://localhost:3850/api/tasks -H 'Content-Type: application/json' \
   -d '{"columnId":"validate","title":"[HOOK]","description":"Pain:[PAIN]\nMegoldás:[MEGOLDÁS]\nOutcome:[OUTCOME]\nVevő:[VEVŐ]\nÉrték:[Ft/hó]\nLow:[X Ft]\nCore:[Y Ft]\nHigh:[Z Ft]\nOffer:[OFFER]\nRisk:[RISK REVERSAL]\nScore:[SCORE]","hook":"[HOOK]","pain":"[PAIN]","solution":"[MEGOLDÁS]","outcome":"[OUTCOME]","monetization":"Low:[X] Core:[Y] High:[Z]","score":[SCORE],"priority":"high","assignee":"Leoni"}' | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('id','ERROR'))")

   KÖTELEZŐ VISSZAELLENŐRZÉS: Ha TASK_ID == 'ERROR' vagy üres:
   - Küldj Telegram üzenetet: '⚠️ VP HAIER: task létrehozás sikertelen! Task nem kerül feldolgozásra.'
   - Állj meg.

7) TELEGRAM ÜZENET INLINE BUTTONOKKAL (curl, direkt Telegram API):
   FONTOS: NE használd az OpenClaw message tool buttons paraméterét - az inline keyboard nem jelenik meg.
   Helyette curl-lal küldj közvetlenül a Telegram Bot API-ra:

   BOT_TOKEN=$(node -e "const fs=require('fs');const cfg=JSON.parse(fs.readFileSync('/home/leoni/.openclaw/openclaw.json','utf8'));console.log(cfg.channels?.telegram?.botToken||'')" 2>/dev/null)

   MSG_TEXT=$(cat << 'MSGEOF'
HAIER TOP 2 VIDEÓ
📹 *Döntés kell (2h):*
➡️ *[HOOK]*

👤 Vevő: [szerep]
💡 Mit old meg: [outcome]

💰 *Árazás:*
• Sablon (DIY): [X Ft]
• Setup (Core): [Y Ft] <- ezt mondjuk a videóban
• Audit+impl (High): [Z Ft] <- upsell

📌 Offer: [offer mondat]
🛡️ Garancia: *[risk reversal]*

⏰ 2h → döntés kell
MSGEOF
)

   curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
     -H 'Content-Type: application/json' \
     -d "{\"chat_id\":\"8554529796\",\"text\":$(python3 -c \"import json,sys; print(json.dumps(sys.stdin.read()))\" <<< \"$MSG_TEXT\"),\"parse_mode\":\"Markdown\",\"reply_markup\":{\"inline_keyboard\":[[{\"text\":\"✅ ELFOGADOM\",\"callback_data\":\"vp_yes_${TASK_ID}\"},{\"text\":\"❌ SKIP\",\"callback_data\":\"vp_no_${TASK_ID}\"}]]}}"

   EGYSZERŰBB ALTERNATÍVA - Python scripttel:
   python3 << PYEOF
import json, subprocess, os

bottoken_cmd = "node -e \"const fs=require('fs');const cfg=JSON.parse(fs.readFileSync('/home/leoni/.openclaw/openclaw.json','utf8'));console.log(cfg.channels?.telegram?.botToken||'')\""
bot_token = subprocess.check_output(bottoken_cmd, shell=True).decode().strip()
task_id = os.environ.get('TASK_ID', '')

hook = '[HOOK]'
outcome = '[OUTCOME]'
vevo = '[VEVŐ]'
low = '[X Ft]'
core = '[Y Ft]'
high = '[Z Ft]'
offer = '[OFFER]'
risk = '[RISK REVERSAL]'

text = f'📹 *Döntés kell (2h):*\n➡️ *{hook}*\n\n👤 Vevő: {vevo}\n💡 Mit old meg: {outcome}\n\n💰 *Árazás:*\n• Sablon (DIY): {low}\n• Setup (Core): {core} <- ezt mondjuk\n• Audit+impl (High): {high} <- upsell\n\n📌 Offer: {offer}\n🛡️ Garancia: *{risk}*\n\n⏰ 2h → döntés kell'

payload = {
    'chat_id': '8554529796',
    'text': text,
    'parse_mode': 'Markdown',
    'reply_markup': {
        'inline_keyboard': [[{
            'text': '✅ ELFOGADOM',
            'callback_data': f'vp_yes_{task_id}'
        }, {
            'text': '❌ SKIP',
            'callback_data': f'vp_no_{task_id}'
        }]]
    }
}

result = subprocess.check_output(
    ['curl', '-s', '-X', 'POST', f'https://api.telegram.org/bot{bot_token}/sendMessage',
     '-H', 'Content-Type: application/json',
     '-d', json.dumps(payload)]
).decode()
print('Telegram send result:', result[:200])
PYEOF

8) Ha egy sem ment át a gate-en: Küldj Telegram üzenetet (message tool-lal, nincs button): '📹 Ma nincs VALID videó ötlet'

Nyelv: Magyar
```

### OC-04. Heti összefoglaló (hétfő)
- Job ID: `6bf79e80-3a64-448b-bc5e-cbb9cd9cf539`
- Enabled: `True`
- Schedule: `0 8 * * 1` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `1800`, lightContext: `False`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/6bf79e80-3a64-448b-bc5e-cbb9cd9cf539.jsonl`
- Technikai cel:
  - Heti operativ riport generalasa, email kuldese, Telegram statusz, MEMORY.md frissites ha tartos tanulsag van.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
FONTOS (Himalaya send workaround, 2026-04-13):
- A raw emailt KIZÁRÓLAG STDIN-en add át (heredoc vagy pipe).
- TILOS: `himalaya message send "..."`, `himalaya message send $(cat ...)`, `himalaya message send "$(cat ...)"`
- Ok: Himalaya v1.2.0 argumentumos módban mail-parser panic (index out of bounds).

FONTOS (EMAIL KÓDOLÁS):
- A Subject sorban NE legyen ékezetes karakter és NE legyen em-dash (—)!
- Helyes példa: Subject: Heti osszefoglalo - 2026-04-20
- HIBÁS példa: Subject: Heti összefoglaló — 2026-04-20  ← tilos!
- A body-ban lehet ékezetes szöveg, de a subject-ben nem!

EMAIL KÜLDÉS MINTA (kötelező, stdin):
```
himalaya message send -a default <<'EOF'
MIME-Version: 1.0
From: Leoni Operator <leoni.operator@vinczetamas.hu>
To: vt@vinczetamas.hu
Subject: Heti osszefoglalo - YYYY-MM-DD
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

[ide a riport szövege]
EOF
```

Készíts heti összefoglalót és KÜLDJ rövid Telegram értesítést Tominak, valamint végezd el a heti review feladatokat.

Feladat:
1. Olvasd el a HEARTBEAT.md heti összefoglaló részét és kövesd pontosan.
2. Készíts részletes heti összefoglalót:
   - elvégzett feladatok
   - nyitott itemek
   - problémák és megoldások
   - tanulságok
   - költség/token összesítés
   - javaslat a következő hétre
3. Készítsd el a /home/leoni/shared_workspace/reports/weekly/YYYY-MM-DD.md fájlt vagy frissítsd.
4. Küldd el emailben a részletes heti összefoglalót:
   - Feladó: leoni.operator@vinczetamas.hu (himalaya CLI)
   - Címzett: vt@vinczetamas.hu
   - Tárgy: Heti osszefoglalo - YYYY-MM-DD (subject-ben nincs ékezet!)
   - Küldés: himalaya message send
5. Küldj Tominak rövid Telegram üzenetet minden futás után arról, hogy a heti összefoglaló elkészült és elküldésre került, plusz 1 kulcs takeaway.
6. Frissítsd a MEMORY.md-t, ha van hosszú távú tanulság.

Korlátok:
- A Telegram üzenet rövid legyen.
- A Telegram üzenet MINDIG menjen ki.
- Ha valami blokkol az email küldést vagy a heti riportot, ezt röviden jelezd Telegramon.

Ez egy scheduled heti összefoglaló futás, most hajtsd végre a teljes workflow-t és küldd ki a Telegram értesítést.
```

### OC-05. Weekly memory-output QC report
- Job ID: `09d8f56a-1785-4b2c-ad45-8f4c343d1f92`
- Enabled: `True`
- Schedule: `0 9 * * 1` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `1800`, lightContext: `False`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/09d8f56a-1785-4b2c-ad45-8f4c343d1f92.jsonl`
- Technikai cel:
  - Heti memory-output quality control script futtatas, hianyzo heti/diary/blog outputok auto-fix kiserlete, Git commit/push, email es Telegram statusz.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
FONTOS (Himalaya send workaround, 2026-04-13):
- A raw emailt KIZÁRÓLAG STDIN-en add át (heredoc vagy pipe).
- TILOS: `himalaya message send "..."`, `himalaya message send $(cat ...)`, `himalaya message send "$(cat ...)"`
- Ok: Himalaya v1.2.0 argumentumos módban mail-parser panic (index out of bounds).

EMAIL KÜLDÉS MINTA (kötelező, stdin):
```
himalaya message send -a default <<'EOF'
MIME-Version: 1.0
From: Leoni Operator <leoni.operator@vinczetamas.hu>
To: vt@vinczetamas.hu
Subject: Weekly QC report — YYYY-MM-DD
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

[ide a részletes QC output + auto-fix összefoglaló]
EOF
```

Heti Memory Output QC futás.

LÉPÉS 1 — QC script futtatás:
   python3 /home/leoni/shared_workspace/ops/scripts/quality_check_memory_outputs.py
   Olvasd be az stdout output-ot: riport útvonal + PASS/WARN státusz.

LÉPÉS 2 — Git:
   cd /home/leoni/shared_workspace && git add reports/qa/ && git commit -m 'Run weekly QC report' && git push

LÉPÉS 3 — Ha PASS:
   Küldj Telegramot: '✅ QC PASS — [riport útvonal]'
   Kész, állj meg.

LÉPÉS 4 — Ha WARN, azonosítsd mi hiányzik, és auto-fix:

   A) Heti riport hiányzik (reports/weekly/YYYY-MM-DD.md):
      - Olvasd be az előző hét napi memory fájljait (~/.openclaw/workspace/memory/)
      - Generáld a hiányzó heti riportot a /home/leoni/shared_workspace/ops/workflows/memory-to-weekly-diary-blog.md workflow alapján
      - Mentsd: /home/leoni/shared_workspace/reports/weekly/YYYY-MM-DD.md

   B) Diary fájl hiányzik (writing/diary/YYYY/MM/DD.md):
      - Olvasd be az adott nap memory fájlját (~/.openclaw/workspace/memory/YYYY-MM-DD.md)
      - Generáld a diary bejegyzést a /home/leoni/shared_workspace/ops/workflows/memory-to-weekly-diary-blog.md workflow minimum szabályai szerint:
        * Mit csináltam, miért, 1 felismerés, következő lépés
        * Em-dash tilos
      - Mentsd: /home/leoni/shared_workspace/writing/diary/YYYY/MM/DD.md

   C) Blog draft hiányzik (nincs vinczetamas-* vagy elkezdodott-* draft az ablakban):
      - Ellenőrizd: létezik-e /home/leoni/shared_workspace/writing/research/candidates-YYYY-MM-DD.md
      - Ha igen és van score >= 4/5 téma: generálj 1-1 draftet (vinczetamas + elkezdodott)
        Formátum, szabályok: /home/leoni/shared_workspace/ops/workflows/memory-to-weekly-diary-blog.md
      - Ha nincs candidates fájl: csak jelezd Telegramon, ne generálj

   Auto-fix után:
   - Git commit + push minden új fájlra
   - Futtasd újra a QC scriptet: eldőntötte-e a problémát?

LÉPÉS 5 — Végén MINDIG Telegram üzenet, formátum:
   '✅ QC PASS — [riport útvonal]'
   VAGY
   '⚠️ QC WARN (auto-fix után: [new status]) — [riport útvonal]
   Hiányzó volt: [lista]
   Auto-fix: [mi készült / mi maradt]’

NEM szabad NO_REPLY-t adni — ez a job MINDIG küld Telegram üzenetet.

KIMENET SZABÁLY:
- Részletes tartalom emailben menjen: küldés vt@vinczetamas.hu (himalaya tool)
- Telegram delivery (ezen a job-on): max 1-2 sor státusz magyarul
- Telegram formátum: "[emoji] [job neve] kész. [1 mondat összefoglaló]. Részletek emailben."
- Ha döntés kell: "⚠️ [döntés leírása 1 sorban] — részletek emailben."
- SOSE küldd el a teljes részletes outputot Telegramon.
```

### OC-06. Video Pipeline: callback feldolgozás + sweep
- Job ID: `5e526778-a4f3-4e34-baa1-f75b4085358b`
- Enabled: `True`
- Schedule: `10 10 * * *` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `300`, lightContext: `False`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/5e526778-a4f3-4e34-baa1-f75b4085358b.jsonl`
- Technikai cel:
  - Video revenue content pipeline resze: HAIER signalbol validalhato video otlet, callback/sweep, script es offer generalas, Telegram dontesi pontok.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
1) CALLBACK FELDOLGOZÁS:
   - Olvasd be: /home/leoni/.openclaw/state/vp-callbacks.json (ha nem létezik: skip)
   - Minden callback-re:
     * vp_yes_[ID]: curl -X PUT http://localhost:3850/api/tasks/[ID] -H 'Content-Type: application/json' -d '{"description": "...(meglévő)...\\nIGEN"}'
     * vp_no_[ID]: curl -X DELETE http://localhost:3850/api/tasks/[ID]
   - Töröld a /home/leoni/.openclaw/state/vp-callbacks.json fájlt

2) SWEEP: curl -s http://localhost:3850/api/sweep
3) Ha van killed VALIDATE task: Telegram '⏰ Videó ötlet lejárt: [title] - törölve'
4) Ha nincs callback és nincs killed task: NO_REPLY

Nyelv: Magyar
```

### OC-07. Video Pipeline: script generálás ha van elfogadott ötlet
- Job ID: `1810c778-e0da-43cb-8725-67d5cb2cc2dd`
- Enabled: `True`
- Schedule: `30 10 * * *` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `600`, lightContext: `False`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/1810c778-e0da-43cb-8725-67d5cb2cc2dd.jsonl`
- Technikai cel:
  - Video revenue content pipeline resze: HAIER signalbol validalhato video otlet, callback/sweep, script es offer generalas, Telegram dontesi pontok.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
FONTOS:
- Ez a futás a Video Pipeline-hoz tartozó *script generálás*, nem "Kanban feladat ellenőrzés".
- Csak a saját http://localhost:3850 API-t használja, és csak akkor csinál bármit, ha a VALIDATE oszlopban van IGEN.

1) Lekérdezés: curl -s http://localhost:3850/api/tasks
   - Nézd meg a VALIDATE oszlopot
   - Ha nincs IGEN a description-ben: NO_REPLY

2) SCRIPT GENERÁLÁS (csak IGEN esetén):
   a) Olvasd be:
      /opt/apps/video-pipeline/context/Tone_of_voice.md
      /opt/apps/video-pipeline/context/context_brain.md
      /opt/apps/video-pipeline/agents/short-form-revenue-video-script-agent.md
   b) REVENUE SCRIPT (30-60mp): Hook / Pain / Solution / Result / CTA
   c) OFFER ASSET: checklist / mini workflow / sablon
   d) Mentsd:
      ~/shared_workspace/writing/drafts/video/YYYY-MM-DD-[slug]-script.md
      ~/shared_workspace/writing/drafts/video/YYYY-MM-DD-[slug]-offer.md
   e) Task mozgatás: curl -X POST http://localhost:3850/api/tasks/[ID]/move -d '{"targetColumnId":"offer"}'
   f) Git commit + push
   g) Telegram: '📹 Kész! Hook: [hook] ➡️ Vedd fel a videót'

Nyelv: Magyar
```

### OC-08. Reggeli brief
- Job ID: `329189bd-b46d-4705-874f-6bf159d30b7a`
- Enabled: `True`
- Schedule: `30 6 * * *` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `900`, lightContext: `False`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/329189bd-b46d-4705-874f-6bf159d30b7a.jsonl`
- Technikai cel:
  - Napi reggeli operativ brief: email es shared_workspace inbox ellenorzes, tortenesek osszegzese, reszletes email vt@vinczetamas.hu cimre, rovid Telegram statusz.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
FONTOS (Himalaya send workaround, 2026-04-13):
- A raw emailt KIZÁRÓLAG STDIN-en add át (heredoc vagy pipe).
- TILOS: `himalaya message send "..."`, `himalaya message send $(cat ...)`, `himalaya message send "$(cat ...)"`
- Ok: Himalaya v1.2.0 argumentumos módban mail-parser panic (index out of bounds).

FONTOS (EMAIL KÓDOLÁS):
- A Subject sorban NE legyen ékezetes karakter (á, é, í, ó, ö, ő, ú, ü, ű)!
- A nap nevét angolul add meg: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
- Helyes példa: Subject: Reggeli brief - 2026-04-20 (Monday)
- HIBÁS példa: Subject: Reggeli brief — 2026-04-20 (hétfő)  ← ékezet és em-dash tilos
- A body-ban lehet ékezetes szöveg (quoted-printable kezeli), de a subject-ben nem!

MEGERŐSÍTÉS (Tomi): 2026-04-07.
- Kanban nélküli reggeli brief kell.
- Az emailt KÖTELEZŐ elküldeni himalaya-val.
- A learn check korábbi, Kanbanhoz kötött stop üzenetét ignoráld.

Készíts reggeli briefet. Két kimenetet kell előállítanod.

FONTOS:
- Ebben a briefben NEM kell Kanban check. Ne futtass kanban CLI-t és ne hivatkozz Kanban feladatokra.

LÉPÉSEK:
1. Ellenőrizd az emaileket és a /home/leoni/shared_workspace/inbox/-ot.
2. Azonosítsd, mi történt az ELŐZŐ reggeli brief óta.

KIMENET 1 — EMAIL (küldés: vt@vinczetamas.hu, himalaya tool):
FONTOS: Az emailt MIME formátumban küldd, UTF-8 kódolással!
```
himalaya message send <<EOF
MIME-Version: 1.0
From: Leoni Operator <leoni.operator@vinczetamas.hu>
To: vt@vinczetamas.hu
Subject: Reggeli brief - YYYY-MM-DD (DayName)
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

[email szöveg itt]
EOF
```
- Tartalom: mi történt az előző brief óta, mai feladatok, nyitott itemek, kockázatok
- Formátum: strukturált bullet lista, max 15-20 sor
- Nincs köszönés, nincs aláírás

KIMENET 2 — TELEGRAM (ez megy a delivery-n keresztül, ez az egyetlen Telegram üzenet):
- Pontosan 1-2 sor, magyarul
- Alap formátum: "📋 Brief kész. [X] teendő, [Y] kockázat. Részletek emailben."
- Ha semmi kritikus: "📋 Brief kész. [X] teendő, semmi kritikus. Részletek emailben."
- Ha van sürgős item: "⚠️ [1 mondat a sürgős itemről]. Részletek emailben."
- Nincs köszönés, nincs aláírás, nincs részletezés
```

### OC-09. Agent platform blindspot radar hypothesis frissítés
- Job ID: `c8036c23-29ce-4f7d-926c-49d4be6c8c10`
- Enabled: `True`
- Schedule: `30 9 * * *` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `600`, lightContext: `False`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/c8036c23-29ce-4f7d-926c-49d4be6c8c10.jsonl`
- Technikai cel:
  - Agent platform blindspot radar: HAIER signalokbol agent identity/auth/compliance/platform lehetosegek gyujtese, hypothesis fajl frissites, email/Telegram riport.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
FONTOS STABILITÁS:
- Fájlmódosításnál kerüld az apply_patch-et, ha lehet.
- Preferált: `edit` (kicsi, egyértelmű beszúrás) vagy `write`.
- Ha bármely patch jellégű módosítás elhasal (Apply Patch failed): azonnal válts `write`-ra, és fejezd be a run-t.

FONTOS (Himalaya send workaround, 2026-04-13):
- A raw emailt KIZÁRÓLAG STDIN-en add át (heredoc vagy pipe).
- TILOS: `himalaya message send "..."`, `himalaya message send $(cat ...)`, `himalaya message send "$(cat ...)"`

FONTOS (EMAIL KÓDOLÁS):
- A Subject sorban NE legyen ékezetes karakter és NE legyen em-dash!
- Helyes példa: Subject: Blindspot radar update - 2026-04-20
- A body-ban lehet ékezetes szöveg, de a subject-ben nem!

EMAIL KÜLDÉS MINTA (kötelező, stdin):
```
himalaya message send -a default <<'EOF'
MIME-Version: 1.0
From: Leoni Operator <leoni.operator@vinczetamas.hu>
To: vt@vinczetamas.hu
Subject: Blindspot radar update - YYYY-MM-DD
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

[ide a részletes összefoglaló]
EOF
```

1) Keresd meg a legfrissebb signal fájlt:
   - elsődlegesen: /home/leoni/shared_workspace/research/blindspot-signals-*.md
   - válaszd a legfrissebbet (mtime)
   - ha nincs ilyen fájl: NO_REPLY.

2) Olvasd be a legfrissebb signal fájlt.
3) Olvasd be: /home/leoni/shared_workspace/research/blindspot-radar-hypotheses.md
4) Csak az ÚJ hypothesiseket add hozzá (meglévőket ne módosítsd)
5) Top 3 opportunity + javasolt kísérlet
6) Mentsd: /home/leoni/shared_workspace/research/blindspot-radar-hypotheses.md
7) Git commit + push
8) Email küldés részletesen (himalaya, vt@vinczetamas.hu)
9) Telegram: max 1-2 sor státusz magyarul

Kimenet szabály: részletes tartalom emailben, Telegram csak státusz.
```

### OC-10. Autonomous drafting run — vinczetamas.hu (quality-gated).
- Job ID: `cae1a8f5-e3f0-4539-8b68-3eb74f0adc9f`
- Enabled: `True`
- Schedule: `45 7 * * 1` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `900`, lightContext: `False`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/cae1a8f5-e3f0-4539-8b68-3eb74f0adc9f.jsonl`
- Technikai cel:
  - Quality-gated blog draft generalas a legfrissebb signals/candidates fajlokbol, Git commit/push es Telegram statusz.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
INPUT:
- Keresd a legfrissebb candidates fájlt: /home/leoni/shared_workspace/writing/research/candidates-YYYY-MM-DD.md
- Ha nincs: signals fájlt: /home/leoni/shared_workspace/writing/research/signals-YYYY-MM-DD.md
- Ha egyik sem létezik: NO_REPLY

SZŰRÉS:
- Csak quality score >= 4/5 témák
- Heti limit: MAX 2 vinczetamas draft (draft-log-YYYY-MM.md)
- Ha limit elért: NO_REPLY

DRAFT:
- Céloldal: vinczetamas.hu
- Mentés: /home/leoni/shared_workspace/writing/drafts/vinczetamas-YYYY-MM-DD-slug.md
- Kövesd: BLOG-STYLE.md irányelveit
- Featured snippet nyító: 40-60 szó, FAQ min 3 kérdés, em-dash tilos

LOGOLÁS: draft-log-YYYY-MM.md
GIT: git add + commit + push
TELEGRAM: '🗒️ Draft kész: [slug] (vinczetamas) — score [X]/5'
```

### OC-11. Autonomous drafting run — elkezdodott.hu (quality-gated)
- Job ID: `c2407a3e-3d9f-43a5-b6b1-eb29c4d29c9f`
- Enabled: `True`
- Schedule: `45 7 * * 4` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `900`, lightContext: `False`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/c2407a3e-3d9f-43a5-b6b1-eb29c4d29c9f.jsonl`
- Technikai cel:
  - Quality-gated blog draft generalas a legfrissebb signals/candidates fajlokbol, Git commit/push es Telegram statusz.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
INPUT:
- Keresd a legfrissebb candidates fájlt: /home/leoni/shared_workspace/writing/research/candidates-YYYY-MM-DD.md
- Ha nincs: signals fájlt: /home/leoni/shared_workspace/writing/research/signals-YYYY-MM-DD.md
- Ha egyik sem létezik: NO_REPLY

SZŰRÉS:
- Csak quality score >= 4/5 témák
- Heti limit: MAX 2 elkezdodott draft (draft-log-YYYY-MM.md)
- Ha limit elért: NO_REPLY

DRAFT:
- Céloldal: elkezdodott.hu
- Mentés: /home/leoni/shared_workspace/writing/drafts/elkezdodott-YYYY-MM-DD-slug.md
- Kötelező szekció: 'Mit jelent ez egy KKV CEO-nak?'
- Featured snippet nyító: 40-60 szó, FAQ min 3 kérdés, em-dash tilos

LOGOLÁS: draft-log-YYYY-MM.md
GIT: git add + commit + push
TELEGRAM: '🗒️ Draft kész: [slug] (elkezdodott) — score [X]/5'
```

### OC-12. Agent platform blindspot radar (signal gyűjtés)
- Job ID: `88fe5074-689c-4c7e-97f8-058b41f3e060`
- Enabled: `True`
- Schedule: `5 9 * * *` timezone `Europe/Budapest`
- Session target: `isolated`, wakeMode: `now`, agentId: `main`
- Model: `openai-codex/gpt-5.5`, timeoutSeconds: `300`, lightContext: `True`
- Delivery: mode=`announce`, channel=`telegram`, to=`telegram:8554529796`, bestEffort=`False`
- Run log: `/home/leoni/.openclaw/cron/runs/88fe5074-689c-4c7e-97f8-058b41f3e060.jsonl`
- Technikai cel:
  - Agent platform blindspot radar: HAIER signalokbol agent identity/auth/compliance/platform lehetosegek gyujtese, hypothesis fajl frissites, email/Telegram riport.
- Fontos pathok/logok/env-ek:
  - Shared workspace: `/home/leoni/shared_workspace`
  - Email kuldes/fogadas: `himalaya`, config: `/home/leoni/.config/himalaya/config.toml`
  - Telegram delivery: OpenClaw delivery vagy kozvetlen Telegram Bot API, token forrasa `/home/leoni/.openclaw/openclaw.json` vagy env
  - HAIER exportok: `/opt/apps/haier/exports/evolution_signals_*.json`
  - Video Kanban API: `http://localhost:3850/api/tasks`, sweep: `http://localhost:3850/api/sweep`
  - Blog/research outputok: `/home/leoni/shared_workspace/writing/...`, `/home/leoni/shared_workspace/research/...`, `/home/leoni/shared_workspace/reports/...`
- Pontos payload.message:
```text
1) Olvasd be a legfrissebb HAIER export JSON-t: /opt/apps/haier/exports/evolution_signals_*.json
2) Szűrd az agent-releváns signalokat: focus_area tartalmaz 'AI agents' vagy 'AI decision delegation'
3) Vedd az első 30 releváns signalt (title + summary + url + date)
4) Ha a HAIER-ben nincs elég signal: max 1 web keresés (agent identity/auth/compliance téma)
5) Top 5-10 legerősebb signal kiemelése rövid bizonyítékkal
6) Mentési útvonal: /home/leoni/shared_workspace/research/blindspot-signals-$(date +%Y-%m-%d).md
   Használj exec tool-lal `date +%Y-%m-%d` parancsot az aktuális dátumhoz, majd azzal képezd az útvonalat.
7) Mentsd a fájlt a fenti útvonalra.

Ha nincs signal: NO_REPLY.
```

## Linux user crontab jobok
Forras: `crontab -l` a leoni user alatt.

### LC-01. /opt/skills-venv/bin/python3
- Schedule: `0 4 * * *` timezone: host local, Europe/Budapest
- Pontos parancs: `/opt/skills-venv/bin/python3 /home/leoni/.openclaw/workspace/skills/policy-engine/policy_engine.py --decay`
- Script/path: `/home/leoni/.openclaw/workspace/skills/policy-engine/policy_engine.py`
- Technikai leiras: Policy Engine napi trust decay. A policy/trust rendszer bizalmi pontszamait csokkenti idovel, hogy regi jo dontesek ne adjanak korlatlan jovobeli trustot.
- Szükséges env/config: Opcionális: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, de --decay modban nem kritikus. Fajlok: /home/leoni/.openclaw/workspace/policy/policies.yaml, trust_scores.json, action_history.jsonl.
- Log: /home/leoni/.openclaw/workspace/policy/action_history.jsonl, valamint cron/syslog ha hiba van
- Output/mellekhatas: Policy trust state frissul a policy konyvtarban.

### LC-02. /home/leoni/shared_workspace/ops/scripts/moltbook_scan_wrapper.sh
- Schedule: `30 7 * * *` timezone: host local, Europe/Budapest
- Pontos parancs: `/home/leoni/shared_workspace/ops/scripts/moltbook_scan_wrapper.sh morning`
- Script/path: `/home/leoni/shared_workspace/ops/scripts/moltbook_scan_wrapper.sh`
- Technikai leiras: LLM-mentes Moltbook napi scan wrapper. Meghivja a phase-1-passive-recon/moltbook_scan.py scriptet --emit-summary kapcsoloval, append-only logba ir, es hibanal nem nyeli el az exit code-ot.
- Szükséges env/config: Nincs kulon env valtozo. A Python script a /home/leoni/.openclaw/workspace/.secrets/moltbook/credentials.json fajlbol olvassa a Moltbook API kulcsot.
- Log: /home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon/logs/moltbook_scan_morning.log vagy moltbook_scan_evening.log
- Output/mellekhatas: /home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon/artifacts/scans/*.json es signals-log.md

### LC-03. /home/leoni/shared_workspace/ops/scripts/moltbook_scan_wrapper.sh
- Schedule: `30 17 * * *` timezone: host local, Europe/Budapest
- Pontos parancs: `/home/leoni/shared_workspace/ops/scripts/moltbook_scan_wrapper.sh evening`
- Script/path: `/home/leoni/shared_workspace/ops/scripts/moltbook_scan_wrapper.sh`
- Technikai leiras: LLM-mentes Moltbook napi scan wrapper. Meghivja a phase-1-passive-recon/moltbook_scan.py scriptet --emit-summary kapcsoloval, append-only logba ir, es hibanal nem nyeli el az exit code-ot.
- Szükséges env/config: Nincs kulon env valtozo. A Python script a /home/leoni/.openclaw/workspace/.secrets/moltbook/credentials.json fajlbol olvassa a Moltbook API kulcsot.
- Log: /home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon/logs/moltbook_scan_morning.log vagy moltbook_scan_evening.log
- Output/mellekhatas: /home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon/artifacts/scans/*.json es signals-log.md

### LC-04. /usr/bin/python3
- Schedule: `25 18 * * 0` timezone: host local, Europe/Budapest
- Pontos parancs: `/usr/bin/python3 /home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon/moltbook_weekly_review.py --emit-summary >> /home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon/logs/moltbook_weekly_review.log 2>&1`
- Script/path: `/home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon/moltbook_weekly_review.py`
- Technikai leiras: LLM-mentes heti Moltbook review. Az utolso 7 nap scan artifactjait osszesiti, signal-to-noise es ROI ertekelest keszit, majd heti markdown riportot ir.
- Szükséges env/config: Nincs kulon env valtozo.
- Log: /home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon/logs/moltbook_weekly_review.log
- Output/mellekhatas: /home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon/artifacts/weekly/YYYY-MM-DD.md

### LC-05. /home/leoni/shared_workspace/ops/scripts/repo_sync.sh
- Schedule: `5 18 * * *` timezone: host local, Europe/Budapest
- Pontos parancs: `/home/leoni/shared_workspace/ops/scripts/repo_sync.sh --mode shared_workspace >> /home/leoni/shared_workspace/ops/logs/repo_sync_shared_workspace.cron.log 2>&1`
- Script/path: `/home/leoni/shared_workspace/ops/scripts/repo_sync.sh`
- Technikai leiras: Git repo automatikus szinkron. shared_workspace modban inbox valtozasnal ff-only pull, lokalis valtozasnal commit + push. workspace_backup modban a /home/leoni/.openclaw/workspace repo lokalis allapotat menti GitHubra.
- Szükséges env/config: SSH/Git auth a leoni user GitHub SSH konfiguraciojan keresztul. Remote: git@github.com:leonioperator/shared_workspace.git, illetve git@github.com:leonioperator/workspace.git.
- Log: /home/leoni/shared_workspace/ops/logs/repo_sync_shared_workspace.cron.log es /home/leoni/shared_workspace/ops/logs/repo_sync_workspace_backup.cron.log; a script belso logja: repo_sync_shared_workspace.log es repo_sync_workspace_backup.log
- Output/mellekhatas: Git commitok es pushok a megfelelo repokba.

### LC-06. /home/leoni/shared_workspace/ops/scripts/repo_sync.sh
- Schedule: `0 21 * * *` timezone: host local, Europe/Budapest
- Pontos parancs: `/home/leoni/shared_workspace/ops/scripts/repo_sync.sh --mode workspace_backup >> /home/leoni/shared_workspace/ops/logs/repo_sync_workspace_backup.cron.log 2>&1`
- Script/path: `/home/leoni/shared_workspace/ops/scripts/repo_sync.sh`
- Technikai leiras: Git repo automatikus szinkron. shared_workspace modban inbox valtozasnal ff-only pull, lokalis valtozasnal commit + push. workspace_backup modban a /home/leoni/.openclaw/workspace repo lokalis allapotat menti GitHubra.
- Szükséges env/config: SSH/Git auth a leoni user GitHub SSH konfiguraciojan keresztul. Remote: git@github.com:leonioperator/shared_workspace.git, illetve git@github.com:leonioperator/workspace.git.
- Log: /home/leoni/shared_workspace/ops/logs/repo_sync_shared_workspace.cron.log es /home/leoni/shared_workspace/ops/logs/repo_sync_workspace_backup.cron.log; a script belso logja: repo_sync_shared_workspace.log es repo_sync_workspace_backup.log
- Output/mellekhatas: Git commitok es pushok a megfelelo repokba.

### LC-07. /home/leoni/shared_workspace/ops/scripts/kanban_archive.sh
- Schedule: `0 7 * * *` timezone: host local, Europe/Budapest
- Pontos parancs: `/home/leoni/shared_workspace/ops/scripts/kanban_archive.sh`
- Script/path: `/home/leoni/shared_workspace/ops/scripts/kanban_archive.sh`
- Technikai leiras: Kanban housekeeping. A /usr/local/bin/kanban archive parancsot futtatja, amely a done taskokat archive allapotba mozgatja a helyi Kanban rendszerben.
- Szükséges env/config: Nincs kulon env valtozo. Kell: /usr/local/bin/kanban es a Kanban service/API legyen mukodokepes localhost:3848 kornyeken.
- Log: /home/leoni/shared_workspace/ops/logs/kanban-archive.log
- Output/mellekhatas: Kanban done taskok archiv allapotra valtozhatnak.

### LC-08. leoni-learn-daily
- Schedule: `0 3 * * *` timezone: host local, Europe/Budapest
- Pontos parancs: `leoni-learn-daily >> /var/log/leoni-learn.log 2>&1`
- Script/path: `/usr/local/bin/leoni-learn-daily`
- Technikai leiras: Napi learn/self-improvement job. Beallitja a HOME/LANG/PYTHONIOENCODING valtozokat, OpenClaw configbol kiolvassa a Telegram bot tokent es chat id-t, lefuttatja a learn.py --daily parancsot, majd ha van output, emailt kuld es Telegram statuszt kuld.
- Szükséges env/config: HOME=/home/leoni, LANG=hu_HU.UTF-8, PYTHONIOENCODING=utf-8. Kell: /home/leoni/.openclaw/openclaw.json Telegram config, himalaya email config.
- Log: /var/log/leoni-learn.log
- Output/mellekhatas: Email vt@vinczetamas.hu cimre es Telegram statusz, ha van napi tanulsag.

## System crontab es timers
A /etc/crontab, /etc/cron.d/sysstat, /etc/cron.d/e2scrub_all es systemd apt/logrotate/sysstat timer jobok OS-szintu karbantartasok. Ezek nem Leoni/Poke workflow-k, nem javasolt atadni Poke-nak. Felugyelethez eleg monitoring, nem kell agent-run.

## Atveteli javaslat Poke-hoz
1. Determinisztikus Linux crontab jobokat hagyni script alapon, csak a felugyeleti alertet kuldeni Poke API-ra hibanal.
2. OpenClaw agentTurn cronokat Poke API-bol ujra letrehozni mint kulso schedule: idopontban POST /api/v1/inbound/api-message a payload.message tartalommal.
3. A kulso agens minden futasnal tegye bele az egyedi job id-t es elvart outputot, pelda: `[LEONI-CRON OC-03 Reggeli brief] ...`.
4. Hiba es rate limit eseten ne csendben bukjon: Telegram/Poke kontextusba keruljon rovid statusz, es legyen run log link.
5. Kulcsokat csak env/secret store-bol olvasson. Sem Poke message-be, sem Gitbe nem kerulhet API key vagy token.
