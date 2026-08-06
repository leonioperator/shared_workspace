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


STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "for", "by", "with", "on", "in", "its", "is", "as", "at", "from",
    "warns", "warning", "warn", "reveals", "confirms", "says", "reported", "report", "news", "breached", "breach", "hacked",
}
PUBLISHER_SUFFIX_RE = re.compile(
    r"\s+(?:-|–|—|:)\s+(bleepingcomputer|help net security|security affairs|the hacker news|cybersecuritynews|techcrunch|wired|venturebeat|forbes|zdnet|databricks)\s*$",
    re.I,
)
KNOWN_PUBLISHERS = (
    "BleepingComputer", "Help Net Security", "Security Affairs", "The Hacker News", "CyberSecurityNews",
    "TechCrunch", "Wired", "VentureBeat", "Forbes", "ZDNet", "Databricks",
)


def strip_publisher(v):
    t = clean(v)
    t = re.sub(r"&nbsp;.*$", "", t)
    return PUBLISHER_SUFFIX_RE.sub("", t).strip()


def source_label(sig):
    hay = f"{clean(sig.get('title'))} {clean(sig.get('summary'))}"
    for pub in KNOWN_PUBLISHERS:
        if pub.lower() in hay.lower():
            return pub
    return md_line(sig.get("source"))


def norm_title(v):
    t = strip_publisher(v).lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def token_set(v):
    t = norm_title(v)
    toks = {x for x in t.split() if len(x) > 2 and x not in STOPWORDS}
    # Normalize a few recurring entity/event words so syndicated headlines cluster.
    if "hugging" in toks and "face" in toks:
        toks.add("huggingface")
    if "autonomous" in toks and "agent" in toks:
        toks.add("autonomousagent")
    return toks


def similar_title(a, b):
    ta, tb = token_set(a), token_set(b)
    if not ta or not tb:
        return False
    inter = len(ta & tb)
    return inter >= 3 and inter / min(len(ta), len(tb)) >= 0.55


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
    title = md_line(sig.get("display_title") or sig.get("title")) or "Untitled signal"
    summary = md_line(sig.get("summary")) or "No summary."
    url = md_line(sig.get("url"))
    sig_date = md_line(sig.get("date")) or md_line(sig.get("created_at"))
    source = source_label(sig)
    focus = md_line(sig.get("focus_area"))
    tech = md_line(sig.get("technology_type"))
    sources = sig.get("sources") or ([source] if source else [])
    urls = sig.get("urls") or ([url] if url else [])
    lines.append(f"### {idx}. {title}")
    lines.append(f"- Weighted score: {weighted_score(sig):.2f}")
    lines.append(f"- Deep score: {score(sig):g}")
    if len(sources) > 1:
        lines.append(f"- Coverage: {len(sources)} sources ({', '.join(sources[:8])})")
    if sig_date:
        lines.append(f"- Date: {sig_date}")
    if source:
        lines.append(f"- Primary source: {source}")
    if focus or tech:
        lines.append(f"- Focus/tech: {focus} / {tech}")
    if urls:
        lines.append(f"- URL: {urls[0]}")
        for extra in urls[1:4]:
            lines.append(f"  - Alt: {extra}")
    lines.append(f"- Summary: {summary}")
    lines.append("")


def weighted_score(sig):
    base = score(sig)
    sources = sig.get("sources") or []
    coverage = max(0, len(set(sources)) - 1)
    # Multi-source coverage matters, but should not drown strong deep_score signals.
    return base + min(0.30, coverage * 0.08)


def cluster_relevant(signals):
    clusters = []
    for sig in signals:
        title = sig.get("title")
        placed = False
        for c in clusters:
            if similar_title(title, c["title"]):
                c["items"].append(sig)
                placed = True
                break
        if not placed:
            clusters.append({"title": title, "items": [sig]})

    out = []
    for c in clusters:
        items = c["items"]
        # Representative: highest deep_score, then prefer non-google_news, then latest.
        def rep_key(x):
            return (score(x), 1 if x.get("source") != "google_news" else 0, clean(x.get("date") or x.get("created_at")))
        rep = max(items, key=rep_key).copy()
        rep["display_title"] = strip_publisher(c["title"] or rep.get("title")) or rep.get("title")
        rep["sources"] = []
        rep["urls"] = []
        seen_s, seen_u = set(), set()
        for item in sorted(items, key=rep_key, reverse=True):
            src = source_label(item)
            url = md_line(item.get("url"))
            if src and src not in seen_s:
                seen_s.add(src); rep["sources"].append(src)
            if url and url not in seen_u:
                seen_u.add(url); rep["urls"].append(url)
        rep["cluster_size"] = len(items)
        out.append(rep)
    out.sort(key=weighted_score, reverse=True)
    return out


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
raw_relevant_count = len(relevant)
# Cluster syndicated coverage of the same event into one weighted item.
relevant = cluster_relevant(relevant)
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
    f"- Agent-relevant raw signals: {raw_relevant_count}",
    f"- Deduped/weighted signal clusters: {len(relevant)}",
    f"- Novel vs previous reports: {len(novel)}",
    "- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`",
    "- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.",
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
    "## Top Signals By Weighted Score (including already-seen)",
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
    ("\n## Top Signals By Weighted Score (including already-seen)\n" in written, "hiányzik Top Signals blokk"),
    (len(re.findall(r"^### [0-9]+\. ", written, flags=re.M)) >= 5, "kevesebb mint 5 valós signal cím"),
    (not re.search(r"Signal [0-9]+ cím|placeholder|TODO", written, flags=re.I), "placeholder/TODO maradt a fájlban"),
]
for ok, msg in checks:
    if not ok:
        fail(msg)

novel_top5 = [md_line(sig.get("display_title") or sig.get("title")) for sig in novel[:5]]
if not novel_top5:
    print(f"NO_REPLY: nincs új blindspot signal; archiválva: {out}; agent-releváns {len(relevant)} / {len(signals)}")
    sys.exit(0)
print("✅ Blindspot radar signal gyűjtés sikeres")
print(f"Fájl: {out}")
print(f"Forrás: {export}")
print(f"Agent-releváns jelek: {raw_relevant_count} / {len(signals)}")
print(f"Dedupált/weighted signal clusterek: {len(relevant)}")
print(f"Új signal clusterek korábbi riportokhoz képest: {len(novel)}")
print("Új Top 5:")
for i, item in enumerate(novel_top5, 1):
    print(f"- {i}. {item}")
