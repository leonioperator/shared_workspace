# Blindspot Signals Report - 2026-11-17

- Source export: `/opt/apps/haier/exports/evolution_signals_20261117_020421.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 600
- Deduped/weighted signal clusters: 570
- Novel vs previous reports: 22
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. Evaluating Language Models as Orchestrators in a Tool-First Biomedical Discovery Platform
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-16T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.13.766436
- Summary: Large language models (LLMs) increasingly orchestrate agentic biomedical discovery systems, but cloud deployment raises concerns about inference cost, data privacy, and governance. Small language models (SLMs) that run on-premises are an alternative, provided they orchestrate scientific tools about as well as larger models. We built a tool-first, multi-agent system for scientific discovery in which an orchestrator coordinates six specialized tool systems: differential expression, literature retrieval, pathway enrichment, network-based gene prioritization and knowledge-graph analysis, perturbation signature matching, and structural/druggability assessment. In a tool-first design, specialized tools supply the domain knowledge and computation, so the model's main task is coordination, e.g. choosing tools, passing the right parameters, calling them in the right order, and carrying results across turns. With the tools, prompts, workflow, and benchmark held constant, we compared three orchestrators, Gemma 4 (26B, open-weight and locally deployable), Gemini 2.5 Flash, and Claude Sonnet 5. Evaluation used a custom benchmark of 104 single-turn and multi-turn tests, an LLM-as-judge protocol (groundedness and evidence validity), tool-use accuracy and efficiency metrics, and blind expert review. On single-turn tasks, the three models performed comparably, and reviewers did not rate the SLM below the larger models. In multi-turn tasks, Claude Sonnet 5 showed marginally higher evidence validity, Gemma 4 was weakest when parameters had to be assembled across turns, and all three models struggled with tool ordering on memory-dependent tasks. These differences were illustrated with case studies. Finally, we propose strategies to help SLMs address the multi-turn limitations and support cost- and privacy-aware deployment.

### 2. From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-13T17:59:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2611.18484
- Summary: AI-enabled remote patient monitoring is evolving beyond passive data collection toward agentic AI systems that interpret patient states, coordinate care, and initiate action across domestic and clinical settings. This structured scoping review finds that mature agentic care has not yet emerged: Most systems remain human led, while stronger decision-action coupling and embodied AI remain largely confined to prototypes and pilots. Healthcare robotics makes the transition from monitoring to action especially visible by translating AI-generated recommendations and decisions into speech, movement, prompting, physical assistance, escalation, and care coordination, making embodiment, clinical integration, human oversight, and governance fundamental design requirements. Further progress requires safe and interoperable care architectures in which intelligent components operate through clinically validated and accountable workflows. We propose agentic robotics as a future direction for supervised systems embedded in the care ecosystem, connecting AI agents and robots with clinicians, caregivers, and patients through auditable workflows that can be interrupted and remain subject to human oversight and explicit AI governance.

### 3. Envisioning Agentic Robotics: A New Era of Robotic Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-13T16:07:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.18359
- Summary: The release of GPT-6 Astra marks the emergence of a new paradigm in robotics: agentic robotics. Within weeks, frontier models with agentic harnesses matched or exceeded task-specific policies on many embodied benchmarks. Instead of training a dedicated policy for each family of tasks, an agentic robotic system applies a foundation model to open-world embodied tasks. It operates in a closed loop: observing the environment, interpreting user intent, reasoning about the task, invoking skills and tools, verifying outcomes, and adapting its strategy. Despite these advances, the community has yet to converge on a shared definition, a reliable evaluation framework, or a research roadmap. We argue that Embodied System 2, realized by a foundation model together with an embodied harness, forms the decision-making core of agentic robotics. Its central challenge is to translate general-purpose reasoning into effective and verifiable actions under physical constraints such as limited reaction time, mechanical limits, unpredictable environment changes, and irreversible consequences. Motivated by this perspective, we propose an evaluation framework that measures both model capabilities and closed-loop system performance. Furthermore, we identify the principles that carry over from digital to physical agents and the challenges that must be addressed to achieve reliable physical autonomy. On top of the Embodied System 2 and the evaluation framework, we envision a research roadmap toward sustained autonomy: the ability to perform work safely and reliably with progressively broader responsibility, from executing individual primitives to fulfilling standing roles.

### 4. AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-13T06:06:36+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.17790
- Summary: Recursive self-improvement (RSI) is one of the most promising paths toward an AI singularity for superintelligence. Achieving this vision requires AI systems to undertake the full training pipeline for iterative improvement. Reinforcement learning (RL) plays an essential role in this cycle to improve model capabilities and generalization, yet automating RL remains difficult due to unstable training dynamics and the need for sustained supervision. We introduce AutoRL, a multi-agent system for automating RL training, as a cornerstone for future RSI. Different from conducting research by end-to-end complete experiments, AutoRL monitors the evolving training state and integrates process-level supervision and research into an ongoing RL training, following the practical workflow of an RL researcher. Specifically, AutoRL consists of three RL-specific agentic roles. Perceptors track training dynamics, rollouts, evaluation, and efficiency, triggering deliberation when they detect anomalies, degradation, or stagnation. Three complementary Proposers diagnose problems and refine candidate interventions through shared evidence and checks. The Orchestrator reviews their recommendation and applies approved changes through online hot updates or checkpoint-based resumption. Experiments on Qwen3 and LongCat-Flash-Lite demonstrate the superiority of AutoRL over static RL recipes and a general agent. The research records show that existing agents can handle unattended RL supervision and dynamic adjustment. The difficulty for future RSI lies in developing fundamental methods that are valuable for resource-consuming validation.

### 5. google research / paper orchestra
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-17T02:01:54.840514+00:00
- Primary source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/google-research/paper-orchestra
- Summary: PaperOrchestra is a multi-agent framework for automated AI research paper writing.

### 6. Designing a Multi-Agent Architecture Guided by Advanced Type Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-16T18:03:52+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://leastsquared.substack.com/p/designing-a-multi-agent-architecture
- Summary: No summary.

### 7. Jay Ramnundlall: Why Human Accountability Must Remain At The Centre Of AI Governance - CIO Africa
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-16T09:56:53+00:00
- Primary source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMiqAFBVV95cUxObkdad3dSZ1NTZXhlRlRTaEtqQU4zLUhKR2VOVWRTa0dJemtNN2tKdUhTOE5oZXJaTmh2elhoNV9Ob3E3aks0Y2RtR29XX2lVQWNWWHdFU2otYjQyQ1Fad2kzX1JvUHc3bk1HNUFIMm4wWkVPOTBCZHdZQzdaOVpITGh2aWJoQ3NJdXBYR0o1N0M3VGh5MmthVWZNbEI1OTNGa2FUSFpKV3o?oc=5
- Summary: Jay Ramnundlall: Why Human Accountability Must Remain At The Centre Of AI Governance&nbsp;&nbsp;CIO Africa

### 8. Ego2Sim2Humanoid: Agentic Real-to-Sim for Learning Loco-Manipulation VLAs without Robot Demonstrations
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-14T06:32:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.19196
  - Alt: https://arxiv.org/abs/2611.12885
- Summary: Imitation learning for visuomotor policies typically relies on teleoperated robot demonstrations, which are costly because every episode requires a trained operator controlling a physical robot in real time through teleoperation interfaces and wearable body-tracking hardware. Egocentric glasses capture human demonstrations without a robot or handheld grippers, yet they track only the head and in-view human hands, and directly copying human motion to a robot with different stature, arm reach and hand morphology fails to produce feasible contacts. \method{} converts egocentric glasses recordings into physically verified robot training trajectories. An agentic real-to-sim stage reconstructs collision and textured visual assets from the recorded RGB-D and head streams, completes unseen surfaces when needed, and predicts target contact bands on the manipulated objects. During motion adaptation, a grasp planner turns each contact band into a feasible robot wrist pose and finger closure, bilevel stance optimization plans collision-free standing postures that keep hand targets reachable, and a whole-body motion generator synthesizes lower-body locomotion and out-of-view arm motion. Two-stage motion correction then blends visibility transitions kinematically and trains a reinforcement-learning tracking policy in physics simulation under agent-designed semantic rewards, completing manipulation phases even when the object leaves the camera view. Rendering the reconstructed scene through the robot's onboard camera along the optimized rollout yields synchronized robot-view images, proprioception and verified action labels. Fine-tuned exclusively on this converted dataset, without real-robot demonstrations, GR00T N1.7 performed loco-manipulation tasks autonomously on a Unitree G1. Project page: https://robonana.github.io/ego2sim2humanoid/

### 9. Training Reasoning Models in Simulation to Natively Use Real Robots
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-13T18:59:02+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.18562
- Summary: Robot-use agents (RUAs) have emerged as a promising approach to general-purpose robot control. However, strong performance has so far been achieved only by frontier proprietary models such as GPT-6 Astra and Claude Fable 5.2, whereas open-weight models remain substantially less capable. We show that an open-weight 27B reasoning model can be trained to use real robots natively through reinforcement learning, entirely in simulation and without demonstrations. Like a computer-use agent (CUA), the model observes the environment, reasons in a chain of thought, and generates the next end-effector pose, without any harness. We build a Post-training Engine for Agentic Robotics (PEAR) and use it to train the model on simulated robot tasks at scale with robot-use reinforcement learning (RURL), mirroring how frontier models acquire computer use. We find that the skills acquired in simulation generalize well beyond the training tasks: they transfer to an unseen robot, to the real world, and to novel instructions. After training on LIBERO and RoboDojo in simulation, the model succeeds in 60% of our trials on a real dual-arm robot, whereas the base model succeeds in none. On LIBERO, training raises the success rate from 1.6% to 74.4%, approaching GPT-6 Astra and GPT-6.1 Sol at maximum reasoning effort. Compared with $π_{0.5}$, a vision-language-action model fine-tuned on demonstrations, our model is substantially more robust to changes in the task itself. On LIBERO-Pro, $π_{0.5}$ succeeds in only 0.75% of episodes when assigned a new task in a familiar scene whereas our model succeeds in 57.4%. Finally, the model retains its general capabilities, with no measurable degradation on nine reasoning, coding and vision benchmarks. These results highlight robot-use reinforcement learning as a promising component of foundation-model post-training.

### 10. Forget the Lineage: Forward-Secure, Lineage-Complete Cryptographic Erasure for LLM-Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-13T13:01:47+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.18133
- Summary: Large language model (LLM) agents keep a long-term memory that the model itself writes: summaries, extracted facts and embeddings derived from what users said. Deleting a message is therefore not enough: its derivatives, storage residue and backups survive. We define lineage-complete forward-secure erasure: after a forget request, an adversary that later obtains all storage and the agent's current keys learns nothing about the forgotten input or any memory derived from it. We present LinEra, which encrypts each memory under a key derived from its parents' keys along the derivation graph; source keys come from a puncturable pseudorandom function, so forgetting is a single puncture and every descendant becomes unreadable without being located. A sound lineage rule records as parents everything the writer saw, which confines all influence of a source to its descendants. We prove security and lineage integrity and integrate LinEra with mem0. With real LLMs from two families (1.5B to 7B parameters) writing the memory of LoCoMo conversations, an attacker holding every file and the current keys recovers, on all ten conversations written by the largest model, 70 of 71 forgotten secrets after logical deletion, 67 with per-object or epoch keys, and none with LinEra; the same holds for every writer tested. The price is a larger forgetting radius, which follows a simple law in the writer's fan-in: forgetting 1% of turns erases 73.0% of derived memories with session-level summaries but only 3.8% with four-turn windows, which also answer better; re-deriving restores what is lost.

### 11. X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-12T23:38:27+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.17598
- Summary: Long-horizon navigation from indoors to outdoors remains an open problem for humanoid robots: one instruction covers rooms, doors and roads, and the camera moves with the gait. Worken, AGIBOT's measure of productive robot work, depends on robots that reach their workplaces autonomously. We present X-Nav, to our knowledge the first system to take a bipedal humanoid through a language-instructed long-horizon mission from indoors to outdoors. X-Nav covers a pipeline from data to deployment. Its data engine collects navigation data in open-source scenes, in digital twins of deployment sites and on real robots. Its navigation model, MELIOR, takes only RGB images from the robot's built-in camera and comes in two versions: MELIOR-A predicts actions, and MELIOR-N predicts a navigation goal. Its agentic workflow, X-Navarch, turns a brief human instruction into sub-tasks and deploys MELIOR on the robot with explicit target navigation and obstacle avoidance. On the Lingxi X2, X-Nav completes a mission of about a hundred metres from an office lobby to a store in a neighbouring building; LiDAR and odometry are used for target approach and low-level control. The mission is completed with both versions of MELIOR: the robot follows a change of destination and walks through a door from the lobby to the road, and with X-Navarch it also passes static and dynamic obstacles on the route. During deployment, MELIOR is adapted with data collected in a digital twin of the site; the adaptation raises its closed-loop success rate in the twin, and the adapted model is then deployed on the robot at the real site. In addition, MELIOR achieves competitive results on the R2R-CE and RxR-CE benchmarks.

### 12. The Fed Is Worried AI Agents Could Trigger a Bank Run
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-16T21:12:02+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://gizmodo.com/the-fed-is-worried-ai-agents-could-trigger-a-bank-run-2000840566
- Summary: No summary.

### 13. Apple reveals new Mac security controls as AI agents raise privacy risks
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-16T21:01:02+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/16/apple-reveals-new-mac-security-controls-as-ai-agents-raise-privacy-risks/
- Summary: Following an October announcement, Apple has detailed new permission controls, warnings, and transparency features coming to macOS 27.3 to address risks posed by AI agents and other apps.

### 14. FBI says Artex AI open source hacking tool used to breach networks in ‘under three hours’
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-16T17:36:43+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/
- Summary: The FBI says that the open source hacking tool was used in cyberattacks targeting a U.S. IT giant and the South Korean financial industry.

### 15. Google: AI agent turned a security patch into a exploit with no human help
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-16T14:14:09+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.theregister.com/research/2026/11/16/google-ai-agent-turned-a-security-patch-into-a-working-exploit-with-no-human-help/5309926
- Summary: No summary.

### 16. Agentic AI Designs an Analog Synthesizer
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-16T01:28:10+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://cpldcpu.github.io/2026/11/14/touchsynth/
- Summary: No summary.

### 17. StateWeave
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-15T20:32:35+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/stateweave
- Summary: <p> Test your AI agent on working clones of the apps it uses </p> <p> <a href="https://www.producthunt.com/products/stateweave?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="http://www.producthunt.com/r/p/1317996?app_id=339">Link</a> </p>

### 18. Puffin
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-15T19:51:59+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/puffin-2
- Summary: <p> Identity and inboxes for AI agents </p> <p> <a href="https://www.producthunt.com/products/puffin-2?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="http://www.producthunt.com/r/p/1317965?app_id=339">Link</a> </p>

### 19. UI SDK by Vercel
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-15T12:01:57+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/ui-sdk
- Summary: <p> Give AI agents the building blocks to create UI </p> <p> <a href="https://www.producthunt.com/products/ui-sdk?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="http://www.producthunt.com/r/p/1317488?app_id=339">Link</a> </p>

### 20. EcoToxFred: A knowledge-graph-grounded conversational agent for exploring ecotoxicological monitoring and hazard data
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-15T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.1101/2025.07.04.663152
- Summary: Assessing chemical risks to aquatic ecosystems requires the joint interpretation of monitoring data, ecotoxicity data, and derived risk indicators, yet such integrated data are rarely accessible to users without database expertise. We present EcoToxFred, an open-source conversational agent that provides natural language access to a curated knowledge graph of chemical monitoring and hazard data for European surface waters. EcoToxFred couples a large language model (LLM) with a Neo4j graph database in a retrieval-augmented generation (RAG) architecture. An agent interprets user questions, selects tools, translates questions into graph queries, and returns answers as text, tables, or interactive maps, together with the executed query for reproducibility. We evaluated EcoToxFred with GPT-4.1 and GPT-5 on a benchmark of 25 questions, including six questions derived from an expert workshop, each posed three times. Answers were scored for tool selection, execution accuracy against human-written reference queries, and goal accuracy using the RAGAS evaluation framework with an independent LLM judge. With both models, EcoToxFred selected an appropriate tool in at least 92% of runs and reproduced the reference result in 74% of runs with a reference query, including all lookup questions. Goal accuracy was 52% with GPT-4.1 and 63% with GPT-5. Failures concentrated on multi-step analytical questions, incomplete presentation of long results, and mismatches between user and database vocabulary. EcoToxFred shows how knowledge-graph-grounded LLM agents can lower the barrier to ecotoxicological data exploration while keeping answers traceable to the underlying data, and its architecture is transferable to other ecological data infrastructures.

### 21. OpenFrame
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-04T18:56:32+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/openframe-3
- Summary: <p> AI agents that run your IT. You approve every fix. </p> <p> <a href="https://www.producthunt.com/products/openframe-3?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="http://www.producthunt.com/r/p/1304602?app_id=339">Link</a> </p>

### 22. Boost.space AgentOS
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-03T08:33:13+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/boost-space
- Summary: <p> One operating system for all your AI agents </p> <p> <a href="https://www.producthunt.com/products/boost-space?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="http://www.producthunt.com/r/p/1302625?app_id=339">Link</a> </p>

## Top Signals By Weighted Score (including already-seen)

### 1. Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-11-09T19:45:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.13161
- Summary: Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazards, and aligning with human mission intent. Existing language-guided reinforcement learning (RL) methods primarily focus on single-agent instruction following and lack mechanisms for team-level coordination in complex, partially observable environments. This paper presents a Cognitive Multi-Agent Framework based on Language-Grounded Hierarchical Reinforcement Learning (LG-HRL) that integrates natural-language understanding, hierarchical policy decomposition, and a shared cognitive workspace to achieve cohesive multi-agent behavior in SAR scenarios. Human instructions are interpreted by a large language model (LLM) and transformed into structured semantic cues that guide high-level strategy selection and role assignment across UAV and UGV agents. A formal Language-Grounded Multi-Agent Hierarchical Decision Process (LG-MAHDP) is introduced to model the interplay between semantic grounding, hierarchical control, and distributed coordination. Comprehensive experiments in a simulated disaster environment show that LG-HRL improves learning speed by 2.3 times, increases coordination coherence by 37%, and enhances subgoal accuracy and hazard avoidance by 46% and 31%, respectively. The system achieves 20-30% higher victim rescue rates, demonstrates emergent role specialization, and adapts immediately to human verbal updates. Ablation studies confirm that both the shared cognitive workspace and language grounding are critical to overall system performance. Overall, this work establishes a new paradigm for language-guided multi-agent SAR robotics, demonstrating that semantic grounding combined with hierarchical reasoning enables safer, more efficient, and more interpretable autonomous rescue operations.

### 2. Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-11-09T11:57:33+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.12269
  - Alt: https://arxiv.org/abs/2611.12068
- Summary: Cryptocurrency markets provide a natural testbed for autonomous AI agents because they are digital-native, high-frequency, and machine-speed environments, yet existing methods often struggle with non-stationary market regimes, opaque decisions, and fixed aggregation rules. In this paper, we propose Agent4Crypto, a dual-reflective and market-feedback-aligned multi-agent system. The framework coordinates specialized agents for data collection, analysis, risk assessment, reflection, and trading, synthesizing heterogeneous signals from prices, indicators, news, and charts in an interpretable decision pipeline. Our central design is a trader-centric decision mechanism: three style-specific trader agents, Aggressive, Neutral, and Conservative, generate candidate actions and natural-language rationales from the same market context, while their influence is learned rather than manually fixed. A PPO-based gating policy dynamically allocates trader weights through a dual-reflective feedback process. One reflection stream evaluates post-trade decision quality from realized portfolio outcomes and distills reusable lessons into a Financial ReasoningBank for retrieval in subsequent trader prompts, while the other estimates trader-level counterfactual contribution, indicating which style has recently aligned better with market movements. The PPO state combines Counterfactual Contribution Memory with market features, previous trader weights, and current trader actions, so trader influence adapts across bull, sideways, and bear regimes. Experiments on BTC, ETH, and XRP show that Agent4Crypto improves total return and Sharpe ratio over traditional strategies, machine learning and reinforcement learning baselines, and existing LLM-based trading systems, demonstrating the value of interpretable trader competition and market-feedback-driven adaptation in volatile cryptocurrency markets.

### 3. PANINI-DR: Controlled Deep Research through Generative Semantic Workspaces
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-10-10T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2610.15208
- Summary: Deep research requires connecting multiple steps of search, reasoning, and computation, with intermediate findings guiding what to investigate next. As investigations grow, agents must maintain research state across model calls and check findings before errors propagate into subsequent work. We introduce PANINI-DR, a multi-agent harness that separates coordination of the overall investigation from the research and verification of individual subquestions. A shared workspace, built on the Generative Semantic Workspace representation, records subquestions, their dependencies, findings, and supporting evidence. Researchers investigate individual subquestions, while a separate verification agent checks proposed answers against those subquestions and their evidence. Verification feedback guides further investigation, and recorded findings inform subsequent assignments. We evaluate PANINI-DR on BrowseComp-Plus, FRAMES, and MoNaCo against seven state-of-the-art deep-research harnesses, all using a shared language-model backbone and frozen corpora. PANINI-DR achieves the strongest average performance across the three benchmarks. On BrowseComp-Plus, it achieves 73.3% accuracy, outperforming the next-best harness by 16.0 points. Its advantage is strongest on hard questions, where it answers nearly twice as many as the next-best harness. Ablations further show that structured planning and persistent state improve performance, as does checking each finding against its cited evidence before it is reused. Because a model can answer correctly from memory alone, we also analyze the evidence retained by each harness. PANINI-DR achieves the highest answer recoverability from saved evidence on all three benchmarks, while complementary claim-support audits show stronger evidence-backed answers. Accounting for this evidence changes how harnesses compare and further strengthens PANINI-DR's advantage.

### 4. Evaluating Language Models as Orchestrators in a Tool-First Biomedical Discovery Platform
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-16T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.13.766436
- Summary: Large language models (LLMs) increasingly orchestrate agentic biomedical discovery systems, but cloud deployment raises concerns about inference cost, data privacy, and governance. Small language models (SLMs) that run on-premises are an alternative, provided they orchestrate scientific tools about as well as larger models. We built a tool-first, multi-agent system for scientific discovery in which an orchestrator coordinates six specialized tool systems: differential expression, literature retrieval, pathway enrichment, network-based gene prioritization and knowledge-graph analysis, perturbation signature matching, and structural/druggability assessment. In a tool-first design, specialized tools supply the domain knowledge and computation, so the model's main task is coordination, e.g. choosing tools, passing the right parameters, calling them in the right order, and carrying results across turns. With the tools, prompts, workflow, and benchmark held constant, we compared three orchestrators, Gemma 4 (26B, open-weight and locally deployable), Gemini 2.5 Flash, and Claude Sonnet 5. Evaluation used a custom benchmark of 104 single-turn and multi-turn tests, an LLM-as-judge protocol (groundedness and evidence validity), tool-use accuracy and efficiency metrics, and blind expert review. On single-turn tasks, the three models performed comparably, and reviewers did not rate the SLM below the larger models. In multi-turn tasks, Claude Sonnet 5 showed marginally higher evidence validity, Gemma 4 was weakest when parameters had to be assembled across turns, and all three models struggled with tool ordering on memory-dependent tasks. These differences were illustrated with case studies. Finally, we propose strategies to help SLMs address the multi-turn limitations and support cost- and privacy-aware deployment.

### 5. WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-09T18:45:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.12856
  - Alt: https://arxiv.org/abs/2611.17883
  - Alt: https://arxiv.org/abs/2610.33282
  - Alt: https://arxiv.org/abs/2610.22316
- Summary: Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shifting the design of system structure from developers to the model at run time. The quality of this organization therefore constitutes a distinct capability, yet existing benchmarks either measure end-to-end task completion or evaluate coordination under structures specified in advance. We formalize this capability as workflow orchestration and introduce WorkflowArena, a benchmark of 145 long-horizon tasks spanning 8 professional domains, from software engineering and formal mathematics to legal analysis and 3D production. Each task specifies an initial workspace and an integrated deliverable composed of interdependent components, which is assessed by a hidden verifier. Agents determine autonomously whether and how to delegate, and all delegation is recorded, enabling joint evaluation of deliverable quality and the organization of the underlying work. Experiments with nine models show that no single configuration performs best across all domains and that systems exhibit distinct delegation strategies: at high effort, Claude models in Claude Code invoke workflows less frequently but with larger worker groups, whereas GPT models in Codex delegate more frequently in smaller units. When the executing model is held fixed on a challenging subset of tasks, workflows authored by Claude Opus 5.5 substantially improve weaker executors, indicating that workflow organization is itself a measurable determinant of task performance.

### 6. Multi-Modal Multi-Agent System for Bridge Operation and Maintenance based on Large Language Model
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-02T08:26:24+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02738
- Summary: Bridges are critical transportation infrastructure, and reliable operation and maintenance (O&M) is essential for traffic safety and long-term structural performance. However, bridge O&M faces key bottlenecks: no unified architecture coordinates heterogeneous resources; model inferences lack clear links to physical-mechanical laws; and experts' tacit knowledge remains difficult to formalize. This study proposes a knowledge-enhanced autonomy formalization methodology and apply it to construct the Bridge O&M Multi-Modal Multi-Agent System (BOMMA), which integrates heterogeneous diagnostic actions, physics-mechanics-informed representations, long-term memory, and structured experiential knowledge within a coordinated multi-agent workflow, enabling interpretable and traceable scheduling, analysis, and decision-making. On 3,492 multi-source instructions, the proposed method achieves scheduling recalls of 85.37% for simple and 99.40% for composite tasks, with 95.35% BERT F1-score for O&M action reasoning. Ablation studies confirm the contributions of the components in the autonomy. This study bridges general LLM reasoning and specialized bridge O&M requirements.

### 7. Locating and Closing Information Gaps in Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-29T14:45:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.40186
  - Alt: https://arxiv.org/abs/2610.18780
- Summary: Multi-step Web tasks often require several LLM agents to gather and combine evidence. The communication graph of a fixed workflow restricts which agents can read each other's outputs: evidence retrieved by one agent may never reach the agent that needs it, leaving an information gap and an incomplete or incorrect answer. Adding a connection can deliver the missing evidence, but can also lead the receiver to adopt an incorrect upstream conclusion that displaces a correct answer; the final output alone does not separate the two. We propose Selective Probing and Link Insertion for Closing information gaps in multi-agent Execution (SPLICE), which locates information gaps per query and decides what to adopt after adding an edge. After the original workflow runs, SPLICE uses the query and node outputs to locate a possible gap, adds one directed edge from a source to a receiver to deliver the relevant evidence, and re-executes the receiver and affected downstream nodes, producing a candidate answer. The adoption decision reads both the final answers of the two runs and the process changes the edit caused inside the workflow: how far the receiver moved, where its new content came from, and whether the change reached the final answer. A selector trained on these process features chooses between adopting the candidate answer and retaining the original. On five benchmarks, SPLICE raises the task score on Web tool use by 8.0% and the mean score on four reasoning and planning benchmarks by 5.7% relative to the static skeleton, at 1.25 to 1.44$\times$ the skeleton's cost, and transfers zero-shot to four unseen backbones.

### 8. EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-25T17:09:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.34450
- Summary: Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control. Agents need to adapt to other agents at test time and reuse accumulated experience to refine their interaction strategies for future interactions across cooperative, mixed-motive, and adversarial settings. However, existing approaches often develop adaptation mechanisms for particular interaction settings. This raises a central question: how can decentralized MAS support test-time adaptation and reliable experience reuse across interaction settings? We propose EvolveMAS, a unified self-evolution framework that supports experience-driven adaptation within and across episodes. EvolveMAS pairs each main agent with a dedicated MemoryAgent for test-time memory governance, which maintains isolated Structured Memory outside the main agent's reasoning context. EvolveMAS organizes adaptation into two complementary processes: Within-Episode Online Adaptation and Cross-Episode Knowledge Evolution. During Within-Episode Online Adaptation, MemoryAgent updates episodic, semantic, and working memory from interaction evidence to inform subsequent actions. During Cross-Episode Knowledge Evolution, the main agent uses memory and episode outcomes to distill reusable interaction knowledge comprising partner profiles and interaction strategies for subsequent episodes. Across five benchmarks and six evaluation configurations spanning the three interaction settings, EvolveMAS achieves the highest normalized average score of 77.2 among the compared methods. Ablations show that test-time memory governance and cross-episode knowledge reuse both improve performance. Interaction traces further illustrate how updated memory and distilled knowledge guide subsequent interactions. These results support experience-driven adaptation in decentralized MAS without updating model parameters.

### 9. From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-21T10:49:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.29560
- Summary: Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work has begun to address these challenges by augmenting foundation-model policies with memory and by introducing hierarchical architectures that separate high-level planning from low-level execution. We organize the high-level VLM as a robotic agent through an editable harness to maintain task context and improve planning through execution experience. We instantiate this approach as SERA (Self-Evolving Robotic Agent), with a fixed VLA executor providing low-level control. The harness maintains and updates task context using observations and execution feedback to guide subsequent planning. Self-evolution uses environment rollouts to propose and evaluate harness revisions, with the selected configuration fixed before held-out testing. On RoboMME, SERA achieves 51.38% overall success with autonomous selection, compared with 44.38% without self-evolution. Our exploration suggests that agentic planning is a promising direction for history-dependent robotic manipulation.

### 10. Refuse the Harm, Complete the Task via Graph-of-Rules Planning for LLM-Enabled Robots
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-17T10:13:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.24603
- Summary: Large Language Models (LLMs) are increasingly used in embodied AI for robotic manipulation and planning, but their deployment in physical systems exposes vulnerabilities such as jailbreak attacks that induce unsafe behavior. Existing inference-time defenses are mainly evaluated on short instructions containing a single hazard, whereas realistic tasks may interleave safe and unsafe sub-tasks, conceal hazardous steps, or combine individually safe actions into unsafe outcomes. Such compound instructions make it harder for a single safety decision to distinguish hazardous sub-tasks from legitimate ones, risking either overlooking the hazard or rejecting the whole instruction. We introduce safe task completion, a task that requires an LLM-enabled robot to refuse the harmful part of an instruction while completing its legitimate part. To address this problem, we propose RuleGraph, a multi-agent Graph-of-Rules planning framework that distributes safety enforcement across multiple reasoning and verification stages. Five cooperating agents are used to ground general safety principles into world-specific rules, assess the instruction's sub-tasks in context, and derive a safe goal from the legitimate ones. Planning toward this goal is then organized as a graph of rule-specific nodes, where higher-level nodes inherit the union of their parents' rules, and candidate plans are progressively verified and aggregated until a single plan satisfies every relevant rule. In this way, RuleGraph reduces reliance on a single centralized safety decision. We evaluate RuleGraph on pure-attack and compound instructions across two benchmarks in two environments using Attack Success Rate (ASR) and Task Success Rate (TSR). RuleGraph reduces ASR to 0% on both benchmarks while achieving the highest TSR among all methods, reaching 98.57% on the RoboGuard benchmark and 84.54% on our long-horizon compound instructions.

### 11. ChunkAct: Action Chunking for Agentic Robotics
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-13T17:59:57+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.18874
- Summary: Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.

### 12. From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-13T17:59:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2611.18484
- Summary: AI-enabled remote patient monitoring is evolving beyond passive data collection toward agentic AI systems that interpret patient states, coordinate care, and initiate action across domestic and clinical settings. This structured scoping review finds that mature agentic care has not yet emerged: Most systems remain human led, while stronger decision-action coupling and embodied AI remain largely confined to prototypes and pilots. Healthcare robotics makes the transition from monitoring to action especially visible by translating AI-generated recommendations and decisions into speech, movement, prompting, physical assistance, escalation, and care coordination, making embodiment, clinical integration, human oversight, and governance fundamental design requirements. Further progress requires safe and interoperable care architectures in which intelligent components operate through clinically validated and accountable workflows. We propose agentic robotics as a future direction for supervised systems embedded in the care ecosystem, connecting AI agents and robots with clinicians, caregivers, and patients through auditable workflows that can be interrupted and remain subject to human oversight and explicit AI governance.

### 13. On Private Knowledge Retrieval and Private Inference for secure multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-10T07:43:02+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.13696
  - Alt: https://arxiv.org/abs/2610.23078
- Summary: Multi-agent systems provide a convenient framework for the massive deployment of agents based on Large Language Models (LLMs). It provides a sound framework where agents can interact with existing software to perform actions in an autonomous way. Agentic AI is the new term to denote these AI-based autonomous systems. In real multi-agent systems, agents need to deal with malicious agents some of which can exploit security vulnerabilities to do harm. A memory poisoning attack is an example of exploiting a vulnerability to modify agents knowledge and, thus, affect its behavior. In an agent, there are different types of memory systems (semantic, episodic, and short-term) which have their own characteristics and for which different memory poisoning attacks may be developed. In this paper we focus on semantic memory, we discuss its attack, and mitigation strategies. We introduce private knowledge retrieval and private inference. We propose a signature system in the knowledge base to prevent from undesired manipulation. This should avoid memory poisoning attacks by introducing security by design in the construction of the semantic memory. In our architecture, an agent contains a local Prolog-like inference system (i.e., using Horn clauses to represent knowledge) which accesses an external knowledge base to get the required knowledge. This externally signed knowledge base is accessed privately. We provide different implementations in Python using different privacy levels including k-anonymity and information-theoretical privacy (IT-PIR).

### 14. A Common Recognition Architecture Across Memory Scales
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-09T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://www.biorxiv.org/content/10.64898/2026.11.04.764437
- Summary: Recognition decisions occur across memory episodes that vary vastly in scale, from compact single-item episodes to extended experiences involving hundreds of items. To test how memory scale shapes the neural mechanisms underlying old/new judgments, we recorded EEG while participants performed a recognition memory task across set sizes ranging from 1 to 128 items (spanning 2 to 256 recognition judgments). Classic electrophysiological signatures of recognition, including frontal and parietal old/new effects, persisted continuously across set sizes. Furthermore, multivariate neural classifiers trained on small memory scales generalized robustly across set sizes. Rather than revealing distinct neural formats, increasing memory scale produced systematic, continuous shifts in the timing and strength of a shared recognition response: signals emerged progressively later and weaker at larger memory scales. Temporal-alignment and cross-correlation analyses demonstrated that responses across scales followed a common waveform trajectory, with timing shifts propagating into motor response preparation. Finally, individual difference analyses revealed that this common recognition format exhibits scale-dependent behavioral relevance, tracking working-memory capacity at smaller scales and long-term memory performance at larger scales. Together, these findings demonstrate that recognition signals share a common neural format across scale while changing dynamically in timing, strength, and behavioral relevance, providing evidence for convergence onto a shared recognition architecture.

### 15. Coordinated Mixed-Precision KV Cache Quantization for Efficient LLM-based Multi-agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-06T17:07:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.10096
- Summary: LLM-based multi-agent systems solve complex tasks through collaboration, but their growing, simultaneously resident key-value (KV) caches create a memory bottleneck. Applying single-model quantization policies independently ignores differences in agents' precision needs, potentially degrading collective reasoning. We introduce Coordinated Mixed-Precision KV Cache Quantization (CoMixKV), which combines online sensitivity estimation with joint agent-layer bit-width allocation under a shared memory budget. To our knowledge, CoMixKV is the first mixed-precision KV-cache quantization framework to jointly allocate precision across simultaneously resident agent caches under such a budget. The estimator derives sensitivity from a local attention-error bound using recent queries, keys, and values, without calibration data, trial quantization, or additional model passes. A shared controller combines these scores with remaining quantizable capacity and byte-level storage costs to minimize total estimated error. Allocations are refreshed as agents start or finish and new observations become available. Selected widths apply only to newly quantized blocks; recent states retain native precision and previously quantized blocks remain unchanged. Across four benchmarks and three LLM backbones at average 2-bit, 3-bit, and 4-bit settings, CoMixKV achieves strong accuracy against the evaluated quantization baselines. At the average 3-bit setting on Gemma-4-31B-it, it achieves 68.35% average accuracy, exceeding the strongest quantized baseline by 0.59%. On Qwen3-32B, it reduces peak KV-cache memory by 32.08% and achieves a 1.38x inference speedup over FullKV.

### 16. HomeLoop: A Simulation Framework and Benchmark for Robot-IoT Coordination in Everyday Domestic Assistance and Safety
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-06T02:54:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.08914
- Summary: Recent progress in embodied robotics is bringing robots closer to deployment in homes, as vision-language models (VLMs) are demonstrating significant advances in reasoning, making VLM-driven robots promising home assistant agents. These agents will often be introduced into homes that already have cameras, Internet of Things (IoT) devices, and residents with wearables. To fulfill their potential, they need to integrate with existing smart infrastructure and reason through ambiguous scenarios: a smoke alarm may come from a pan about to ignite, a pan already on fire, a resident cooking or a faulty sensor, and each calls for a different response. To that end, we introduce HomeLoop, a simulation framework and benchmark built on Isaac Sim that combines robot bodies, networked devices and wearables, simulated residents and visitors, faulty sensors, and hazards that evolve over time. Our benchmark is composed of 20 tasks across five families grounded in real-world household hazards and needs, and designed so that the same alert can have different causes. A runtime monitor scores each episode with temporal-logic checks on the final outcome and the actions along the way, and every action carries a predefined cost. We evaluate six open-weight and proprietary VLMs. The best achieves a family-balanced score of 61.9%, and across models we see a pattern of over-reaction: failed episodes involving prohibited interventions outnumber those involving missed required interventions by more than two to one, with models often shutting off the stove before investigating the alarm's cause. HomeLoop is an extensible foundation intended for use in research on robot-IoT coordination, long-term memory, proactive assistance, and privacy-safety trade-offs. HomeLoop will be released with 2,100 home layouts that can be automatically furnished in diverse configurations, five robot bodies and 20 networked device types.

### 17. H^2MARL: Hierarchical Heterogeneous Multi-agent Reinforcement Learning for Humanoid Robot Control
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-04T13:48:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.06523
- Summary: Coordinated whole-body control of humanoid robots remains challenging due to high-dimensional coupled dynamics and substantial physical heterogeneity across joint degrees of freedom (JDoFs). Existing multi-agent reinforcement learning methods either employ coarse agent partitions or directly apply generic heterogeneous-agent algorithms, while hierarchical controllers commonly optimize high-level planning and low-level execution independently, leading to uncoordinated motion. In this paper, we propose H^2MARL, a hierarchical heterogeneous multi-agent reinforcement learning framework with two key mechanisms. We first formulate humanoid whole-body control using a JDoF-level physical-heterogeneity-aware policy factorization, where each torque-actuated JDoF is conditioned on an explicit descriptor of its actuation, kinematic, and dynamic properties. Moreover, we develop a closed-loop policy-executor co-optimization mechanism that jointly adapts the high-level pose planner and the low-level joint executor using shared interaction trajectories, thereby reducing the distribution mismatch between planning and execution. Extensive experiments in MuJoCo and Isaac Gym demonstrate that H^2MARL consistently improves locomotion stability, gait coordination, and motion quality over homogeneous, coarse-grained, and independently optimized alternatives.

### 18. ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-03T04:57:47+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.04321
- Summary: Multi-agent LLM systems assign different responsibilities to different agents: one plans, another retrieves evidence, another verifies, another executes. This division of labor is only meaningful if each agent stays within the functions it is authorized to perform. Over many turns, however, an agent can produce a locally reasonable message that exercises authority belonging to another role: a verifier that begins planning, a retriever that asserts unsupported conclusions, an executor that changes state no one approved. We formalize this as role drift, a turn-level breach of an agent's role contract. We introduce Agent Trajectory Control (ATC), which makes each role's authority explicit as a contract and enforces it at the point where a message would enter the shared conversation. ATC scores a proposed output for out-of-role deviation, leakage into the functions of other roles, impermissible speech acts, and logical contract breaches, then computes a leakage-regularized target that constrains regeneration; the revised message is re-checked before admission. Enforcement acts on the message rather than the generator, so ATC governs agents whose internal representations are unavailable. Across homogeneous and heterogeneous teams, ATC improves task performance and role consistency while lowering role-drift energy relative to strong baselines spanning prompting, memory, workflow control, and activation editing, with the largest gains under explicit role-confusion stress tests and in larger, more diverse teams.

### 19. Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-02T01:09:24+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02361
- Summary: Can a language model that reads the full history of an access log say whether a service may act now? On an executable benchmark of grants, withdrawals, reinstatements, expiries, groups and change windows under a known policy, scored on pairs of histories that differ only in the order or one field of the deciding events, open models of 7 to 32 billion parameters fall from 72 to 86 percent after eight or sixteen events to 48 to 55 percent after 256, while reasoning-trained 32B models reading the current state reach 96 and 98 percent. A reasoning model of 120 billion parameters trails the state by four and seven points at 256 and 512 events and by about ten at 1,024, so the length beyond which explicit state outlasts long context grows with the reader. We treat agent memory as recursive filtering. The decision depends on the history only through a state whose size is set by the number of tracked keys. A store holding fewer component records than the state forgets on a time scale set by its capacity, and a reader model predicts its accuracy within 0.02 on average in a registered test. Retaining log lines without regard to time order errs with probability approaching one half, a bound that is attained. A filter in which a model parses each line and an explicit rule applies the updates answers 80 to 89 percent at 256 events and beats relevance retrieval, model-kept ledgers, a reimplementation of StateMem and the Mem0 library. A retriever that selects at query time the lines the queried state depends on matches it at 256 events on the first domain, so what decides is selection by the state's dependencies, which the filter performs when writing, without the query. Applying parsed updates themselves, the models fall to 58 and 59 percent. A frozen replication on a second domain with fresh wording reproduces the horizon.

### 20. Head movement allocation in freely-moving macaques learning object-context sequences
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-02T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.1101/2023.12.11.571113
- Summary: Flexible learning and long-term memory are hallmark features of primate cognition that are shaped by interactions with changing environments. A comprehensive understanding of these brain-body-environment interactions requires minimal constraints on behavior, and environments rich with conditional cues that encourage diverse behavioral dynamics. In this study, we introduce a multi-level enclosure (Treehouse) that allows for independent control of spatially distributed touchscreens for studying cognition in freely moving macaques. To test flexible learning, two monkeys completed trials consisting of a regular sequence of conditional object choices (targets) across four distinct spatiotemporal contexts (screens). Both monkeys acquired numerous unique, conditional object-context sequences without detriment to new learning as memoranda accumulated. They also successfully recalled their correct choices after weeks without exposure. To assess how monkeys allocate movement during learning and memory-guided decision making, we tracked their head kinematics and used recurrent neural networks to decode different aspects of their engagement with the environment during the choice epoch of the task. One such model predicted the position of the object about to be touched, including on error trials, tracking overt gaze towards objects. Separate models decoded sequence corner, the ordinal step, and the individual screen stations the monkeys occupied, despite identical stimulus layouts and behavioral demands at each station. Head movements also showed efficiencies that the task did not require: under conditions of uncertainty, monkeys were biased in their initial search locations to the targets that were closest to reach, and across days they made smoother head movements as training progressed, with no change in accuracy. These results demonstrate the potential of immersive 3-D environments, in which body kinematics can shed light on animals' goals, and reveal that situated learning …

### 21. The Agentic Observer Hackathon: Autonomous Decision-making in Simulated Astronomical Surveys
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-01T15:25:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2611.01988
- Summary: Astronomical surveys must allocate observing time while responding to changing conditions and competing scientific priorities. We present the Agentic Observer Hackathon (AOH), a community challenge for studying autonomous survey operations. Within a synthetic multi-object survey with prescribed exposure responses and assignment constraints, decision systems select pointings, assign targets and choose exposure configurations while responding to observing requests, instrumental faults and data loss. We evaluate systems submitted by 102 teams on campaigns reserved for evaluation and analyse target completion in a reference campaign. The leading systems combine numerical exposure planning with language models for interpreting operational information and supporting longer-term decisions. Exploratory tests show improved fault reporting with model access in several systems, while revised scientific priorities produce substantial changes in ranking. The reference campaign traces target completion and diagnoses errors in the baseline's inference of prescribed quality bands. The released simulator and reference strategies provide common survey conditions for comparing exposure allocation, target selection and recovery from interruptions.

### 22. A complete analytical characterization of optimal collision-free motion for two robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:53:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41558
- Summary: Collision-free motion planning for multi-agent robotic systems remains an active research area because of the complexity of coordinating robot trajectories, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. Importantly, the analytical difficulty of nonconvex collision-avoidance constraints has so far driven the development of exclusively numerical methods. We derive a complete analytical characterization of the optimal trajectories for two robots that start and end at rest, under double-integrator dynamics and a squared-acceleration objective. We prove that these trajectories belong to eight distinct contact families and determine which family applies for each configuration of initial and final positions. We analyze the geometrical properties of the optimal trajectories, provide a numerical algorithm for computing them, and discuss how these insights may improve the performance of existing numerical trajectory optimizers.

### 23. Contact-based optimization for collision-free motion planning for a million robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:46:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41548
- Summary: Multi-agent robotic systems have attracted growing interest in recent years, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. At the planning level, robot motion is often modeled using double-integrator dynamics (with low-level controllers handling the physical dynamics during execution) with a minimum-energy objective subject to collision-avoidance constraints and limits on position, velocity, and acceleration. The complexity of the problem resides in the constraints, which couple the trajectories and make the optimization problem nonconvex. Existing numerical approaches typically discretize and optimize entire trajectories, which becomes expensive for large fleets. We exploit the structure of optimal trajectories by organizing optimization around contacts, at which robots reach the minimum allowed separation. We formulate a coupled algebraic system in contact variables and reconstruct trajectories analytically between contacts. Our algorithm, sequential contact insertion (SCI), starts from unconstrained trajectories, inserts contacts at separation violations, and jointly adjusts their times and states. Numerical experiments demonstrate planning for one million robots in minutes and thousands of robots in fractions of a second. On problems feasible for a fixed-grid sequential convex programming baseline, SCI achieves median speedups of several orders of magnitude at matching solution accuracy.

### 24. Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-28T20:40:33+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.38869
- Summary: Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments across retrieval, memory, tools, and peer communication. In this paper, we define belief as an engineering abstraction for evidence-based commitments that guide downstream action. Building on this view, we propose the Explicit Belief Multi-Agent System (EB-MAS), which externalizes belief states into a structured substrate, uses belief operators to propose candidate updates, and applies a Cognitive Firewall to bound or reject updates that are weakly evidenced but strongly driven by vulnerability cues. We also discuss the risk of group belief at the group level, including manufactured consensus, collusion, and cascading misinformation, and outline practical integration challenges around grounding, false positives, scalability, and ethical misuse. Therefore, scalable agent safety requires not only better output filtering or stronger base models, but also explicit interfaces for tracing, calibrating, and constraining belief revision at runtime.

### 25. Remembering Is Not Enough: Refining Memories and Learning When to Use Them in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-27T05:12:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.36652
- Summary: Memory helps LLM-based multi-agent systems reuse experience, but stored advice can be flawed or applied in the wrong situation. Team-level success or failure alone cannot reliably show whether a memory needs correction or should not have been used. We propose DiscernMem, a training-free framework that improves both memory quality and memory use. To improve quality, Defect-Aware Memory Refinement (DMR) compares team executions with a single memory and with no memory, diagnoses rule defects, and tests repairs on current and earlier tasks to guard against losing previously useful behavior. To guide appropriate use, Boundary-Learning Meta-Memory (BLM) records each memory's past uses and effects, learning when its owner role should apply or avoid it based on task context and incoming messages. Together, these components help teams correct flawed experience while retaining useful rules that were applied incorrectly. Experiments with Qwen3-4B-Instruct-2507 on four benchmarks show that DiscernMem achieves the highest average score on AutoGen, CAMEL, and MacNet, exceeding the strongest reported baselines by 0.51-4.32 points. It leads on code generation and symbolic planning across all three systems, including a PDDL score of 37.71 versus 28.48 on CAMEL.

### 26. Compatibility and future-proof testing for multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-26T21:14:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.36289
- Summary: Independently developed autonomous agents, such as autonomous vehicles, must guarantee joint compatibility, such as safety and task-completion requirements, when they operate in a shared environment. Existing methods require a centrally designed specification, or interaction mechanism before any agent is deployed. However, such centralized design is unrealistic when agent designs are confidential to their developers, and it is not flexible enough to accommodate future agent designs. We study a bi-level structure in which a regulator coordinates developers by publishing seed agents, and each developer independently tests its agent to ensure that it is compatible with every seed-compatible agent, a property we call future-proofness. Under this structure, joint compatibility is guaranteed for any agents that are designed and tested independently, without any coordination with each other. In this work, we first formulate compatibility for general multi-agent systems and show why it is not trivially implied by seed-compatibility. We then characterize the future-proof agents as the closure of the seed and show that this closure is monotone in the seed. Finally, we study a class of executable tests that involve interaction with the seed alone, and we ask to what extent such tests can distinguish the future-proof agents.

### 27. RobotAgentBench: Towards Open-world Robot Autonomy
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-26T00:26:30+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.34649
- Summary: Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm for this transition, integrating task discovery, contextual reasoning, physical execution, and adaptive recovery into a closed interaction loop. However, existing benchmarks largely evaluate isolated capabilities, failing to capture the complexity of open-world robot autonomy. We introduce RobotAgentBench (RAB), a comprehensive benchmark for evaluating robot agents in realistic, open-world household environments. Through an agent-assisted, human-in-the-loop real-to-sim pipeline, RAB constructs 50 diverse household layouts with interactive objects and physically grounded tasks, encompassing 90 atomic tasks, 18 short-horizon tasks, 8 long-horizon tasks, and 4 open-ended scenarios. RAB provides a multi-level evaluation of robot agent capabilities: (1) task-level assessments systematically examine five complementary dimensions: task discovery, context reasoning, manipulation, failure recovery, and robustness; (2) scenario-level evaluation assesses how agents integrate these capabilities to autonomously fulfill high-level user needs. Furthermore, RAB enables systematic comparisons of standalone VLA/WAM models and diverse robot agent architectures under a unified planning-execution-verification framework. Extensive experiments reveal substantial gaps between manipulation and autonomy, demonstrate the advantages of agentic architectures and recursive self-improvement, and highlight the remaining challenges toward open-world robot autonomy.

### 28. Strategic Calibration in LLM Multi-Agent Systems: Audited Pivot Scoring for Truthful Elicitation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-24T15:18:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.33728
- Summary: In large language model (LLM)-based multi-agent systems, reported confidence increasingly determines the allocation of scarce downstream attention, computation, and decision influence. This makes reporting strategic: an agent may overstate the relevance of its contribution even when its underlying belief is well calibrated. Existing calibration methods largely assume passive reporting and therefore do not address strategic incentives created when confidence determines downstream allocation. We formulate strategic calibration as a reporting-layer incentive problem and propose the Audited Pivot Scoring Mechanism (APSM). APSM offsets platform-controlled allocation benefits, uses inverse-propensity-weighted sparse audits, charges the Clarke pivot externality, and applies a strictly proper score. Under the stated model assumptions, truthful reporting is the unique expected-utility best response. We also characterize approximate execution and the audit-variance trade-off. Calculator-free experiments show that LLM agents inflate confidence under Top-$K$ incentives. With a shared agent-local utility interface, LLM agents reduce distortion under both Compensated Proper Scoring (CPS) and APSM. CPS achieves higher exact allocation match, whereas APSM yields lower Brier loss and numerically fewer cutoff crossings. Experiments further show that APSM enlarges the utility margin against allocation-changing deviations by $1.93\times$ and improves robustness under approximate execution. These results support incentive-aware elicitation as a distinct layer for reliable multi-agent coordination.

### 29. CoEvolve: Counterfactual-Guided Co-Evolution of Memory and Collaboration in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-24T08:35:39+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.33539
  - Alt: https://arxiv.org/abs/2611.14980
- Summary: Large language model (LLM)-based multi-agent systems have demonstrated remarkable capabilities across diverse tasks. Yet their memory and collaboration architectures often remain static, constraining continued adaptation and improvement over time. Recent work addresses this limitation by evolving memory or collaboration based on interaction experience. However, updates to these interdependent components are not necessarily aligned: an evolved workflow may require experience that memory does not provide, while evolved memory may encode guidance that the workflow cannot use. To address this problem, we propose CoEvolve, a skill-centered framework for aligned memory--collaboration evolution. CoEvolve represents reusable local collaboration patterns as skills that link evolving collaboration decisions to their supporting memories. It further compares original and counterfactual trajectories to identify local evolution signals, which coordinate updates to the skill library, skill memory, and executor memories across rounds. Experiments on the ALFWorld and WebShop benchmarks confirm that CoEvolve achieves the best overall performance among the evaluated baselines, while ablation studies further validate the effectiveness of aligned co-evolution and counterfactual-guided evolution.

### 30. SCOPE: Scene-graph Construction Optimized by Plan Error-correction for Robot Long-term Planning Datasets
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-22T16:31:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.31518
- Summary: Task and Motion Planning (TAMP) stands as a fundamental challenge in robotics, essential for enabling autonomous agents to execute complex, long-horizon tasks in diverse environments. While Large Language Models (LLMs) introduce a new paradigm for TAMP by leveraging extensive common sense, their inherent reasoning limitations hinder direct application, and fine-tuning strategies to enhance these capabilities are currently bottlenecked by the scarcity of high-quality datasets. Existing automated generation methods often suffer from homogeneity, limiting model generalization, and unsolvability, where hallucinated scene graphs create physical mismatches with task goals. To address these issues, we propose Scene-graph Construction Optimized by Plan Error-correction (SCOPE), an automated framework designed to generate diverse and executable TAMP datasets. SCOPE incorporates multi-level diversity metrics to maximize the information entropy of scenarios. Crucially, it introduces a Plan Feedback Error-correction pipeline that utilizes planner execution failures as feedback signals to retroactively rectify logical inconsistencies in scene graphs, ensuring physical feasibility. Experimental results demonstrate that SCOPE exhibits greater robustness to erroneous scene graphs and generates higher-quality data. When utilized for LLM fine-tuning, SCOPE-generated data yield a downstream TAMP model that achieves an absolute 12.33% gain in success rate over its counterpart fine-tuned with data generated by DELTA, a state-of-the-art PDDL-based planner.
