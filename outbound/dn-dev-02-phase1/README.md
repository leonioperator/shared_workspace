# dn-dev-02 Phase 1 pack (kritikus fixek)

Cél: a **publikus dev gateway** lezárása, és egy minimál **backup + deploy** alap bevezetése.

## Mit kapsz ebben a packban?

- `secure-dev-gateway.sh` – `.env` patch, hogy a dev gateway csak loopback legyen (127.0.0.1)
- `backup.sh` – SQLite + snapshot backup (tömörített), 7 nap retention
- `deploy.sh` – idempotens compose deploy (pull + up -d), opcionális backup hívással
- `cron.example` – minta cron bejegyzések

## Futási sorrend (javaslat)

1) **secure-dev-gateway.sh**

2) **backup.sh** (egyszer kézzel, hogy lásd hogy jó helyre ment)

3) **cron beállítás** (backup naponta 03:10)

4) **deploy.sh** (kézzel egyszer, aztán csak ha frissítesz)

## Kell hozzá

- SSH hozzáférés a dn-dev-02-re
- Docker Compose (v2) elérhető legyen (`docker compose`)

## Megjegyzés

Ezek a scriptek **nem tartalmaznak secreteket**. Ha a szerveren eltérnek az útvonalak, a README-ben jelzett környezeti változókkal állítható.

