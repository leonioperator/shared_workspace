#!/bin/bash
###############################################################################
# Leoni Operator — Full Bootstrap Script
# 
# Használat: Friss Ubuntu 24.04 LTS-en, root-ként:
#   curl -sL https://raw.githubusercontent.com/leonioperator/shared_workspace/main/recovery/bootstrap.sh | bash
#   VAGY:
#   git clone git@github.com:leonioperator/shared_workspace.git /root/shared_workspace
#   bash /root/shared_workspace/recovery/bootstrap.sh
#
# Ez a script mindent telepít ami kell ahhoz, hogy OpenClaw + Leoni elinduljon.
# Utána Leoni átveszi és befejezi a recovery-t (cron jobok, tesztelés).
#
# FONTOS: A script FUTÁS ELŐTT kéri a szükséges secreteket (.env tartalom).
# Ha a /root/.env már létezik, azt használja.
#
# Utolsó frissítés: 2026-02-17
###############################################################################

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() { echo -e "${GREEN}[BOOTSTRAP]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
err() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

###############################################################################
# 0. Pre-flight checks
###############################################################################
log "Pre-flight checks..."
[ "$(id -u)" -eq 0 ] || err "Root jogosultság szükséges!"
[ -f /etc/lsb-release ] && grep -q "24.04" /etc/lsb-release || warn "Nem Ubuntu 24.04 — lehet hogy nem minden működik."

###############################################################################
# 1. Secrets (.env)
###############################################################################
if [ ! -f /root/.env ]; then
  warn "A /root/.env fájl nem létezik!"
  echo ""
  echo "Másold be a .env tartalmát a régi szerverről, vagy hozd létre manuálisan:"
  echo "  nano /root/.env"
  echo ""
  echo "Szükséges kulcsok:"
  echo "  EMAIL_ADDRESS, EMAIL_PASSWORD"
  echo "  EMAIL_IMAP_HOST, EMAIL_IMAP_PORT, EMAIL_SMTP_HOST, EMAIL_SMTP_PORT"
  echo "  GITHUB_TOKEN, GITHUB_USER"
  echo "  SSH_TARGET_IP, SSH_TARGET_PORT, SSH_USER_NAME, SSH_USER_PASSWORD"
  echo "  VINCZETAMAS_WP_URL, VINCZETAMAS_WP_USER, VINCZETAMAS_WP_PASSWORD, VINCZETAMAS_WP_APP_PASSWORD, VINCZETAMAS_WPCLI_PATH"
  echo "  MAINWP_DASHBOARD_URL, MAINWP_BEARER_TOKEN"
  echo "  ELKEZDODOTT_WP_URL, ELKEZDODOTT_WP_USER, ELKEZDODOTT_WP_PASSWORD, ELKEZDODOTT_WP_APP_PASSWORD, ELKEZDODOTT_WP_CLI_PATH"
  echo "  OPENAI_API_KEY, BRAVE_API_KEY, ELEVENLABS_AP_KEY"
  echo "  GOOGLE_GEMINI_API_KEY, GEMINI_API_KEY"
  echo "  TTS_DEFAULT, TTS_ELEVENLABS_VOICE_ID, TTS_ELEVENLABS_MODEL"
  echo "  TWILIO_ACCOUNT_SID, TWILIO_PHONE_NUMBER, TWILIO_AUT_TOKEN"
  echo ""
  read -p "Nyomj ENTER-t ha kész, vagy Ctrl+C a kilépéshez: "
  [ -f /root/.env ] || err "/root/.env még mindig nem létezik!"
fi

log ".env OK"

###############################################################################
# 2. System packages
###############################################################################
log "System csomagok telepítése..."
apt-get update -qq
apt-get install -y -qq \
  build-essential cmake git curl wget \
  python3 python3-pip python3-venv \
  ffmpeg sshpass imagemagick \
  jq unzip htop tmux \
  chromium-browser \
  > /dev/null 2>&1

log "System csomagok OK"

###############################################################################
# 3. Node.js 22 LTS
###############################################################################
if ! command -v node &>/dev/null || ! node --version | grep -q "v22"; then
  log "Node.js 22 telepítése..."
  curl -fsSL https://deb.nodesource.com/setup_22.x | bash - > /dev/null 2>&1
  apt-get install -y -qq nodejs > /dev/null 2>&1
fi
log "Node.js $(node --version) OK"

###############################################################################
# 4. SSH keys
###############################################################################
if [ ! -f /root/.ssh/id_ed25519 ]; then
  log "SSH kulcs generálása..."
  ssh-keygen -t ed25519 -f /root/.ssh/id_ed25519 -N "" -q
  echo ""
  warn "ÚJ SSH KULCS GENERÁLVA! Add hozzá a GitHub-hoz (leonioperator account):"
  cat /root/.ssh/id_ed25519.pub
  echo ""
  read -p "Nyomj ENTER-t ha hozzáadtad a GitHub-hoz: "
else
  log "SSH kulcs OK"
fi

###############################################################################
# 5. OpenClaw
###############################################################################
if ! command -v openclaw &>/dev/null; then
  log "OpenClaw telepítése..."
  npm install -g openclaw > /dev/null 2>&1
fi
log "OpenClaw $(openclaw --version 2>&1) OK"

###############################################################################
# 6. Git repos klónozása
###############################################################################
# Workspace
if [ ! -d /root/.openclaw/workspace/.git ]; then
  log "Workspace repo klónozása..."
  mkdir -p /root/.openclaw
  git clone git@github.com:leonioperator/workspace.git /root/.openclaw/workspace
else
  log "Workspace repo OK (pull)..."
  cd /root/.openclaw/workspace && git pull --ff-only
fi

# Shared workspace
if [ ! -d /root/shared_workspace/.git ]; then
  log "Shared workspace repo klónozása..."
  git clone git@github.com:leonioperator/shared_workspace.git /root/shared_workspace
else
  log "Shared workspace repo OK (pull)..."
  cd /root/shared_workspace && git pull --ff-only
fi

###############################################################################
# 7. OpenClaw konfiguráció
###############################################################################
log "OpenClaw konfigurálás..."
if [ ! -f /root/.openclaw/openclaw.json ]; then
  if [ -f /root/shared_workspace/recovery/openclaw.json.template ]; then
    cp /root/shared_workspace/recovery/openclaw.json.template /root/.openclaw/openclaw.json
    warn "openclaw.json TEMPLATE-ből létrehozva!"
    warn "Szerkeszd és töltsd ki a __FILL_IN__ mezőket:"
    warn "  nano /root/.openclaw/openclaw.json"
    warn "Szükséges: Telegram botToken, Anthropic/OpenAI API key, Twilio tokens"
    read -p "Nyomj ENTER-t ha kész: "
  else
    warn "openclaw.json nem létezik — futtasd: openclaw configure"
    read -p "Futtassam az 'openclaw configure'-t? [y/N]: " CONF
    if [ "$CONF" = "y" ] || [ "$CONF" = "Y" ]; then
      openclaw configure
    fi
  fi
else
  log "openclaw.json OK"
fi

###############################################################################
# 8. Himalaya (email kliens)
###############################################################################
if ! command -v himalaya &>/dev/null; then
  log "Himalaya telepítése..."
  HIMALAYA_VERSION="1.0.0"
  wget -q "https://github.com/pimalaya/himalaya/releases/latest/download/himalaya-x86_64-unknown-linux-gnu.tar.gz" -O /tmp/himalaya.tar.gz
  tar -xzf /tmp/himalaya.tar.gz -C /usr/local/bin/
  chmod +x /usr/local/bin/himalaya
  rm /tmp/himalaya.tar.gz
fi
log "Himalaya OK"

# Himalaya config
mkdir -p /root/.config/himalaya
if [ ! -f /root/.config/himalaya/config.toml ]; then
  if [ -f /root/shared_workspace/recovery/himalaya-config.toml.template ]; then
    source /root/.env
    # Substitute env vars into template
    envsubst < /root/shared_workspace/recovery/himalaya-config.toml.template > /root/.config/himalaya/config.toml 2>/dev/null || true
  fi
  # Fallback: generate from .env
  if [ ! -f /root/.config/himalaya/config.toml ] || ! grep -q "imap" /root/.config/himalaya/config.toml; then
    source /root/.env
    cat > /root/.config/himalaya/config.toml << HIMALAYA
[accounts.default]
email = "${EMAIL_ADDRESS}"
display-name = "Leoni Operator"
default = true
backend.type = "imap"
backend.host = "${EMAIL_IMAP_HOST}"
backend.port = ${EMAIL_IMAP_PORT}
backend.encryption.type = "tls"
backend.login = "${EMAIL_ADDRESS}"
backend.auth.type = "password"
backend.auth.cmd = "printf %s ${EMAIL_PASSWORD}"

message.send.backend.type = "smtp"
message.send.backend.host = "${EMAIL_SMTP_HOST}"
message.send.backend.port = ${EMAIL_SMTP_PORT}
message.send.backend.encryption.type = "start-tls"
message.send.backend.login = "${EMAIL_ADDRESS}"
message.send.backend.auth.type = "password"
message.send.backend.auth.cmd = "printf %s ${EMAIL_PASSWORD}"

folder.aliases.inbox = "INBOX"
folder.aliases.sent = "INBOX.Sent"
folder.aliases.drafts = "INBOX.Drafts"
folder.aliases.trash = "INBOX.Trash"

message.send.save-copy = true
HIMALAYA
    log "Himalaya config létrehozva"
  fi
else
  log "Himalaya config OK"
fi

###############################################################################
# 9. ClawGuard + extra tools
###############################################################################
log "ClawGuard + extra tools..."
npm install -g @jaydenbeard/clawguard clawhub opencode-ai > /dev/null 2>&1
log "ClawGuard $(clawguard --version 2>&1) OK"

###############################################################################
# 10. Kanban Board
###############################################################################
if [ ! -d /root/kanban ]; then
  log "Kanban board telepítése..."
  mkdir -p /root/kanban
  # A Kanban forráskód a workspace-ben van, másoljuk
  if [ -d /root/.openclaw/workspace/ops/kanban ]; then
    cp -r /root/.openclaw/workspace/ops/kanban/* /root/kanban/
  else
    warn "Kanban forráskód nem található workspace/ops/kanban/ -ban!"
    warn "Manuálisan kell visszaállítani."
  fi
  cd /root/kanban && npm install > /dev/null 2>&1
  # Restore tasks
  if [ -f /root/.openclaw/workspace/ops/kanban/tasks.json ]; then
    cp /root/.openclaw/workspace/ops/kanban/tasks.json /root/kanban/tasks.json
    log "Kanban tasks restored"
  fi
fi

# Kanban systemd service
cat > /etc/systemd/system/kanban.service << 'SVC'
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
SVC

# Kanban CLI
cat > /usr/local/bin/kanban << 'KANBANCLI'
#!/bin/bash
API="http://localhost:3848/api"
case "$1" in
  list)
    FILTER="$2"
    curl -s "$API/tasks" | python3 -c "
import sys,json
d=json.load(sys.stdin)
filt='$FILTER'
for c in d['columns']:
    if filt and c['id'] != filt:
        continue
    if c['id'] == 'archive' and not filt:
        continue
    if c['tasks']:
        print(f\"\\n[{c['title']}] ({len(c['tasks'])})\")
        for t in c['tasks']:
            p = t.get('priority','?')
            a = t.get('assignee','')
            print(f\"  {t['id']} | {p.upper():6} | {t['title']} {('('+a+')') if a else ''}\" )
" ;;
  add) curl -s -X POST "$API/tasks" -H 'Content-Type: application/json' -d "{\"columnId\":\"$2\",\"title\":\"$3\",\"description\":\"${4:-}\",\"priority\":\"${5:-medium}\",\"assignee\":\"${6:-Leoni}\"}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Created: {d[\"id\"]} | {d[\"title\"]}')" ;;
  move) curl -s -X POST "$API/tasks/$2/move" -H 'Content-Type: application/json' -d "{\"targetColumnId\":\"$3\"}" | python3 -c "import sys,json; d=json.load(sys.stdin); print('Moved OK' if d.get('ok') else f'Error: {d}')" ;;
  done) curl -s -X POST "$API/tasks/$2/move" -H 'Content-Type: application/json' -d '{"targetColumnId":"done"}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Moved to Done' if d.get('ok') else f'Error: {d}')" ;;
  review) curl -s -X POST "$API/tasks/$2/move" -H 'Content-Type: application/json' -d '{"targetColumnId":"review"}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Moved to Review' if d.get('ok') else f'Error: {d}')" ;;
  find) curl -s "$API/tasks" | python3 -c "import sys,json; d=json.load(sys.stdin); s='$2'.lower(); [print(f\"{t['id']} | {c['title']:12} | {t['title']}\") for c in d['columns'] for t in c['tasks'] if s in t['title'].lower()]" ;;
  delete) curl -s -X DELETE "$API/tasks/$2" | python3 -c "import sys,json; d=json.load(sys.stdin); print('Deleted' if d.get('ok') else f'Error: {d}')" ;;
  archive) curl -s -X POST "$API/tasks/archive" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Archived: {d[\"archived\"]} tasks (total in archive: {d[\"total_archive\"]})')" ;;
  *) echo "Usage: kanban {list|add|move|done|review|find|delete|archive} [args]" ;;
esac
KANBANCLI
chmod +x /usr/local/bin/kanban
log "Kanban OK"

###############################################################################
# 11. TokenCTL Dashboard
###############################################################################
if [ ! -d /root/tokenctl ]; then
  log "TokenCTL dashboard..."
  if [ -d /root/.openclaw/workspace/ops/tokenctl ]; then
    mkdir -p /root/tokenctl
    cp -r /root/.openclaw/workspace/ops/tokenctl/* /root/tokenctl/
    cd /root/tokenctl && npm install > /dev/null 2>&1
  else
    warn "TokenCTL forráskód nem található!"
  fi
fi

cat > /etc/systemd/system/tokenctl.service << 'SVC'
[Unit]
Description=TokenCTL Dashboard
After=network.target

[Service]
Type=simple
WorkingDirectory=/root/tokenctl
ExecStart=/usr/bin/node /root/tokenctl/server.js
Restart=on-failure
RestartSec=5
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
SVC
log "TokenCTL OK"

###############################################################################
# 12. TTS / Voice Clone setup
###############################################################################
log "TTS setup..."

# Sherpa-onnx (berta - default free TTS)
if [ ! -d /root/.openclaw/tools/sherpa-onnx-tts ]; then
  warn "Sherpa-onnx nem található. OpenClaw fogja telepíteni az első TTS hívásnál."
fi

# Python venv for Coqui TTS (voice cloning)
if [ ! -d /opt/tts-venv ]; then
  log "Coqui TTS venv létrehozása..."
  python3 -m venv /opt/tts-venv
  /opt/tts-venv/bin/pip install -q TTS 2>/dev/null || warn "TTS pip install sikertelen (lehet hogy kell GPU/CPU config)"
fi

# Voice reference files
mkdir -p /usr/local/share/tts-voices/{tomi,evi,leoni}
if [ -d /root/shared_workspace/processed ]; then
  [ -f /root/shared_workspace/processed/Evi-hang.ogg ] && \
    ffmpeg -i /root/shared_workspace/processed/Evi-hang.ogg -ar 22050 -ac 1 /usr/local/share/tts-voices/evi/reference.wav -y 2>/dev/null && \
    log "Evi voice reference OK"
  [ -f /root/shared_workspace/processed/Leoni-hang.ogg ] && \
    ffmpeg -i /root/shared_workspace/processed/Leoni-hang.ogg -ar 22050 -ac 1 /usr/local/share/tts-voices/leoni/reference.wav -y 2>/dev/null && \
    log "Leoni voice reference OK"
fi

# Voice generate scripts from workspace backup
for voice in tomi evi leoni; do
  if [ -f /root/.openclaw/workspace/ops/tts-voices/$voice/generate.py ]; then
    cp /root/.openclaw/workspace/ops/tts-voices/$voice/generate.py /usr/local/share/tts-voices/$voice/generate.py
    log "Voice script restored: $voice"
  else
    warn "Voice generate script hiányzik: $voice"
  fi
done

# speak wrapper
cat > /usr/local/bin/speak << 'SPEAKEOF'
#!/bin/bash
TEXT="$1"
VOICE="${2:-berta}"
OUTFILE="${3:-/tmp/tts-output.ogg}"
source /root/.env 2>/dev/null

if [ "$VOICE" = "leoni-local" ]; then
  /opt/tts-venv/bin/python /usr/local/share/tts-voices/leoni/generate.py "$TEXT" /tmp/tts-tmp-leoni.wav "${4:-hu}" 2>/dev/null
  ffmpeg -i /tmp/tts-tmp-leoni.wav -c:a libopus "$OUTFILE" -y 2>/dev/null
elif [ "$VOICE" = "evi" ]; then
  /opt/tts-venv/bin/python /usr/local/share/tts-voices/evi/generate.py "$TEXT" /tmp/tts-tmp-evi.wav "${4:-hu}" 2>/dev/null
  ffmpeg -i /tmp/tts-tmp-evi.wav -c:a libopus "$OUTFILE" -y 2>/dev/null
elif [ "$VOICE" = "tomi" ]; then
  /opt/tts-venv/bin/python /usr/local/share/tts-voices/tomi/generate.py "$TEXT" /tmp/tts-tmp-tomi.wav "${4:-hu}" 2>/dev/null
  ffmpeg -i /tmp/tts-tmp-tomi.wav -c:a libopus "$OUTFILE" -y 2>/dev/null
elif [ "$VOICE" = "leoni" ]; then
  curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/$TTS_ELEVENLABS_VOICE_ID" \
    -H "xi-api-key: $ELEVENLABS_AP_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"text\":\"$TEXT\",\"model_id\":\"$TTS_ELEVENLABS_MODEL\",\"voice_settings\":{\"stability\":0.5,\"similarity_boost\":0.75,\"style\":0.0}}" \
    --output /tmp/tts-tmp.mp3
  ffmpeg -i /tmp/tts-tmp.mp3 -c:a libopus "$OUTFILE" -y 2>/dev/null
else
  export LD_LIBRARY_PATH=~/.openclaw/tools/sherpa-onnx-tts/runtime/lib
  MODEL_DIR=~/.openclaw/tools/sherpa-onnx-tts/models/vits-piper-hu_HU-berta-medium-int8
  ~/.openclaw/tools/sherpa-onnx-tts/runtime/bin/sherpa-onnx-offline-tts \
    --vits-model="$MODEL_DIR/hu_HU-berta-medium.onnx" \
    --vits-tokens="$MODEL_DIR/tokens.txt" \
    --vits-data-dir="$MODEL_DIR/espeak-ng-data" \
    --output-filename=/tmp/tts-tmp.wav \
    "$TEXT" 2>/dev/null
  ffmpeg -i /tmp/tts-tmp.wav -c:a libopus "$OUTFILE" -y 2>/dev/null
fi
echo "$OUTFILE"
SPEAKEOF
chmod +x /usr/local/bin/speak
log "TTS OK"

###############################################################################
# 13. Systemd services indítása
###############################################################################
log "Systemd services..."
systemctl daemon-reload
systemctl enable --now kanban.service 2>/dev/null || warn "Kanban service hiba"
systemctl enable --now tokenctl.service 2>/dev/null || warn "TokenCTL service hiba"
log "Services OK"

# ClawGuard (nem systemd, háttérben fut)
nohup clawguard > /var/log/clawguard.log 2>&1 &
log "ClawGuard elindítva"

# ClawGuard patches
if [ -d /root/.openclaw/workspace/ops/clawguard-patches ]; then
  for patch in /root/.openclaw/workspace/ops/clawguard-patches/*.sh; do
    bash "$patch" 2>/dev/null
  done
  log "ClawGuard patches alkalmazva"
fi

###############################################################################
# 14. IP-függő konfigok frissítése
###############################################################################
PUBLIC_IP=$(curl -s ifconfig.me 2>/dev/null || curl -s icanhazip.com 2>/dev/null || echo "UNKNOWN")
log "Publikus IP: $PUBLIC_IP"

if [ "$PUBLIC_IP" != "UNKNOWN" ] && [ -f /root/.openclaw/openclaw.json ]; then
  # Frissítsd a Twilio publicUrl-t az új IP-re
  sed -i "s|http://[0-9.]*:3001/voice|http://$PUBLIC_IP:3001/voice|g" /root/.openclaw/openclaw.json
  log "Twilio publicUrl frissítve: http://$PUBLIC_IP:3001/voice"
  warn "FONTOS: A Twilio dashboard-on is frissítsd a webhook URL-t!"
  warn "  https://console.twilio.com → Phone Numbers → $PUBLIC_IP:3001/voice"
fi

###############################################################################
# 15. OpenClaw indítása
###############################################################################
log "OpenClaw indítása..."
openclaw gateway start

###############################################################################
# KÉSZ
###############################################################################
echo ""
echo "============================================================"
echo -e "${GREEN}  BOOTSTRAP KÉSZ!${NC}"
echo "============================================================"
echo ""
echo "  OpenClaw fut. Leoni hamarosan jelentkezik Telegramon."
echo ""
echo "  Leoni első feladata: recovery/RECOVERY-CHECKLIST.md"
echo "  végrehajtása — cron jobok, tesztek, verifikáció."
echo ""
echo "  Portok:"
echo "    18789 — OpenClaw Gateway (localhost)"
echo "    3001  — Twilio Voice webhook"
echo "    3847  — ClawGuard UI"
echo "    3848  — Kanban Board"
echo "    3849  — TokenCTL Dashboard"
echo ""
echo "  Ha valami nem működik:"
echo "    openclaw status"
echo "    openclaw gateway logs"
echo "    journalctl -u kanban -f"
echo ""
echo "============================================================"
