# AI Model Kutatás: Agent Munkára Melyik a Legjobb?

*Készült: 2026-02-15 | Leoni kutatás Tomi számára*

---

## 1. GPT-4o vs Claude Opus -- Autonóm Agent Munkára

### A probléma
Tomi tapasztalata: GPT-4o agent módban **nem vesz iniciativát**, túl sok kérdést tesz fel, és passzívan várakozik utasításra. Claude Opus ezzel szemben önállóan dolgozik, döntéseket hoz, és végrehajtja a feladatokat.

### Miért jobb a Claude agent munkára?

**1. Tervezési filozófia különbség:**
- Az OpenAI modelljeit erősen "safety-first" megközelítéssel tanítják: inkább kérdezzen vissza, mint hogy hibázzon. Ez chatbot-nak jó, agent-nek katasztrofális.
- Az Anthropic Claude modelljeit úgy hangolták, hogy **kontextusból következtessen** és cselekedjen, ne pedig visszakérdezzen minden apróságnál.

**2. Instruction following vs. initiative:**
- GPT-4o hajlamos "clarification loop"-ba kerülni: "Would you like me to..." "Should I..." "Do you want me to..."
- Claude Opus/Sonnet a system prompt-ot mélyebben internalizálja, és aszerint cselekszik. Ha az agent keretrendszer (pl. OpenClaw) azt mondja "cselekedj önállóan", Claude tényleg azt teszi.

**3. Hosszabb kontextus, koherensebb viselkedés:**
- Claude Opus: 200K token kontextus, GPT-4o: 128K
- Agent munkánál a hosszabb kontextusablak = jobb feladat-emlékezet = kevesebb "elfelejtette mit kell csinálni" hiba

**4. Kódolás és tool use:**
- Claude modellek (Opus, Sonnet 4) kiemelkedőek tool calling-ban és strukturált output-ban
- A Reddit/fejlesztői közösség véleménye (2024-2025): Claude egyértelműen erősebb autonóm kódolási és agent feladatokban

### Közösségi tapasztalatok
- r/ClaudeAI, r/Anthropic: rengeteg poszt arról, hogy Claude "megérti mit akarsz" míg GPT-4o "robotikus és elavult"
- r/LocalLLaMA: agent keretrendszerek fejlesztői (SWE-bench, Devin-klónok) szinte kizárólag Claude-ot használják
- OpenClaw-szerű rendszereknél Claude Opus a de facto sztenderd

### Összefoglaló
| Szempont | GPT-4o | Claude Opus |
|---|---|---|
| Önálló cselekvés | ❌ Gyenge | ✅ Kiváló |
| Tool calling | Jó | Kiváló |
| Kontextus | 128K | 200K |
| Kódolás | Jó | Kiváló |
| Agent munkára | Nem ajánlott | Ajánlott |

---

## 2. Lokális/Nyílt Forráskódú Modellek Agent Munkára (2025-2026)

### Top modellek

| Modell | Méret | Licensz | Agent képesség | Magyar nyelv |
|---|---|---|---|---|
| **Qwen 3** (2507) | 0.6B - 235B | Apache 2.0 | ✅ Kiváló instruction following | ✅ Jó (multilingvális fókusz) |
| **DeepSeek V3/R1** | 8B - 671B | MIT | ✅ Erős reasoning | ⚠️ Közepes |
| **Llama 4** | 8B - 405B | Llama License | ✅ Jó | ⚠️ Közepes |
| **Mistral Large / Mixtral** | 7B - 123B | Apache 2.0 | Jó | ⚠️ Gyenge |
| **Phi-3/4 Mini** | 3.8B - 14B | MIT | Korlátozott | ❌ Gyenge |

### Agent munkára a legjobb nyílt modellek (2025 konszenzus):
1. **Qwen 3 (72B+)**: legjobb instruction following, multilingvális (magyar is!), tool calling támogatás
2. **DeepSeek R1**: erős reasoning, jó kódolás, de inkább gondolkodós feladatokra
3. **Llama 4 (70B+)**: általános célú, nagy közösség

### Magyar nyelvi képesség
- **Qwen modellek** a legjobbak multilingvális feladatokra (kifejezetten erre tervezték)
- DeepSeek és Llama is tud magyarul, de gyengébben
- 7-8B méretű modelleknél a magyar minőség **drámaian romlik**

---

## 3. Tech Setup -- Mit futtathatunk a mi VPS-ünkön?

