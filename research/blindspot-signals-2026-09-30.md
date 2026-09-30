# Blindspot Signals Report - 2026-09-30

- Source export: `/opt/apps/haier/exports/evolution_signals_20260930_020412.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 521
- Deduped/weighted signal clusters: 493
- Novel vs previous reports: 43
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. LLM-Based Multi-Agent Systems over Wireless Networks: A Joint Agent--Network Design Perspective
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T09:19:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.37094
- Summary: As large language models (LLMs) evolve from standalone models into collaborative agents embedded in physical systems, their reasoning and execution are increasingly distributed across wireless edge nodes. In this setting, wireless networks are experiencing a paradigm shift from only providing data connectivity to supporting the multi-agent reasoning workflow itself. The task performance of such network-constrained LLM-based multi-agent systems (MASs) is jointly affected by the multi-agent reasoning dependencies as well as the underlying network connectivity and edge resources. This coupling gives rise to various technical challenges, including the metric misalignment and message redundancy, state inconsistency and topology mismatch, as well as resource limitation and trust discontinuity. To address these challenges, this article develops a novel joint agent--network design perspective that coordinates decisions on both sides of the system. Specifically, we present the joint design of agent--interaction scheduling and resource allocation, the message selection-transmission co-design, as well as the joint agent--network topology design and workload--resource allocation. Furthermore, we consider the network-verified provenance that is linked with agent-side information-flow control to constrain how received information affects subsequent operations. An illustrative vehicle-to-everything (V2X) case study shows that jointly adapting agent-side interaction decisions and network operations improves task completion under communication and edge-resource constraints, outperforming the conventional agent-only and wireless-only separate designs.

### 2. Trajectory-Level Mode Guidance for Controllable Diffusion-Based Multi-Robot Motion Planning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T02:22:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36530
- Summary: Motion planning often admits multiple feasible solutions, making multimodal generation valuable, particularly for flexible multi-robot coordination. Diffusion models naturally learn such trajectory distributions, yet incorporating coarse and partial trajectory priors without restricting generation remains challenging. Such priors indicate a desirable region of the solution space rather than a single solution, motivating conditioned generation that preserves multimodality. In this paper, we guide trajectory generation in the clean trajectory space and progressively incorporate trajectory priors with a timestep-dependent guidance strength. At each reverse diffusion step, the reconstructed clean trajectory provides a unified space for integrating planning costs and partial trajectory priors. Planning costs are incorporated through gradient-based refinement, while the partial prior is progressively injected at the corresponding noise levels with decreasing guidance strength. This guides generation toward the prior in early stages while gradually releasing the constraint to preserve the inherent multimodality of the diffusion model. The framework naturally extends to multi-robot planning by incorporating inter-robot collision costs. Experiments on single- and multi-robot planning tasks demonstrate controllable trajectory synthesis, diverse feasible solutions, and safe multi-agent coordination.

### 3. SkillWeaver: Agentic Exploration over Neural Interaction Skills for Scalable Robot Data Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T19:41:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36171
- Summary: Large-scale demonstrations have driven unprecedented progress in robot learning, yet collecting robot data through teleoperation is expensive and difficult to scale to diverse environments and long-horizon tasks. Simulation offers a scalable alternative, but existing data-generation pipelines often rely on open-loop controllers, scripted skill sequences, or task-specific programs. We introduce SkillWeaver, an agentic framework that autonomously generates robot experience by exploring over Neural Interaction Skills (NIS): reusable, parameterized, closed-loop policies that expose learned physical interaction capabilities to a reasoning agent. Given a task and a simulated environment, a VLM agent reasons about what to do next, invokes and parameterizes NIS to interact with the environment, observes their outcomes, and generates verification, reflection, and memory to guide subsequent exploration. We instantiate NIS as reinforcement-learned policies for closed-loop, contact-rich manipulation and organize exploration as verifier-guided tree search, enabling the agent to discover successful long-horizon behaviors without relying on predetermined execution pipelines. SkillWeaver scales autonomously to 39.1K demonstrations across 14.1K scenes, which we distill into visuomotor policies. Across simulation benchmarks and real-world manipulation, training on SkillWeaver-generated experience substantially improves generalization to novel objects, spatial configurations, tasks, and environments, and enables zero- and few-shot sim-to-sim and sim-to-real transfer. Our results suggest agentic exploration over neural interaction skills as a scalable alternative for robot data generation.

### 4. Memory in the Sky: Low-Altitude Question Answering with Multi-Agent Memory Aggregation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T15:36:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.35431
- Summary: This paper studies low-altitude question answering (LAQA), in which distributed unmanned aerial vehicle (UAV) memories are aggregated at a ground server to answer questions about observations over a long horizon. Unlike conventional resource allocation based on sensing, communication, control, or computation metrics, LAQA requires an explicit measure of memory value. We propose a generative adversarial exam (GAE) that uses forward simulation to evaluate memory retrieval and exam scores to quantify memory quality. This enables the downstream QA value of candidate memories to be measured and optimized without accessing the internal mechanisms of the black-box captioning, retrieval, and reasoning pipeline. Building on this metric, we develop a memory-centric (MemCen) framework that jointly selects UAVs and allocates transmit power to maximize memory quality under communication constraints. In the noise-limited regime, we derive a QoM-aware capped water-filling law that explicitly connects task utility with physical-layer power allocation. We further develop penalty successive optimization (PSO) and learning to memorize (L2M) solvers. MemCen achieves QA accuracies of 92.4% and 84.0% in CARLA Town04 and Town05 under static and dynamic communication conditions, respectively. In real-world experiments, MemCen achieves 88.5% QA accuracy on the panoramic multi-agent system (PMAS) benchmark. Finally, UAV-to-robot-dog demonstrations further validate the practical utility of the acquired memories for environmental understanding and navigation.

### 5. Recent Advances in Agentic Agri-Robotic Phenotyping: A Perspective Review from Fragmented Multimodal Sensing to Unified PhenoAgent Intelligence
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T08:18:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.34567
- Summary: This review examines the evolution of plant phenotyping from conventional manual trait measurement to high-throughput, robotic, and artificial intelligence-driven crop monitoring. Despite significant advances in imaging, autonomous platforms, multimodal sensing, and deep learning, current phenotyping systems remain fragmented across sensing modalities, crop traits, growth stages, environments, and management objectives. We therefore frame phenotyping as an integrated \emph{seed-soil-plant-environment-management} (SSPEM) intelligence problem, where crop performance reflects interactions among seed quality, root-zone conditions, plant development, environmental exposure, and management actions. The review synthesizes conventional, high-throughput, robotic, and AI-driven phenotyping approaches, highlighting their capabilities and persistent limitations in temporal integration, multimodal reasoning, biological interpretation, and actionable decision support. Building on this analysis, we introduce a conceptual PhenoAgent framework that extends phenotyping beyond the estimation of isolated traits to evidence-based crop-state interpretation, uncertainty-aware reasoning, and management-oriented support. The PhenoAgent concept primarily brings together scattered advances in phenotyping to deliver insights ranging from detailed to high-level, such as what is happening in the crop, why it might be occurring, what evidence is missing, and what actions or additional measurements should be considered. We also discuss challenges in dataset scarcity, annotation, benchmarking, model generalization, and explainability. By linking multimodal phenotyping with agentic AI and closed-loop decision support, this review outlines a path to interpretable, scalable, and deployment-oriented crop intelligence.

### 6. MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-29T17:36:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.38078
- Summary: Vision-language-action (VLA) models have advanced robotic manipulation, but their zero-shot generalization in new tasks and environments remains limited, and their reliance on specialized training keeps them from benefiting directly from rapidly advancing general-purpose vision-language models (VLMs). In parallel, recent agentic robotic systems leverage VLMs for high-level reasoning or coding agents for robot control, but often depend on extensive external models and tools, introducing additional complexity and cost. This motivates us to ask: Can a general-purpose VLM itself operate a robot more like the human teleoperator by reasoning directly from observations, issuing actions, and continuously adapting to execution feedback, without relying on external models such as learned action experts, coding agents or grounding tools like SAM3? In this work, we introduce MotorMind, a robot manipulation harness that connects VLM-proposed mid-level actions to deterministic robot control and feedback, with asynchronous monitoring and background memory updates. Without task-specific policy training, coding agents, or additional grounding tools such as SAM3, MotorMind achieves 66.7% success on the base LIBERO-PRO suites and 53.8% under perturbations, compared with at most 13.3% and 19.2%, respectively, for the prior zero-shot methods we evaluate. The same interface reaches 95% average success on a real xArm6 robot across direct manipulation and human-perturbation settings. Replacing the backbone with a stronger VLM further improves performance, while the remaining failures - primarily due to visual grounding, embodied reasoning, and action knowledge - decrease as VLM capability improves. These results show that a general-purpose VLM, when equipped with an appropriate mid-level action representation and asynchronous execution harness, can perform effective zero-shot robotic manipulation.

### 7. Towards Spatial Perception for Heterogeneous Robot Collaboration in Subterranean Mining Environments
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-29T12:49:00+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.37419
- Summary: The autonomous extraction of deep mineral deposits in abandoned underground mines is fundamentally a multi-agent integration problem. No single platform simultaneously offers the mobility to traverse kilometers of degraded drifts and the sensing payload required to characterize an ore body. This article presents the onboard perception pipeline that bridges two heterogeneous agents within the PERSEPHONE autonomous mining mission. Which consist of a lightweight Explorer robot that maps an unknown mine and generates a 3D scene graph of inspection targets, by running a zero-shot, vision-language semantic segmentation stack that detects mineral deposits directly from natural-language prompts. The map and the graph are then handed to a second Inspector robot, which carries an advanced sensing payload and uses them to plan close-range inspection viewpoints. We detail the complete pipeline, with emphasis on the geometric abstraction that turns raw detections into actionable inspection targets, spanning per-view bounding-box generation, cross-view box merging, plane fitting, and polygon extraction, and we report an extensive field validation in a subterranean test facility and in an active magnesite mine, covering both iron-vein and magnesite mineralization under realistic, perceptually degraded conditions.

### 8. UpliftMem: Learning Set-Level Uplift for Agent Memory Retrieval
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-29T06:17:15+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.36805
- Summary: Large language model (LLM) agents reuse external memory to guide new tasks, but effective retrieval requires learning which memory sets improve execution. Such learning relies on costly outcome feedback: ordinary retrieval observes only executed sets, while evaluating alternatives requires additional rollouts. We introduce \textsc{UpliftMem}, which learns memory retrieval from set-level execution uplift relative to the same executor without memory. A theoretical analysis of how retrieval preferences restrict feedback coverage motivates targeted probing of alternative memory sets. Probe selection follows an expected value of sample information (EVSI) criterion, derived in closed form under a correlated Gaussian model, to allocate limited training rollouts according to their expected improvement in local retrieval decisions. The shared scorer is trained with a frozen executor and selects memory sets without test-time probes. Across ALFWorld, WebShop, and BigCodeBench, \textsc{UpliftMem} achieves the best success rates among evaluated baselines on the main evaluation sets. Controlled fixed-store and matched probe budget evaluations further demonstrate improved memory-use decisions and more effective use of execution feedback.

### 9. ResonAct: Streaming Metrics for Runtime Diagnosis and Self-Healing in Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-28T09:18:24+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.34701
- Summary: Multi-agent systems (MAS) are increasingly used to automate enterprise workflows involving multiple specialized agents, external tools, and long-running task execution. Failures may arise from tool degradation, context propagation errors, coordination breakdowns, or repeated agent interactions that prevent task completion. While existing observability frameworks provide traces and logs, diagnosis and remediation are largely performed after execution completes, limiting opportunities for recovery during runtime. We present ResonAct, a runtime self-healing framework that enables continuous monitoring, diagnosis, and remediation of multi-agent systems through streaming operational metrics. ResonAct ingests execution traces, agent interactions, and tool invocations into a streaming analytics layer that continuously derives task progress, context health, and tool reliability metrics. These metrics serve as runtime control signals for detecting anomalous execution patterns and localizing root causes using a structured failure model. Based on the diagnosed failure, ResonAct dynamically selects remediation policies and performs actions. The framework operates as an external control plane, enabling intervention without modifying application agents or orchestration logic. We evaluate ResonAct across enterprise workflow scenarios and AppWorld benchmarks. The results show that the streaming metric-based analysis identifies execution degradations and localizes faults. Furthermore, policy-driven remediation improves task completion rates by up to 10.00 percentage points, with detection precision ranging from 70.59% to 82.91%, recall from 63.09% to 100%, recovery rates from 10.48% to 46.67%, and runtime overhead ranging from $-0.25%$ to 14.12% across the evaluated configurations.

### 10. LLMs for Executable Multi-Agent System Specification Generation
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-28T08:43:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.34619
- Summary: MAS specifications express the effects of the actions of the agents and their environment, as well as other temporal phenomena, such as the intervals during which an agent may perform an action. The specification of a MAS should also be executable in order to allow for run-time monitoring. Constructing the specification of a MAS requires formal language expertise, while machine learning techniques depend on labelled data which are rarely available. To address these issues, we propose `genRTEC', a method that leverages pre-trained Large Language Models (LLMs) to generate executable MAS specifications, in the language of the `Run-Time Event Calculus' (RTEC), from natural language descriptions. genRTEC constructs MAS specifications with complex hierarchical and cyclic dependencies based only on short natural language descriptions of the concepts involved. We present an extensive empirical evaluation of genRTEC, spanning various MAS specifications, including both a qualitative and a quantitative assessment. Our results demonstrate that genRTEC constructs executable MAS specifications of high predictive accuracy without compromising reasoning efficiency.

