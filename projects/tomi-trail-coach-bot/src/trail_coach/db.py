from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA = """
create table if not exists checkins (
  id integer primary key autoincrement,
  created_at text not null,
  sleep_hours real,
  weight_kg real,
  resting_hr integer,
  mood integer,
  energy integer,
  soreness integer,
  readiness_score integer,
  readiness_color text,
  note text
);

create table if not exists food_logs (
  id integer primary key autoincrement,
  created_at text not null,
  type text not null,
  amount_ml integer,
  text text
);

create table if not exists workout_logs (
  id integer primary key autoincrement,
  created_at text not null,
  workout_type text not null,
  minutes integer,
  distance_km real,
  avg_hr integer,
  rpe integer,
  decision text,
  note text
);
"""


class TrailCoachDb:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def init(self) -> None:
        with self.connect() as conn:
            conn.executescript(SCHEMA)

    def insert(self, table: str, data: dict[str, Any]) -> None:
        data = {"created_at": now_iso(), **data}
        keys = ", ".join(data.keys())
        placeholders = ", ".join("?" for _ in data)
        with self.connect() as conn:
            conn.execute(f"insert into {table} ({keys}) values ({placeholders})", tuple(data.values()))

    def latest_checkin(self) -> sqlite3.Row | None:
        with self.connect() as conn:
            return conn.execute("select * from checkins order by id desc limit 1").fetchone()

    def recent_rows(self, table: str, limit: int = 30) -> list[sqlite3.Row]:
        with self.connect() as conn:
            return conn.execute(
                f"select * from {table} order by created_at desc limit ?",
                (limit,),
            ).fetchall()


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
