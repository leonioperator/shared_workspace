# EMAIL_CONFIG.md - E-mail küldési szabályok és workaroundok

Ez a fájl tartalmazza az AI agent által használt e-mail küldési beállításokat, workaroundokat és általános szabályokat.

## Himalaya send workaround (2026-04-13)

**FONTOS:** A raw emailt KIZÁRÓLAG STDIN-en add át (heredoc vagy pipe).
**TILOS:** `himalaya message send "..."`, `himalaya message send $(cat ...)`, `himalaya message send "$(cat ...)"`
**Ok:** Himalaya v1.2.0 argumentumos módban mail-parser panic (index out of bounds).

## E-mail kódolási szabályok

**FONTOS:** A Subject sorban NE legyen ékezetes karakter (á, é, í, ó, ö, ő, ú, ü, ű) és NE legyen em-dash (—)!
**Helyes példa:** `Subject: Reggeli brief - 2026-04-20 (Monday)`
**Hibás példa:** `Subject: Reggeli brief — 2026-04-20 (hétfő)`
**Megjegyzés:** A body-ban lehet ékezetes szöveg (quoted-printable kezeli), de a Subject-ben nem!

---

## Alapértelmezett e-mail küldési minta

```
himalaya message send -a default <<'EOF'
MIME-Version: 1.0
From: Leoni Operator <leoni.operator@vinczetamas.hu>
To: vt@vinczetamas.hu
Subject: [Tárgy ide, ékezet és em-dash nélkül]
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

[e-mail szöveg ide]
EOF
```
