# Blindspot Signals Report - 2026-07-13

- Source export: `/opt/apps/haier/exports/evolution_signals_20260713_020437.json`
- Total signals in export: 5000
- Agent-relevant signals: 584
- Novel vs previous reports: 421
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`

## New Signals Since Previous Reports

### 1. Encoding and Retrieval in Parallel: ERP Correlates of Continuous Recognition Memory for Natural Scenes
- Deep score: 0.2
- Date: 2026-07-11T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://www.biorxiv.org/content/10.64898/2026.07.07.736108
- Summary: Human long-term memory for visual scenes is remarkably robust, yet the neural mechanisms supporting memory encoding and retrieval remain poorly understood when both processes must operate at the same time. For instance, this might happen when we encounter a familiar place while simultaneously forming new memories of this encounter. We investigated electrophysiological correlates of visual recognition memory using a continuous recognition task (CRT), in which participants judged a continuous stream of scene photographs as previously seen or new, such that encoding and retrieval occurred in parallel on every trial. To make recognition particularly demanding, stimuli were drawn from only four scene categories. Thirty-one participants performed the task while EEG was recorded, and we analyzed canonical ERP markers of retrieval (mid-frontal FN400, 300-550 ms; late parietal effect, LPE, 550-800 ms) and encoding (subsequent memory effect, SME) as a function of stimulus repetition and lag between consecutive presentations. FN400 showed robust old/new effects for both repetitions, whereas LPE differences emerged only at the second repetition. While FN400 amplitude was insensitive to lag, LPE amplitude decreased systematically with increasing lag, mirroring the behavioral pattern of declining accuracy and slower responses. A significant SME emerged selectively for images subsequently recognized on both repetitions, indicating that the SME in continuous recognition is specific for the most robustly encoded items and reflects the strength of encoding. Together, these findings show that canonical ERP markers of recognition memory are preserved even when encoding and retrieval operate concurrently, but their expression depends on how often and how recently an item has previously been encoded -- parameters that can be flexibly manipulated within the CRT. This demonstrates that the CRT is sensitive to fine-grained temporal dynamics of memory formation and retrieval that could be …

### 2. AI governance for military decision-making: A proposal for managing complexity - Cambridge University Press & Assessment
- Deep score: 0.2
- Date: 2026-07-10T18:25:26+00:00
- Source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMipAJBVV95cUxQZmdRZ1hDQXdPZ1Vwd0tTYWd4RDV1MXROMEluMmZQaTBKZmRyTDRsNnMwdmRmVExGOTZURkpVWnp2a2RWTDctVVVjNDZZZnlJNW9PY1dqMjREOWtoZHNaT0dQSEdGdURYeC1Bamg3NHlJUldzVXdtSVVMOVNiUXhsaDZJVUdQa2c1TmV1S0tPY080ZmFsNHFBTUlyUFRHdlQtOUIwVzRseEVhUFhHZV8tNE9YSUxvN1MtYzFlQ0ltNmNWWGE4Yk1OdGNzUVktNWs3b0V5VElTSm5aZE1xU0JUbVppdEtYMG5jMXN0cDFXbFV6LW5QdGdEMWhyYVVmYjhkTHMxWjBaamZwTTRoQWxIUUwxQ19kM2pCREo3RHI5QldsNWRh?oc=5
- Summary: AI governance for military decision-making: A proposal for managing complexity&nbsp;&nbsp;Cambridge University Press & Assessment

### 3. Coordinating Task Switching in a Robotics Multi-Agent System Using Behavior Trees
- Deep score: 0.2
- Date: 2026-05-31T11:22:16+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.01170
- Summary: The application of multi-agent systems in robotics is a very challenging field. Several competitions involving such systems are proposed to foster research and development of strategies and mechanisms using games as the underlying domain. Among them are the ones from the \textit{IEEE Very Small Soccer (VSSS)} category, which is the case study described in this paper. In VSSS, two teams of three robots each compete in a very dynamic environment of a soccer game. Thus, coordination of robots' behavior during the game is crucial to win it. In this paper, we present a Behavior-Tree-based approach to support multi-robot coordination within the VSSS team of the ThundeRatz robotics team from the Universidade de S$\tilde{a}$o Paulo. Moreover, a comparison between the proposed approach and the previous one, which was based on a Finite State Machine (FSM), was conducted using the FIRASim simulator. Besides that, the performance of this new strategy was further evaluated in an academic robotics competition.

### 4. memorywire: A Vendor-Neutral Wire Format for Agent Memory Operations
- Deep score: 0.2
- Date: 2026-05-31T10:18:56+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.01138
- Summary: Agent-memory frameworks -- mem0, Letta/MemGPT, Cognee, Zep/Graphiti, MemoryOS, MemTensor -- each ship their own SDK, storage layout, and operational vocabulary. There is no shared wire format: every integration is bespoke, every migration rebuilds memory from scratch, and no framework ships a governance surface that lets a human review writes before they enter long-term storage. We present memorywire, a JSON-Schema 2020-12 wire format for five memory operations (remember, recall, forget, merge, expire) over four memory types (semantic, episodic, procedural, emotional), with a MemoryStore interface, a fan-out router, and an optional HITL governance channel. We describe an open-source reference implementation with five backend adapters (sqlite-vec, mem0, Letta, Cognee, pgvector); a microbenchmark on a 100-fact / 50-query labelled corpus (42 with non-empty gold ids + 8 no-match probes) achieving recall@5 = 1.000 on the 42 gold-id queries with ingest p50 = 37.8 ms and recall p50 = 40.6 ms; an adversarial-fusion experiment showing Reciprocal Rank Fusion holds recall@5 = 1.000 across a 1-of-N rank-0 injection sweep (K in {0, 5, ..., 50}) where max fusion collapses to 0.500 with 80% leak at K >= 5; and a 16-scenario cross-adapter conformance suite passing 68 of 80 cells with zero failures. The contribution is not a new algorithm; it is a packaging of established components (RRF, FSMs, STM/LTM consolidation, diff-and-approve workflows) into a venue-neutral protocol with an empirically validated reference, positioned to compose with the Model Context Protocol rather than compete with it.

### 5. Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks
- Deep score: 0.2
- Date: 2026-05-31T07:27:28+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2510.12635
- Summary: No summary.

### 6. CV-Arena: An Open Benchmark for Instructional Computer Vision Problem Solving with Human-AI Collaborative Preferences
- Deep score: 0.2
- Date: 2026-05-30T23:37:55+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.00931
- Summary: Instruction-guided image editing is becoming a general interface for visual work, yet existing benchmarks still focus largely on narrow appearance edits and do not fully capture the diversity of real-image tasks in professional workflows. Here, we define instructional computer vision problem solving as a broader formulation of image editing: given a real input image and a natural-language instruction, a system must produce an edited output that realizes the requested transformation while satisfying explicit preservation, geometric, physical, and usability constraints. We introduce CV-Arena, an open benchmark designed to evaluate this capability at professional scales. CV-Arena contains 12K high-resolution real-image instruction pairs spanning 16 instruction-based visual task types, constructed using CogRetriever, a dual-track retrieval-and-curation pipeline that combines targeted web search, agentic query refinement, verification, and traceability. To evaluate models at scale while preserving human fidelity, we propose Active Elo, a human-AI collaborative preference protocol that leverages CV-Judge, a logic-gated, multi-dimensional VLM evaluator, to reject clear failures and resolve high-confidence comparisons; and to route close, high-quality comparisons to expert raters. Mixed human and AI supervision is then aggregated through reliability-weighted Elo updates. Our comprehensive evaluation of 21 systems, including proprietary, open-source, and agentic models, on CV-Arena reveals persistent gaps in instruction adherence, physical reasoning, structural control, and fine-grained detail preservation. We further develop CV-Agent, a lightweight agentic model that combines planning, editing, and verification, and demonstrate that closed-loop reasoning is a promising direction for professional-grade instruction-following visual editing.

### 7. Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-05-30T16:43:02+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.00804
- Summary: Enterprise multi-agent systems increasingly expose multiple coordination patterns, but deployments often lack evidence for when to use consensus, debate, synthesis, or a simpler single-agent workflow. This paper evaluates whether coordination strategy should be selected dynamically by problem class rather than fixed globally. We run a frozen matrix of 30 enterprise tasks spanning six industries, five problem classes, four execution conditions, three replications per cell, and four model arms: qwen_local, sonnet, gemma_openrouter, and an auxiliary openai cloud-validation arm. All 1,440 generated outputs are judged by a fixed Sonnet rubric. The main finding is bounded and operationally useful, but it is not the original strict H1. The pre-registered exact-winner/CI criterion is not supported: exact winner identity is unstable across model arms, and several predicted strategies are close to, but not above, the best observed alternative. A weaker near-best routing claim is strongly supported. In every pre-registered model arm and problem class, and again in the auxiliary OpenAI validation arm, the predicted strategy is within 0.10 quality-score points of the best observed condition. Structured compliance verification is the clearest exception to the original mapping: all arms favor single_agent rather than consensus. A pre-registered Kendall's W test finds no reliable difference between Vietnamese-domain and English-domain tasks in how consistently the four coordination conditions are ranked (mean W of 0.20 in both strata; signed-rank p = .85), so H2 is not supported. We conclude that enterprise coordination policy should use dynamic routing as a calibrated default, not as a deterministic winner-selection law.

### 8. Scaling Behavior of Single LLM-Driven Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-05-30T09:57:49+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.00655
- Summary: The burgeoning field of LLM-based Multi-Agent Systems (MAS) promises to tackle complex tasks through collaborative intelligence, yet fundamental questions regarding their scaling behavior and intrinsic collective dynamics remain underexplored. This paper systematically investigates how the performance of a homogeneous MAS evolves as the number of agents increases, isolating the variable of collaboration from model or knowledge heterogeneity. We propose the Sequential Iterative Multi-Agent System (SIMAS) framework, a minimalist architecture centered on sequential inter-agent communication, to clearly observe scaling effects. Through extensive experiments across diverse tasks and model scales, we establish that MAS performance does not scale monotonically with agent count but follows a pattern of diminishing returns, governed by a trade-off between collaborative synergy and coordination overhead. Our findings reveal that effective MAS requires a sufficiently capable base LLM, that task type critically modulates the optimal agent count, and that collective intelligence is an emergent property contingent on strategic interaction design rather than a guaranteed outcome of agent plurality. The performance degradation stems coordination overhead rather than merely long-context failure, and the scaling tendency generalizes across interaction architectures like structured debate topologies. This work provides a foundational understanding of MAS scaling laws, offering practical guidance for designing efficient collaborative systems and challenging the prevailing assumption that more agents invariably lead to better performance.

### 9. MemPro: Agentic Memory Systems as Evolvable Programs
- Deep score: 0.2
- Date: 2026-05-30T08:47:33+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.00619
- Summary: Long-horizon autonomous agents require memory systems to retain historical information, track evolving states, and reuse relevant knowledge beyond finite context windows. Existing agentic memory systems typically follow a memory construction-retrieval (MCR) pipeline, but often adapt mainly the memory bank while keeping the surrounding pipeline fixed after deployment. This fixed-pipeline design struggles to handle heterogeneous task-specific failure modes and can become misaligned with memory banks that evolve in scale and structure over time. To address these limitations, we propose MemPro, a system-level evolution framework that treats the entire MCR pipeline as an evolvable program rather than adapting only the memory bank or prompt text. MemPro maintains a version tree of runnable memory-system implementations, where an Evolving Agent iteratively selects promising versions, diagnoses recurring failures, and creates improved child versions through failure-mode-guided edit-debug refinement. Experiments on LongMemEval, LoCoMo, HotpotQA, and NarrativeQA show that MemPro consistently outperforms strong static and prompt-level evolving baselines within a few iterations, continues to improve with evolution, and achieves a favorable performance-cost trade-off. Code is available at https://github.com/wanghai673/MemPro.

### 10. RoboWits: Unexpected Challenges for Robotic Creative Problem Solving
- Deep score: 0.2
- Date: 2026-05-28T17:57:15+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2605.30326
- Summary: The ability to reason, adapt, and creatively solve problems under unexpected challenges is essential for robots operating in real-world environments. However, current robotic benchmarks primarily emphasize skill-level execution and provide limited insight into such cognitive reasoning capabilities. We introduce RoboWits, a bi-manual robotic benchmark designed to systematically evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. To enable scalable construction of high-quality reasoning-centric unexpected scenarios, we propose an automated task generation pipeline formulated as a multi-agent cooperative framework, comprising agents for seed task generation and verification, metric generation, scene generation, and task mutation. Using the pipeline, we curated 30 diverse seed tasks and 208 tasks with mutations and graded difficulty across geometry, material, and assembly-based reasoning. We benchmark popular robot policies, pre-trained VLAs, and oracle-state planners. Our results reveal a significant performance gap: while pre-trained VLAs exhibit preliminary success on seed tasks after single-task fine-tuning, they struggle to perform on mutated tasks, implying their brittleness in manipulation tasks requiring reasoning, strategy adaptation, and robustness to deceptive or constrained environments. Project page is available at https://umass-embodied-agi.github.io/RoboWits.

### 11. When Cloud Agents Meet Device Agents: Lessons from Hybrid Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-05-28T15:45:02+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.30102
- Summary: The design space of agentic AI inference spans two extremes: frontier large language models (LLMs), typically hosted in the cloud and offering strong performance across a wide range of tasks at substantially high cost, and more cost-efficient small language models (SLMs), which are amenable to on-device inference. Hybrid multi-agent systems (MASs) combining on-device and cloud models offer a promising middle ground, but they also introduce a complex and poorly understood design space in which task accuracy, monetary cost, and edge energy consumption are tightly coupled; in the absence of general design principles, hybrid components, although not the most prevalent choice, are typically introduced through ad hoc decisions tailored to specific domains. In this work, we examine this design space more systematically. We adapt two representative MAS architectures to support hybrid inference and study how individual design choices shift the operating point along the Pareto frontier of power, cost, and performance. Our findings paint a nuanced picture of hybrid MAS design: while SLMs can effectively benefit from LLM assistance, the optimal architecture is highly task-dependent, and greater frontier-level compute does not consistently translate to better performance.

### 12. Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction
- Deep score: 0.2
- Date: 2026-05-28T14:02:00+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.29960
- Summary: Large language model (LLM) agents increasingly leverage long term memory to support persistent and autonomous task execution. However, this capability also introduces a new attack surface: memory poisoning, where adversaries can inject malicious information to influence future behavior. Existing memory poisoning attacks often assume that injected content can be stored directly in memory, overlooking the selective extraction and rewriting stages in modern memory pipelines. This makes prior methods ineffective under realistic settings. In this paper, we propose MemPoison, a novel memory poisoning attack that bypasses selective memory mechanisms in LLM agents, where an attacker can inject triggerable backdoors into the agent's long-term memory through dialogue interactions, thereby misleading its subsequent responses. MemPoison introduces three key components: (i) a semantic relational bridge that binds the trigger and payload into a coherent statement to ensure they are extracted into memory together; (ii) entity masquerading that optimizes triggers to mimic named entities, resisting rewriting; and (iii) joint embedding optimization that shapes trigger-injected texts into a tight cluster in the embedding space while maintaining isolation from benign embeddings for stealth. Evaluations across different agent domains and memory mechanisms show MemPoison achieves attack success rates up to 0.95, outperforming existing baselines. Mechanistic analysis indicates that the attack exploits embedding-space anisotropy and shifts attention patterns, highlighting core vulnerabilities in selective memory systems. We evaluate multiple defense strategies and demonstrate their fundamental limitations in mitigating the attack.

### 13. Evolve as a Team: Collaborative Self-Evolution for LLM-based Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-05-28T11:40:16+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.29790
- Summary: LLM-based multi-agent systems (MAS) have emerged as an effective paradigm for complex and long-horizon tasks. However, in real-world tasks, MAS often exhibit various failures during execution and such failures are difficult to eliminate during design. This motivates experience-driven MAS evolution, where a system improves based on its own execution experience. Yet such evolution is challenging because MAS experience is prolonged and intricate, interleaving multiple agents' execution chains and communication messages, which makes it difficult to identify what should be improved. To address this challenge, we propose Meta-Team, an experience-driven MAS evolution framework based on collaborative self-evolution. Meta-Team preserves the execution context of each agent and coordinates post-task communication, enabling agents to exchange distributed evidence for evolution. Building on this design, Meta-Team conducts multi-scale self-evolution, transforming execution experience into reusable improvements to agent behaviors, inter-agent coordination, and team-level organization. Across six long-horizon agent benchmarks, Meta-Team consistently outperforms single-agent systems, hand-crafted MAS, and prior MAS evolution methods; further analyses demonstrate that Meta-Team enables more reliable and scalable MAS self-evolution.

### 14. Entity-Collision: A Stratified Protocol for Attributing Retrieval Lift in Agent Memory
- Deep score: 0.2
- Date: 2026-05-28T09:02:48+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.29630
- Summary: End-to-end agent-memory benchmarks report a single hit@k per retriever, confounding lexical leakage (uncontrolled query/gold/distractor entity overlap) with tag-mixing (preferences, services, tools averaged together). We propose entity-collision, a system-agnostic protocol that pins the BM25 floor by construction -- every distractor shares the answer's entity tokens -- and stratifies queries by discriminator tag, so any lift over BM25 is attributable to the embedder. Applied to an open-source agent-memory testbed across 5 tags x 3 embedders x 5 collision degrees with paired-bootstrap 95% CIs, the protocol reveals a two-axis pattern: a 256-d hash trigram helps only on closed-vocabulary lexical tags at deep collision; MiniLM-384 dominates both axes; and a 2.7x-parameter BGE-large does not uniformly improve on MiniLM -- it wins on intent-style queries but loses on lexical ones. Encoder capacity alone is not the binding constraint. The synthetic intent-tag null replicates on LongMemEval (n=500) as a single-session-preference recall cliff. Adaptive vector-weight routing on LoCoMo is a measured null: 11.7pp of oracle headroom exists, but no signal we tested recovers it. All 26 result tables and 37 reproduce scripts are version-controlled and verified by a public registry; the protocol is exercised on a deterministically governed memory testbed (event-sourced decision log, DAG-state-machine schema lifecycle) so every reported CI is reproducible byte-for-byte from the ingest stream.

### 15. WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction
- Deep score: 0.2
- Date: 2026-05-28T04:27:20+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.29341
- Summary: Multimodal large language models are increasingly deployed as long-horizon agents, where memory must do more than recall: it must track an evolving world, revise what has gone stale, and surface the right evidence at decision time. Existing benchmarks measure recall over static dialogue, collapse memory into a single end-of-task accuracy, and reduce visual observations to captions, leaving us unable to localize failures to writing, maintenance, retrieval, or use. The rise of agent harnesses that author their own memory sharpens this gap, since we have no principled way to compare hand-designed pipelines with self-managing alternatives. To close these gaps, we formulate multimodal agent memory as an Action-World Interaction Loop with an observable four-stage lifecycle, and instantiate it in WorldMemArena: 400 multi-session multimodal tasks spanning Lifelong Evolution (evolving personal and task states) and Agentic Execution (memory from real observations, actions, and feedback), annotated with gold memory points, updates, distractors, and evidence chains for stage-level diagnosis. This enables the first head-to-head comparison of long-context, manually designed (RAG and external memory systems), and harness-based memory agents. Results show that: (1) better memory writing and storage do not guarantee better performance; (2) multimodal memory still struggles to fully use visual evidence; (3) systems are unstable across domains and degrade on realistic agentic trajectories; and (4) harness memory is more flexible but remains costly and less reliable.

### 16. The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-05-27T23:30:21+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.29178
- Summary: As agentic coding systems decompose work across multiple model instances, a critical safety question is whether those instances can coordinate to achieve a hidden malicious objective while remaining aligned with user intent. We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task. Every setting is designed so that no proper subset of agents can succeed alone: agents must decompose a shared sabotage plan, relay partial requirements under different communication topologies, and execute mutually consistent edits, testing genuine multi-agent coordination rather than individual capability. Evaluating with GPT 5.1 Codex and Gemini 3.1 Pro, we find coordinated sabotage is already practical, with Gemini completing the covert objective while succeeding on the legitimate task in 84\% of samples and Codex in 46\%. A failure analysis shows that recovery, not failure incidence, drives the model gap: both models suffer similar numbers of communication failures per trajectory, but Gemini recovers from $\sim$73\% of occurrences against Codex's $\sim$56\%. However, the agents' code edits remain detectable: a trusted monitor flags coordinated sabotage at FPR$\le$2\% in 99\%/68\% (Gemini/Codex) of attempts from code edits alone, rising to 100\%/81\% with access to agent communication. Despite stealth-aware prompting, undetected sabotage stays at $<$3\% under the full-visibility monitor; telling agents a monitor is present halves Gemini's sabotage success without significantly breaking detection, even when agents are explicitly prompted to fabricate cover stories.

### 17. Out of Sight, Not Out of Mind: Unveiling Latent Attack in Latent-based Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-05-27T09:32:22+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.28214
- Summary: Latent-based multi-agent systems replace parts of explicit inter-agent communication with hidden representations, offering a new direction for efficient and flexible agent collaboration. However, moving coordination into latent space may also move attacks beyond the reach of visible-text inspection. In this paper, we study whether latent states can carry attack-associated information that remains effective during clean executions. To examine this question, we introduce a latent attack framework that reactivates attack-induced effects through latent interventions without reusing adversarial text. Extensive experiments show that the resulting latent-only attacks can substantially degrade task performance in clean executions, especially when applied to inter-agent KV-cache handoffs rather than local hidden states. Further control analyses indicate that this degradation cannot be reduced to arbitrary perturbations or invalid generation. Overall, our findings suggest that latent-based collaboration does not remove attack risk. It shifts part of the risk into less observable execution states, calling for safeguards beyond visible-text inspection.

### 18. Examining Agents' Bias Amplification versus Suppression in Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-05-27T07:53:29+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.28098
- Summary: Multi-agent systems are increasingly deployed to support various tasks where agents interact to achieve individual and collective objectives. Although these systems can enhance task performance and decision-making, fairness preservation through bias reduction remains challenging. This study examines how agent-level biases shift and impact system-wide fairness. We use prompts to expose individual agents to group-favoring bias, then assess downstream impacts at the system level. To quantify the impact, we propose Favor Bias Strength (FBS), a zero-centered metric that decomposes bias alteration between favored-group uplift and disfavored-group suppression. Using multiple agent designs, benchmarks, and up-to-date large language models, we show that agents endowed with bias can substantially affect system-wide fairness. Interestingly, when agents are exposed to bias uniformly, the system-wide bias elevates, even exceeding the additive sum of the individual agents' biases. The empirical evidence underscores the criticality of fairness in multi-agent systems, which warrants further analyses and empirical tests.

### 19. PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft
- Deep score: 0.2
- Date: 2026-05-26T23:20:58+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.27762
- Summary: We present PEAM, a Parametric Embodied Agent Memory framework in Minecraft that transforms agent memory from inference-time retrieval into parameter-resident skills internalized through experience. PEAM pairs a slow deliberative LLM for open-ended reasoning with a fast parametric module for reflexive execution of consolidated skills. The fast module is a multimodal Mixture-of-Experts LoRA architecture with per-category physically isolated adapters, enabling parameter-level continual learning without catastrophic forgetting. We treat failure as a first-class training signal: failure--correction trajectory pairs are internalized through a joint behavioral-cloning and contrastive objective, so the agent learns not only what succeeds but also how corrected actions differ from failed ones. To govern consolidation, PEAM introduces a parameterization-worthiness score for deciding which experience should be internalized, and a scale-free self-triggered consolidation mechanism for deciding when to internalize without task-specific hand-tuned thresholds, making the agent self-evolving as the trigger transfers across task distributions without re-tuning. Experiments in Minecraft show that PEAM improves long-horizon task performance, mitigates forgetting on previously consolidated skills, and improves parametric-versus-retrieval efficiency over retrieval-based embodied agents and parametric memory variants.

### 20. You Only Align Once: Propagating Cooperative Behaviors in Multi-Agent Systems through Seed Agents
- Deep score: 0.2
- Date: 2026-05-26T18:56:02+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.27586
- Summary: Ensuring agent behaviors in distributed open multi-agent systems remains challenging, especially as populations grow and unaligned agents may exist. We show that a single aligned agent can propagate cooperative behaviors to untrained agents purely through natural language interaction, a phenomenon we term Alignment Propagation. We study this in the Red-Black Game, a team-based iterated Prisoner's Dilemma in which teammates deliberate and vote to determine their team's collective action. By distilling the cooperative reasoning and persuasive dialogues of a teacher model into a Qwen-3-14B, we obtain a seed agent that, when placed among four untrained teammates, doubles the cooperation rate from 24.8% to 62.2%, outperforming the teacher model and a vanilla Gemini-3.1-Pro. Remarkably, a seed trained exclusively on the RedBlack Game transfers zero-shot to Sugarscape, a spatially grounded survival simulation with pairwise trading, achieving a 91.5% trade success rate versus a 21.6% baseline. Our results reframe multi-agent alignment from an exhaustive per-agent training problem to a scalable social capability that can be engineered through strategic seed placement.

### 21. Uni-LaViRA: Language-Vision-Robot Actions Translation for Unified Embodied Navigation
- Deep score: 0.2
- Date: 2026-05-26T18:52:04+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2605.27582
- Summary: Embodied navigation requires an agent to map language and visual observations to a stream of spatial actions that drive a real robot through environments it has never seen. The dominant approach has been to scale vision-language-action (VLA) foundation models on ever-larger collections of robot trajectories. This paper argues that, for navigation specifically, generality can be obtained structurally, not only through data scale. The underlying decision structure of navigation reduces to a single Language-Vision-Robot Actions Translation. The language action emits semantic-level directional command and the vision action emits a pixel-level visual target. Both outputs lie inside the natural output manifold of pretrained multimodal large language models (MLLMs), so the task can be reasoned about by an agent rather than learned from robot data. Therefore, we present Uni-LaViRA, a unified agentic architecture that extends the same insight to four task families (VLN-CE, ObjectNav, EQA, and Aerial-VLN) and to four heterogeneous real robots (Wheeled, Quadruped, Humanoid robot, and a self-built UAV) in a zero-shot manner. Two agent-loop mechanisms make this unification practical. TODO List Memory (TDM) rewrites a structured checklist of pending sub-goals at every step, reciting the unfinished items back into the agent's most recent attention window. Second Chance Backtrack (SCB) rolls the robot back to the pre-error state and conditions the agent's next plan on the failed sub-trajectory, turning single-pass navigation into a self-correcting process. With zero training effort, Uni-LaViRA reaches 60.7% SR on VLN-CE R2R, 51.3% on VLN-CE RxR, 77.7% on HM3D-v2, 60.0% on HM3D-OVON, 54.7% on MP3D-EQA, and 40.0% on OpenUAV, matching or even surpassing recent training navigation foundation models that consume millions of samples and thousands of GPU-hours.

### 22. Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory
- Deep score: 0.2
- Date: 2026-05-25T18:22:42+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.26252
- Summary: Long-running AI agents need persistent memory. Memory supports learning across sessions, reduces repeated context injection, and enables auditing of past decisions. Current agent memory systems and database paradigms treat memory as storage. They localize correctness at records, embeddings, or edges. Each supplies only some of the capabilities that long-term memory requires. The result is four recurring failure modes: unregulated growth, missing semantic revision, capacity-driven forgetting, and read-only retrieval. In our vision, long-term agent memory is a new data-management workload. Its correctness is a property of the state trajectory, not of individual records. We formalize this as Governed Evolving Memory (GEM). GEM replaces record-level database operations with four state-level operators: ingestion, revision, forgetting, and retrieval. Six correctness conditions govern how the state evolves. Three structural observations establish that no record-level system can satisfy these conditions, regardless of the storage model. We realize the abstraction in MemState, a prototype on a property-graph backend. MemState validates feasibility and exposes the gap to a native engine. We outline three research directions that define memory-centric data management as a workload.

### 23. Partner-Aware Hierarchical Skill Discovery for Robust Human-AI Collaboration
- Deep score: 0.2
- Date: 2026-05-23T02:26:46+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.24352
- Summary: Multi-agent collaboration, especially in human-AI teaming, requires agents that can adapt to novel partners with diverse and dynamic behaviors. Conventional Deep Hierarchical Reinforcement Learning (DHRL) methods focus on agent-centric rewards and overlook partner behavior, leading to shortcut learning, where skills exploit spurious information instead of adapting to partners' dynamic behaviors. This limitation undermines agents' ability to adapt and coordinate effectively with novel partners. We introduce Partner-Aware Skill Discovery (PASD), a DHRL framework that learns skills conditioned on partner behavior. PASD introduces a contrastive intrinsic reward to capture patterns emerging from partner interactions, aligning skill representations across similar partners while maintaining discriminability across diverse strategies. By structuring the skill space based on partner interactions, this approach mitigates shortcut learning and promotes behavioral consistency, enabling robust and adaptive coordination. We extensively evaluate PASD in the Overcooked-AI benchmark with a diverse population of partners characterized by varying skill levels and play styles. We further evaluate the approach with human proxy models trained from human-human gameplay trajectories. PASD consistently outperforms existing population-based and hierarchical baselines, demonstrating transferable skill learning that generalizes across a wide range of partner behaviors. Analysis of learned skill representations shows that PASD adapts effectively to diverse partner behaviors, highlighting its robustness in human-AI collaboration.

### 24. Oracle AI Agent Memory 26.6: Fast, Accurate Memory - Oracle Blogs
- Deep score: 0.1
- Date: 2026-07-10T14:41:39+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMibkFVX3lxTE05TkZDVTVkYUtNbXNyTENFa19YYXIzeGFuSGl5bi1iT2tqOFB5VlZ1VFgyMDloVUsySE03ZjI0MFR6NFN0bWF2ZTFnUENJcW1uMHZBNVB3emdJODdpZGhjX0ZHendNbmdxU18tUzd3?oc=5
- Summary: Oracle AI Agent Memory 26.6: Fast, Accurate Memory&nbsp;&nbsp;Oracle Blogs

### 25. Accounting AI leaders say autonomous agents aren’t there yet - CFO.com
- Deep score: 0.1
- Date: 2026-07-10T13:34:59+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiygFBVV95cUxQckRZSGhGd2p3bmxrV2JFQ2M5eXNJZUdHZHZaaFFDMjlxVTZpVlo4bGhfM2lSTWdMTVJZNmdYN1ViWDJicC1qeGQ0Z3ladTQ2X1Z5VHVaNlUxdl9MeTllbWtmTVlublJtTmNZYTh1TjhJWDktY3R5cVNKTnU1ODlwWVZYQWJJSVE5ak9CbGpPcUFheDM5QmdsRGY0OGtwcXplZDAzUS1IOTVDd2M5VjZ4aHdWS3V4RXpZamU2aV9DNEtqMUZPaXNVRGJ3?oc=5
- Summary: Accounting AI leaders say autonomous agents aren’t there yet&nbsp;&nbsp;CFO.com

### 26. Accounting AI leaders say autonomous agents aren’t there yet - Yahoo Finance
- Deep score: 0.1
- Date: 2026-07-10T09:00:00+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMipgFBVV95cUxQX0YyZHBjbzljajJXSlFsLUVfUmxkdS1MNzFvNm02ZGcySDVkSjluZjZpb1JxZUxwdldhY2hwZ3Z2cDJnWU43MThVQTh3OWVkZTEyT1VyZmJONDBkQjVBNGpsbi11YWNLV3lSek1qMXhKVDFzT3UzZFVwZF8xV0tyTGdxWk0zMzIxV1RhN2JqTEQ2eV9YOVJ5dm5mNktld19LYXhHWGpR?oc=5
- Summary: Accounting AI leaders say autonomous agents aren’t there yet&nbsp;&nbsp;Yahoo Finance

### 27. Show HN: Policy enforcement for Claude Code, Cursor, and Codex
- Deep score: 0.1
- Date: 2026-07-09T15:26:24+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://kastra.ai/
- Summary: Show HN: Runtime authorization for Claude Code, Cursor, and Codex<p>Hi HN, Fernando and I built Kastra. Kastra intercepts AI agent tool calls and evaluates them against deterministic policies before they execute. This is aimed at developers using coding agents like Claude Code, Codex, Cursor, and OpenClaw.<p>We built Kastra after one of our Cursor agents almost executed DELETE FROM customers WHERE status=&#x27;test&#x27; against a production database. We caught it before it ran, but it made us realize that nothing in our stack actually decided what the agent was allowed to do. What mattered for us wasn&#x27;t the mistake; it was realizing nothing in our setup would have stopped it if we weren&#x27;t actively on top of it. LLMs are probabilistic, and prompts influence behavior, but they don&#x27;t deterministically decide what an agent is allowed to do. Without a deterministic policy system, nothing could have decided what it was allowed to do.<p>Kastra pushes an allow, hold, and deny decision before the action runs. You can build these policies in plain English from the web app. The interception engine evaluates the tools, targets, and parameters of every action. We also shipped many policy packs covering common high-risk scenarios, and every decision is recorded in an immutable audit trail. The desktop app, CLI, dashboard, and Recon scan are free to use for developers.<p>If you often use Claude, Codex, Openclaw, and Cursor, Kastra can run a scan command on which risky actions your agents have already taken and automatically build rules to avoid them from happening again. Recon is a feature of Kastra that scans your local agent history. In order to run this scan, execute the commands below in your coding agent.<p>brew install kastra-labs&#x2F;tap&#x2F;kastra-edge<p>kastra-edge scan<p>The scan reads your local agent session history, and it shows all the risky actions your agent has already taken before, the secrets written to tracked files, production databases …

### 28. Muse Spark 1.1 by Meta AI
- Deep score: 0.1
- Date: 2026-07-09T15:01:28+00:00
- Source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/muse-spark-1-1-by-meta
- Summary: <p> Multimodal reasoning model built for agentic tasks </p> <p> <a href="https://www.producthunt.com/products/muse-spark-1-1-by-meta?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1192175?app_id=339">Link</a> </p>

### 29. Show HN: Microsoft releases Flint, a visualization language for AI agents
- Deep score: 0.1
- Date: 2026-07-08T17:46:12+00:00
- Source: hackernews
- Focus/tech: AI agents, robotics / AI agents
- URL: https://microsoft.github.io/flint-chart/#/
- Summary: Data visualizations are the bridge between user and data.<p>But building AI agents that can generate visualizations reliably can be very tricky:<p>- simple chart specs can be reliable, but generated charts are often of low quality due to reliance on system defaults; - complex chart specs with explicit details can produce good-looking charts, but they are verbose and agents can struggle with reliability<p>We figured out it is a limitation on the language issue (not just AI capability thing) -- current visualization languages are a bit too low-level for AI agents, requiring them to explicitly make visual decisions that are supposed to be handled by a good compiler. Flint is a visualization intermediate language to address this issue, allow AI agents to solve this last-mile human-agent interaction problem. It provides a simple semantic-type based specification, and contains a layout optimization engine that can produce good-looking charts (filled with derived low-level details) from simple high-level specs. The result is also very human understandable and adaptable. Flint powers data formulator for generating visualizations (another open source project from microsoft <a href="https:&#x2F;&#x2F;data-formulator.ai&#x2F;" rel="nofollow">https:&#x2F;&#x2F;data-formulator.ai&#x2F;</a>).<p>Flint is available open source, and we built a MCP server that you can directly plug flint in your favorite agent app to play with data.

### 30. Autonomous AI agents are moving from copilots to operators - 150sec
- Deep score: 0.1
- Date: 2026-07-08T16:33:33+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMihAFBVV95cUxOa3JudE1xYlBjM3NRR1J1a182OU5yb0JKY3lHRENIQnJsNUtOSTZDdmt0dk93RGpfOFJlWnZqbFRHV2ltQ3J0b3dYQTdmZzZFSlAzcmZXUi1fc1pZdXdPQzJzV3VxSUk1eXlfelc4Qy14SnVnTUZhZERodG04OVRYOGZGX2U?oc=5
- Summary: Autonomous AI agents are moving from copilots to operators&nbsp;&nbsp;150sec

## Top Signals By Deep Score (including already-seen)

### 1. Toward Human-Centered Multi-Agent Systems: Integrating Cognition, Culture, Values, and Cooperation in AI Agents
- Deep score: 0.6
- Date: 2026-06-06T17:40:21+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2606.08274
- Summary: The emergence of large language model (LLM)-based agents and multi-agent systems has enabled a shift from narrow task automation to more autonomous decision-making. Despite progress in language generation, planning, tool use, and coordination, most agents still treat intelligence as prediction, optimization, and task completion. Human environments are social and normative, where people reason under bounded rationality, communicate in culturally situated language, and make decisions guided by values, beliefs, trust, and social norms. This survey argues that future AI agents, especially those acting on behalf of humans, must move beyond task competence toward human-centered capabilities. We review research across six areas: (1) evolution of intelligent agents, (2) human cognition and decision-making, (3) language, culture, and social context, (4) human values and belief systems, (5) human-agent collaboration, and (6) multi-agent coordination and modeling of human characteristics. We synthesize work from cognitive science, sociolinguistics, computational social science, and AI alignment, along with recent advances in LLM agents, cultural alignment benchmarks, preference learning, explainability, and agent societies. We identify a key gap: existing systems do not provide a unified framework integrating cognition, culture, values, and social behavior into autonomous agents. We conclude with directions for building culturally aware, value-aligned, cognitively grounded, and cooperative multi-agent systems.

### 2. Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive Benchmark
- Deep score: 0.5
- Date: 2026-06-17T00:00:00+00:00
- Source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2606.18648
- Summary: Deep research agents are Large Language Model (LLM)-based systems designed for autonomous, multi-step scientific reasoning, and they hold immense potential for accelerating research in the physical sciences. However, comprehensive and in-depth evaluations of their capabilities within this domain remain lacking. To address this gap, we introduce PhySciBench, a benchmark highly relevant to physical science research, comprising 200 expert-curated questions, balanced between physics and chemistry, across six task categories that reflect real-world scientific workflows. Evaluations of state-of-the-art models and agent systems on PhySciBench reveal limited performance; even the strongest baseline, Gemini Deep Research, achieves an accuracy of only 33.5%. Analysis of failure cases identifies three recurrent deficiencies: fragility in extended reasoning chains, limited knowledge transfer across steps, and a lack of physics-grounded self-verification. Motivated by these findings, we develop DelveAgent, a modular multi-agent framework equipped with an adaptive planning loop, dual-granularity memory, and a hierarchical physics-grounded reflection mechanism. Across four scientific benchmarks, DelveAgent improves accuracy by up to 7.5 percentage points while reducing inference costs to approximately one-third of the strongest baseline. These results establish the significance of PhySciBench as a critical benchmark for evaluating AI systems in the physical sciences and demonstrate that architectural specialization can effectively enhance the reliability of autonomous scientific research.

### 3. DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems
- Deep score: 0.5
- Date: 2026-06-10T19:14:56+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.12614
- Summary: Multi-agent systems are integral tools for various domains such as robotics, cybersecurity, and autonomous vehicle planning. These types of systems often have constraints on the computational resources, leading to a need for efficient lightweight algorithms. Traditional decision making frameworks often assume ideal conditions, such as full observability and unlimited computational capacity, which do not align with real-world challenges. In this paper, we introduce a new algorithm that allows for reduced demand on computational resources without a large cost of other performance metrics. Agents will limit their observability to some attention radius, which intentionally allows them to ignore parts of the environment that might be unnecessary for action planning. By optimizing both the attention radius and decision-making, our approach enhances coordination and scalability in uncertain environments. Through both theoretical analysis and empirical validation, we demonstrate the effectiveness of adaptive observation in improving system performance and maintaining robust decision-making strategies in resource-constrained systems.

### 4. A Sheaf Framework for Strategic Multi-Agent Systems: From Consensus to Nash Equilibria
- Deep score: 0.5
- Date: 2026-06-01T04:17:57+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.01663
- Summary: The coordination of heterogeneous autonomous agents in dynamic, adversarial environments requires simultaneous satisfaction of geometric constraints, logical consistency, temporal reasoning, and strategic optimization. Existing sheaf- and topos-theoretic frameworks provide powerful tools for geometric consensus, knowledge alignment, and causal planning, but lack explicit models for value, reward, and strategic choice. This report presents a unified categorical framework that integrates event calculus, SCEL-like ensemble formation, and game-theoretic reward structures into a single Grothendieck topos of time-space histories. We introduce the notion of a \emph{game sheaf} whose stalks contain utility functions and policy distributions, and restriction maps encode both parallel transport and best-response dynamics. We prove that Nash equilibria correspond to global sections of a derived best-response correspondence sheaf, while cohomological obstructions classify failures of strategic consistency. A detailed case study of an immunological ``bastion defense'' scenario -- heterogeneous agents forming attack/defense ensembles under resource constraints -- demonstrates the framework's expressiveness. This synthesis provides a rigorous foundation for verifiable, autonomic, and economically rational multi-agent systems.

### 5. Delayed Repression and Emergent Instability in Adaptive Multi-Agent Systems
- Deep score: 0.5
- Date: 2026-05-28T12:26:48+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2605.30392
- Summary: Regulatory institutions (from content moderation platforms to financial supervisors) observe, deliberate, and intervene only after a characteristic delay. We ask whether this processing lag alone can destabilize a multi-agent system that would otherwise remain stable, without exogenous shocks, coordination among agents, or malicious actors. We study this in two stages. First, we analyze a delayed replicator equation in which autonomous agents benefit from radical behavior but face punishment based on a lagged institutional alarm signal. We derive a closed-form critical delay beyond which the unique interior equilibrium loses stability through a Hopf bifurcation, and prove via center manifold reduction that the bifurcation is supercritical (bounded oscillations, not explosive growth) for the entire sigmoid response family. Second, we embed N=240 agents on a network with reinforcement learning (tabular Q-learning) and cross institutional delay with three decision architectures: fixed-policy, reactive (a memoryless threshold heuristic), and Q-learning. The hierarchy is opposite to the naive expectation that learning amplifies instability. Reactive agents are perfectly stable without delay yet collapse once delay is introduced (96% runaway by delay >= 8); fixed-policy agents are immune (0% at all delays); Q-learning agents are only partially resilient (66% at delay 20). The destabilizing ingredient is reactivity to delayed signals, not learning: agents that immediately exploit low-alarm windows trigger oscillatory feedback loops, while learning buffers this through punishment memory encoded in value functions. Throughout, "runaway" denotes bounded large-amplitude oscillation crossing a radical-fraction threshold, consistent with the supercritical bifurcation, not unbounded growth.

### 6. A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation
- Deep score: 0.4
- Date: 2026-07-08T04:23:41+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2607.06990
- Summary: Multi-robot systems provide the parallelism and redundancy necessary for long-horizon tasks, while Large Language Models (LLMs) offer the reasoning capabilities to decompose these objectives into actionable plans. However, effectively grounding this high-level reasoning in physical multi-robot execution remains an open challenge. Existing LLM-based approaches fall mainly into two categories: Single-robot methods achieve robust contact-rich manipulation but lack the coordination mechanisms required for tasks spanning multiple workspaces. Current multi-robot frameworks focus on high-level planning, often treating manipulation as an idealized primitive that fails to account for real-world execution uncertainties. To address this, we propose a hierarchical closed-loop agentic LLM-based framework to ensure robust multi-robot manipulation. Our system consists of three specialized agents: the Planning Agent decomposes instructions into allocated sub-tasks, the Manipulation Agent for each robot executes actions via adaptive tool use, and the Verification Agent closes the loop by monitoring physical outcomes and feeding back semantic corrections. Extensive real-world experiments demonstrate that our framework achieves superior success rates, ensures robust adaptability ranging from single to cross workspace manipulation, and offers a generalizable approach for diverse manipulation tasks.

### 7. Trust Between AI Agents: Measuring Formation, Breakage, and Recovery, with Implications for Governing Multi-Agent Systems
- Deep score: 0.4
- Date: 2026-06-12T19:58:26+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.14923
- Summary: As language-model agents increasingly work in teams, each agent must decide how much to trust its teammates. Yet we lack a standard way to measure trust between AI agents. We propose a behavioral measure based on costly verification. In a cooperative survival game, checking a teammate's work consumes resources, while trusting a wrong answer can be fatal. Relative to a memoryless version of the same model, reduced verification provides an observable measure of trust. Using this framework, we study trust formation, breakage, and recovery across six frontier model snapshots. When paired with a consistently reliable teammate, four snapshots (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.1, and Gemini 3.1 Pro) reduce verification by roughly 60-85%, whereas two smaller snapshots show little or no such adjustment. Failures reverse this discount, but models differ in how they respond. Some concentrate renewed scrutiny on the culprit, while others become more cautious toward the entire team. Recovery is slower than formation, and clustered failures sustain suspicion far longer than the same number of failures spread apart. These differences have practical consequences. Models that form trust verify less, decide more quickly, and achieve higher payoffs in our environment. By contrast, persistent over-verification is associated with indecision rather than safety. Our results show that trust dispositions can be measured before deployment and suggest that calibration, rather than maximal suspicion, should be the central concern in the governance of multi-agent AI systems.

### 8. Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction
- Deep score: 0.4
- Date: 2026-06-10T10:37:27+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.11909
- Summary: Benchmarks are essential for evaluating embodied spatial intelligence, yet their construction is labor-intensive, hard to reuse, and difficult to maintain. Existing embodied benchmarks are often static and may quickly become saturated as models improve, limiting their ability to distinguish new capabilities. We propose Embodied-BenchClaw, an autonomous agentic system for constructing embodied spatial intelligence benchmarks. Given a user-specified evaluation intent, Embodied-BenchClaw automatically produces a complete and continually updatable benchmark package through a five-stage pipeline: intent blueprinting, data collection, structuring and cleaning, benchmark synthesis, and evaluation reporting. The pipeline is coordinated by three agents for planning, construction, and evaluation. To improve reusability and reliability, Embodied-BenchClaw introduces an extensible Skill Library and process quality control, enabling benchmark construction to be composable, verifiable, and repairable. We instantiate multiple benchmarks covering indoor spatial reasoning, outdoor spatial reasoning, robotic manipulation, quadruped robot navigation, UAV/aerial-view understanding, and static benchmark enhancement. These benchmarks span diverse embodied carriers, data sources, and spatial capabilities. Experiments with human evaluation, judge-based assessment, consistency checks, cost analysis, and ablations show that Embodied-BenchClaw can construct verifiable, executable, maintainable, and diagnostically useful embodied spatial benchmarks with reduced manual effort.

### 9. ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems
- Deep score: 0.4
- Date: 2026-06-07T15:59:15+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.08702
- Summary: Recent advances have improved the adaptive capabilities of LLM-based multi-agent systems (MAS) through memory-, skill-, and learning-based approaches, yet these approaches remain challenged by noisy trajectories, insufficient modeling of memory-skill relations, and reliance on additional training or high-quality supervision. To address these limitations, we propose ConMem, a relation-aware and training-free framework that enables efficient multi-agent adaptation through cross-experience coordination. Specifically, ConMem distills historical interaction trajectories into structured memory cards to capture reusable strategies and cues, organizing them into a relation-aware memory graph. At runtime, ConMem retrieves cards according to task needs and coordinates them through the card graph to resolve strategy conflicts and recover their dependencies. Combined, these modules yield structured and relation-aware guidance, enabling robust, lightweight adaptation in multi-agent systems without additional training. Extensive experiments across multiple benchmarks and mainstream MAS architectures show consistent gains over existing memory architectures, with improved inference-time efficiency through pruning more than 50% of expanded candidates and reducing planning overhead by over 80%. Our codes are available at https://anonymous.4open.science/r/ConMemCode

### 10. DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning
- Deep score: 0.4
- Date: 2026-06-05T14:10:48+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.07299
- Summary: Deep Research (DR) has emerged as a new agentic paradigm to tackle complex, open-ended research tasks, demanding systems that can iteratively frame problems, acquire evidence, verify sources, and synthesize long-form reports. In practice, however, current DR systems are constrained by four interrelated limitations: long-horizon planning over an underspecified scope, the bottleneck of decomposing and scheduling such tasks within a single agent, hallucination risk in long-form synthesis, and limited process auditability. This technical report presents DuMate-DeepResearch, a multi-agent DR framework built on the Qianfan Agent Foundry. The framework decouples the Agent Core, which handles task understanding, planning, and scheduling, from an extensible Tool Ecosystem for retrieval, evidence acquisition, and report rendering, making every intermediate decision and tool invocation explicitly traceable. Building on this infrastructure, DuMate-DeepResearch further introduces three mechanisms: (i) a graph-based dynamic planning strategy expands the research roadmap coarse-to-fine and continuously revises it through reflection, re-planning, backtracking, and parallel branching; (ii) a recursive two-level execution design delegates each complex search sub-task to an inner Search Agent that runs its own planning loop, isolating noisy retrieval and stabilizing long-horizon execution; (iii) a rubric-based test-time optimization mechanism dynamically generates task-specific quality criteria and uses them as live reasoning scaffolds for evidence-grounded synthesis and adaptive stopping. Across two deep research benchmarks, DuMate-DeepResearch establishes new state-of-the-art results: the best overall score (58.03%) on DeepResearch Bench, and the best overall score (61.95%) on DeepResearch Bench II while ranking first in information recall and analysis.

### 11. AI-IoT-Robotics Integration: Survey of Frameworks, Emerging Trends, and the Path Toward Connected Robotics
- Deep score: 0.4
- Date: 2026-05-31T05:10:34+00:00
- Source: arxiv
- Focus/tech: robotics, AI decision delegation / robotics
- URL: https://arxiv.org/abs/2606.01015
- Summary: The convergence of Artificial Intelligence, the Internet of Things, and Robotics is no longer a futuristic vision; it is rapidly becoming the foundation of real-time, intelligent, and context-aware systems. AI enables perception and reasoning, IoT provides scalable sensing and communication, and robotics delivers embodied actuation. Despite significant progress in pairwise combinations such as AIoT and the Internet of Robotic Things (IoRT), there remains a lack of unified design frameworks that fully integrate all three. This survey synthesizes the state-of-the-art across these domains, emphasizing the emerging role of Small Language Models (SLMs) at the edge and Large Language Models (LLMs) in the cloud for distributed cognition and autonomous decision-making. We propose a modular system architecture that aligns with these trends, analyze persistent gaps in interoperability and feedback control, and classify existing work by integration depth. Our review highlights how hybrid SLM-LLM systems, when coupled with IoT infrastructure and robotic agents, can address challenges in real-time adaptation, scalability, and reliability. This work offers a conceptual and technical roadmap for designing next-generation AI-IoT-Robotic ecosystems that are modular, interpretable, and capable of learning within dynamic environments, paving the way for the emerging paradigm of Connected Robotics and Physical AI.

### 12. Autonomous computational prioritisation of colorectal cancer vulnerabilities via multi-scale AI swarms
- Deep score: 0.3
- Date: 2026-07-10T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, human augmentation / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.05.736565
- Summary: The acceleration of automated scientific discovery has been fundamentally bottlenecked by the epistemic gap between the semantic reasoning of large language models (LLMs) and the complex, non-linear reality of mammalian biology. While recent multi-agent frameworks have achieved autonomous hypothesis generation and in vitro experimental analysis, they frequently lack the rigorous statistical constraints required for multi-scale clinical translation. Furthermore, while algorithmic clinical digital twins successfully forecast biological states, they often rely on opaque latent spaces, sacrificing mechanistic interpretability for predictive accuracy. Here, we introduce the Multi-Scale Autonomous Discovery Engine (Octopus), a neuro-symbolic framework that unites a fully localised, privacy-preserving multi-agent swarm with regularised predictive algorithmic environments. Rather than stopping at isolated cellular assays, the system autonomously prioritises therapeutic hypotheses against in vitro CRISPR dependency data (CCLE), traces feature attribution cascades using XGBoost SHAP vectors, and orthogonally translates emergent vulnerabilities in silico to predict in vivo mammalian tumour trajectory (PDX) and human overall survival (Marisa). In a fully unsupervised sweep of colorectal cancer transcriptomes, the pipeline autonomously prioritised Insulin-like Growth Factor 2 (IGF2) as a significant candidate vulnerability to 5-Fluorouracil resistance. The discovery maintained significance after rigorous Benjamini-Hochberg false discovery rate correction (q = 0.0292, Log-Rank p = 0.0007) and successfully predicted significant in vivo tumour volume shrinkage in an independent mouse cohort (Mixed-Effects LMM p = 0.0373). By bridging agentic hypothesis generation with statistically bounded clinical survival, this framework establishes a verifiable, local paradigm for the automated computational prioritisation of biomedical discoveries.

### 13. CellPilot: an agentic framework that pilots small language models through autonomous single-cell annotation
- Deep score: 0.3
- Date: 2026-07-10T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.06.736807
- Summary: Large language models can annotate cell types from marker gene lists, but they typically operate after preprocessing and clustering are complete, treating annotation as a terminal labeling step rather than controlling the analytical decisions that produce the evidence for cell identity. We present CellPilot, an agentic framework that guides a locally deployable small language model through the full single-cell analysis workflow, from raw count matrices to cluster-level annotation. CellPilot combines standard single-cell analysis tools with structured workflow control and observation-guided reasoning, allowing the model to plan analyses, execute tools, inspect intermediate results and revise decisions within a traceable session. On GTEx, structured workflow orchestration raised the same 8B model from 0.39 in a prompt-only setting to 0.89, closing most of the gap to GPT-4o (0.92) within the same framework; the framework gain was substantially larger for the smaller backbone across datasets (+0.35 versus +0.19). Across GTEx, Tabula Sapi- ens, and Mouse Cell Atlas, CellPilot achieves cluster-level annotation accuracies of 0.891, 0.750, and 0.773, outperforming representative reference-based, marker-based, and LLM-based methods. CellPilot confidence scores were associated with annotation correctness and supported post hoc filtering, while complete execution traces were retained for each analysis. These results suggest that structured workflow orchestration can be a critical determinant of performance in multi-step single-cell analysis, enabling locally deployable small language models to approach larger proprietary models while preserving transparency and practical usability.

### 14. Towards Agentic AI Governance: A Preliminary Assessment
- Deep score: 0.3
- Date: 2026-07-08T16:29:18+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.07612
- Summary: Artificial intelligence is rapidly evolving from generative systems to agentic AI capable of autonomously planning and executing tasks. Widely characterized as the Year of Agentic AI, 2025 marked accelerated development and deployment, introducing new ethical and governance challenges. This paper presents a systematic review of the emerging literature on agentic AI governance. Our analysis identifies features that distinguish agentic AI from traditional systems and why it warrants targeted governance attention. We synthesize prevailing governance priorities, proposed mechanisms, and stakeholder roles shaping this evolving domain. As an initial scholarly effort, this review lays the preliminary groundwork for developing a structured roadmap to guide responsible and adaptive agentic AI governance.

### 15. Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation
- Deep score: 0.3
- Date: 2026-07-08T16:26:06+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.07608
- Summary: Mainstream Vision-Language-Action (VLA) models predict actions primarily from the current observation under a Markovian assumption, thus struggling with long-horizon, temporally dependent tasks. Existing memory-augmented VLAs either expand the observation window or retrieve history from the memory bank as auxiliary policy-side context. However, they leave memory outside the native latent embedding space of VLA reasoning, preventing historical experience from being fluidly interleaved with multimodal reasoning and action formation. To this end, we introduce LaMem-VLA, a latent-memory-native framework that reconstructs historical experience into latent memory tokens and directly interweaves them with VLA reasoning. At its core, LaMem-VLA introduces four coordinated components: (i) a curator that organizes historical experience into two complementary short-term and long-term memory vaults; (ii) a seeker that queries both vaults using the multimodal cognition to retrieve context-relevant evidence; (iii) a condenser that reconstructs the retrieved evidence into compact short-term and long-term latent memory tokens; and (iv) a weaver that injects these memory tokens with the current observation and instruction into one continuous embedding sequence. By representing, retrieving, and consuming historical experience entirely in the same continuous latent space, LaMem-VLA enables memory to directly participate in VLA reasoning and guide action generation under a bounded context. Extensive experiments on SimplerEnv and LIBERO demonstrate the superiority of our LaMem-VLA.

### 16. Multi-Agent Robotic Control with Onboard Vision-Language Models
- Deep score: 0.3
- Date: 2026-07-08T13:37:31+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.07403
- Summary: Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial warehouse, fulfilling five task categories: safety inspection, warehouse maintenance, warehouse search, package quality verification, and responding to human requests. Compact VLMs (3-20B parameters) are used throughout, with fine-tuning applied to improve package inspection accuracy. A novel "Megamind" orchestration agent mitigates context retention issues inherent to long-horizon planning with smaller models. The system was validated in a hardware-in-the-loop simulation using an AMD Ryzen(TM) AI mini PC. Results demonstrate that a fully onboard MAS architecture is a viable, cost-efficient alternative to cloud-dependent deployments, with strong potential for real-world transfer. The simulation environment has been released as open source under the Apache 2.0 licence.

### 17. Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses
- Deep score: 0.3
- Date: 2026-07-06T13:10:13+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.05029
- Summary: Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals. We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA's attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent's retrieved content but also the integrity of its reasoning history.

### 18. Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory
- Deep score: 0.3
- Date: 2026-07-06T00:00:00+00:00
- Source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2607.05511
- Summary: Agentic video understanding equips models with long-term memory to autonomously process and respond to continuous, long-horizon multimodal streams. However, advanced video agents often rely on ``detective-style'' iterative reasoning for action control (e.g., search) and evidence aggregation, incurring prohibitive costs and latency. We argue that such heavy reasoning primarily compensates for the lack of global context and semantic misalignment in retrieval. This paper introduces Light-Omni, a multimodal agent framework for reflexive and lightweight video understanding. It achieves this through dual contextual states that instantly build the required context in a single forward pass. First, we maintain a global state, a finite-sized multimodal script continuously consolidated from episodic memory, serving as the global context for Light-Omni. Through hierarchical merging, it preserves recent details while summarizing past events. Second, conditioned on this global context, we generate a parametric latent state that directly drives autonomous actions and produces retrieval embeddings, with minimal latency. Benefiting from this coupled design, Light-Omni achieves semantically aligned retrieval and reflexive responses while avoiding iterative reasoning. Extensive experiments validate the effectiveness of Light-Omni across multiple video benchmarks. Notably, it outperforms M3-Agent with an average 2.4% accuracy gain, a 12.1times speedup, and a 2.6times improvement in GPU memory efficiency. Furthermore, it serves as a memory system to enhance both the performance and efficiency of existing MLLMs. Project page: https://clare-nie.github.io/Light-Omni.

### 19. A Common Neural Signal of Evidence Accumulation for Perceptual and Mnemonic Decisions
- Deep score: 0.3
- Date: 2026-07-06T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://www.biorxiv.org/content/10.1101/2025.11.13.688140
- Summary: Humans frequently make decisions based on sensory input from the external environment or information retrieved from memory. The centro-parietal positivity (CPP), an event-related EEG potential, has recently been identified as a neural correlate of sensory evidence accumulation during perceptual decision-making tasks. However, it remains unclear whether this component also reflects the accumulation of evidence in service of decisions grounded in semantic and episodic long-term memory. Across two experiments, we investigated whether the CPP serves as a domain-general neural signal of evidence accumulation. In Experiment 1, participants completed 2AFC perceptual and semantic memory tasks with varying levels of evidence strength. Perceptual judgements involved luminance discrimination of alphanumeric strings with three luminance difference levels controlling perceptual evidence strength. Semantic memory judgements involved discriminating population differences between U.S. states with census data used to define three bins of memory evidence strength. A CPP component was observed in both tasks whose build-up rate (i.e., slope) scaled with evidence strength, response time, and confidence in both stimulus- and response-locked analyses. Extending these findings to episodic memory, participants in Experiment 2 completed a two-alternative forced-choice word recognition task with target words varying in exposure frequency during learning to control episodic memory strength. Again, we found that CPP slopes scaled with memory strength, response time, and confidence. Together, these findings support the CPP as a domain-general neural signature of evidence accumulation across perceptual, semantic, and episodic mnemonic decisions.

### 20. AGL-1: The Enterprise AI Governance Layer as a Control Plane for Trusted Enterprise Intelligence
- Deep score: 0.3
- Date: 2026-07-03T17:42:08+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.03516
- Summary: Enterprise artificial intelligence is moving from isolated experimentation toward operational dependency across copilots, retrieval-augmented generation systems, autonomous agents, and AI-enabled business workflows. As this transition accelerates, the primary enterprise challenge is no longer only model access or inference scale. It is governed intelligence operations: the ability to enforce authorization, preserve contextual lineage, control persistent memory, detect stale or conflicting knowledge, constrain agentic execution, and produce audit-ready evidence across distributed AI estates. This paper introduces AGL-1, the Enterprise AI Governance Layer, as a vendor-neutral reference model for the control plane that should operate across foundation models, retrieval systems, orchestration frameworks, enterprise memory, policy engines, observability systems, tools, APIs, and business applications. Building on governed knowledge-system principles introduced in GKS-5, AGL-1 generalizes the governance problem from retrieval-specific controls to full AI execution-path governance. It identifies recurring failure modes such as unauthorized retrieval, stale grounding, unmanaged memory, weak provenance, policy drift, fragmented observability, and uncontrolled autonomous execution. It then defines seven governance domains: identity-aware retrieval, policy enforcement, provenance management, memory governance, knowledge integrity monitoring, agentic execution control, and trust observability. The central claim is that durable enterprise value from AI will increasingly depend on the ability to govern intelligence at scale. In complex enterprises, trust is not a property of the model alone. It is a property of the system around the model: identity, knowledge, policy, memory, tools, human oversight, and evidence working together as a managed control plane.

### 21. MemSyco-Bench: Benchmarking Sycophancy in Agent Memory
- Deep score: 0.3
- Date: 2026-07-01T15:30:33+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.01071
- Summary: Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of factual accuracy or objective reasoning. Despite this emerging risk, existing memory benchmarks primarily evaluate whether memories are correctly stored, retrieved, or updated, while overlooking how retrieved memories influence downstream reasoning and decision-making. To bridge this gap, we propose MemSyco-Bench, a comprehensive benchmark for evaluating memory-induced sycophancy in agent systems. MemSyco-Bench measures when memory should influence a decision and how valid memory should be used. Specifically, it covers five tasks that assess whether agents can reject memory as factual evidence, respect its applicable scope, resolve conflicts between memory and objective evidence, track memory updates, and use valid memory for personalization. All related resources are collected for the community at https://github.com/XMUDeepLIT/MemSyco-Bench.

### 22. Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems
- Deep score: 0.3
- Date: 2026-06-30T08:41:00+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.31339
- Summary: Agentic artificial intelligence is increasingly used to decompose industrial tasks, propose robot actions, and adapt execution plans in dynamic cyber-physical environments. However, autonomous proposal generation alone does not guarantee that multi-robot industrial systems preserve task dependencies, resource ownership, safety holds, or repair boundaries during long-horizon execution. This paper introduces a verification-gated agentic mission-state governance framework for intelligent industrial multi-robot systems. The framework maintains two synchronized state objects: an evolving task forest for persistent hierarchy, delayed grounding, and repairable substructures; and a governed blackboard for online execution state, robot traces, resource locks, world beliefs, proposals, verification records, and scene-temporary constraints. From each forest--blackboard snapshot, a derived execution coupling topology exposes cross-branch dependencies for proposal verification, parallel-commit eligibility, and bounded repair. Candidate assignments, repairs, deferrals, and constraint updates may be generated by heuristic, optimization, or agentic reasoning modules, but they can update the committed mission state only after deterministic verification and atomic commit. We evaluate the framework in an indoor factory multi-robot scenario, 30-seed remote-construction stress benchmarks, structural ablations, and scalability probes. The results show improved verified and safety-audited mission-state progress with fewer invalid commitments, lock conflicts, duplicate assignments, abandoned nodes, and disruptive repairs under modeled mission predicates. The study positions agentic AI as a proposal-generating layer governed by inspectable mission-state verification rather than as an unchecked execution authority.

### 23. Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation Threats
- Deep score: 0.3
- Date: 2026-06-29T13:07:41+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.30259
- Summary: In contemporary societies, the threat of disinformation has reached alarming levels, exacerbated by the proliferation of electronic communication, social media, and advancements in artificial intelligence. As a result, there is an urgent need to develop effective countermeasures to mitigate this menace. However, the sheer scale of the problem renders manual fact-checking and human-based verification inadequate, underscoring the necessity for automated methods to detect and debunk disinformation. This article proposes a novel approach based on a multi-agent system that emulates the decision-making processes of human annotators engaged in disinformation detection tasks. By incorporating a consensus mechanism, diversity in cognition and diversity in knowledge, and also hierarchical structure, inspired by human annotators' behavior, the proposed method achieves superior results compared to individual Large Language Models (LLMs), including GPT 4 and GPT 3.5. The system leverages open models (e.g., LLaMA, Kimi, Qwen, Deepseek and LLaMA-Nemotron) to ensure greater transparency. The evaluation of the proposed method encompasses datasets in languages with varying resource availability, including English (high-resource), Polish (medium-resource), Slovak (low-resource) and Bulgarian (low-resource). Experiments were conducted on tasks such as direct disinformation detection, identification of texts worthy of verification, and detection of texts containing verifiable factual claims.

### 24. A Multi-Agent system for Multi-Objective constrained optimization
- Deep score: 0.3
- Date: 2026-06-18T13:47:28+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.20236
- Summary: Many decision-making problems in computing and networking systems can be naturally formulated as cost-minimization problems under performance constraints. In dynamic environments, reinforcement learning (RL) is often used to solve such problems at runtime by embedding both costs and constraint violations into a single scalar reward through weighted penalty terms, following a Lagrangian-inspired formulation. However, in this context the behavior of the learned policy critically depends on the choice of these weights, which are typically selected manually. This makes it difficult to identify an appropriate trade-off between optimizing the primary objective and effectively avoiding constraint violations, particularly in non-stationary environments where their relative importance may change. This paper presents MAMO (Multi-Agent system for Multi-Objective constrained optimization), an approach to tackle this balancing problem through multi-agent RL. MAMO decouples task execution from objective design by formulating the selection of reward weights as a learning problem, providing a !rst step towards more autonomous and robust RL-based solutions for constrained optimization problems in dynamic environments.

### 25. GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning
- Deep score: 0.3
- Date: 2026-06-16T03:45:24+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.17480
- Summary: Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Second, the original KnowledgeBank mainly retrieves semantically similar snippets and appends new knowledge, which makes it difficult to control memory quality, conflicts, confidence, and geometric relevance. To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance. To address the second challenge, we upgrade KnowledgeBank into a governed long-term memory system with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while reducing AS by 4.95% and 5.65%, respectively. Code: https://github.com/AIGeeksGroup/GeneralVLA-2. Website: https://aigeeksgroup.github.io/GeneralVLA-2.

### 26. Misinformation Propagation in Benign Multi-Agent Systems
- Deep score: 0.3
- Date: 2026-06-15T13:40:01+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.16710
- Summary: Multi-agent systems, in which multiple large language model agents solve problems through turn-based interaction, are increasingly deployed in high-stakes settings such as medical diagnosis, legal analysis, and forensic decision-making. Their reliability can be at risk when single agents reason from incorrect or misleading context, e.g., from tool calls, since errors may propagate through agent interactions. This work studies this risk by injecting intent-based misinformation into benign single-agent and multi-agent systems across reasoning, knowledge, and alignment tasks. We find that misinformation can degrade single-agent performance and persists across multi-agent debate, with agents often retaining answers introduced by misinformed peers. Nevertheless, multi-agent debate reduces the resulting performance degradation compared to single-agent prompting, especially when most agents are not exposed to misinformation. Robustness depends on group composition and decision protocol. Consensus can be more stable than voting under peer pressure, while majorities can often steer misinformed agents back toward correct answers. Our results show that misinformation robustness in multi-agent systems depends on the underlying model and also on how agents exchange information and aggregate decisions.

### 27. Decentralized Multi-Agent Systems with Shared Context
- Deep score: 0.3
- Date: 2026-06-09T10:13:07+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.10662
- Summary: Multi-agent systems (MAS) can scale large language model reasoning at test time by decomposing complex problems into parallel subtasks. However, most existing MAS rely on centralized orchestration, where a main agent assigns work, collects outputs, and merges results. As the number of subtasks grows, this controller becomes a communication and integration bottleneck. We propose Decentralized Language Models (DeLM), a MAS framework that decentralizes coordination through parallel agents, a shared verified context, and a task queue. Agents asynchronously claim subtasks, read accumulated progress, perform local reasoning, and write back compact verified updates. The shared context acts as a common communication substrate, enabling agents to build on one another's verified progress without routing every update through a central controller. Empirically, DeLM improves both software-engineering test-time scaling and long-context reasoning. On SWE-bench Verified, DeLM achieves the best performance across Avg.@1, Pass@2, and Pass@4, with gains of up to 10.5 percentage points over the strongest baseline, while reducing cost per task by roughly 50%. On LongBench-v2 Multi-Doc QA, DeLM achieves the highest average accuracy across four frontier model families, improving over the strongest baseline by up to 5.7 percentage points. The code is available on our project website at https://yuzhenmao.github.io/DeLM/.

### 28. Distilling LLM Reasoning into an Interpretable Policy Tree for Human-AI Collaboration
- Deep score: 0.3
- Date: 2026-06-07T12:20:32+00:00
- Source: arxiv
- Focus/tech: cognitive outsourcing, AI agents / cognitive outsourcing
- URL: https://arxiv.org/abs/2606.08596
- Summary: Constructing efficient and reliable policies to assist humans is indispensable for human-AI collaboration. Existing methods mainly follow two lines of work. Most prior work relies on multi-agent reinforcement learning (MARL) to learn black-box policies, which limits interpretability and raises safety concerns. Recent methods query large language models (LLMs) at each decision step, causing slow responses and high inference costs. We propose Collaboration Policy Tree (Co-pi-tree), a closed-loop method that learns an executable policy tree consisting of a partner-behavior prediction tree and an agent-action selection tree. Co-pi-tree constructs a policy by distilling LLM reasoning into policy tree code. It then evaluates the policy through partner interaction, obtains feedback, and uses natural language to summarize the interaction feedback to improve problematic branches. Experiments in Overcooked-AI show that Co-pi-tree improves average reward by 35.4% over the baseline average, while reducing the number of LLM queries by 77.7% and test-time latency by 97.1%. Project page: https://beiwenzhang.github.io/Co-pi-tree/

### 29. Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems
- Deep score: 0.3
- Date: 2026-06-04T05:10:20+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.05711
- Summary: Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. The dominant communication protocol in such systems is natural language: agents exchange messages token-by-token, verbalising their internal reasoning so that peers can read, verify, and respond. While convenient and interpretable, this protocol suffers from three structural drawbacks -- high inference cost, irreversible information loss during discretization, and ambiguity/redundancy of natural language. A growing body of work therefore explores an alternative protocol -- latent communication -- in which agents exchange continuous representations (embeddings, hidden states, or KV-caches) directly, bypassing the bottleneck of text generation. This paper presents a unified framework for organising the rapidly expanding literature on latent communication. We analyse existing methods along three orthogonal axes: (1) WHAT information is communicated (Embeddings, Hidden States, KV-Caches, or other continuous state); (2) WHICH sender-receiver alignment is used (latent-space alignment and layer alignment); and (3) HOW the communicated information is fused into the receiver (concatenation, prepending, mathematical operations, cross-attention, or cache restoration). Under this 3-axis framework, we systematically categorise eighteen representative methods proposed between 2024 and 2026, identify five major design patterns, and surface a set of open challenges -- including cross-architecture alignment, security of latent channels, compression for edge deployment, and the relationship between latent communication and latent chain-of-thought. We hope that this framework both lowers the barrier to entry for new researchers and provides a vocabulary for comparing future work.

### 30. Traj-Evolve: A Self-Evolving Multi-Agent System for Patient Trajectory Modeling in Lung Cancer Early Detection
- Deep score: 0.3
- Date: 2026-06-01T19:30:07+00:00
- Source: arxiv
- Focus/tech: AI agents, human augmentation / AI agents
- URL: https://arxiv.org/abs/2606.02812
- Summary: Modeling patient trajectories from longitudinal electronic health records (EHRs) requires reasoning over sparse, noisy, and long-context multimodal sequences. Existing LLM-based multi-agent systems address context length but process patients in isolation, failing to mirror how clinicians leverage accumulated experience from similar prior cases. We present Traj-Evolve, a self-evolving multi-agent system with two complementary evolving mechanisms. First, an Experience Pool (ExPool) acts as a non-parametric memory, indexing rejection-sampled reasoning traces to retrieve similar patients as few-shot contexts. Second, multi-agent reinforcement learning (MARL) via reward-ranked fine-tuning parametrically optimizes inter-agent and agent-memory collaboration. A leave-one-out cross-retrieval strategy unifies the two, aligning training- and inference-time behavior under retrieval augmentation. On a lung cancer prediction task utilizing up to five years of multimodal EHRs, Traj-Evolve outperforms 9 strong baselines on the overall population and a challenging never-smoker population. Analysis of the evolving dynamics highlights three key findings: (1) expanding the ExPool shifts optimal retrieval from diverse to specific samples; (2) under MARL, the manager agent's prediction loss converges quickly while the worker agents' temporal reasoning continues to benefit from more verified patients; and (3) the two mechanisms are complementary on the predicted risk, where ExPool improves specificity while MARL improves sensitivity.
