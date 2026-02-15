# RECOVERY.md — Teljes rendszer újjáépítési útmutató

**Utolsó frissítés:** 2026-02-15
**Cél:** Ha a VPS meghal, EBBŐL építed újra a teljes működő rendszert.

---

## 1. VPS alapadatok

- **OS:** Ubuntu 24.04.3 LTS (noble)
- **Kernel:** 6.8.0-100-generic (x64)
- **Hozzáférés:** root
- **Hostname:** dn-optigen-01

---

## 2. Alapcsomagok telepítése

```bash
apt update && apt upgrade -y
apt install -y curl git tmux build-essential
```

### Node.js (v22.x)
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
# Ellenőrzés: node --version → v22.22.0, npm --version → 10.9.4
```

### Himalaya (email CLI, v1.1.0)
```bash
curl -sSL https://raw.githubusercontent.com/pimalaya/himalaya/master/install.sh | sh
# Ellenőrzés: himalaya --version
```

---

## 3. SSH kulcs (GitHub hozzáférés)

```bash
ssh-keygen -t ed25519 -C "leoni.operator@vinczetamas.hu"
# Public key hozzáadása a GitHub leonioperator accounthoz:
# https://github.com/settings/keys
```

**Jelenlegi public key:**
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOQv5MuTxteak0YF3htjUaxBae9qb9D5s5pOkZe0D7Tz leoni.operator@vinczetamas.hu
```

**Git config:**
```bash
git config --global user.name "Leoni Operator"
git config --global user.email "leoni.operator@vinczetamas.hu"
```

---

## 4. OpenClaw telepítés

```bash
npm install -g openclaw@2026.2.13
```

**Config helye:** `~/.openclaw/openclaw.json` (secretek env variable-ből, NE ide)
**Workspace:** `~/.openclaw/workspace/`
**Session logok:** `~/.openclaw/agents/main/sessions/*.jsonl`

OpenClaw indítás:
```bash
openclaw gateway start
```

---

## 5. Globális NPM csomagok

```bash
npm install -g openclaw@2026.2.13
npm install -g @jaydenbeard/clawguard@0.4.1
npm install -g clawhub@0.6.1
npm install -g opencode-ai@1.2.1
```

---

## 6. Email konfiguráció (Himalaya)

**Fiók:** leoni.operator@vinczetamas.hu (saját fiók, autonóm kezelés)
**Szerver:** thsixtyfour.tarhely.eu (vinczetamas.hu tárhelyen)

**Config fájl:** `~/.config/himalaya/config.toml`
```toml
[accounts.default]
email = "leoni.operator@vinczetamas.hu"
display-name = "Leoni Operator"
default = true
backend.type = "imap"
backend.host = "thsixtyfour.tarhely.eu"
backend.port = 993
backend.encryption.type = "tls"
backend.login = "leoni.operator@vinczetamas.hu"
backend.auth.type = "password"
backend.auth.cmd = "printf %s <JELSZÓ_IDE>"

message.send.backend.type = "smtp"
message.send.backend.host = "thsixtyfour.tarhely.eu"
message.send.backend.port = 587
message.send.backend.encryption.type = "start-tls"
message.send.backend.login = "leoni.operator@vinczetamas.hu"
message.send.backend.auth.type = "password"
message.send.backend.auth.cmd = "printf %s <JELSZÓ_IDE>"

folder.aliases.inbox = "INBOX"
folder.aliases.sent = "INBOX.Sent"
folder.aliases.drafts = "INBOX.Drafts"
folder.aliases.trash = "INBOX.Trash"

message.send.save-copy = true
```

**FONTOS:**
- IMAP port 993 TLS — működik
- SMTP port **587 STARTTLS** — működik (port 465 TLS NEM működik ezen a szerveren!)
- Folder aliasok: `folder.aliases` (NEM `folder.alias`)
- Jelszót Tomi adja meg újra rebuild esetén

---

## 7. GitHub repók

### shared_workspace (SSOT — közös munkaterület Tomival)
```bash
git clone git@github.com:leonioperator/shared_workspace.git /root/shared_workspace
```

- **Inbox workflow:** Tomi → `/root/shared_workspace/inbox/` → git push → Leoni heartbeat-kor pull + feldolgozás
- **Struktúra:**
  ```
  shared_workspace/
  ├── README.md
  ├── projects/
  ├── writing/ (drafts/, published/, archived/)
  ├── outbound/
  ├── project_ideas/
  ├── recovery/ (RECOVERY.md másolat)
  └── inbox/ (Tomi feladatai → feldolgozás után processed/)
  ```