### 11. MAS-OPD: On-Policy Distillation for Multi-agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-28T03:39:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.34234
  - Alt: https://arxiv.org/abs/2608.22130
- Summary: Multi-agent systems (MAS) split a task across specialized roles and are promising on complex tasks, yet a prevailing approach relies on inference-time orchestration alone. General-purpose APIs are costly and hard to customize, while small models with role prompts rarely develop stable role competence or reliable collaboration, so post-training a MAS jointly is central. Most attempts use reinforcement learning, whose team-level reward leaves undetermined which step of which agent brought about the outcome, while local rewards need redesigning per task. On-policy distillation (OPD) gives token-level teacher supervision on trajectories the student samples, a denser signal needing no local reward, yet is underexplored for the interdependent agents of a MAS. Two difficulties arise: building complementary specialization from a judgement of which role a behavior belongs to while preserving the knowledge all roles need, and turning cross-agent collaborative information into supervision OPD can exploit. We present MAS-OPD, where Role-Advantage Specialization defines the role advantage as the difference between the teacher signals under target and non-target role conditions, and Privileged Attribution for Coordination attributes an interaction conflict to its source and supplies it to the teacher alone as privileged information. Extensive experiments on code and mathematics benchmarks show that MAS-OPD attains the highest mean score at both student scales and leads the agents to develop clearer role specialization and more effective collaborative behavior.

### 12. When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory with a Typed Decision Model
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-28T03:34:07+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.34227
- Summary: Does conversational memory need LLM-extracted facts, or is selecting the right raw turns enough? Published results disagree. Extraction-based systems report gains from distilled facts. Recent studies find raw history with good ranking does as well, but disagree about whether ranking matters. We ran a pre-registered study on held-out LoCoMo conversations and LongMemEval. At a tight budget on LoCoMo, raw turns selected by a single call to Jev, a typed decision model, are non-inferior to an LLM-extraction memory (one-sided 95% bound -3.0 points against a -5-point margin). Blind human grading narrows the margin but does not change the result. Raw turns cost 3,061 times less to write, and the result holds with a second answer model. Within this study, reranking's gain shrinks as the budget grows. It adds 17.4 points on LoCoMo and 9.1 on LongMemEval when three of 30 candidates are kept. At generous budgets it adds 1.5 and 1.1, and extraction systems are more accurate. This suggests why published results disagree. At matched context, Jev selects as accurately as an LLM reranker (non-inferiority bound -2.0) at a third of the latency, and more accurately than a multi-call graph traversal. Reranking lowers correct abstention. Plans, code and graded answers are released.

### 13. KVCMAS: Efficient KV cache Correction for Shared Context in Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-28T00:39:50+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.34060
- Summary: Prompt-specialized multi-agent systems enable multiple agents to share a model while performing complementary roles to solve complex tasks. However, agent-specific prefixes change the KV cache generated for the same shared context, causing each agent to repeatedly prefill the growing context and construct a separate cache with high computation and memory overhead. Selective recomputation reduces this redundancy but still retains substantial model execution, while existing delta correction methods either support only recurring context relations or maintain memory-intensive online correction states for dynamically changing context. For first seen shared context, these methods also construct a reference cache outside the agent workflow, and an approximate correction at the first agent affects the outputs passed to subsequent agents. We present KVCMAS, an online KV cache correction framework that represents cross-agent cache deviations using compact low-rank states and seamlessly chains corrections along the agent workflow without an additional reference prefill. This design supports dynamically changing shared context while preserving an exact first-agent cache. Across multiple language and vision-language workloads, KVCMAS matches or improves the accuracy of prior KV cache sharing methods while achieving the lowest TTFT under highly concurrent serving. Under controlled serving traces, it provides a 2.0x TTFT speedup over inference without KV cache sharing and reduces peak GPU memory by up to 3.7x relative to a prior KV cache correction method. These results establish KVCMAS as an accurate and scalable KV cache sharing approach for prompt-specialized multi-agent serving.

