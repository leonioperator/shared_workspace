# Modell összehasonlítás: GPT-4o vs Claude Opus + Lokális LLM lehetőségek

**Dátum:** 2026-02-15
**Kutató:** Leoni
**Kérte:** Tomi

---

## 1. GPT-4o vs Claude Opus — Agent-ként használva

### Tomi tapasztalata
- **GPT-4o:** nem dolgozik autonóm módon, folyamatos "kézenfogást" igényel
- **Claude Opus:** szinte szárnyal, önállóan végrehajtja a komplex feladatokat

### Mások tapasztalatai (internetes kutatás alapján)

**Igen, széles körben megerősített tapasztalat.** A közösség és a szakmai források is hasonló mintákat írnak le:

#### Claude Opus erősségei agent-ként
- **Hosszú autonóm futás:** Anthropic szerint az Opus 4 "órákig képes folyamatosan dolgozni, több ezer lépésen keresztül anélkül, hogy elveszítené a fókuszt"
- **Extended thinking + tool use:** A Claude 4 natívan képes tool-okat használni a gondolkodási folyamat közben (multi-step reasoning + action loop)
- **Kódolás:** SWE-bench Verified-en vezető teljesítmény, a fejlesztők konszenzusa szerint a Claude Sonnet 4 is megelőzi a GPT-4o-t kódolásban
- **Reddit (r/ClaudeAI):** Firmware mérnök tapasztalata szerint Claude Opus 4 és Sonnet 4 is megbízhatóbb agent-ként, mint GPT-4.1

#### GPT-4o gyengeségei agent-ként
- **Nincs natív tool-use loop:** A GPT-4o nem rendelkezik beépített iteratív tool-használati képességgel (plugin framework-ön kívül)
- **Rövidebb válaszok, kevesebb önállóság:** Hajlamos "kérdezni ahelyett, hogy csinálná" — ez pontosan az, amit Tomi tapasztalt
- **Benchmarkokon közel van, de practice-ben elmarad:** MMLU ~88.7% (GPT-4o) vs ~87.4% (Claude Opus 4) — szinte azonos, de az agentic viselkedésben nagy a különbség

#### Összefoglaló vélemény
| Szempont | GPT-4o | Claude Opus 4 |
|---|---|---|
| Autonóm munka | ⚠️ Gyenge | ✅ Kiváló |
| Tool calling / function calling | ✅ Jó (de nem iteratív) | ✅ Natív multi-step |
| Kódolás | Jó | Kiváló (SWE-bench leader) |
| Kreativitás / írás | Tömör, strukturált | Részletes, empatikus |
| Multimodális | ✅ Kép+hang+szöveg | ⚠️ Szöveg+kép (hang limitált) |
| Ár (API) | Olcsóbb | Drágább |
| Kontextus | 128K | 200K |

**Konklúzió:** Tomi tapasztalata nem egyedi — a Claude Opus egyértelműen jobb agent, különösen hosszú, önálló munkafolyamatokhoz.

---

## 2. Lokális (Self-hosted) LLM lehetőségek

### Követelmények
- ✅ Ingyenes / open-source
- ✅ Magyar nyelv támogatás
- ✅ Tool calling / function calling
- ✅ Futtatható: 8 CPU / 16GB RAM VPS (GPU NÉLKÜL!)

### ⚠️ Fontos korlátozás: GPU nélkül
A VPS-ünkön nincs GPU. Ez azt jelenti, hogy CPU-n kell futtatni a modelleket, ami:
- Lassú lesz (1-5 token/sec a modell méretétől függően)
- Max 7-8B paraméterű modellt érdemes futtatni
- Agent-ként való használat erősen korlátozott a válaszidő miatt

### Ajánlott modellek

#### 🥇 Qwen3-8B (LEGJOBB VÁLASZTÁS)
- **Méret:** ~5GB (Q4 kvantált)
- **Magyar:** ✅ 119 nyelv támogatás, beleértve a magyart
- **Tool calling:** ✅ Natív function calling, MCP támogatás
- **Kontextus:** 32K (natív), 131K (YaRN-nel)
- **Ollama:** `ollama run qwen3:8b`
- **RAM igény:** ~8-10GB
- **Értékelés:** A legjobb nyílt forráskódú modell ebben a méretben. Erős reasoning, jó magyar, natív tool calling.

#### 🥈 Qwen3-4B (könnyebb alternatíva)
- **Méret:** ~2.5GB (Q4)
- **Magyar:** ✅ Ugyanúgy 119 nyelv
- **Tool calling:** ✅ Natív
- **RAM igény:** ~5-6GB
- **Ollama:** `ollama run qwen3:4b`
- **Értékelés:** Ha a 8B túl lassú CPU-n, ez a kompromisszum. Gyengébb reasoning, de használható.

#### 🥉 Llama 3.1 8B-Instruct
- **Méret:** ~4.7GB (Q4)
- **Magyar:** ⚠️ Korlátozott (angol-centrikus, de van magyar tudása)
- **Tool calling:** ✅ Támogatott
- **RAM igény:** ~8GB
- **Ollama:** `ollama run llama3.1:8b`
- **Értékelés:** Jó function calling, de magyar nyelv gyengébb mint Qwen3.

