# Blindspot Signals Report - 2026-06-12

Source export: `/opt/apps/haier/exports/evolution_signals_20260612_020412.json`

Signals processed: 5000 total, 734 agent-relevant.

## Top Signals By Deep Score

### 1. Toward Human-Centered Multi-Agent Systems: Integrating Cognition, Culture, Values, and Cooperation in AI Agents
- Source: arxiv
- Focus: AI agents, AI decision delegation
- Date: 2026-06-06T17:40:21+00:00
- Deep score: 0.6
- Why it matters: The emergence of large language model (LLM)-based agents and multi-agent systems has enabled a shift from narrow task automation to more autonomous decision-making. Despite progress in language generation, planning, tool use, and coordination, most agents still treat intelligence as prediction, optimization, and task completion. Human environments are social and normative, where people reason under bounded rationality, communicate in culturally situated language, and make decisions guided by values, beliefs, trust, and social norms. This survey argues that future AI agents, especially those acting on behalf of humans, must move beyond task competence toward human-centered capabilities.   We review research across six areas: (1) evolution of intelligent agents, (2) human cognition and decision-making, (3) language, culture, and social context, (4) human values and belief systems, (5) human-agent collaboration, and (6) multi-agent coordination and modeling of human characteristics. We synthesize work from cognitive science, sociolinguistics, computational social science, and AI alignment, along with recent advances in LLM agents, cultural alignment benchmarks, preference learning, explainability, and agent societies. We identify a key gap: existing systems do not provide a unified framework integrating cognition, culture, values, and social behavior into autonomous agents. We conclude with directions for building culturally aware, value-aligned, cognitively grounded, and cooperative multi-agent systems.
- URL: https://arxiv.org/abs/2606.08274

### 2. Delayed Repression and Emergent Instability in Adaptive Multi-Agent Systems
- Source: arxiv
- Focus: AI agents
- Date: 2026-05-28T12:26:48+00:00
- Deep score: 0.5
- Why it matters: Regulatory institutions (from content moderation platforms to financial supervisors) observe, deliberate, and intervene only after a characteristic delay. We ask whether this processing lag alone can destabilize a multi-agent system that would otherwise remain stable, without exogenous shocks, coordination among agents, or malicious actors. We study this in two stages. First, we analyze a delayed replicator equation in which autonomous agents benefit from radical behavior but face punishment based on a lagged institutional alarm signal. We derive a closed-form critical delay beyond which the unique interior equilibrium loses stability through a Hopf bifurcation, and prove via center manifold reduction that the bifurcation is supercritical (bounded oscillations, not explosive growth) for the entire sigmoid response family. Second, we embed N=240 agents on a network with reinforcement learning (tabular Q-learning) and cross institutional delay with three decision architectures: fixed-policy, reactive (a memoryless threshold heuristic), and Q-learning. The hierarchy is opposite to the naive expectation that learning amplifies instability. Reactive agents are perfectly stable without delay yet collapse once delay is introduced (96% runaway by delay >= 8); fixed-policy agents are immune (0% at all delays); Q-learning agents are only partially resilient (66% at delay 20). The destabilizing ingredient is reactivity to delayed signals, not learning: agents that immediately exploit low-alarm windows trigger oscillatory feedback loops, while learning buffers this through punishment memory encoded in value functions. Throughout, "runaway" denotes bounded large-amplitude oscillation crossing a radical-fraction threshold, consistent with the supercritical bifurcation, not unbounded growth.
- URL: https://arxiv.org/abs/2605.30392

### 3. A Sheaf Framework for Strategic Multi-Agent Systems: From Consensus to Nash Equilibria
- Source: arxiv
- Focus: AI agents
- Date: 2026-06-01T04:17:57+00:00
- Deep score: 0.5
- Why it matters: The coordination of heterogeneous autonomous agents in dynamic, adversarial environments requires simultaneous satisfaction of geometric constraints, logical consistency, temporal reasoning, and strategic optimization. Existing sheaf- and topos-theoretic frameworks provide powerful tools for geometric consensus, knowledge alignment, and causal planning, but lack explicit models for value, reward, and strategic choice. This report presents a unified categorical framework that integrates event calculus, SCEL-like ensemble formation, and game-theoretic reward structures into a single Grothendieck topos of time-space histories. We introduce the notion of a \emph{game sheaf} whose stalks contain utility functions and policy distributions, and restriction maps encode both parallel transport and best-response dynamics. We prove that Nash equilibria correspond to global sections of a derived best-response correspondence sheaf, while cohomological obstructions classify failures of strategic consistency. A detailed case study of an immunological ``bastion defense'' scenario -- heterogeneous agents forming attack/defense ensembles under resource constraints -- demonstrates the framework's expressiveness. This synthesis provides a rigorous foundation for verifiable, autonomic, and economically rational multi-agent systems.
- URL: https://arxiv.org/abs/2606.01663

