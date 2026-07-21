#!/usr/bin/env python3
import json, glob, os, re, sys, tempfile
from datetime import date
from pathlib import Path

EXPORT_GLOB = "/opt/apps/haier/exports/evolution_signals_*.json"
OUT_DIR = Path("/home/leoni/shared_workspace/research")
NEEDLES = ("ai agents", "ai decision delegation")


def fail(msg: str, code: int = 1):
    print(f"⚠️ Blindspot signal gyűjtés failed: {msg}", file=sys.stderr)
    sys.exit(code)


def text(v):
    if v is None:
        return ""
    if isinstance(v, (list, tuple, set)):
        return " ".join(text(x) for x in v)
    if isinstance(v, dict):
        return " ".join(f"{k} {text(val)}" for k, val in v.items())
    return str(v)


def clean(v):
    return re.sub(r"\s+", " ", text(v).strip())


def md_line(v):
    return clean(v).replace("\r", " ").replace("\n", " ")


def score(sig):
    try:
        return float(sig.get("deep_score", -1))
    except Exception:
        return -1.0


def norm_title(v):
    return re.sub(r"[^a-z0-9]+", " ", clean(v).lower()).strip()


def previous_titles(today):
    seen = set()
    for path in sorted(OUT_DIR.glob("blindspot-signals-*.md")):
        if path.name == f"blindspot-signals-{today}.md":
            continue
        try:
            txt = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for m in re.finditer(r"^###\s+(?:[0-9]+\.\s+)?(.+)$", txt, flags=re.M):
            t = norm_title(m.group(1))
            if t:
                seen.add(t)
    return seen


def append_signal(lines, sig, idx):
    title = md_line(sig.get("title")) or "Untitled signal"
    summary = md_line(sig.get("summary")) or "No summary."
    url = md_line(sig.get("url"))
    sig_date = md_line(sig.get("date")) or md_line(sig.get("created_at"))
    source = md_line(sig.get("source"))
    focus = md_line(sig.get("focus_area"))
    tech = md_line(sig.get("technology_type"))
    lines.append(f"### {idx}. {title}")
    lines.append(f"- Deep score: {score(sig):g}")
    if sig_date:
        lines.append(f"- Date: {sig_date}")
    if source:
        lines.append(f"- Source: {source}")
    if focus or tech:
        lines.append(f"- Focus/tech: {focus} / {tech}")
    if url:
        lines.append(f"- URL: {url}")
    lines.append(f"- Summary: {summary}")
    lines.append("")


exports = sorted(glob.glob(EXPORT_GLOB), key=os.path.getmtime, reverse=True)
if not exports:
    fail("nincs olvasható HAIER export")
export = exports[0]
if not os.access(export, os.R_OK):
    fail(f"nincs olvasható HAIER export: {export}")

try:
    with open(export, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:
    fail(f"export JSON olvasás/parszolás hiba: {e}")

signals = data.get("signals")
if not isinstance(signals, list):
    fail("hibás HAIER séma: nincs .signals[] tömb")

relevant = []
for sig in signals:
    if not isinstance(sig, dict):
        continue
    hay = (text(sig.get("focus_area")) + " " + text(sig.get("technology_type"))).lower()
    if any(n in hay for n in NEEDLES):
        relevant.append(sig)

if len(relevant) < 5:
    fail(f"túl kevés agent-releváns signal: {len(relevant)}")

relevant.sort(key=score, reverse=True)
# Dedupe same-title duplicates within one export (Google News RSS often repeats the same article with different wrapper URLs).
deduped_relevant = []
current_seen = set()
for sig in relevant:
    t = norm_title(sig.get("title"))
    if not t or t in current_seen:
        continue
    current_seen.add(t)
    deduped_relevant.append(sig)
relevant = deduped_relevant
today = date.today().isoformat()
out = OUT_DIR / f"blindspot-signals-{today}.md"
OUT_DIR.mkdir(parents=True, exist_ok=True)
seen_titles = previous_titles(today)
novel = [sig for sig in relevant if norm_title(sig.get("title")) and norm_title(sig.get("title")) not in seen_titles]

lines = [
    f"# Blindspot Signals Report - {today}",
    "",
    f"- Source export: `{export}`",
    f"- Total signals in export: {len(signals)}",
    f"- Agent-relevant signals: {len(relevant)}",
    f"- Novel vs previous reports: {len(novel)}",
    "- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`",
    "",
    "## New Signals Since Previous Reports",
    "",
]

if novel:
    for i, sig in enumerate(novel[:30], 1):
        append_signal(lines, sig, i)
else:
    lines.append("No new previously unseen agent-relevant signals in today's export.")
    lines.append("")

lines.extend([
    "## Top Signals By Deep Score (including already-seen)",
    "",
])
for i, sig in enumerate(relevant[:30], 1):
    append_signal(lines, sig, i)

content = "\n".join(lines).rstrip() + "\n"
fd, tmp = tempfile.mkstemp(prefix=out.name + ".", suffix=".tmp", dir=str(OUT_DIR), text=True)
try:
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp, out)
finally:
    if os.path.exists(tmp):
        os.unlink(tmp)

written = out.read_text(encoding="utf-8")
checks = [
    (out.exists() and out.stat().st_size > 0, "output fájl nem jött létre vagy üres"),
    (written.startswith(f"# Blindspot Signals Report - {today}"), "hiányzik report cím"),
    ("\n## New Signals Since Previous Reports\n" in written, "hiányzik New Signals blokk"),
    ("\n## Top Signals By Deep Score (including already-seen)\n" in written, "hiányzik Top Signals blokk"),
    (len(re.findall(r"^### [0-9]+\. ", written, flags=re.M)) >= 5, "kevesebb mint 5 valós signal cím"),
    (not re.search(r"Signal [0-9]+ cím|placeholder|TODO", written, flags=re.I), "placeholder/TODO maradt a fájlban"),
]
for ok, msg in checks:
    if not ok:
        fail(msg)

novel_top5 = [md_line(sig.get("title")) for sig in novel[:5]]
if not novel_top5:
    print(f"NO_REPLY: nincs új blindspot signal; archiválva: {out}; agent-releváns {len(relevant)} / {len(signals)}")
    sys.exit(0)
print("✅ Blindspot radar signal gyűjtés sikeres")
print(f"Fájl: {out}")
print(f"Forrás: {export}")
print(f"Agent-releváns jelek: {len(relevant)} / {len(signals)}")
print(f"Új signalok korábbi riportokhoz képest: {len(novel)}")
print("Új Top 5:")
for i, item in enumerate(novel_top5, 1):
    print(f"- {i}. {item}")