---

## 8. ClawGuard (activity monitor)

```bash
npm install -g @jaydenbeard/clawguard@0.4.1
clawguard install  # systemd user service
clawguard          # indítás
```

- **Port:** 3847
- **Dashboard:** http://localhost:3847
- **Auto-start:** systemd user service (`~/.config/systemd/user/clawguard.service`)
- **Módosítás:** Kanban link hozzáadva a tab bar-hoz
  - Fájl: `/usr/lib/node_modules/@jaydenbeard/clawguard/public/index.html`
  - A Bookmarks tab után `<a>` elem a `http://localhost:3848` Kanban-ra

---

## 9. Kanban Board (feladatkezelő)

**Forráskód:** `/root/kanban/`
```
kanban/
├── server.js      # Express API szerver
├── package.json   # dependencies: express
├── tasks.json     # feladatok (JSON)
└── public/
    └── index.html # Drag & drop UI
```

**Telepítés rebuild után:**
```bash
mkdir -p /root/kanban
# Másold be a server.js, package.json, public/index.html fájlokat a GitHub repóból
cd /root/kanban
npm install
```

**Systemd service:** `/etc/systemd/system/kanban.service`
```ini
[Unit]
Description=Leoni Kanban Board
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/node /root/kanban/server.js
WorkingDirectory=/root/kanban
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
systemctl daemon-reload
systemctl enable kanban
systemctl start kanban
```

- **Port:** 3848
- **Dashboard:** http://localhost:3848
- **API:** GET/POST/PUT/DELETE /api/tasks, POST /api/tasks/:id/move

---

## 10. OpenClaw Cron jobok

Ezek az OpenClaw cron rendszerében vannak, nem system crontab-ban.

| Job | Schedule | Leírás |
|-----|----------|--------|
| Email and GitHub Check (daytime) | `0,30 5-21 * * *` CET | 30 percenként email + shared_workspace inbox check, csak 06:30-21:30 CET |
| Reggeli brief | `30 5 * * *` CET | Napi journal, tegnapi review, email check, brief Tominek Telegramon |
| Heti összefoglaló (hétfő) | `0 7 * * 1` CET | Heti report, MEMORY.md frissítés, recovery kit check, GitHub karbantartás |

**Újra létrehozás:** OpenClaw `cron add` paranccsal (lásd AGENTS.md a payloadokért).

---

## 11. Workspace fájl struktúra

```
~/.openclaw/workspace/
├── SOUL.md              # Ki vagyok
├── IDENTITY.md          # Bemutatkozás
├── USER.md              # Tomi profil
├── TOOLS.md             # Eszközök és konfig
├── AGENTS.md            # Működési szabályok
├── HEARTBEAT.md         # Heartbeat feladatok
├── TASKS.md             # Feladat tracker
├── MEMORY.md            # Hosszú távú memória
├── BLOG-STYLE.md        # Blog stílus útmutató
├── BLOG-SITE.md         # Blog technikai setup
├── BLOG-DESIGN-INSTRUCTION.md  # WP design spec
├── memory/
│   └── YYYY-MM-DD.md    # Napi journalok
├── recovery/
│   └── RECOVERY.md      # EZ A FÁJL
├── research/
├── artifacts/
└── skills/
    └── himalaya/        # Email skill
```

---

## 12. Portok összefoglaló

| Port | Szolgáltatás | Hozzáférés |
|------|-------------|------------|
| 3847 | ClawGuard | localhost |
| 3848 | Kanban Board | localhost |

---

## 13. Rebuild sorrend

1. Alapcsomagok (apt, node, git, himalaya)
2. SSH kulcs generálás + GitHub-hoz kötés
3. Git config
4. `git clone` shared_workspace → `/root/shared_workspace`
5. OpenClaw telepítés + config (Tomi segít a secretekkel)
6. Workspace fájlok visszaállítása (shared_workspace/recovery/ + workspace fájlok)
7. Himalaya email config (jelszó Tomitól)
8. ClawGuard telepítés + indítás
9. Kanban telepítés + systemd service
10. ClawGuard UI módosítás (Kanban link)
11. OpenClaw cron jobok újra létrehozása
12. Teszt: email, GitHub, heartbeat, Telegram

---

*Ez a fájl a rendszered gerince. MINDIG frissítsd, ha bármi változik.*