### 4. DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems
- Source: arxiv
- Focus: AI agents, robotics
- Date: 2026-06-10T19:14:56+00:00
- Deep score: 0.5
- Why it matters: Multi-agent systems are integral tools for various domains such as robotics, cybersecurity, and autonomous vehicle planning. These types of systems often have constraints on the computational resources, leading to a need for efficient lightweight algorithms. Traditional decision making frameworks often assume ideal conditions, such as full observability and unlimited computational capacity, which do not align with real-world challenges. In this paper, we introduce a new algorithm that allows for reduced demand on computational resources without a large cost of other performance metrics. Agents will limit their observability to some attention radius, which intentionally allows them to ignore parts of the environment that might be unnecessary for action planning. By optimizing both the attention radius and decision-making, our approach enhances coordination and scalability in uncertain environments. Through both theoretical analysis and empirical validation, we demonstrate the effectiveness of adaptive observation in improving system performance and maintaining robust decision-making strategies in resource-constrained systems.
- URL: https://arxiv.org/abs/2606.12614

### 5. Agentic Copyright, Data Scraping & AI Governance: Toward a Coasean Bargain in the Era of Artificial Intelligence
- Source: arxiv
- Focus: AI agents, AI decision delegation
- Date: 2026-04-08T19:43:28+00:00
- Deep score: 0.4
- Why it matters: This paper examines how the rapid deployment of multi-agentic AI systems is reshaping the foundations of copyright law and creative markets. It argues that existing copyright frameworks are ill-equipped to govern AI agent-mediated interactions that occur at scale, speed, and with limited human oversight. The paper introduces the concept of agentic copyright, a model in which AI agents act on behalf of creators and users to negotiate access, attribution, and compensation for copyrighted works. While multi-agent ecosystems promise efficiency gains and reduced transaction costs, they also generate novel market failures, including miscoordination, conflict, and collusion among autonomous agents. To address these market failures, the paper develops a supervised multi-agent governance framework that integrates legal rules and principles, technical protocols, and institutional oversight. This framework emphasizes ex ante and ex post coordination mechanisms capable of correcting agentic market failures before they crystallize into systemic harm. By embedding normative constraints and monitoring functions into multi-agent architectures, supervised governance aims to align agent behavior with the underlying values of copyright law. The paper concludes that AI should be understood not only as a source of disruption, but also as a governance tool capable of restoring market-based ordering in creative industries. Properly designed, agentic copyright offers a path toward scalable, fair, and legally meaningful copyright markets in the age of AI.
- URL: https://arxiv.org/abs/2604.07546

### 6. AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration
- Source: arxiv
- Focus: AI agents
- Date: 2026-05-19T15:49:51+00:00
- Deep score: 0.4
- Why it matters: Automating scientific discovery requires more than generating papers from ideas. Real research is iterative: hypotheses are challenged from multiple perspectives, experiments fail and inform the next attempt, and lessons accumulate across cycles. Existing autonomous research systems often model this process as a linear pipeline: they rely on single-agent reasoning, stop when execution fails, and do not carry experience across runs. We present AutoResearchClaw, a multi-agent autonomous research pipeline built on five mechanisms: structured multi-agent debate for hypothesis generation and result analysis, a self-healing executor with a \textsc{Pivot}/\textsc{Refine} decision loop that transforms failures into information, verifiable result reporting that prevents fabricated numbers and hallucinated citations, human-in-the-loop collaboration with seven intervention modes spanning full autonomy to step-by-step oversight, and cross-run evolution that converts past mistakes into future safeguards. On ARC-Bench, a 25-topic experiment-stage benchmark, AutoResearchClaw outperforms AI Scientist v2 by 54.7%. A human-in-the-loop ablation across seven intervention modes reveals that precise, targeted collaboration at high-leverage decision points consistently outperforms both full autonomy and exhaustive step-by-step oversight. We position AutoResearchClaw as a research amplifier that augments rather than replaces human scientific judgment. Code is available at https://github.com/aiming-lab/AutoResearchClaw.
- URL: https://arxiv.org/abs/2605.20025

### 7. AI-IoT-Robotics Integration: Survey of Frameworks, Emerging Trends, and the Path Toward Connected Robotics
- Source: arxiv
- Focus: robotics, AI decision delegation
- Date: 2026-05-31T05:10:34+00:00
- Deep score: 0.4
- Why it matters: The convergence of Artificial Intelligence, the Internet of Things, and Robotics is no longer a futuristic vision; it is rapidly becoming the foundation of real-time, intelligent, and context-aware systems. AI enables perception and reasoning, IoT provides scalable sensing and communication, and robotics delivers embodied actuation. Despite significant progress in pairwise combinations such as AIoT and the Internet of Robotic Things (IoRT), there remains a lack of unified design frameworks that fully integrate all three. This survey synthesizes the state-of-the-art across these domains, emphasizing the emerging role of Small Language Models (SLMs) at the edge and Large Language Models (LLMs) in the cloud for distributed cognition and autonomous decision-making. We propose a modular system architecture that aligns with these trends, analyze persistent gaps in interoperability and feedback control, and classify existing work by integration depth. Our review highlights how hybrid SLM-LLM systems, when coupled with IoT infrastructure and robotic agents, can address challenges in real-time adaptation, scalability, and reliability. This work offers a conceptual and technical roadmap for designing next-generation AI-IoT-Robotic ecosystems that are modular, interpretable, and capable of learning within dynamic environments, paving the way for the emerging paradigm of Connected Robotics and Physical AI.
- URL: https://arxiv.org/abs/2606.01015