#### 🏷️ OpenEuroLLM-Hungarian (speciális)
- **Elérhető Ollama-n:** `ollama run jobautomation/OpenEuroLLM-Hungarian`
- **Magyar:** ✅ Kifejezetten magyar nyelvre optimalizált
- **Tool calling:** ❌ Nem ismert natív support
- **Értékelés:** Magyar nyelvű válaszokra jó, de agent-ként nem alkalmas.

#### Mistral 7B-Instruct v0.3
- **Méret:** ~4GB (Q4)
- **Magyar:** ⚠️ Mérsékelt
- **Tool calling:** ✅ Jó support
- **RAM igény:** ~6-8GB
- **Értékelés:** Gyors, hatékony function calling, de magyar nyelv nem erőssége.

### Összehasonlító táblázat

| Modell | Méret (Q4) | Magyar | Tool calling | RAM | Agent képesség |
|---|---|---|---|---|---|
| **Qwen3-8B** | ~5GB | ✅ Jó | ✅ Natív | ~10GB | ⭐⭐⭐⭐ |
| Qwen3-4B | ~2.5GB | ✅ Jó | ✅ Natív | ~6GB | ⭐⭐⭐ |
| Llama 3.1 8B | ~4.7GB | ⚠️ Mérs. | ✅ Jó | ~8GB | ⭐⭐⭐⭐ |
| Mistral 7B | ~4GB | ⚠️ Mérs. | ✅ Jó | ~8GB | ⭐⭐⭐ |
| OpenEuroLLM-HU | ~? | ✅ Kiváló | ❌ Nincs | ~? | ⭐ |

---

## 3. Tech Setup terv

### Szoftver stack

```
Ollama (inference engine)
  └── Qwen3-8B (Q4_K_M kvantálás)
      └── OpenAI-kompatibilis API (localhost:11434)
```

### Telepítés lépései

```bash
# 1. Ollama telepítés
curl -fsSL https://ollama.ai/install.sh | sh

# 2. Modell letöltés
ollama pull qwen3:8b

# 3. Szerver indítás (automatikusan elindul)
ollama serve

# 4. Teszt
curl http://localhost:11434/api/chat -d '{
  "model": "qwen3:8b",
  "messages": [{"role": "user", "content": "Szia, hogy vagy?"}]
}'
```

### Hardver követelmények (minimum a VPS-ünkön)

| Erőforrás | Minimum | Ajánlott | VPS-ünk |
|---|---|---|---|
| CPU | 4 core | 8+ core | ✅ 8 core |
| RAM | 10GB szabad | 12GB+ szabad | ⚠️ 16GB összesen |
| Disk | 10GB | 20GB | ✅ Elég |
| GPU | Nem kell | CUDA GPU = 10x gyorsabb | ❌ Nincs |

### Várható teljesítmény (CPU-only, 8 core)

| Modell | Token/sec (becsült) | Válaszidő (100 token) |
|---|---|---|
| Qwen3-8B Q4 | ~2-4 t/s | ~25-50 sec |
| Qwen3-4B Q4 | ~5-10 t/s | ~10-20 sec |

### ⚠️ Realitás check

**CPU-only futtatás NEM alkalmas valós agent munkára.** A válaszidők túl hosszúak ahhoz, hogy hatékony iteratív tool calling-ot végezzen. Egy egyszerű agent loop, ami 5 tool call-t igényel, akár 5-10 percig is tarthat.

**Mire JÓ lokális LLM a mi VPS-ünkön:**
- 🟢 Egyszerű kérdés-válasz magyar nyelven
- 🟢 Szöveg összefoglalás, fordítás
- 🟢 Egyszeri function call (pl. időjárás lekérdezés)
- 🟢 Privacy-érzékeny feldolgozás (adat nem hagyja el a szervert)

**Mire NEM JÓ:**
- 🔴 Komplex, többlépéses agent workflow (mint amit Leoni csinál)
- 🔴 Valós idejű chat interakció
- 🔴 Kód generálás és iteratív javítás

---

## 4. Javaslatok Tominak

### Rövid táv (most)
✅ **Maradj a Claude Opus-nál agent munkára.** A kutatás egyértelműen megerősíti, hogy ez a legjobb választás autonóm agent-hez.

### Közép táv (ha kell lokális kiegészítés)
- Telepítsd az Ollama + Qwen3-8B-t **kiegészítő eszközként** (nem agent-ként):
  - Magyar nyelvű szövegfeldolgozás
  - Privacy-érzékeny feladatok
  - Offline fallback

### Hosszú táv (ha GPU-s VPS lesz)
- Egy RTX 3090 / 4090 (24GB VRAM) VPS-sel a Qwen3-8B 30-50 t/s lenne
- Akkor már agent-ként is használható lenne
- Havi költség: ~$50-100 GPU VPS

---

## 5. Költségbecslés

| Megoldás | Havi költség | Agent képesség |
|---|---|---|
| Claude Opus API (jelenlegi) | ~$50-200 (használattól függően) | ⭐⭐⭐⭐⭐ |
| Lokális Qwen3-8B (CPU VPS) | $0 (meglévő VPS) | ⭐⭐ |
| Lokális Qwen3-8B (GPU VPS) | ~$50-100 | ⭐⭐⭐⭐ |
| GPT-4o API | ~$30-100 | ⭐⭐⭐ |

---

*Kutatás lezárva: 2026-02-15 15:14 UTC*
*Következő lépés: Tomi döntése szükséges a lokális modell telepítéséről*
