from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from .config import AthleteProfile


@dataclass(frozen=True)
class Workout:
    week: int
    day: str
    kind: str
    title: str
    minutes: int
    intensity: str
    notes: str


BASE_PLAN: tuple[Workout, ...] = (
    Workout(1, "Tue", "run_walk", "Run-walk reset", 24, "Z1-Z2", "6 x 2 min jog / 2 min walk"),
    Workout(1, "Thu", "strength", "Foundation strength", 35, "easy", "legs, core, pull pattern"),
    Workout(1, "Sat", "hike", "Easy trail walk", 50, "Z1", "keep it conversational"),
    Workout(2, "Tue", "run_walk", "Run-walk build", 28, "Z1-Z2", "7 x 2 min jog / 2 min walk"),
    Workout(2, "Thu", "strength", "Foundation strength", 38, "easy", "same pattern, add one set if fresh"),
    Workout(2, "Sat", "hike", "Trail walk plus strides", 55, "Z1", "4 x 15 sec relaxed uphill stride"),
    Workout(3, "Tue", "easy_run", "Easy continuous attempt", 25, "Z2 cap", "walk breaks allowed"),
    Workout(3, "Thu", "strength", "Strength plus mobility", 40, "easy-moderate", "no leg failure"),
    Workout(3, "Sat", "hike_run", "Trail walk-run", 65, "Z1-Z2", "short jogs on flats only"),
    Workout(4, "Tue", "easy_run", "Easy aerobic", 30, "Z2 cap", "stop if form degrades"),
    Workout(4, "Thu", "strength", "Strength maintenance", 35, "easy", "reduce if soreness > 3"),
    Workout(4, "Sat", "hike_run", "Long trail base", 75, "Z1-Z2", "fuel and drink rehearsal"),
    Workout(5, "Tue", "easy_run", "Easy aerobic", 35, "Z2 cap", "flat route preferred"),
    Workout(5, "Thu", "hill_walk", "Uphill power walk", 35, "Z2", "steady, no racing"),
    Workout(5, "Sat", "trail", "Trail endurance", 85, "Z1-Z2", "include hiking sections"),
    Workout(6, "Tue", "easy_run", "Easy aerobic", 38, "Z2 cap", "HR discipline"),
    Workout(6, "Thu", "strength", "Strength maintenance", 35, "easy", "core and posterior chain"),
    Workout(6, "Sat", "trail", "Trail endurance", 95, "Z1-Z2", "practice race kit"),
    Workout(7, "Tue", "easy_run", "Easy aerobic", 30, "Z2 cap", "freshness first"),
    Workout(7, "Thu", "hill_walk", "Short uphill primer", 28, "Z2", "finish fresh"),
    Workout(7, "Sat", "trail", "Peak trail session", 105, "Z1-Z2", "no hero effort"),
    Workout(8, "Tue", "easy_run", "Taper easy", 25, "Z1-Z2", "short and relaxed"),
    Workout(8, "Thu", "mobility", "Mobility and activation", 25, "easy", "leave energy in the tank"),
    Workout(8, "Sat", "race_rehearsal", "Race-week confidence", 35, "Z1", "gear and nutrition check"),
)


def week_for_day(today: date, race_date: date) -> int:
    start = race_date - timedelta(weeks=8)
    if today <= start:
        return 1
    return min(8, max(1, ((today - start).days // 7) + 1))


def todays_workouts(today: date, profile: AthleteProfile = AthleteProfile()) -> list[Workout]:
    week = week_for_day(today, profile.race_date)
    day = today.strftime("%a")
    return [workout for workout in BASE_PLAN if workout.week == week and workout.day == day]


def readiness_score(
    sleep_hours: float | None,
    resting_hr: int | None,
    mood: int | None,
    energy: int | None,
    soreness: int | None,
) -> tuple[int, str]:
    score = 70
    if sleep_hours is not None:
        score += 10 if sleep_hours >= 7 else -15 if sleep_hours < 6 else 0
    if resting_hr is not None:
        score += -15 if resting_hr >= 68 else 5 if resting_hr <= 58 else 0
    if mood is not None:
        score += (mood - 3) * 5
    if energy is not None:
        score += (energy - 3) * 7
    if soreness is not None:
        score -= max(0, soreness - 2) * 10
    score = max(0, min(100, score))
    if score >= 75:
        return score, "green"
    if score >= 55:
        return score, "yellow"
    return score, "red"


def preworkout_decision(
    readiness_color: str | None,
    planned_kind: str,
    planned_minutes: int,
) -> tuple[str, str]:
    if readiness_color == "red":
        return "skip_or_walk", "Ma ne fuss. 20-30 perc seta vagy mobilitas eleg."
    if readiness_color == "yellow":
        adjusted = max(20, int(planned_minutes * 0.7))
        return "adjust", f"Mehet, de csokkentve: {adjusted} perc, csak Z1-Z2."
    if planned_kind in {"easy_run", "run_walk", "hike_run", "trail"} and planned_minutes > 45:
        return "go_capped", "Mehet, de LTHR alapon maradjon kontrollalt Z1-Z2."
    return "go", "Mehet a terv szerint, erolkodes nelkul."