### 8. DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning
- Source: arxiv
- Focus: AI agents
- Date: 2026-06-05T14:10:48+00:00
- Deep score: 0.4
- Why it matters: Deep Research (DR) has emerged as a new agentic paradigm to tackle complex, open-ended research tasks, demanding systems that can iteratively frame problems, acquire evidence, verify sources, and synthesize long-form reports. In practice, however, current DR systems are constrained by four interrelated limitations: long-horizon planning over an underspecified scope, the bottleneck of decomposing and scheduling such tasks within a single agent, hallucination risk in long-form synthesis, and limited process auditability. This technical report presents DuMate-DeepResearch, a multi-agent DR framework built on the Qianfan Agent Foundry. The framework decouples the Agent Core, which handles task understanding, planning, and scheduling, from an extensible Tool Ecosystem for retrieval, evidence acquisition, and report rendering, making every intermediate decision and tool invocation explicitly traceable. Building on this infrastructure, DuMate-DeepResearch further introduces three mechanisms: (i) a graph-based dynamic planning strategy expands the research roadmap coarse-to-fine and continuously revises it through reflection, re-planning, backtracking, and parallel branching; (ii) a recursive two-level execution design delegates each complex search sub-task to an inner Search Agent that runs its own planning loop, isolating noisy retrieval and stabilizing long-horizon execution; (iii) a rubric-based test-time optimization mechanism dynamically generates task-specific quality criteria and uses them as live reasoning scaffolds for evidence-grounded synthesis and adaptive stopping. Across two deep research benchmarks, DuMate-DeepResearch establishes new state-of-the-art results: the best overall score (58.03%) on DeepResearch Bench, and the best overall score (61.95%) on DeepResearch Bench II while ranking first in information recall and analysis.
- URL: https://arxiv.org/abs/2606.07299

### 9. ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems
- Source: arxiv
- Focus: AI agents
- Date: 2026-06-07T15:59:15+00:00
- Deep score: 0.4
- Why it matters: Recent advances have improved the adaptive capabilities of LLM-based multi-agent systems (MAS) through memory-, skill-, and learning-based approaches, yet these approaches remain challenged by noisy trajectories, insufficient modeling of memory-skill relations, and reliance on additional training or high-quality supervision. To address these limitations, we propose ConMem, a relation-aware and training-free framework that enables efficient multi-agent adaptation through cross-experience coordination. Specifically, ConMem distills historical interaction trajectories into structured memory cards to capture reusable strategies and cues, organizing them into a relation-aware memory graph. At runtime, ConMem retrieves cards according to task needs and coordinates them through the card graph to resolve strategy conflicts and recover their dependencies. Combined, these modules yield structured and relation-aware guidance, enabling robust, lightweight adaptation in multi-agent systems without additional training. Extensive experiments across multiple benchmarks and mainstream MAS architectures show consistent gains over existing memory architectures, with improved inference-time efficiency through pruning more than 50% of expanded candidates and reducing planning overhead by over 80%. Our codes are available at https://anonymous.4open.science/r/ConMemCode
- URL: https://arxiv.org/abs/2606.08702

### 10. Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction
- Source: arxiv
- Focus: AI agents, robotics
- Date: 2026-06-10T10:37:27+00:00
- Deep score: 0.4
- Why it matters: Benchmarks are essential for evaluating embodied spatial intelligence, yet their construction is labor-intensive, hard to reuse, and difficult to maintain. Existing embodied benchmarks are often static and may quickly become saturated as models improve, limiting their ability to distinguish new capabilities. We propose Embodied-BenchClaw, an autonomous agentic system for constructing embodied spatial intelligence benchmarks. Given a user-specified evaluation intent, Embodied-BenchClaw automatically produces a complete and continually updatable benchmark package through a five-stage pipeline: intent blueprinting, data collection, structuring and cleaning, benchmark synthesis, and evaluation reporting. The pipeline is coordinated by three agents for planning, construction, and evaluation. To improve reusability and reliability, Embodied-BenchClaw introduces an extensible Skill Library and process quality control, enabling benchmark construction to be composable, verifiable, and repairable. We instantiate multiple benchmarks covering indoor spatial reasoning, outdoor spatial reasoning, robotic manipulation, quadruped robot navigation, UAV/aerial-view understanding, and static benchmark enhancement. These benchmarks span diverse embodied carriers, data sources, and spatial capabilities. Experiments with human evaluation, judge-based assessment, consistency checks, cost analysis, and ablations show that Embodied-BenchClaw can construct verifiable, executable, maintainable, and diagnostically useful embodied spatial benchmarks with reduced manual effort.
- URL: https://arxiv.org/abs/2606.11909

## First 30 Relevant Signals

### 1. NVIDIA / SkillSpector
- Summary: Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks.
- URL: https://github.com/NVIDIA/SkillSpector
- Date: 2026-06-12T02:01:54.286272+00:00
- Deep score: 0.0

### 2. Meta’s Edits app is getting an AI assistant and a desktop version
- Summary: By integrating an AI assistant directly into Edits, Meta is aiming to keep creators engaged on Instagram as it continues to compete with TikTok and YouTube for creators' attention.
- URL: https://techcrunch.com/2026/06/11/metas-edits-app-is-getting-an-ai-assistant-and-a-desktop-version/
- Date: 2026-06-11T17:30:00+00:00
- Deep score: 0.0

