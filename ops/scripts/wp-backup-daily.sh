#!/bin/bash
set -euo pipefail

# Daily WordPress DB Backup Script
# Csak DB export (gyors, kis méret)
# Cron: minden nap 03:00 CET

# Load env
source /root/.env

DATE=$(date +%F)
BACKUP_ROOT="/backup"
SITES=("vinczetamas.hu" "elkezdodott.hu")

log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
}

telegram_alert() {
  # TODO: Telegram message tool hívás
  log "ALERT: $*"
}

# Cleanup old daily backups (>7 days)
cleanup() {
  log "Cleanup: napi backupok törlése (>7 nap)"
  for site in "${SITES[@]}"; do
    find "$BACKUP_ROOT/$site/daily" -type f -mtime +7 -delete 2>/dev/null || true
  done
}

# Backup DB only
backup_db() {
  local site="$1"
  local path_var="${site//./_}_WPCLI_PATH"
  local path="${!path_var}"
  local backup_dir="$BACKUP_ROOT/$site/daily"
  
  log "DB backup: $site"
  
  mkdir -p "$backup_dir"
  
  sshpass -p "$SSH_USER_PASSWORD" ssh -o StrictHostKeyChecking=no -p "$SSH_TARGET_PORT" \
    "$SSH_USER_NAME@$SSH_TARGET_IP" \
    "wp db export --path=$path" > "$backup_dir/$DATE.sql" 2>&1
  
  if [ $? -ne 0 ]; then
    telegram_alert "Daily DB backup FAILED: $site"
    return 1
  fi
  
  log "DB backup OK: $(du -h "$backup_dir/$DATE.sql" | cut -f1)"
  
  # Git push
  cp "$backup_dir/$DATE.sql" "/root/shared_workspace/ops/backups/$site-daily-$DATE.sql"
  cd /root/shared_workspace
  git add ops/backups/
  git commit -m "Daily backup: $site $DATE" || true
  git pull --rebase origin main
  git push origin main
}

# Main
log "========================================="
log "Daily DB Backup START"
log "========================================="

mkdir -p /root/shared_workspace/ops/backups

for site in "${SITES[@]}"; do
  backup_db "$site" || telegram_alert "Daily backup FAILED: $site"
done

cleanup

log "Daily DB Backup COMPLETE"
