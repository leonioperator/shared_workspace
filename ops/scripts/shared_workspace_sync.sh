#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/home/leoni/shared_workspace"
LOG_DIR="/home/leoni/shared_workspace/ops/logs"
LOG_FILE="$LOG_DIR/shared_workspace_sync.log"

mkdir -p "$LOG_DIR"

now() { date -Is; }
log() { echo "[$(now)] $*" | tee -a "$LOG_FILE"; }

cd "$REPO_DIR"

log "START shared_workspace_sync"

# Ensure we're on main
branch="$(git rev-parse --abbrev-ref HEAD)"
if [[ "$branch" != "main" ]]; then
  log "ERROR: expected branch main, got $branch"
  exit 2
fi

# Fetch remote state
log "git fetch origin"
git fetch --quiet origin

# If remote inbox changed, pull fast-forward only
remote_inbox_changes="$(git diff --name-only HEAD..origin/main -- inbox/ || true)"
if [[ -n "$remote_inbox_changes" ]]; then
  log "Remote inbox changes detected; pulling (ff-only)"
  git pull --ff-only origin main
else
  log "No remote inbox changes"
fi

# Push local changes if any
if [[ -n "$(git status --porcelain)" ]]; then
  log "Local changes detected; committing + pushing"
  git add -A
  if ! git diff --cached --quiet; then
    msg="Sync: $(date +%F' '%R)"
    git commit -m "$msg" >/dev/null
    git push --quiet origin main
    log "PUSHED: $msg"
  else
    log "Nothing staged after add -A (unexpected); skipping push"
  fi
else
  log "No local changes to push"
fi

log "DONE shared_workspace_sync"