### 3. Notes from the Asia-Pacific region: Australia kicks AI governance, digital responsibility into high gear - IAPP
- Summary: Notes from the Asia-Pacific region: Australia kicks AI governance, digital responsibility into high gear&nbsp;&nbsp;IAPP
- URL: https://news.google.com/rss/articles/CBMixAFBVV95cUxPd3dSa2M4M1VVN1dYdGZvLVNsWVRXM2pjSmVCbk8yQ2dzZ1BKM0c1cExWR3hTZ1hSVGtYX05OY1FuaVVaVzZ4UDJyS3p2UHRFMThydFZtMmdzVTVlQ0lnMy0xQWlEWERKSHdwODA0cExKS2FmNXZMUnRSS3hEUWVEQ2hxXzIza3JjYkRWWjBpUUpjVDJEd1BIUHdVaXd6MVlGOHlnYVZBS1c2NnhDclZCek16Wnk2dGVzMFR2LTZZdnZsaDZ1?oc=5
- Date: 2026-06-11T17:08:31+00:00
- Deep score: 0.1

### 4. A Reactive Redistribution Mechanism for STL Tasks in Multi-Agent Systems Under Time-Varying Communication
- Summary: We present a communication-aware task decomposition framework for multi-agent systems with collaborative relative configuration objectives specified in Signal Temporal Logic (STL), allowing for dynamic task reallocation under time-varying communication networks. Building on our prior work, the framework supports the direct use of existing feedback controllers for reactive task satisfaction. We address two key challenges: disjunctive STL specifications and time-varying communication networks. Disjunctive specifications are handled through a graph transition system that captures the alternative task sequences induced by logical OR operators. To address time-varying connectivity, we introduce a redistribution mechanism that transfers tasks from disconnected agents to connected ones as the network evolves while preserving decentralized execution. Simulations and experiments on a swarm of Crazyflie drones demonstrate scalability in the number of agents, communication connectivity, and specification complexity.
- URL: https://arxiv.org/abs/2606.13479
- Date: 2026-06-11T15:30:50+00:00
- Deep score: 0.1

### 5. Middle East boards lead globally in AI governance, but skills gap remains key challenge - Economy Middle East
- Summary: Middle East boards lead globally in AI governance, but skills gap remains key challenge&nbsp;&nbsp;Economy Middle East
- URL: https://news.google.com/rss/articles/CBMivwFBVV95cUxNbUIweU1pRzJMVDBHejRCalBKeXFSa21jVnpkc2JGOU44dTBFTHJ1d3RKdVpHWXJiYjRraTFvblVrSEJ2Z1ZEcFBiTzFLaXFLREFuLUtkT0ZTQmlpaVo0c2hsOHhoZ1JEVzRyQXozal9MYjk4YzdCdXRXcFdsUVV1SHdEMm85djZYQ2N1NV8wdUFueGhsMkNPQndLX1U1VnpRblc3N0ptZGVxeXhGMEtSYUx1UmQ5eG9MMXd1d3NuMA?oc=5
- Date: 2026-06-11T13:44:27+00:00
- Deep score: 0.1

### 6. How State Leaders Can Put People First in AI Decision-Making - Federation of American Scientists
- Summary: How State Leaders Can Put People First in AI Decision-Making&nbsp;&nbsp;Federation of American Scientists
- URL: https://news.google.com/rss/articles/CBMidkFVX3lxTE4xdVVIMG5KX0hzYV9vb1F3OGpIdUZQS2FKQkZoWTNDNVBGdjF0WmIzUzBsTU1INzR1aHJzY3Jmc0VQdVdtN3RabTRlOW10aFQySlV5T3FCbURMM1p0MXZwWjZRMTdIYXB6N2hkbm1WVkM4Mjl3Wmc?oc=5
- Date: 2026-06-11T12:51:08+00:00
- Deep score: 0.1

### 7. The AI Agent in the Billing Department of Verizon Is a Mentally Handicapped Thug
- Summary: No summary
- URL: https://samhenrycliff.medium.com/the-ai-agent-in-the-billing-department-of-verizon-wireless-is-a-mentally-handicapped-thug-99890a389ff5
- Date: 2026-06-11T12:19:17+00:00
- Deep score: 0.0

### 8. Proprioceptive-visual correspondence enables self-other distinction in humanoid robots
- Summary: Distinguishing self from others is a prerequisite for social intelligence, yet humanoid robots that increasingly share workspaces with humans still lack this ability. Here we show that a humanoid robot can learn self-other distinction from proprioceptive-visual correspondence, without any identity labels or kinematic models. Once established, this distinction bootstraps a predictive self-model that maps joint configurations to three-dimensional body occupancy, capturing how the robot's body changes with action. In multi-agent scenes involving humans or morphologically identical robots, the system reliably identifies itself, learns a 3D self-model, and supports downstream tasks including target reaching, collision-aware motion planning, and human-to-robot motion retargeting. Together, these results outline a route toward bodily self-representation in robots that act and coordinate alongside others in shared physical environments. Project page: https://euron-zc.github.io/humanoid-self-model/.
- URL: https://arxiv.org/abs/2606.13222
- Date: 2026-06-11T11:38:34+00:00
- Deep score: 0.2