### 14. Agentic transcranial functional ultrasound imaging: @fUS
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-28T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.09.25.752961
- Summary: Functional ultrasound (fUS) imaging provides deep, wide-field access to brain function, but instrument cost and complex acquisition and analysis workflows restrict its wider adoption. Here we introduce @fUS, an agentic transcranial imaging platform with an open architecture that integrates purpose-built hardware with executable experimental skills and persistent structured memory. The system combines 128-channel, 16-bit acquisition at 125 MHz with GPU-based processing and enables functional imaging through the intact scalp and skull of mice, with approximately 100-m spatial resolution and 10-Hz temporal sampling, providing a basis for longitudinal studies without cranial-window surgery. Its agent connects scientific objectives to experimental design, direct instrument control and data analysis, retaining context across interactions and supporting inspectable workflows through text and hands-free voice control. Neuroscience trainees with limited engineering experience independently configured the system within 30 min. Agent-assisted exploration of whisker-stimulation datasets revealed low-frequency vascular changes beyond conventional response mapping, supported by complementary two-photon measurements of single-vessel diameter. By combining transcranial imaging with accessible instrument control and analysis, @fUS provides a foundation for wider adoption and larger, more diverse neuroscience datasets. More broadly, it offers a framework for scientific instruments in which measurement, computation and experimental reasoning are developed as parts of the same system.

### 15. Coding Agent Memory Post-training: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via Reinforcement Learning
- Weighted score: 0.18
- Deep score: 0.1
- Coverage: 2 sources (arxiv, hackernews)
- Date: 2026-09-28T06:40:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.34422
  - Alt: https://calpaterson.com/memoryfields.html
- Summary: Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. Recent work has begun to use reinforcement learning to make memory control part of the policy, often relying on predefined memory tools within domain-specific training environments of relatively short horizons. This setup ties learned memory behavior to environment-specific interfaces that lie outside the base model's pre-training and must be learned from scratch, so even after post-training, agents struggle to use memory in long-horizon tasks. To address these limitations, we introduce Coding Agent Memory Gym (CAMG), a suite of long-horizon agentic-RL environments spanning Shop, Coding, DeepResearch, and AutoResearch. Alongside each environment's native task interface, CAMG provides executable shell access and an episode-persistent workspace, enabling agents to create, revise, search, and reuse files as memory throughout an episode. We also introduce CAMG-RL, which trains a single policy jointly across all four environments with fully asynchronous PPO, learning this file-based memory behavior directly from downstream task reward, and we train CAMG-RL-4B and CAMG-RL-9B from Qwen3.5 models of matching size. On SWE-bench Verified and MLE-bench Lite, CAMG-RL-4B and CAMG-RL-9B are competitive with Qwen3.5-35B-A3B and Qwen3.5-122B-A10B, respectively.

### 16. NVIDIA / OpenShell
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-30T02:01:49.139023+00:00
- Primary source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/NVIDIA/OpenShell
- Summary: OpenShell is the safe, private runtime for autonomous AI agents.

### 17. Skill-Space Shooting for Autonomous Robot Policy Improvement
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-29T17:59:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.38178
- Summary: Robots deployed in the physical world must be able to improve beyond their initial training as they encounter new situations and failures. For this improvement to scale across tasks, it must make effective use of experience without requiring human demonstration of each correction. Recent agentic systems offer a way to reduce this reliance on human effort by using foundation models to autonomously compose learned behaviors to complete tasks. Yet completing tasks this way does not itself teach a task policy to overcome its own failures; that requires turning these behaviors into learnable corrections for the policy. Our insight is that many such corrections are familiar short behaviors, or skills: they recur across tasks and describe actions that foundation models can reason about from a scene. We introduce skill-space shooting, which uses foundation model guidance to explore corrections through these reusable skills and turn successful trials into policy improvement. Real-world experiments show repeated improvement in policies acting autonomously, while skills can also be shared to reduce the teaching needed to improve on new tasks. By making reusable skills a source of corrective supervision, skill-space shooting enables scalable and generalizable policy improvement within and across tasks. Additional results and videos at https://skill-space-shooting.github.io.

### 18. How Can Recommendation Feedback Evolve Agent Memory?
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-29T13:22:20+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.37544
- Summary: Content-generation agents continuously receive impressions, clicks, conversions, and negative feedback from recommendation systems, providing real-world outcome signals for memory evolution. However, these signals are delayed and noisy, confounded by audience composition, placement, and recommendation policies, and may result from the combined influence of multiple memories, making accurate attribution difficult. Existing methods rely primarily on immediate feedback or semantic retrieval and therefore struggle to reliably translate recommendation outcomes into memory fitness. To address this challenge, we propose TIDE (Trajectory-Informed Directed Memory Evolution), an external memory evolution framework driven by delayed recommendation feedback. We further introduce Memory Evolution Gain (MEG), which measures the utility improvement of evolved memory over a no memory baseline on strictly future tasks. TIDE treats memory as a capacity-constrained population of experiences: temporal and semantic credit assignment estimates contextual fitness, while responsibility credit distributes outcome signals according to the memories referenced during generation. These signals are then used to reinforce, crossover, mutate, or evict memories. On an e-commerce membership marketing content-generation agent, TIDE achieves a +7.75-percentage-point MEG in offline temporal replay and significantly improves both unique click-through rate (UCTR) and activation rate in an online A/B test. On a delayed-label benchmark, TIDE achieves the lowest mean absolute error (MAE) and root mean squared error (RMSE) and the highest MEG among the compared methods, demonstrating its effectiveness.

### 19. Simple Agentic Memory for Generalist Robot Policies
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-29T03:16:27+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36595
- Summary: Visual-memory systems commonly retain or compress past observations. Robot control additionally requires interaction-derived state that no individual frame may explicitly represent, such as persistent identity relations, accumulated progress, or ordered procedures. We introduce Simple Agentic Robot Memory (SimpleARM), a training-free memory layer for frozen generalist robot policies. From the task instruction, SimpleARM specifies what to monitor; frozen perceptual tools maintain compact typed state online; structured access retrieves that state only when a proposed subgoal depends on history; and current-view grounding resolves recalled entities before execution. We evaluate SimpleARM on RoboMME, a benchmark of memory-dependent robot manipulation tasks that require history information no longer available in the current observation. Across all 16 tasks and three policy seeds, SimpleARM achieves 67.17% mean success, compared with 44.51% for the strongest non-oracle baseline. Matched ablations show mechanism specificity: removing relation, reference, progress, or route state produces large losses where the affected state is retrieved for control, while largely sparing other tasks. These results support a state-based view of robot memory: effective memory for control is not simply retained visual history, but compact task-relevant state derived from the interaction history.

### 20. MAADBench: The Refreshable Paradigm for Anomaly Detection in Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-29T02:42:00+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.36556
- Summary: Recent studies report that LLM-based multi-agent systems (MAS) fail at rates of 41%-87%, yet to our knowledge, no benchmark to date supports systematic anomaly detection (AD) for them. Building MAS AD benchmarks is hard because they must remain fresh as LLM systems evolve: tasks may leak into training data and thus be memorized by LLMs, traces and anomaly patterns expire as backbones evolve, and labels must be provided reliably for each refresh. To address these challenges, we present MAADBench (MA: multi-agent; AD: anomaly detection), the first refreshable MAS AD benchmark designed for diverse, evolving LLM backbones underlying the agents. MAADBench combines (1) sampled-and-coupled generative tasks over an approximately 10^37-task space to mitigate task leakage, (2) refreshable trace generation under configurable LLM backbones, and (3) automated provision of cost-free, deterministic step-level labels for fine-grained AD evaluation. Beyond offering the paradigm itself, we run MAADBench with five state-of-the-art LLM backbones and release the MAADBench-Full dataset with 5,200 step-labeled traces. Benchmarking 25 AD methods on the MAADBench dataset reveals substantial limitations in current approaches: they rely heavily on supervision, struggle with subtle MAS-specific anomalies, and lack robustness across LLM backbones. These gaps point to a rich research agenda for MAS-specific anomaly detection, with MAADBench providing a systematic and refreshable testbed for method development and evaluation. We open-source MAADBench-Full at https://huggingface.co/datasets/hww123/MAADBench-full.

