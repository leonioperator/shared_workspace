# Blindspot Signals Report - 2026-10-15

- Source export: `/opt/apps/haier/exports/evolution_signals_20261015_020454.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 569
- Deduped/weighted signal clusters: 531
- Novel vs previous reports: 40
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. ChunkAct: Action Chunking for Agentic Robotics
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-13T17:59:57+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.18874
- Summary: Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.

### 2. Towards Agentic Robots: Model, Data, Environment, and Harness
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-14T16:32:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.20442
- Summary: Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic environments, rectify execution errors autonomously, and dynamically adjust operational strategies. Although this field develops fast, current studies are not well connected. Researchers have no consistent view of how to combine different agentic functions into a complete robot system. This paper provides a unified overview of existing research on agentic robots. We first trace the development from robot policies to agentic systems, covering vision-language-action models, world models, and world-action models. We then clarify the definition and scope of agentic robots and organize existing research into seventeen categories across four functional domains: Model, Data, Environment, and Harness. Across these domains, we examine how agents shape model learning and robot decisions, collect and curate robot data, construct worlds, tasks, and tests for learning and evaluation, and organize capabilities for robot use. Finally, we discuss open challenges and outline directions for future research. Looking forward, we hope this work contributes to a clearer understanding of agentic robots and supports new approaches to making them more capable, reliable, and adaptive.

### 3. HEM-Med: A Hierarchical Agentic Memory Framework for Safe Multi-Center Medication Recommendation
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-14T13:39:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.20191
- Summary: Medication recommendation (MR) is critical for clinical decision support. While existing MR methods are mostly designed for single-center learning, where only one independent hospital is involved, multi-center MR with hospitals of different scales has become increasingly demanding in practice. In multi center settings, abundant data from large medical centers can improve recommendation performance for low-resource centers. Despite a few preliminary attempts on this task, two critical gaps remain. Gap 1: Existing multi-center methods fail to disentangle transferable cross-hospital clinical experience from hospital-specific prescribing patterns, limiting clinical feasibility and physician acceptance. Gap 2: They commonly overlook multi label safety constraints of MR, including drug-drug interaction risks and local formulary feasibility, which are essential for safe real-world deployment. To address these gaps, we propose HEM-Med, a novel hierarchical agentic memory framework for multi-center MR. To address Gap 1, we design a disentangled hierarchical memory module that builds patient-level medication context attribution records and disentangles them into cross hospital experience memory and hospital-specific residual memory. To address Gap 2, we introduce a safety-aware medication set generation module, which integrates dual-level experience retrieval with safety-aware set decoding to produce clinically relevant, safer, and locally adaptive medication recommendations. Experiments on a real-world multi-center eICU dataset show that HEM-Med outperforms representative transfer learning, LLM-based, and MR baselines in terms of both recommendation accuracy and safety.

### 4. EGCForest: Structured Agent Memory Organization for Enterprise Group Chats
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-14T09:07:53+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.19836
- Summary: Enterprise group chats record project progress, decisions, task ownership, and other organizational information valuable to enterprise agents. Reliable retrieval is challenging because evidence spans interleaved threads, channels, and time, with meaning and authority conditioned on the speaker. Neither RAG's independent chunk retrieval nor memory systems' summary-based consolidation can reliably recover such distributed evidence. We present EGCForest, a novel multi-view hierarchical memory framework for enterprise group chats. EGCForest organizes an immutable message log into three complementary forests: a Channel forest for temporal workflows, an Actor forest for speaker-conditioned context, and an Artifact forest for deliverable lifecycles. Cross-view connections are enabled by a Placement Map and sparse structural bridges. Built on this memory backbone, EGCForest retrieves and assembles evidence by jointly leveraging message-level relevance, hierarchical context from forest summaries, and cross-view links, recovering distributed evidence. Experiments on three enterprise-chat benchmarks show that EGCForest consistently outperforms RAG and memory-system baselines, improving answer accuracy by up to 20.85 points over MemOS while supporting efficient online retrieval.

### 5. Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-14T05:18:16+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.19600
- Summary: Recent vision-language-action (VLA) models have shown strong performance on local robot manipulation, yet their success does not readily translate to long-horizon mobile manipulation. In our experiments, a pretrained subtask VLA achieves 80% success rate on atomic manipulation tasks but only 19% when these skills are composed into mobile manipulation. We argue that this gap stems from failures across the execution process rather than from local manipulation capability alone. To uncover these bottlenecks, we systematically diagnose failures in long-horizon mobile manipulation and identify three dominant regimes: task planning, navigation and base positioning, and local manipulation. Based on this diagnosis, we develop failure-guided agentic intervention that augments a fixed subtask VLA with demonstration-based planning guidance, adaptive visual memory, accessibility-aware base adjustment, and local end-effector adjustment. On RoboCasa365, these interventions progressively improve task success from 19% to 47%, with the finalized system reaching 49% on held-out episode seeds, compared with 18% for the baseline. The same design improves performance from 14% to 37% on BEHAVIOR-1K and from 5/20 to 13/20 on real-robot tasks. These results suggest that reliable mobile manipulation can be advanced by diagnosing and intervening on the current bottleneck, rather than uniformly scaling the underlying policy. Our code will be released at https://github.com/PKU-VaLuE-Lab/Cracking-Mobile-Manipulation.git.

### 6. Optimistic Distributed Submodular Coordination with Applications to Multi-Target Tracking with Multiple Robots
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-14T02:06:54+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.19417
- Summary: We provide a distributed online algorithm for multi-agent submodular coordination in bandit environments, i.e., environments whose evolution is unknown a priori and may even adapt to the agents' actions. We are motivated by multi-robot tasks such as target tracking, where the optimal actions change over time and the agents must track them rather than a single fixed optimum. To address such problems, we provide the Optimistic Distributed Online Greedy (O-DOG) algorithm, that leverages predictions about the environment's behavior and improves regret guarantees. The agents select actions simultaneously over arbitrary, possibly time-varying, network topologies, and each agent acts optimistically, i.e., leveraging predictions of its upcoming rewards, e.g., from forecasts of the targets' motion and of its neighbors' actions. We bound O-DOG's tracking regret in terms of the agents' prediction error and the bound never exceeds its prediction-free counterpart. Particularly, it is sublinear even when the optimal action changes at every time step, provided the predictions are accurate enough. We further quantify the suboptimality due to decentralization as a function of the network structure, and show that accurate predictions accelerate convergence. We validate O-DOG in simulated multi-robot target tracking.

### 7. Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-14T01:11:57+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.19366
- Summary: Multimodal models and agents have emerged to enable AI systems to learn from and interact with the real world more like humans by integrating information across multiple modalities. However, enabling multimodal agents to continually acquire useful information from complex, heterogeneous multimodal data remains a significant challenge as they move toward long-horizon tasks and lifelong settings. Addressing this challenge requires effective memory mechanisms that can maintain continuity across sessions, adapt to changing users and environments, and refine memory-management policies through accumulated experience. We introduce a two-axis analytical framework for multimodal agent memory structured around two key questions: how multimodal information is formed and represented (Axis I, Formation and Representation), and how its management adapts with accumulated experience (Axis II, Memory Management). Axis I, Formation and Representation, characterizes what information is retained and how it is encoded (e.g., modality-specific embeddings, textual and structured records, latent and parametric representations) to support subsequent reasoning and action. Axis II, Memory Management, distinguishes three tiers: T1 Static Memory reuses fixed memory; T2 Dynamic Memory updates memory through a stable policy; and T3 Self-Evolving Memory updates memory through an evolving policy. Based on this framework, we synthesize recurring design patterns and derive principles for balancing source fidelity with abstraction, maintaining temporal validity and provenance, grounding memory use in recoverable evidence, and evolving memory policies over time. Furthermore, we discuss the challenges and potential future directions for the memory mechanism of multimodal agents.

### 8. FACT: A Multimodal Force-Action-Track Foundation Model for Human-to-Robot Dexterity
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-13T20:21:52+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.19155
- Summary: Human demonstrations offer a scalable alternative to costly robot data collection for dexterous manipulation, but most human datasets lack force measurements. Dexterous manipulation requires not only visual and proprioceptive understanding but also the ability to anticipate and regulate interaction forces. To scale force-aware human-robot co-training, we introduce EgoForce, a large-scale human tactile dataset capturing force-rich manipulation experience, and combine it with robot demonstrations for pretraining. We present FACT, a robot foundation model that cascades from prospective visual planning to force-aware refinement for dexterous manipulation. FACT comprises two jointly trained components. A Track-Guided Coarse Planner jointly predicts actions, future video, and visual tracks. Future video and visual tracks also provide a shared task representation that facilitates cross-embodiment knowledge transfer and coarse action generation. Building on this coarse plan, a Force-Action Joint Refiner jointly predicts future force and refines the coarse action, allowing anticipated force and action to shape each other during refinement. We evaluate the model on ten tasks requiring fine-grained coordination and force feedback, including tool use, musical instruments, and precision laboratory procedures. Using as few as 10 robot trajectories with 90 human trajectories for fine-tuning, FACT outperforms both baselines, with success-rate gains of up to 60 percentage points over T-Rex. Ablations show that force supervision in human pretraining data is crucial for downstream robot performance after fine-tuning, while visual track prediction and training with future-force prediction improve dexterous execution. Experiments varying the human-robot data ratio during fine-tuning further suggest that FACT learns from human demonstrations nearly as effectively as from robot demonstrations.

### 9. BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-13T17:34:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.18780
  - Alt: https://arxiv.org/abs/2610.11600
- Summary: Large language model multi-agent systems extend individual agents' capabilities through collaboration across specialized roles, tools, and workflows. Yet collaboration makes failures harder to diagnose: one agent may misinterpret a correct result while others carry the mistake forward. Failure attribution therefore seeks to identify the responsible agent and decisive error step. Recent methods trace dependencies, but knowing where information came from is not the same as knowing where it went wrong. We introduce BLADE (Blame Localization via Audited Dependency Evidence), a training-free framework that moves beyond tracing information to auditing its use. Using Jev for structured probabilistic judgments, BLADE uses dependency probabilities to select relevant source-decision handoffs for auditing. At these handoffs, it examines whether receiving decisions use their sources faithfully and within task requirements, distinguishing error introduction, propagation, and repair. These findings inform a global diagnosis that considers all execution steps. Without reference answers, BLADE achieves the best or tied-best step accuracy among eight strategies under a shared Jev decision interface on 1,228 failed runs across five Who&When and Who&When Pro subsets, outperforming All-at-once by 2.2-11.1 percentage points. Making responsibility evidence explicit offers a path toward more interpretable and reliable agentic systems.

### 10. BRIDGE: Selective Boundary Repair with Dependency Graph Evidence in Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-13T06:31:57+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.17805
- Summary: Multi-agent collaboration has emerged as a critical paradigm for tackling complex, long-horizon tasks; however, while coordination protocols continue to advance, systemic failures at the inter-agent collaboration interface remain a pervasive bottleneck. In collaborative workflows, systems frequently suffer from \emph{broken handoffs}---where critical task context is omitted, misrouted, or ignored despite each agent emitting locally plausible responses. To address this challenge, we present \method, a verifiable runtime control framework that treats handoff repair as selective intervention over explicit dependency graphs. Central to \method is an integrated fault-attribution and calibration pipeline, \dataset, which decouples execution dependencies and injects counterfactual handoff perturbations to provide empirical supervision for runtime intervention. Leveraging this diagnostic foundation, \method dynamically compiles observable interaction traces into a provenance graph to pinpoint unresolved dependencies, without accessing private agent states. It then evaluates candidate repairs through an empirical gate that weighs expected gains against disruption risks, and executes repairs only when formal local postconditions hold. Extensive evaluations across demanding benchmarks demonstrate that \method boosts task success by up to 12.3 absolute percentage points on SILO-BENCH and 11.1 on TeamBench. Across both backbones, \method maintains strict cost-effectiveness, adding as little as 2.0\% marginal token overhead. Furthermore, on 562 handoff-relevant traces from the MAST benchmark, \method achieves 69.8\% F1 in a single pass, establishing a reliable operational boundary for verifiable coordination repair.

### 11. MAS-Gate: Unlocking Multi-Agent System Lifecycle via Node-Centric Quantification
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-13T02:33:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.17613
- Summary: Large language model (LLM)-based multi-agent systems (MAS) can solve complex problems beyond the reach of a single agent by decomposing tasks and coordinating complementary capabilities. Despite extensive research on MAS, existing work largely focuses on specific aspects or individual phases of their development and operation, resulting in fragmented perspectives with objectives and signals that are difficult to reconcile across these different settings. To bridge these disconnected perspectives, we conceptualize MAS development and operation as a three-phase lifecycle spanning design-time orchestration before execution, runtime intervention during execution, and post-hoc attribution after execution, and introduce MAS-Gate, a unified node-centric quantification applicable across these phases. Modeling each execution as a directed acyclic graph, MAS-Gate combines within-node utility, which estimates a node's contribution through changes in reference-answer likelihood, with inter-node strength, which approximates semantic uptake and potential downstream reach. We adapt this shared quantification to three objectives: providing a structure-aware dense reward for Orchestrator training, training an Editor to act on execution prefixes using paired rewards from completed edited and unedited trajectories, and supplying risk-ranked nodes as auxiliary evidence for LLM-based post-hoc attribution. Experiments spanning interaction environments, knowledge-intensive multi-hop question answering, general reasoning, and post-hoc attribution demonstrate that MAS-Gate improves workflow construction, targeted runtime editing, and LLM-assisted error localization over corresponding phase-specific baselines. Together, these results establish MAS-Gate as a unified structural interface for improving MAS generation, dynamic editing, and error attribution throughout the lifecycle.

### 12. IBM Study: Eight in Ten EMEA Enterprises Escalate AI Incidents to Board or C-Suite as AI Agents Test Governance - IBM Newsroom
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-14T23:02:03+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMi3wFBVV95cUxNOGRIM2VCbDY1bEs0czNwNS1hRFg0em9JaTJVQV9MVVgyQkZvZ0txeFJGLURkQmVCT0lEZHdCaXByalU5aV9remJDZ3pIUWM2aEg5azFPWG91NUV4ZjJHek1EMWxBenEwNHpWWkVfd0R1NkFqSk1lUXBVSWpTUDhBcmhBMHpDRERLNHlqR05BWGNiREF4X01aSUtoRW85bWNPWWUxNmk0X19zcFRIMjBueDdSSFRXN3FXX0FKVTZtWTRsUVViYWN2N015dVZTazd3SlZ4SDVNcU5PMGV0OW93?oc=5
- Summary: IBM Study: Eight in Ten EMEA Enterprises Escalate AI Incidents to Board or C-Suite as AI Agents Test Governance&nbsp;&nbsp;IBM Newsroom

### 13. The AI Governance Gap CX Leaders Cannot Afford to Inherit - CMSWire
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-14T20:49:13+00:00
- Primary source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMiuAFBVV95cUxPei1zTGt1ek9nbmhBTW9veVhIdTFjQ3M3VFk4RVBKczRRaWFsSDJ0aDhEankzNjF0UjlqUXI3VWVhbmpSZURQSDlrcHVBQzc3eVRpeUZpRXRYNGJSVjh0LVpWQ2RIcjVGMk9neTFJaVBaWi1zbDJfaVZ3M1hPeGpTRTU4OEJNdDVNaGdWSnZpVWJIUThzN05XN3JjcG1SUzljWGtNLXZ5d1ppMmV3dlNVdjR6VWhOUFZB?oc=5
- Summary: The AI Governance Gap CX Leaders Cannot Afford to Inherit&nbsp;&nbsp;CMSWire

### 14. Micro-payments power autonomous AI software as onchain agentic transactions soar - CoinDesk
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-14T15:35:36+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMixAFBVV95cUxNYXpmbGVmNXZ0OVUxVVE3dHNUTUR3cF9SSURfYVNEd2h1UGh0RVRzdFVZQUk0VWZQWTNHVm9HTVlkY1ZFNVkwbVc2VDFadGZaekJDV1JOZG5VSHFZS25TZjNTejlkci0zQjF5LXhHd2JZcEpWSThKNnViakVMOEduTUF1TEJnVU9vaEV4ajdvM2o0bGdZTXV4TWpqQlltNzZzRlBKQ1pocEFSYlc0WEZUcUFIZWFyRmlkQ2hKUlljZ3ByejZC?oc=5
- Summary: Micro-payments power autonomous AI software as onchain agentic transactions soar&nbsp;&nbsp;CoinDesk

### 15. Think Once, Reflect Twice: How Feedback Shapes Human-AI Collaboration
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-14T11:09:31+00:00
- Primary source: arxiv
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://arxiv.org/abs/2610.19991
- Summary: As artificial intelligence (AI) increasingly supports human decision-making in high-stakes domains, designing effective human-AI collaboration becomes critical. Successful collaboration requires humans to reflect on decision-making processes and adjust their strategies accordingly. Current research typically investigates interventions, such as explainable AI, that target reflection during the decision-making process (reflection-in-action). Less attention has been given to retrospective examination of decisions (reflection-on-action). This work explores reflection-on-action by studying the impact of feedback on reliance behavior and human-AI team performance. Specifically, we investigate feedback interventions targeting overrides of AI advice through a behavioral study (N=244). We find that such feedback influences reflection-on-action, while unidirectional feedback risks reducing subsequent reflection-in-action. Furthermore, we identify opposing shifts in reliance behavior that leave overall human-AI team performance unchanged but show context-dependent effects. Balanced feedback did not show these risks, preserving both concurrent and retrospective reflection, offering insights for designing for appropriate reliance on AI.

### 16. When Extremists Enter LLM Societies: Investigating Extreme Behavior in Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-14T09:27:13+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.19863
- Summary: Large language model (LLM) agents increasingly serve as computational actors in multi-agent social simulations. While existing work emphasizes representative personas and average-case behavior, social science shows that persistent tail actors can disproportionately shape collective dynamics. We study this regularity in controlled LLM-based multi-agent systems (LLM-MAS). In these systems, such actors cannot be reduced to fixed scalar states: prompts, natural-language histories, and backbone generation mediate their behavior and influence. We first analyzed three properties of extremists in sociology and model the LLM extremist based on LLM-native perspective. We introduce EXAM, an EXtremist Agent Modeling framework that capable of configuring extremist agents for specific tasks and precisely controlling their population proportion, spatial distribution, interaction protocols, and measurement interfaces. Across four scenarios: congressional election, financial crisis, epidemic public opinion, and iterated prisoner's dilemma, we observe that small persistent tail groups produce measurable, backbone- and scenario-dependent collective shifts. EXAM shows how this social-science regularity manifests through language-mediated mechanisms specific to LLM-based social simulation.

### 17. Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-14T08:42:05+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.19799
- Summary: Recent work lets LLM agents evolve their own harness, up to the team itself. Yet in human groups, the same abilities achieve different outcomes under different social conditions. Borrowing the notion of scaffolding from developmental psychology, we investigate whether the social scaffolding of a self-evolving multi-agent system (MAS), namely its team composition and structure of interdependence (e.g., collaboration, conformity, or competition), shapes how the team evolves. We present AGORA (Agents Growing through Organization and Relational Arrangements), a framework that varies the two axes independently across three evolution mechanisms. Across web search, codebase understanding, and document QA, we find that (1) evolution alone rarely helps, while the right scaffolding surpasses a strong agent evolved alone by up to 25 points; (2) it does so by moving authority to the most capable member while the others step back; and (3) this member, having grown within the team, outperforms the same model alone. Designing a self-evolving MAS thus requires designing its social scaffolding, which shapes not only how its agents learn, but who gets to lead.

### 18. WriterzRoom
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-14T04:35:22+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/writerzroom
- Summary: <p> Governed multi-agent AI content for regulated industries </p> <p> <a href="https://www.producthunt.com/products/writerzroom?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1279741?app_id=339">Link</a> </p>

### 19. Beyond Retrieval: Evidence Access and Event Aggregation in Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-14T02:53:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.19474
- Summary: Questions about an agent's history often require aggregating events, which retrieval alone does not resolve. We combine source-preserving evidence access with executable aggregation. Trajectory Memory (TM) retains the original trajectory and constructs a source-addressable reading view at question time. TallyMem augments it with a reusable event ledger, model-generated event specifications and deterministic execution. With a commit-specific adaptation on 776 questions from 99 held-out MINTEval repositories, TallyMem raises Qwen3-32B exact match from 35.2% to 49.0%, a 13.8-point gain over TM; gains span 12.8-13.9 points across three readers. A controlled probe with event sets parsed independently from raw logs shows an 11.0-point gain, from 82.8% to 93.8%, without routing. On full AMA-Bench, the routed system yields a smaller 1.3-point gain, from 69.8% to 71.1%. These results support executable aggregation on tasks that require combining events, with benefits dependent on the task and event specification, the largest residual system-error category in our diagnostic analysis.

### 20. MemCode: Discrete Semantic Representations for Long-Term Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-14T02:51:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.19472
- Summary: Long-term memory remains a fundamental bottleneck for large language model (LLM) agents across sessions. Existing systems typically adopt a write-then-retrieve paradigm, storing context-dependent dialogue fragments and retrieving them via nearest-neighbor search in a continuous embedding space. This design yields unstable access units and systematically misses logically related but lexically distant evidence. We propose MemCode, a long-term agent memory framework that couples retrieval-oriented writing with discrete associative retrieval. MemCode rewrites dialogue into self-contained atomic memory units (AMUs), maps AMUs into a learnable codebook with isomorphic semantic quantization (ISQ), and uses codebook co-occurrence topology as a retrieval path complementary to vector search. For long-term memory stores, MemCode separates online atomic writes from asynchronous offline consolidation. On LongMemEval-S and LoCoMo with GPT-4o-mini and Qwen3-30B-A3B-Instruct-2507 backbones, MemCode achieves the best overall accuracy while keeping per-dialogue memory construction within roughly 40~130 seconds, making it 3~21 times faster than LightMem and over an order of magnitude faster than A-MEM and MemoryOS.

### 21. Hindsight 1.0 + Memlake
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-13T18:51:23+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/vectorize
- Summary: <p> Open source memory for AI agents to learn from experience </p> <p> <a href="https://www.producthunt.com/products/vectorize?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1279402?app_id=339">Link</a> </p>

### 22. SEAR: Self-Evolving Agentic Robotics
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-13T17:40:20+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.18792
- Summary: Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the agent really learning, or just trying more often? And does what it learns still help on new tasks, in a new simulator, and on a real robot? The framework runs an agent in three modes: it writes code that becomes the policy (code-as-policy), acts live in the control loop (agent-as-policy), or works as a researcher that fine-tunes a vision-language-action model (auto-research). The benchmark adds controls that separate retained experience from repeated attempts, familiar tasks, privileged simulator state, larger budgets, and luck. Across seven frontier language models, 330 simulated and five physical tasks, and over four years of agent runtime, we highlight three findings. First, the learning curve of a robotic agent depends both on the overall time budget and the task difficulty relative to model capability. Harder tasks make longer sessions worthwhile; on easier tasks, re-rolling short attempts does just as well. Second, control code and shared routines transfer across tasks and simulators, while task-specific solutions do not. On a real robot, we observe a performance gap between agent-designed practice and novel human-designed scenes. Third, different models evolve more effectively in different ways. Some do best acting live, others writing code first. And a text-only model keeps pace with a comparable multimodal one: perception helps with error assessment, but agentic reasoning and tool use can matter more. We release the benchmark and codebase to support future research.

### 23. On Symmetry for Characterizing Agent Heterogeneity in Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-13T15:19:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.18538
- Summary: Understanding agent heterogeneity can inform the design of shared and agent-specific policy representations, however existing criteria provide no unified structural test. We study finite-horizon POSGs and define a type-compatible transformation as a policy-evaluation symmetry when complete policy evaluation commutes with it for every decentralized behavioral policy. Policy-evaluation symmetries form a group for which agent orbits define structural agent types. This classification does not depend on the particular policy chosen or the distribution of initial states. We prove that every componentwise environment automorphism is a policy-evaluation symmetry, but that the converse does not hold. Applying the framework to cooperative Dec-POMDPs shows that agents can belong to different structural types even when they share a common reward. For prescribed weighted reward aggregation, we derive an exact value identity and sufficient conditions for the resulting Dec-POMDP to inherit the policy-evaluation symmetries of the source POSG. Finally, we give sufficient conditions under which repeated model factorizations induce policy-evaluation symmetry, and show that preserving an optimal Boltzmann policy set neither implies nor follows from this symmetry in general.

### 24. Make0 Brain
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-10T11:10:23+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/make0-brain
- Summary: <p> A memory store that works across all of your AI agents. </p> <p> <a href="https://www.producthunt.com/products/make0-brain?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1275818?app_id=339">Link</a> </p>

### 25. ifixai ai / iFixAi
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-15T02:02:16.560067+00:00
- Primary source: github_trending
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://github.com/ifixai-ai/iFixAi
- Summary: Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most crucial question in the AI Agent Economy. Is the agent doing what is supposed to do? With iFixAi you can have this answer in less than 120 seconds.

### 26. CedarDB wants one database to handle both transactions and analytics, as AI agents raise the stakes
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-14T22:00:00+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/10/14/cedardb-wants-one-database-to-handle-both-transactions-and-analytics-as-ai-agents-raise-the-stakes/
- Summary: Databases have traditionally been designed either for analytical data or for operational data. But database engine CedarDB supports both, and its approach has gained relevance with the rise of agentic AI.

### 27. Apate sends AI agents undercover to get scammed so they can gather fraud intelligence
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-14T18:00:00+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/10/14/apate-sends-ai-agents-undercover-to-get-scammed-so-they-can-gather-fraud-intelligence/
- Summary: Most companies use AI agents to ship products faster or speed up workflows. Apate.ai sends them undercover to get scammed.

### 28. AI Agents in the Workplace - CBIA
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-14T17:30:27+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiZkFVX3lxTE5CclZKTkIwZ2hCUXp5eHJZTTJUbDVUcUhjY2RGTmtQNlN2Z2J2cndwd2wzWDdwOFprUVc3cTRnd0J0SzlaV2g3TVFDaklLUFBSRUcyYy1yTUZLaVhHdXZSN3BYTE95Zw?oc=5
- Summary: AI Agents in the Workplace&nbsp;&nbsp;CBIA

### 29. I Deleted 168,000 Lines of Comments. My AI Agent Didn't Notice
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-14T16:34:53+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://openstation.blog/2026/10/13/i-deleted-168000-lines-of-comments-my-ai-agent-didnt-notice/
- Summary: No summary.

### 30. Floqer’s AI agents research sales prospects so teams don’t have to
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-14T15:00:00+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/10/14/floqers-ai-agents-help-b2b-revenue-teams-research-customers/
- Summary: The problem Floqer is trying to solve is familiar to anyone who has worked in sales or revenue operations.

## Top Signals By Weighted Score (including already-seen)

### 1. AECG: Asymmetric Experience Consolidation and Governance In Multi-Agent Systems
- Weighted score: 0.60
- Deep score: 0.6
- Date: 2026-10-04T12:38:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.05176
  - Alt: https://arxiv.org/abs/2610.12453
  - Alt: https://arxiv.org/abs/2610.09824
- Summary: Large language model (LLM)-based multi-agent systems increasingly rely on memory to transform execution trajectories into reusable procedural knowledge. Yet repeated retrieval also makes memory errors persistent: memory pollution arises when outdated, weakly supported, or spuriously successful procedures become recurring components of future reasoning. Multi-agent execution introduces an additional structural risk. Scope collapse occurs when procedural knowledge escapes the coordination scope in which it was shown effective and is repeatedly reused at incompatible decision levels, allowing local errors to influence cascades of downstream decisions. Meanwhile, task-level failures provide ambiguous supervision because they rarely reveal which recalled knowledge was responsible. We introduce AECG, a framework for asymmetric experience consolidation and governance for multi-agent systems. AECG turns memory from static experience storage into a dynamic reliability-governance loop, preserving coordination scope and using multi-scale, confidence-aware reliability to detect degradation. It then combines degradation with downstream impact to prioritize high-risk knowledge under a bounded review budget, applies targeted interventions, and reactivates revised skills only after paired replay. Across three multi-agent frameworks and four benchmarks, AECG achieves the best score in 11 of 12 framework--benchmark settings and improves over the strongest competing memory method by as much as 10.23 percentage points; removing scope preservation reduces accuracy by up to 16.89 points. AECG thereby reframes multi-agent memory from passive accumulation into auditable reliability governance. Code is available at https://github.com/fenhg297/AECG

### 2. PANINI-DR: Controlled Deep Research through Generative Semantic Workspaces
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-10-10T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2610.15208
- Summary: Deep research requires connecting multiple steps of search, reasoning, and computation, with intermediate findings guiding what to investigate next. As investigations grow, agents must maintain research state across model calls and check findings before errors propagate into subsequent work. We introduce PANINI-DR, a multi-agent harness that separates coordination of the overall investigation from the research and verification of individual subquestions. A shared workspace, built on the Generative Semantic Workspace representation, records subquestions, their dependencies, findings, and supporting evidence. Researchers investigate individual subquestions, while a separate verification agent checks proposed answers against those subquestions and their evidence. Verification feedback guides further investigation, and recorded findings inform subsequent assignments. We evaluate PANINI-DR on BrowseComp-Plus, FRAMES, and MoNaCo against seven state-of-the-art deep-research harnesses, all using a shared language-model backbone and frozen corpora. PANINI-DR achieves the strongest average performance across the three benchmarks. On BrowseComp-Plus, it achieves 73.3% accuracy, outperforming the next-best harness by 16.0 points. Its advantage is strongest on hard questions, where it answers nearly twice as many as the next-best harness. Ablations further show that structured planning and persistent state improve performance, as does checking each finding against its cited evidence before it is reused. Because a model can answer correctly from memory alone, we also analyze the evidence retained by each harness. PANINI-DR achieves the highest answer recoverability from saved evidence on all three benchmarks, while complementary claim-support audits show stronger evidence-backed answers. Accounting for this evidence changes how harnesses compare and further strengthens PANINI-DR's advantage.

### 3. TRACEDD: A Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-09-18T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.09.12.751167
- Summary: Drug discovery depends on coordinated decisions across target validation, structure analysis, molecular design, developability assessment and synthetic feasibility, but current computational methods often operate as disconnected tools. Here, we introduce TRACEDD (Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design), a framework that makes three primary contributions: (1) It establishes a 'tool-first' multi agentic architecture where LLMs orchestrate validated computational tools rather than replace them, ensuring scientific rigor. (2) It implements a multi-agent system that mirrors expert discovery teams, enabling transparent and traceable decision-making through a Reason-Act-Observe loop. (3) It demonstrates an end-to-end workflow, from target validation to synthesis planning, that adaptively handles real-world data variability, such as the absence of experimental structures. The framework decomposes discovery into specialized agents for target validation, druggability assessment, molecular generation, lead optimization, ADMET evaluation, literature evidence integration and retrosynthesis, all operating through a Reason Act Observe workflow. Using JAK2 as a representative case, we show that the system can retrieve experimental protein structures, invoke AlphaFold when structures are unavailable, identify druggable pockets and perform de novo molecular generation. Known JAK2 inhibitors are used to define design hypotheses and guide reinforcement learning-based molecular generation, with docking scores/predicted pIC50 and other physicochemical/ADMET properties serving as reward and prioritization signals. The framework demonstrates a tool-first, reasoning-driven approach in which each major decision is linked to explicit tool invocation, intermediate evidence. By combining agentic orchestration with domain-specific computational tools, the system supports transparent, adaptable and human-verifiable molecular design workflows, providing a …

### 4. Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-09-10T08:25:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.11225
- Summary: Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

### 5. ChunkAct: Action Chunking for Agentic Robotics
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-13T17:59:57+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.18874
- Summary: Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.

### 6. Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark, and Method
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-07T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents, robotics / AI agents
- URL: https://huggingface.co/papers/2609.35965
- Summary: Vision-and-Language Navigation (VLN) has largely focused on a single agent following a single instruction, yet many real-world applications require teams of robots to tackle tasks beyond the capabilities of any individual agent. We present Systematic Multi-Agent Vision-and-Language Navigation, providing, to our knowledge, the first systematic formalization of multi-agent VLN as a constrained coordination problem: each mission consists of subtasks carrying dependency and resource constraints (presence locks and holding chains). A verified four-stage crafting pipeline instantiates the task as MAVLN, comprising 11,724 episodes across 145 scenes with teams of up to four agents under three instruction regimes, accompanied by tailored constraint-aware metrics. We further present TRISS, a coordination-ready navigation system coupling an LLM-based subtask scheduler, a shared topological memory that turns each agent's exploration into team knowledge, and a conflict-aware execution mechanism that realizes simultaneous intentions as collision-free routes. Extensive experiments establish TRISS as a comprehensive baseline and reveal substantial room for improvement across scheduling, planning, and execution, highlighting the challenges of coordinating under MAVLN task constraints. Project page: https://xyz9911.github.io/mavln.

### 7. PrivMeSA: Privacy-Aware Self-Evolving Multi-Agent System for Medicine via Local-Remote LLM Collaboration
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-29T19:47:38+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38458
  - Alt: https://arxiv.org/abs/2609.37953
  - Alt: https://arxiv.org/abs/2609.19680
- Summary: Clinical large language model (LLM) agents deployed locally can consult more capable remote models, but doing so risks exposing patient information. Privacy-conscious delegation places disclosure decisions with a local agent, yet removing explicit identifiers is insufficient: quasi-identifiers can accumulate across multi-turn consultations and repeated patient visits to enable re-identification. We introduce PrivMeSA, a privacy-aware self-evolving multi-agent system that learns to control disclosure and retains remote expertise for local reuse. A local agent manages each encounter and consults remote specialists that may request additional information. Reinforcement learning balances task accuracy against direct disclosure and registry-based re-identification risk, with privacy evaluated over the complete outbound transcript of each encounter. A local lesson memory distills completed consultations into generalized clinical guidance and retrieves relevant lessons before transmission, allowing subsequent cases to reuse expertise without another remote exchange. Memory grows without additional outcome labels or parameter updates. On an emergency-department benchmark built from MIMIC-IV-ED records, PrivMeSA improves mean task accuracy over delegation by up to 15.8 percentage points. In the same setting, PrivMeSA reduces the disclosure of personal details from 98.0% to 0.2% of cases and the share of cases in which the patient can be narrowed to ten or fewer registry patients from 74% to 0%.

### 8. World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T15:19:39+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.29964
- Summary: General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected automatically from the scene geometry, present the scene around the current interaction. Action rehearsal turns each action into an editable proposal that the agent, alone or through an Imagination Agent, previews and revises against planning feedback before execution. In-view correction closes the loop between observation, rehearsal, and low-level execution, letting the agent remove residual offsets in the view where it observes them. Through the same workspace, WAA acquires embodied procedural knowledge in two ways: it evolves multimodal skills from expert videos and human teaching under evidence-based review and consults them through a Skill Agent, and its interaction traces train smaller VLMs to pilot the same harness. On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art 75.6% average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone; the same skills remain effective on robosuite without further learning. Fine-tuning Qwen3.5-9B on harness traces raises its out-of-domain success from 1.7% to 43.3%.

### 9. RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T11:22:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.29394
- Summary: General-purpose robot agents must learn from experience, transfer to new tasks, and act efficiently. Code as Policies (CaP) methods generate and repair programs at runtime, incurring latency and entangling reusable mechanisms with task-specific decisions. We introduce RACaP, an agentic framework that moves coding to evolution and uses a Reasoning-and-Acting (ReAct) loop to call frozen, typed Policy APIs at deployment. A two-phase strategy combines capability curriculum learning with autonomous self-evolution to improve the APIs, the ReAct harness, and experience memory. The APIs encode reusable physical mechanisms while exposing arguments for runtime adaptation. ReAct combines task-specific working memory, long-term experience memory, and visual feedback to select actions, verify outcomes, and recover from failures without modifying source code. RACaP achieves 54.4% success on LIBERO-90, 45.0% on zero-shot LIBERO-PRO, and 46.0% on LIBERO-Long, compared with at most 4.0% for CaP baselines on long-horizon tasks. On LIBERO-PRO, it achieves 2.5 times the success rate of CaP baselines and a 1.9-fold speedup in median policy time. For efficient on-robot deployment, rejection-sampled fine-tuning distills GPT-5.6 ReAct decisions into Qwen3-VL-8B-Instruct, yielding a 13.2-fold per-decision inference speedup and reducing repeated physical calls from 16 to 4. These results show that separating reusable code from runtime decisions supports continued evolution, effective transfer, and efficient long-horizon control.

### 10. Agent Memory with Episodic Retrieval for Financial Decision-Making
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-23T20:32:54+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.28771
- Summary: Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their applicability to the demands of trading in complicated settings. To address these gaps, we introduce META (Memory Enhanced Trading Agent), the first RAG-like episodic-memory-augmented multi-agent framework for financial decision making. META integrates a family of specialized indicator agents (e.g., Trend, MACD, Stochastic, RSI, SMA, AVWAP, Heikin-Ashi) with a Decision Agent that fuses their reports, and a Memory module that retrieves and updates past trading episodes encoded as market state embeddings with outcomes and reflections. By recalling relevant experiences and adaptively reweighting signals under similar market regimes, META achieves improved directional accuracy and robustness under short-horizon evaluation. Our results demonstrate that episodic memory provides a powerful mechanism for regime-aware, interpretable, and low-latency decision-making in trading and decision making. The code of this project is released on GitHub.

### 11. Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-21T01:43:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.23986
- Summary: Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \textbf{\method}, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6$\times$ speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.

### 12. EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T07:41:56+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15161
- Summary: Large language model (LLM) driven multi-agent systems have shown promise in complex clinical reasoning, yet existing approaches rely on static strategies and lack persistent clinical memory, preventing self-evolving from prior diagnostic successes and failures. We present EMR, a self-evolving medical multi-agent system via Experience Mining and Reuse. EMR introduces a hierarchical clinical experience library that organizes accumulated knowledge into three levels: clinical principles, diagnostic patterns, and representative cases. During inference, EMR emulates multidisciplinary consultation: a planner agent coordinates domain-specific department agents for specialized reasoning, while a summary agent synthesizes their analyses into a final decision. Critically, EMR automatically extracts correct diagnostic insights and failure-related warnings from multi-agent reasoning trajectories, incrementally updating the experience library to guide future cases. Experiments on medical reasoning benchmarks demonstrate that EMR consistently outperforms state-of-the-art medical multi-agent baselines. Further analysis reveals that the hierarchical experience enables cross-specialty generalization and transfer across diverse LLM backbones, offering a scalable and in

### 13. BusMA: A Bus Communication Substrate for Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T05:19:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15054
  - Alt: https://arxiv.org/abs/2610.01042
  - Alt: https://arxiv.org/abs/2610.00925
  - Alt: https://arxiv.org/abs/2609.39788
- Summary: Multi-Agent (MA) systems are effective at solving complex tasks that demand planning, tool use, and the synthesis of evidence from multiple sources. Existing systems typically adopt Hierarchical Manager-Worker (HMW) or Router-based Message Passing (RMP) structures as their communication protocol. However, these designs restrict agent autonomy: Worker agents cannot directly consult specific "peers", and misrouted messages can propagate errors. Inspired by bus architectures in computer systems, we propose BusMA, a communication framework that allows any agent to address other agents through a shared channel, i.e., the Bus. It consists of agent registration, message routing, and shared memory management components. Worker agents, each equipped with tools, have their own local memory and can reason, act (tool usage), and communicate by posting shared messages with specific intents. We introduce four intents: discussion, challenge, guidance, and request for explanation, which support fine-grained communication among agents. A Chair agent monitors the shared memory to coordinate interactions and facilitate convergence among Workers. To evaluate the effectiveness of BusMA, we conduct extensive experiments with two frontier LLMs across 13 tasks spanning visual reasoning, mathematical reasoning, and knowledge retrieval demonstrate that BusMA consistently outperforms state-of-the-art HMW and RMP methods.

### 14. Enhancing Human Mobility Prediction with Spatially Aware LLM-based Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-13T01:41:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.14227
  - Alt: https://arxiv.org/abs/2610.13144
- Summary: Predicting a user's next POI is a task in human mobility modeling, yet LLM-based approaches focus on semantic reasoning from previous mobility records, while neglecting real-world spatial context. However, human mobility is inherently shaped by spatial cognition, including geographic distance and neighborhood context. This issue is further compounded by prior evidence that LLMs often struggle with spatial reasoning tasks, including distance estimation and geographically biased prediction. To address these limitations, we propose our framework, a multi-agent LLM framework that decomposes next-POI prediction into three stages: Firstly, a Pattern Extraction Agent that captures temporal and categorical mobility patterns from trajectory history; Secondly, a Spatial Reasoning Agent that structures candidate activity choices by combining behavioral preferences with real-world spatial constraints, including geographic distance, road network distance, and neighborhood affiliation; and Thirdly, a Decision Synthesis Agent that integrates behavioral patterns and spatial reasoning for final prediction. Experiments on the NYC benchmark dataset with two LLM backbones show improvements over baseline methods, with up to 493% Hit@1 improvement and 37% relative improvement in Hit@5. Ablations show that combining neighborhood affiliation with distance-based features generally outperforms distance-only settings, and that the Spatial Reasoning Agent plays a crucial role in final prediction by integrating behavioral preferences with real-world spatial constraints, especially for smaller models. Overall, the results highlight the importance of spatial reasoning in mobility prediction. Accurate next-POI prediction requires combining behavioral patterns with explicit real-world spatial constraints, and multi-agent decomposition provides an effective structure for organizing these forms of context.

### 15. Towards Agentic Robots: Model, Data, Environment, and Harness
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-14T16:32:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.20442
- Summary: Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic environments, rectify execution errors autonomously, and dynamically adjust operational strategies. Although this field develops fast, current studies are not well connected. Researchers have no consistent view of how to combine different agentic functions into a complete robot system. This paper provides a unified overview of existing research on agentic robots. We first trace the development from robot policies to agentic systems, covering vision-language-action models, world models, and world-action models. We then clarify the definition and scope of agentic robots and organize existing research into seventeen categories across four functional domains: Model, Data, Environment, and Harness. Across these domains, we examine how agents shape model learning and robot decisions, collect and curate robot data, construct worlds, tasks, and tests for learning and evaluation, and organize capabilities for robot use. Finally, we discuss open challenges and outline directions for future research. Looking forward, we hope this work contributes to a clearer understanding of agentic robots and supports new approaches to making them more capable, reliable, and adaptive.

### 16. CLARA: Compound Library Active Learning with Reasoning Agents
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-12T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.05.756921
- Summary: Batch active learning for ligand discovery requires a recurring decision about whether to exploit high predicted affinity, reduce model uncertainty, or broaden chemical coverage. We test whether a language model can make this strategy-level decision while candidate ranking and label revelation remain controlled by a deterministic Gaussian-process environment. Across four protein targets, ten paired seeds, and a 360-compound assay budget, a GPT-5.6 Sol agent outperformed random sampling in all 40 matched campaigns. Its final top-2\% recall was 0.412 on D2R, 0.374 on Mpro, 0.448 on TYK2, and 0.683 on USP7. It was statistically tied with the strongest fixed policy on Mpro and USP7 but underperformed target-specific leaders on D2R and TYK2. The agent shifted from exploration-oriented early batches toward exploitation and produced 686 testable threshold claims with an 86.3\% atomic success rate, although 19.8\% of forecasts were not numerically scorable. In 200 prespecified information-ablation campaigns, removing uncertainty, diversity, or memory caused only small endpoint changes, while shuffling explanatory evidence reproduced the full allocation path in 39 of 40 paired campaigns. A deterministic 80\% availability constraint reduced recall on every target but preserved the target-dependent pattern of wins and losses. These results support language-model strategy control as a feasible and auditable layer.

### 17. Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-08T23:00:01+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.12793
- Summary: Pretrained vision-language-action (VLA) policies fail on memory tasks, behaviour that depends on events observed long before the current frame, because their training data is overwhelmingly Markov and mapping episodic memory directly to action chunks is hard. Yet the same policy, finetuned once to follow a privileged oracle's grounded-subgoal text, nearly solves these tasks: the difficulty lies entirely in mapping memory to a grounded symbolic subgoal. Existing work entrusts this stage to a single VLM that selects keyframes and reasons over raw frames, and falls far short of the oracle: key identities and dynamics are buried in noisy pixels, the reasoning spans hundreds of frames in an unbounded context, and hallucination corrupts the memory itself. We instead present GAMMA (Grounded multi-Agent Memory with Mechanical Audit), which builds the stage as a collaborating two-agent memory system: a detector tool (SAM-3) for spatial grounding, a VLM writer that distils each replan window into one grounded text line, an append-only text memory bank, and a VLM reasoner that reads the bank and emits the next grounded subgoal at the oracle's cadence, wrapped in a propose-verify harness that admits, defers, corrects, or rejects every agent claim against mechanical visual evidence, at training-corpus construction and at deployment alike. On a sixteen-task memory-manipulation suite GAMMA recovers a large fraction of the oracle ceiling with the policy held fixed, reaching the ceiling on several tasks, and transfers with unchanged contracts to a second benchmark.

### 18. iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-07T22:28:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.10962
- Summary: Agentic AI based on Large Language Model generalization capabilities offers a wide range of potential applications, including planning for embodied tasks. For example, embodied agents based on Foundation models can generate plausible plans in autonomous robotics scenarios. Due to limited context windows or hallucinatory phenomena in the next-token prediction formulation, behaviors may be generated without establishing whether the deployed robot and the observed environment actually support the requested operation, in what we call a "grounding failure". Thanks to the recent improvements in reasoning capabilities of foundation models, autonomous robot behavior generation problem can be formulated as a code generation problem. We present iAm.md, a Markdown standard and generation framework, that allows anchoring this process in complementary forms of deployment evidence. Through open-vocabulary semantic mapping, we combine local vision-language detections and object segmentation and refer them to persistent object records in this intermediate standardized representation, allowing agentic introspection. We then study this new technique on a simulated TIAGo, on navigation-and-manipulation tasks, showing how this standardized representation jointly supports skill self-assessment and executable task generalization.

### 19. Beyond Corrected Memory: Execution Consistency in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-06T10:29:41+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.08101
- Summary: Shared memory coordinates agents' actions, but correct records do not establish that those actions satisfy task requirements. Memory governance and failure diagnosis regulate or inspect recorded information; they do not by themselves establish whether it is sufficient to judge task duties. We define execution consistency through duties governing state use, information handoffs, and final-state agreement, with explicit evidence conditions for judging fulfillment. Our core claim is that identical retained records can correspond to compliant and violating executions under the same task rule. Controlled removal of evidence such as receipt, action dependence, or response validity leaves 82.4% of opposite-label pairs indistinguishable; restoration separates 97.9% of the merged pairs. Natural-log annotations identify the defined violations in actual executions. However, existing logs do not always explicitly represent the execution relationships needed for these judgments. To assess the definition's practical value, we use CAVERT, a framework for consistency diagnosis and recovery, to extract supported relationships from logs and apply these criteria. It consistently outperforms contract-prompted LLM and rule-based baselines in diagnosis across all 12 benchmark-executor settings. Under the same gate and executor limits, it also outperforms rule-guided recovery in all four evaluated environments. These findings identify execution evidence that agent-memory and execution interfaces should preserve for reliable judgment.

### 20. OOPMAS: Object-Oriented Multi-Agent Systems for Query-Level Workflow Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-06T05:31:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.07787
- Summary: Multi-agent systems (MAS) powered by large language models have shown strong performance across code generation, mathematical reasoning, and question answering. However, existing methods for automating MAS design mostly operate at the task level, producing a single fixed workflow per benchmark that is applied uniformly to all queries. This assumption fails under realistic conditions. Query difficulty varies widely within a task, and real-world workloads mix heterogeneous task types. We introduce OOPMAS, a training-free framework that generates both the agent set and the coordination workflow at the granularity of individual queries. Agents are represented as object-oriented class definitions with dedicated roles, tools, and persistent state, and workflows are expressed as executable main functions over these agent objects. A dynamic skill library accumulates structured lessons from execution feedback across optimization rounds, enabling in-context improvement without any gradient updates or fine-tuning. On a mixed-task benchmark of queries spanning code, math, and QA, OOPMAS achieves 89.6% accuracy, outperforming the strongest baseline by 18.1 percentage points. A model-swap study across four LLM backbones shows consistent scaling, reaching 92.4% with the strongest model.

### 21. EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-02T14:43:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.03394
- Summary: Emerging multi-agent LLMs demand privacy-preserving edge deployment, yet current inference systems struggle with these collaborative workflows. Specifically, the memory-bound decode phase causes severe bus contention on unified memory architectures (UMA), paralyzing naive CPU-GPU co-execution. Furthermore, speculative decoding in multi-agent workloads faces extreme variance in drafting difficulty, alternating between complex reasoning and predictable structured generation. Compounded by frequent tool-induced stalls, this highly fragmented execution severely underutilizes hardware and defeats traditional static batching. We present EdgeAgent, a cross-layer inference system explicitly co-designed for edge UMA and multi-agent workloads. At the micro-architectural level, it bypasses rigid graph-compiler constraints to enable zero-copy UMA-aware tensor parallelism, utilizing asymmetric memory layouts to fully saturate both CPU and GPU compute units. At the scheduling level, it dynamically allocates draft budgets based on real-time sequence predictability to bound bandwidth waste. Concurrently, an asynchronous suspend-and-yield mechanism actively evicts stalled agents, ensuring continuous hardware saturation during unpredictable tool invocations. Extensive evaluations on an Apple M4 SoC demonstrate that the UMA-aware execution alone contributes a 1.29x speedup over batched speculative decoding. Adding the agent-aware scheduling lifts the full EdgeAgent system to a 1.77x speedup under extreme tool-use latencies.

### 22. From Pixels to Policy: A Multi-Agent System for Intervention and Geo-Spatial Decision Support
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T15:29:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2610.01870
- Summary: Urban environments are shaped by design choices with long-term implications for health, safety, and quality of life, yet evaluating proposed interventions remains costly, time-consuming, and often impractical. Existing geospatial vision methods largely focus on monitoring urban indicators from aerial and street-view imagery, rather than proposing interventions and estimating their effects on such indicators. Moving beyond recognition, we introduce the problem of discovering interventions that improve target indicators for a given aerial or street-view image. We argue that a black-box indicator model, combined with a generative editing model, can serve as an implicit digital twin for testing intervention hypotheses. We present VIDA-Geo , a multi-agent system that explores this intervention space by coordinating segmentation, diffusion-based inpainting, and indicator scoring models to produce interventions that are both perceptually realistic and aligned with real-world policies. We evaluate our system on 8 indicators across aerial and street-view imagery, measuring changes in factors such as perceived safety and greenery. Our approach outperforms existing baselines in many cases, achieving up to 2X higher perceptual quality and policy alignment scores. Finally, our model provides users with multiple candidate interventions, supporting an expert city-planner-in-the-loop workflow.

### 23. MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T05:42:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, human augmentation / robotics
- URL: https://arxiv.org/abs/2610.01102
- Summary: Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control, decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward engineering or task-specific design. We propose MASkillBlender, a general multi-agent reinforcement learning framework to achieve decentralized multi-humanoid whole-body coordination. By learning a shared decentralized high-level policy over reusable pre-trained single-humanoid skills, MASkillBlender enables coordinated behaviors using only task-level rewards, without requiring task-specific motion references. To improve learning efficiency, we further introduce a permutation-based data augmentation strategy for homogeneous multi-humanoid systems, and theoretically show that the permuted samples preserve the policy-gradient direction of the original samples under the homogeneous Markov game formulation. We evaluate MASkillBlender on multiple multi-humanoid coordination tasks across two humanoid embodiments. Simulation results demonstrate that the proposed framework consistently achieves strong task performance and enables coordinated behaviors across different tasks and humanoid embodiments.

### 24. Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T23:36:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38660
- Summary: Long-form subtitle translation requires reasoning over discourse and cultural context spanning episodes or entire series, while maintaining consistent terminology and style. Existing single-LLM methods are largely sentence-level, and multi-agent systems often use static workflows that do not adapt to scene complexity or production context. We propose SMART, a Self-evolving Multi-Agent system for long-foRm subtitle Translation. During test-time training, SMART builds persistent series-level memory and translates a subset of sentences through a dynamic router and Mixture-of-Agents layer with tools for terminology verification, subtitle constraint validation, and contextual retrieval. A judge-refiner loop scores candidates and uses textual critiques to update agent prompts and routing policies without retraining the underlying LLMs. During test-time inference, the evolved configuration translates the remaining series. We also introduce Subtitle Arena, covering 14 genres, 2--198 episodes per series, production years 1959--2023, and 15 target locales, together with SubMQM, a subtitle-adapted MQM framework with seven dimensions and 19 error categories. SMART achieves the best overall MQM score in all 15 Subtitle Arena directions, reducing average penalty by 6.9% over the strongest competing agent system. On the public MuSC benchmark, SMART obtains the best model result across all four language pairs and also achieves the best human-evaluation result, with an overall score of 4.50/5.

### 25. PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T20:10:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38482
- Summary: Existing architectures for LLM-based multi-agent systems (MAS) cannot reliably and efficiently solve multi-step tasks at scale: they struggle to support large numbers of agents and concurrent tasks, tolerate failures, govern agent interactions, and accommodate the diverse planning and execution patterns different tasks require. We present PANDA, a decentralized architecture that connects a large collective of heterogeneous, independently administered agents, letting them discover each other's capabilities and self-organize into small specialized teams per task. PANDA scales by decoupling collective communication from team communication, allowing agents to participate in multiple teams simultaneously, load-balancing tasks across the collective, and scheduling concurrent work within each agent. PANDA further separates the underlying architecture from the orchestration strategy, supporting three planning and execution patterns (star, chain, and mesh) that can be selected according to the structure and requirements of each task. PANDA detects infrastructure and orchestration failures and recovers affected tasks by dynamically replanning around failed components. Finally, to provide governance without a centralized service that would limit scalability, PANDA uses a web-of-trust model to constrain agent interactions to established trust relationships. We evaluate PANDA on the HotPotQA benchmark, demonstrating that it scales to thousands of agents, assembles teams in milliseconds, matches state-of-the-art accuracy at up to 8x the efficiency, and sustains 100% task completion under faults where existing systems fail.

### 26. LLM-Based Multi-Agent Systems over Wireless Networks: A Joint Agent--Network Design Perspective
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T09:19:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.37094
- Summary: As large language models (LLMs) evolve from standalone models into collaborative agents embedded in physical systems, their reasoning and execution are increasingly distributed across wireless edge nodes. In this setting, wireless networks are experiencing a paradigm shift from only providing data connectivity to supporting the multi-agent reasoning workflow itself. The task performance of such network-constrained LLM-based multi-agent systems (MASs) is jointly affected by the multi-agent reasoning dependencies as well as the underlying network connectivity and edge resources. This coupling gives rise to various technical challenges, including the metric misalignment and message redundancy, state inconsistency and topology mismatch, as well as resource limitation and trust discontinuity. To address these challenges, this article develops a novel joint agent--network design perspective that coordinates decisions on both sides of the system. Specifically, we present the joint design of agent--interaction scheduling and resource allocation, the message selection-transmission co-design, as well as the joint agent--network topology design and workload--resource allocation. Furthermore, we consider the network-verified provenance that is linked with agent-side information-flow control to constrain how received information affects subsequent operations. An illustrative vehicle-to-everything (V2X) case study shows that jointly adapting agent-side interaction decisions and network operations improves task completion under communication and edge-resource constraints, outperforming the conventional agent-only and wireless-only separate designs.

### 27. Trajectory-Level Mode Guidance for Controllable Diffusion-Based Multi-Robot Motion Planning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T02:22:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36530
- Summary: Motion planning often admits multiple feasible solutions, making multimodal generation valuable, particularly for flexible multi-robot coordination. Diffusion models naturally learn such trajectory distributions, yet incorporating coarse and partial trajectory priors without restricting generation remains challenging. Such priors indicate a desirable region of the solution space rather than a single solution, motivating conditioned generation that preserves multimodality. In this paper, we guide trajectory generation in the clean trajectory space and progressively incorporate trajectory priors with a timestep-dependent guidance strength. At each reverse diffusion step, the reconstructed clean trajectory provides a unified space for integrating planning costs and partial trajectory priors. Planning costs are incorporated through gradient-based refinement, while the partial prior is progressively injected at the corresponding noise levels with decreasing guidance strength. This guides generation toward the prior in early stages while gradually releasing the constraint to preserve the inherent multimodality of the diffusion model. The framework naturally extends to multi-robot planning by incorporating inter-robot collision costs. Experiments on single- and multi-robot planning tasks demonstrate controllable trajectory synthesis, diverse feasible solutions, and safe multi-agent coordination.

### 28. SkillWeaver: Agentic Exploration over Neural Interaction Skills for Scalable Robot Data Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T19:41:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36171
- Summary: Large-scale demonstrations have driven unprecedented progress in robot learning, yet collecting robot data through teleoperation is expensive and difficult to scale to diverse environments and long-horizon tasks. Simulation offers a scalable alternative, but existing data-generation pipelines often rely on open-loop controllers, scripted skill sequences, or task-specific programs. We introduce SkillWeaver, an agentic framework that autonomously generates robot experience by exploring over Neural Interaction Skills (NIS): reusable, parameterized, closed-loop policies that expose learned physical interaction capabilities to a reasoning agent. Given a task and a simulated environment, a VLM agent reasons about what to do next, invokes and parameterizes NIS to interact with the environment, observes their outcomes, and generates verification, reflection, and memory to guide subsequent exploration. We instantiate NIS as reinforcement-learned policies for closed-loop, contact-rich manipulation and organize exploration as verifier-guided tree search, enabling the agent to discover successful long-horizon behaviors without relying on predetermined execution pipelines. SkillWeaver scales autonomously to 39.1K demonstrations across 14.1K scenes, which we distill into visuomotor policies. Across simulation benchmarks and real-world manipulation, training on SkillWeaver-generated experience substantially improves generalization to novel objects, spatial configurations, tasks, and environments, and enables zero- and few-shot sim-to-sim and sim-to-real transfer. Our results suggest agentic exploration over neural interaction skills as a scalable alternative for robot data generation.

### 29. Memory in the Sky: Low-Altitude Question Answering with Multi-Agent Memory Aggregation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T15:36:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.35431
- Summary: This paper studies low-altitude question answering (LAQA), in which distributed unmanned aerial vehicle (UAV) memories are aggregated at a ground server to answer questions about observations over a long horizon. Unlike conventional resource allocation based on sensing, communication, control, or computation metrics, LAQA requires an explicit measure of memory value. We propose a generative adversarial exam (GAE) that uses forward simulation to evaluate memory retrieval and exam scores to quantify memory quality. This enables the downstream QA value of candidate memories to be measured and optimized without accessing the internal mechanisms of the black-box captioning, retrieval, and reasoning pipeline. Building on this metric, we develop a memory-centric (MemCen) framework that jointly selects UAVs and allocates transmit power to maximize memory quality under communication constraints. In the noise-limited regime, we derive a QoM-aware capped water-filling law that explicitly connects task utility with physical-layer power allocation. We further develop penalty successive optimization (PSO) and learning to memorize (L2M) solvers. MemCen achieves QA accuracies of 92.4% and 84.0% in CARLA Town04 and Town05 under static and dynamic communication conditions, respectively. In real-world experiments, MemCen achieves 88.5% QA accuracy on the panoramic multi-agent system (PMAS) benchmark. Finally, UAV-to-robot-dog demonstrations further validate the practical utility of the acquired memories for environmental understanding and navigation.

### 30. Recent Advances in Agentic Agri-Robotic Phenotyping: A Perspective Review from Fragmented Multimodal Sensing to Unified PhenoAgent Intelligence
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T08:18:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.34567
- Summary: This review examines the evolution of plant phenotyping from conventional manual trait measurement to high-throughput, robotic, and artificial intelligence-driven crop monitoring. Despite significant advances in imaging, autonomous platforms, multimodal sensing, and deep learning, current phenotyping systems remain fragmented across sensing modalities, crop traits, growth stages, environments, and management objectives. We therefore frame phenotyping as an integrated \emph{seed-soil-plant-environment-management} (SSPEM) intelligence problem, where crop performance reflects interactions among seed quality, root-zone conditions, plant development, environmental exposure, and management actions. The review synthesizes conventional, high-throughput, robotic, and AI-driven phenotyping approaches, highlighting their capabilities and persistent limitations in temporal integration, multimodal reasoning, biological interpretation, and actionable decision support. Building on this analysis, we introduce a conceptual PhenoAgent framework that extends phenotyping beyond the estimation of isolated traits to evidence-based crop-state interpretation, uncertainty-aware reasoning, and management-oriented support. The PhenoAgent concept primarily brings together scattered advances in phenotyping to deliver insights ranging from detailed to high-level, such as what is happening in the crop, why it might be occurring, what evidence is missing, and what actions or additional measurements should be considered. We also discuss challenges in dataset scarcity, annotation, benchmarking, model generalization, and explainability. By linking multimodal phenotyping with agentic AI and closed-loop decision support, this review outlines a path to interpretable, scalable, and deployment-oriented crop intelligence.
