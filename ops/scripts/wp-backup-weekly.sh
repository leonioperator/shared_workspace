#!/bin/bash
set -euo pipefail

# Weekly WordPress Backup Script
# Teljes backup: DB + fájlok
# Cron: vasárnap 02:00 CET

# Load env
source /root/.env

DATE=$(date +%F)
BACKUP_ROOT="/backup"
SITES=("vinczetamas.hu" "elkezdodott.hu")

log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
}

telegram_alert() {
  # TODO: Telegram message tool hívás (OpenClaw API vagy curl)
  log "ALERT: $*"
}

# Cleanup old backups (>30 days)
cleanup() {
  log "Cleanup: régi backupok törlése (>30 nap)"
  find "$BACKUP_ROOT" -type d -mtime +30 -exec rm -rf {} + 2>/dev/null || true
}

# Health check
health_check() {
  local url="$1"
  log "Health check: $url"
  if ! curl -sSf -m 60 "$url" > /dev/null; then
    telegram_alert "Health check FAILED: $url"
    return 1
  fi
  log "Health check OK"
}

# Backup single site
backup_site() {
  local site="$1"
  local path_var="${site//./_}_WPCLI_PATH"
  local path="${!path_var}"
  local backup_dir="$BACKUP_ROOT/$site/$DATE"
  
  log "========================================="
  log "Backup START: $site"
  log "========================================="
  
  mkdir -p "$backup_dir"
  
  # 1. DB export
  log "DB export..."
  sshpass -p "$SSH_USER_PASSWORD" ssh -o StrictHostKeyChecking=no -p "$SSH_TARGET_PORT" \
    "$SSH_USER_NAME@$SSH_TARGET_IP" \
    "wp db export --path=$path" > "$backup_dir/database.sql" 2>&1
  
  if [ $? -ne 0 ]; then
    telegram_alert "DB export FAILED: $site"
    return 1
  fi
  
  log "DB export OK: $(du -h "$backup_dir/database.sql" | cut -f1)"
  
  # 2. Files tar.gz (wp-content only, ~90% of data)
  log "Files backup..."
  sshpass -p "$SSH_USER_PASSWORD" ssh -o StrictHostKeyChecking=no -p "$SSH_TARGET_PORT" \
    "$SSH_USER_NAME@$SSH_TARGET_IP" \
    "cd $path && tar -czf - wp-content wp-config.php" > "$backup_dir/files.tar.gz" 2>&1
  
  if [ $? -ne 0 ]; then
    telegram_alert "Files backup FAILED: $site"
    return 1
  fi
  
  log "Files backup OK: $(du -h "$backup_dir/files.tar.gz" | cut -f1)"
  
  # 3. Git push DB dump to shared_workspace
  log "Git push DB dump..."
  cp "$backup_dir/database.sql" "/root/shared_workspace/ops/backups/$site-$DATE.sql"
  cd /root/shared_workspace
  git add ops/backups/
  git commit -m "Backup: $site $DATE" || true
  git pull --rebase origin main
  git push origin main
  
  log "Backup COMPLETE: $site"
}

# Main
log "========================================="
log "Weekly Backup START"
log "========================================="

mkdir -p "$BACKUP_ROOT"
mkdir -p /root/shared_workspace/ops/backups

for site in "${SITES[@]}"; do
  backup_site "$site" || telegram_alert "Backup FAILED: $site"
done

cleanup

# Health checks
health_check "https://vinczetamas.hu"
health_check "https://elkezdodott.hu"

log "========================================="
log "Weekly Backup COMPLETE"
log "========================================="
