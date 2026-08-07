# Tomi Trail Coach Bot v0

Private Telegram-based trail preparation assistant for Tamas.

Goal: daily check-in, food and drink log, pre-workout decision, post-workout log,
weekly report, and an adaptive 8-week preparation plan for UB Trail 2026.

## Athlete Profile

- Birth year: 1972
- Height: 169 cm
- Current weight: 80 kg
- Long-term target weight: 66 kg
- Race: UB Trail, 2026-10-02
- Sections: 4 and 11
- Devices: Garmin Fenix 6X + chest strap
- LTHR: 172 bpm
- Running background: no running for about 18 months
- Home equipment: dumbbells, bench, resistance band, pull-up bar

## v0 Scope

- Private Telegram bot, allowlisted by Telegram user id
- SQLite local storage
- Daily readiness check-in
- Food and drink log
- Pre-workout go / adjust / skip decision
- Post-workout training log
- Weekly summary
- Adaptive 8-week base plan with conservative load control

## Commands

```text
/start
/profile
/today
/checkin sleep=7.2 weight=80.0 rhr=58 mood=4 energy=3 soreness=2 note=ok
/food type=meal text=tojas rizs salata
/drink type=water amount_ml=500
/preworkout planned=easy_run minutes=30
/postworkout type=run minutes=28 distance_km=3.6 avg_hr=139 rpe=4 note=easy
/week
```

Use spaces between `key=value` fields. Free text can be put after `note=` or `text=`.

## Setup

```bash
cd /home/leoni/shared_workspace/projects/tomi-trail-coach-bot
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`:

```text
TELEGRAM_BOT_TOKEN=...
TELEGRAM_ALLOWED_USER_IDS=8554529796
TRAIL_COACH_DB=/home/leoni/shared_workspace/projects/tomi-trail-coach-bot/data/trail_coach.sqlite3
```

Run:

```bash
python -m trail_coach.bot
```

## Avatar

Profile image:

```text
assets/tomi-trail-coach-avatar.png
```

Set it in BotFather after the Telegram bot exists:

```text
/setuserpic
```

## Notes

This is coaching support, not medical advice. v0 deliberately starts with a
conservative run-walk base because the athlete has not run for about 18 months.