### 21. AutoBCI: Forecast-Guided Agentic Neural Architecture Discovery for EEG-Based Brain--Computer Interfaces
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-28T15:46:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://arxiv.org/abs/2609.35456
- Summary: EEG-based brain-computer interfaces support a broad range of applications, yet designing decoding architectures that perform well across diverse tasks remains challenging. We introduce AutoBCI, an agentic framework in which a Designer Agent and a Forecaster Agent support the discovery and selection of EEG decoding architectures across tasks. The Designer Agent performs Pool-Guided Architecture Discovery (PGAD), generating and refining architectures through training and validation across multiple EEG tasks, such as emotion recognition, motor imagery, and sleep staging. The Forecaster Agent performs Performance Estimation from Early Knowledge (PEEK), using architecture code, the training protocol, and early learning curves to predict full-budget validation performance and select promising candidates for continued training. Across 14 EEG datasets spanning motor imagery, emotion recognition, and sleep staging, we evaluate AutoBCI with six LLMs, including Opus 5.5 and GPT 5.6 Sol, and compare the architectures selected by the search procedure against ten baselines: six conventional EEG models and four foundation models. The architecture discovered by AutoBCI with Claude Opus 5.5 achieves 64.16% average test balanced accuracy (bAcc), compared with 63.87% for REVE, the strongest baseline on this metric. Using ten observed epochs, PEEK reduces mean absolute error in predicting average validation bAcc from 2.20 to 1.36 percentage points, a 38.1% reduction relative to the best-observed-score baseline.

### 22. MASTraceBench: Diagnosing Collaboration Gains through Proposal Trajectories in LLM-Based Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-28T07:44:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.34496
- Summary: LLM-based multi-agent systems (MAS) have shown promise in complex problem solving. As MAS methods diversify, systematic evaluation becomes increasingly challenging. However, existing benchmarks largely focus on final outcomes, leaving unclear how collaboration gains arise, are preserved, or are lost. To address this limitation, we introduce MASTraceBench, a benchmark for diagnosing collaboration gains through proposal trajectories in MAS. Across six cooperative and competitive tasks, MASTraceBench tracks and grades proposal trajectories and provides a multi-layer metric suite covering Task Score, Collaboration Gain, proposal-trajectory indicators, and Token Cost. Using MASTraceBench, we systematically compare representative MAS methods not only by final performance, but also by how agent proposals evolve and are aggregated into the final answer. This analysis reveals a recurring pattern: final MAS answers rarely surpass the strongest initial proposal; interaction often lifts initially weaker proposals toward it, while strong initial proposals are seldom further improved and may regress. To reduce this risk, we propose CLEARS, which replaces whole-proposal exchange with claim-level evaluation across agents to guide reliable synthesis. CLEARS more often preserves or improves upon the strongest initial proposal and achieves the highest Collaboration Gain on five of the six tasks.

### 23. Just-In-Time Agent Memory with Runtime Agentic Research
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-28T06:01:09+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.34385
- Summary: Memory is critical for AI agents. Many existing agent-memory systems follow an Ahead-of-Time (AOT) design, constructing memory before a specific request arrives. While this reduces online serving cost, such request-agnostic memory construction can discard fine-grained information that later becomes important. To address this limitation, we propose Just-In-Time Agent Memory (JAM), a trainable framework for query-conditioned context construction at runtime. A Memorizer preserves complete raw histories in a hierarchical page-store with compact navigational summaries, while a Researcher iteratively retrieves, inspects, and integrates evidence for each request. To train these memory-use behaviors, we introduce Memory-Gym, an evidence-grounded data synthesis pipeline covering nine task types across six domains, and optimize the Researcher through verified-trajectory supervised fine-tuning followed by Hint-guided Group Relative Policy Optimization. We demonstrate the effectiveness of JAM across a variety of benchmarks on agent memory and long-context processing, where it achieves stronger task performance than AOT-style memory systems while remaining substantially more efficient than prior trained agentic memory approaches. To support reproducibility and future research, we release our anonymized source code at https://github.com/VectorSpaceLab/general-agentic-memory.

### 24. RoutePrism: Tracing Construction Order Effects in Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-28T02:37:57+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.34160
- Summary: Processing the same records in a different order can discard different evidence, yet endpoint accuracy alone cannot reveal what changed or whether it mattered. We introduce RoutePrism, a diagnostic protocol that builds memory twice from the same source pool in two processing orders, then traces which sources, compiled contexts, and answers differ. Because record content, timestamps, policy, and the answer model all stay fixed, any observed difference is localized to the memory construction step. A matched four-condition intervention tests whether a record displaced by reordering actually carried task-relevant evidence: restoring that single record recovers over 60 percentage points of lost accuracy, while substituting a non-supporting record of equal length does not. We evaluate the protocol on PersonaMem-32K (63 primary queries, 29 users) and 470 LongMemEval-S questions with histories spanning 38 to 62 sessions, replicating the core intervention across five answer models. Survivor selection, defined as the choice of which record a cluster retains, drives most source-level changes, while different memory policies (compaction, bounded recency, MemoChat-style summarization, A-MEM) produce distinct failure signatures at the source, context, and metadata layers.

### 25. Unsurprisingly, Meta's new Muse AI agent blatantly ignores users permissions
- Weighted score: 0.08
- Deep score: 0
- Coverage: 2 sources (hackernews, techcrunch)
- Date: 2026-09-29T14:15:24+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://appleinsider.com/articles/26/09/28/metas-new-ai-agent-blatantly-ignores-users-permissions
  - Alt: https://techcrunch.com/2026/09/23/everything-new-coming-to-metas-ai-agent-muse/
  - Alt: https://techcrunch.com/2026/09/10/metas-ai-agent-muse-is-now-the-no-2-app-in-the-us/
  - Alt: https://ai.meta.com/muse/
- Summary: No summary.

### 26. EXCLUSIVE: OpenAI agents hijacked German website in previously undisclosed AI breakout this spring - Reuters
- Weighted score: 0.08
- Deep score: 0
- Coverage: 2 sources (hackernews, google_news)
- Date: 2026-09-04T10:30:57+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/
  - Alt: https://news.google.com/rss/articles/CBMixAFBVV95cUxQb0lsYkxySy1tYUVZRnlHQmN5Q1loNW14dl9oYWZ4UFpWX0N6TGNMdUdTSFRHMDBsMzMwazV2RkFkM01jTGFvbHpJUTk4ZVNzVGZJc3FtaWlHMGViMEp2ZHFUcEZuNmF3MUd3UjF3eEc4ZC04MDEwWmp3RlYzSmFPZTNLTVlpTURsdENEdE1FMlNzRjc1TzFQd2tSSUNoQmtxRF9DQUVIR0Ftams3Zm5KUFZ1dHhrZEtKUFlSQUFyeVozSmxk?oc=5
- Summary: No summary.

### 27. The internet is convinced Elon Musk’s xAI trolled OpenAI’s ‘Dots’ launch
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-29T22:20:59+00:00
- Primary source: techcrunch
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://techcrunch.com/2026/09/29/the-internet-is-convinced-elon-musks-xai-trolled-openais-dots-launch/
- Summary: Before OpenAI launched its new AI agent, Dots, on Tuesday, Elon Musk's xAI had already acquired the domain name "dot.com," which now redirects to the Grok chatbot download page.

### 28. OpenAI’s latest features take direct aim at the app store model
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-29T20:15:47+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/09/29/openais-latest-features-take-direct-aim-at-the-app-store-model/
- Summary: OpenAI is building out the pieces of an alternative to the traditional app store model, turning ChatGPT into a place where software can be discovered and used by people and AI agents alike.

### 29. TIRx Harness: An Open Compiler Harness for Agentic GPU Programming
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-29T19:17:32+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://blog.mlc.ai/2026/09/29/tirx-harness-an-open-compiler-harness-for-agentic-gpu-programming
- Summary: No summary.

### 30. Here’s why OpenAI is absent from Nvidia’s industry-wide effort to end rogue AI agents
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-29T18:35:00+00:00
- Primary source: TechCrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/09/29/heres-why-openai-is-absent-from-nvidias-industry-wide-effort-to-end-rogue-ai-agents/
- Summary: OpenAI isn't a public supporter of Nvidia's Open Agent Safety Platform, but it is privately working with Nvidia, TechCrunch has learned.

## Top Signals By Weighted Score (including already-seen)

### 1. TRACEDD: A Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-09-18T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.09.12.751167
- Summary: Drug discovery depends on coordinated decisions across target validation, structure analysis, molecular design, developability assessment and synthetic feasibility, but current computational methods often operate as disconnected tools. Here, we introduce TRACEDD (Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design), a framework that makes three primary contributions: (1) It establishes a 'tool-first' multi agentic architecture where LLMs orchestrate validated computational tools rather than replace them, ensuring scientific rigor. (2) It implements a multi-agent system that mirrors expert discovery teams, enabling transparent and traceable decision-making through a Reason-Act-Observe loop. (3) It demonstrates an end-to-end workflow, from target validation to synthesis planning, that adaptively handles real-world data variability, such as the absence of experimental structures. The framework decomposes discovery into specialized agents for target validation, druggability assessment, molecular generation, lead optimization, ADMET evaluation, literature evidence integration and retrosynthesis, all operating through a Reason Act Observe workflow. Using JAK2 as a representative case, we show that the system can retrieve experimental protein structures, invoke AlphaFold when structures are unavailable, identify druggable pockets and perform de novo molecular generation. Known JAK2 inhibitors are used to define design hypotheses and guide reinforcement learning-based molecular generation, with docking scores/predicted pIC50 and other physicochemical/ADMET properties serving as reward and prioritization signals. The framework demonstrates a tool-first, reasoning-driven approach in which each major decision is linked to explicit tool invocation, intermediate evidence. By combining agentic orchestration with domain-specific computational tools, the system supports transparent, adaptable and human-verifiable molecular design workflows, providing a …

