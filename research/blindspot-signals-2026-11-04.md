# Blindspot Signals Report - 2026-11-04

- Source export: `/opt/apps/haier/exports/evolution_signals_20261104_020441.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 592
- Deduped/weighted signal clusters: 562
- Novel vs previous reports: 36
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. Multi-Modal Multi-Agent System for Bridge Operation and Maintenance based on Large Language Model
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-02T08:26:24+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02738
- Summary: Bridges are critical transportation infrastructure, and reliable operation and maintenance (O&M) is essential for traffic safety and long-term structural performance. However, bridge O&M faces key bottlenecks: no unified architecture coordinates heterogeneous resources; model inferences lack clear links to physical-mechanical laws; and experts' tacit knowledge remains difficult to formalize. This study proposes a knowledge-enhanced autonomy formalization methodology and apply it to construct the Bridge O&M Multi-Modal Multi-Agent System (BOMMA), which integrates heterogeneous diagnostic actions, physics-mechanics-informed representations, long-term memory, and structured experiential knowledge within a coordinated multi-agent workflow, enabling interpretable and traceable scheduling, analysis, and decision-making. On 3,492 multi-source instructions, the proposed method achieves scheduling recalls of 85.37% for simple and 99.40% for composite tasks, with 95.35% BERT F1-score for O&M action reasoning. Ablation studies confirm the contributions of the components in the autonomy. This study bridges general LLM reasoning and specialized bridge O&M requirements.

### 2. Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-02T01:09:24+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02361
- Summary: Can a language model that reads the full history of an access log say whether a service may act now? On an executable benchmark of grants, withdrawals, reinstatements, expiries, groups and change windows under a known policy, scored on pairs of histories that differ only in the order or one field of the deciding events, open models of 7 to 32 billion parameters fall from 72 to 86 percent after eight or sixteen events to 48 to 55 percent after 256, while reasoning-trained 32B models reading the current state reach 96 and 98 percent. A reasoning model of 120 billion parameters trails the state by four and seven points at 256 and 512 events and by about ten at 1,024, so the length beyond which explicit state outlasts long context grows with the reader. We treat agent memory as recursive filtering. The decision depends on the history only through a state whose size is set by the number of tracked keys. A store holding fewer component records than the state forgets on a time scale set by its capacity, and a reader model predicts its accuracy within 0.02 on average in a registered test. Retaining log lines without regard to time order errs with probability approaching one half, a bound that is attained. A filter in which a model parses each line and an explicit rule applies the updates answers 80 to 89 percent at 256 events and beats relevance retrieval, model-kept ledgers, a reimplementation of StateMem and the Mem0 library. A retriever that selects at query time the lines the queried state depends on matches it at 256 events on the first domain, so what decides is selection by the state's dependencies, which the filter performs when writing, without the query. Applying parsed updates themselves, the models fall to 58 and 59 percent. A frozen replication on a second domain with fresh wording reproduces the horizon.

### 3. The Agentic Observer Hackathon: Autonomous Decision-making in Simulated Astronomical Surveys
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-01T15:25:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2611.01988
- Summary: Astronomical surveys must allocate observing time while responding to changing conditions and competing scientific priorities. We present the Agentic Observer Hackathon (AOH), a community challenge for studying autonomous survey operations. Within a synthetic multi-object survey with prescribed exposure responses and assignment constraints, decision systems select pointings, assign targets and choose exposure configurations while responding to observing requests, instrumental faults and data loss. We evaluate systems submitted by 102 teams on campaigns reserved for evaluation and analyse target completion in a reference campaign. The leading systems combine numerical exposure planning with language models for interpreting operational information and supporting longer-term decisions. Exploratory tests show improved fault reporting with model access in several systems, while revised scientific priorities produce substantial changes in ranking. The reference campaign traces target completion and diagnoses errors in the baseline's inference of prescribed quality bands. The released simulator and reference strategies provide common survey conditions for comparing exposure allocation, target selection and recovery from interruptions.

### 4. A complete analytical characterization of optimal collision-free motion for two robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:53:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41558
- Summary: Collision-free motion planning for multi-agent robotic systems remains an active research area because of the complexity of coordinating robot trajectories, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. Importantly, the analytical difficulty of nonconvex collision-avoidance constraints has so far driven the development of exclusively numerical methods. We derive a complete analytical characterization of the optimal trajectories for two robots that start and end at rest, under double-integrator dynamics and a squared-acceleration objective. We prove that these trajectories belong to eight distinct contact families and determine which family applies for each configuration of initial and final positions. We analyze the geometrical properties of the optimal trajectories, provide a numerical algorithm for computing them, and discuss how these insights may improve the performance of existing numerical trajectory optimizers.

### 5. Contact-based optimization for collision-free motion planning for a million robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:46:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41548
- Summary: Multi-agent robotic systems have attracted growing interest in recent years, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. At the planning level, robot motion is often modeled using double-integrator dynamics (with low-level controllers handling the physical dynamics during execution) with a minimum-energy objective subject to collision-avoidance constraints and limits on position, velocity, and acceleration. The complexity of the problem resides in the constraints, which couple the trajectories and make the optimization problem nonconvex. Existing numerical approaches typically discretize and optimize entire trajectories, which becomes expensive for large fleets. We exploit the structure of optimal trajectories by organizing optimization around contacts, at which robots reach the minimum allowed separation. We formulate a coupled algebraic system in contact variables and reconstruct trajectories analytically between contacts. Our algorithm, sequential contact insertion (SCI), starts from unconstrained trajectories, inserts contacts at separation violations, and jointly adjusts their times and states. Numerical experiments demonstrate planning for one million robots in minutes and thousands of robots in fractions of a second. On problems feasible for a fixed-grid sequential convex programming baseline, SCI achieves median speedups of several orders of magnitude at matching solution accuracy.

### 6. Clinician-AI Collaboration in Endovascular Neurointerventions: In-Vitro User Study of Copilot Assistance Modes for Robotic Navigation Across the Autonomy Spectrum
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-02T16:57:50+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.03446
- Summary: Mechanical thrombectomy (MT) is an effective treatment for acute ischemic stroke, yet access remains limited by the availability of neurointerventional expertise. Telerobotic and AI-assisted systems may help address this challenge, but it remains unclear how clinicians interact with different levels of autonomy and how autonomous navigation systems perform in realistic environments. This work introduces Copilot Assistance Modes (CAMs), a framework for clinician-AI collaboration in robotic endovascular navigation spanning the autonomy spectrum from manual operation to full autonomy. In the first in-vitro user study comparing clinician-AI collaboration strategies, 11 experts and two students evaluated six navigation modes in a patient-specific vascular phantom. Objective performance metrics were combined with subjective assessments, including workload and usability. Autonomous performance was additionally evaluated both in silico and in vitro to investigate sim-to-real transfer. Hands-on manual navigation achieved the strongest overall performance (100% success). While fully autonomous navigation achieved 81% success in simulation, performance dropped to 23% in vitro. In contrast, several clinician-AI shared-autonomy modes achieved success rates of 92-97%, approximately four times higher than full autonomy and comparable to direct robotic control (95%), demonstrating mitigation of sim-to-real domain shift through clinician-AI collaboration. Among the evaluated AI-driven approaches, user-directed task delegation and rotational shared control demonstrated the most favorable balance between performance and clinician acceptance. These findings suggest that effective clinician-AI collaboration and allocation of control authority may currently be more important for reliable robotic neurointerventional navigation than increasing autonomy alone.

### 7. A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-02T10:44:02+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02912
- Summary: Long-lived agents rely on persistent memory of users, tasks and decisions, and this memory must stay consistent with a world that keeps changing. When an upstream fact changes, however, memory systems can revise the contradicted memory itself while the beliefs, plans and actions derived from it remain accepted, even though they have lost their support. We therefore formulate dependency-aware state revision, which asks not only what changed but also which dependent states should no longer be trusted. To address it, StateGraph maintains an evolving state dependency graph whose edges are recovered from interaction histories. Its core design is counterfactual verification: each candidate edge is tested by asking whether the dependent state would survive the loss of its premise, which separates support dependence from semantic relatedness, and revision then invalidates a dependent state only when a strict dependency fails and no independent support path survives. To test this design, we introduce StateChangeBench, a controlled benchmark of 50 author-constructed cases annotated with cascade depth, hard negatives and action consequences. On it, StateGraph's Impact-F1 margin over a CUPMem reimplementation is 6.9 percentage points at depth 1 and 26.0 at depth 3+. On public long-term memory benchmarks, its point estimates are comparable to or higher than those of the evaluated baselines on most datasets. These results provide initial evidence that explicit dependency tracking can improve selective memory revision under changing conditions.

### 8. Late Autumn: LLM Agents Specialize a General Multi-Robot Planner for One Warehouse
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-02T02:04:21+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.02391
- Summary: No algorithm is best on all problems, but a real warehouse is a narrow problem: its layout and processes rarely change. Operators still run one general multi-robot planner at many sites, because experts cannot tune it for each one. In this work, which we call Late Autumn, we explore whether LLM coding agents running autonomous research can specialize a general planner for one site, trading generality for throughput, much as post-training adapts a pretrained LLM to one task. We study six campaigns on a lifelong planner that combines task assignment with multi-agent path finding, on a floor modeled on an existing automated warehouse. We find that (1) the agents raise throughput by 22--60%, and the gains hold on unseen seeds; (2) they rediscover known MAPF mechanisms, such as corridor-exit priorities, local guidance, and rollouts, and independent campaigns find the same bottleneck; (3) the gains largely carry over to another layout, a larger fleet, and other service times, shrink with a smaller fleet, and mostly vanish under an outbound-heavy demand mix; and (4) each final patch (0.7k--2.4k lines) is a chain of scored commits with a median step of 27 lines, so experts can review it, and review finds problems that the score misses; some patches multiply planner compute by over 100x. LLM agents can therefore turn each site's bias into extra throughput at little engineering cost, with reviewable patches; we expect experts to shift toward designing insightful metrics and fast simulators that mirror the real problem.

### 9. Towards a Theory for the Design of Rules in Multi-Agent Systems: the case of Homogeneous Fleets
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-01T22:30:01+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02260
- Summary: The regulation of systems composed of many interacting decentralised agents is a long-standing problem. This problem has typically been resolved by the imposition of rules. Rules resolve the limitations of sub-optimal agents whilst simultaneously aligning the behaviour of the agents with the demands of society. Traffic laws, for example, let a driver cross a junction without seeing around the corner, and transport protocols such as TCP let applications share a network without knowing of one another. The problem is more pressing today, as autonomous systems are deployed in society. In this work, we establish the basis of a system-agnostic theory of rule design for multi-agent systems. We first state the rule design problem (RDP) in its generality. It relates a rule to the set of system performances, defined by the regulator, that the agents deployed under it can attain. However, it is not yet possible to solve the RDP in full generality. As such, we introduce the homogeneous rule design problem (HRDP), in which the agents in each environment are identical, and among other interesting properties, show that under worst-case aggregation the two problems have the same solution, bypassing the combinatorial complexity of the RDP. To solve the RDP under worst-case aggregation we propose Rule Branch and Bound (RuleBnB), an anytime branch-and-bound algorithm. Finally, we illustrate the value of solving the RDP on an autonomous driving case study.

### 10. GURU: A Hierarchical Neuro-Symbolic Multi-Agent System for Verification-Aware Automation of Mission-Critical Digital Engineering and Operations
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-31T14:41:00+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.01001
- Summary: An AI can find a safe action faster than any human, but it must never decide what counts as safe. We present GURU, a hierarchical neuro-symbolic multi-agent system for mission-critical digital engineering and operations, built on one partition of authority: learned models propose, rank, and accelerate; a symbolic rules engine checks every consequential action against hard limits before it executes; and validated physics confirms and decides. GURU runs a workflow as a closed control loop, with Navigation, Action, and Planning agents sharing one Common Internal Language and one training factory. Nuclear, aviation, and national-security guidance now requires this pattern; a harnessed language model keeps the model at the center, GURU puts a validated reference there. In computational fluid dynamics, the workflow raised the converged-simulation rate on unseen aircraft geometries from under 1 percent to 74 percent over 100 single-attempt cases, ran 54 live cases to Mach 6 on three facilities, and an ablation put the symbolic layer at 13 points of boundary-layer capture. Knowledge-graph retrieval and role adapters raised ParaView control success from 55 to 75 percent. In space domain awareness, where a language model cannot be trusted to decide, a frozen self-supervised world model under validated propagation scored highest of five methods at conjunction risk, including fully fine-tuned language models, with several-times-lower seed variance: the trustworthy design gives up nothing in accuracy, and the recipe transferred to reactor anomaly detection. A radar-to-avoidance debris pipeline was demonstrated in stages on a 2026 reentry; the hierarchy coordinates simulated teams of 200 aircraft. Training scaled near-linearly past 1,000 Aurora nodes and ran at 8,000. The approach extends to a control-grade microreactor digital twin with validated physics, not a learned model, as the safety basis.

### 11. Who Schedules Agent Memory? A Sidecar Approach to Long-Horizon Tasks
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-31T09:45:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.00779
- Summary: As large language model agents increasingly undertake complex, long-horizon tasks, memory has become an important component for supporting sustained decision-making and action. Existing methods primarily focus on memory storage, updating, and retrieval, but often overlook how memory scheduling affects task execution: the main agent must identify memory needs, initiate retrieval, and wait for results while advancing the task, increasing both scheduling burden and execution time. To address this problem, we propose MemSidecar, which decouples memory scheduling from task execution through two independently selectable modes. Hooks directly delivers bound memory to the main agent when execution events match predefined conditions. Foresight uses an independent agent to predict potential queries, retrieve results in parallel, and store them in a cache, delivering matching and valid results when actual requests arrive. Hooks and Foresight achieve scores of 41.23% and 44.34% on MCP-Persona, respectively, while effectively reducing execution costs and latency and improving the efficiency of long-horizon agent execution.

### 12. The Promises and Limitations of Evaluation-Based AI Governance: Evidence from Expert Interviews
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-30T23:39:48+00:00
- Primary source: arxiv
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://arxiv.org/abs/2611.00465
- Summary: We conducted 37 semi-structured expert interviews to examine how frontier AI evaluations reduce societal-level AI risks. Evaluations have become central to AI risk governance, despite their shortcomings being widely critiqued. Still, the case for how they reduce risks in practice remains largely implicit. Drawing on expert accounts, we reconstruct this case by identifying the mechanisms through which evaluations are expected to reduce risk, the assumptions underpinning those mechanisms, and the challenges those assumptions face. Our findings suggest that `evaluation-based governance' could contain foundational gaps which undermine risk-reduction strategies that depend on evaluations. Using thematic analysis, we identified three key pathways through which evaluations could reduce risk: by (i) making societal-level risks concrete to decision-makers and the public (raised in 18 out of 37 interviews), (ii) serving as a basis for governance commitments and regulation (18), and (iii) incentivizing a better risk culture within AI companies (16). However, these pathways often depended on shared assumptions that participants themselves doubted. The main challenges included, in order of frequency: (i) diminishing informativeness of evaluation results as model capabilities improve (21), (ii) measurement limitations that may be inherent to the evaluation paradigm (18), (iii) a lack of guarantees that evaluation results will be acted upon by companies or governments (16), and (iv) the degree of control and discretion AI companies retain over evaluation design, disclosure, and response (12). Participants also noted that evaluation-based governance could prove counterproductive, by functioning as a permission structure for developers' continued capability improvement (4). We finish by discussing the implications of our findings for evaluation-based governance, and what would improve its prospects.

