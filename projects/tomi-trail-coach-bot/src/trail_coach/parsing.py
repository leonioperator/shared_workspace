from __future__ import annotations


def parse_kv_args(text: str) -> dict[str, str]:
    """Parse simple key=value command arguments while preserving note/text tails."""
    parts = text.split()
    result: dict[str, str] = {}
    i = 0
    while i < len(parts):
        part = parts[i]
        if "=" not in part:
            i += 1
            continue
        key, value = part.split("=", 1)
        if key in {"note", "text"}:
            tail = [value] + parts[i + 1 :]
            result[key] = " ".join(tail).strip()
            break
        result[key] = value.strip()
        i += 1
    return result


def as_float(data: dict[str, str], key: str, default: float | None = None) -> float | None:
    value = data.get(key)
    if value is None:
        return default
    return float(value.replace(",", "."))


def as_int(data: dict[str, str], key: str, default: int | None = None) -> int | None:
    value = data.get(key)
    if value is None:
        return default
    return int(value)