### 9. Show HN: I applied Lyapunov stability theory to detect when LLM agents spiral
- Summary: No summary
- URL: https://github.com/vishal-dehurdle/state-harness
- Date: 2026-06-11T11:21:54+00:00
- Deep score: 0.0

### 10. Multi-Modal Multi-Agent Robotic Cognitive Alignment enabled by Non-Invasive Consumer Brain Computer Interfaces: A Proof of Concept Exploration
- Summary: While non-verbal behaviors and expressive movements are essential for natural human-robot interaction, existing methods often overlook a crucial element: the human's internal cognitive state. Frequently, proactive multi-agent systems can interrupt humans at inopportune moments, leading to cognitive overload and decreased task performance. This paper introduces a framework for generating "cognitively aligned" multi-agent interactions, enhancing the ability of robotic systems to contextually defer communications to the user of an agent system during moments of high human mental workload and engagement. We present the design and implementation of a closed-loop architecture that explores the interplay between autonomous task execution and real-time neurophysiological focus. Using a consumer-grade Brain-Computer Interface (BCI), our approach continuously monitors Electroencephalography (EEG) spectral band powers while a human performs an engagement-inducing task. We propose an engagement-driven pipeline where an HTTP-based signaling mechanism places a primary agent's sensory inputs and audio outputs into a holding state upon detecting high engagement. This allows secondary agents to seamlessly process complex, delegated tasks in the background. Once the human's cognitive state returns to a lower cognitive load baseline, the primary agent releases the queued agent message. Our preliminary results demonstrate the feasibility of leveraging real-time signal processing, Large Language Models (LLMs), and physical robotic embodiments to create cognitively-aware, non-intrusive multi-agent systems.
- URL: https://arxiv.org/abs/2606.13190
- Date: 2026-06-11T10:58:31+00:00
- Deep score: 0.2

### 11. MemRefine: LLM-Guided Compression for Long-Term Agent Memory
- Summary: Large language model (LLM) agents are increasingly expected to operate over long-term interactions, where information from past dialogues must be preserved and recalled to support future tasks. However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence. Furthermore, this is especially limiting on resource-constrained platforms with hard memory budgets, motivating us to formulate storage-budgeted memory management, the task of keeping an already constructed memory store within a fixed budget while preserving information useful for future interactions. To this end, we then propose MemRefine, an LLM-guided framework that, since surface similarity poorly reflects factual value, uses similarity only to propose candidate pairs and defers delete, merge, and preserve decisions to an LLM judge based on factual content, iterating until the budget is met. Across multiple memory frameworks and long-term conversation benchmarks, MemRefine consistently meets target budgets while preserving downstream performance and outperforming rule-based baselines under tight budgets.
- URL: https://arxiv.org/abs/2606.13177
- Date: 2026-06-11T10:46:17+00:00
- Deep score: 0.2

### 12. MIDSim: Simulating Multi-Channel Information Diffusion in Social Media with LLM-Powered Multi-Agent System
- Summary: Information diffusion in social media shapes public opinion and collective behavior, making its modeling and simulation an important research problem. Existing studies have investigated information diffusion through epidemic-based, cascade-based, and point process models. However, they predominantly focus on diffusion through social links, overlooking other diffusion channels enabled by platform algorithms (e.g., recommender systems) and failing to capture user behavioral complexity. To address these limitations, we propose an LLM-powered multi-agent system for simulating multi-channel information diffusion, where large language models instantiate personalized user agents and the diffusion process jointly models social and algorithmic exposure streams. We further construct three real-world diffusion dataset spanning Sina Weibo, RedNote, and Twitter, containing diffusion records, user profiles, historical posts, and social relationships. Experimental results on real diffusion events show that our proposed framework realistically simulate macro diffusion phenomenon and generate diverse comment content, significantly outperforming baselines.
- URL: https://arxiv.org/abs/2606.13140
- Date: 2026-06-11T10:05:11+00:00
- Deep score: 0.1

### 13. Y-BotFrame: An Extensible Embodied Agent Framework for Quadruped Robot Assistants
- Summary: Quadruped robots are capable of traversing a wide range of complex terrains with high flexibility. As highly mobile ground-based intelligent platforms, they can be equipped with modules for navigation control, environmental perception, and intelligent interaction, thereby serving as real-world mobile deployment platforms for various algorithms. In this paper, we introduce Y-BotFrame, an extensible embodied platform that turns a robot into an intelligent ground assistant. Y-BotFrame integrates multimodal perception capabilities, including speech, vision, and LiDAR, and employs a large language model as the cognitive core for environmental understanding, contextual reasoning, and task planning. The system maps user natural-language instructions into executable embodied task units that can be carried out by the robot. Y-BotFrame supports natural interaction through voice commands and visual feedback, removing the need for a remote controller and enabling efficient human-robot collaboration. With a highly extensible framework, Y-BotFrame supports plug-and-play integration of new functional modules as well as modular upgrades and iterative development, offering a reference implementation for the real-world deployment of general-purpose, instruction-driven embodied agents.The supplementary video is available at https://xdei-group.github.io/Y-BotFrame/.
- URL: https://arxiv.org/abs/2606.13049
- Date: 2026-06-11T08:33:43+00:00
- Deep score: 0.2

