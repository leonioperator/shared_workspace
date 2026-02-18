# OpenClaw/Claude API Token Költségcsökkentési Jelentés

**Dátum:** 2026-02-17  
**Jelenlegi setup:** Claude Opus 4.6 ($5/MTok input, $25/MTok output)

---

## Jelenlegi költségszerkezet (becsült)

Heavy user szinten (~50-200M token/hó) a költség **$70-150+/hó**. A mi setupunk (24/7 asszisztens, nagy system prompt, napi journal, tool hívások) inkább a felső tartomány.

### Hol megy el a token?

| Forrás | Arány | Leírás |
|--------|-------|--------|
| Kontextus akkumuláció | 40-50% | Session history minden kérésnél újraküldésre kerül |
| Tool output tárolás | 20-30% | JSON/log eredmények a historyban maradnak |
| System prompt | 10-15% | AGENTS.md + TOOLS.md + SOUL.md stb. minden hívásnál |
| Multi-round reasoning | 10-15% | Összetett feladatok több API hívást igényelnek |
| Model választás | 5-10% | Opus 25x drágább mint Haiku |
| Cache miss-ek | 5-10% | Lejárt cache = teljes újra-számlázás |

---

## 1. Anthropic Prompt Caching (BEÉPÍTETT)

### Mi ez?
Az Anthropic natívan támogatja a prompt caching-et. A system prompt és a conversation history eleje cache-elhető, így ismételt kéréseknél csak **10%-át** fizetjük az input árnak.

### Árazás (Opus 4.6)

| Típus | Ár/MTok |
|-------|---------|
| Normál input | $5.00 |
| 5 perces cache write | $6.25 (1.25x) |
| 1 órás cache write | $10.00 (2x) |
| **Cache hit (olvasás)** | **$0.50 (0.1x)** |
| Output | $25.00 |

### Megtakarítás
Ha a kontextus 80%-a cache hit (tipikus aktív session):
- **Input költség csökkenés: ~70-80%**
- Feltétel: session aktív maradjon a TTL-en belül

### OpenClaw konfiguráció
```yaml
agents:
  defaults:
    model:
      primary: "anthropic/claude-opus-4-6"
    models:
      "anthropic/claude-opus-4-6":
        params:
          cacheRetention: "long"    # 1 órás cache
    heartbeat:
      every: "55m"                  # cache warm tartása
```

**A heartbeat kulcsfontosságú:** ha a cache lejár (1 óra), a teljes kontextust újra kell cache-elni ($10/MTok). 55 perces heartbeat-tel ez elkerülhető.

---

## 2. CacheForge

A "CacheForge" nevet az OpenClaw Discord közösségben említették, de **nem találtam önálló, publikusan elérhető eszközt** ezzel a névvel. Valószínűleg az alábbiak egyikére utaltak:

- Az OpenClaw beépített **cache-ttl pruning** funkciója (session pruning a cache lejárta után)
- Közösségi proxy megoldások (pl. "tapes" proxy layer ami API hívásokat loggol)
- Az Anthropic natív prompt caching konfigurálása OpenClaw-ban

**Javaslat:** Ha Tomi pontosabb referenciát talál a Discord-on, érdemes újra ránézni.

---

## 3. Model Routing (LEGNAGYOBB MEGTAKARÍTÁS)

### Árkülönbségek

| Modell | Input/MTok | Output/MTok | Cache hit/MTok | Relatív költség |
|--------|-----------|-------------|----------------|----------------|
| Opus 4.6 | $5.00 | $25.00 | $0.50 | 100% |
| Sonnet 4.5 | $3.00 | $15.00 | $0.30 | 60% |
| Sonnet 4 | $3.00 | $15.00 | $0.30 | 60% |
| Haiku 4.5 | $1.00 | $5.00 | $0.10 | 20% |
| Haiku 3.5 | $0.80 | $4.00 | $0.08 | 16% |
| Haiku 3 | $0.25 | $1.25 | $0.03 | 5% |