### 13. META-Robot: Self-Cognition and Capability Scaling in Agentic Robots
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-30T15:19:31+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41868
- Summary: LLM-based robotic agent systems can generate programs for robot control, yet their generalization to new tasks often depends on elaborate scaffolding. Expanding their skill repertoires alone offers limited guidance on how to assess new capabilities or identify what remains beyond their reach. We introduce META-Robot, a framework that couples self cognition with capability scaling by expanding the criteria through which an agent evaluates and develops its skills. At its core, action-level predicates make execution outcomes explicit and available for LLM reasoning. The agent uses these assessments to identify its own limitations, extend relevant evaluation criteria, and guide the structured expansion of its skills. Proprioceptive feedback further grounds this process in the robot's physical state, enriching the evidence available for self-cognition. Experiments in simulation and on real robots demonstrate stronger overall task performance, generalization to new tasks, continued expansion of skills and evaluation criteria, and effective use of non-visual proprioceptive signals.

### 14. CONSORT: Uncertainty-Constrained Multi-Robot Planning for Cooperative Localization in GPS-Denied Environments
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-30T04:18:51+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.41235
- Summary: Centralized multi-agent path planning with cooperative localization in GPS-denied environments is generally computationally intractable when formulated in full belief space due to tightly coupled uncertainty dynamics. Prior work typically approximates belief dynamics or restricts inter-agent coupling. This work examines a multi-agent planning problem in which a primary agent must reach a goal in minimum time subject to a chance-constrained collision-avoidance requirement and a terminal bound on localization uncertainty. We obtain a tractable surrogate of the underlying belief-space problem by optimizing over the mean-state trajectories of all agents and propagating covariance for terminal constraint evaluation only. We propose CONSORT (Cooperative Navigation with Support-Optimized Routing and Trajectories), a discrete-to-continuous pipeline combining hexagonal-grid joint search with spline-based trajectory refinement. Across 50 randomized scenarios, the planners separate as the terminal uncertainty bound tightens, with CONSORT solving 80% of scenarios where the strongest baseline solves 54%, at comparable path length. In marine simulations, with the plans executed under feedback control on an independently developed factor-graph estimate, the trajectories remain collision-free and their terminal uncertainty falls within 6% of the planner's prediction.