### 14. Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems
- Summary: Large Language Model based Multi-Agent Systems (LLM-MAS) have emerged as a powerful paradigm for tackling complex tasks by breaking them into collaborative workflows of specialized LLM-powered agents. However, deploying such multi-agent workloads at scale poses significant system challenges. Each user query spawns an iterative pipeline of LLM calls, greatly amplifying resource consumption compared to single-turn queries. In resource-constrained cloud settings, these workflows face non-deterministic and input-dependent costs at decode stage, heavy-tailed multi-model requirements with memory fragmentation and over-provisioning, and cross-cluster scheduling trade-offs. We present Maestro, a workload-aware scheduling system designed for LLM-MAS serving under strict GPU budgets. Maestro explicitly leverages agent semantics and roles: it predicts the output length and memory usage of each stage and uses this prediction to drive a hierarchical scheduler. At the node level, Maestro enables dynamic multi-model co-location via hierarchical weight caching and elastic memory provisioning. At the cluster level, it performs latency-aware routing to avoid cold-start delays and memory overloads. At the global level, it enforces workflow-aware prioritization to minimize head-of-line blocking for interactive tasks. Across prototype experiments and trace-driven simulations, Maestro reduces KV-reservation HBM by 67.2% and improves high-contention SLO attainment over EDF by 23.6 percentage points.
- URL: https://arxiv.org/abs/2606.12950
- Date: 2026-06-11T06:22:39+00:00
- Deep score: 0.2

### 15. Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory
- Summary: Long-running LLM agents accumulate interaction histories far larger than any context window, forcing a standing decision: what to encode deeply, what to forget, and what to retrieve under a fixed memory budget. Production systems answer with semantic similarity or recency -- both mis-specified for the forgetting decision, which is made at consolidation time before the future query is known. We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank. We make a methodological point: on LongMemEval, scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at \approx 0.98 -- this measures retrieval, not forgetting. In the realistic blind regime, a learned multi-factor value retains 0.770 \pm 0.011 of gold evidence across 479 usable cases, versus 0.657 for uniform weights, 0.518 for the best single factor, and 0.368 for recency; every paired gap's 95% bootstrap CI is above zero, and a neural network over the same factors ties the linear model. The learned weights are interpretable -- reliability, emotional intensity, and self/user relevance dominate, while query-time goal similarity is correctly down-weighted for the forgetting decision. A controlled synthetic task with planted confounds confirms the learner recovers a separating weighting (1.00 retention) where uniform weighting fails (0.62). The substrate is open-source; all experiments run on a single CPU with no API calls.
- URL: https://arxiv.org/abs/2606.12945
- Date: 2026-06-11T06:17:31+00:00
- Deep score: 0.2

### 16. MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems
- Summary: Hierarchical multi-agent systems (MAS) are rapidly being deployed in high-stakes workflows across domains such as finance and software engineering. In these systems, safety and security are inherently distributed across role-specialized agents, significantly expanding the attack surface, particularly under coordinated adversarial behaviors such as privilege escalation and cross-agent collusion. Existing red-teaming approaches for MAS remain limited: they rely on heuristic selection of target agents and perturb isolated message streams, leaving critical questions unanswered as which agents are most responsible for system safety, and how compromised agents can coordinate to bypass defenses. We propose MAStrike, a closed-loop framework for collusive red-teaming in hierarchical MAS. We propose the first agent-level Shapley value analysis for MAS, quantifying each agent's marginal contribution to system robustness under task-specific distributions. GGuided by this attribution, MAStrike identifies vulnerable agent coalitions and generates coordinated, role-aware adversarial manipulations. These attacks are iteratively refined through structured causal diagnosis, attributing failure cases to uncompromised agents that block adversarial attempts. We further build a comprehensive MAS red-teaming benchmark and controllable environments spanning diverse hierarchical topologies and domains, including finance, software engineering, and CRM. Extensive experiments across MAS built on multiple frontier models show that MAStrike substantially outperforms heuristic baselines. Our analysis further uncovers non-trivial Shapley value distributions and higher-order interaction structures among agents, revealing critical vulnerabilities and coordination patterns that are overlooked by prior single-agent or template-based methods.
- URL: https://arxiv.org/abs/2606.12918
- Date: 2026-06-11T05:21:39+00:00
- Deep score: 0.2

### 17. AI agent runs amok in Fedora and elsewhere
- Summary: No summary
- URL: https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/
- Date: 2026-06-11T00:10:08+00:00
- Deep score: 0.0

### 18. xAI fired an engineer who raised alarms about Grok safety, new lawsuit claims
- Summary: A former xAI engineer is suing the company and SpaceX, alleging he was fired for raising AI safety concerns about Grok days before SpaceX's historic IPO.
- URL: https://techcrunch.com/2026/06/10/xai-fired-an-engineer-who-raised-alarms-about-grok-safety-new-lawsuit-claims/
- Date: 2026-06-10T22:31:19+00:00
- Deep score: 0.0

