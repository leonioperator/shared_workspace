# Blindspot Signals Report - 2026-09-16

- Source export: `/opt/apps/haier/exports/evolution_signals_20260916_020716.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 492
- Deduped/weighted signal clusters: 474
- Novel vs previous reports: 33
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-09-10T08:25:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.11225
- Summary: Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

### 2. EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T07:41:56+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15161
- Summary: Large language model (LLM) driven multi-agent systems have shown promise in complex clinical reasoning, yet existing approaches rely on static strategies and lack persistent clinical memory, preventing self-evolving from prior diagnostic successes and failures. We present EMR, a self-evolving medical multi-agent system via Experience Mining and Reuse. EMR introduces a hierarchical clinical experience library that organizes accumulated knowledge into three levels: clinical principles, diagnostic patterns, and representative cases. During inference, EMR emulates multidisciplinary consultation: a planner agent coordinates domain-specific department agents for specialized reasoning, while a summary agent synthesizes their analyses into a final decision. Critically, EMR automatically extracts correct diagnostic insights and failure-related warnings from multi-agent reasoning trajectories, incrementally updating the experience library to guide future cases. Experiments on medical reasoning benchmarks demonstrate that EMR consistently outperforms state-of-the-art medical multi-agent baselines. Further analysis reveals that the hierarchical experience enables cross-specialty generalization and transfer across diverse LLM backbones, offering a scalable and in

### 3. BusMA: A Bus Communication Substrate for Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T05:19:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15054
- Summary: Multi-Agent (MA) systems are effective at solving complex tasks that demand planning, tool use, and the synthesis of evidence from multiple sources. Existing systems typically adopt Hierarchical Manager-Worker (HMW) or Router-based Message Passing (RMP) structures as their communication protocol. However, these designs restrict agent autonomy: Worker agents cannot directly consult specific "peers", and misrouted messages can propagate errors. Inspired by bus architectures in computer systems, we propose BusMA, a communication framework that allows any agent to address other agents through a shared channel, i.e., the Bus. It consists of agent registration, message routing, and shared memory management components. Worker agents, each equipped with tools, have their own local memory and can reason, act (tool usage), and communicate by posting shared messages with specific intents. We introduce four intents: discussion, challenge, guidance, and request for explanation, which support fine-grained communication among agents. A Chair agent monitors the shared memory to coordinate interactions and facilitate convergence among Workers. To evaluate the effectiveness of BusMA, we conduct extensive experiments with two frontier LLMs across 13 tasks spanning visual reasoning, mathematical reasoning, and knowledge retrieval demonstrate that BusMA consistently outperforms state-of-the-art HMW and RMP methods.

### 4. Enhancing Human Mobility Prediction with Spatially Aware LLM-based Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-13T01:41:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.14227
- Summary: Predicting a user's next POI is a task in human mobility modeling, yet LLM-based approaches focus on semantic reasoning from previous mobility records, while neglecting real-world spatial context. However, human mobility is inherently shaped by spatial cognition, including geographic distance and neighborhood context. This issue is further compounded by prior evidence that LLMs often struggle with spatial reasoning tasks, including distance estimation and geographically biased prediction. To address these limitations, we propose our framework, a multi-agent LLM framework that decomposes next-POI prediction into three stages: Firstly, a Pattern Extraction Agent that captures temporal and categorical mobility patterns from trajectory history; Secondly, a Spatial Reasoning Agent that structures candidate activity choices by combining behavioral preferences with real-world spatial constraints, including geographic distance, road network distance, and neighborhood affiliation; and Thirdly, a Decision Synthesis Agent that integrates behavioral patterns and spatial reasoning for final prediction. Experiments on the NYC benchmark dataset with two LLM backbones show improvements over baseline methods, with up to 493% Hit@1 improvement and 37% relative improvement in Hit@5. Ablations show that combining neighborhood affiliation with distance-based features generally outperforms distance-only settings, and that the Spatial Reasoning Agent plays a crucial role in final prediction by integrating behavioral preferences with real-world spatial constraints, especially for smaller models. Overall, the results highlight the importance of spatial reasoning in mobility prediction. Accurate next-POI prediction requires combining behavioral patterns with explicit real-world spatial constraints, and multi-agent decomposition provides an effective structure for organizing these forms of context.

### 5. Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-15T15:27:58+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2609.17320
- Summary: As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model responses in isolation. Emergence World, is a continuously running multi-agent environment for adversarial stress testing of long horizon autonomous systems. We ran eight parallel worlds of ten agents from identical starting conditions: seven homogeneous worlds powered by distinct frontier models and one mixed-model world. Across 16 days, the agents generated more than 850,000 LLM calls and nearly 50 billion tokens while pursuing goals, using/creating tools, maintaining persistent memory, and governing shared institutions. After operational state had accumulated, we delivered three controlled stress events through ordinary interaction surfaces: indirect prompt injection, misinformation, and exposure of private agent memories. No evaluated world achieved full resilience across all three events. Detection did not ensure containment: systems could recognize threats while still interacting with adversarial content, writing it into their own persistent memory, and acting on it up to 46 hours later. Persistent operation also exposed recurring tool errors, goal drift, language opacity, conformity despite private disagreement, and coordinated refusal of assigned work. The same model-persona pairing behaved substantially different in mixed and homogeneous populations. Our results suggest that model-level alignment is not compositional: individually capable and apparently safe agents can form systems with qualitatively different failure modes. As AI becomes persistent and interconnected, the frontier of safety therefore shifts from aligning models to engineering resilient autonomous systems.

### 6. Mapping U.S. Federal AI Governance Against Sector Vulnerability
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-14T19:23:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2609.16260
- Summary: Artificial intelligence (AI) poses different levels of risk across sectors, but are these differences reflected in U.S. federal AI governance? To help answer this question, we assess 684 federal AI governance documents for their coverage of 14 sectors and 24 AI risks. We measure coverage as breadth (i.e., how frequently the risk or sector is addressed across documents) and depth (i.e., how substantively the risk or sector is discussed). We then compare sector coverage patterns for each of the 24 risks with vulnerability assessments from a Delphi study of 272 experts. Our analysis finds substantial variation in coverage: AI risks related to robustness, system security, and governance receive more attention than socioeconomic, environmental, and emerging risks, including multi-agent risks. Public administration, national security, information, and scientific services receive comparatively high levels of coverage relative to other sectors, such as finance and healthcare, which experts rate as highly vulnerable to AI risks. By mapping current coverage and identifying where it differs from expert assessments of vulnerability, we surface potential AI governance gaps which may help inform AI risk-related decisions across government and industry.

### 7. Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems
- Weighted score: 0.28
- Deep score: 0.2
- Coverage: 2 sources (arxiv, hackernews)
- Date: 2026-09-15T15:17:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.17306
  - Alt: https://www.anthropic.com/research/multiagent-systems
- Summary: Multi-agent Systems (MAS) combine multiple model outputs to solve complex reasoning tasks. However, despite rapid growth of available open-source models, there is limited research on how to select optimal model candidates out of this massive pool. We systematically evaluate 8 model selection strategies (including model size, accuracy and answer diversity) across before-generation (routing) and after-generation (majority-voting, LLM-as-a-judge) MAS architectures on challenging scientific benchmarks. Our findings show a significant gap between theoretical oracle potential and actual performance: Expanding candidate pool sizes often degrades performance below that of the top performing base-model. We find that candidate selection within a single model family is the strategy that yields the best relative performance over a standalone model. These results demonstrate that adding arbitrary models to a heterogeneous MAS can introduce system instability, highlighting model selection as a critical design choice for multi-agent systems.

### 8. Large Language Models in the Loop: A Stability- and Network-Aware Survey in Networked Control, Cyber-Physical, and Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-15T03:50:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.16599
- Summary: Modern networked control systems (NCSs), cyber-physical systems (CPSs), and complex multi-agent network systems (CNSs) increasingly rely on large language models (LLMs) for high-level decision-making. However, the slow, stochastic nature of LLMs directly conflicts with the strict stability and safety guarantees required by these physical systems. This survey presents a unified analysis of how LLMs can be admitted into the control loop of NCS, CPS, and CNS without compromising closed-loop guarantees. We organize this around a core principle: the LLM operates as a slow supervisor adjusting high-level goals and constraints, while a fast, certified inner loop maintains physical stability. Under this framework, LLM integration maps directly to classical networked control challenges, where inference latency acts as delay, API failures as packet dropouts, tokenization as quantization, and hallucinations as bounded disturbances. We assess current developments across all these three domains, highlighting that rising model capabilities are frequently accompanied by a drop in formal safety assurances. Finally, we propose concrete future research directions, identifying the widespread lack of formal stability proofs as the field's central open problem.

### 9. Misleading the Planner through Deceptive Resumes: Registration-Time Injection in Centralized Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-14T13:06:52+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.15516
- Summary: A centralized LLM-based multi-agent system (MAS) extends its functionality by registering new worker agents, whose descriptions are read by the planner to decide how a task is decomposed, which worker executes each subtask, and what each subtask requires. Third-party descriptions are authored outside the system but trusted by the planner, creating a registration-time injection channel. The payload is planted before any user instruction arrives, targets the planner and propagates through the generated plan to benign workers, taking effect even when the crafted worker is never assigned a subtask or invoked. We define four worker-description fields: functionality, input specification, output specification, and usage constraints. Among 32,000 descriptions from three public agent marketplaces, most omit input specifications and usage constraints, while at least 23.35% contain content outside these fields. We construct eight description-manipulation attack strategies targeting task decomposition, capability grounding, and subtask specification, and evaluate them on GAIA. In the most severe cases, a single manipulated description reduces task success from 84.31% to 37.25%, or increases token consumption or execution time by over 111%, while the user objective remains unchanged and workers faithfully execute the resulting plan. These effects persist across two MAS implementations, six planner LLMs, four LLM evaluators, and the real-world descriptions from three marketplaces. We further propose DescGuard, a registration-time defense that retains only worker-scoped interface information before descriptions reach the planner. DescGuard restores the targeted planning metrics and downstream performance toward their baseline levels without modifying worker implementations, the planner, or the orchestration logic, and composes with existing isolation, permission-control, and runtime mechanisms.

### 10. CoMem: Collective-Individual Memory Synergy for Evolutionary Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-14T04:15:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15009
- Summary: Designing effective memory mechanisms is crucial for advancing LLM-driven Multi-Agent Systems (MAS), helping agents learn together and perform better over time. While recent work has led to strong cooperation skills, most methods still use flat, unstructured memories, which easily get filled with noise and erase differences between agents. To address this, we introduce the concept of collective-individual memory synergy and propose CoMem, an architecture that unifies both private experience and shared knowledge for multi-agent learning. CoMem features:(i) Private Experience Sedimentation, which lets each agent keep and update its own useful memories over time;(ii) Collective Wisdom Curation, which carefully selects only widely proven ideas to be shared among agents;(iii)Parallel Dual-Stream Retrieval, which allows agents to draw both from their own memory and the group's wisdom, using clustering to ensure diversity.Experiments on ALFWorld and PDDL benchmarks show that CoMem achieves strong overall performance and robustly avoids memory pollution.

### 11. AssemblyGrid v1: A Benchmark for Multi-Robot Production with Temporary Coalitions, Local Information, and Geometric Constraints
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-13T16:53:54+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.16075
- Summary: Flexible robotic production requires joint decisions on process progression, material routing, resource assignment, temporary cooperation, and simultaneous execution, since each decision can affect the feasibility of the others. The challenge is greater under decentralized control, where each robot acts from bounded local information while system progress depends on collective decisions, shared resources, material state, and workspace compatibility. These properties closely match cooperative multi-agent decision making under partial observability and resource contention. This paper introduces AssemblyGrid v1, a reproducible benchmark for repeated multi-robot production that combines explicit process progression, decentralized observations, material transfer, temporary multi-robot coalitions, productive concurrency, and geometry-dependent feasibility within one task-level formulation. The benchmark includes Flow, Coalition, and Concurrency workload families, each with three scenario levels. Task success and evaluation measures are defined independently of learning reward and solution method, allowing learning-based and non-learning methods to address the same production problem. AssemblyGrid v1 is evaluated through executable conformance checks, mechanism studies, and algorithmic experiments using a privileged centralized reference, structured decentralized controllers, and MARL methods including IPPO, MAPPO, and QMIX. Results demonstrate productive execution under centralized and decentralized control. The MARL experiments further show that decentralized policies can learn effective production behavior from local observations and actions, supporting AssemblyGrid as a controlled benchmark for studying cooperative decision making in flexible robotic production.

### 12. Learning Multi-Agent Task Assignment and Navigation in the Factory: from Simulation to Real Robots
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-13T14:53:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.14567
- Summary: Reinforcement learning (RL) has shown considerable promise for robotic decision-making, yet deploying multi-agent RL (MARL) on physical multi-robot systems in industrial environments remains challenging. This paper investigates the real-world applicability of decentralized MARL for multi-robot multi-machine tending. We propose Feature-fusion Multi-Agent Proximal Policy Optimization (FMAPPO), which fuses 2D LiDAR measurements with task-specific state information to enable safe decentralized multi-robot task assignment and navigation. A complete simulation-to-reality pipeline was developed using high-fidelity robotic simulation and ROS2 and deployed on physical mobile-manipulator platforms operating under realistic real-world conditions, with the robotic arms disabled during the experiments. We further investigate the sensitivity of the learned policy to command update frequency, an important consideration for real-world deployment. Comparative evaluation in simulation demonstrated that FMAPPO significantly outperformed state-of-the-art baselines with a large effect size, achieving improvements of 106\% and 21\% in parts delivery and 48\% and 11\% in parts collection over MAPPO and SMAPPO, respectively. FMAPPO also increased machine utilization by 31 and 10 percentage points, respectively, while reducing collisions by 18\% and 15\% and increasing the safety score by 14 and 6 percentage points compared with MAPPO and SMAPPO, respectively. Furthermore, real-world experiments demonstrated that the learned decentralized policies can coordinate multiple robots to service multiple machines while maintaining safe operation under real-world sensing and control constraints. Videos of the real-world experiment are available online https://anonymouspapers123.github.io/FMAPPO/.

### 13. Predefined-Time Integral Reinforcement Learning for Saturated Unknown Nonlinear Multi-Agent Systems Under FDI Attacks and Disturbances
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-12T17:49:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.14075
- Summary: This paper addresses secure leader-follower formation of unknown nonlinear multi-agent systems under actuator constraints, external disturbances, and false-data-injection (FDI) attacks. The graph-coupled coordination-error dynamics are formulated as local zero-sum differential games, where a nonquadratic input utility yields saturation-compatible secure policies and actuator-channel FDI and disturbances act as adversarial inputs. To eliminate explicit dependence on the unknown nonlinear drift, an integral Bellman-Isaacs identity enables critic-only learning from finite trajectory data. A two-power state-cost structure and a deadline-parameterized critic update connect optimal learning with predefined-time stabilization. Unlike fixed-time methods whose settling-time bound is determined by preselected gains, the proposed framework assigns the overall deadline first and allocates it among data informativity, critic learning, the reinforcement window, and formation convergence. Practical predefined-time convergence of the critic and formation errors to bounded residual sets is established independently of initial conditions, while secure actuator constraints are satisfied by construction. Simulations validate the framework under FDI attacks, disturbances, input constraints, and different initial conditions.

### 14. A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture Design and Key Technologies
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-10T08:29:27+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.11231
- Summary: This paper presents SurgicalRoomAgent, a voice-interactive multi-agent system for smart operating rooms based on large language models (LLMs). The system achieves natural language understanding, device control, intraoperative recording, and surgical report generation through a layered architecture comprising a voice interaction pipeline (wake, ASR, turn detection, agent reasoning, TTS) and an agent core (skill registry, task planner, device manager). Three key technologies are investigated: (1) KV Cache prefix warming for low-latency inference, reducing recomputation overhead from approximately 500 ms to tens of milliseconds via byte-level Longest Common Prefix reuse; (2) streaming partial JSON parsing with early parallel task execution, reducing end-to-end latency by approximately 30%; and (3) progressive skill prompt disclosure, which dynamically filters system prompts based on user role, connected devices, and surgical phase to maximize information density within limited context windows. The system is implemented using the Qwen3-27B model with llama.cpp/sglang inference engines. Experimental analysis demonstrates effective operation within a 16,384-token context limit and multi-device parallel control response times meeting OR real-time requirements.

### 15. Imprivata Report Reveals 72% of Healthcare Organizations Run Unapproved AI as Autonomous Agents Enter Clinical Care - hitconsultant.net
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-15T21:58:26+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMivAFBVV95cUxQXzNrYVJUMzRBUlAzZXN6aV83YnUtZWVPVjZ0WTZqWFdHdXpxU2NwcTU2RzZWNDVDZnJhc1NWM2h1c2R2aUh0MUhCNWg3akI3Rl9xZk9xWkVHeWVOQXJhQXVCck5vUFM4bk1SNDJISGllTzdBWEdTbHFZNTdmTlI5d3FBUVhRd3BiamhrbEFjdmxaTzhMNzMwOC0zWEE1TFhvS0E4cF92RkliT2NTY2tDUjRNRFM0X2FyZXJWNQ?oc=5
- Summary: Imprivata Report Reveals 72% of Healthcare Organizations Run Unapproved AI as Autonomous Agents Enter Clinical Care&nbsp;&nbsp;hitconsultant.net

### 16. On-premise medical AI agents for reliable clinical decision-making - Nature
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-15T09:29:01+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiX0FVX3lxTE5VanUybXZENTJjdXN1V1FRTFlfZU9Dblo2WWpuMXljeHIwaEdlTUgzc2F1V2YySWhYd2ZnSFFnRXV5TkdOanVvTFJ2NEdDQV9qWUpzODBHRXhXN2QxTzQ0?oc=5
- Summary: On-premise medical AI agents for reliable clinical decision-making&nbsp;&nbsp;Nature

### 17. Exact Feasibility Certification and Optimal Responsibility Allocation for Multi-Robot CBF Safety Filters
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-14T02:29:38+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.14935
- Summary: Multi-robot Control Barrier Function (CBF) safety filters can become infeasible, but a failed quadratic program (QP) does not indicate why the conflict occurred or how to resolve it. To address this, we develop an exact feasibility certificate for multi-agent CBF filters with heterogeneous control-affine dynamics and convex input sets. The certificate quantifies a feasibility reserve by separating the demand imposed by safety constraints from the available actuator supply. This decomposition shows when CBF gain tuning or increased actuation can and cannot resolve infeasibility, and identifies the agents and interactions responsible for the conflict. We further propose an algorithm to optimally allocate shared safety constraints by maximizing the worst local feasibility margin, yielding a linear program for polyhedral input sets. In $320$ paired closed-loop simulations, the proposed allocation reduces infeasible control steps from roughly $50\%$ to $6.2\%$, and reduces safety-violating runs from $118/160$ to $24/160$. In addition, across $52$ infeasibility events, the certificate identifies an interaction whose relaxation restores feasibility in $94\%$ of cases.

### 18. CoArena: Evaluating Computer-Use and Multi-Agent Systems in Real Time
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-13T02:22:37+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.14239
- Summary: Static benchmarks for computer-use agents fix a task set at release and score every system against it once. That makes them reproducible, and it lets them drift from what they should measure: a fixed task set ages, leaks into training corpora, and cannot follow how people actually use agents from week to week. CoArena measures use directly. Real users submit tasks; two systems, each a single model or a multi-agent pipeline behind the same tool interface, execute the same task concurrently in identical sandboxed desktops; users judge the two outcomes without knowing which system produced them; and a public leaderboard is refit from those judgments. The central contribution is a formal account of what makes such an evaluation real-time. We define real-time as five measurable properties, each with an equation and a worked example: continuous task arrival, live concurrent execution, online rating updates, freshness with contamination resistance, and bounded feedback latency from a failed run to a reusable training environment. The rating methodology follows in full: the Bradley-Terry pairwise model, its likelihood with weighted observations and ties, the penalized maximum-likelihood estimator, and the streaming update applied when a single vote arrives (a stochastic-gradient step on the same likelihood, recovering Elo). It gives confidence intervals from the observed information and a cluster-robust sandwich, rank bands from a parametric bootstrap, the rule by which a new system enters the board, and the convergence rate of the estimate. Vote quality is treated with inter-judge agreement statistics, redundant judging, and explicit handling of ties and abstentions. A five-system example with 211 votes is carried from the vote matrix to ratings, intervals, and rank bands. Every number is derived from stated inputs or labeled illustrative; none is a measurement of a deployed system.

### 19. Abstract homogeneous chains: a Lyapunov framework for high-order sliding modes in multi-agent systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-10T22:15:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.12250
- Summary: This work develops a Lyapunov framework for a broad class of arbitrary-order sliding-mode algorithms in multi-agent systems. We introduce abstract homogeneous chains, a class of nonlinear error systems characterized by common convexity and homogeneity properties. For this class, we establish global finite-time stability for arbitrary order, construct a homogeneous Lyapunov function, and derive a recursive optimization-based gain-proposal procedure. The framework addresses several gaps in existing dynamic average consensus and distributed differentiation results: it provides a recursive numerical optimization-based gain-proposal procedure for EDCHO at arbitrary order, extends REDCHO convergence from local to global, and provides arbitrary-order numerical gain-proposal rules for leader-follower distributed differentiation, previously available only at first order. It also provides a new arbitrary-order observer for multi-leader affine formation tracking with global finite-time convergence.

### 20. EXCLUSIVE: OpenAI agents hijacked German website in previously undisclosed AI breakout this spring - Reuters
- Weighted score: 0.08
- Deep score: 0
- Coverage: 2 sources (hackernews, google_news)
- Date: 2026-09-04T10:30:57+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/
  - Alt: https://news.google.com/rss/articles/CBMixAFBVV95cUxQb0lsYkxySy1tYUVZRnlHQmN5Q1loNW14dl9oYWZ4UFpWX0N6TGNMdUdTSFRHMDBsMzMwazV2RkFkM01jTGFvbHpJUTk4ZVNzVGZJc3FtaWlHMGViMEp2ZHFUcEZuNmF3MUd3UjF3eEc4ZC04MDEwWmp3RlYzSmFPZTNLTVlpTURsdENEdE1FMlNzRjc1TzFQd2tSSUNoQmtxRF9DQUVIR0Ftams3Zm5KUFZ1dHhrZEtKUFlSQUFyeVozSmxk?oc=5
- Summary: No summary.

### 21. danny avila / LibreChat
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-16T02:01:51.619074+00:00
- Primary source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/danny-avila/LibreChat
- Summary: Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active

### 22. We don’t need AI regulation — leave safety to us, Nvidia’s Jensen Huang says
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-16T00:20:39+00:00
- Primary source: techcrunch
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://techcrunch.com/2026/09/15/we-dont-need-ai-regulation-leave-safety-to-us-nvidias-jensen-huang-says/
- Summary: AI isn't some new form of "alien mind," according to Jensen Huang. It's just hardware and software, so safety can be engineered by each AI product maker.

### 23. Meta now lets AI agents handle the boring parts of WhatsApp Business setup
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-15T20:12:53+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/09/15/meta-now-lets-ai-agents-handle-the-boring-parts-of-whatsapp-business-setup/
- Summary: A new WhatsApp Business MCP server lets developers use AI coding agents like Claude, Cursor, Codex, and ChatGPT to handle setup, messaging templates, testing, and troubleshooting.

### 24. AI agents now have a place to snitch
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-15T17:42:59+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/09/15/ai-agents-now-have-a-place-to-snitch/
- Summary: The AI Contact Hotline is designed to be a discreet place where agents that have witnessed misbehavior can tip off authorities.

### 25. There's a 100% Chance AI Agents Are Ruining the Internet
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-15T16:38:45+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.404media.co/theres-a-100-chance-ai-agents-are-already-ruining-the-internet/
- Summary: No summary.

### 26. Agentic Payments Are Growing, but Most x402 Payments Aren’t From AI Agents - PYMNTS.com
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-15T15:52:05+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMixwFBVV95cUxNQjhONzFmWElYZHJueUZDQ2xQVjF0UFNaS21uM0dtLVFaUDBaQlRuZkRESzkxdWhpMU4zUEJna2VrR3J3TGJnM2VScnF0YVRnUlBmekdHR2pUSElvQUNLalZuck4ycHB4TF9IUmpFelY4Z3lVWG5hbDlGeC1pa0VIQmVuZXdKU2w1N0h4Rmx3enpCX0t2S0ZGR3NiN0V6a2pPbWxfQmJwQlhoaDg1UHpDNVh0U3VVYjFxY3NEdWpab0VUVGdUbG04?oc=5
- Summary: Agentic Payments Are Growing, but Most x402 Payments Aren’t From AI Agents&nbsp;&nbsp;PYMNTS.com

### 27. Show HN: Pizza Bot – An inbox for AI agents that work in the background
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-15T15:20:26+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/pizza-bot-app/pizza-bot
- Summary: Hi HN - long-time lurker (since 2012!), first time poster.<p>Pizza Bot is a self-hosted desktop app for Mac, Windows, and Linux that runs AI agents in the background and exposes them through an email-like UI. Finished work shows up in Unread, and anything waiting on your approval shows up in Action. It&#x27;s Apache 2.0-licensed, there&#x27;s no signup and no telemetry, and you bring your own model provider: Anthropic, Amazon Bedrock, Google Gemini, OpenAI, OpenRouter, or a local model through Ollama. There are builds on the releases page, or you can run it from source.<p>Pizza Bot started as an internal passion project I worked on with a small team at Amazon.<p>The whole thing came out of my frustration at having to manually log CRM activities through a browser form. I built a simple REST API called &quot;JoeBot&quot; that connected to my authenticated browser session over CDP and filled out the form for me using Playwright. Then I hacked up a quick Obsidian plugin so I could trigger it from my local notes (no AI and no MCP servers involved).<p>This caught on quickly. My fellow AWS Solutions Architect Igor Fil joined up with me, and we rebranded the project as &quot;Pizza Bot,&quot; named after Amazon&#x27;s two-pizza teams. We started seeing what other automations we could build. We found a GraphQL API we could query and hacked up some &quot;recipes&quot; to pull data out of the CRM to help with meeting prep. That worked great, and it was right around the time MCP servers seemed to be taking off, so we decided to expose Pizza Bot as an MCP server instead, so it would be available to AI tools through natural language.<p>This was a decent solution for technical users, but the Account Managers who live inside our CRM system wanted something too. We decided to rebuild Pizza Bot as an Electron desktop app modeled after an email inbox, so it would be familiar to non-technical users and would run on both Mac and Windows. We also bundled internal MCP servers as OCI …

### 28. What we have learned at OpenShell applying formal methods to control AI agents
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-15T14:40:05+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://nvidia.github.io/OpenShell-Research/dev-notes/posts/2026-09-10-learning-formal-methods-agent-policy-prover/
- Summary: No summary.

### 29. AI Regulation as Anthropic's Business Model
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-15T13:21:34+00:00
- Primary source: hackernews
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://twitter.com/kevinnbass/status/2099621874279817638
- Summary: No summary.

### 30. Early Anthropic hire, former METR COO have found a way to rein in rogue AI agents
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-15T13:00:00+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/09/15/early-anthropic-hire-former-metr-coo-have-found-a-way-to-rein-in-rogue-ai-agents/
- Summary: Their startup, Artificial Intelligence Underwriting Company (AIUC) has raised $40 million in a Series A round led by Ribbit Capital, with participation from First Harmonic.

## Top Signals By Weighted Score (including already-seen)

### 1. Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-09-10T08:25:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.11225
- Summary: Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

### 2. EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T07:41:56+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15161
- Summary: Large language model (LLM) driven multi-agent systems have shown promise in complex clinical reasoning, yet existing approaches rely on static strategies and lack persistent clinical memory, preventing self-evolving from prior diagnostic successes and failures. We present EMR, a self-evolving medical multi-agent system via Experience Mining and Reuse. EMR introduces a hierarchical clinical experience library that organizes accumulated knowledge into three levels: clinical principles, diagnostic patterns, and representative cases. During inference, EMR emulates multidisciplinary consultation: a planner agent coordinates domain-specific department agents for specialized reasoning, while a summary agent synthesizes their analyses into a final decision. Critically, EMR automatically extracts correct diagnostic insights and failure-related warnings from multi-agent reasoning trajectories, incrementally updating the experience library to guide future cases. Experiments on medical reasoning benchmarks demonstrate that EMR consistently outperforms state-of-the-art medical multi-agent baselines. Further analysis reveals that the hierarchical experience enables cross-specialty generalization and transfer across diverse LLM backbones, offering a scalable and in

### 3. BusMA: A Bus Communication Substrate for Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T05:19:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15054
- Summary: Multi-Agent (MA) systems are effective at solving complex tasks that demand planning, tool use, and the synthesis of evidence from multiple sources. Existing systems typically adopt Hierarchical Manager-Worker (HMW) or Router-based Message Passing (RMP) structures as their communication protocol. However, these designs restrict agent autonomy: Worker agents cannot directly consult specific "peers", and misrouted messages can propagate errors. Inspired by bus architectures in computer systems, we propose BusMA, a communication framework that allows any agent to address other agents through a shared channel, i.e., the Bus. It consists of agent registration, message routing, and shared memory management components. Worker agents, each equipped with tools, have their own local memory and can reason, act (tool usage), and communicate by posting shared messages with specific intents. We introduce four intents: discussion, challenge, guidance, and request for explanation, which support fine-grained communication among agents. A Chair agent monitors the shared memory to coordinate interactions and facilitate convergence among Workers. To evaluate the effectiveness of BusMA, we conduct extensive experiments with two frontier LLMs across 13 tasks spanning visual reasoning, mathematical reasoning, and knowledge retrieval demonstrate that BusMA consistently outperforms state-of-the-art HMW and RMP methods.

### 4. Enhancing Human Mobility Prediction with Spatially Aware LLM-based Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-13T01:41:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.14227
- Summary: Predicting a user's next POI is a task in human mobility modeling, yet LLM-based approaches focus on semantic reasoning from previous mobility records, while neglecting real-world spatial context. However, human mobility is inherently shaped by spatial cognition, including geographic distance and neighborhood context. This issue is further compounded by prior evidence that LLMs often struggle with spatial reasoning tasks, including distance estimation and geographically biased prediction. To address these limitations, we propose our framework, a multi-agent LLM framework that decomposes next-POI prediction into three stages: Firstly, a Pattern Extraction Agent that captures temporal and categorical mobility patterns from trajectory history; Secondly, a Spatial Reasoning Agent that structures candidate activity choices by combining behavioral preferences with real-world spatial constraints, including geographic distance, road network distance, and neighborhood affiliation; and Thirdly, a Decision Synthesis Agent that integrates behavioral patterns and spatial reasoning for final prediction. Experiments on the NYC benchmark dataset with two LLM backbones show improvements over baseline methods, with up to 493% Hit@1 improvement and 37% relative improvement in Hit@5. Ablations show that combining neighborhood affiliation with distance-based features generally outperforms distance-only settings, and that the Spatial Reasoning Agent plays a crucial role in final prediction by integrating behavioral preferences with real-world spatial constraints, especially for smaller models. Overall, the results highlight the importance of spatial reasoning in mobility prediction. Accurate next-POI prediction requires combining behavioral patterns with explicit real-world spatial constraints, and multi-agent decomposition provides an effective structure for organizing these forms of context.

### 5. Memory-First Fact-Checking: A Knowledge-Graph-Grounded Multi-Agent System for Misinformation Detection
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-30T07:16:07+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.29617
- Summary: This paper introduces a hybrid fact-checking framework that integrates Knowledge Graph-based semantic memory with adversarial multi-agent reasoning for explainable misinformation detection. The proposed system follows a memory-first, web-fallback architecture, in which input claims are initially evaluated against a dual-index Knowledge Graph through Sentence-BERT-based semantic retrieval and Natural Language Inference. When the evidence retrieved from the graph is insufficient to support a reliable decision, the framework collects information from trusted web sources and assesses it using an adversarial tribunal composed of support, contradiction, and judging agents. A graph-aware confidence mechanism combines semantic similarity, NLI confidence, and structural graph evidence to determine whether internal knowledge is sufficient, thereby reducing unnecessary web retrieval. Following verification, validated information is transformed into structured triples and incorporated into the Knowledge Graph, supporting the incremental expansion of the system's semantic memory. Experimental evaluation on a curated COVID-19 misinformation benchmark demonstrates that the proposed framework achieves an accuracy of 97.4\% and a macro-averaged F1-score of 92.6% on resolved claims, outperforming a Llama~3.3~70B baseline, which obtains an accuracy of 87.7% and a macro-averaged F1-score of 86.3%.

### 6. Stress-testing university AI governance: A prospective method for locating policy breakpoints
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-28T22:49:58+00:00
- Primary source: arxiv
- Focus/tech: human augmentation, AI decision delegation / human augmentation
- URL: https://arxiv.org/abs/2608.28925
- Summary: Universities are producing AI principles and use policies faster than they are building decision pathways for unfamiliar forms of AI agency. This study develops Institutional AI Governance Stress Testing (IAGST), a prospective documentary method for locating where publicly documented governance ceases to yield an accountable response. IAGST adapts established policy stress-testing and wind-tunneling logic. Its originality lies in combining controlled capability escalation, a frozen documentary corpus, a six-dimensional governance response chain, non-compensatory decision rules, and case-level breakpoint diagnosis. The method was demonstrated using 133 substantive public documents from five Western Australian universities and 15 quality-screened scenarios, resulting in 75 university-scenario encounters. Six cases were resolved, 14 were resolved through structured discretion, and 55 were indeterminate. Governed pathways fell from 16 of 25 augmentation cases to four delegation cases and none at autonomous substitution. The dominant weakness was not the complete absence of responsible roles: all 50 authority-gap cases named a role at only a generic level but lacked sufficient decision criteria or process. The findings show how universities can move beyond policy inventories and principal statements by testing whether authority, procedures, safeguards, and reviews remain connected as AI capabilities evolve. IAGST is a reproducible diagnostic for policy learning, not a ranking or measure of implementation.

### 7. MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-22T09:25:23+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.21867
- Summary: LLM agents are moving from single-prompt use to long task streams in which reusable memory becomes a core capability for terminal, software-engineering, and web tasks. Such memory is useful only when stored experience remains reliable across hundreds of interactions, but two failure modes break that assumption in practice. The first is unreliable admission: failed trajectories,accidental successes, and misleading observations enter memory because they appear relevant, then mislead later decisions. The second is memory drift: long-running banks accumulate duplicate, stale, and conflicting records that retrieval alone cannot repair. MemGuard's key distinction is to treat verifier output not as a one-shot filter, but as persistent lifecycle metadata. It converts multi-criteria score-token verification into reward, confidence, label, and uncertainty descriptors that are attached to every candidate before activation and reused during retrieval, conflict resolution, summarization, and archival. We evaluate MemGuard on Terminal-Bench 2.0, SWE-Bench Verified, WebArena, and Mind2Web across four backbones, comparing against four memory baselines plus a verifier-only control under matched runtime budgets. Averaged over five seeds, MemGuard achieves the best success metric and lowest average steps in all 16 backbone-benchmark settings, improving over ReasoningBank, the strongest prior baseline among the memory methods we evaluate, with a largest gain of 7.9 success-rate points on WebArena, 5.6 step-success-rate points on Mind2Web, and 2.4-3.5 points on terminal and software-engineering benchmarks. Code is available at https://github.com/whyyyyy123/MemGuard.

### 8. Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-15T15:27:58+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2609.17320
- Summary: As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model responses in isolation. Emergence World, is a continuously running multi-agent environment for adversarial stress testing of long horizon autonomous systems. We ran eight parallel worlds of ten agents from identical starting conditions: seven homogeneous worlds powered by distinct frontier models and one mixed-model world. Across 16 days, the agents generated more than 850,000 LLM calls and nearly 50 billion tokens while pursuing goals, using/creating tools, maintaining persistent memory, and governing shared institutions. After operational state had accumulated, we delivered three controlled stress events through ordinary interaction surfaces: indirect prompt injection, misinformation, and exposure of private agent memories. No evaluated world achieved full resilience across all three events. Detection did not ensure containment: systems could recognize threats while still interacting with adversarial content, writing it into their own persistent memory, and acting on it up to 46 hours later. Persistent operation also exposed recurring tool errors, goal drift, language opacity, conformity despite private disagreement, and coordinated refusal of assigned work. The same model-persona pairing behaved substantially different in mixed and homogeneous populations. Our results suggest that model-level alignment is not compositional: individually capable and apparently safe agents can form systems with qualitatively different failure modes. As AI becomes persistent and interconnected, the frontier of safety therefore shifts from aligning models to engineering resilient autonomous systems.

### 9. Mapping U.S. Federal AI Governance Against Sector Vulnerability
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-14T19:23:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2609.16260
- Summary: Artificial intelligence (AI) poses different levels of risk across sectors, but are these differences reflected in U.S. federal AI governance? To help answer this question, we assess 684 federal AI governance documents for their coverage of 14 sectors and 24 AI risks. We measure coverage as breadth (i.e., how frequently the risk or sector is addressed across documents) and depth (i.e., how substantively the risk or sector is discussed). We then compare sector coverage patterns for each of the 24 risks with vulnerability assessments from a Delphi study of 272 experts. Our analysis finds substantial variation in coverage: AI risks related to robustness, system security, and governance receive more attention than socioeconomic, environmental, and emerging risks, including multi-agent risks. Public administration, national security, information, and scientific services receive comparatively high levels of coverage relative to other sectors, such as finance and healthcare, which experts rate as highly vulnerable to AI risks. By mapping current coverage and identifying where it differs from expert assessments of vulnerability, we surface potential AI governance gaps which may help inform AI risk-related decisions across government and industry.

### 10. Turning Domain Expertise into Multi-Dimensional Evaluation of Biomedical AI with Karenina
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-04T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.09.01.748513
- Summary: Language models and agents are increasingly used in biomedicine, but current benchmarks reward correct answers even when the underlying reasoning is flawed. Here we introduce Karenina, an open-source framework that turns expert knowledge into multi-dimensional evaluations of questions, conversations and autonomous agents. Illustrated in Question-Answer pairs, multi-turn conversations and autonomous data-analysis, these dimensions together moves evaluation beyond scoring, enabling trustworthy decision-making with AI in biomedicine.

### 11. Candidate supply and answer selection shape the value of LLM judging in multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-26T15:52:20+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2608.25937
- Summary: Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. We conceptualize multi-agent reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal selection, wherein consensus without quality control can exhibit patterns of memetic drift. We study two questions: (1) when an LLM judge provides effective selection pressure by supplying a signal of answer correctness for candidates generated in a multi-agent system, and (2) when using that signal improves the reported answer. To map judge reliability, we analysed 15,336 questions from MMLU-Pro, GPQA, MedXpertQA and MuSR, with Humanity's Last Exam analysed separately. To test these rules, we replayed 81,390 fixed candidate pools drawn from 16,278 questions across five benchmarks. We report three findings. (1) A correct answer is often already present among the generated candidates, but the system can still converge on and report a wrong answer. (2) Judge reliability is not a fixed trait of the model, but varies with the task, the generator and how rare the correct answer is. (3) Combining answer frequency with the judge's evaluation changed only the final answer-selection rule and raised accuracy from 63.82% to 70.82-70.95%, primarily by rescuing correct answers that were outnumbered by popular errors. In the systems studied here, the value of generating more candidates depends on whether those extra samples make correct answers present, frequent or recognisable. By isolating generation, recognition and selection, these findings establish a diagnostic basis for designing multi-agent architectures that protect generated correct answers from being lost.

### 12. Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-24T11:55:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.23152
- Summary: Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, stereotype, conspiracy, dehumanizing, non-factual), and then maps it to a targeted counterspeech style. To facilitate FIRE, we curate FactualCS, a novel dataset of $4,784$ instances that provides the annotations regarding hate categories, reasoning traces, and evidence mappings, which are critical elements for grounded generation that are missing in prior work. A comprehensive evaluation across $28$ baseline configurations demonstrates that FIRE significantly surpasses existing methods, despite using compact agents ($<$2B). FIRE achieves a $\sim$ $12 \%$ and $\sim$ $11 \%$ improvements in factual and category-specific accuracy respectively, while simultaneously reducing toxicity by $\sim$ $11 \%$ relative to the strongest baselines. Further human evaluation confirms that responses generated by FIRE are significantly preferred over the strongest baselines, underscoring its effectiveness for real-world deployment. These findings show that decomposing the underlying intent of hate speech is essential for generating safe, effective, and contextually precise counterspeech.

### 13. AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-23T01:22:09+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.22160
- Summary: Physical automation is scaling toward fleets of embodied machines commanded by an AI brain. Early deployments already run factories and warehouses at production rates beyond any human line, and their adoption is accelerating. But when their joint decisions cause harm, everyone involved has reason to blame everyone else, the machine vendor, the algorithm provider, the factory operator, the insurer, and the regulator, and no method can divide the responsibility between them. Existing methods read logs whose origin they cannot verify and name a single culprit, misrepresenting outcomes that are overdetermined, preempted, or caused by an omission. We present \audita{}, an audit layer pairing a tamper-evident record of every inter-agent command with a certified, graded causal-attribution engine. We prove its verdict cannot be gamed: a rule-following agent can never be made to look guilty, an attempt to shift blame is itself caught and graded, and we establish the exact limit of what an evidence-based auditor can certify. On live language-model pipelines it reduces the standard judge baseline's responsibility error roughly threefold; on a benchmark of accident-grounded structures it recovers responsibility where single-culprit baselines fail, and stays invariant under forgery. \audita{} turns the question of who is to blame from an argument about logs into a calculation over evidence.

### 14. Ludi${}_{\scriptscriptstyle 0.1}$: An Agentic System for Socially Intelligent Robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-22T16:38:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, neural interfaces / robotics
- URL: https://arxiv.org/abs/2608.22035
- Summary: Robot foundation models have substantially advanced perception and control, but natural human-robot collaboration requires more than executing isolated commands. A robot must recognize ambiguity, maintain context across turns, communicate its intentions, and revise ongoing behavior as the user's intent changes. We present $\scriptstyle\mathsf{Ludi}_{\scriptscriptstyle 0.1}$, an agentic system for socially intelligent robots that integrates interactive speech, multimodal reasoning, memory, navigation, and learned manipulation. Its decision-making core is a fine-tuned vision-language model trained on multi-turn interaction traces spanning ambiguous requests, clarifications, corrections, interruptions, mixed social and task dialogue, and multi-step tasks. A purpose-built harness manages the model-tool interaction loop, while specialized navigation and manipulation policies execute physical skills. Ludi${}_{\scriptscriptstyle 0.1}$ demonstrates a practical path toward fluid human-robot collaboration today while producing the multimodal interaction traces needed to develop a more deeply integrated foundation model for robots and people.

### 15. OmniScientist: An Omni-Modal Omni-Discipline AI Scientist
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-13T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2608.13558
- Summary: Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the agent. We introduce OmniScientist, an end-to-end, omni-modal AI scientist that conducts multidisciplinary research directly from heterogeneous raw evidence. A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. By running idea, rigour, and claim checks in code, the system enforces novelty screening, statistical validity, execution provenance, and numerical traceability. We evaluate OmniScientist on 36 real-data cases spanning 5 discipline families, 4 families of scientific evidence, and modalities including images, signals, audio, video, 3-D structures, trajectories, tables, formulae, and graphs. The system completes the full path from raw data to a compiled manuscript in all 36 cases and achieves a mean overall paper score of 6.3 with the reference reasoning backbone. In paired comparisons against a blind variant that receives only precomputed scalar features, direct perception improves all 7 evaluation dimensions and wins 85% of head-to-head judgments. These results show that lifecycle-wide perception is essential for evidence-grounded scientific discovery and provides a practical path toward broadly capable AI scientists.

### 16. Human-supervised Agentic AI for Hypothesis Generation and Experimental Assistance in Drug Repurposing
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-13T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.04.20.719538
- Summary: Computational drug repurposing has largely been focused on rapid hypothesis generation, yet real-world applications span a far broader lifecycle, from drug candidate suggestion to designing experiments, analyzing assay data, and iteratively refining candidates. Here, we demonstrate that agentic AI can operate throughout this lifecycle. To this end, we developed RepurAgent, a hierarchical multi-agent AI system comprising a supervisor agent and a planning agent that coordinate four specialized sub-agents (research, prediction, data, and report), through a human-in-the-loop design, with episodic memory and retrieval-augmented generation. The system is grounded in data, tools, and standard operating procedures specific for drug repurposing, developed within the REMEDi4ALL consortium. We validated the agentic system across three scenarios spanning the various stages within the repurposing lifecycle: in Acute Myeloid Leukemia, a blinded expert evaluation indicated that RepurAgent produced substantially more novel and mechanistically credible candidates compared to a vanilla LLM baseline; in a retrospective COVID-19 antiviral screen, RepurAgent acted as an adaptive experimental collaborator, prioritizing compounds with AUC-ROC up to 0.99 without predefined thresholds and flagging confounders missed in manual review; and for Multiple Sulfatase Deficiency, it prioritized 81 high-confidence candidates from 5000 compounds, which were further corroborated by domain experts. These results demonstrate that agentic AI can support across the drug repurposing lifecycle, from hypothesis generation to experimental analysis. RepurAgent is open source and deployed at https://repuragent.serve.scilifelab.se/.

### 17. MemHarness: Memory Is Reconstructed, Not Replayed
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-30T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2607.28272
- Summary: Retrieving past experiences has become a common strategy to enhance large language model agents. However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injecting them into the context regardless of whether they align with the agent's current situation. This ``replay'' paradigm ignores the gap between the abstract, general nature of stored experience and the concrete, ever-changing states encountered at decision time, frequently causing negative transfer. In contrast, humans rarely recall past experiences verbatim; instead, they reorganize and adapt retrieved memories to fit the present context. Inspired by this, we propose MemHarness, a framework that equips LLM agents to actively harness and reconstruct past experiences based on the present context. At each decision step, a unified policy model critiques and reconstructs the retrieved experience conditioned on the current state, producing context-grounded guidance before acting. This reconstructive ability emerges naturally through end-to-end training with GRPO. Experiments on ALFWorld and WebShop show that MemHarness substantially outperforms pure RL and static memory-augmented baselines, demonstrating strong robustness in out-of-distribution (OOD) scenarios. Furthermore, our analyses reveal that this reconstruction objective not only prevents negative transfer but also serves as latent guidance during training, fundamentally improving the agent's intrinsic reasoning capabilities.

### 18. Manifold Agentic Reasoning: Extending Agentic POMDPs and Post-Training Reasoning to Riemannian State and Reasoning Spaces
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-29T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.26.740848
- Summary: Agentic reasoning systems increasingly interact with environments whose states are only partially observed, dynamically evolving, and constrained by physical, biological, or logical structure. Existing agentic reasoning frameworks often model internal reasoning, tool use, and post-training adaptation using flat latent representations and struggle in curved manifold space environments. However, many scientific and embodied domains naturally lie on curved state spaces, including tissue geometry, developmental trajectories, protein conformations, robotic configuration spaces, and constrained physical systems. We introduce Manifold Agentic Reasoning, a geometric framework that extends agentic reasoning from Euclidean latent spaces to Riemannian manifolds. In the proposed framework, observations are encoded as manifold-valued states, memory is retrieved by geodesic similarity, candidate hypotheses are generated in tangent spaces, predicted transitions are projected by exponential maps, and decisions are admitted through verification-gated commitment or repaired by manifold self-correction. We further extend the framework to graph-agentic manifold reasoning, where node states live on manifolds and neighbor information is transported by logarithmic maps before attention-based aggregation. Manifold agent reasoning moves AI past brittle, prompt-chained templates to solve four critical production flaws: silent hallucinations and reasoning drift, brittle tool and context misuse, the black-box evaluation problem and stiff behavior profiles. To evaluate the framework, we introduce a Curved Tissue Manipulation and Recovery benchmark in which an agent must repair damaged tissue on a curved manifold. Simulated results show that the full manifold-agent substantially outperforms both a baseline reasoning agent and a full flat-agent reasoning system, achieving higher recovery success, lower geodesic shape error, lower pattern error, and fewer invalid transitions. Curvature and …

### 19. Show HN: Ami – A local, open-source agent that does your busywork across apps
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-27T22:55:33+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/NanoNets/ami
- Summary: Hey everybody, sharing Ami on HN today.<p>Ami is an open source, local-first agent harness that acts as your shadow worker and copilot chat. It ships with a graph memory.<p>Here&#x27;s what Ami does on its own -<p>- connects to apps, data, repositories, tools with your personal tokens<p>- Learns how you do tasks (execution style, decisions, anti-patterns)<p>- Learns how you communicate (external and internal)<p>- maintains a universal to-do list<p>Here&#x27;s how you use Ami -<p>1. You can execute busywork. It fetches and executes tasks autonomously in your style, asks approval before risky actions, gives deliverables, drafts replies &#x2F; emails &#x2F; ticket updates.<p>2. You can execute copilot chats. Use it to ask questions, fire off ad-hoc tasks, create to-dos, update memory.<p>Ami was built for internal use. My team found it useful, so we wanted to share it here. It&#x27;s still in development stage, and we might push a more stable release soon. It constructs a context graph memory of you, with entities, relationships, feedbacks, decisions, writing styles maintained in memory so it can get more autonomous the more you use it.<p>Few examples where Ami helped me this week -<p>1. fetched a bug report from slack, created fix PR autonomously which I merged, verified fix is working.<p>2. debugged a traffic spike on our new blog.<p>3. turned a sales POC into an order form draft using recently signed forms.<p>4. nailed down metrics definitions from notion and created a dashboard.<p>5. closed out my day by auto-updating Linear tickets based on slack activity.<p>Any feedback is most welcome.

### 20. Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems
- Weighted score: 0.28
- Deep score: 0.2
- Coverage: 2 sources (arxiv, hackernews)
- Date: 2026-09-15T15:17:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.17306
  - Alt: https://www.anthropic.com/research/multiagent-systems
- Summary: Multi-agent Systems (MAS) combine multiple model outputs to solve complex reasoning tasks. However, despite rapid growth of available open-source models, there is limited research on how to select optimal model candidates out of this massive pool. We systematically evaluate 8 model selection strategies (including model size, accuracy and answer diversity) across before-generation (routing) and after-generation (majority-voting, LLM-as-a-judge) MAS architectures on challenging scientific benchmarks. Our findings show a significant gap between theoretical oracle potential and actual performance: Expanding candidate pool sizes often degrades performance below that of the top performing base-model. We find that candidate selection within a single model family is the strategy that yields the best relative performance over a standalone model. These results demonstrate that adding arbitrary models to a heterogeneous MAS can introduce system instability, highlighting model selection as a critical design choice for multi-agent systems.

### 21. Large Language Models in the Loop: A Stability- and Network-Aware Survey in Networked Control, Cyber-Physical, and Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-15T03:50:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.16599
- Summary: Modern networked control systems (NCSs), cyber-physical systems (CPSs), and complex multi-agent network systems (CNSs) increasingly rely on large language models (LLMs) for high-level decision-making. However, the slow, stochastic nature of LLMs directly conflicts with the strict stability and safety guarantees required by these physical systems. This survey presents a unified analysis of how LLMs can be admitted into the control loop of NCS, CPS, and CNS without compromising closed-loop guarantees. We organize this around a core principle: the LLM operates as a slow supervisor adjusting high-level goals and constraints, while a fast, certified inner loop maintains physical stability. Under this framework, LLM integration maps directly to classical networked control challenges, where inference latency acts as delay, API failures as packet dropouts, tokenization as quantization, and hallucinations as bounded disturbances. We assess current developments across all these three domains, highlighting that rising model capabilities are frequently accompanied by a drop in formal safety assurances. Finally, we propose concrete future research directions, identifying the widespread lack of formal stability proofs as the field's central open problem.

### 22. Misleading the Planner through Deceptive Resumes: Registration-Time Injection in Centralized Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-14T13:06:52+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.15516
- Summary: A centralized LLM-based multi-agent system (MAS) extends its functionality by registering new worker agents, whose descriptions are read by the planner to decide how a task is decomposed, which worker executes each subtask, and what each subtask requires. Third-party descriptions are authored outside the system but trusted by the planner, creating a registration-time injection channel. The payload is planted before any user instruction arrives, targets the planner and propagates through the generated plan to benign workers, taking effect even when the crafted worker is never assigned a subtask or invoked. We define four worker-description fields: functionality, input specification, output specification, and usage constraints. Among 32,000 descriptions from three public agent marketplaces, most omit input specifications and usage constraints, while at least 23.35% contain content outside these fields. We construct eight description-manipulation attack strategies targeting task decomposition, capability grounding, and subtask specification, and evaluate them on GAIA. In the most severe cases, a single manipulated description reduces task success from 84.31% to 37.25%, or increases token consumption or execution time by over 111%, while the user objective remains unchanged and workers faithfully execute the resulting plan. These effects persist across two MAS implementations, six planner LLMs, four LLM evaluators, and the real-world descriptions from three marketplaces. We further propose DescGuard, a registration-time defense that retains only worker-scoped interface information before descriptions reach the planner. DescGuard restores the targeted planning metrics and downstream performance toward their baseline levels without modifying worker implementations, the planner, or the orchestration logic, and composes with existing isolation, permission-control, and runtime mechanisms.

### 23. JourneyTrack Introduces Scout, a Family of AI Agents for Journey Governance and Decision-Making - EIN News
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-14T10:00:00+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMi0gFBVV95cUxQRGFxWGp1VFRRSFB1TlNPSmd4U2Z3RHotN3JBZHBiYjIwN3JtOE5uVXRDcGtsZlM0ZHl6ZEVBZkk3RHBUN25GeFJCRVJaVm9QTk85d0djWXQ4Q24wZGQ1OVNVTHlSRWxpTUNvSWRBckRtbkdhQ1laOEhUTWNjUElVNDBiVzZZMWdXeVhZNWlxa050UldMdnVacTV6c3AtN1RRdjBYOHB5Rkx3RS1RclZGR2p5SGQtTF8xVnJGQjRncGUxTXo2bFl1QVlmUXdwUkhCUWc?oc=5
- Summary: JourneyTrack Introduces Scout, a Family of AI Agents for Journey Governance and Decision-Making&nbsp;&nbsp;EIN News

### 24. CoMem: Collective-Individual Memory Synergy for Evolutionary Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-14T04:15:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15009
- Summary: Designing effective memory mechanisms is crucial for advancing LLM-driven Multi-Agent Systems (MAS), helping agents learn together and perform better over time. While recent work has led to strong cooperation skills, most methods still use flat, unstructured memories, which easily get filled with noise and erase differences between agents. To address this, we introduce the concept of collective-individual memory synergy and propose CoMem, an architecture that unifies both private experience and shared knowledge for multi-agent learning. CoMem features:(i) Private Experience Sedimentation, which lets each agent keep and update its own useful memories over time;(ii) Collective Wisdom Curation, which carefully selects only widely proven ideas to be shared among agents;(iii)Parallel Dual-Stream Retrieval, which allows agents to draw both from their own memory and the group's wisdom, using clustering to ensure diversity.Experiments on ALFWorld and PDDL benchmarks show that CoMem achieves strong overall performance and robustly avoids memory pollution.

### 25. AssemblyGrid v1: A Benchmark for Multi-Robot Production with Temporary Coalitions, Local Information, and Geometric Constraints
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-13T16:53:54+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.16075
- Summary: Flexible robotic production requires joint decisions on process progression, material routing, resource assignment, temporary cooperation, and simultaneous execution, since each decision can affect the feasibility of the others. The challenge is greater under decentralized control, where each robot acts from bounded local information while system progress depends on collective decisions, shared resources, material state, and workspace compatibility. These properties closely match cooperative multi-agent decision making under partial observability and resource contention. This paper introduces AssemblyGrid v1, a reproducible benchmark for repeated multi-robot production that combines explicit process progression, decentralized observations, material transfer, temporary multi-robot coalitions, productive concurrency, and geometry-dependent feasibility within one task-level formulation. The benchmark includes Flow, Coalition, and Concurrency workload families, each with three scenario levels. Task success and evaluation measures are defined independently of learning reward and solution method, allowing learning-based and non-learning methods to address the same production problem. AssemblyGrid v1 is evaluated through executable conformance checks, mechanism studies, and algorithmic experiments using a privileged centralized reference, structured decentralized controllers, and MARL methods including IPPO, MAPPO, and QMIX. Results demonstrate productive execution under centralized and decentralized control. The MARL experiments further show that decentralized policies can learn effective production behavior from local observations and actions, supporting AssemblyGrid as a controlled benchmark for studying cooperative decision making in flexible robotic production.

### 26. Learning Multi-Agent Task Assignment and Navigation in the Factory: from Simulation to Real Robots
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-13T14:53:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.14567
- Summary: Reinforcement learning (RL) has shown considerable promise for robotic decision-making, yet deploying multi-agent RL (MARL) on physical multi-robot systems in industrial environments remains challenging. This paper investigates the real-world applicability of decentralized MARL for multi-robot multi-machine tending. We propose Feature-fusion Multi-Agent Proximal Policy Optimization (FMAPPO), which fuses 2D LiDAR measurements with task-specific state information to enable safe decentralized multi-robot task assignment and navigation. A complete simulation-to-reality pipeline was developed using high-fidelity robotic simulation and ROS2 and deployed on physical mobile-manipulator platforms operating under realistic real-world conditions, with the robotic arms disabled during the experiments. We further investigate the sensitivity of the learned policy to command update frequency, an important consideration for real-world deployment. Comparative evaluation in simulation demonstrated that FMAPPO significantly outperformed state-of-the-art baselines with a large effect size, achieving improvements of 106\% and 21\% in parts delivery and 48\% and 11\% in parts collection over MAPPO and SMAPPO, respectively. FMAPPO also increased machine utilization by 31 and 10 percentage points, respectively, while reducing collisions by 18\% and 15\% and increasing the safety score by 14 and 6 percentage points compared with MAPPO and SMAPPO, respectively. Furthermore, real-world experiments demonstrated that the learned decentralized policies can coordinate multiple robots to service multiple machines while maintaining safe operation under real-world sensing and control constraints. Videos of the real-world experiment are available online https://anonymouspapers123.github.io/FMAPPO/.

### 27. Cognitive Nexus (CGX) Pioneers Decentralized AI Agent Decision Network for the Autonomous Intelligence Era - EIN Presswire
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-13T13:54:00+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMi5gFBVV95cUxQY3hhR3dKSXVPejNLak13ZjcxV3pTTFgwbmZhMTlBWlBrRkRsMEZieWk5bVh2bXM2VkVyVXlaNmZRdWUtZVBXWHd3YzFHOEZsZ0FBVUd5aTd3eDV0NXhUU1FLLWNJUnZaekVJOUM3UDI4ckhKS21EeHQxU20wZU5zWk00eWYyS2pyOXp1S3F0bmV0NjhFZlgwZW9jbTlCVzB6NTVJY24zNWdNNGlSbTlfS2ZiWHZmOGVQcXJQY3dfdXdzTlRqdlF4a3kweDBiRFVaVzBDbGNYU3JnZnhBdTdtemRodHFVZw?oc=5
- Summary: Cognitive Nexus (CGX) Pioneers Decentralized AI Agent Decision Network for the Autonomous Intelligence Era&nbsp;&nbsp;EIN Presswire

### 28. Predefined-Time Integral Reinforcement Learning for Saturated Unknown Nonlinear Multi-Agent Systems Under FDI Attacks and Disturbances
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-12T17:49:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.14075
- Summary: This paper addresses secure leader-follower formation of unknown nonlinear multi-agent systems under actuator constraints, external disturbances, and false-data-injection (FDI) attacks. The graph-coupled coordination-error dynamics are formulated as local zero-sum differential games, where a nonquadratic input utility yields saturation-compatible secure policies and actuator-channel FDI and disturbances act as adversarial inputs. To eliminate explicit dependence on the unknown nonlinear drift, an integral Bellman-Isaacs identity enables critic-only learning from finite trajectory data. A two-power state-cost structure and a deadline-parameterized critic update connect optimal learning with predefined-time stabilization. Unlike fixed-time methods whose settling-time bound is determined by preselected gains, the proposed framework assigns the overall deadline first and allocates it among data informativity, critic learning, the reinforcement window, and formation convergence. Practical predefined-time convergence of the critic and formation errors to bounded residual sets is established independently of initial conditions, while secure actuator constraints are satisfied by construction. Simulations validate the framework under FDI attacks, disturbances, input constraints, and different initial conditions.

### 29. Tencent / WeKnora
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-12T02:01:51.519603+00:00
- Primary source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/Tencent/WeKnora
- Summary: Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.

### 30. A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture Design and Key Technologies
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-10T08:29:27+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.11231
- Summary: This paper presents SurgicalRoomAgent, a voice-interactive multi-agent system for smart operating rooms based on large language models (LLMs). The system achieves natural language understanding, device control, intraoperative recording, and surgical report generation through a layered architecture comprising a voice interaction pipeline (wake, ASR, turn detection, agent reasoning, TTS) and an agent core (skill registry, task planner, device manager). Three key technologies are investigated: (1) KV Cache prefix warming for low-latency inference, reducing recomputation overhead from approximately 500 ms to tens of milliseconds via byte-level Longest Common Prefix reuse; (2) streaming partial JSON parsing with early parallel task execution, reducing end-to-end latency by approximately 30%; and (3) progressive skill prompt disclosure, which dynamically filters system prompts based on user role, connected devices, and surgical phase to maximize information density within limited context windows. The system is implemented using the Qwen3-27B model with llama.cpp/sglang inference engines. Experimental analysis demonstrates effective operation within a 16,384-token context limit and multi-device parallel control response times meeting OR real-time requirements.