### 15. Snowflake Adds Autonomous Bots to CoCo and CoWork AI Agents - HPCwire
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-03T19:38:10+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMirgFBVV95cUxNMHdPTGptS0FsUWRPUDZJTlJNaXFydzRNSHZ0VUVpWVF5RTZPaEZuX29FaFZLTEJQakVjZkh1ZHJRVUJWWXNxamZJWXhwamQzME5xZmF0ci02dzZkX0tCSy1WeV9mY3ZWMnk4a1p5dFFuOXllNVktYmF0cWIzY2gxWUkyVW91cW4yUG1kZkhQQ2VSRHEyZnJwdkIxTS1tVHQySFhJb1diakNvOFV1eXc?oc=5
- Summary: Snowflake Adds Autonomous Bots to CoCo and CoWork AI Agents&nbsp;&nbsp;HPCwire

### 16. Sam George urges Africa to lead in global internet and AI governance - Modern Ghana
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-03T07:29:00+00:00
- Primary source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMinAFBVV95cUxQVEVGeHYzX0ZkVFRKODNoaFh1QUJvajByNDZFdXFLenhlN1lCLWlQb2YyZlhWQmpkbTdWazA2M3lVVjVuYWlvMUNCeUlOQTlxX1ZFazQzLWR6RmJjT3BsUWJEdnhXcENGQmdDaG80LWZIeUZnMnVzaUcxUnFHWHhpMHVSTGt5V2NxdEQ1bW1XRktHS1R5d1NtTVpmcXbSAZsBQVVfeXFMUFh6SnVodGNCcGJOS1NHblIxa1dUSGc1OWk5V2RtMXU4QmpwOU9La1JheUR4N2xnaFRmWUFpMm0ya2pFcW50bVdBU3VVMXEwVktNSjExUDJRVFJCUlB5UlJWMFVoU1FrVms3NW1tTTlvMU15T2N5OFhzVVoyMkdqd2lNSTd0T2x3by04ZnFTVUE1UkhmQXlhWFpYTXc?oc=5
- Summary: Sam George urges Africa to lead in global internet and AI governance&nbsp;&nbsp;Modern Ghana

### 17. LabWeaver: reliable agentic data analysis grounded in laboratory knowled
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-03T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.28.762601
- Summary: Agentic systems powered by large language models are rapidly automating biological data analysis. However, their reliability remains questionable because they often overlook experimental context, such as disease domain and experimental protocol. Existing agentic systems organize context around individual users and projects, whereas research is organized around laboratories whose projects share experimental context. As a result, experimental context learned in one project remains unavailable to related projects. We introduce LabWeaver, an agentic data analysis framework with a laboratory-organized architecture of three tiers: laboratory, user and project. Further, LabWeaver distills experimental context into laboratory memory and skills, which are shared across users and projects after human-gated review. To isolate the contribution of experimental context, we analyzed a synovial sarcoma single-cell RNA-seq dataset in two sessions that differed only in whether laboratory memory and skills were available. The context-free session lost the fusion reporter at read alignment and misannotated the tumor cells. In contrast, the context-enabled session recovered reporter expression and resolved five fusion-anchored tumor cell states.

### 18. An Axiomatic Framework for Reinforcement Learning in Open Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-02T15:36:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.03301
  - Alt: https://arxiv.org/abs/2610.28966
- Summary: Open multi-agent systems, where only a subset of agents are controllable, are central to real-world domains such as smart grids, yet lack a principled foundation for reinforcement learning algorithm design. We study this setting through n-agent ad hoc teamwork (NAHT), a recent framework for learning in open multi-agent environments. We propose an axiomatic framework that derives value function learning from the Shapley axioms (Efficiency, Symmetry and Linearity), treating them as structural constraints rather than heuristic design choices. This formulation builds on a novel NAHT decomposition, which characterises the fundamental difference between open and fully controllable multi-agent systems, and establishes a cooperative game-theoretic foundation for learning. We further show that enforcing these axioms on learning individual value functions recovers the Shapley value for Dec-POMDPs, providing a principled bridge between reinforcement learning and classical cooperative game theory. Building on this framework, we introduce Shapley Machines and Banzhaf Machines, two generic algorithmic templates that can be instantiated with standard reinforcement learning methods. When applied to strong base algorithms such as IPPO and POAM, our methods consistently improve learning efficiency and generalisation to unseen agent types and conventions across NAHT benchmark tasks. The code of experiments is published on https://github.com/hsvgbkhgbv/axiomatic-rl-naht.

### 19. Delivered, Not Used: Evaluating Agent Memory at Its Point of Use
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-01T09:09:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.01718
- Summary: Task success, retrieval quality, and cost do not show whether an LLM agent used a delivered memory or what followed from that use. We introduce MemUse, which evaluates memory at its point of use in recorded trajectories: each memory delivery is compared with what the agent could already see and followed through the agent's later actions and their consequences. An agentic judge rates each delivered entry's relevance, accuracy, novelty, influence, and observed effect; programmatic checks enforce complete reading of cited evidence, and fixed rules aggregate the ratings into verdicts linked to memory histories and delivery cost. On 8,000 SWE-bench Verified episodes from three memory systems, resolve rates stay within 0.4 percentage points of a no-memory baseline, yet MemUse shows that most delivered entries were irrelevant, most relevant entries went unused, and in two systems most deliveries restated content the agent could still see. It also surfaces effects that outcomes hide: 23.2\% of episodes with beneficial memory use still failed, and 5 of 16 with harmful use still succeeded.

### 20. Serving Agentic Robot Fleets: Workload Characterization, KV-Cache Thrashing, and Admission Control
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-01T01:15:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.01404
- Summary: Agentic robots combine a vision-language brain, a tool-using harness, and a vision-language-action (VLA) policy. Serving a fleet of these agents introduces two coupled resource constraints: the brain repeatedly revisits long, growing key-value (KV) cache states, while the VLA executes action chunks under tight control deadlines. We characterize 80 LIBERO-PRO episodes generated by GPT-6-Astra, RPent, and pi0.5 (1,862 brain turns and 1,582 VLA inference chunks), profile both layers on H800 graphics processing units (GPUs), and replay the resulting agent programs on a vLLM serving engine. Brain contexts reach 215k tokens; the median Astra request takes 7.78 s, while the intervening environment-step gap is only 1.0 s. Under a 0.25 s action-chunk deadline, one VLA GPU meets the 1% starvation target for one robot; under a 1.0 s deadline, its measured capacity reaches at least 32. In sustained brain replay, increasing concurrency from 20 to 32 robots reduces throughput from about 2.4 to 0.6 requests/s as repetitive prefill displaces generation. A static active-episode cap restores 2.24-2.25 requests/s and raises completed trace-program throughput from 1.30 to 5.00-5.55 episodes/min. Our measurements expose the workload-dependent shift between action deadlines and brain KV residency, and establish practical principles for capacity planning and admission in sustained agentic robot fleets.

