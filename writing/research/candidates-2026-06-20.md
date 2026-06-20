# Napi Jelöltek - 2026-06-20

## 🛠️ ESZKÖZÖK ÉS TECHNOLÓGIÁK

### Frontend & Design Tools
| Eszköz | Fókusz | Status | Megjegyzés |
|--------|--------|--------|-----------|
| **Efecto** | Design + Code under the hood | Beta | Ageansok számára - szerkeszthető canvas |
| **Figma Chrome Extension** | Website → Editable Figma | Release | Copy/paste weboldal → Figma layers |
| **drop.new (Vercel)** | Upload folder → Deploy | Release | Zip/file upload → Website/app deploy |
| **Firecrawl** | Web scraping + PDF → Markdown | Beta | Automated, API-free scale-ig |
| **UI Skills** | Design engineering skills | Free | Codex/Cursor/Claude Code agent skills |

### Coding & Development Agents
| Eszköz | Fókusz | Status | Megjegyzés |
|--------|--------|--------|-----------|
| **Cursor Composer 3** | 1.5T+ param. coding model | Announced | SpaceX, 10-20x compute, 2-3 hét |
| **OpenRouter Fusion API** | Multiple models + judge | Release | Multi-model inference optimization |
| **React Security Doctor** | Security vulnerability fix | Release | Auto-fix React exploits |
| **Extend CLI** | Document corpus parsing | Release | Agent document-parsing capability |

### Speech & Audio
| Eszköz | Fókusz | Status | Megjegyzés |
|--------|--------|--------|-----------|
| **Sonic-3.5** | Text to Speech | Release | Cartesia model |
| **Ink-2** | Speech to Text | Release | Cartesia model |

### AI Infrastructure
| Eszköz | Fókusz | Status | Megjegyzés |
|--------|--------|--------|-----------|
| **Castform** | Open-source model training | Release | Bring data, train öszesen, GPU abstraction |
| **Runpod** | AI Developer Cloud | Active | Cheaper AI infrastructure alternative |
| **CoreWeave** | MLPerf training records | Active | DeepSeek-V3 671B in 2 min (8192 GB300 GPUs) |
| **Baseten** | Lower-cost AI API | Active | $13B startup (alternative to OpenAI/Anthropic) |

### API & Model Services
| Eszköz | Fókusz | Status | Megjegyzés |
|--------|--------|--------|-----------|
| **Exa Agent** | Deep research API | Beta | Entity enrichment, structured output |
| **MDN MCP Server** | Browser compatibility data | Free | VS Code/Cursor/Claude Code integration |
| **Grok in PowerPoint** | Slides + diagrams gen | Release | Free Excel add-in, M365 required |
| **Framer 3.0** | Website builder with AI | Free | Branching experiments, analytics |
| **Skywork Design** | Website flow & page layouts | Subscription | Infinite canvas, prompt-based |

### Model & Training Services
| Eszköz | Fókusz | Status | Megjegyzés |
|--------|--------|--------|-----------|
| **Qwen Robot Suite (Alibaba)** | Robot navigation, manipulation, world prediction | Release | Physical world intelligence |
| **GLM-5.2 (Z.ai)** | 1M-token context, open-weights | Release | Strong long-horizon coding |
| **SubQ 1.1 Small** | 12M-token long-context | Technical report | 64.5x less compute vs dense attention |
| **PA-DR (ServiceNow)** | Privacy-preserving research agent | Academic | 34% → 9.9% information leakage |

---

## 📊 MODELL BENCHMARK

### Coding Performance (Ramp SWE-Bench)
| Modell | Pozíció | Költség | Megjegyzés |
|--------|---------|---------|-----------|
| **Fable 5** | 🥇 1. | ❌ Unavailable | 3 nap után lekapcsolva |
| **GPT-5.5** | 🥈 2. | 1.5x Opus vs Fable | Alternatív choice |
| **Opus 4.7** | 🥉 3. | 1x baseline | Opus szeries |
| **Opus 4.8** | 4. | ~1x | Költség-performance kompromisszum |

### Long-Context Performance (SubQ 1.1 Small)
- **12M token** retrieval without dense attention
- **64.5x less compute** than dense attention at 1M tokens
- **Near-perfect retrieval** up to 12M tokens

---

## 🎯 STRATÉGIAI JELÖLTEK

### 1. Cursor Composer 3
**Típus**: Coding model
**Miért fontos**: 
- SpaceX acquisition → Long-term stability
- 10-20x compute vs Composer 1
- Frontier-class intelligence (Claude Opus / GPT-5.5 szintén)
- 2-3 hét múlva elérhető
**Ajánlás**: Érdemes tesztelni, **szeptemberig nyomon követni**

### 2. OpenRouter Fusion API
**Típus**: Multi-model inference
**Miért fontos**:
- Judge model decides final answer
- Cost optimization (use cheaper models, expensive judge)
- Fable 5 alternatív stratégia
**Ajánlás**: Alternatív routing stratégiához tesztelni

### 3. GLM-5.2 (Z.ai)
**Típus**: Open-weights, long-context
**Miért fontos**:
- 1M token context (Qwen, Claude 3.5 szintje)
- Strong coding performance
- Open-weights → Local fine-tuning lehetőség
**Ajánlás**: Open-source alternatíva nyomon követni

### 4. Qwen Robot Suite (Alibaba)
**Típus**: Fizikai AI
**Miért fontos**:
- Navigation, manipulation, world prediction models
- Kínai infrastruktúra push (10,000+ robots 2026)
- Vertikális integrációs trend
**Ajánlás**: Robotika monitoring

### 5. Runpod + Castform
**Típus**: Infrastructure
**Miért fontos**:
- Cheaper alternative to Hyperscaler capex
- GPU abstraction (Castform)
- Open-source model training support
**Ajánlás**: Cost-conscious AI deployment stratégia

### 6. Firecrawl
**Típus**: Web scraping API
**Miért fontos**:
- API-free scale-ig (no key required)
- Markdown output
- PDF parsing
**Ajánlás**: Research automation tooling

### 7. Perplexity Brain
**Típus**: Agent memory system
**Miért fontos**:
- Persistent context graph
- Token reduction via better retrieval
- "Starting with relevant context" paradigma
**Ajánlás**: Long-running agent optimization

---

## ⚠️ ELKERÜLENDŐ / KORLÁTOK

| Eszköz/Modell | Probléma | Ajánlás |
|---------|---------|----------|
| **Claude Fable 5** | Szabályozási kikapcsolás | Alternatíva: GPT-5.5, Grok, Opus 4.7 |
| **Anthropic Mythos** | Select-only access | Nyilvánosságra hozatal várakozás |
| **Hyperscaler Capex** | Fenntarthatóság kérdés | Edge compute / open-source alternativák |
| **US-only models** | Geopolitikai limitáció | Nyitott modellekre váltás javaslott |

---

## 🚀 AZONNALI AKCIÓK

1. **Cursor Composer 3**: Regisztrálj a whitelist-re, 2-3 hét múlva tesztel
2. **OpenRouter Fusion**: Tesztelj multi-model routing stratégiákat
3. **GLM-5.2**: Nyilvánosság után tesztelj local fine-tuning-ot
4. **Firecrawl**: Integráld research automation workflow-ba
5. **Runpod/Castform**: Evaluate cost-effectiveness vs current vendor

---

**Prepared**: 2026-06-20 06:00 CET
**Source**: TLDR AI, The Neuron, Ben's Bites
**Next Review**: 2026-06-23 (vasárnap)
