#!/usr/bin/env bash
set -euo pipefail

# Purpose: ensure the DEV gateway does not bind publicly.
# Default target: /opt/openclaw/.env

ENV_FILE="${ENV_FILE:-/opt/openclaw/.env}"
KEY="OPENCLAW_GATEWAY_HOST"
VALUE="127.0.0.1"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "ERROR: env file not found: $ENV_FILE" >&2
  exit 1
fi

cp -a "$ENV_FILE" "${ENV_FILE}.bak.$(date +%Y%m%d_%H%M%S)"

if grep -qE "^${KEY}=" "$ENV_FILE"; then
  # Replace existing
  sed -i -E "s#^${KEY}=.*#${KEY}=${VALUE}#" "$ENV_FILE"
else
  # Append
  printf '\n%s=%s\n' "$KEY" "$VALUE" >> "$ENV_FILE"
fi

echo "OK: patched $ENV_FILE → ${KEY}=${VALUE}"

echo "Next step (manual): restart the dev stack in /opt/openclaw"
echo "  cd /opt/openclaw && docker compose restart"

