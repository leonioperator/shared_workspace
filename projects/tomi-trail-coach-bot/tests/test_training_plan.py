from datetime import date

from trail_coach.config import AthleteProfile
from trail_coach.training_plan import preworkout_decision, readiness_score, todays_workouts, week_for_day


def test_week_for_day_starts_eight_weeks_before_race():
    profile = AthleteProfile()
    assert week_for_day(date(2026, 8, 7), profile.race_date) == 1
    assert week_for_day(date(2026, 9, 30), profile.race_date) == 8


def test_low_readiness_turns_training_red():
    score, color = readiness_score(sleep_hours=5.0, resting_hr=70, mood=2, energy=2, soreness=4)
    assert score < 55
    assert color == "red"


def test_red_preworkout_skips_running():
    action, reason = preworkout_decision("red", "easy_run", 30)
    assert action == "skip_or_walk"
    assert "ne fuss" in reason


def test_today_returns_matching_day_workout():
    workouts = todays_workouts(date(2026, 8, 11))
    assert workouts
    assert workouts[0].week == 1