### 21. Illusion: Safeguarding Topology Confidentiality in LLM Multi-Agent Systems via Behavior-Preserving Obfuscation
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-31T13:23:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.00923
- Summary: The communication topology of Large Language Model Multi-Agent Systems (LLM-MASs) governs how information propagates among agents and encodes critical domain knowledge and expert workflow design. It is valuable intellectual property and plays a decisive role in system utility and safety, yet remains vulnerable to inference attacks that stealthily reconstruct it from agent outputs. Existing defenses detect or mitigate such attacks but do not proactively conceal the topology itself. We propose \textit{Illusion}, a proactive topology obfuscation defense for LLM-MAS. \textit{Illusion} injects fake edges and fake messages to present attackers with a deceptive topology, while selecting low-impact candidates that preserve output-distribution equivalence and task-accuracy non-inferiority. The resulting fake edges are designed to be indistinguishable from genuine messages under black-box observation. Extensive experiments show that \textit{Illusion} reduces edge-level F1 from over 0.87 to 0.62 and graph similarity from over 0.94 to 0.71. It also largely preserves output distributions and task performance, and its fake edges resist both similarity-based and LLM-judge filtering, even under adaptive pruning.

### 22. MAS-Loop: Beyond One-Shot Orchestration towards Self-Evolving Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-28T21:32:05+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.38946
- Summary: Training-time multi-agent system (MAS) design seeks to learn reusable orchestration policies, yet prevailing approaches remain largely one-shot: an Orchestrator generates a system but only observes and learns from its terminal outcome. This paradigm discards execution trajectories that expose system-level failures and contain fine-grained information beyond the terminal outcome, leaving no direct basis for revising the source MAS, evaluating the updated MAS, or learning from the resulting contrast. To this end, we introduce MAS-Loop, an execution-grounded framework that closes this feedback loop by coupling an Orchestrator with a trajectory-conditioned Refiner. For each task, the Orchestrator constructs and executes a source MAS to obtain an outcome score and an intermediate trajectory. Conditioned on the trajectory, the Refiner localizes an actionable failure, formulates a trajectory-grounded diagnosis, and proposes a bounded patch to the agents, information flow, or execution configuration. The executable updated MAS is re-executed on the same task to measure its realized outcome under stochastic execution. This pair-MAS comparison provides complementary learning signals: the Orchestrator learns to generate strong systems with fewer recoverable failures, whereas the Refiner learns to expose and repair observed weaknesses, thereby driving policy-level co-evolution across training iterations. Experiments show that MAS-Loop achieves the strongest overall performance among the evaluated baselines, with consistent gains from refinement across all evaluated benchmarks. The co-evolution process also yields MAS-JudgeCorpus, a dataset of execution-grounded source-updated pairs with orchestration- and trajectory-level supervision, which can provide the community with support for MAS reward modeling and trajectory-aware investigation.

### 23. MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-16T10:01:52+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.23234
- Summary: In a hierarchical multi-agent system, a Leader assigns tasks and subagents carry them out. Jointly training the Leader and the subagents is difficult because a final answer gives only indirect feedback to the subagents. An LLM judge can score the performance of the subagents, but these scores depend on the judge's own assessment of the quality of subagents' responses. We present MultiAgent-OPD, which combines on-policy distillation with reinforcement learning to jointly train a shared-parameter Leader-Searcher-Answerer team end to end. We first train a Teacher in a Searcher-Answerer workflow using answer correctness. During team training, the frozen Teacher scores student-generated search and summary tokens to provide local process supervision for the Searchers, while the Leader learns from team success and the Answerer from candidate correctness. Across seven datasets, the trained system reaches 38.68% macro avg@4, exceeding Prompted Critic by 4.06 percentage points and C-MAS + RL, the trained cascaded multiagent system, by 2.61 percentage points. The team also solves more questions within four attempts.

### 24. LatentRemedy: Efficient Remedy For Non-Prefix KV Cache Reuse in Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-13T09:12:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.18014
- Summary: Non-prefix KV cache reuse is a promising approach for improving inference efficiency in multi-agent systems as agents share the same context blocks. However, when agents have conflicting tasks, directly reusing non-prefix KV caches across agents can severely degrade model performance, causing up to a 90% drop. Existing remedies, including selective recomputation and offset-based calibration, recover a limited fraction of this loss. We argue that the problem lies not only in contaminated KV representations but also in the agent's difficulty interpreting reused context under its own instructions. To this end, we introduce LatentRemedy, which uses a few task-conditioned latent tokens to help the target agent leverage reused context without recomputing the shared block. Specifically, we use an MLP to map the last hidden state of the target prefix into a small number of latent tokens, which are placed after the reused KV block to interact with the shared context. To guide subsequent predictions toward the target task, we train the MLP through full-prefill distillation. Experiments show that LatentRemedy consistently outperforms existing reuse baselines on conflicting tasks while maintaining TTFT close to direct reuse as cache size grows. Code and data are available at https://github.com/chenzhwsysu57/kvreuse.

### 25. Inherit-MAS: Test-Time Evolution of Multi-Agent Systems through Workflow and Execution Inheritance
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-01T19:23:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.02396
- Summary: Multi-agent systems (MAS) built from large language models coordinate specialized agents to tackle complex tasks, but effective workflows are difficult to design in advance. Test-time evolution refines workflows using execution feedback, yet broad revisions can disturb useful components, while re-executing unchanged requests can incur redundant computation. Inspired by the interplay of inheritance and selection in biological evolution, we introduce Inherit-MAS, which makes inheritance explicit at the workflow and execution levels. A meta-model first synthesizes a workflow of worker agents with declared roles, communication inputs, and tool permissions, and a separately prompted judge scores each executed candidate and diagnoses its deficiencies. In ordinary refinement rounds, \emph{workflow inheritance} starts from the latest completed candidate, may discard removable nodes judged unhelpful, and applies a validated edit to address the diagnosed deficiency. When the new candidate executes, \emph{execution inheritance} inherits eligible stored results only if the complete resolved request and execution context match, avoiding redundant model and tool calls. With GPT-4o-mini workers, Inherit-MAS achieves 55.4\% completion on WorkBench and 49.7\% joint F1 on HotpotQA FullWiki, outperforming EvoAgent, EvoMAS, and TacoMAS. With Qwen3-32B workers, it also exceeds these evolving-MAS baselines on both benchmarks. Compared with rerunning the same controller with execution inheritance disabled, execution inheritance reduces worker-token usage by 29.1\% on WorkBench and 34.6\% on HotpotQA, and total token usage by 5.3\% and 18.1\%.

### 26. Apple warns rogue AI agents could ‘conceal’ and ‘manipulate,’ causing unintended consequences for its business - Fortune
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-03T21:56:00+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMimwFBVV95cUxOa2VfS2pfY1pWVWg5TkJsa3JBLTNOSm1oVDFjYnhJdkVDWDZzdHJLWVV6bS1FU3p2RF9WX1BlV0ZNS2x0RkNxN0JudDNaUzdMdnJ2YmlXc0ZpazJsN3hzREp0dlItSVI0SGtiSkVDSWM1WTJiOGlHdG1vRHRxTDJkcHl5T1FadzUycUZTVks4LTRCSGU5cVNiVjdlaw?oc=5
- Summary: Apple warns rogue AI agents could ‘conceal’ and ‘manipulate,’ causing unintended consequences for its business&nbsp;&nbsp;Fortune

### 27. Apple Flags AI Agent Risks in Annual Filing - The Tech Buzz
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-03T21:22:09+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiggFBVV95cUxQME1jR1lQNHF5RGZwNW9RZ1E0OW9nNzNhWUVXSTJ2RzQtYnpNVXU4aUlCVk1xM2FGOWwtb20zUmhzRDRmVGRyZ3BiR1M1UmpnbXB3Vmxwc3UxSjI5R3hiaU1TUm9FY2VaeTZNNUNacEJXNk5RV1E5eGNIdkdLQnNwQ2Nn?oc=5
- Summary: Apple Flags AI Agent Risks in Annual Filing&nbsp;&nbsp;The Tech Buzz

### 28. AI Agents Used by Railway Breach Systems of Rival Primcloud
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-03T20:40:14+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://securityboulevard.com/2026/11/ai-agents-used-by-railway-breach-systems-of-rival-primcloud/
- Summary: No summary.

### 29. CrowdStrike to shell out nearly $500M for 2 AI security startups as the market for securing agents takes off
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-03T17:56:52+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/03/crowdstrike-to-shell-out-nearly-500m-for-2-ai-security-startups-as-the-market-for-securing-agents-takes-off/
- Summary: CrowdStrike said it will buy Fiddler AI, which makes AI agent observability software, and Dreadnode, which helps companies automate AI security testing.