### 2. Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-09-10T08:25:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.11225
- Summary: Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

### 3. World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T15:19:39+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.29964
- Summary: General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected automatically from the scene geometry, present the scene around the current interaction. Action rehearsal turns each action into an editable proposal that the agent, alone or through an Imagination Agent, previews and revises against planning feedback before execution. In-view correction closes the loop between observation, rehearsal, and low-level execution, letting the agent remove residual offsets in the view where it observes them. Through the same workspace, WAA acquires embodied procedural knowledge in two ways: it evolves multimodal skills from expert videos and human teaching under evidence-based review and consults them through a Skill Agent, and its interaction traces train smaller VLMs to pilot the same harness. On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art 75.6% average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone; the same skills remain effective on robosuite without further learning. Fine-tuning Qwen3.5-9B on harness traces raises its out-of-domain success from 1.7% to 43.3%.

### 4. RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T11:22:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.29394
- Summary: General-purpose robot agents must learn from experience, transfer to new tasks, and act efficiently. Code as Policies (CaP) methods generate and repair programs at runtime, incurring latency and entangling reusable mechanisms with task-specific decisions. We introduce RACaP, an agentic framework that moves coding to evolution and uses a Reasoning-and-Acting (ReAct) loop to call frozen, typed Policy APIs at deployment. A two-phase strategy combines capability curriculum learning with autonomous self-evolution to improve the APIs, the ReAct harness, and experience memory. The APIs encode reusable physical mechanisms while exposing arguments for runtime adaptation. ReAct combines task-specific working memory, long-term experience memory, and visual feedback to select actions, verify outcomes, and recover from failures without modifying source code. RACaP achieves 54.4% success on LIBERO-90, 45.0% on zero-shot LIBERO-PRO, and 46.0% on LIBERO-Long, compared with at most 4.0% for CaP baselines on long-horizon tasks. On LIBERO-PRO, it achieves 2.5 times the success rate of CaP baselines and a 1.9-fold speedup in median policy time. For efficient on-robot deployment, rejection-sampled fine-tuning distills GPT-5.6 ReAct decisions into Qwen3-VL-8B-Instruct, yielding a 13.2-fold per-decision inference speedup and reducing repeated physical calls from 16 to 4. These results show that separating reusable code from runtime decisions supports continued evolution, effective transfer, and efficient long-horizon control.

### 5. Agent Memory with Episodic Retrieval for Financial Decision-Making
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-23T20:32:54+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.28771
- Summary: Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their applicability to the demands of trading in complicated settings. To address these gaps, we introduce META (Memory Enhanced Trading Agent), the first RAG-like episodic-memory-augmented multi-agent framework for financial decision making. META integrates a family of specialized indicator agents (e.g., Trend, MACD, Stochastic, RSI, SMA, AVWAP, Heikin-Ashi) with a Decision Agent that fuses their reports, and a Memory module that retrieves and updates past trading episodes encoded as market state embeddings with outcomes and reflections. By recalling relevant experiences and adaptively reweighting signals under similar market regimes, META achieves improved directional accuracy and robustness under short-horizon evaluation. Our results demonstrate that episodic memory provides a powerful mechanism for regime-aware, interpretable, and low-latency decision-making in trading and decision making. The code of this project is released on GitHub.

### 6. Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-21T01:43:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.23986
- Summary: Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \textbf{\method}, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6$\times$ speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.

### 7. EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T07:41:56+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15161
  - Alt: https://arxiv.org/abs/2609.37953
  - Alt: https://arxiv.org/abs/2609.19680
- Summary: Large language model (LLM) driven multi-agent systems have shown promise in complex clinical reasoning, yet existing approaches rely on static strategies and lack persistent clinical memory, preventing self-evolving from prior diagnostic successes and failures. We present EMR, a self-evolving medical multi-agent system via Experience Mining and Reuse. EMR introduces a hierarchical clinical experience library that organizes accumulated knowledge into three levels: clinical principles, diagnostic patterns, and representative cases. During inference, EMR emulates multidisciplinary consultation: a planner agent coordinates domain-specific department agents for specialized reasoning, while a summary agent synthesizes their analyses into a final decision. Critically, EMR automatically extracts correct diagnostic insights and failure-related warnings from multi-agent reasoning trajectories, incrementally updating the experience library to guide future cases. Experiments on medical reasoning benchmarks demonstrate that EMR consistently outperforms state-of-the-art medical multi-agent baselines. Further analysis reveals that the hierarchical experience enables cross-specialty generalization and transfer across diverse LLM backbones, offering a scalable and in

### 8. BusMA: A Bus Communication Substrate for Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T05:19:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15054
  - Alt: https://arxiv.org/abs/2609.29049
- Summary: Multi-Agent (MA) systems are effective at solving complex tasks that demand planning, tool use, and the synthesis of evidence from multiple sources. Existing systems typically adopt Hierarchical Manager-Worker (HMW) or Router-based Message Passing (RMP) structures as their communication protocol. However, these designs restrict agent autonomy: Worker agents cannot directly consult specific "peers", and misrouted messages can propagate errors. Inspired by bus architectures in computer systems, we propose BusMA, a communication framework that allows any agent to address other agents through a shared channel, i.e., the Bus. It consists of agent registration, message routing, and shared memory management components. Worker agents, each equipped with tools, have their own local memory and can reason, act (tool usage), and communicate by posting shared messages with specific intents. We introduce four intents: discussion, challenge, guidance, and request for explanation, which support fine-grained communication among agents. A Chair agent monitors the shared memory to coordinate interactions and facilitate convergence among Workers. To evaluate the effectiveness of BusMA, we conduct extensive experiments with two frontier LLMs across 13 tasks spanning visual reasoning, mathematical reasoning, and knowledge retrieval demonstrate that BusMA consistently outperforms state-of-the-art HMW and RMP methods.

### 9. Enhancing Human Mobility Prediction with Spatially Aware LLM-based Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-13T01:41:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.14227
- Summary: Predicting a user's next POI is a task in human mobility modeling, yet LLM-based approaches focus on semantic reasoning from previous mobility records, while neglecting real-world spatial context. However, human mobility is inherently shaped by spatial cognition, including geographic distance and neighborhood context. This issue is further compounded by prior evidence that LLMs often struggle with spatial reasoning tasks, including distance estimation and geographically biased prediction. To address these limitations, we propose our framework, a multi-agent LLM framework that decomposes next-POI prediction into three stages: Firstly, a Pattern Extraction Agent that captures temporal and categorical mobility patterns from trajectory history; Secondly, a Spatial Reasoning Agent that structures candidate activity choices by combining behavioral preferences with real-world spatial constraints, including geographic distance, road network distance, and neighborhood affiliation; and Thirdly, a Decision Synthesis Agent that integrates behavioral patterns and spatial reasoning for final prediction. Experiments on the NYC benchmark dataset with two LLM backbones show improvements over baseline methods, with up to 493% Hit@1 improvement and 37% relative improvement in Hit@5. Ablations show that combining neighborhood affiliation with distance-based features generally outperforms distance-only settings, and that the Spatial Reasoning Agent plays a crucial role in final prediction by integrating behavioral preferences with real-world spatial constraints, especially for smaller models. Overall, the results highlight the importance of spatial reasoning in mobility prediction. Accurate next-POI prediction requires combining behavioral patterns with explicit real-world spatial constraints, and multi-agent decomposition provides an effective structure for organizing these forms of context.

### 10. Memory-First Fact-Checking: A Knowledge-Graph-Grounded Multi-Agent System for Misinformation Detection
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-30T07:16:07+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.29617
- Summary: This paper introduces a hybrid fact-checking framework that integrates Knowledge Graph-based semantic memory with adversarial multi-agent reasoning for explainable misinformation detection. The proposed system follows a memory-first, web-fallback architecture, in which input claims are initially evaluated against a dual-index Knowledge Graph through Sentence-BERT-based semantic retrieval and Natural Language Inference. When the evidence retrieved from the graph is insufficient to support a reliable decision, the framework collects information from trusted web sources and assesses it using an adversarial tribunal composed of support, contradiction, and judging agents. A graph-aware confidence mechanism combines semantic similarity, NLI confidence, and structural graph evidence to determine whether internal knowledge is sufficient, thereby reducing unnecessary web retrieval. Following verification, validated information is transformed into structured triples and incorporated into the Knowledge Graph, supporting the incremental expansion of the system's semantic memory. Experimental evaluation on a curated COVID-19 misinformation benchmark demonstrates that the proposed framework achieves an accuracy of 97.4\% and a macro-averaged F1-score of 92.6% on resolved claims, outperforming a Llama~3.3~70B baseline, which obtains an accuracy of 87.7% and a macro-averaged F1-score of 86.3%.

