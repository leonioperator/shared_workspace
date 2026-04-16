#!/usr/bin/env bash
set -euo pipefail

# Minimal backup for dn-dev-02 (Navibase/OpenClaw stack)
# - backs up known SQLite DB names + snapshot.json when found
# - stores tar.gz under BACKUP_DIR
# - keeps last RETENTION_DAYS daily backups

BACKUP_DIR="${BACKUP_DIR:-/var/backups/navibase-oc}"
RETENTION_DAYS="${RETENTION_DAYS:-7}"

# Where to search (safe defaults)
SEARCH_ROOTS=(
  "${SEARCH_ROOT_1:-/opt}"
)

DB_NAMES=(
  "approval_gate.db"
  "audit_log.db"
  "budget_state.db"
  "token_usage_offsets.db"
)

EXTRA_NAMES=(
  "snapshot.json"
)

ts="$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

tmpdir="$(mktemp -d)"
cleanup() { rm -rf "$tmpdir"; }
trap cleanup EXIT

found_any=0

find_one() {
  local name="$1"
  local root
  for root in "${SEARCH_ROOTS[@]}"; do
    # maxdepth keeps it fast, adjust if needed
    local p
    p="$(find "$root" -maxdepth 6 -type f -name "$name" 2>/dev/null | head -n 1 || true)"
    if [[ -n "$p" ]]; then
      echo "$p"
      return 0
    fi
  done
  return 1
}

manifest="$tmpdir/manifest.txt"
: > "$manifest"

for n in "${DB_NAMES[@]}"; do
  if p="$(find_one "$n")"; then
    echo "$p" | tee -a "$manifest" >/dev/null
    cp -a "$p" "$tmpdir/" 
    found_any=1
  fi
done

for n in "${EXTRA_NAMES[@]}"; do
  if p="$(find_one "$n")"; then
    echo "$p" | tee -a "$manifest" >/dev/null
    cp -a "$p" "$tmpdir/" 
    found_any=1
  fi
done

if [[ "$found_any" -eq 0 ]]; then
  echo "ERROR: did not find any known DB/snapshot files under: ${SEARCH_ROOTS[*]}" >&2
  echo "Hint: set SEARCH_ROOT_1=/opt/navibase-oc or point to the real root." >&2
  exit 2
fi

out="${BACKUP_DIR}/dn-dev-02-backup_${ts}.tar.gz"
tar -C "$tmpdir" -czf "$out" .

echo "OK: created $out"

# Retention: delete older than RETENTION_DAYS
find "$BACKUP_DIR" -type f -name 'dn-dev-02-backup_*.tar.gz' -mtime "+${RETENTION_DAYS}" -print -delete 2>/dev/null || true

