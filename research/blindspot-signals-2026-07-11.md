# Blindspot Signals Report - 2026-07-11

- Source export: `/opt/apps/haier/exports/evolution_signals_20260711_020536.json`
- Total signals in export: 5000
- Agent-relevant signals: 606
- Novel vs previous reports: 481
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`

## New Signals Since Previous Reports

### 1. Choosing the Right AI Agent Memory Strategy: A Decision-Tree Approach
- Deep score: 0.2
- Date: 2026-07-11T00:43:39+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://machinelearningmastery.com/choosing-the-right-ai-agent-memory-strategy-a-decision-tree-approach/
- Summary: No summary.

### 2. Introducing Oracle Autonomous AI Database A2A Server for Governed Multi-Agent Systems - Oracle Blogs
- Deep score: 0.2
- Date: 2026-07-07T21:56:50+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMixAFBVV95cUxNNWEzeEVaT281Qks1Q0pLTU4tbE44NmNIVV9tMjQxTGNENHROOTFCQjVjSWRLV0Viak4yLXdyOEtLbTBvM1VYX0JrLVJiUTIwVXlYdFNlcXdkano4ZFA3NjB1b1J4RklTUjNUcDViRTVTZUt2MlVQNDN1TC10Q1lLdEdkWmVLdTJjckZhOFFteVo2WkwtRERTMjU4VXBQWU9seWYtRXM2a3NocUlDSEllckViQ2hCQ3VxMTRydVE2VTFpSUh3?oc=5
- Summary: Introducing Oracle Autonomous AI Database A2A Server for Governed Multi-Agent Systems&nbsp;&nbsp;Oracle Blogs

### 3. When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-07-07T21:12:27+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.06807
- Summary: While enabling effective collaboration on complex tasks, LLM-based Multi-Agent Systems (MAS) face critical security challenges due to vulnerabilities at the agent and interaction levels. Most existing MAS security defenses are built upon two core assumptions: semantically-explicit malicious attacks and explicit graph-based modeling of the MAS topology and agent-level interactions. In practice, real-world attacks are becoming more semantically stealthy, while MAS execution is typically asynchronous without the temporal alignment assumed by graph-based propagation models. To address these limitations, we propose AcMAS, an activation-based framework for malicious-behavior detection in MAS. By analyzing internal reasoning states in the activation space of local agents, AcMAS detects even stealthy attacks in a synchronization-robust fashion, without relying on explicit interaction graphs. Moreover, our activation analysis provides critical signals to guide AcMAS in restoring the functionality of compromised agents, rather than the disruptive agent isolation commonly used by the state-of-the-art methods. Comprehensive evaluation demonstrates that AcMAS significantly outperforms graph-based baselines against stealthy attacks, by +0.22 F1 in synchronous settings (0.94 vs. 0.72) and by +0.55 F1 in asynchronous settings (0.93 vs. 0.38), with generalization across diverse open-source LLM backbones, attack intensity, and MAS scale.

### 4. StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-07-07T05:06:33+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.05844
- Summary: Agent systems accumulate conflicting observations across branches, retries, and replicas, yet many practical memory layers still collapse disagreement behind overwrite rules that are difficult to inspect or correct. We present StateFuse, a conflict-aware replicated memory contract built on standard OpSet/CRDT merge. StateFuse does not introduce a new join algebra; it defines an agent-facing semantics layer with immutable history, explicit conflict objects, exact and semantic correction handles (claim_id / claim_ref), deterministic predicate contracts, and projection-time resolution that cannot rewrite replicated state. We evaluate StateFuse against flat multi-value, raw-log, provenance-style, and collapsed baselines under matched resolver and verification policies. On a 282-question official conflict-bearing MemoryAgentBench slice, the compared methods tie on answer accuracy, but conflict-preserving surfaces keep contradictions visible while collapsed surfaces do not. In a controlled agent loop with uniform verification, preserving ambiguity enables safer abstention and correction than early collapse. A correction-handle ablation further shows that semantic handles matter when exact prior identifiers are unavailable. The resulting claim is narrow: StateFuse is best supported as a safer public memory contract for contradiction surfacing, abstention, and auditable correction, not as a universal accuracy gain.

### 5. When AI Agents Attack: Autonomous Cyber Operations and Europe’s Governance Gap - Carnegie Endowment for International Peace
- Deep score: 0.2
- Date: 2026-07-06T22:17:06+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiwAFBVV95cUxNRjNxNmcxQXE4anJQX1Jsemx0akk2RXR3YTNidnlXZnBUSVFkZ3BSQy12MHdqRW82WHUxcTZoS29NT3lPM3RQLUpSdVkxSVhTZmV1RTBvSXhLaV9zNDFPU19JNGdBdVJmMm1GMjJYTm1ndnprUUVaYkFpUHR3MFYzM3BQR21MY3V2Snpla1dJeWhYY3FSU2YxUHhPX2lZRHotS2ZQbXlxWTRKYkhaSUlzTmdjWFJ5RVJMZVo0NWF6WUM?oc=5
- Summary: When AI Agents Attack: Autonomous Cyber Operations and Europe’s Governance Gap&nbsp;&nbsp;Carnegie Endowment for International Peace

### 6. OthmanAdi / planning with files
- Deep score: 0.2
- Date: 2026-07-06T02:01:45.718108+00:00
- Source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/OthmanAdi/planning-with-files
- Summary: Persistent file-based planning for AI coding agents and long-running agentic tasks. Crash-proof markdown plans that survive context loss and /clear, plus a deterministic completion gate and multi-agent shared state on disk. Manus-style. Works with Claude Code, Codex CLI, Cursor, Kiro, OpenCode and 60+ agents via the SKILL.md standard.

### 7. Nuggets, Innovation Labs advance governance for autonomous AI agents - Biometric Update
- Deep score: 0.2
- Date: 2026-07-03T20:25:00+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiqgFBVV95cUxQTTdNT1Zpc1hyQjQtVTc0NnFpOXNRSllSYmNzbzlTeHllQ1pNUmVzVHJjQWdhWWk1bXUzcURIRjdwLW8tZlJ5OC1feVRiYThFZF85SnNLQ2t4eWlxRUdPWExQQUFiaWYtVmVtUkNOblNVenlZcnI3ZTVHMGJ6NmNfanlaMXlTN19sSGI5WmpReVNsajEyVmFkR1BWR3hsUi1qSU1Ub3Y3cGZ6UQ?oc=5
- Summary: Nuggets, Innovation Labs advance governance for autonomous AI agents&nbsp;&nbsp;Biometric Update

### 8. Cache Merging as a Convergent Replicated State for Multi-Agent Latent Reasoning
- Deep score: 0.2
- Date: 2026-07-03T14:12:38+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.01308
- Summary: No summary.

### 9. Consensus-Breaking Global Hopf Bifurcation in Memory-Based Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-07-02T16:24:42+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.02388
- Summary: This dissertation provides the first systematic study of symmetric consensus-breaking bifurcation to periodic multiconsensus in multi-agent systems. It analyzes this for three classes of multi-agent systems based on three different types of memory, whose closed-loop dynamics equations form delay differential equations of retarded type, neutral type, and pseudoneutral type - a subclassification of retarded type equations introduced in this dissertation which bridges retarded and neutral type delay equations. Equivariant twisted degree is used to analyze the symmetric global Hopf bifurcation problem in these systems, i.e. bifurcation from a stable consensus to periodic multiconsensus. This shows how the effects of memory allow self-organizing agents to move beyond mere stationary consensus. Theoretical results for the global Hopf bifurcation and symmetric classification of periodic multiconsensus solutions across all three systems are provided, and numerical results are conducted to both validate and enhance the theoretical predictions by providing stability information on the branches which is not obtainable by the degree alone. These principles are demonstrated in three real-world applications: one involving the control of formations of UAVs, allowing them to maintain their overall spatial relationships while dancing in complex selectable oscillations; and two more in networked asset markets featuring different traders with different memory-based strategies, showing how similar mechanisms can be responsible for economic cycles of bubbles and crashes. Finally, we also numerically investigate resonant double Hopf bifurcations in the neutral delay system, showing strong evidence of a breakdown to chaos via the Ruelle-Takens-Newhouse scenario and the existence of riddled basins.

### 10. A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory
- Deep score: 0.2
- Date: 2026-07-02T09:28:29+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.01935
- Summary: Long term memory lets LLM agents act as persistent assistants, but user facts change. A useful memory system must know what is true now, what used to be true, and what changed. We study \emph{ghost memory}, a state coordination failure in which old, current, and transition facts coexist in the memory bank, remain mixed during retrieval, and mislead the answer model. We argue that memory systems should be understood and optimized from three levels: bank maintenance, retrieval, and answer time resolution. We propose ATMA, a state aware overlay for existing memory systems. ATMA keeps superseded and transition records in the bank, builds evidence packets for the query's requested state view, and exposes current, historical, and transition labels to QA. We further call for decoupled evaluation of bank, retrieval, and answer level failures, since final QA accuracy can hide where ghost memory occurs. To make this failure measurable, we build LTP (LoCoMo Temporal Plus), a conflict heavy benchmark for ghost memory, and evaluate on LoCoMo for long conversation generalization. On LTP, Graphiti+ATMA improves conflict accuracy by 0.240 absolute over Graphiti. On LoCoMo, Graphiti+ATMA raises temporal F1 from 0.0295 to 0.1705. The gains are host dependent, but they indicate that explicit state roles can reduce memory failures hidden by final QA accuracy.

### 11. Robots Ask the Way: Communication-Enabled Social Navigation
- Deep score: 0.2
- Date: 2026-07-01T15:07:40+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.01044
- Summary: Assistive autonomous robots operating in multi-agent environments require efficient strategies to locate specific individuals among multiple residents. Current social navigation methods focus on reactive collision avoidance and trajectory adaptation, but lack mechanisms to proactively gather information through human-robot communication. We introduce Communication-enabled Social Navigation (CommNav). In this novel task, robotic agents actively seek assistance from residents to locate target individuals by requesting information about recent sightings, locations, and movements. To evaluate CommNav, we extend Habitat 3.0 to create Habitat 3.0c, a communication-enabled variant supporting multi-human environments with information exchange protocols. Adding our communication module (COMM) to a state-of-the-art social navigation model yields a 10 percentage-point improvement in Episode Success. We further investigate the transition from structured data to natural language by evaluating models trained on LLM-generated instructions and on colloquial instructions collected from a human study. Our experiments reveal that: (i) explicit human-robot communication substantially enhances multi-person navigation performance; (ii) pre-training COMM on a communication pretext task effectively addresses the challenge of occasional interaction signals; and (iii) the navigation policy is highly robust to natural, colloquial human language, achieving an episode success statistically similar to the model using perfect structured data.

### 12. ASPIRE: Agentic /Skills Discovery for Robotics
- Deep score: 0.2
- Date: 2026-06-30T23:38:46+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.00272
- Summary: Traditional robot programming is challenging: it requires orchestrating multimodal perception, managing physical contact dynamics, and handling diverse configurations and execution failures. We introduce ASPIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. ASPIRE discovers skills that persist across tasks, simulation and real-world settings, and embodiments. It operates in an open-ended loop with three components: (1) a closed-loop robot execution engine that exposes fine-grained multimodal traces, enabling autonomous failure diagnosis, repair synthesis, and validation; (2) a continually expanding skill library that distills validated fixes into reusable, transferable knowledge; and (3) evolutionary search that generates diverse task sequences and control programs to explore beyond single-trajectory refinement. ASPIRE surpasses prior methods by up to 77% on LIBERO-Pro manipulation under perturbation, 72% on Robosuite bimanual handover, and 32% on BEHAVIOR-1K long-horizon household tasks. Its accumulated library also enables zero-shot generalization to unseen long-horizon tasks: on LIBERO-Pro Long, ASPIRE achieves 31% success versus 4% for prior methods despite their use of test-time reasoning and retries. Finally, simulation-discovered skills provide initial evidence of sim-to-real transfer, substantially reducing real-robot programming effort across different embodiments and robot APIs.

### 13. Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping
- Deep score: 0.2
- Date: 2026-06-30T06:30:22+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.31200
- Summary: Generalizable robotic grasping in cluttered environments is essential for deploying manipulators in unstructured human spaces, yet existing VLM-based methods rely on visual similarity for object matching, neglecting physical affordances such as handle graspability and material fragility, and operate open-loop without spatial reasoning or failure recovery, limiting their effectiveness when objects are densely packed or physically diverse. We present Agentic RAG-VLM, a unified framework that bridges VLM-based semantic understanding and physically grounded grasp execution by integrating retrieval-augmented generation (RAG) with vision-language models (VLMs) and agentic self-reflective planning. Agentic RAG-VLM introduces three tightly coupled components: (1) a Hierarchical Affordance-Aware RAG (HAA-RAG) that encodes four-dimensional affordance descriptors, including type, material, fragility, and graspable region, and retrieves strategies by functional affordance compatibility rather than visual appearance; (2) a Scene Graph Constraint Reasoner that constructs spatial relationship graphs from VLM perception and translates proximity, occlusion, and support constraints into concrete grasp parameter adjustments; and (3) an Agentic Self-Reflective Pipeline with a 14-type failure taxonomy and three-level adaptive retry for closed-loop grasp refinement. Evaluated on a 12-task benchmark spanning single-grasp, interactive, and long-horizon scenarios with 360 trials per configuration, Agentic RAG-VLM achieves 78.3 percent overall success, a 53.3 percentage-point absolute gain over VLM-only baselines, demonstrating that affordance-aware retrieval, scene graph reasoning, and agentic recovery are jointly essential for robust manipulation.

### 14. GeneBench-Pro: Evaluating Multistage Statistical Reasoning\\in Genomics, Quantitative Biology, and Translational Biomedicine
- Deep score: 0.2
- Date: 2026-06-30T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.06.29.735386
- Summary: We introduce GeneBench-Pro, an expanded and improved version of GeneBench that comprises harder problems across a wider breadth of domains. GeneBench-Pro is a benchmark for AI agents performing realistic multi-stage scientific analyses in genomics, quantitative biology, and translational biomedicine which seeks to capture the complexity of real-world problems that computational life scientists face when tasked with producing a conclusion upon which a downstream scientific or translational decision is contingent. The benchmark comprises 129 evaluations targeting quantities of direct practical relevance across 10 primary domains and 21 terminal subdomains, with a genomics-centered core. Similarly to GeneBench, each problem provides the agent with brief context, a target estimand, and minimal guidance otherwise; the agent must then navigate multiple dependent decision points; i.e., substantive inferential forks where a plausible wrong choice changes the downstream analysis, to identify and execute the correct analysis workflow and arrive at the correct answer. Relative to GeneBench, GeneBench-Pro adds 29 new problems, drops three, and introduces significantly redesigned versions of 54 of the remaining 100 overlapping problems. 82 of the 129 problems were reviewed by external domain experts, whose findings led to prompt/data modifications and redesign of those problems whose targets were not sufficiently identifiable. Ten externally reviewed problems are released publicly, 50 held-out problems were provided to Artificial Analysis for independent third-party model benchmarking, and the remainder are retained as an internal holdout. In evaluations over the full 129-problem suite, GPT-5.6 Sol reaches an eval-level pass rate of 28.7% at the max reasoning level, and GPT-5.6 Sol Pro reaches 31.5% in separately reported GPT Pro runs. GPT-5.5 reaches 12.0%, GPT-5.4 reaches 8.9%, and the strongest non-GPT baseline, Claude Opus 4.8, reaches 16.0%. As with GeneBench, models often …

### 15. Sampling-Based Coordination-Informed Multi-Objective Multi-Robot Reinforcement Learning
- Deep score: 0.2
- Date: 2026-06-29T20:31:03+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.30893
- Summary: Multi-robot systems must simultaneously optimize competing objectives while maintaining coordinated behavior. Existing multi-agent reinforcement learning approaches often rely on fixed or centralized coordination, which limits adaptability and violates distributed constraints. This work introduces the Coordination-Informed Multi-Objective Reinforcement Learning (CIMORL) framework, integrating a distributed weight prediction mechanism, a privileged expert training strategy, and theoretical guarantees for Pareto-optimal solutions. We present the base CIMORL method alongside two sampling-based variants, CIMORL-TS (Tree Search) and CIMORL-MPPI (MPPI), which leverage privileged global information during training to enable fully decentralized deployment. Experimental validation in cooperative and adversarial scenarios demonstrates a $21.2\%$ hypervolume improvement and superior policy stability compared to state-of-the-art baselines. Real-world experiments with Crazyflie drones further validate the framework's robustness in resource allocation and multi-attacker multi-defend scenarios under partial observability.

### 16. Training Therapeutic Judges and Multi-Agent Systems for Human-Aligned Mental Health Support
- Deep score: 0.2
- Date: 2026-06-29T20:22:25+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.30887
- Summary: Large language models show promise for mental health support, yet therapeutic quality improves only when evaluation functions as an actionable control signal rather than a passive metric. We introduce a framework that formulates therapeutic response generation as a decision-refinement problem driven by multi-dimensional, human-aligned evaluation. In Stage I, we introduce TheraJudge, an open-source therapeutic evaluator trained via preference-based optimization on human-annotated data to produce reliable judgments across 7 psychological dimensions. In Stage II, we introduce TheraAgent, which operationalizes TheraJudge's evaluations through a coordinated refinement process with specialized Critic, Coach, and Therapist roles that translate evaluative signals into targeted response revisions. Empirically, TheraJudge achieves strong agreement with clinician ratings, with intraclass correlation coefficients (ICC = 0.87-0.95), surpassing supervised baselines and strong closed-source judges, particularly on critical dimensions such as Safety, Relevance, and Empathy. Acting on these evaluations, TheraAgent yields a +0.43 improvement in human-rated therapeutic quality (on a 5-point scale) under blind evaluation, with 96\% clinician inter-rater reliability. Low-quality responses ($\leq 3$) improve by +2.45 points with a 94\% recovery rate, demonstrating targeted correction of unsafe outputs. Overall, our results indicate that effective alignment of mental-health LLMs stems from acting on human-aligned evaluation, rather than relying solely on stronger generation. We release code at https://github.com/vis-nlp/TheraAlign.

### 17. MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-06-29T17:40:45+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.30602
- Summary: Multi-agent systems (MAS) are increasingly used to automate complex, distributed workflows. However, their inter-agent communication channels introduce new attack surfaces that remain poorly understood and are difficult to defend against. In this paper, we address how defenders should prioritize limited security effort to protect vulnerable communication channels before attacks are observed. This is motivated by our observation that the channel-level attack impact is highly non-uniform: a single compromised edge can account for up to 75% of total attack success. We introduce Mesa, a label-free framework for proactively ranking which MAS edges are most security-critical -- that is, most likely to affect the system's decision if compromised. Mesa combines six graph-theoretic metrics and two dynamic probes (ablation and masking) without requiring attack traces. We evaluate Mesa against a dynamic misinformation attack pipeline across three diverse MAS scenarios, eight network topologies, and five open-source LLMs from Qwen, Llama, and Gemma families. Mesa rankings correlate strongly with empirical per-edge attack success rate, achieving mean Spearman $ρ=+0.60$ (peaking at $+0.73$). In resource-constrained defense deployment, monitoring the top 10% of Mesa-ranked edges intercepts about 3x the successful attacks as random allocation. We further test Mesa under varying attacker and defender models and LangGraph workflows and characterize its limits under adaptive attacks and high-redundancy graphs. Overall, our results show that edge-level risk in MAS is often concentrated and predictable, allowing proactive hardening of multi-agent infrastructures.

### 18. Understanding LLM Intervention Explanations in Multi-Party Human-Robot Interaction
- Deep score: 0.2
- Date: 2026-06-28T15:30:15+00:00
- Source: arxiv
- Focus/tech: robotics, AI decision delegation / robotics
- URL: https://arxiv.org/abs/2606.29460
- Summary: Large Language Models (LLMs) are increasingly embedded in social robots to support natural group interactions, yet their role in complex multi-party settings remains underexplored. In particular, it is unclear how LLM-driven robots decide when and why to intervene in group conversations. This paper investigates the intervention explanations generated by an LLM-based orchestrator in a multi-party interaction involving three human participants and two robots. We conducted a between-subjects study with 24 groups (66 university students), comparing a homogeneous condition (two robots with the same role, i.e., a mover) and a heterogeneous condition (two robots with different roles, i.e., a mover and an opposer). At each conversational turn, the LLM orchestrator decided whether to intervene and generated a textual explanation of its decision. We performed a thematic analysis of 610 intervention explanations, identifying five recurring themes. Results show that explanations are facilitation-oriented, emphasizing agreement, participation, and interaction flow. While patterns remain stable across conditions, role differentiation emerges: the mover supports coordination, whereas the opposer drives goal-oriented interventions. These findings contribute to explainable AI by characterizing how LLM-driven systems justify intervention decisions in real-time, multi-party human-robot interaction.

### 19. GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-06-26T15:32:33+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.28187
- Summary: Multi-agent systems (MAS) built on large language models (LLMs) provide a promising framework for solving complex tasks through role specialization and structured interaction. However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents. Existing approaches typically rely on coarse-grained feedback, making it difficult to identify which agents or interaction steps are responsible for errors. We propose Gradient-Based Connections (GBC), an approach for fine-grained attribution and optimization of multi-agent systems. GBC models a MAS as a computational graph and introduces gradient-based connection weights to quantify the influence of each agent's output on downstream agents at the token level. By constructing an attribution graph and propagating task-specific loss signals backward, our method enables precise identification of error sources and targeted prompt optimization. We further develop AgentChord, an efficient implementation that leverages prefix-based gradient computation. Experiments on MultiWOZ and τ-bench show that GBC improves multi-agent performance and outperforms strong single-agent and multi-agent baselines, and higher attribution quality is associated with greater optimization effectiveness. Code is available at: https://github.com/yxc-cyber/AgentChord.

### 20. When Multi-Robot Systems Meet Agentic AI:Towards Embodied Collective Intelligence
- Deep score: 0.2
- Date: 2026-06-26T10:21:52+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.27929
- Summary: Embodied AI is increasingly becoming agentic, shifting robots from perception--control pipelines towards closed-loop systems that can retrieve context, deliberate during execution, monitor feedback, and refine future behavior. In parallel, robotics research has also moved from single-robot autonomy towards multi-robot systems, driven by the need for wider sensing, distributed action, heterogeneous capabilities, and fault tolerance. As AI agents move from single-agent use towards multi-agent collaboration, robotics faces a parallel challenge: robot teams must move beyond sharing maps, task assignments, and datasets towards sharing the state produced by embodied agent loops. This article explores Embodied Collective Intelligence (ECI), a future multi-robot paradigm in which a robot team accumulates and uses world context, task progress, and skill experience as shared resources. Specifically, we first review how embodied AI is becoming agentic and how multi-robot cooperation has evolved. We then present Embodied Collective Intelligence through Co-Perception, Co-Action, and Co-Evolution. Finally, we use an illustrative navigation study to examine one concrete component of the concept: shared world-memory inheritance. The study shows that a newly added robot can benefit from merged team memory, but it is not intended as a full evaluation of the ECI framework. Taken together, the review and conceptual framework motivate Embodied Collective Intelligence as a direction for embodied multi-agent intelligence, while the case study grounds one measurable part of the concept.

### 21. QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-06-25T19:16:51+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.27492
- Summary: Large language model (LLM) multi-agent systems increasingly depend not only on how individual agents reason, but also on how agents are connected. This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. A pool of worker agents, the task adapter, and the scoring function are frozen; only an outer LLM planner learns to generate temporal communication DAGs specifying who sends information to whom, in which round, who merges messages, and who emits the final answer. Execution traces are distilled into evidence-backed design rules with three actions: \emph{Preserve}, \emph{Modify}, and \emph{Avoid}. To prevent self-evolution from turning lucky runs or plausible but false explanations into policy, QueenBee uses held-out acceptance gates, variance-aware credit, motif-level attribution, transfer trust, insight falsification, and structural deduplication. We evaluate the method on Count-Frequency aggregation and Silo-Bench-style distributed coordination tasks. With fixed workers, self-evolved graph generation produces communication structures that improve over fixed topologies and cold generation. In the CF fulltest setting, the best generated graph reduces RMSE from 12.53 for the strongest fixed topology to 7.87 while also reducing messages, model calls, and token cost; Silo-style results show the same direction of improvement over cold and fixed-topology baselines. These results suggest that multi-agent systems can learn reusable architectural design knowledge rather than merely memorizing task answers.

### 22. Qwen-Image-Agent: Bridging the Context Gap in Real-World Image Generation
- Deep score: 0.2
- Date: 2026-06-25T00:00:00+00:00
- Source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2606.26907
- Summary: While text-to-image (T2I) models have achieved remarkable progress, they struggle with real-world requests that are often underspecified, implicit, or dependent on up-to-date knowledge. We identify this challenge as the Context Gap: the mismatch between the user context and the sufficient generation context for T2I models. To bridge this gap, we propose Qwen-Image-Agent, a unified agentic framework that integrates plan, reason, search, memory and feedback in a context-centric manner. Qwen-Image-Agent treats user input as partial context and progressively constructs the generation context through Context-Aware Planning and Context Grounding. Specifically, Context-Aware Planning identifies missing context and plans how it should be acquired and used, while Context Grounding gathers this context from reason, search, memory, and feedback. To evaluate agentic image generation, we further introduce Image Agent Bench (IA-Bench), a benchmark covering four core image agent capabilities: Plan, Reason, Search, and Memory. Experiments on IA-Bench, Mindbench and WISE-Verified show that Qwen-Image-Agent outperforms strong baselines and achieves state-of-the-art performance.

### 23. RBI proposes AI governance framework for banks, mandates human oversight of model driven decisions - BFSI News
- Deep score: 0.2
- Date: 2026-06-24T14:15:50+00:00
- Source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMizgFBVV95cUxNYXl2cmxtc2ZuQmlEQ1lOWnJnS3AtclRVT19TQWlUTWRRM0pUQ0YyOGVBZm5JWDZqWGNPN3AyWlZyUEdQNW5NUzh5aHZRZmEtaWp4NDhUS2pPdkZIdW8wcDRrM0g3ZkgyNmpxbUlMc3puVnVhLUV2QzNmQ2RrSzRrZzloY0k3Z1dNZjNaY2UwNFRMdkplVUF5WWRpbkJjRFJYdjRhd0lJa1RKQkFHQ3FPZGlEMGQ2cG0wVXNqc1B4UFo2UThvNkdsQWRxR2R6d9IB0wFBVV95cUxQZzY2aGxWYVdzWkpMTk9DaHBjSkJOcTNHLUxxV1hDaVN4dUVYd1ZtMVRUZVVVcllhaFYtRkZMU1k1OFF6eEFKV2p1SHB5WFZDYUQ2azBDanVpTFlfNHVKdXJQaUc2M2NWdV9yUXhJUWxtZHM2TUN1V1otVHkzaUpFcDg0ZFhMczM1VU5EUFBLVWtsYlotWUVoUjZpNjNMekxYLXN5ZlhPLXB5R1lDUGRtYlRXTElqRlBleGdZMmNralBIQUtaUHZwRHFBaGk0aGJ5NTVr?oc=5
- Summary: RBI proposes AI governance framework for banks, mandates human oversight of model driven decisions&nbsp;&nbsp;BFSI News

### 24. MedGuards: Multi-Agent System for Reliable Medical Error Detection and Correction
- Deep score: 0.2
- Date: 2026-06-24T10:07:59+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.25651
- Summary: As Large Language Models (LLMs) are increasingly deployed in healthcare settings, accurate error detection and correction in generated or existing text becomes critical, as even minor mistakes can pose risks to patient safety. Existing methods for error detection and correction, including automated checks and heuristic-based approaches, do not generalize well across unseen datasets. In this paper, we propose MedGuards as a medical safety guardrail, which is a new framework that treats medical error detection and correction as a multi-agent in-context learning task. Specialized agents separately detect, localize, and correct errors, while a confidence-guided arbitration mechanism resolves disagreements using reasoning traces and confidence scores. This design enhances interpretability, robustness, and adaptability, without requiring additional training of the base LLMs. Additionally, we introduce the Keyword-Prioritized Correction Score (KPCS), a new evaluation metric that considers whether critical keywords within the reference text are generated correctly, providing a more comprehensive assessment than conventional metrics. Experiments across four multilingual medical datasets consisting of clinical notes demonstrate significant improvements by the proposed framework across several metrics and models. Our aim is to enable safer deployment of LLMs in real-world healthcare applications. For reproducibility, we make our code publicly available at https://github.com/congboma/MedErrBench.

### 25. Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz
- Deep score: 0.2
- Date: 2026-06-24T09:31:06+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.25622
- Summary: The NIS-2 Directive mandates robust Risk Management from thousands of small and medium enterprises. To ensure compliance, companies rely on established standards such as the German IT-Grundschutz (IT-GS) of the Federal Office for Information Security. However, IT-GS certification is resource-intensive and requires a high level of manual effort for documentation, validation, and revision, making scalable implementation difficult and expensive. Building upon our previous conceptual framework, this paper presents the technical implementation and empirical evaluation of a Multi-Agent System (MAS) architecture combined with Hybrid Retrieval Augmented Generation (HybridRAG) for the partial automation of IT-GS certification. We introduce two novel technical contributions to the MAS architecture to enforce the compliance rigor. The Hypothesis-Verification Loop in the Structural Analysis (SA) phase that cross-references agent-inferred dependencies against the Knowledge Graph to reduce hallucinations, and a Decoupled Reasoning Pipeline that separates agent-driven semantic extraction from the deterministic protection need inheritance. We utilize the BSI's "RecPlast GmbH" case study as a human expert-generated reference data set for end-to-end evaluation of the architecture and to quantify Precision, Recall, and F1-scores. The performance of the system is investigated across the phases of SA, Protection Needs Assessment (PNA), Modeling, and IT-GS Check. The empirical results reveal noticeable differences throughout the different steps of IT-GS. While the MAS demonstrates high efficacy in semantic tasks (SA and Modeling), significantly reducing manual effort through automated information extraction, quantitative results reveal limitations in logical reasoning phases (PNA and IT-GS Check) as the probabilistic nature of current LLMs struggles to meet the deterministic rigor required by IT-GS.

### 26. Varying Bundle Size Reactive Multi-Task Assignment using Selective Cost Estimation for Multi-Agent Systems
- Deep score: 0.2
- Date: 2026-06-23T11:55:20+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.24462
- Summary: This paper presents a scalable framework for multi-robot task allocation in complex environments where estimating task execution costs is computationally expensive. While combinatorial auction-based approaches offer reliable solutions, the exponential complexity of bundle generation typically renders them intractable for real-time reactive applications, particularly when accurate path planning is required for cost validation. We address this through a distributed, two-stage multi-fidelity bundle generation approach. Agents utilize a local search tree guided by a low-fidelity heuristic (such as euclidean distance) to rapidly explore the bundle space, applying high-fidelity path planning only to the most promising candidates in a best-first manner. These refined bids are then submitted to a central coordinator that solves a set packing problem to ensure global feasibility and maximize the overall utility. Simulation results in multiple environments demonstrate that the framework is able to improve the performance of reactive auction-based task allocation. Overall, the presented framework is shown to enable reactive task allocation with dynamic bundle sizes in multiple settings without exposing the agents' state and internal cost estimation models.

### 27. AdsMind: A Physics-Grounded Multi-Agent System for Self-Correcting Discovery of Adsorption Configurations on Heterogeneous Catalyst Surfaces
- Deep score: 0.2
- Date: 2026-06-17T14:57:16+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.19152
- Summary: Identifying the lowest-energy surface-adsorbate configuration is critical for modeling heterogeneous catalysis, yet exhaustive exploration with ab initio calculations is computationally prohibitive. Machine-learning force fields (MLFFs) accelerate structural relaxation but leave the search over the vast configurational space a major bottleneck, and open-loop large language model (LLM) agents lack a physics-grounded feedback mechanism to correct erroneous initial guesses. We propose AdsMind (Adsorption configuration discovery with Machine intelligence and relaxation feedback), a closed-loop multi-agent framework that enables autonomous error correction through MLFF relaxation feedback. Across four LLM backends, AdsMind achieves consistently high search reliability, with success rates of 100% and 98.8% on the benchmarks AA20 and OCD-GMAE62. Relative to its single-pass (1-Shot) ablation it reduces cross-backend energy dispersion, and it uses only 4.11 and 4.67 MLFF relaxations per case, respectively -- an approximately 14-fold reduction over heuristic enumeration baselines. Density functional theory (DFT) validation using VASP/PBE on six representative AA20 systems shows that the reported open-loop Adsorb-Agent outputs exhibit qualitative adsorption-energy sign errors for molecular adsorbates, whereas AdsMind preserves the correct sign in all tested cases with closer quantitative agreement. AdsMind thus delivers reliability, self-reflection, and interpretability simultaneously, supporting more DFT-informed autonomous chemistry workflows.

### 28. PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning
- Deep score: 0.2
- Date: 2026-06-17T03:03:53+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.18633
- Summary: Effective programming education requires personalized instruction adapted to diverse learner backgrounds. However, while LLM-based multi-agent systems (MAS) excel at complex planning, existing planners often lack profile-grounding and pedagogical scaffolding, thereby undermining personalized programming learning. To fill in the gap, we first introduce \textbf{MAP-PPL} (\textbf{M}ulti-\textbf{A}gent \textbf{P}lans for \textbf{P}ersonalized \textbf{P}rogramming \textbf{L}earning), a profile-conditioned multi-agent planning dataset with 3{,}043 query--profile--plan instances from 1{,}730 Stack Overflow question groups and 2{,}738 learner profiles. Each plan specifies agents, subtasks, executable steps, and prerequisite dependencies. Then, we propose \textbf{PersonalPlan}, a two-stage MAS planner that first performs hierarchical SFT with separate LoRA adapters for profile-aware task decomposition and step dependency planning, then applies a Reward-Adaptive GRPO to encourage the model to generate executable, personalized, and pedagogically scaffolded plans. Extensive experiments on MAP-PPL comparing PersonalPlan against frontier LLMs, generic MAS frameworks, and agentic planners demonstrate its superiority. With only 8B and 32B variants, PersonalPlan achieves state-of-the-art plan executability, personalization, and pedagogical quality, effectively orchestrating MAS for agent-student interactions.

### 29. Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications
- Deep score: 0.2
- Date: 2026-06-16T21:30:10+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.18502
- Summary: Large language model (LLM)-based multi-agent systems demonstrate strong performance on complex reasoning and task execution, enabling broad enterprise applications. However, production deployment remains challenging due to domain-specific customization requirements and high latency and inference costs in agentic workflows. We propose a unified framework for customization and efficient deployment of multi-agent systems in real-world settings. The first stage, Agentic Model Customization, combines continual pretraining, supervised fine-tuning, and preference optimization to adapt a compact model to specialized domains while retaining strong agentic capabilities. The second stage, Inference Optimization, integrates speculative decoding and FP8 quantization with targeted calibration to enable cost-efficient serving with minimal quality loss. Across enterprise workloads, our framework enables rapid domain adaptation and achieves a 4.48x speedup in throughput while maintaining performance and improving robustness on long-tail scenarios.

### 30. Searching for Synergy in Shared Workspace Human-AI Collaboration
- Deep score: 0.2
- Date: 2026-06-16T19:08:43+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.18413
- Summary: Automated AI agents are increasingly capable, yet many scientific and professional tasks require human judgment and contextual expertise. We study shared-workspace human-AI teams, where AI agents and human collaborators must coordinate responsibilities before submitting a final answer. Using the Collaborative Gym environment with DiscoveryBench tasks, we examine when adding simulated human collaborators improves performance and when process loss turns additional collaborators into coordination overhead. Across 1,482 sessions, adding relevant collaborators can lower performance when teams lack structure to coordinate their contributions. We then evaluate scaffolding that combines shared group memory with simulated human-in-the-loop (HITL) gates, where selected actions require approval from a designated simulated participant. This scaffolding yields higher mean performance, most clearly in three-person teams, with clearer responsibility signals and stronger routing of expertise to team actions. Overall, how human-AI teams coordinate and integrate expertise matters as much as the capability available to them.

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

### 12. Towards Agentic AI Governance: A Preliminary Assessment
- Deep score: 0.3
- Date: 2026-07-08T16:29:18+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.07612
- Summary: Artificial intelligence is rapidly evolving from generative systems to agentic AI capable of autonomously planning and executing tasks. Widely characterized as the Year of Agentic AI, 2025 marked accelerated development and deployment, introducing new ethical and governance challenges. This paper presents a systematic review of the emerging literature on agentic AI governance. Our analysis identifies features that distinguish agentic AI from traditional systems and why it warrants targeted governance attention. We synthesize prevailing governance priorities, proposed mechanisms, and stakeholder roles shaping this evolving domain. As an initial scholarly effort, this review lays the preliminary groundwork for developing a structured roadmap to guide responsible and adaptive agentic AI governance.

### 13. Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation
- Deep score: 0.3
- Date: 2026-07-08T16:26:06+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.07608
- Summary: Mainstream Vision-Language-Action (VLA) models predict actions primarily from the current observation under a Markovian assumption, thus struggling with long-horizon, temporally dependent tasks. Existing memory-augmented VLAs either expand the observation window or retrieve history from the memory bank as auxiliary policy-side context. However, they leave memory outside the native latent embedding space of VLA reasoning, preventing historical experience from being fluidly interleaved with multimodal reasoning and action formation. To this end, we introduce LaMem-VLA, a latent-memory-native framework that reconstructs historical experience into latent memory tokens and directly interweaves them with VLA reasoning. At its core, LaMem-VLA introduces four coordinated components: (i) a curator that organizes historical experience into two complementary short-term and long-term memory vaults; (ii) a seeker that queries both vaults using the multimodal cognition to retrieve context-relevant evidence; (iii) a condenser that reconstructs the retrieved evidence into compact short-term and long-term latent memory tokens; and (iv) a weaver that injects these memory tokens with the current observation and instruction into one continuous embedding sequence. By representing, retrieving, and consuming historical experience entirely in the same continuous latent space, LaMem-VLA enables memory to directly participate in VLA reasoning and guide action generation under a bounded context. Extensive experiments on SimplerEnv and LIBERO demonstrate the superiority of our LaMem-VLA.

### 14. Multi-Agent Robotic Control with Onboard Vision-Language Models
- Deep score: 0.3
- Date: 2026-07-08T13:37:31+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.07403
- Summary: Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial warehouse, fulfilling five task categories: safety inspection, warehouse maintenance, warehouse search, package quality verification, and responding to human requests. Compact VLMs (3-20B parameters) are used throughout, with fine-tuning applied to improve package inspection accuracy. A novel "Megamind" orchestration agent mitigates context retention issues inherent to long-horizon planning with smaller models. The system was validated in a hardware-in-the-loop simulation using an AMD Ryzen(TM) AI mini PC. Results demonstrate that a fully onboard MAS architecture is a viable, cost-efficient alternative to cloud-dependent deployments, with strong potential for real-world transfer. The simulation environment has been released as open source under the Apache 2.0 licence.

### 15. Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses
- Deep score: 0.3
- Date: 2026-07-06T13:10:13+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.05029
- Summary: Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals. We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA's attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent's retrieved content but also the integrity of its reasoning history.

### 16. Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory
- Deep score: 0.3
- Date: 2026-07-06T00:00:00+00:00
- Source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2607.05511
- Summary: Agentic video understanding equips models with long-term memory to autonomously process and respond to continuous, long-horizon multimodal streams. However, advanced video agents often rely on ``detective-style'' iterative reasoning for action control (e.g., search) and evidence aggregation, incurring prohibitive costs and latency. We argue that such heavy reasoning primarily compensates for the lack of global context and semantic misalignment in retrieval. This paper introduces Light-Omni, a multimodal agent framework for reflexive and lightweight video understanding. It achieves this through dual contextual states that instantly build the required context in a single forward pass. First, we maintain a global state, a finite-sized multimodal script continuously consolidated from episodic memory, serving as the global context for Light-Omni. Through hierarchical merging, it preserves recent details while summarizing past events. Second, conditioned on this global context, we generate a parametric latent state that directly drives autonomous actions and produces retrieval embeddings, with minimal latency. Benefiting from this coupled design, Light-Omni achieves semantically aligned retrieval and reflexive responses while avoiding iterative reasoning. Extensive experiments validate the effectiveness of Light-Omni across multiple video benchmarks. Notably, it outperforms M3-Agent with an average 2.4% accuracy gain, a 12.1times speedup, and a 2.6times improvement in GPU memory efficiency. Furthermore, it serves as a memory system to enhance both the performance and efficiency of existing MLLMs. Project page: https://clare-nie.github.io/Light-Omni.

### 17. A Common Neural Signal of Evidence Accumulation for Perceptual and Mnemonic Decisions
- Deep score: 0.3
- Date: 2026-07-06T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://www.biorxiv.org/content/10.1101/2025.11.13.688140
- Summary: Humans frequently make decisions based on sensory input from the external environment or information retrieved from memory. The centro-parietal positivity (CPP), an event-related EEG potential, has recently been identified as a neural correlate of sensory evidence accumulation during perceptual decision-making tasks. However, it remains unclear whether this component also reflects the accumulation of evidence in service of decisions grounded in semantic and episodic long-term memory. Across two experiments, we investigated whether the CPP serves as a domain-general neural signal of evidence accumulation. In Experiment 1, participants completed 2AFC perceptual and semantic memory tasks with varying levels of evidence strength. Perceptual judgements involved luminance discrimination of alphanumeric strings with three luminance difference levels controlling perceptual evidence strength. Semantic memory judgements involved discriminating population differences between U.S. states with census data used to define three bins of memory evidence strength. A CPP component was observed in both tasks whose build-up rate (i.e., slope) scaled with evidence strength, response time, and confidence in both stimulus- and response-locked analyses. Extending these findings to episodic memory, participants in Experiment 2 completed a two-alternative forced-choice word recognition task with target words varying in exposure frequency during learning to control episodic memory strength. Again, we found that CPP slopes scaled with memory strength, response time, and confidence. Together, these findings support the CPP as a domain-general neural signature of evidence accumulation across perceptual, semantic, and episodic mnemonic decisions.

### 18. AGL-1: The Enterprise AI Governance Layer as a Control Plane for Trusted Enterprise Intelligence
- Deep score: 0.3
- Date: 2026-07-03T17:42:08+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.03516
- Summary: Enterprise artificial intelligence is moving from isolated experimentation toward operational dependency across copilots, retrieval-augmented generation systems, autonomous agents, and AI-enabled business workflows. As this transition accelerates, the primary enterprise challenge is no longer only model access or inference scale. It is governed intelligence operations: the ability to enforce authorization, preserve contextual lineage, control persistent memory, detect stale or conflicting knowledge, constrain agentic execution, and produce audit-ready evidence across distributed AI estates. This paper introduces AGL-1, the Enterprise AI Governance Layer, as a vendor-neutral reference model for the control plane that should operate across foundation models, retrieval systems, orchestration frameworks, enterprise memory, policy engines, observability systems, tools, APIs, and business applications. Building on governed knowledge-system principles introduced in GKS-5, AGL-1 generalizes the governance problem from retrieval-specific controls to full AI execution-path governance. It identifies recurring failure modes such as unauthorized retrieval, stale grounding, unmanaged memory, weak provenance, policy drift, fragmented observability, and uncontrolled autonomous execution. It then defines seven governance domains: identity-aware retrieval, policy enforcement, provenance management, memory governance, knowledge integrity monitoring, agentic execution control, and trust observability. The central claim is that durable enterprise value from AI will increasingly depend on the ability to govern intelligence at scale. In complex enterprises, trust is not a property of the model alone. It is a property of the system around the model: identity, knowledge, policy, memory, tools, human oversight, and evidence working together as a managed control plane.

### 19. MemSyco-Bench: Benchmarking Sycophancy in Agent Memory
- Deep score: 0.3
- Date: 2026-07-01T15:30:33+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.01071
- Summary: Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of factual accuracy or objective reasoning. Despite this emerging risk, existing memory benchmarks primarily evaluate whether memories are correctly stored, retrieved, or updated, while overlooking how retrieved memories influence downstream reasoning and decision-making. To bridge this gap, we propose MemSyco-Bench, a comprehensive benchmark for evaluating memory-induced sycophancy in agent systems. MemSyco-Bench measures when memory should influence a decision and how valid memory should be used. Specifically, it covers five tasks that assess whether agents can reject memory as factual evidence, respect its applicable scope, resolve conflicts between memory and objective evidence, track memory updates, and use valid memory for personalization. All related resources are collected for the community at https://github.com/XMUDeepLIT/MemSyco-Bench.

### 20. Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems
- Deep score: 0.3
- Date: 2026-06-30T08:41:00+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.31339
- Summary: Agentic artificial intelligence is increasingly used to decompose industrial tasks, propose robot actions, and adapt execution plans in dynamic cyber-physical environments. However, autonomous proposal generation alone does not guarantee that multi-robot industrial systems preserve task dependencies, resource ownership, safety holds, or repair boundaries during long-horizon execution. This paper introduces a verification-gated agentic mission-state governance framework for intelligent industrial multi-robot systems. The framework maintains two synchronized state objects: an evolving task forest for persistent hierarchy, delayed grounding, and repairable substructures; and a governed blackboard for online execution state, robot traces, resource locks, world beliefs, proposals, verification records, and scene-temporary constraints. From each forest--blackboard snapshot, a derived execution coupling topology exposes cross-branch dependencies for proposal verification, parallel-commit eligibility, and bounded repair. Candidate assignments, repairs, deferrals, and constraint updates may be generated by heuristic, optimization, or agentic reasoning modules, but they can update the committed mission state only after deterministic verification and atomic commit. We evaluate the framework in an indoor factory multi-robot scenario, 30-seed remote-construction stress benchmarks, structural ablations, and scalability probes. The results show improved verified and safety-audited mission-state progress with fewer invalid commitments, lock conflicts, duplicate assignments, abandoned nodes, and disruptive repairs under modeled mission predicates. The study positions agentic AI as a proposal-generating layer governed by inspectable mission-state verification rather than as an unchecked execution authority.

### 21. Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation Threats
- Deep score: 0.3
- Date: 2026-06-29T13:07:41+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.30259
- Summary: In contemporary societies, the threat of disinformation has reached alarming levels, exacerbated by the proliferation of electronic communication, social media, and advancements in artificial intelligence. As a result, there is an urgent need to develop effective countermeasures to mitigate this menace. However, the sheer scale of the problem renders manual fact-checking and human-based verification inadequate, underscoring the necessity for automated methods to detect and debunk disinformation. This article proposes a novel approach based on a multi-agent system that emulates the decision-making processes of human annotators engaged in disinformation detection tasks. By incorporating a consensus mechanism, diversity in cognition and diversity in knowledge, and also hierarchical structure, inspired by human annotators' behavior, the proposed method achieves superior results compared to individual Large Language Models (LLMs), including GPT 4 and GPT 3.5. The system leverages open models (e.g., LLaMA, Kimi, Qwen, Deepseek and LLaMA-Nemotron) to ensure greater transparency. The evaluation of the proposed method encompasses datasets in languages with varying resource availability, including English (high-resource), Polish (medium-resource), Slovak (low-resource) and Bulgarian (low-resource). Experiments were conducted on tasks such as direct disinformation detection, identification of texts worthy of verification, and detection of texts containing verifiable factual claims.

### 22. A Multi-Agent system for Multi-Objective constrained optimization
- Deep score: 0.3
- Date: 2026-06-18T13:47:28+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.20236
- Summary: Many decision-making problems in computing and networking systems can be naturally formulated as cost-minimization problems under performance constraints. In dynamic environments, reinforcement learning (RL) is often used to solve such problems at runtime by embedding both costs and constraint violations into a single scalar reward through weighted penalty terms, following a Lagrangian-inspired formulation. However, in this context the behavior of the learned policy critically depends on the choice of these weights, which are typically selected manually. This makes it difficult to identify an appropriate trade-off between optimizing the primary objective and effectively avoiding constraint violations, particularly in non-stationary environments where their relative importance may change. This paper presents MAMO (Multi-Agent system for Multi-Objective constrained optimization), an approach to tackle this balancing problem through multi-agent RL. MAMO decouples task execution from objective design by formulating the selection of reward weights as a learning problem, providing a !rst step towards more autonomous and robust RL-based solutions for constrained optimization problems in dynamic environments.

### 23. GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning
- Deep score: 0.3
- Date: 2026-06-16T03:45:24+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.17480
- Summary: Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Second, the original KnowledgeBank mainly retrieves semantically similar snippets and appends new knowledge, which makes it difficult to control memory quality, conflicts, confidence, and geometric relevance. To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance. To address the second challenge, we upgrade KnowledgeBank into a governed long-term memory system with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while reducing AS by 4.95% and 5.65%, respectively. Code: https://github.com/AIGeeksGroup/GeneralVLA-2. Website: https://aigeeksgroup.github.io/GeneralVLA-2.

### 24. Misinformation Propagation in Benign Multi-Agent Systems
- Deep score: 0.3
- Date: 2026-06-15T13:40:01+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.16710
- Summary: Multi-agent systems, in which multiple large language model agents solve problems through turn-based interaction, are increasingly deployed in high-stakes settings such as medical diagnosis, legal analysis, and forensic decision-making. Their reliability can be at risk when single agents reason from incorrect or misleading context, e.g., from tool calls, since errors may propagate through agent interactions. This work studies this risk by injecting intent-based misinformation into benign single-agent and multi-agent systems across reasoning, knowledge, and alignment tasks. We find that misinformation can degrade single-agent performance and persists across multi-agent debate, with agents often retaining answers introduced by misinformed peers. Nevertheless, multi-agent debate reduces the resulting performance degradation compared to single-agent prompting, especially when most agents are not exposed to misinformation. Robustness depends on group composition and decision protocol. Consensus can be more stable than voting under peer pressure, while majorities can often steer misinformed agents back toward correct answers. Our results show that misinformation robustness in multi-agent systems depends on the underlying model and also on how agents exchange information and aggregate decisions.

### 25. Decentralized Multi-Agent Systems with Shared Context
- Deep score: 0.3
- Date: 2026-06-09T10:13:07+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.10662
- Summary: Multi-agent systems (MAS) can scale large language model reasoning at test time by decomposing complex problems into parallel subtasks. However, most existing MAS rely on centralized orchestration, where a main agent assigns work, collects outputs, and merges results. As the number of subtasks grows, this controller becomes a communication and integration bottleneck. We propose Decentralized Language Models (DeLM), a MAS framework that decentralizes coordination through parallel agents, a shared verified context, and a task queue. Agents asynchronously claim subtasks, read accumulated progress, perform local reasoning, and write back compact verified updates. The shared context acts as a common communication substrate, enabling agents to build on one another's verified progress without routing every update through a central controller. Empirically, DeLM improves both software-engineering test-time scaling and long-context reasoning. On SWE-bench Verified, DeLM achieves the best performance across Avg.@1, Pass@2, and Pass@4, with gains of up to 10.5 percentage points over the strongest baseline, while reducing cost per task by roughly 50%. On LongBench-v2 Multi-Doc QA, DeLM achieves the highest average accuracy across four frontier model families, improving over the strongest baseline by up to 5.7 percentage points. The code is available on our project website at https://yuzhenmao.github.io/DeLM/.

### 26. Distilling LLM Reasoning into an Interpretable Policy Tree for Human-AI Collaboration
- Deep score: 0.3
- Date: 2026-06-07T12:20:32+00:00
- Source: arxiv
- Focus/tech: cognitive outsourcing, AI agents / cognitive outsourcing
- URL: https://arxiv.org/abs/2606.08596
- Summary: Constructing efficient and reliable policies to assist humans is indispensable for human-AI collaboration. Existing methods mainly follow two lines of work. Most prior work relies on multi-agent reinforcement learning (MARL) to learn black-box policies, which limits interpretability and raises safety concerns. Recent methods query large language models (LLMs) at each decision step, causing slow responses and high inference costs. We propose Collaboration Policy Tree (Co-pi-tree), a closed-loop method that learns an executable policy tree consisting of a partner-behavior prediction tree and an agent-action selection tree. Co-pi-tree constructs a policy by distilling LLM reasoning into policy tree code. It then evaluates the policy through partner interaction, obtains feedback, and uses natural language to summarize the interaction feedback to improve problematic branches. Experiments in Overcooked-AI show that Co-pi-tree improves average reward by 35.4% over the baseline average, while reducing the number of LLM queries by 77.7% and test-time latency by 97.1%. Project page: https://beiwenzhang.github.io/Co-pi-tree/

### 27. Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems
- Deep score: 0.3
- Date: 2026-06-04T05:10:20+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.05711
- Summary: Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. The dominant communication protocol in such systems is natural language: agents exchange messages token-by-token, verbalising their internal reasoning so that peers can read, verify, and respond. While convenient and interpretable, this protocol suffers from three structural drawbacks -- high inference cost, irreversible information loss during discretization, and ambiguity/redundancy of natural language. A growing body of work therefore explores an alternative protocol -- latent communication -- in which agents exchange continuous representations (embeddings, hidden states, or KV-caches) directly, bypassing the bottleneck of text generation. This paper presents a unified framework for organising the rapidly expanding literature on latent communication. We analyse existing methods along three orthogonal axes: (1) WHAT information is communicated (Embeddings, Hidden States, KV-Caches, or other continuous state); (2) WHICH sender-receiver alignment is used (latent-space alignment and layer alignment); and (3) HOW the communicated information is fused into the receiver (concatenation, prepending, mathematical operations, cross-attention, or cache restoration). Under this 3-axis framework, we systematically categorise eighteen representative methods proposed between 2024 and 2026, identify five major design patterns, and surface a set of open challenges -- including cross-architecture alignment, security of latent channels, compression for edge deployment, and the relationship between latent communication and latent chain-of-thought. We hope that this framework both lowers the barrier to entry for new researchers and provides a vocabulary for comparing future work.

### 28. Traj-Evolve: A Self-Evolving Multi-Agent System for Patient Trajectory Modeling in Lung Cancer Early Detection
- Deep score: 0.3
- Date: 2026-06-01T19:30:07+00:00
- Source: arxiv
- Focus/tech: AI agents, human augmentation / AI agents
- URL: https://arxiv.org/abs/2606.02812
- Summary: Modeling patient trajectories from longitudinal electronic health records (EHRs) requires reasoning over sparse, noisy, and long-context multimodal sequences. Existing LLM-based multi-agent systems address context length but process patients in isolation, failing to mirror how clinicians leverage accumulated experience from similar prior cases. We present Traj-Evolve, a self-evolving multi-agent system with two complementary evolving mechanisms. First, an Experience Pool (ExPool) acts as a non-parametric memory, indexing rejection-sampled reasoning traces to retrieve similar patients as few-shot contexts. Second, multi-agent reinforcement learning (MARL) via reward-ranked fine-tuning parametrically optimizes inter-agent and agent-memory collaboration. A leave-one-out cross-retrieval strategy unifies the two, aligning training- and inference-time behavior under retrieval augmentation. On a lung cancer prediction task utilizing up to five years of multimodal EHRs, Traj-Evolve outperforms 9 strong baselines on the overall population and a challenging never-smoker population. Analysis of the evolving dynamics highlights three key findings: (1) expanding the ExPool shifts optimal retrieval from diverse to specific samples; (2) under MARL, the manager agent's prediction loss converges quickly while the worker agents' temporal reasoning continues to benefit from more verified patients; and (3) the two mechanisms are complementary on the predicted risk, where ExPool improves specificity while MARL improves sensitivity.

### 29. Generative Multi-Robot Motion Planning via Diffusion Modeling with Multi-Agent Reinforcement Learning Guidance
- Deep score: 0.3
- Date: 2026-05-30T23:54:04+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.00933
- Summary: Coordinating multiple robots in shared environments requires generating feasible trajectories for each agent while accounting for interactions among agents. Centralized planning approaches become difficult to scale as the number of robots increases, while decentralized approaches that allow each agent to plan independently do not inherently account for inter-agent interactions. This paper presents a framework for coordinated multi-robot motion planning that combines decentralized generative trajectory planning with multi-agent reinforcement learning (MARL)-based coordination. Each robot independently generates candidate trajectories using a diffusion model trained on single-agent motion data, leveraging the generative model's ability to produce feasible and diverse trajectories. To reduce conflicts between agents, a centralized value function trained via MARL guides the reverse diffusion process through gradient-based steering, enabling interaction-aware trajectory generation without centralized joint planning or retraining of the generative model. This guidance follows an exponential tilting formulation, in which the value function biases the denoising distribution toward trajectories with higher expected multi-agent return. The framework is evaluated in a simulated maze environment with four mobile robots. Experimental results show that the proposed value-guided diffusion planning reduces the inter-agent interference rate from 55.4% to 41.8%, demonstrating that coordination can be effectively achieved while preserving the scalability of decentralized trajectory generation. These results suggest that MARL-based value guidance can effectively introduce coordination into decentralized generative planners without requiring a fully joint multi-robot model.

### 30. MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented Generation
- Deep score: 0.3
- Date: 2026-05-30T08:18:53+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.00610
- Summary: Retrieval-Augmented Generation (RAG) has become an essential method for mitigating hallucinations in Large Language Models (LLMs) by leveraging external knowledge. Although effective for simple queries, traditional RAG struggles with large-scale, unstructured corpora where information is highly fragmented. Graph-based RAG (GraphRAG) incorporates knowledge graphs to capture structural relationships, enabling more comprehensive retrieval for complex reasoning. However, existing GraphRAG methods rely on isolated, fragment-level extraction for graph construction, lacking a global perspective on the whole corpus. As a result, these methods frequently lead to thematically inconsistent, logically conflicting, and structurally fragmented graphs that degrade retrieval performance. In this paper, we propose MemGraphRAG, a novel framework that introduces a memory-based multi-agent system to ensure high-quality graph construction. Specifically, MemGraphRAG employs a collaborative society of agents supported by shared memory, which provides a unified global context throughout the extraction process. This mechanism allows agents to dynamically resolve logical conflicts and maintain structural connectivity throughout the corpus. Furthermore, we propose a memory-aware hierarchical retrieval algorithm tailored for the constructed graph. Extensive experiments on multiple benchmarks demonstrate that MemGraphRAG outperforms the state-of-the-art baseline models with comparable efficiency. Our code is available at https://github.com/XMUDeepLIT/MemGraphRAG.
