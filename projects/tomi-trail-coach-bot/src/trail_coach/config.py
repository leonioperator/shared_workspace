from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class AthleteProfile:
    name: str = "Tamas"
    birth_year: int = 1972
    height_cm: int = 169
    current_weight_kg: float = 80.0
    target_weight_kg: float = 66.0
    race_date: date = date(2026, 10, 2)
    race_sections: tuple[int, int] = (4, 11)
    lthr_bpm: int = 172
    device: str = "Garmin Fenix 6X + chest strap"
    running_gap_months: int = 18
    equipment: tuple[str, ...] = (
        "dumbbells",
        "bench",
        "resistance band",
        "pull-up bar",
    )


@dataclass(frozen=True)
class Settings:
    token: str
    allowed_user_ids: set[int]
    db_path: Path


def load_settings() -> Settings:
    load_dotenv()
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    allowed_raw = os.environ.get("TELEGRAM_ALLOWED_USER_IDS", "").strip()
    db_raw = os.environ.get(
        "TRAIL_COACH_DB",
        "/home/leoni/shared_workspace/projects/tomi-trail-coach-bot/data/trail_coach.sqlite3",
    )
    allowed_user_ids = {int(item.strip()) for item in allowed_raw.split(",") if item.strip()}
    return Settings(token=token, allowed_user_ids=allowed_user_ids, db_path=Path(db_raw))