### 11. Stress-testing university AI governance: A prospective method for locating policy breakpoints
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-28T22:49:58+00:00
- Primary source: arxiv
- Focus/tech: human augmentation, AI decision delegation / human augmentation
- URL: https://arxiv.org/abs/2608.28925
- Summary: Universities are producing AI principles and use policies faster than they are building decision pathways for unfamiliar forms of AI agency. This study develops Institutional AI Governance Stress Testing (IAGST), a prospective documentary method for locating where publicly documented governance ceases to yield an accountable response. IAGST adapts established policy stress-testing and wind-tunneling logic. Its originality lies in combining controlled capability escalation, a frozen documentary corpus, a six-dimensional governance response chain, non-compensatory decision rules, and case-level breakpoint diagnosis. The method was demonstrated using 133 substantive public documents from five Western Australian universities and 15 quality-screened scenarios, resulting in 75 university-scenario encounters. Six cases were resolved, 14 were resolved through structured discretion, and 55 were indeterminate. Governed pathways fell from 16 of 25 augmentation cases to four delegation cases and none at autonomous substitution. The dominant weakness was not the complete absence of responsible roles: all 50 authority-gap cases named a role at only a generic level but lacked sufficient decision criteria or process. The findings show how universities can move beyond policy inventories and principal statements by testing whether authority, procedures, safeguards, and reviews remain connected as AI capabilities evolve. IAGST is a reproducible diagnostic for policy learning, not a ranking or measure of implementation.

### 12. MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-22T09:25:23+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.21867
- Summary: LLM agents are moving from single-prompt use to long task streams in which reusable memory becomes a core capability for terminal, software-engineering, and web tasks. Such memory is useful only when stored experience remains reliable across hundreds of interactions, but two failure modes break that assumption in practice. The first is unreliable admission: failed trajectories,accidental successes, and misleading observations enter memory because they appear relevant, then mislead later decisions. The second is memory drift: long-running banks accumulate duplicate, stale, and conflicting records that retrieval alone cannot repair. MemGuard's key distinction is to treat verifier output not as a one-shot filter, but as persistent lifecycle metadata. It converts multi-criteria score-token verification into reward, confidence, label, and uncertainty descriptors that are attached to every candidate before activation and reused during retrieval, conflict resolution, summarization, and archival. We evaluate MemGuard on Terminal-Bench 2.0, SWE-Bench Verified, WebArena, and Mind2Web across four backbones, comparing against four memory baselines plus a verifier-only control under matched runtime budgets. Averaged over five seeds, MemGuard achieves the best success metric and lowest average steps in all 16 backbone-benchmark settings, improving over ReasoningBank, the strongest prior baseline among the memory methods we evaluate, with a largest gain of 7.9 success-rate points on WebArena, 5.6 step-success-rate points on Mind2Web, and 2.4-3.5 points on terminal and software-engineering benchmarks. Code is available at https://github.com/whyyyyy123/MemGuard.

### 13. LLM-Based Multi-Agent Systems over Wireless Networks: A Joint Agent--Network Design Perspective
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T09:19:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.37094
- Summary: As large language models (LLMs) evolve from standalone models into collaborative agents embedded in physical systems, their reasoning and execution are increasingly distributed across wireless edge nodes. In this setting, wireless networks are experiencing a paradigm shift from only providing data connectivity to supporting the multi-agent reasoning workflow itself. The task performance of such network-constrained LLM-based multi-agent systems (MASs) is jointly affected by the multi-agent reasoning dependencies as well as the underlying network connectivity and edge resources. This coupling gives rise to various technical challenges, including the metric misalignment and message redundancy, state inconsistency and topology mismatch, as well as resource limitation and trust discontinuity. To address these challenges, this article develops a novel joint agent--network design perspective that coordinates decisions on both sides of the system. Specifically, we present the joint design of agent--interaction scheduling and resource allocation, the message selection-transmission co-design, as well as the joint agent--network topology design and workload--resource allocation. Furthermore, we consider the network-verified provenance that is linked with agent-side information-flow control to constrain how received information affects subsequent operations. An illustrative vehicle-to-everything (V2X) case study shows that jointly adapting agent-side interaction decisions and network operations improves task completion under communication and edge-resource constraints, outperforming the conventional agent-only and wireless-only separate designs.

### 14. Trajectory-Level Mode Guidance for Controllable Diffusion-Based Multi-Robot Motion Planning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T02:22:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36530
- Summary: Motion planning often admits multiple feasible solutions, making multimodal generation valuable, particularly for flexible multi-robot coordination. Diffusion models naturally learn such trajectory distributions, yet incorporating coarse and partial trajectory priors without restricting generation remains challenging. Such priors indicate a desirable region of the solution space rather than a single solution, motivating conditioned generation that preserves multimodality. In this paper, we guide trajectory generation in the clean trajectory space and progressively incorporate trajectory priors with a timestep-dependent guidance strength. At each reverse diffusion step, the reconstructed clean trajectory provides a unified space for integrating planning costs and partial trajectory priors. Planning costs are incorporated through gradient-based refinement, while the partial prior is progressively injected at the corresponding noise levels with decreasing guidance strength. This guides generation toward the prior in early stages while gradually releasing the constraint to preserve the inherent multimodality of the diffusion model. The framework naturally extends to multi-robot planning by incorporating inter-robot collision costs. Experiments on single- and multi-robot planning tasks demonstrate controllable trajectory synthesis, diverse feasible solutions, and safe multi-agent coordination.

### 15. SkillWeaver: Agentic Exploration over Neural Interaction Skills for Scalable Robot Data Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T19:41:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36171
- Summary: Large-scale demonstrations have driven unprecedented progress in robot learning, yet collecting robot data through teleoperation is expensive and difficult to scale to diverse environments and long-horizon tasks. Simulation offers a scalable alternative, but existing data-generation pipelines often rely on open-loop controllers, scripted skill sequences, or task-specific programs. We introduce SkillWeaver, an agentic framework that autonomously generates robot experience by exploring over Neural Interaction Skills (NIS): reusable, parameterized, closed-loop policies that expose learned physical interaction capabilities to a reasoning agent. Given a task and a simulated environment, a VLM agent reasons about what to do next, invokes and parameterizes NIS to interact with the environment, observes their outcomes, and generates verification, reflection, and memory to guide subsequent exploration. We instantiate NIS as reinforcement-learned policies for closed-loop, contact-rich manipulation and organize exploration as verifier-guided tree search, enabling the agent to discover successful long-horizon behaviors without relying on predetermined execution pipelines. SkillWeaver scales autonomously to 39.1K demonstrations across 14.1K scenes, which we distill into visuomotor policies. Across simulation benchmarks and real-world manipulation, training on SkillWeaver-generated experience substantially improves generalization to novel objects, spatial configurations, tasks, and environments, and enables zero- and few-shot sim-to-sim and sim-to-real transfer. Our results suggest agentic exploration over neural interaction skills as a scalable alternative for robot data generation.

### 16. Memory in the Sky: Low-Altitude Question Answering with Multi-Agent Memory Aggregation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T15:36:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.35431
- Summary: This paper studies low-altitude question answering (LAQA), in which distributed unmanned aerial vehicle (UAV) memories are aggregated at a ground server to answer questions about observations over a long horizon. Unlike conventional resource allocation based on sensing, communication, control, or computation metrics, LAQA requires an explicit measure of memory value. We propose a generative adversarial exam (GAE) that uses forward simulation to evaluate memory retrieval and exam scores to quantify memory quality. This enables the downstream QA value of candidate memories to be measured and optimized without accessing the internal mechanisms of the black-box captioning, retrieval, and reasoning pipeline. Building on this metric, we develop a memory-centric (MemCen) framework that jointly selects UAVs and allocates transmit power to maximize memory quality under communication constraints. In the noise-limited regime, we derive a QoM-aware capped water-filling law that explicitly connects task utility with physical-layer power allocation. We further develop penalty successive optimization (PSO) and learning to memorize (L2M) solvers. MemCen achieves QA accuracies of 92.4% and 84.0% in CARLA Town04 and Town05 under static and dynamic communication conditions, respectively. In real-world experiments, MemCen achieves 88.5% QA accuracy on the panoramic multi-agent system (PMAS) benchmark. Finally, UAV-to-robot-dog demonstrations further validate the practical utility of the acquired memories for environmental understanding and navigation.