### 19. DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems
- Summary: Multi-agent systems are integral tools for various domains such as robotics, cybersecurity, and autonomous vehicle planning. These types of systems often have constraints on the computational resources, leading to a need for efficient lightweight algorithms. Traditional decision making frameworks often assume ideal conditions, such as full observability and unlimited computational capacity, which do not align with real-world challenges. In this paper, we introduce a new algorithm that allows for reduced demand on computational resources without a large cost of other performance metrics. Agents will limit their observability to some attention radius, which intentionally allows them to ignore parts of the environment that might be unnecessary for action planning. By optimizing both the attention radius and decision-making, our approach enhances coordination and scalability in uncertain environments. Through both theoretical analysis and empirical validation, we demonstrate the effectiveness of adaptive observation in improving system performance and maintaining robust decision-making strategies in resource-constrained systems.
- URL: https://arxiv.org/abs/2606.12614
- Date: 2026-06-10T19:14:56+00:00
- Deep score: 0.5

### 20. How memory tools can make AI models worse
- Summary: New research suggests that AI memory systems can degrade model performance and encourage sycophantic tendencies.
- URL: https://techcrunch.com/2026/06/10/how-memory-tools-can-make-ai-models-worse/
- Date: 2026-06-10T16:11:08+00:00
- Deep score: 0.1

### 21. Apache Burr: Build reliable AI agents and applications
- Summary: No summary
- URL: https://burr.apache.org/
- Date: 2026-06-10T15:01:06+00:00
- Deep score: 0.0

### 22. Lua.ex: Sandboxed Lua 5.3 on the Beam, Built for AI Agents · Lua.ex
- Summary: No summary
- URL: https://deflua.com/
- Date: 2026-06-10T13:44:54+00:00
- Deep score: 0.0

### 23. A €0.01 bank transfer could compromise a banking AI agent
- Summary: No summary
- URL: https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/
- Date: 2026-06-10T13:39:11+00:00
- Deep score: 0.0

### 24. Jedify raises $24M to help companies arm AI agents with context on their business
- Summary: The funding round was led by Norwest, with participation from S Capital VC, Cerca Partners, and Oceans Ventures. Snowflake Ventures also participated as a strategic investor.
- URL: https://techcrunch.com/2026/06/10/jedify-raises-24m-to-help-companies-arm-ai-agents-with-context-on-their-business/
- Date: 2026-06-10T13:33:09+00:00
- Deep score: 0.0

### 25. Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction
- Summary: Benchmarks are essential for evaluating embodied spatial intelligence, yet their construction is labor-intensive, hard to reuse, and difficult to maintain. Existing embodied benchmarks are often static and may quickly become saturated as models improve, limiting their ability to distinguish new capabilities. We propose Embodied-BenchClaw, an autonomous agentic system for constructing embodied spatial intelligence benchmarks. Given a user-specified evaluation intent, Embodied-BenchClaw automatically produces a complete and continually updatable benchmark package through a five-stage pipeline: intent blueprinting, data collection, structuring and cleaning, benchmark synthesis, and evaluation reporting. The pipeline is coordinated by three agents for planning, construction, and evaluation. To improve reusability and reliability, Embodied-BenchClaw introduces an extensible Skill Library and process quality control, enabling benchmark construction to be composable, verifiable, and repairable. We instantiate multiple benchmarks covering indoor spatial reasoning, outdoor spatial reasoning, robotic manipulation, quadruped robot navigation, UAV/aerial-view understanding, and static benchmark enhancement. These benchmarks span diverse embodied carriers, data sources, and spatial capabilities. Experiments with human evaluation, judge-based assessment, consistency checks, cost analysis, and ablations show that Embodied-BenchClaw can construct verifiable, executable, maintainable, and diagnostically useful embodied spatial benchmarks with reduced manual effort.
- URL: https://arxiv.org/abs/2606.11909
- Date: 2026-06-10T10:37:27+00:00
- Deep score: 0.4

### 26. FanRuan holds Data and AI Summit 2026 in Hong Kong to advance trusted AI decision-making - Vietnam Investment Review - VIR
- Summary: FanRuan holds Data and AI Summit 2026 in Hong Kong to advance trusted AI decision-making&nbsp;&nbsp;Vietnam Investment Review - VIR
- URL: https://news.google.com/rss/articles/CBMiuwFBVV95cUxNSzRPTTR6dXFERlRMZTU5Mm14dXFNbE5NM19JblMzZFBMS1RHeGpZSXU5alVHN0hfb2dNRmxxUEJSRnpMZ0Jkb09TaUZWYk9HSWhVUktlcjdKaGFEbENBMkc4VjZPbjM1VUMxQ0U0NTZfbThOWHJnVzFLNVZCeVJPQUtFQ09WemgwMlNvSE9adGgwdTBoTkpzZUFWQml2WjhXVmxGOWp6MWFMOXA3MEJRSEo0RHlKTFFsd0V3?oc=5
- Date: 2026-06-10T08:32:07+00:00
- Deep score: 0.1

