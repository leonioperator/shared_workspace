#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-morning}"
BASE="/home/leoni/shared_workspace/projects/moltbook-ecosystem-exploration/phase-1-passive-recon"
LOG_DIR="$BASE/logs"
mkdir -p "$LOG_DIR"

# one append-only log per mode
LOG_FILE="$LOG_DIR/moltbook_scan_${MODE}.log"

ts() { date -Is; }

echo "[$(ts)] START moltbook_scan mode=${MODE}" >> "$LOG_FILE"
if /usr/bin/python3 "$BASE/moltbook_scan.py" --emit-summary >> "$LOG_FILE" 2>&1; then
  echo "[$(ts)] OK" >> "$LOG_FILE"
else
  code=$?
  echo "[$(ts)] ERROR exit_code=$code" >> "$LOG_FILE"
  exit $code
fi