### 30. Open models can do 90 percent of agentic work at a twentieth of the cost
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-03T07:46:36+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.theregister.com/ai-and-ml/2026/11/03/open-models-can-do-90-percent-of-agentic-work-at-a-twentieth-of-the-cost-of-a-frontier-llm-gartner/5307132
- Summary: No summary.

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

### 3. Multi-Modal Multi-Agent System for Bridge Operation and Maintenance based on Large Language Model
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-02T08:26:24+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02738
- Summary: Bridges are critical transportation infrastructure, and reliable operation and maintenance (O&M) is essential for traffic safety and long-term structural performance. However, bridge O&M faces key bottlenecks: no unified architecture coordinates heterogeneous resources; model inferences lack clear links to physical-mechanical laws; and experts' tacit knowledge remains difficult to formalize. This study proposes a knowledge-enhanced autonomy formalization methodology and apply it to construct the Bridge O&M Multi-Modal Multi-Agent System (BOMMA), which integrates heterogeneous diagnostic actions, physics-mechanics-informed representations, long-term memory, and structured experiential knowledge within a coordinated multi-agent workflow, enabling interpretable and traceable scheduling, analysis, and decision-making. On 3,492 multi-source instructions, the proposed method achieves scheduling recalls of 85.37% for simple and 99.40% for composite tasks, with 95.35% BERT F1-score for O&M action reasoning. Ablation studies confirm the contributions of the components in the autonomy. This study bridges general LLM reasoning and specialized bridge O&M requirements.

### 4. Locating and Closing Information Gaps in Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-29T14:45:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.40186
  - Alt: https://arxiv.org/abs/2610.18780
- Summary: Multi-step Web tasks often require several LLM agents to gather and combine evidence. The communication graph of a fixed workflow restricts which agents can read each other's outputs: evidence retrieved by one agent may never reach the agent that needs it, leaving an information gap and an incomplete or incorrect answer. Adding a connection can deliver the missing evidence, but can also lead the receiver to adopt an incorrect upstream conclusion that displaces a correct answer; the final output alone does not separate the two. We propose Selective Probing and Link Insertion for Closing information gaps in multi-agent Execution (SPLICE), which locates information gaps per query and decides what to adopt after adding an edge. After the original workflow runs, SPLICE uses the query and node outputs to locate a possible gap, adds one directed edge from a source to a receiver to deliver the relevant evidence, and re-executes the receiver and affected downstream nodes, producing a candidate answer. The adoption decision reads both the final answers of the two runs and the process changes the edit caused inside the workflow: how far the receiver moved, where its new content came from, and whether the change reached the final answer. A selector trained on these process features chooses between adopting the candidate answer and retaining the original. On five benchmarks, SPLICE raises the task score on Web tool use by 8.0% and the mean score on four reasoning and planning benchmarks by 5.7% relative to the static skeleton, at 1.25 to 1.44$\times$ the skeleton's cost, and transfers zero-shot to four unseen backbones.

### 5. EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-25T17:09:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.34450
  - Alt: https://arxiv.org/abs/2609.37953
- Summary: Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control. Agents need to adapt to other agents at test time and reuse accumulated experience to refine their interaction strategies for future interactions across cooperative, mixed-motive, and adversarial settings. However, existing approaches often develop adaptation mechanisms for particular interaction settings. This raises a central question: how can decentralized MAS support test-time adaptation and reliable experience reuse across interaction settings? We propose EvolveMAS, a unified self-evolution framework that supports experience-driven adaptation within and across episodes. EvolveMAS pairs each main agent with a dedicated MemoryAgent for test-time memory governance, which maintains isolated Structured Memory outside the main agent's reasoning context. EvolveMAS organizes adaptation into two complementary processes: Within-Episode Online Adaptation and Cross-Episode Knowledge Evolution. During Within-Episode Online Adaptation, MemoryAgent updates episodic, semantic, and working memory from interaction evidence to inform subsequent actions. During Cross-Episode Knowledge Evolution, the main agent uses memory and episode outcomes to distill reusable interaction knowledge comprising partner profiles and interaction strategies for subsequent episodes. Across five benchmarks and six evaluation configurations spanning the three interaction settings, EvolveMAS achieves the highest normalized average score of 77.2 among the compared methods. Ablations show that test-time memory governance and cross-episode knowledge reuse both improve performance. Interaction traces further illustrate how updated memory and distilled knowledge guide subsequent interactions. These results support experience-driven adaptation in decentralized MAS without updating model parameters.

### 6. From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-21T10:49:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.29560
- Summary: Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work has begun to address these challenges by augmenting foundation-model policies with memory and by introducing hierarchical architectures that separate high-level planning from low-level execution. We organize the high-level VLM as a robotic agent through an editable harness to maintain task context and improve planning through execution experience. We instantiate this approach as SERA (Self-Evolving Robotic Agent), with a fixed VLA executor providing low-level control. The harness maintains and updates task context using observations and execution feedback to guide subsequent planning. Self-evolution uses environment rollouts to propose and evaluate harness revisions, with the selected configuration fixed before held-out testing. On RoboMME, SERA achieves 51.38% overall success with autonomous selection, compared with 44.38% without self-evolution. Our exploration suggests that agentic planning is a promising direction for history-dependent robotic manipulation.

### 7. Refuse the Harm, Complete the Task via Graph-of-Rules Planning for LLM-Enabled Robots
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-17T10:13:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.24603
- Summary: Large Language Models (LLMs) are increasingly used in embodied AI for robotic manipulation and planning, but their deployment in physical systems exposes vulnerabilities such as jailbreak attacks that induce unsafe behavior. Existing inference-time defenses are mainly evaluated on short instructions containing a single hazard, whereas realistic tasks may interleave safe and unsafe sub-tasks, conceal hazardous steps, or combine individually safe actions into unsafe outcomes. Such compound instructions make it harder for a single safety decision to distinguish hazardous sub-tasks from legitimate ones, risking either overlooking the hazard or rejecting the whole instruction. We introduce safe task completion, a task that requires an LLM-enabled robot to refuse the harmful part of an instruction while completing its legitimate part. To address this problem, we propose RuleGraph, a multi-agent Graph-of-Rules planning framework that distributes safety enforcement across multiple reasoning and verification stages. Five cooperating agents are used to ground general safety principles into world-specific rules, assess the instruction's sub-tasks in context, and derive a safe goal from the legitimate ones. Planning toward this goal is then organized as a graph of rule-specific nodes, where higher-level nodes inherit the union of their parents' rules, and candidate plans are progressively verified and aggregated until a single plan satisfies every relevant rule. In this way, RuleGraph reduces reliance on a single centralized safety decision. We evaluate RuleGraph on pure-attack and compound instructions across two benchmarks in two environments using Attack Success Rate (ASR) and Task Success Rate (TSR). RuleGraph reduces ASR to 0% on both benchmarks while achieving the highest TSR among all methods, reaching 98.57% on the RoboGuard benchmark and 84.54% on our long-horizon compound instructions.

### 8. ChunkAct: Action Chunking for Agentic Robotics
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-13T17:59:57+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.18874
- Summary: Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.

### 9. Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark, and Method
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-07T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents, robotics / AI agents
- URL: https://huggingface.co/papers/2609.35965
- Summary: Vision-and-Language Navigation (VLN) has largely focused on a single agent following a single instruction, yet many real-world applications require teams of robots to tackle tasks beyond the capabilities of any individual agent. We present Systematic Multi-Agent Vision-and-Language Navigation, providing, to our knowledge, the first systematic formalization of multi-agent VLN as a constrained coordination problem: each mission consists of subtasks carrying dependency and resource constraints (presence locks and holding chains). A verified four-stage crafting pipeline instantiates the task as MAVLN, comprising 11,724 episodes across 145 scenes with teams of up to four agents under three instruction regimes, accompanied by tailored constraint-aware metrics. We further present TRISS, a coordination-ready navigation system coupling an LLM-based subtask scheduler, a shared topological memory that turns each agent's exploration into team knowledge, and a conflict-aware execution mechanism that realizes simultaneous intentions as collision-free routes. Extensive experiments establish TRISS as a comprehensive baseline and reveal substantial room for improvement across scheduling, planning, and execution, highlighting the challenges of coordinating under MAVLN task constraints. Project page: https://xyz9911.github.io/mavln.

### 10. PrivMeSA: Privacy-Aware Self-Evolving Multi-Agent System for Medicine via Local-Remote LLM Collaboration
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-29T19:47:38+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38458
  - Alt: https://arxiv.org/abs/2610.30851