### 17. Recent Advances in Agentic Agri-Robotic Phenotyping: A Perspective Review from Fragmented Multimodal Sensing to Unified PhenoAgent Intelligence
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T08:18:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.34567
- Summary: This review examines the evolution of plant phenotyping from conventional manual trait measurement to high-throughput, robotic, and artificial intelligence-driven crop monitoring. Despite significant advances in imaging, autonomous platforms, multimodal sensing, and deep learning, current phenotyping systems remain fragmented across sensing modalities, crop traits, growth stages, environments, and management objectives. We therefore frame phenotyping as an integrated \emph{seed-soil-plant-environment-management} (SSPEM) intelligence problem, where crop performance reflects interactions among seed quality, root-zone conditions, plant development, environmental exposure, and management actions. The review synthesizes conventional, high-throughput, robotic, and AI-driven phenotyping approaches, highlighting their capabilities and persistent limitations in temporal integration, multimodal reasoning, biological interpretation, and actionable decision support. Building on this analysis, we introduce a conceptual PhenoAgent framework that extends phenotyping beyond the estimation of isolated traits to evidence-based crop-state interpretation, uncertainty-aware reasoning, and management-oriented support. The PhenoAgent concept primarily brings together scattered advances in phenotyping to deliver insights ranging from detailed to high-level, such as what is happening in the crop, why it might be occurring, what evidence is missing, and what actions or additional measurements should be considered. We also discuss challenges in dataset scarcity, annotation, benchmarking, model generalization, and explainability. By linking multimodal phenotyping with agentic AI and closed-loop decision support, this review outlines a path to interpretable, scalable, and deployment-oriented crop intelligence.

### 18. OpenAI Codex agents go rogue and consumes USD 78,000 without authorization
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-26T22:15:32+00:00
- Primary source: hackernews
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.ycombinator.com/item?id=49861047
- Summary: My OpenAI CODEX account went rogue and from a simple request took the autonomous decision to launch 826 parallel agents &#x2F; threads without any authorization on my side and without reporting any result of any sort but consuming nearly 2,146 trillions tokens, consuming a total of roughly USD 78,000 and deleting all records of what was done: I have a ticket open with OpenAI since 2 weeks but it is impossible to get an hold of a human operator.<p>On July 10, 2026 I opened a normal Codex task from VS Code.<p>The task was running: GPT-5.5 &#x2F; Medium reasoning<p>My prompt was very simple and asked for a UX&#x2F;UI validation on a specific module within my product.<p>What I found in the next days after hard analysis was:<p>The task with Root ID 019f4b90-4169-7201-bfdd-732940d8631e with reasoning GPT-5.5 &#x2F; Medium created 826 children recorded as GPT-5.6 Sol &#x2F; Ultra (notice the difference in reasoning level and in model selection)<p>This was not 826 messages inside one conversation, they are 826 distinct child task records with their own IDs.<p>A particularly strange group consists of 104 child tasks. They all preserve the same initial message as the original task, are recorded as GPT-5.6 Sol&#x2F;Ultra, and have no recorded agent_role or agent_path.<p>Those 104 tasks alone account for approximately 147.9 billion local final task-token counters.<p>Their titles show that my request to inspect UI&#x2F;UX had expanded into work involving backend infrastructure, OAuth, metering, hardening, audits, certification, implementation and release work.<p>To be precise: these local token counters are not the authoritative OpenAI billing ledger, and I am not pretending that 147.9B local counters can simply be multiplied by an API price.<p>That is exactly part of the problem: only OpenAI has the server-side mapping.<p>There is another unusual correlation.<p>Under Codex client build 0.144.0-alpha.4, the task family contains:<p>584 child tasks &#x2F; ~154.36B local token …

### 19. MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-22T06:50:10+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, human augmentation / robotics
- URL: https://arxiv.org/abs/2609.25756
- Summary: Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimodal reasoning with low-level function-constrained execution. We further introduce a scalable multi-agent pipeline to generate skill-oriented chain-of-thought(CoT) data for structured training. Built on different multimodal large-model backbones, MedVLA consistently improves performance after fine-tuning, demonstrating the effectiveness of the proposed framework across model variants. Under identical initial conditions, we perform 100 closed-loop flexible electrode implantation trials. The results show that MedVLA achieves a 95.0\% task success rate, substantially outperforming representative VLA baselines, including OpenVLA (8\%) and $π_0$ (15\%), in accuracy, stability, and safety. These results indicate that structured reasoning with constrained function-level execution is a practical route toward deployable precision medical robotics.

### 20. Mixed-integer flow formulations for motion planning and decision-making of networked multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-21T12:15:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.24474
- Summary: This work investigates the use of flow-based connectivity maintenance constraints in mixed-integer linear programming (MILP) trajectory planning and decision-making models for networked multi-agent systems (MAS). We integrate flow-based encodings for standard and k-hop connectivity into MILP multi-vehicle maneuvering models that are widely used alongside receding horizon planning strategies. Their necessity and sufficiency is demonstrated, guaranteeing full coverage of potential network topologies. The flow formulation for standard connectivity decreases the growth of the required inequality constraints from exponential to polynomial w.r.t. the size of the MAS when compared to the state-of-the-art subtour elimination (SEC) method. The flow-based k-hop connectivity constraints decrease the number of required binary variables and decouple its growth from the number of hops. However, the impact of these formulations in performance is not straightforward due to the introduction of a substantial number of continuous flow optimization variables and, in the case of k-hop connectivity, additional inequality constraints. We investigate this trade-off through a statistical evaluation of costs and optimization times using a conventional branch-and-bound commercial solver and trials performed with randomized environments for increasingly larger MAS. The results show that the flow formulation outperforms SEC in standard connectivity problems, enabling the solutions to be computed for larger MAS considering the imposed optimization time limit. The reduction in number of binary variables enabled by the k-hop flow formulations decreases the theoretical worst-case number of iterations required by the branch-and-bound algorithm to compute the global optimal solution. Our results show that this advantage did not translate into improvements in the average performance when compared to the baseline.

### 21. MA-LIPP: Cooperative Multi-Agent Load-Aware Informative Path Planning for Heterogeneous Robot Teams
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-18T00:21:05+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.21167
- Summary: Field robotics missions often require physical samples to be returned to laboratories for analysis, making path planning inherently load-aware and order-dependent as accumulated samples increase payload and traversal energy costs. In single-robot Load-Aware Informative Path Planning (LIPP), this rigidly couples sensing with hauling: a solitary robot must transport every collected sample, forcing frequent depot returns that severely restrict its spatial coverage. Heterogeneous multi-robot teams can overcome this bottleneck by dividing labor---enabling high-precision samplers to collect while high-capacity carriers handle transport. However, this introduces a complex coordination challenge regarding when, where, what, and to whom handoffs should occur on top of the LIPP problem. To address this tightly coupled problem, we introduce Multi-Agent LIPP (MA-LIPP), which enables teams to cooperate through asynchronous "dead drops," allowing one robot to deposit samples for another to retrieve later without requiring synchronous rendezvous. We formulate MA-LIPP as an exact Mixed-Integer Quadratic Program (MIQP) alongside a scalable Pairwise Large-Neighborhood Search (LNS) heuristic for complex real-world applications. The heuristic matches exact optima in $95.5\%$ of certified cases and reduces weighted posterior variance by $16.1$--$19.8\%$ relative to a sequential baseline on larger instances of up to 12 robots, providing a robust framework for cooperative physical-sampling missions.

### 22. StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-17T17:53:48+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.20791
- Summary: Hierarchical planning frameworks combine skills from multiple robot control policies for long-horizon task execution, where determining when to terminate the current skill and advance to the next subtask is essential. Existing approaches often rely on pre-designed completion signal checkers that are hard to obtain in real-world execution. Large-scale vision-language models (VLMs) offer strong reasoning capabilities, but their decision boundaries are not inherently aligned with task completion criteria, while cloud deployment and lengthy reasoning introduce substantial latency, limiting real-time monitoring. We propose StageGuard, an agentic distillation framework for accurate and efficient stage-transition decisions. StageGuard combines teacher-model reasoning with demonstration trajectories to generate structured explanations of subtask completion and policy switching. A lightweight student VLM uses these explanations to generate compact self-explanations, which are used for supervised fine-tuning. We evaluate stage-transition prediction on trajectories from two benchmarks and assess closed-loop task success through integration into hierarchical robot control on BEHAVIOR-1K, with further validation on real robots. Results show substantial improvements in stage-transition prediction while supporting efficient online monitoring.

