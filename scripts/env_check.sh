#!/usr/bin/env bash
set -euo pipefail

ENV_FILE="/home/leoni/.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "ERROR: env file not found: $ENV_FILE" >&2
  exit 2
fi

set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

trim() {
  local s="$1"
  s="${s#${s%%[![:space:]]*}}"
  s="${s%${s##*[![:space:]]}}"
  printf '%s' "$s"
}

is_set() {
  local key="$1"
  local value="${!key-}"
  value="$(trim "$value")"
  [[ -n "$value" ]]
}

check_group() {
  local label="$1"
  shift
  local key status="missing"
  for key in "$@"; do
    if is_set "$key"; then
      status="present"
      break
    fi
  done
  if [[ "$status" == "present" ]]; then
    printf '[OK] %s: present in %s\n' "$label" "$ENV_FILE"
  else
    printf '[MISSING] %s: missing from %s\n' "$label" "$ENV_FILE"
    return 1
  fi
}

printf 'Environment check report\n'
printf 'Host: %s\n' "$(hostname)"
printf 'Env file: %s\n' "$ENV_FILE"
printf '\n'

missing_count=0
check_group 'OpenAI' OPENAI_API_KEY || missing_count=$((missing_count + 1))
check_group 'Anthropic' ANTHROPIC_API_KEY || missing_count=$((missing_count + 1))
check_group 'Gemini' GEMINI_API_KEY GOOGLE_API_KEY || missing_count=$((missing_count + 1))
check_group 'ElevenLabs' ELEVENLABS_API_KEY || missing_count=$((missing_count + 1))

printf '\nSummary: %d missing critical group(s)\n' "$missing_count"
exit $(( missing_count > 0 ? 1 : 0 ))