- Summary: Clinical large language model (LLM) agents deployed locally can consult more capable remote models, but doing so risks exposing patient information. Privacy-conscious delegation places disclosure decisions with a local agent, yet removing explicit identifiers is insufficient: quasi-identifiers can accumulate across multi-turn consultations and repeated patient visits to enable re-identification. We introduce PrivMeSA, a privacy-aware self-evolving multi-agent system that learns to control disclosure and retains remote expertise for local reuse. A local agent manages each encounter and consults remote specialists that may request additional information. Reinforcement learning balances task accuracy against direct disclosure and registry-based re-identification risk, with privacy evaluated over the complete outbound transcript of each encounter. A local lesson memory distills completed consultations into generalized clinical guidance and retrieves relevant lessons before transmission, allowing subsequent cases to reuse expertise without another remote exchange. Memory grows without additional outcome labels or parameter updates. On an emergency-department benchmark built from MIMIC-IV-ED records, PrivMeSA improves mean task accuracy over delegation by up to 15.8 percentage points. In the same setting, PrivMeSA reduces the disclosure of personal details from 98.0% to 0.2% of cases and the share of cases in which the patient can be narrowed to ten or fewer registry patients from 74% to 0%.

### 11. Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-02T01:09:24+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02361
- Summary: Can a language model that reads the full history of an access log say whether a service may act now? On an executable benchmark of grants, withdrawals, reinstatements, expiries, groups and change windows under a known policy, scored on pairs of histories that differ only in the order or one field of the deciding events, open models of 7 to 32 billion parameters fall from 72 to 86 percent after eight or sixteen events to 48 to 55 percent after 256, while reasoning-trained 32B models reading the current state reach 96 and 98 percent. A reasoning model of 120 billion parameters trails the state by four and seven points at 256 and 512 events and by about ten at 1,024, so the length beyond which explicit state outlasts long context grows with the reader. We treat agent memory as recursive filtering. The decision depends on the history only through a state whose size is set by the number of tracked keys. A store holding fewer component records than the state forgets on a time scale set by its capacity, and a reader model predicts its accuracy within 0.02 on average in a registered test. Retaining log lines without regard to time order errs with probability approaching one half, a bound that is attained. A filter in which a model parses each line and an explicit rule applies the updates answers 80 to 89 percent at 256 events and beats relevance retrieval, model-kept ledgers, a reimplementation of StateMem and the Mem0 library. A retriever that selects at query time the lines the queried state depends on matches it at 256 events on the first domain, so what decides is selection by the state's dependencies, which the filter performs when writing, without the query. Applying parsed updates themselves, the models fall to 58 and 59 percent. A frozen replication on a second domain with fresh wording reproduces the horizon.

### 12. Head movement allocation in freely-moving macaques learning object-context sequences
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-02T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.1101/2023.12.11.571113
- Summary: Flexible learning and long-term memory are hallmark features of primate cognition that are shaped by interactions with changing environments. A comprehensive understanding of these brain-body-environment interactions requires minimal constraints on behavior, and environments rich with conditional cues that encourage diverse behavioral dynamics. In this study, we introduce a multi-level enclosure (Treehouse) that allows for independent control of spatially distributed touchscreens for studying cognition in freely moving macaques. To test flexible learning, two monkeys completed trials consisting of a regular sequence of conditional object choices (targets) across four distinct spatiotemporal contexts (screens). Both monkeys acquired numerous unique, conditional object-context sequences without detriment to new learning as memoranda accumulated. They also successfully recalled their correct choices after weeks without exposure. To assess how monkeys allocate movement during learning and memory-guided decision making, we tracked their head kinematics and used recurrent neural networks to decode different aspects of their engagement with the environment during the choice epoch of the task. One such model predicted the position of the object about to be touched, including on error trials, tracking overt gaze towards objects. Separate models decoded sequence corner, the ordinal step, and the individual screen stations the monkeys occupied, despite identical stimulus layouts and behavioral demands at each station. Head movements also showed efficiencies that the task did not require: under conditions of uncertainty, monkeys were biased in their initial search locations to the targets that were closest to reach, and across days they made smoother head movements as training progressed, with no change in accuracy. These results demonstrate the potential of immersive 3-D environments, in which body kinematics can shed light on animals' goals, and reveal that situated learning …

### 13. The Agentic Observer Hackathon: Autonomous Decision-making in Simulated Astronomical Surveys
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-01T15:25:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2611.01988
- Summary: Astronomical surveys must allocate observing time while responding to changing conditions and competing scientific priorities. We present the Agentic Observer Hackathon (AOH), a community challenge for studying autonomous survey operations. Within a synthetic multi-object survey with prescribed exposure responses and assignment constraints, decision systems select pointings, assign targets and choose exposure configurations while responding to observing requests, instrumental faults and data loss. We evaluate systems submitted by 102 teams on campaigns reserved for evaluation and analyse target completion in a reference campaign. The leading systems combine numerical exposure planning with language models for interpreting operational information and supporting longer-term decisions. Exploratory tests show improved fault reporting with model access in several systems, while revised scientific priorities produce substantial changes in ranking. The reference campaign traces target completion and diagnoses errors in the baseline's inference of prescribed quality bands. The released simulator and reference strategies provide common survey conditions for comparing exposure allocation, target selection and recovery from interruptions.

### 14. A complete analytical characterization of optimal collision-free motion for two robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:53:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41558
- Summary: Collision-free motion planning for multi-agent robotic systems remains an active research area because of the complexity of coordinating robot trajectories, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. Importantly, the analytical difficulty of nonconvex collision-avoidance constraints has so far driven the development of exclusively numerical methods. We derive a complete analytical characterization of the optimal trajectories for two robots that start and end at rest, under double-integrator dynamics and a squared-acceleration objective. We prove that these trajectories belong to eight distinct contact families and determine which family applies for each configuration of initial and final positions. We analyze the geometrical properties of the optimal trajectories, provide a numerical algorithm for computing them, and discuss how these insights may improve the performance of existing numerical trajectory optimizers.

### 15. Contact-based optimization for collision-free motion planning for a million robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:46:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41548
- Summary: Multi-agent robotic systems have attracted growing interest in recent years, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. At the planning level, robot motion is often modeled using double-integrator dynamics (with low-level controllers handling the physical dynamics during execution) with a minimum-energy objective subject to collision-avoidance constraints and limits on position, velocity, and acceleration. The complexity of the problem resides in the constraints, which couple the trajectories and make the optimization problem nonconvex. Existing numerical approaches typically discretize and optimize entire trajectories, which becomes expensive for large fleets. We exploit the structure of optimal trajectories by organizing optimization around contacts, at which robots reach the minimum allowed separation. We formulate a coupled algebraic system in contact variables and reconstruct trajectories analytically between contacts. Our algorithm, sequential contact insertion (SCI), starts from unconstrained trajectories, inserts contacts at separation violations, and jointly adjusts their times and states. Numerical experiments demonstrate planning for one million robots in minutes and thousands of robots in fractions of a second. On problems feasible for a fixed-grid sequential convex programming baseline, SCI achieves median speedups of several orders of magnitude at matching solution accuracy.

### 16. Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-28T20:40:33+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.38869
  - Alt: https://arxiv.org/abs/2610.22316
  - Alt: https://arxiv.org/abs/2609.39788
- Summary: Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments across retrieval, memory, tools, and peer communication. In this paper, we define belief as an engineering abstraction for evidence-based commitments that guide downstream action. Building on this view, we propose the Explicit Belief Multi-Agent System (EB-MAS), which externalizes belief states into a structured substrate, uses belief operators to propose candidate updates, and applies a Cognitive Firewall to bound or reject updates that are weakly evidenced but strongly driven by vulnerability cues. We also discuss the risk of group belief at the group level, including manufactured consensus, collusion, and cascading misinformation, and outline practical integration challenges around grounding, false positives, scalability, and ethical misuse. Therefore, scalable agent safety requires not only better output filtering or stronger base models, but also explicit interfaces for tracing, calibrating, and constraining belief revision at runtime.