### Stratégia
- **Egyszerű feladatok** (email check, status, kérdés-válasz): **Haiku 4.5** ($1/$5)
- **Közepes feladatok** (kód írás, kutatás, blog draft): **Sonnet 4.5** ($3/$15)
- **Komplex feladatok** (architektúra döntések, kreatív munka): **Opus 4.6** ($5/$25)

### Becsült megtakarítás
Ha a feladatok 50%-a Haiku-ra, 30%-a Sonnet-re, 20%-a Opus-ra megy:
- **Átlagos költségcsökkenés: ~60-70%**

### OpenClaw konfiguráció
```yaml
agents:
  defaults:
    model:
      primary: "anthropic/claude-sonnet-4.5"  # alapértelmezett
  main:
    model:
      primary: "anthropic/claude-sonnet-4.5"
```
Opus-t kézileg `/model anthropic/claude-opus-4-6` paranccsal lehet váltani amikor kell.

---

## 4. Context Window Optimalizálás

### 4a. Rendszeres `/compact` használat
A `/compact` parancs összefoglalja a session history-t, drasztikusan csökkentve a kontextus méretét.
- **Megtakarítás: 30-50%** a session token használatból

### 4b. Új session indítása feladatonként
Ahelyett, hogy egy végtelen session-ben dolgozunk, feladatonként új session:
- `/session new` vagy automatikus session rotation
- **Megtakarítás: 20-40%** (nincs irreleváns kontextus akkumuláció)

### 4c. Bootstrap fájlok méretcsökkentése
Jelenlegi bootstrap: AGENTS.md + TOOLS.md + SOUL.md + USER.md + MEMORY.md stb.
- `bootstrapMaxChars` limit: 20,000 karakter/fájl (default)
- `bootstrapTotalMaxChars`: 150,000 karakter összesen
- **Javaslat:** AGENTS.md és TOOLS.md tömörítése, felesleges szekciók eltávolítása
- **Megtakarítás: 5-15%** az input tokenekből

### 4d. Tool output korlátozás
Nagy JSON/log outputok elkerülése; `read` parancsokat `limit`-tel használni.

---

## 5. Összefoglaló-alapú memória

Jelenlegi rendszer: napi memory fájlok + MEMORY.md a bootstrap-ben.

### Javaslat
- `memory/*.md` fájlok NEM kerülnek auto-inject-re (ez már így van az új OpenClaw-ban)
- MEMORY.md-t tartani tömören (max 2-3000 karakter)
- Napi journal-t csak on-demand olvasni, ne bootstrap-elni

---

## Összesített megtakarítási becslés

| Stratégia | Becsült megtakarítás | Implementálás nehézsége |
|-----------|---------------------|------------------------|
| Prompt caching + heartbeat | 70-80% input költség | Könnyű (config) |
| Model routing (Haiku/Sonnet default) | 60-70% teljes költség | Könnyű (config) |
| Rendszeres /compact | 30-50% session token | Szokás kérdése |
| Session rotation | 20-40% | Szokás kérdése |
| Bootstrap tömörítés | 5-15% | Egyszeri munka |

### Kombinált hatás (konzervatív becslés)
- **Jelenlegi:** Opus 4.6 mindenre, nincs cache optimalizáció = **100%**
- **Optimalizált:** Sonnet 4.5 default + cache + compact = **~15-25% az eredetinek**

**Vagyis 75-85%-os költségcsökkenés reális a minőség jelentős romlása nélkül.**

---

## Javasolt azonnali lépések

1. ✅ **Heartbeat beállítás** 55 percre a cache warm tartásához
2. ✅ **Default modell váltás** Sonnet 4.5-re (Opus csak ha kell)
3. ✅ **`cacheRetention: "long"`** bekapcsolása (1 órás cache)
4. ✅ **AGENTS.md és TOOLS.md tömörítése** (felesleges részek eltávolítása)
5. ✅ **Rendszeres `/compact`** szokás kialakítása hosszú session-öknél
6. 📋 **Sub-agentek:** olcsóbb modellel futtatni ahol lehet

---

*Készítette: Leoni | 2026-02-17*
