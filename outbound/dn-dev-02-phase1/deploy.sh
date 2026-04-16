#!/usr/bin/env bash
set -euo pipefail

# Idempotent deploy helper for dn-dev-02 Navibase stack.
# Default stack dir: /opt/navibase-oc

STACK_DIR="${STACK_DIR:-/opt/navibase-oc}"
COMPOSE_FILE="${COMPOSE_FILE:-docker-compose.yml}"
DO_BACKUP="${DO_BACKUP:-0}"  # set to 1 to run backup.sh before deploy

if [[ ! -d "$STACK_DIR" ]]; then
  echo "ERROR: STACK_DIR not found: $STACK_DIR" >&2
  exit 1
fi

cd "$STACK_DIR"

if [[ ! -f "$COMPOSE_FILE" ]]; then
  echo "ERROR: compose file not found: $STACK_DIR/$COMPOSE_FILE" >&2
  exit 1
fi

if [[ "$DO_BACKUP" == "1" ]]; then
  echo "Running backup..."
  # Expect backup.sh beside this script, or provide BACKUP_SH path
  BACKUP_SH="${BACKUP_SH:-$(dirname "$0")/backup.sh}"
  bash "$BACKUP_SH"
fi

echo "Deploying stack in $STACK_DIR ($COMPOSE_FILE)"
docker compose -f "$COMPOSE_FILE" pull
docker compose -f "$COMPOSE_FILE" up -d

echo "OK: deploy finished"