### 17. Remembering Is Not Enough: Refining Memories and Learning When to Use Them in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-27T05:12:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.36652
- Summary: Memory helps LLM-based multi-agent systems reuse experience, but stored advice can be flawed or applied in the wrong situation. Team-level success or failure alone cannot reliably show whether a memory needs correction or should not have been used. We propose DiscernMem, a training-free framework that improves both memory quality and memory use. To improve quality, Defect-Aware Memory Refinement (DMR) compares team executions with a single memory and with no memory, diagnoses rule defects, and tests repairs on current and earlier tasks to guard against losing previously useful behavior. To guide appropriate use, Boundary-Learning Meta-Memory (BLM) records each memory's past uses and effects, learning when its owner role should apply or avoid it based on task context and incoming messages. Together, these components help teams correct flawed experience while retaining useful rules that were applied incorrectly. Experiments with Qwen3-4B-Instruct-2507 on four benchmarks show that DiscernMem achieves the highest average score on AutoGen, CAMEL, and MacNet, exceeding the strongest reported baselines by 0.51-4.32 points. It leads on code generation and symbolic planning across all three systems, including a PDDL score of 37.71 versus 28.48 on CAMEL.

### 18. Compatibility and future-proof testing for multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-26T21:14:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.36289
- Summary: Independently developed autonomous agents, such as autonomous vehicles, must guarantee joint compatibility, such as safety and task-completion requirements, when they operate in a shared environment. Existing methods require a centrally designed specification, or interaction mechanism before any agent is deployed. However, such centralized design is unrealistic when agent designs are confidential to their developers, and it is not flexible enough to accommodate future agent designs. We study a bi-level structure in which a regulator coordinates developers by publishing seed agents, and each developer independently tests its agent to ensure that it is compatible with every seed-compatible agent, a property we call future-proofness. Under this structure, joint compatibility is guaranteed for any agents that are designed and tested independently, without any coordination with each other. In this work, we first formulate compatibility for general multi-agent systems and show why it is not trivially implied by seed-compatibility. We then characterize the future-proof agents as the closure of the seed and show that this closure is monotone in the seed. Finally, we study a class of executable tests that involve interaction with the seed alone, and we ask to what extent such tests can distinguish the future-proof agents.

### 19. RobotAgentBench: Towards Open-world Robot Autonomy
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-26T00:26:30+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.34649
- Summary: Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm for this transition, integrating task discovery, contextual reasoning, physical execution, and adaptive recovery into a closed interaction loop. However, existing benchmarks largely evaluate isolated capabilities, failing to capture the complexity of open-world robot autonomy. We introduce RobotAgentBench (RAB), a comprehensive benchmark for evaluating robot agents in realistic, open-world household environments. Through an agent-assisted, human-in-the-loop real-to-sim pipeline, RAB constructs 50 diverse household layouts with interactive objects and physically grounded tasks, encompassing 90 atomic tasks, 18 short-horizon tasks, 8 long-horizon tasks, and 4 open-ended scenarios. RAB provides a multi-level evaluation of robot agent capabilities: (1) task-level assessments systematically examine five complementary dimensions: task discovery, context reasoning, manipulation, failure recovery, and robustness; (2) scenario-level evaluation assesses how agents integrate these capabilities to autonomously fulfill high-level user needs. Furthermore, RAB enables systematic comparisons of standalone VLA/WAM models and diverse robot agent architectures under a unified planning-execution-verification framework. Extensive experiments reveal substantial gaps between manipulation and autonomy, demonstrate the advantages of agentic architectures and recursive self-improvement, and highlight the remaining challenges toward open-world robot autonomy.

### 20. Strategic Calibration in LLM Multi-Agent Systems: Audited Pivot Scoring for Truthful Elicitation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-24T15:18:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.33728
- Summary: In large language model (LLM)-based multi-agent systems, reported confidence increasingly determines the allocation of scarce downstream attention, computation, and decision influence. This makes reporting strategic: an agent may overstate the relevance of its contribution even when its underlying belief is well calibrated. Existing calibration methods largely assume passive reporting and therefore do not address strategic incentives created when confidence determines downstream allocation. We formulate strategic calibration as a reporting-layer incentive problem and propose the Audited Pivot Scoring Mechanism (APSM). APSM offsets platform-controlled allocation benefits, uses inverse-propensity-weighted sparse audits, charges the Clarke pivot externality, and applies a strictly proper score. Under the stated model assumptions, truthful reporting is the unique expected-utility best response. We also characterize approximate execution and the audit-variance trade-off. Calculator-free experiments show that LLM agents inflate confidence under Top-$K$ incentives. With a shared agent-local utility interface, LLM agents reduce distortion under both Compensated Proper Scoring (CPS) and APSM. CPS achieves higher exact allocation match, whereas APSM yields lower Brier loss and numerically fewer cutoff crossings. Experiments further show that APSM enlarges the utility margin against allocation-changing deviations by $1.93\times$ and improves robustness under approximate execution. These results support incentive-aware elicitation as a distinct layer for reliable multi-agent coordination.

### 21. CoEvolve: Counterfactual-Guided Co-Evolution of Memory and Collaboration in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-24T08:35:39+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.33539
- Summary: Large language model (LLM)-based multi-agent systems have demonstrated remarkable capabilities across diverse tasks. Yet their memory and collaboration architectures often remain static, constraining continued adaptation and improvement over time. Recent work addresses this limitation by evolving memory or collaboration based on interaction experience. However, updates to these interdependent components are not necessarily aligned: an evolved workflow may require experience that memory does not provide, while evolved memory may encode guidance that the workflow cannot use. To address this problem, we propose CoEvolve, a skill-centered framework for aligned memory--collaboration evolution. CoEvolve represents reusable local collaboration patterns as skills that link evolving collaboration decisions to their supporting memories. It further compares original and counterfactual trajectories to identify local evolution signals, which coordinate updates to the skill library, skill memory, and executor memories across rounds. Experiments on the ALFWorld and WebShop benchmarks confirm that CoEvolve achieves the best overall performance among the evaluated baselines, while ablation studies further validate the effectiveness of aligned co-evolution and counterfactual-guided evolution.

### 22. SCOPE: Scene-graph Construction Optimized by Plan Error-correction for Robot Long-term Planning Datasets
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-22T16:31:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.31518
- Summary: Task and Motion Planning (TAMP) stands as a fundamental challenge in robotics, essential for enabling autonomous agents to execute complex, long-horizon tasks in diverse environments. While Large Language Models (LLMs) introduce a new paradigm for TAMP by leveraging extensive common sense, their inherent reasoning limitations hinder direct application, and fine-tuning strategies to enhance these capabilities are currently bottlenecked by the scarcity of high-quality datasets. Existing automated generation methods often suffer from homogeneity, limiting model generalization, and unsolvability, where hallucinated scene graphs create physical mismatches with task goals. To address these issues, we propose Scene-graph Construction Optimized by Plan Error-correction (SCOPE), an automated framework designed to generate diverse and executable TAMP datasets. SCOPE incorporates multi-level diversity metrics to maximize the information entropy of scenarios. Crucially, it introduces a Plan Feedback Error-correction pipeline that utilizes planner execution failures as feedback signals to retroactively rectify logical inconsistencies in scene graphs, ensuring physical feasibility. Experimental results demonstrate that SCOPE exhibits greater robustness to erroneous scene graphs and generates higher-quality data. When utilized for LLM fine-tuning, SCOPE-generated data yield a downstream TAMP model that achieves an absolute 12.33% gain in success rate over its counterpart fine-tuned with data generated by DELTA, a state-of-the-art PDDL-based planner.

### 23. Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-20T14:15:04+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.28259
- Summary: Recent advances in visuospatial understanding and agentic reasoning enable direct robotic manipulation with general-purpose multimodal models, but their embodied capabilities remain poorly understood. This paper systematically evaluate GPT-6 Astra for closed-loop robotic manipulation using a lightweight agent execution framework. We first probe three fundamental embodied capabilities-depth perception, embodied in-context learning, and tactile understanding-and demonstrate that the model can exploit depth information, acquire simple manipulation strategies from contextual demonstrations, and use tactile feedback to correct its actions. We then evaluate GPT-6 Astra across five established manipulation benchmarks along six capability dimensions. Despite competitive performance on several benchmarks-26.92\% success on RoboDojo and 76.0\% on RoboTwin 2.0-our analysis reveals a pronounced gap between semantic reasoning and physical execution, particularly in consequence-aware action planning, precision, and complex motion coordination. To further examine these limitations, we introduce LIBERO-GeoMotion, a new benchmark of geometry-constrained tasks that require precise pose alignment, coordinated translation and rotation, and anticipation of physical action consequences. GPT-6 Astra achieves only 11.1\% zero-shot success, exposing the difficulty of translating spatial understanding into physically feasible motion. Real-world experiments corroborate these findings: zero-shot execution is feasible for simple tasks, yet persistent deficits remain in motion feasibility, precise control, and physical safety, while substantial inference latency further hinders practical deployment. Overall, our results characterize the emerging embodied capabilities of general-purpose multimodal models and delineate the key challenges toward safe, efficient, and reliable robotic manipulation.

