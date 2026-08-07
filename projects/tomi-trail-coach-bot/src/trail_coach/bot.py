from __future__ import annotations

import logging
from datetime import date

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from .config import AthleteProfile, load_settings
from .db import TrailCoachDb
from .parsing import as_float, as_int, parse_kv_args
from .training_plan import preworkout_decision, readiness_score, todays_workouts


logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s: %(message)s", level=logging.INFO)
LOG = logging.getLogger(__name__)


PROFILE = AthleteProfile()


def private_only(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id if update.effective_user else None
        allowed = context.bot_data["allowed_user_ids"]
        if user_id not in allowed:
            LOG.warning("Rejected unauthorized user_id=%s", user_id)
            if update.message:
                await update.message.reply_text("Private bot.")
            return
        return await func(update, context)

    return wrapper


def command_text(update: Update) -> str:
    if not update.message or not update.message.text:
        return ""
    return update.message.text.split(maxsplit=1)[1] if " " in update.message.text else ""


@private_only
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Tomi Trail Coach v0 aktiv.\n"
        "Parancsok: /profile /today /checkin /food /drink /preworkout /postworkout /week"
    )


@private_only
async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "\n".join(
            [
                "Sportprofil",
                f"Szuletesi ev: {PROFILE.birth_year}",
                f"Magassag / suly: {PROFILE.height_cm} cm / {PROFILE.current_weight_kg:g} kg",
                f"Hosszu tavu cel: {PROFILE.target_weight_kg:g} kg",
                f"UB Trail: {PROFILE.race_date.isoformat()}, szakaszok: {PROFILE.race_sections[0]}, {PROFILE.race_sections[1]}",
                f"LTHR: {PROFILE.lthr_bpm} bpm",
                f"Eszkoz: {PROFILE.device}",
                "Alapelv: 18 honap futaskihagyas utan konzervativ run-walk epites.",
            ]
        )
    )


@private_only
async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    workouts = todays_workouts(date.today(), PROFILE)
    latest = context.bot_data["db"].latest_checkin()
    readiness = latest["readiness_color"] if latest else None
    if not workouts:
        await update.message.reply_text("Ma nincs kotelezo edzes. Seta, mobilitas vagy piheno.")
        return
    lines = ["Mai terv"]
    for workout in workouts:
        action, reason = preworkout_decision(readiness, workout.kind, workout.minutes)
        lines.extend(
            [
                f"{workout.title}: {workout.minutes} perc, {workout.intensity}",
                f"Dontes: {action}",
                reason,
                workout.notes,
            ]
        )
    await update.message.reply_text("\n".join(lines))


@private_only
async def checkin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = parse_kv_args(command_text(update))
    sleep_hours = as_float(data, "sleep")
    weight_kg = as_float(data, "weight")
    resting_hr = as_int(data, "rhr")
    mood = as_int(data, "mood")
    energy = as_int(data, "energy")
    soreness = as_int(data, "soreness")
    score, color = readiness_score(sleep_hours, resting_hr, mood, energy, soreness)
    context.bot_data["db"].insert(
        "checkins",
        {
            "sleep_hours": sleep_hours,
            "weight_kg": weight_kg,
            "resting_hr": resting_hr,
            "mood": mood,
            "energy": energy,
            "soreness": soreness,
            "readiness_score": score,
            "readiness_color": color,
            "note": data.get("note"),
        },
    )
    await update.message.reply_text(f"Check-in mentve. Readiness: {score}/100, {color}.")


@private_only
async def food(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = parse_kv_args(command_text(update))
    context.bot_data["db"].insert(
        "food_logs",
        {"type": data.get("type", "meal"), "amount_ml": None, "text": data.get("text", "")},
    )
    await update.message.reply_text("Etel log mentve.")


@private_only
async def drink(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = parse_kv_args(command_text(update))
    context.bot_data["db"].insert(
        "food_logs",
        {"type": data.get("type", "water"), "amount_ml": as_int(data, "amount_ml"), "text": data.get("text", "")},
    )
    await update.message.reply_text("Ital log mentve.")


@private_only
async def preworkout(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = parse_kv_args(command_text(update))
    latest = context.bot_data["db"].latest_checkin()
    readiness = latest["readiness_color"] if latest else None
    planned_kind = data.get("planned", "easy_run")
    minutes = as_int(data, "minutes", 30) or 30
    action, reason = preworkout_decision(readiness, planned_kind, minutes)
    await update.message.reply_text(f"Dontes: {action}\n{reason}")


@private_only
async def postworkout(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = parse_kv_args(command_text(update))
    context.bot_data["db"].insert(
        "workout_logs",
        {
            "workout_type": data.get("type", "unknown"),
            "minutes": as_int(data, "minutes"),
            "distance_km": as_float(data, "distance_km"),
            "avg_hr": as_int(data, "avg_hr"),
            "rpe": as_int(data, "rpe"),
            "decision": data.get("decision"),
            "note": data.get("note"),
        },
    )
    await update.message.reply_text("Edzes log mentve.")


@private_only
async def week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db = context.bot_data["db"]
    checkins = db.recent_rows("checkins", 7)
    workouts = db.recent_rows("workout_logs", 20)
    total_minutes = sum(row["minutes"] or 0 for row in workouts)
    avg_readiness = round(sum(row["readiness_score"] for row in checkins) / len(checkins), 1) if checkins else 0
    await update.message.reply_text(
        "\n".join(
            [
                "Heti riport",
                f"Check-in: {len(checkins)}",
                f"Atlag readiness: {avg_readiness}",
                f"Logolt edzes: {len(workouts)}",
                f"Ossz ido: {total_minutes} perc",
                "Kovetkezo fokusz: kovetkezetesseg, Z1-Z2 kontroll, serulesmentes epites.",
            ]
        )
    )


def main() -> None:
    settings = load_settings()
    if not settings.token:
        raise SystemExit("TELEGRAM_BOT_TOKEN is missing")
    if not settings.allowed_user_ids:
        raise SystemExit("TELEGRAM_ALLOWED_USER_IDS is missing")
    db = TrailCoachDb(settings.db_path)
    db.init()
    app = Application.builder().token(settings.token).build()
    app.bot_data["allowed_user_ids"] = settings.allowed_user_ids
    app.bot_data["db"] = db
    for name, handler in {
        "start": start,
        "profile": profile,
        "today": today,
        "checkin": checkin,
        "food": food,
        "drink": drink,
        "preworkout": preworkout,
        "postworkout": postworkout,
        "week": week,
    }.items():
        app.add_handler(CommandHandler(name, handler))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