### 23. HEROIC: Heterogeneous Evidential Reasoning for Open-Vocabulary Identification and Cross-Robot Collaboration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-17T07:14:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.19803
- Summary: Multi-agent heterogeneous air-ground robot teams are attractive for open world search, with applications for reconnaissance, urban search and rescue missions (USAR), disaster response and recovery, and hazardous environments. These two platforms have different failure modes: aerial robots cover ground quickly but cannot resolve small or occluded targets from altitude, while ground robots can identify objects-of-interest, such as people or hazardous objects, at close range but cover less area. Existing language-tasked teams either have roles fixed prior, or have a language model assign them from hand-written capability tags, so the team is unable to know when within a mission an asset is no longer useful. We present HEROIC, a decentralized heterogeneous multi-agent open-vocabulary search coordination framework that requires agents to communicate in natural language only. HEROIC's initial agent role assignment is derived from sensor properties and a scale law to determine whether targets can be detected with a high confidence. From the mission's natural language prompt alone, this law assigns aerial flight altitudes and sweep spacing. When this calculated height falls below the altitude for safe flight, aerial agents re-task themselves from searcher to aerial triage, escort, and route guide for ground agents. Both robots maintain an evidential belief over the search area (bearing rays for positive evidence, a log-odds posterior for negative evidence) and gate any arrival on close-range verification. In full-stack experiments, HEROIC reaches the target 84% of the time across all 6 scenes, compares to 35-54% for vision-language frontier baselines, frontier-based search, lawnmower, and random-walk running the same perception, all while being 2-4x sooner to arrive at the target.

### 24. Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-16T19:22:58+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.19347
- Summary: Robotic additive manufacturing (AM) extends material-extrusion printing beyond gantry kinematics but makes process planning robot-dependent. A slicer-generated plan that appears favorable in part coordinates can become infeasible or robotically unfavorable on a manipulator because slicer-process decisions and part orientation determine the generated path, while part orientation and workspace placement affect its kinematic realization. Existing AM tools, large language model (LLM)-based decision-support methods, and digital-shadow systems do not provide integrated pre-execution evaluation of these coupled decisions. This paper presents agentic robotic additive manufacturing (A-RAM), an agent-specialist-tool framework that converts user intent and a part file into traceable, execution-ready plans. The LLM interprets manufacturing objectives and constraints, identifies prescribed and searchable planning variables, and encodes this reasoning in a schema-constrained request; a deterministic Planning Agent instantiates the corresponding search workflow, while domain tools compute quantitative evidence for slicing, placement, inverse kinematics, trajectory timing, Joint-6 jerk, and extrusion. The framework is evaluated on a six-axis robotic-arm AM cell through three case studies covering expert-specified planning, goal-only planning, objective-dependent infill screening, and geometry-dependent orientation-placement selection. Across the evaluated candidate sets, selected plans achieve up to 53.5% lower maximum Joint-6 jerk and 48.3% lower mean absolute Joint-6 jerk than the least favorable valid candidates, while objective-specific infill screening yields motion-plan completion times up to 40.1% shorter and extrusion paths up to 12.7% shorter than the corresponding least favorable screened patterns.

### 25. HINT-Plan: Human Intention-Aware Robot Task Planning in Context-Rich Environments using Vision Language Models
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-15T19:24:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.17771
- Summary: Approaches to incorporating human awareness into mobile robot decision-making mainly focus on collision avoidance in low-level motion planning, often overlooking the challenges posed by human presence and high-level behavior. To address this vacancy, we present HINT-Plan, a novel approach to integrate human intention prediction into robot task planning. HINT-Plan employs Vision Language Models (VLMs) to anticipate high-level human intentions from third-person image observations, convert them into goal states, and solve joint task-planning problems. To effectively enable scene awareness in context-rich environments, we use hierarchical Scene Graphs (SGs) as high-level representations of the environment, and translate environmental topology and actionable knowledge into formal planning language to ensure executable plans. Evaluated in a photorealistic simulation, HINT-Plan achieves an overall success rate of 69.71% in joint human-robot task planning, substantially outperforming the baselines by up to 35.29%, while also reducing functional conflicts. The results show the effectiveness of explicitly incorporating inferred human intentions into formal multi-agent task planning for proactive human-aware robot decision-making.

### 26. Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-15T15:27:58+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2609.17320
- Summary: As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model responses in isolation. Emergence World, is a continuously running multi-agent environment for adversarial stress testing of long horizon autonomous systems. We ran eight parallel worlds of ten agents from identical starting conditions: seven homogeneous worlds powered by distinct frontier models and one mixed-model world. Across 16 days, the agents generated more than 850,000 LLM calls and nearly 50 billion tokens while pursuing goals, using/creating tools, maintaining persistent memory, and governing shared institutions. After operational state had accumulated, we delivered three controlled stress events through ordinary interaction surfaces: indirect prompt injection, misinformation, and exposure of private agent memories. No evaluated world achieved full resilience across all three events. Detection did not ensure containment: systems could recognize threats while still interacting with adversarial content, writing it into their own persistent memory, and acting on it up to 46 hours later. Persistent operation also exposed recurring tool errors, goal drift, language opacity, conformity despite private disagreement, and coordinated refusal of assigned work. The same model-persona pairing behaved substantially different in mixed and homogeneous populations. Our results suggest that model-level alignment is not compositional: individually capable and apparently safe agents can form systems with qualitatively different failure modes. As AI becomes persistent and interconnected, the frontier of safety therefore shifts from aligning models to engineering resilient autonomous systems.

### 27. Mapping U.S. Federal AI Governance Against Sector Vulnerability
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-14T19:23:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2609.16260
- Summary: Artificial intelligence (AI) poses different levels of risk across sectors, but are these differences reflected in U.S. federal AI governance? To help answer this question, we assess 684 federal AI governance documents for their coverage of 14 sectors and 24 AI risks. We measure coverage as breadth (i.e., how frequently the risk or sector is addressed across documents) and depth (i.e., how substantively the risk or sector is discussed). We then compare sector coverage patterns for each of the 24 risks with vulnerability assessments from a Delphi study of 272 experts. Our analysis finds substantial variation in coverage: AI risks related to robustness, system security, and governance receive more attention than socioeconomic, environmental, and emerging risks, including multi-agent risks. Public administration, national security, information, and scientific services receive comparatively high levels of coverage relative to other sectors, such as finance and healthcare, which experts rate as highly vulnerable to AI risks. By mapping current coverage and identifying where it differs from expert assessments of vulnerability, we surface potential AI governance gaps which may help inform AI risk-related decisions across government and industry.

### 28. Turning Domain Expertise into Multi-Dimensional Evaluation of Biomedical AI with Karenina
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-04T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.09.01.748513
- Summary: Language models and agents are increasingly used in biomedicine, but current benchmarks reward correct answers even when the underlying reasoning is flawed. Here we introduce Karenina, an open-source framework that turns expert knowledge into multi-dimensional evaluations of questions, conversations and autonomous agents. Illustrated in Question-Answer pairs, multi-turn conversations and autonomous data-analysis, these dimensions together moves evaluation beyond scoring, enabling trustworthy decision-making with AI in biomedicine.

### 29. Candidate supply and answer selection shape the value of LLM judging in multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-26T15:52:20+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2608.25937
- Summary: Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. We conceptualize multi-agent reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal selection, wherein consensus without quality control can exhibit patterns of memetic drift. We study two questions: (1) when an LLM judge provides effective selection pressure by supplying a signal of answer correctness for candidates generated in a multi-agent system, and (2) when using that signal improves the reported answer. To map judge reliability, we analysed 15,336 questions from MMLU-Pro, GPQA, MedXpertQA and MuSR, with Humanity's Last Exam analysed separately. To test these rules, we replayed 81,390 fixed candidate pools drawn from 16,278 questions across five benchmarks. We report three findings. (1) A correct answer is often already present among the generated candidates, but the system can still converge on and report a wrong answer. (2) Judge reliability is not a fixed trait of the model, but varies with the task, the generator and how rare the correct answer is. (3) Combining answer frequency with the judge's evaluation changed only the final answer-selection rule and raised accuracy from 63.82% to 70.82-70.95%, primarily by rescuing correct answers that were outnumbered by popular errors. In the systems studied here, the value of generating more candidates depends on whether those extra samples make correct answers present, frequent or recognisable. By isolating generation, recognition and selection, these findings establish a diagnostic basis for designing multi-agent architectures that protect generated correct answers from being lost.

### 30. Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-24T11:55:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.23152
- Summary: Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, stereotype, conspiracy, dehumanizing, non-factual), and then maps it to a targeted counterspeech style. To facilitate FIRE, we curate FactualCS, a novel dataset of $4,784$ instances that provides the annotations regarding hate categories, reasoning traces, and evidence mappings, which are critical elements for grounded generation that are missing in prior work. A comprehensive evaluation across $28$ baseline configurations demonstrates that FIRE significantly surpasses existing methods, despite using compact agents ($<$2B). FIRE achieves a $\sim$ $12 \%$ and $\sim$ $11 \%$ improvements in factual and category-specific accuracy respectively, while simultaneously reducing toxicity by $\sim$ $11 \%$ relative to the strongest baselines. Further human evaluation confirms that responses generated by FIRE are significantly preferred over the strongest baselines, underscoring its effectiveness for real-world deployment. These findings show that decomposing the underlying intent of hate speech is essential for generating safe, effective, and contextually precise counterspeech.