### 24. Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-19T17:30:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.27039
- Summary: Foundation models offer a promising basis for robotic agents, but long-horizon tasks require them to sustain coherent reasoning and reliable physical execution across interdependent stages. We introduce Embodied Playground, a benchmark for evaluating how foundation-model agents coordinate physical, strategic, and spatial reasoning throughout such tasks. Agents must track task progress, satisfy intermediate constraints, and revise their plans using execution feedback as earlier actions shape subsequent decisions. The playground comprises 410 task environments spanning basic manipulation, sequential puzzles, and multi-stage household activities, with variations in planning depth, geometric constraints, and physical execution demands. We curate EP-100, a representative selection of 100 tasks across five suites and 16 task types, together with the EP-Easy and EP-Hard difficulty splits and the compact EP-20 selection. A shared protocol specifies observation and tool access, resource budgets, repeated trials, and independent checks of goal completion, task-rule compliance, and physical validity. Embodied Playground provides a unified framework for studying whether foundation-model agents can sustain effective reasoning and action over extended task horizons. https://winniechen2002.github.io/Agent-bench-website/

### 25. IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-17T02:36:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.24383
- Summary: Improving every agent in an LLM-based multi-agent system can be prohibitively costly, making it important to identify which agent should be prioritized to achieve the greatest system-level gain with limited resources. Failure attribution can inform this decision, but an agent's responsibility for failures does not directly reveal the system-level gains achievable by improving it. We therefore introduce IF-MAP, an influence-function-inspired method for identifying agents with high potential for system-level improvement. For each agent, IF-MAP measures end-to-end loss changes under controlled semantic prompt perturbations, fits a regularized local response model in a low-dimensional prompt-embedding subspace, and uses the estimated response norm as a priority score. This black-box procedure requires no access to model parameters or gradients and produces agent priorities that can guide subsequent improvement effort. We evaluate IF-MAP across six multi-agent workflows spanning code generation, question answering, and mathematical reasoning, using the same priorities for prompt optimization and model upgrades. Optimizing the selected agents' prompts achieves a macro-average gain of 3.81 percentage points, compared with 1.85 for uniform agent selection. Across five target models, upgrading the selected agents yields macro-average gains of 7.62-16.42 percentage points, compared with 3.81-8.62 for uniform agent selection. Despite its probing overhead, IF-MAP reduces Qwen3-8B and DeepSeek-V3.2 token use by 74.2% and 35.2%, respectively, relative to optimizing every agent, and reduces target-model tokens by 63.6-64.9% relative to upgrading every agent. These results support the use of IF-MAP to identify promising agents and direct improvement effort toward greater end-to-end performance gains.

### 26. From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-16T11:23:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.23319
  - Alt: https://arxiv.org/abs/2610.18792
- Summary: Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences. As a result, memory has become a fundamental component for enabling embodied agents to perform long-horizon reasoning and adaptive decision-making. This survey presents a systematic taxonomy of VLA memory mechanisms based on memory scope and persistence, categorizing existing approaches into five representative paradigms and one emerging frontier. Based on this taxonomy, we compare representative VLA memory systems in terms of memory characteristics, architectural com-plexity, and open-source maturity, revealing a clear trade-off in which increasing architectural complexity is generally accompanied by decreasing open-source ma-turity. Finally, we discuss the key challenges in building full-lifecycle memory systems, including efficient memory management and lifelong knowledge evolu-tion. Overall, this survey provides a unified perspective on memory architectures for VLA agents and offers insights into the development of lifelong embodied in-telligence.

### 27. SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-16T05:29:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.22959
- Summary: Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions. However, information collected from external sources can introduce security risks when untrusted claims (i.e., atomic statements) are later treated as authorized preferences, policies, or permissions. Existing defenses typically rely on content-based filtering or coarse-grained provenance tracking, which either fail to prevent unauthorized memory use or block legitimate information, sacrificing memory utility. To address these limitations, we propose SAFE-Mem, a fine-grained memory governance framework that improves security while preserving legitimate memory use. First, SAFE-Mem annotates each claim with three governance labels (i.e., kind, authority, and scope) to capture its provenance and permitted use. Second, governance-aware retrieval matches query requirements with claim permissions to block unauthorized influence while retaining legitimate information. Third, a governance-enabled memory graph connects source sentences, claims, and entities to support provenance tracking and efficient retrieval. Across four LLM backbones on MPBench and LoCoMo, SAFE-Mem attains the lowest attack success among defenses that retain legitimate memory, at least 77% below the strongest of them, and the highest answer accuracy of all evaluated defenses, improving it by up to 15%. The code is available at https://github.com/LVenum/SAFE-Mem.

### 28. Towards Agentic Robots: Model, Data, Environment, and Harness
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-14T16:32:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.20442
- Summary: Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic environments, rectify execution errors autonomously, and dynamically adjust operational strategies. Although this field develops fast, current studies are not well connected. Researchers have no consistent view of how to combine different agentic functions into a complete robot system. This paper provides a unified overview of existing research on agentic robots. We first trace the development from robot policies to agentic systems, covering vision-language-action models, world models, and world-action models. We then clarify the definition and scope of agentic robots and organize existing research into seventeen categories across four functional domains: Model, Data, Environment, and Harness. Across these domains, we examine how agents shape model learning and robot decisions, collect and curate robot data, construct worlds, tasks, and tests for learning and evaluation, and organize capabilities for robot use. Finally, we discuss open challenges and outline directions for future research. Looking forward, we hope this work contributes to a clearer understanding of agentic robots and supports new approaches to making them more capable, reliable, and adaptive.

### 29. CLARA: Compound Library Active Learning with Reasoning Agents
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-12T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.05.756921
- Summary: Batch active learning for ligand discovery requires a recurring decision about whether to exploit high predicted affinity, reduce model uncertainty, or broaden chemical coverage. We test whether a language model can make this strategy-level decision while candidate ranking and label revelation remain controlled by a deterministic Gaussian-process environment. Across four protein targets, ten paired seeds, and a 360-compound assay budget, a GPT-5.6 Sol agent outperformed random sampling in all 40 matched campaigns. Its final top-2\% recall was 0.412 on D2R, 0.374 on Mpro, 0.448 on TYK2, and 0.683 on USP7. It was statistically tied with the strongest fixed policy on Mpro and USP7 but underperformed target-specific leaders on D2R and TYK2. The agent shifted from exploration-oriented early batches toward exploitation and produced 686 testable threshold claims with an 86.3\% atomic success rate, although 19.8\% of forecasts were not numerically scorable. In 200 prespecified information-ablation campaigns, removing uncertainty, diversity, or memory caused only small endpoint changes, while shuffling explanatory evidence reproduced the full allocation path in 39 of 40 paired campaigns. A deterministic 80\% availability constraint reduced recall on every target but preserved the target-dependent pattern of wins and losses. These results support language-model strategy control as a feasible and auditable layer.

### 30. Competence-Aware Orchestration for LLM-Based Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-09T07:33:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.13144
  - Alt: https://arxiv.org/abs/2609.37094
  - Alt: https://arxiv.org/abs/2610.23673
  - Alt: https://arxiv.org/abs/2610.11600
- Summary: LLM-based multi-agent systems (MAS) have emerged as a promising paradigm for enhancing complex reasoning through role specialization and collaboration, yet a key challenge remains: how can collaboration be adapted to a backbone's competence on the current query? This problem matters because more collaboration is not always better--richer coordination may help on difficult cases, but it also incurs additional token cost and redundant interactions. We propose a two-stage competence-aware framework for automatic MAS orchestration. It first models the LLM backbone's task-conditioned competence for the current query, and then uses this signal to adapt role activation and the communication graph. Across six benchmarks, our method achieves an average score of 93.81%. Experiments with six LLM backbones of varying competence levels further show that our method adjusts collaboration according to the inferred competence: for higher-competence backbones, it improves average accuracy from 87.22 to 89.97 while reducing token cost by 36.26%; for lower-competence backbones, it yields a further average gain of 4.58 points over existing methods. The same trend also holds on unseen backbones.
