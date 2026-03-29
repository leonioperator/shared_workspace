#!/usr/bin/env bash
set -euo pipefail

LOG_FILE="/home/leoni/shared_workspace/ops/logs/kanban-archive.log"
mkdir -p "$(dirname "$LOG_FILE")"

ts() { date -Is; }

echo "[$(ts)] START kanban archive" >> "$LOG_FILE"
if /usr/local/bin/kanban archive >> "$LOG_FILE" 2>&1; then
  echo "[$(ts)] OK" >> "$LOG_FILE"
else
  code=$?
  echo "[$(ts)] ERROR exit_code=$code" >> "$LOG_FILE"
  exit $code
fi