### A mi VPS specifikációnk
- **8 vCPU, 16GB RAM, GPU NINCS**

### Realitás check

**GPU nélkül, CPU-only futtatás:**
- 7-8B modell (Q4 kvantált): **futtatható**, ~5-10 token/sec
- 14B modell (Q4): **éppen futtatható**, ~2-5 token/sec, lassú
- 32B+: **NEM futtatható** 16GB RAM-mal

**Ami reálisan megy a VPS-en:**

| Modell | Méret RAM-ban | Sebesség (CPU) | Használható? |
|---|---|---|---|
| Qwen 3 8B (Q4_K_M) | ~5GB | ~8 tok/s | ✅ Igen |
| DeepSeek-R1 8B (Q4) | ~5GB | ~7 tok/s | ✅ Igen |
| Llama 3.1 8B (Q4) | ~5GB | ~8 tok/s | ✅ Igen |
| Phi-3 Mini 3.8B (Q4) | ~2.5GB | ~15 tok/s | ✅ Gyors, de buta |
| Qwen 3 14B (Q4) | ~9GB | ~3 tok/s | ⚠️ Lassú |
| Bármi 32B+ | 20GB+ | - | ❌ Nem fér el |

**Fontos:** 5-10 tok/s CPU-n azt jelenti, hogy egy 500 tokenes válasz **50-100 másodperc**. Ez agent munkára **nagyon lassú**. Egy Claude Opus válasz ~2-5 másodperc.

### Szoftver stack
- **Ollama**: legegyszerűbb, `curl -fsSL https://ollama.ai/install.sh | sh` és `ollama pull qwen3:8b`
- **llama.cpp**: alacsonyabb szintű, több kontroll
- **vLLM**: GPU-ra optimalizált, CPU-n nem ajánlott

### Telepítés 1 perc alatt
```bash
# Ollama telepítés
curl -fsSL https://ollama.ai/install.sh | sh

# Modell letöltés
ollama pull qwen3:8b

# Teszt
ollama run qwen3:8b "Írj egy rövid magyar összefoglalót az AI trendekről."
```

---

## 4. Javaslat Tominak

### Rövid válasz
**Maradj a Claude Opus-nál az OpenClaw agent munkára.** A lokális modellek 2025-ben még nem érik el azt a szintet, ami autonóm agent munkához kell, különösen GPU nélkül.

### Részletes javaslat

**Fő agent (OpenClaw):** Claude Opus -- ez marad, működik, a legjobb erre a célra.

**Kísérletezésre érdemes (a VPS-en, Ollama-val):**
1. **Qwen 3 8B** -- kipróbálni egyszerűbb feladatokra (fordítás, összefoglalás, draft írás). Tud magyarul, gyors(abb) a kis modellek között.
2. **DeepSeek-R1 8B** -- ha reasoning/gondolkodós feladat van

**Mire JÓ a lokális modell (mellék-feladatok):**
- Gyors szövegfeldolgozás (nem kell API hívás)
- Draft generálás, amit Claude finomít
- Tesztelés, prototipizálás
- Offline működés

**Mire NEM jó (a mi setup-unkkal):**
- Autonóm agent munka (túl lassú, túl buta a 8B)
- Komplex kódolás
- Magyar nyelvű hosszú szövegírás (8B modellnél gyenge)

**Ha komolyabban akarod a lokálist:**
- Egy **GPU-s VPS** (pl. RTX 4090 24GB, ~$0.5/óra cloud-ban) már futtat 70B modelleket, ami közelíti a Claude minőségét
- Vagy: várj 2026 második felére, a nyílt modellek gyorsan fejlődnek

### Költség összehasonlítás
| Megoldás | Havi költség (becsült) | Minőség agent munkára |
|---|---|---|
| Claude Opus (OpenClaw) | ~$50-150 (token alapú) | ⭐⭐⭐⭐⭐ |
| GPU VPS + 70B modell | ~$100-300 | ⭐⭐⭐⭐ |
| Mi VPS-ünk + 8B modell | $0 (extra) | ⭐⭐ |

---

*Összefoglalva: Claude Opus marad a fő agent. Érdemes Ollama + Qwen 3 8B-t felrakni kísérletezésre, de ne várd, hogy kiváltja a Claude-ot. A nyílt modellek gyorsan fejlődnek, 2026 végére lehet, hogy már más a helyzet.*
