#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-}"

usage() {
  echo "Usage: $0 --mode shared_workspace|workspace_backup" >&2
  exit 2
}

if [[ "$MODE" != "--mode" ]]; then usage; fi
MODE="${2:-}"

now() { date -Is; }

log_init() {
  local log_dir="$1"
  local log_file="$2"
  mkdir -p "$log_dir"
  echo "[$(now)] START $MODE" | tee -a "$log_file"
}

log_line() {
  local log_file="$1"; shift
  echo "[$(now)] $*" | tee -a "$log_file"
}

sync_shared_workspace() {
  local repo_dir="/home/leoni/shared_workspace"
  local log_dir="$repo_dir/ops/logs"
  local log_file="$log_dir/repo_sync_shared_workspace.log"

  log_init "$log_dir" "$log_file"

  cd "$repo_dir"

  local branch
  branch="$(git rev-parse --abbrev-ref HEAD)"
  if [[ "$branch" != "main" ]]; then
    log_line "$log_file" "ERROR: expected branch main, got $branch"
    exit 3
  fi

  log_line "$log_file" "git fetch origin"
  git fetch --quiet origin

  local remote_inbox_changes
  remote_inbox_changes="$(git diff --name-only HEAD..origin/main -- inbox/ || true)"
  if [[ -n "$remote_inbox_changes" ]]; then
    log_line "$log_file" "Remote inbox changes detected; pulling (ff-only)"
    git pull --ff-only origin main
  else
    log_line "$log_file" "No remote inbox changes"
  fi

  if [[ -n "$(git status --porcelain)" ]]; then
    log_line "$log_file" "Local changes detected; committing + pushing"
    git add -A
    if ! git diff --cached --quiet; then
      local msg
      msg="Sync(shared): $(date +%F' '%R)"
      git commit -m "$msg" >/dev/null
      git push --quiet origin main
      log_line "$log_file" "PUSHED: $msg"
    else
      log_line "$log_file" "Nothing staged after add -A; skipping push"
    fi
  else
    log_line "$log_file" "No local changes to push"
  fi

  log_line "$log_file" "DONE"
}

sync_workspace_backup() {
  local repo_dir="/home/leoni/.openclaw/workspace"
  local log_dir="/home/leoni/.openclaw/workspace/ops/logs"
  local log_file="$log_dir/repo_sync_workspace_backup.log"

  log_init "$log_dir" "$log_file"

  cd "$repo_dir"

  local branch
  branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")"
  if [[ -z "$branch" ]]; then
    log_line "$log_file" "ERROR: not a git repo: $repo_dir"
    exit 4
  fi

  # No pull here: backup repo should only push local state.
  if [[ -n "$(git status --porcelain)" ]]; then
    log_line "$log_file" "Local workspace changes detected; committing + pushing"
    git add -A
    if ! git diff --cached --quiet; then
      local msg
      msg="Daily auto-sync $(date +%F)"
      git commit -m "$msg" >/dev/null || true
      git push --quiet origin "$branch" || git push --quiet origin main
      log_line "$log_file" "PUSHED: $msg"
    else
      log_line "$log_file" "Nothing staged after add -A; skipping push"
    fi
  else
    log_line "$log_file" "No local changes to push"
  fi

  log_line "$log_file" "DONE"
}

case "$MODE" in
  shared_workspace) sync_shared_workspace ;;
  workspace_backup) sync_workspace_backup ;;
  *) usage ;;
esac
