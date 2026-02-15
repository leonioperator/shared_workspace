# Ops Scripts — WordPress Backup & Automation

Automatizált maintenance scriptek WordPress oldalakhoz.

---

## wp-backup-weekly.sh

**Cél:** Teljes heti backup (DB + fájlok)

**Mikor:** Vasárnap 02:00 CET

**Mit csinál:**
1. DB export (`wp db export`)
2. wp-content/, uploads/, themes/, plugins/ tar.gz-be
3. wp-config.php mentés
4. Fájlok: `/backup/<site>/YYYY-MM-DD/`
5. DB dump: git push shared_workspace
6. Régi backupok törlése (>30 nap)
7. Health check (site elérhető?)
8. Telegram alert ha hiba

**Függőségek:**
- WP-CLI 2.12+
- sshpass
- tar, gzip
- curl (health check)

**Env változók:** (`.env`)
```bash
SSH_TARGET_IP
SSH_TARGET_PORT
SSH_USER_NAME
SSH_USER_PASSWORD
VINCZETAMAS_WPCLI_PATH
ELKEZDODOTT_WPCLI_PATH
```

**Használat:**
```bash
/root/shared_workspace/ops/scripts/wp-backup-weekly.sh
```

**Cron setup:**
```bash
# Heti vasárnap 02:00 CET
0 2 * * 0 /root/shared_workspace/ops/scripts/wp-backup-weekly.sh >> /var/log/wp-backup-weekly.log 2>&1
```

**Log:** `/var/log/wp-backup-weekly.log`

---

## wp-backup-daily.sh

**Cél:** Napi DB backup (gyors, kis méret)

**Mikor:** Minden nap 03:00 CET

**Mit csinál:**
1. DB export (`wp db export`)
2. Fájl: `/backup/<site>/daily/YYYY-MM-DD.sql`
3. Git push shared_workspace
4. Régi napi backupok törlése (>7 nap)
5. Telegram alert ha hiba

**Függőségek:** (mint weekly)

**Használat:**
```bash
/root/shared_workspace/ops/scripts/wp-backup-daily.sh
```

**Cron setup:**
```bash
# Minden nap 03:00 CET
0 3 * * * /root/shared_workspace/ops/scripts/wp-backup-daily.sh >> /var/log/wp-backup-daily.log 2>&1
```

**Log:** `/var/log/wp-backup-daily.log`

---

## Backup retention

- **Heti teljes:** 4 hét (30 nap)
- **Napi DB:** 7 nap
- Automatikus cleanup mindkét scriptben

---

## Recovery

### Teljes restore (heti backupból)
```bash
# DB
wp db import /backup/vinczetamas.hu/2026-02-16/database.sql \
  --path=/home/hogyanvi/addond/vinczetamas.hu

# Fájlok
cd /home/hogyanvi/addond/vinczetamas.hu
tar -xzf /backup/vinczetamas.hu/2026-02-16/files.tar.gz
```

### Csak DB restore (napi backupból)
```bash
wp db import /backup/vinczetamas.hu/daily/2026-02-15.sql \
  --path=/home/hogyanvi/addond/vinczetamas.hu
```

---

## Monitoring

- Sikeres backup: csak log
- Sikertelen backup: **Telegram alert Tominak**
- Health check timeout (>60s): alert

---

## Jövőbeli bővítés

- [ ] Remote storage (Google Drive / Hetzner Storage Box)
- [ ] Backup encryption (gpg)
- [ ] Incremental file backup (rsync)
- [ ] Multi-site support (loop minden WP path-en)