### 27. SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems
- Summary: LLM-based multi-agent systems (MAS) solve complex tasks through inter-agent collaboration, but their communication-driven nature also allows security risks to spread across agents and trigger system-wide failures. Existing MAS defenses mainly follow a reactive paradigm after execution by detecting and isolating harmful agents, which may cause irreversible damage and degrade collaborative utility. To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard). SAIGuard performs communication-state simulation over the MAS interaction graph, estimates the impact of incoming messages on local agent states and the global MAS state, and detects risky messages via reconstruction deviations from benign communication patterns. Instead of isolating agents, SAIGuard sanitizes or regenerates suspicious messages before it propagation into system. Experiments across diverse topologies and attack scenarios show that SAIGuard reduces attack success rates while maintaining MAS utility, outperforming reactive defenses.
- URL: https://arxiv.org/abs/2606.12474
- Date: 2026-06-10T05:37:58+00:00
- Deep score: 0.1

### 28. MedMisBench: Measuring Epistemic Resilience of LLMs Under Misleading Medical Context
- Summary: Large language models (LLMs) now reach expert-level scores on medical licensing exams, encouraging the assumption that high scores imply safe medical judgment while patients increasingly use them for health advice. We show this assumption is fragile: when misleading context is injected into questions that LLMs originally answer correctly, they abandon the correct answer. We call the ability to maintain correct judgment under adversarial context epistemic resilience, and introduce MedMisBench to measure it. MedMisBench contains 10,932 medical question items and 48,889 misleading context-option pairs spanning medical reasoning, agentic capability, and patient-journey evaluation. Across 11 model configurations, mean accuracy falls from 71.1% on original questions to 38.0% under focused misleading context, with 51.5% attack success. The most damaging injections are formal, rule-like fabrications: authority-framed falsehoods reach 69.5% attack success and exception-poisoning claims reach 64.1%. A 14-member clinical panel from 7 countries identified serious potential harm in 38.2% of reviewed cases. MedMisBench exposes a structural blind spot in LLM evaluation in medical settings: existing benchmarks measure what models know, but not whether they preserve correct medical judgment under misleading context.
- URL: https://www.biorxiv.org/content/10.64898/2026.05.25.727671
- Date: 2026-06-10T00:00:00+00:00
- Deep score: 0.1

### 29. Distinct neural correlates for focusing on similar memory contents originating from current or previous experience
- Summary: Flexible, goal-directed behavior depends on the ability to select and prioritize information from memory representations freshly encoded from the sensory stream as well as retrieved from previous experience. The spatial gating signatures of internal attention in working memory (WM) are increasingly well characterized, but it remains unclear whether the same neurophysiological mechanisms are recruited for orienting attention to items from long-term memory (LTM). We recorded EEG and eye movements while participants focused on WM versus LTM representations in a unified precision-report task. Retrocues improved performance for both WM and LTM items, but with larger behavioral gains for WM items. Neural and oculomotor markers of spatial orienting, including contralateral posterior alpha suppression and gaze biases toward remembered locations, were robust when focusing on WM items; but were reliably weakened or absent when focusing on LTM items. Multivariate pattern analyses provided complementary evidence for the recruitment of dissociable neural mechanisms when focusing on WM vs. LTM items, which unfolded with similar time courses. Together, the results establish the existence of dissociable neural mechanisms for internal attention, which can be deployed flexibly depending on the relevant memory trace to guide performance. The findings raise interesting and tractable questions about whether differences in representational formats or representational domains drive the distinct internal attention mechanisms.
- URL: https://www.biorxiv.org/content/10.64898/2026.06.05.730490
- Date: 2026-06-10T00:00:00+00:00
- Deep score: 0.1

### 30. Show HN: The agent that builds and operates its own SaaS tools
- Summary: For context, we started working on our general AI agent CraftBot before OpenClaw came out. It works similarly to OpenClaw and Hermes agent: control your PC to do task + memory + proactivity. However, here is the catch: it can create and operate its own SaaS tools with the concept of Living UI<p>Living UI is a system where an AI agent can scaffold and launch real, working web apps on demand. Each living UI can be a dashboard&#x2F;software&#x2F;internal tool. They are essentially just frontend with X techstack talking to a backend + database with the techstack of your choice, spun up in its own pair of ports as supervised subprocesses managed by a host process. The backend owns all the state (so the app survives page reloads, tab switches, even host restarts), while the frontend is just a dumb view that fetches data and posts user actions. CraftBot can create a project from a template, install dependencies and launch it. It can also read and write its data through a scoped HTTP client, plus built-in endpoints that return a DOM snapshot and a screenshot so the agent can see what&#x27;s on screen.<p>Currently, there are 3 ways to create a living UI<p>(1) Build from scratch. Just describe what you want, and CraftBot generates the backend, API, and UI, then iterates with you.<p>(2) Install from the marketplace. Use ready-to-use apps built by the community (we are looking for contributors!).<p>(3) Import your existing project or GitHub repo. CraftBot converts it into a Living UI and integrates itself into it (similar to CLI-anything, except the app runs directly in the agent UI).<p>Besides, if CraftBot encounters a problem it can’t solve with a simple script, it invents the Saas tool required to solve it proactively (with user approval, of course). It’s not just building a UI for you, but it’s building a workspace for itself to be more efficient.<p>The net effect: You no longer have to subscribe to Saas tools that are not built 100% for your needs, plus, the Saas tools …
- URL: https://craftbot.live
- Date: 2026-06-09T23:44:41+00:00
- Deep score: 0.1

