# Blindspot Signals Report - 2026-10-10

- Source export: `/opt/apps/haier/exports/evolution_signals_20261010_020407.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 548
- Deduped/weighted signal clusters: 512
- Novel vs previous reports: 23
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-07T22:28:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.10962
- Summary: Agentic AI based on Large Language Model generalization capabilities offers a wide range of potential applications, including planning for embodied tasks. For example, embodied agents based on Foundation models can generate plausible plans in autonomous robotics scenarios. Due to limited context windows or hallucinatory phenomena in the next-token prediction formulation, behaviors may be generated without establishing whether the deployed robot and the observed environment actually support the requested operation, in what we call a "grounding failure". Thanks to the recent improvements in reasoning capabilities of foundation models, autonomous robot behavior generation problem can be formulated as a code generation problem. We present iAm.md, a Markdown standard and generation framework, that allows anchoring this process in complementary forms of deployment evidence. Through open-vocabulary semantic mapping, we combine local vision-language detections and object segmentation and refer them to persistent object records in this intermediate standardized representation, allowing agentic introspection. We then study this new technique on a simulated TIAGo, on navigation-and-manipulation tasks, showing how this standardized representation jointly supports skill self-assessment and executable task generalization.

### 2. RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-08T15:49:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.12185
- Summary: Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors. However, recovery methods based on repeated vision-language reasoning or iterative online optimization can incur substantial latency, delaying intervention. To address these challenges, we introduce RESETTLE(Robotic rEcovery through diSagrEement-Triggered reTrievaL and Efficient Corrective Control), a model-agnostic framework that provides computationally efficient recovery at the action-execution interface of frozen robot policies. RESETTLE triggers recovery when two action proposals independently sampled under identical conditioning persistently disagree. It retrieves a same-task demonstration reference using an adapted V-JEPA encoder and combines a state-servo prior with a guarded visual residual to execute one corrective action without online trajectory optimization or additional vision-language reasoning, then returns control to the base policy. Across six base policies in simulation, RESETTLE achieves up to 8.70%, 6.28%, and 6.83% absolute success-rate gains on LIBERO-Plus, Meta-World, and RoboCasa Tabletop, respectively, with further improvements on four real-world tasks using two policies. In QwenPI-based comparisons, its monitoring-and-recovery computation latency is 74.04%--93.57% lower than VoLoAgent's monitoring-and-planning latency for grasp and place tool calls. It also raises Harness VLA's LIBERO-Pro Swap success from 42% to 50%, demonstrating compatibility with high-level agentic planning. Code available at: https://github.com/JIA-Lab-research/RESETTLE

### 3. Error-Propagation Modeling for Failure Attribution in LLM-Based Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-08T09:44:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.11600
- Summary: LLM-based multi-agent systems (MASs) are increasingly used to solve complex tasks through coordinated reasoning, tool use, and interaction with external resources. However, attributing failures in such systems remains challenging because the observed outcome often does not directly reveal the error responsible for the failed execution. In this work, the attribution target is the decisive error, defined as the agent--step pair whose correction would recover the failed execution. Existing approaches largely identify suspicious steps without explicitly modeling how errors propagate across interactions or persist in unresolved loops, making decisive errors difficult to distinguish from downstream failure symptoms. We propose \textbf{E}rror-Propagation \textbf{M}odeling for \textbf{F}ailure \textbf{A}ttribution (\textbf{EMFA}). EMFA constructs a structured representation of the failed trajectory, models both cascading propagation and persistent interaction loops, and uses propagation-aware candidate screening followed by counterfactual verification to identify the decisive agent--step pair. On the Who\&When benchmark, EMFA achieves state-of-the-art step-level attribution accuracy and remains competitive at the agent level. It improves the previous best step-level results by 3.45 and 4.40 percentage points on the Hand-Crafted and Algorithm-Generated subsets, respectively.

### 4. EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-07T17:48:02+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.10498
- Summary: Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolving harnesses use robot trials inefficiently when deciding which code and skill changes to pursue. We introduce EmbodiedRSI, a self-evolving agentic harness that autonomously decides where to explore next and turns the resulting physical interaction into improved code and skills. EmbodiedRSI realizes this through a Fast-Slow Dual-System Architecture, in which competing code and skill hypotheses are maintained in a Hypothesis Graph. Value-of-Information Experiment Selection chooses physical experiments that can distinguish these hypotheses. Their outcomes guide Code-Skill Co-Evolution. The Slow System builds Hierarchical Memory, and Reward-Grounded Memory Learning selects effective memory according to their value for later Fast-System improvement. On RoboCasa365, EmbodiedRSI reaches 77.0% overall success and 71.3% on Composite-Unseen, compared with 40.1% for the best baseline. EmbodiedRSI also reaches 86.8% overall success on LIBERO-Pro. Beyond benchmark performance, EmbodiedRSI transfers zero-shot to real-world robot, achieving 71.3% overall success across multiple challenging tasks.

### 5. HGP:An on-device personalized agent memory via hybrid graph storage
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-07T13:37:38+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.10071
- Summary: LLM-based agents face challenges in personalized interactive tasks due to heterogeneous, multi-typed, and implicitly constrained long-term traces. Existing memory mechanisms struggle with accurate routing and retrieval, especially on-device where personalization is critical. Most methods use single-vector representations, blurring type distinctions and relational structure. We propose HGP, a hybrid graph memory framework. HGP employs a lightweight self-enhancement classifier for personalized memory routing and constructs episodic, semantic, and procedural memories as graphs. It also extracts working memory as a state trajectory to capture current state and implicit constraints, ensuring reliable decision-making. The classifier reduces large-model calls, enabling on-device deployment, while graph storage enables accurate retrieval and incremental user profile refinement. Experiments on two benchmarks show that on PAL-Set solution selection, HGP achieves an S-score of 35.58, nearly 7 points above the strongest baseline. Code and data are at https://github.com/Ouan6/HGP-.git.

### 6. Marinela Profi, SAS: On governing autonomous AI agents - AI News
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-08T14:56:27+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMioAFBVV95cUxNVHFta3NpVTRsWFBTNjFHRnJxbG1HLXNYaFo5T2dMSFgwM1MyQkdteXEybU1vTkhEOXRhaFh2a1JNVE5CcmQyd2NaQmVXX2JiWERpZ1JiWmJiRWZSTUxDYWh5emhiVDkzWlVDZ3JOMDUtR1ItRUlxY1hNZHlZMTV4UW15VXVYV3hDSmR0VThQbFpzT1phRGFHSXZ1VHFYQXpI?oc=5
- Summary: Marinela Profi, SAS: On governing autonomous AI agents&nbsp;&nbsp;AI News

### 7. Evaluating Autonomous LLM Agents Across Molecular Prediction and Optimization Benchmarks
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-08T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.01.755314
- Summary: Large language model (LLM) agents are increasingly capable of carrying out autonomous computational research, but it remains unclear whether they can develop molecular modeling methods that compete with strong human-developed approaches. Here, we evaluate autonomous method development across four settings: Therapeutics Data Commons (TDC) ADMET tasks, the OpenADMET ExpansionRx Challenge, the activity prediction track of the OpenADMET PXR Induction Challenge, and the Practical Molecular Optimization (PMO) benchmark. Agents followed the prescribed data splits, metrics, and evaluation protocols for each benchmark. On TDC, the best agent-developed score across configurations improved on the leaderboard reference on 18 of 21 tasks and on the combined leaderboard and peer-reviewed reference on 17, while individual Codex configurations improved on the combined reference on 13 tasks. On ExpansionRx, five-agent and single-agent Codex configurations achieved overall scores corresponding to fourth and sixth place relative to the published final leaderboard, with the five-agent configuration reaching top-five performance on seven of nine endpoints. On PXR, five-agent Codex achieved a mean absolute error slightly outperforming the best published challenge entry. On PMO, five-agent Codex developed a molecular optimizer that outperformed existing methods evaluated under the benchmark's standard setup; other methods obtained higher reported scores under modified conditions, including additional molecular pretraining data or a different oracle-call budget. Together, these results show that current LLM agents can autonomously develop high-performing molecular prediction and optimization methods across substantially different drug-discovery settings, in several cases matching or exceeding leading human-developed approaches.

### 8. Dietary magnesium supplement enhances memory through Hippo signaling
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-08T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.02.756214
- Summary: Dietary magnesium (Mg2+) supplement enhances memory in mammals and Drosophila, but whether and how Mg2+ changes molecular states of neurons, remains unknown. Here we used single-cell RNA sequencing to map cell-type specific transcriptional responses to memory-enhancing dietary Mg2+. These analyses revealed changes in Hippo-pathway gene expression in memory-relevant {beta} Kenyon Cells (KCs) of the mushroom bodies. Targeted knock-down of Merlin, hippo (hpo) and warts demonstrated requirement in {beta} KCs for Mg2+-enhanced, but not baseline memory. Further study of Hippo signaling identified Yorkie (yki) transcriptional coactivator and DNA-binding partner Scalloped (sd) to be required for baseline and Mg2+-enhanced memory. Moreover, releasing Yki::Sd of inhibition from Tondu-domain containing growth inhibitor (Tgi) specifically in {beta} KCs enhanced memory, independent of diet. Analyses of Yki::Sd target genes identified several required in {beta} KCs for baseline memory, including crb and Glut1 which are also Mg2+-induced in a Hippo-dependent manner in {beta} KCs. These genes suggest that aiding the metabolic demands of long-term memory and facilitating structural neuronal plasticity are key mediators of Mg2+-induced memory enhancement. We propose pharmacological enhancement of Sd-dependent transcription, and activity of particular Sd-target genes may have therapeutic potential for memory disorders.

### 9. On-Demand Robotic Assembly via Differentiable Geometric Part Repair
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-07T09:57:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.09777
- Summary: Transitioning from a digital design to a robotic assembly process currently requires months of expert manual tuning to reconcile part geometries with robotic constraints. This paper presents an end-to-end, autonomous pipeline for the design and physical construction of bespoke wooden assemblies. A generative AI agent translates user prompts into initial 3D geometries, balancing the visual fidelity of the design with select physical constraints. The assemblability of the design is further improved by a gradient-based repair stage that backpropagates through a graph attention network surrogate to adjust component geometries. In addition to correcting for disjointed and overlapping components, we demonstrate hardware-specific corrections, differentiably optimizing the geometry of components to enable robot screwdriving for 86.7% of 60 novel natural language inputs, significantly outperforming prior work by a factor of ten. For ten of the structures, we physically demonstrate assemblability with two UR5e robots. This work marks a meaningful step toward on-demand robotic manufacturing, enabling the rapid production of customized, low-volume goods.

### 10. Careful Judge: Safe and Efficient Human-AI Collaborative Decision Making
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-06T19:44:15+00:00
- Primary source: arxiv
- Focus/tech: robotics, AI decision delegation / robotics
- URL: https://arxiv.org/abs/2610.09043
- Summary: In human-AI collaborative decision making, human review can prevent unsafe AI decisions, but each human judgment is costly. Treating human intervention after AI abstention as a one-off fallback misses the opportunity to improve future AI decisions for greater automation, yet AI adaptively learning from selectively queried human feedback breaks safety guardrails calibrated for old models. We approach this challenge with CARE---calibrated adaptive rectification and escalation---an end-to-end pipeline that combines AI models and human reviewers to guarantee safe, human-aligned decisions, while continuously learning from human feedback to achieve greater automation with fewer human queries. CARE is principled, general, modular, and works with any black-box AI model. Our novel adaptive calibration module guarantees risk control at every time step for any rectification module. We further show how CARE improves query efficiency when the AI model is well trained and the human-AI misalignment has a clear structure. Experiments on four safety-critical real-world datasets spanning driving, language, and robotics demonstrate that CARE achieves human-aligned decisions while reducing human queries by 25-81% relative to baselines.

### 11. Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-06T18:03:09+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.08933
- Summary: Deep-space crews cannot rely on real-time ground support for urgent off-nominal events. Initial alerts may underdetermine cause, while discriminating evidence may reside in crew observations or at locations that are unsafe, costly, or unavailable for crew inspection. We present an evidence-driven architecture for human-agent-robot teaming in Earth-independent anomaly triage. Agentic AI is treated as a stateful coordinator over bounded, inspectable services rather than as a fully autonomous vehicle controller. A triage state manager maintains hypotheses, evidence provenance, uncertainty, operational context, and tool status; a crew-facing embodied agent elicits observations and explains assessment changes; and a mobile robot acquires targeted, localized evidence. Typed interfaces separate dialogue and orchestration from monitoring, robot command, context retrieval, and safety-critical control. Two scenarios illustrate the architecture: a crewed deep-space mission based on an actual ISS ammonia false alarm, where suspected contamination restricts crew access, and a power-interface anomaly at a crewed lunar base, where robotic inspection distinguishes a local connector fault from other causes ambiguous in remote telemetry. Our main contribution is an authority-bounded closed evidence-loop architecture, exercised in a hardware-in-the-loop integration prototype using Reachy Mini and an Innate MARS mobile robot.

### 12. EXCLUSIVE: OpenAI agents hijacked German website in previously undisclosed AI breakout this spring - Reuters
- Weighted score: 0.08
- Deep score: 0
- Coverage: 2 sources (hackernews, google_news)
- Date: 2026-09-04T10:30:57+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/
  - Alt: https://news.google.com/rss/articles/CBMixAFBVV95cUxQb0lsYkxySy1tYUVZRnlHQmN5Q1loNW14dl9oYWZ4UFpWX0N6TGNMdUdTSFRHMDBsMzMwazV2RkFkM01jTGFvbHpJUTk4ZVNzVGZJc3FtaWlHMGViMEp2ZHFUcEZuNmF3MUd3UjF3eEc4ZC04MDEwWmp3RlYzSmFPZTNLTVlpTURsdENEdE1FMlNzRjc1TzFQd2tSSUNoQmtxRF9DQUVIR0Ftams3Zm5KUFZ1dHhrZEtKUFlSQUFyeVozSmxk?oc=5
- Summary: No summary.

### 13. Anthropic can’t reliably control its AI agents. It’s cutting off its internal evals from the live internet instead
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-10T00:18:32+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/
- Summary: Anthropic said it "turned off live internet access" for "all our internal evaluations" until further notice.

### 14. Amazon and others are done keeping data center deals secret. Is it enough to build trust?
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-09T16:56:42+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/video/amazon-and-others-are-done-keeping-data-center-deals-secret-is-it-enough-to-build-trust/
- Summary: Amazon says it will&#160;stop using NDAs&#160;when negotiating data center deals with local governments, following&#160;a&#160;similar move from Microsoft&#160;earlier this year. Secrecy has fueled community backlash against AI infrastructure, with opposition leading to&#160;hundreds of&#160;proposed and enacted moratoriums from New York to San Francisco. Meanwhile, a wave of startups is betting that consumers will hand AI agents access [&#8230;]

### 15. Amazon drops data center NDAs, and AI agents want your credit card
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-09T16:53:02+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/podcast/amazon-drops-data-center-ndas-and-ai-agents-want-your-credit-card/
- Summary: Amazon says it will&#160;stop using NDAs&#160;when negotiating data center deals with local governments, following&#160;a&#160;similar move from Microsoft&#160;earlier this year. Secrecy has fueled community backlash against AI infrastructure, with opposition leading to&#160;hundreds of&#160;proposed and enacted moratoriums from New York to San Francisco. Meanwhile, a wave of startups is betting that consumers will hand AI agents access [&#8230;]

### 16. Show HN: Let your AI agents paint big arrows, boxes and text on your screen
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-09T11:03:48+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/franzenzenhofer/big-arrow-on-the-screen
- Summary: No summary.

### 17. OpenPilot
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-09T05:53:51+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/openpilot
- Summary: <p> Open-source desktop AI agent for any model you choose </p> <p> <a href="https://www.producthunt.com/products/openpilot?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1274507?app_id=339">Link</a> </p>

### 18. OpenVids
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-08T19:58:50+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/openvids
- Summary: <p> Open-source video editor you run by chatting with AI agents </p> <p> <a href="https://www.producthunt.com/products/openvids?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1274179?app_id=339">Link</a> </p>

### 19. Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-07T17:37:20+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.10479
- Summary: A simulation of a real robot workspace must preserve task-relevant interactions, while policies developed in it must operate on observations available to the real robot. Yet scene reconstruction and policy development are often treated separately. We present Agentic Real-to-Sim-to-Real (Agentic RSR), a framework that links scene reconstruction, policy development, and real-robot execution through the same manipulation task. Given a workspace video, a task description, and a known robot model, an agent recovers metric scale, iteratively refines the scene using visual feedback, and checks task-relevant interactions in MuJoCo. A coding agent then develops an executable policy, progressing from privileged object poses to visual observations and randomized simulation. The policy can interleave multiple observations and actions within one invocation, while the agent uses execution feedback to continue, retry, or revise its approach. A shared task-level interface carries the policy and accumulated experience to the real robot, where fresh observations and safety checks guide execution. Across 18 reconstructed scenes involving two robots, the mean four-view Depth MAE against reference depth estimates is 0.1057 m, the mean Lab $ΔE_{76}$ is 11.04, and the mean grayscale SSIM is 0.6990. In real-robot experiments, the aggregate task success rate reaches 80% of the simulation task success rate, indicating substantial retention of simulated performance on hardware. Code and reconstructed scene data will be made publicly available.

### 20. OpenCharm
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-07T15:54:37+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/opencharm
- Summary: <p> Open-source body for the AI agent you already run </p> <p> <a href="https://www.producthunt.com/products/opencharm?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1272865?app_id=339">Link</a> </p>

### 21. Ambiguous Workspace
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-07T05:46:52+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/ambiguous-workspace
- Summary: <p> 18 productivity apps built for AI agents and humans </p> <p> <a href="https://www.producthunt.com/products/ambiguous-workspace?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1272323?app_id=339">Link</a> </p>

### 22. Co-Evolving Robot Orchestrators and Policies through Deployment
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-06T23:44:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.09228
- Summary: Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment. Agentic robot systems complement the policy with a vision-language model (VLM) orchestrator that learns when to call the policy, how to instruct it, and when to use scripted skills instead. However, because the harness is built around a frozen policy that has limited language steerability, the orchestrator can avoid the policy's failures but never overcome them. The policy becomes the bottleneck of the whole system. Fine-tuning the policy can remove this bottleneck, but updating it alone decouples it from an orchestrator tuned to its old behavior. We propose Robo-COP, in which the orchestrator and policy co-evolve during deployment. Robo-COP curates skill demonstrations from its own executions, fine-tunes the policy when this data can address recurring failures, and adopts each new policy only after it improves the skills it was trained for. Across ten simulated RoboLab tasks, Robo-COP raises mean held-out success from 64.8% to 73.8% over the same harness with a frozen policy, while fine-tuning on a fixed schedule without verification reaches only 65.8%. On three real-world tasks, Robo-COP raises held-out success from 38.3% to 50.0%. Robo-COP turns deployment into a self-improving flywheel in which robots learn by doing, with each improvement in execution producing better data for the next round of learning. Videos and code are available at https://robo-cop.pages.dev/.

### 23. Cakie
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-06T01:16:50+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/cakie-2
- Summary: <p> Turn screen recordings into prompts for AI agents </p> <p> <a href="https://www.producthunt.com/products/cakie-2?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1271093?app_id=339">Link</a> </p>

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

### 2. TRACEDD: A Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-09-18T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.09.12.751167
- Summary: Drug discovery depends on coordinated decisions across target validation, structure analysis, molecular design, developability assessment and synthetic feasibility, but current computational methods often operate as disconnected tools. Here, we introduce TRACEDD (Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design), a framework that makes three primary contributions: (1) It establishes a 'tool-first' multi agentic architecture where LLMs orchestrate validated computational tools rather than replace them, ensuring scientific rigor. (2) It implements a multi-agent system that mirrors expert discovery teams, enabling transparent and traceable decision-making through a Reason-Act-Observe loop. (3) It demonstrates an end-to-end workflow, from target validation to synthesis planning, that adaptively handles real-world data variability, such as the absence of experimental structures. The framework decomposes discovery into specialized agents for target validation, druggability assessment, molecular generation, lead optimization, ADMET evaluation, literature evidence integration and retrosynthesis, all operating through a Reason Act Observe workflow. Using JAK2 as a representative case, we show that the system can retrieve experimental protein structures, invoke AlphaFold when structures are unavailable, identify druggable pockets and perform de novo molecular generation. Known JAK2 inhibitors are used to define design hypotheses and guide reinforcement learning-based molecular generation, with docking scores/predicted pIC50 and other physicochemical/ADMET properties serving as reward and prioritization signals. The framework demonstrates a tool-first, reasoning-driven approach in which each major decision is linked to explicit tool invocation, intermediate evidence. By combining agentic orchestration with domain-specific computational tools, the system supports transparent, adaptable and human-verifiable molecular design workflows, providing a …

### 3. Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-09-10T08:25:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.11225
- Summary: Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

### 4. PrivMeSA: Privacy-Aware Self-Evolving Multi-Agent System for Medicine via Local-Remote LLM Collaboration
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-29T19:47:38+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38458
  - Alt: https://arxiv.org/abs/2609.37953
  - Alt: https://arxiv.org/abs/2609.19680
- Summary: Clinical large language model (LLM) agents deployed locally can consult more capable remote models, but doing so risks exposing patient information. Privacy-conscious delegation places disclosure decisions with a local agent, yet removing explicit identifiers is insufficient: quasi-identifiers can accumulate across multi-turn consultations and repeated patient visits to enable re-identification. We introduce PrivMeSA, a privacy-aware self-evolving multi-agent system that learns to control disclosure and retains remote expertise for local reuse. A local agent manages each encounter and consults remote specialists that may request additional information. Reinforcement learning balances task accuracy against direct disclosure and registry-based re-identification risk, with privacy evaluated over the complete outbound transcript of each encounter. A local lesson memory distills completed consultations into generalized clinical guidance and retrieves relevant lessons before transmission, allowing subsequent cases to reuse expertise without another remote exchange. Memory grows without additional outcome labels or parameter updates. On an emergency-department benchmark built from MIMIC-IV-ED records, PrivMeSA improves mean task accuracy over delegation by up to 15.8 percentage points. In the same setting, PrivMeSA reduces the disclosure of personal details from 98.0% to 0.2% of cases and the share of cases in which the patient can be narrowed to ten or fewer registry patients from 74% to 0%.

### 5. World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T15:19:39+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.29964
- Summary: General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected automatically from the scene geometry, present the scene around the current interaction. Action rehearsal turns each action into an editable proposal that the agent, alone or through an Imagination Agent, previews and revises against planning feedback before execution. In-view correction closes the loop between observation, rehearsal, and low-level execution, letting the agent remove residual offsets in the view where it observes them. Through the same workspace, WAA acquires embodied procedural knowledge in two ways: it evolves multimodal skills from expert videos and human teaching under evidence-based review and consults them through a Skill Agent, and its interaction traces train smaller VLMs to pilot the same harness. On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art 75.6% average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone; the same skills remain effective on robosuite without further learning. Fine-tuning Qwen3.5-9B on harness traces raises its out-of-domain success from 1.7% to 43.3%.

### 6. RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T11:22:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.29394
- Summary: General-purpose robot agents must learn from experience, transfer to new tasks, and act efficiently. Code as Policies (CaP) methods generate and repair programs at runtime, incurring latency and entangling reusable mechanisms with task-specific decisions. We introduce RACaP, an agentic framework that moves coding to evolution and uses a Reasoning-and-Acting (ReAct) loop to call frozen, typed Policy APIs at deployment. A two-phase strategy combines capability curriculum learning with autonomous self-evolution to improve the APIs, the ReAct harness, and experience memory. The APIs encode reusable physical mechanisms while exposing arguments for runtime adaptation. ReAct combines task-specific working memory, long-term experience memory, and visual feedback to select actions, verify outcomes, and recover from failures without modifying source code. RACaP achieves 54.4% success on LIBERO-90, 45.0% on zero-shot LIBERO-PRO, and 46.0% on LIBERO-Long, compared with at most 4.0% for CaP baselines on long-horizon tasks. On LIBERO-PRO, it achieves 2.5 times the success rate of CaP baselines and a 1.9-fold speedup in median policy time. For efficient on-robot deployment, rejection-sampled fine-tuning distills GPT-5.6 ReAct decisions into Qwen3-VL-8B-Instruct, yielding a 13.2-fold per-decision inference speedup and reducing repeated physical calls from 16 to 4. These results show that separating reusable code from runtime decisions supports continued evolution, effective transfer, and efficient long-horizon control.

### 7. Agent Memory with Episodic Retrieval for Financial Decision-Making
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-23T20:32:54+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.28771
- Summary: Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their applicability to the demands of trading in complicated settings. To address these gaps, we introduce META (Memory Enhanced Trading Agent), the first RAG-like episodic-memory-augmented multi-agent framework for financial decision making. META integrates a family of specialized indicator agents (e.g., Trend, MACD, Stochastic, RSI, SMA, AVWAP, Heikin-Ashi) with a Decision Agent that fuses their reports, and a Memory module that retrieves and updates past trading episodes encoded as market state embeddings with outcomes and reflections. By recalling relevant experiences and adaptively reweighting signals under similar market regimes, META achieves improved directional accuracy and robustness under short-horizon evaluation. Our results demonstrate that episodic memory provides a powerful mechanism for regime-aware, interpretable, and low-latency decision-making in trading and decision making. The code of this project is released on GitHub.

### 8. Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-21T01:43:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.23986
- Summary: Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \textbf{\method}, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6$\times$ speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.

### 9. EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T07:41:56+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15161
- Summary: Large language model (LLM) driven multi-agent systems have shown promise in complex clinical reasoning, yet existing approaches rely on static strategies and lack persistent clinical memory, preventing self-evolving from prior diagnostic successes and failures. We present EMR, a self-evolving medical multi-agent system via Experience Mining and Reuse. EMR introduces a hierarchical clinical experience library that organizes accumulated knowledge into three levels: clinical principles, diagnostic patterns, and representative cases. During inference, EMR emulates multidisciplinary consultation: a planner agent coordinates domain-specific department agents for specialized reasoning, while a summary agent synthesizes their analyses into a final decision. Critically, EMR automatically extracts correct diagnostic insights and failure-related warnings from multi-agent reasoning trajectories, incrementally updating the experience library to guide future cases. Experiments on medical reasoning benchmarks demonstrate that EMR consistently outperforms state-of-the-art medical multi-agent baselines. Further analysis reveals that the hierarchical experience enables cross-specialty generalization and transfer across diverse LLM backbones, offering a scalable and in

### 10. BusMA: A Bus Communication Substrate for Multi-Agent Systems
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

### 11. Enhancing Human Mobility Prediction with Spatially Aware LLM-based Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-13T01:41:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.14227
- Summary: Predicting a user's next POI is a task in human mobility modeling, yet LLM-based approaches focus on semantic reasoning from previous mobility records, while neglecting real-world spatial context. However, human mobility is inherently shaped by spatial cognition, including geographic distance and neighborhood context. This issue is further compounded by prior evidence that LLMs often struggle with spatial reasoning tasks, including distance estimation and geographically biased prediction. To address these limitations, we propose our framework, a multi-agent LLM framework that decomposes next-POI prediction into three stages: Firstly, a Pattern Extraction Agent that captures temporal and categorical mobility patterns from trajectory history; Secondly, a Spatial Reasoning Agent that structures candidate activity choices by combining behavioral preferences with real-world spatial constraints, including geographic distance, road network distance, and neighborhood affiliation; and Thirdly, a Decision Synthesis Agent that integrates behavioral patterns and spatial reasoning for final prediction. Experiments on the NYC benchmark dataset with two LLM backbones show improvements over baseline methods, with up to 493% Hit@1 improvement and 37% relative improvement in Hit@5. Ablations show that combining neighborhood affiliation with distance-based features generally outperforms distance-only settings, and that the Spatial Reasoning Agent plays a crucial role in final prediction by integrating behavioral preferences with real-world spatial constraints, especially for smaller models. Overall, the results highlight the importance of spatial reasoning in mobility prediction. Accurate next-POI prediction requires combining behavioral patterns with explicit real-world spatial constraints, and multi-agent decomposition provides an effective structure for organizing these forms of context.

### 12. iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-07T22:28:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.10962
- Summary: Agentic AI based on Large Language Model generalization capabilities offers a wide range of potential applications, including planning for embodied tasks. For example, embodied agents based on Foundation models can generate plausible plans in autonomous robotics scenarios. Due to limited context windows or hallucinatory phenomena in the next-token prediction formulation, behaviors may be generated without establishing whether the deployed robot and the observed environment actually support the requested operation, in what we call a "grounding failure". Thanks to the recent improvements in reasoning capabilities of foundation models, autonomous robot behavior generation problem can be formulated as a code generation problem. We present iAm.md, a Markdown standard and generation framework, that allows anchoring this process in complementary forms of deployment evidence. Through open-vocabulary semantic mapping, we combine local vision-language detections and object segmentation and refer them to persistent object records in this intermediate standardized representation, allowing agentic introspection. We then study this new technique on a simulated TIAGo, on navigation-and-manipulation tasks, showing how this standardized representation jointly supports skill self-assessment and executable task generalization.

### 13. Beyond Corrected Memory: Execution Consistency in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-06T10:29:41+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.08101
- Summary: Shared memory coordinates agents' actions, but correct records do not establish that those actions satisfy task requirements. Memory governance and failure diagnosis regulate or inspect recorded information; they do not by themselves establish whether it is sufficient to judge task duties. We define execution consistency through duties governing state use, information handoffs, and final-state agreement, with explicit evidence conditions for judging fulfillment. Our core claim is that identical retained records can correspond to compliant and violating executions under the same task rule. Controlled removal of evidence such as receipt, action dependence, or response validity leaves 82.4% of opposite-label pairs indistinguishable; restoration separates 97.9% of the merged pairs. Natural-log annotations identify the defined violations in actual executions. However, existing logs do not always explicitly represent the execution relationships needed for these judgments. To assess the definition's practical value, we use CAVERT, a framework for consistency diagnosis and recovery, to extract supported relationships from logs and apply these criteria. It consistently outperforms contract-prompted LLM and rule-based baselines in diagnosis across all 12 benchmark-executor settings. Under the same gate and executor limits, it also outperforms rule-guided recovery in all four evaluated environments. These findings identify execution evidence that agent-memory and execution interfaces should preserve for reliable judgment.

### 14. OOPMAS: Object-Oriented Multi-Agent Systems for Query-Level Workflow Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-06T05:31:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.07787
- Summary: Multi-agent systems (MAS) powered by large language models have shown strong performance across code generation, mathematical reasoning, and question answering. However, existing methods for automating MAS design mostly operate at the task level, producing a single fixed workflow per benchmark that is applied uniformly to all queries. This assumption fails under realistic conditions. Query difficulty varies widely within a task, and real-world workloads mix heterogeneous task types. We introduce OOPMAS, a training-free framework that generates both the agent set and the coordination workflow at the granularity of individual queries. Agents are represented as object-oriented class definitions with dedicated roles, tools, and persistent state, and workflows are expressed as executable main functions over these agent objects. A dynamic skill library accumulates structured lessons from execution feedback across optimization rounds, enabling in-context improvement without any gradient updates or fine-tuning. On a mixed-task benchmark of queries spanning code, math, and QA, OOPMAS achieves 89.6% accuracy, outperforming the strongest baseline by 18.1 percentage points. A model-swap study across four LLM backbones shows consistent scaling, reaching 92.4% with the strongest model.

### 15. EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-02T14:43:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.03394
- Summary: Emerging multi-agent LLMs demand privacy-preserving edge deployment, yet current inference systems struggle with these collaborative workflows. Specifically, the memory-bound decode phase causes severe bus contention on unified memory architectures (UMA), paralyzing naive CPU-GPU co-execution. Furthermore, speculative decoding in multi-agent workloads faces extreme variance in drafting difficulty, alternating between complex reasoning and predictable structured generation. Compounded by frequent tool-induced stalls, this highly fragmented execution severely underutilizes hardware and defeats traditional static batching. We present EdgeAgent, a cross-layer inference system explicitly co-designed for edge UMA and multi-agent workloads. At the micro-architectural level, it bypasses rigid graph-compiler constraints to enable zero-copy UMA-aware tensor parallelism, utilizing asymmetric memory layouts to fully saturate both CPU and GPU compute units. At the scheduling level, it dynamically allocates draft budgets based on real-time sequence predictability to bound bandwidth waste. Concurrently, an asynchronous suspend-and-yield mechanism actively evicts stalled agents, ensuring continuous hardware saturation during unpredictable tool invocations. Extensive evaluations on an Apple M4 SoC demonstrate that the UMA-aware execution alone contributes a 1.29x speedup over batched speculative decoding. Adding the agent-aware scheduling lifts the full EdgeAgent system to a 1.77x speedup under extreme tool-use latencies.

### 16. From Pixels to Policy: A Multi-Agent System for Intervention and Geo-Spatial Decision Support
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T15:29:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2610.01870
- Summary: Urban environments are shaped by design choices with long-term implications for health, safety, and quality of life, yet evaluating proposed interventions remains costly, time-consuming, and often impractical. Existing geospatial vision methods largely focus on monitoring urban indicators from aerial and street-view imagery, rather than proposing interventions and estimating their effects on such indicators. Moving beyond recognition, we introduce the problem of discovering interventions that improve target indicators for a given aerial or street-view image. We argue that a black-box indicator model, combined with a generative editing model, can serve as an implicit digital twin for testing intervention hypotheses. We present VIDA-Geo , a multi-agent system that explores this intervention space by coordinating segmentation, diffusion-based inpainting, and indicator scoring models to produce interventions that are both perceptually realistic and aligned with real-world policies. We evaluate our system on 8 indicators across aerial and street-view imagery, measuring changes in factors such as perceived safety and greenery. Our approach outperforms existing baselines in many cases, achieving up to 2X higher perceptual quality and policy alignment scores. Finally, our model provides users with multiple candidate interventions, supporting an expert city-planner-in-the-loop workflow.

### 17. MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T05:42:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, human augmentation / robotics
- URL: https://arxiv.org/abs/2610.01102
- Summary: Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control, decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward engineering or task-specific design. We propose MASkillBlender, a general multi-agent reinforcement learning framework to achieve decentralized multi-humanoid whole-body coordination. By learning a shared decentralized high-level policy over reusable pre-trained single-humanoid skills, MASkillBlender enables coordinated behaviors using only task-level rewards, without requiring task-specific motion references. To improve learning efficiency, we further introduce a permutation-based data augmentation strategy for homogeneous multi-humanoid systems, and theoretically show that the permuted samples preserve the policy-gradient direction of the original samples under the homogeneous Markov game formulation. We evaluate MASkillBlender on multiple multi-humanoid coordination tasks across two humanoid embodiments. Simulation results demonstrate that the proposed framework consistently achieves strong task performance and enables coordinated behaviors across different tasks and humanoid embodiments.

### 18. Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T23:36:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38660
- Summary: Long-form subtitle translation requires reasoning over discourse and cultural context spanning episodes or entire series, while maintaining consistent terminology and style. Existing single-LLM methods are largely sentence-level, and multi-agent systems often use static workflows that do not adapt to scene complexity or production context. We propose SMART, a Self-evolving Multi-Agent system for long-foRm subtitle Translation. During test-time training, SMART builds persistent series-level memory and translates a subset of sentences through a dynamic router and Mixture-of-Agents layer with tools for terminology verification, subtitle constraint validation, and contextual retrieval. A judge-refiner loop scores candidates and uses textual critiques to update agent prompts and routing policies without retraining the underlying LLMs. During test-time inference, the evolved configuration translates the remaining series. We also introduce Subtitle Arena, covering 14 genres, 2--198 episodes per series, production years 1959--2023, and 15 target locales, together with SubMQM, a subtitle-adapted MQM framework with seven dimensions and 19 error categories. SMART achieves the best overall MQM score in all 15 Subtitle Arena directions, reducing average penalty by 6.9% over the strongest competing agent system. On the public MuSC benchmark, SMART obtains the best model result across all four language pairs and also achieves the best human-evaluation result, with an overall score of 4.50/5.

### 19. PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T20:10:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38482
- Summary: Existing architectures for LLM-based multi-agent systems (MAS) cannot reliably and efficiently solve multi-step tasks at scale: they struggle to support large numbers of agents and concurrent tasks, tolerate failures, govern agent interactions, and accommodate the diverse planning and execution patterns different tasks require. We present PANDA, a decentralized architecture that connects a large collective of heterogeneous, independently administered agents, letting them discover each other's capabilities and self-organize into small specialized teams per task. PANDA scales by decoupling collective communication from team communication, allowing agents to participate in multiple teams simultaneously, load-balancing tasks across the collective, and scheduling concurrent work within each agent. PANDA further separates the underlying architecture from the orchestration strategy, supporting three planning and execution patterns (star, chain, and mesh) that can be selected according to the structure and requirements of each task. PANDA detects infrastructure and orchestration failures and recovers affected tasks by dynamically replanning around failed components. Finally, to provide governance without a centralized service that would limit scalability, PANDA uses a web-of-trust model to constrain agent interactions to established trust relationships. We evaluate PANDA on the HotPotQA benchmark, demonstrating that it scales to thousands of agents, assembles teams in milliseconds, matches state-of-the-art accuracy at up to 8x the efficiency, and sustains 100% task completion under faults where existing systems fail.

### 20. LLM-Based Multi-Agent Systems over Wireless Networks: A Joint Agent--Network Design Perspective
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T09:19:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.37094
- Summary: As large language models (LLMs) evolve from standalone models into collaborative agents embedded in physical systems, their reasoning and execution are increasingly distributed across wireless edge nodes. In this setting, wireless networks are experiencing a paradigm shift from only providing data connectivity to supporting the multi-agent reasoning workflow itself. The task performance of such network-constrained LLM-based multi-agent systems (MASs) is jointly affected by the multi-agent reasoning dependencies as well as the underlying network connectivity and edge resources. This coupling gives rise to various technical challenges, including the metric misalignment and message redundancy, state inconsistency and topology mismatch, as well as resource limitation and trust discontinuity. To address these challenges, this article develops a novel joint agent--network design perspective that coordinates decisions on both sides of the system. Specifically, we present the joint design of agent--interaction scheduling and resource allocation, the message selection-transmission co-design, as well as the joint agent--network topology design and workload--resource allocation. Furthermore, we consider the network-verified provenance that is linked with agent-side information-flow control to constrain how received information affects subsequent operations. An illustrative vehicle-to-everything (V2X) case study shows that jointly adapting agent-side interaction decisions and network operations improves task completion under communication and edge-resource constraints, outperforming the conventional agent-only and wireless-only separate designs.

### 21. Trajectory-Level Mode Guidance for Controllable Diffusion-Based Multi-Robot Motion Planning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T02:22:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36530
- Summary: Motion planning often admits multiple feasible solutions, making multimodal generation valuable, particularly for flexible multi-robot coordination. Diffusion models naturally learn such trajectory distributions, yet incorporating coarse and partial trajectory priors without restricting generation remains challenging. Such priors indicate a desirable region of the solution space rather than a single solution, motivating conditioned generation that preserves multimodality. In this paper, we guide trajectory generation in the clean trajectory space and progressively incorporate trajectory priors with a timestep-dependent guidance strength. At each reverse diffusion step, the reconstructed clean trajectory provides a unified space for integrating planning costs and partial trajectory priors. Planning costs are incorporated through gradient-based refinement, while the partial prior is progressively injected at the corresponding noise levels with decreasing guidance strength. This guides generation toward the prior in early stages while gradually releasing the constraint to preserve the inherent multimodality of the diffusion model. The framework naturally extends to multi-robot planning by incorporating inter-robot collision costs. Experiments on single- and multi-robot planning tasks demonstrate controllable trajectory synthesis, diverse feasible solutions, and safe multi-agent coordination.

### 22. SkillWeaver: Agentic Exploration over Neural Interaction Skills for Scalable Robot Data Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T19:41:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36171
- Summary: Large-scale demonstrations have driven unprecedented progress in robot learning, yet collecting robot data through teleoperation is expensive and difficult to scale to diverse environments and long-horizon tasks. Simulation offers a scalable alternative, but existing data-generation pipelines often rely on open-loop controllers, scripted skill sequences, or task-specific programs. We introduce SkillWeaver, an agentic framework that autonomously generates robot experience by exploring over Neural Interaction Skills (NIS): reusable, parameterized, closed-loop policies that expose learned physical interaction capabilities to a reasoning agent. Given a task and a simulated environment, a VLM agent reasons about what to do next, invokes and parameterizes NIS to interact with the environment, observes their outcomes, and generates verification, reflection, and memory to guide subsequent exploration. We instantiate NIS as reinforcement-learned policies for closed-loop, contact-rich manipulation and organize exploration as verifier-guided tree search, enabling the agent to discover successful long-horizon behaviors without relying on predetermined execution pipelines. SkillWeaver scales autonomously to 39.1K demonstrations across 14.1K scenes, which we distill into visuomotor policies. Across simulation benchmarks and real-world manipulation, training on SkillWeaver-generated experience substantially improves generalization to novel objects, spatial configurations, tasks, and environments, and enables zero- and few-shot sim-to-sim and sim-to-real transfer. Our results suggest agentic exploration over neural interaction skills as a scalable alternative for robot data generation.

### 23. Memory in the Sky: Low-Altitude Question Answering with Multi-Agent Memory Aggregation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T15:36:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.35431
- Summary: This paper studies low-altitude question answering (LAQA), in which distributed unmanned aerial vehicle (UAV) memories are aggregated at a ground server to answer questions about observations over a long horizon. Unlike conventional resource allocation based on sensing, communication, control, or computation metrics, LAQA requires an explicit measure of memory value. We propose a generative adversarial exam (GAE) that uses forward simulation to evaluate memory retrieval and exam scores to quantify memory quality. This enables the downstream QA value of candidate memories to be measured and optimized without accessing the internal mechanisms of the black-box captioning, retrieval, and reasoning pipeline. Building on this metric, we develop a memory-centric (MemCen) framework that jointly selects UAVs and allocates transmit power to maximize memory quality under communication constraints. In the noise-limited regime, we derive a QoM-aware capped water-filling law that explicitly connects task utility with physical-layer power allocation. We further develop penalty successive optimization (PSO) and learning to memorize (L2M) solvers. MemCen achieves QA accuracies of 92.4% and 84.0% in CARLA Town04 and Town05 under static and dynamic communication conditions, respectively. In real-world experiments, MemCen achieves 88.5% QA accuracy on the panoramic multi-agent system (PMAS) benchmark. Finally, UAV-to-robot-dog demonstrations further validate the practical utility of the acquired memories for environmental understanding and navigation.

### 24. Recent Advances in Agentic Agri-Robotic Phenotyping: A Perspective Review from Fragmented Multimodal Sensing to Unified PhenoAgent Intelligence
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T08:18:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.34567
- Summary: This review examines the evolution of plant phenotyping from conventional manual trait measurement to high-throughput, robotic, and artificial intelligence-driven crop monitoring. Despite significant advances in imaging, autonomous platforms, multimodal sensing, and deep learning, current phenotyping systems remain fragmented across sensing modalities, crop traits, growth stages, environments, and management objectives. We therefore frame phenotyping as an integrated \emph{seed-soil-plant-environment-management} (SSPEM) intelligence problem, where crop performance reflects interactions among seed quality, root-zone conditions, plant development, environmental exposure, and management actions. The review synthesizes conventional, high-throughput, robotic, and AI-driven phenotyping approaches, highlighting their capabilities and persistent limitations in temporal integration, multimodal reasoning, biological interpretation, and actionable decision support. Building on this analysis, we introduce a conceptual PhenoAgent framework that extends phenotyping beyond the estimation of isolated traits to evidence-based crop-state interpretation, uncertainty-aware reasoning, and management-oriented support. The PhenoAgent concept primarily brings together scattered advances in phenotyping to deliver insights ranging from detailed to high-level, such as what is happening in the crop, why it might be occurring, what evidence is missing, and what actions or additional measurements should be considered. We also discuss challenges in dataset scarcity, annotation, benchmarking, model generalization, and explainability. By linking multimodal phenotyping with agentic AI and closed-loop decision support, this review outlines a path to interpretable, scalable, and deployment-oriented crop intelligence.

### 25. OpenAI Codex agents go rogue and consumes USD 78,000 without authorization
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-26T22:15:32+00:00
- Primary source: hackernews
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.ycombinator.com/item?id=49861047
- Summary: My OpenAI CODEX account went rogue and from a simple request took the autonomous decision to launch 826 parallel agents &#x2F; threads without any authorization on my side and without reporting any result of any sort but consuming nearly 2,146 trillions tokens, consuming a total of roughly USD 78,000 and deleting all records of what was done: I have a ticket open with OpenAI since 2 weeks but it is impossible to get an hold of a human operator.<p>On July 10, 2026 I opened a normal Codex task from VS Code.<p>The task was running: GPT-5.5 &#x2F; Medium reasoning<p>My prompt was very simple and asked for a UX&#x2F;UI validation on a specific module within my product.<p>What I found in the next days after hard analysis was:<p>The task with Root ID 019f4b90-4169-7201-bfdd-732940d8631e with reasoning GPT-5.5 &#x2F; Medium created 826 children recorded as GPT-5.6 Sol &#x2F; Ultra (notice the difference in reasoning level and in model selection)<p>This was not 826 messages inside one conversation, they are 826 distinct child task records with their own IDs.<p>A particularly strange group consists of 104 child tasks. They all preserve the same initial message as the original task, are recorded as GPT-5.6 Sol&#x2F;Ultra, and have no recorded agent_role or agent_path.<p>Those 104 tasks alone account for approximately 147.9 billion local final task-token counters.<p>Their titles show that my request to inspect UI&#x2F;UX had expanded into work involving backend infrastructure, OAuth, metering, hardening, audits, certification, implementation and release work.<p>To be precise: these local token counters are not the authoritative OpenAI billing ledger, and I am not pretending that 147.9B local counters can simply be multiplied by an API price.<p>That is exactly part of the problem: only OpenAI has the server-side mapping.<p>There is another unusual correlation.<p>Under Codex client build 0.144.0-alpha.4, the task family contains:<p>584 child tasks &#x2F; ~154.36B local token …

### 26. MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-22T06:50:10+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, human augmentation / robotics
- URL: https://arxiv.org/abs/2609.25756
- Summary: Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimodal reasoning with low-level function-constrained execution. We further introduce a scalable multi-agent pipeline to generate skill-oriented chain-of-thought(CoT) data for structured training. Built on different multimodal large-model backbones, MedVLA consistently improves performance after fine-tuning, demonstrating the effectiveness of the proposed framework across model variants. Under identical initial conditions, we perform 100 closed-loop flexible electrode implantation trials. The results show that MedVLA achieves a 95.0\% task success rate, substantially outperforming representative VLA baselines, including OpenVLA (8\%) and $π_0$ (15\%), in accuracy, stability, and safety. These results indicate that structured reasoning with constrained function-level execution is a practical route toward deployable precision medical robotics.

### 27. Mixed-integer flow formulations for motion planning and decision-making of networked multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-21T12:15:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.24474
- Summary: This work investigates the use of flow-based connectivity maintenance constraints in mixed-integer linear programming (MILP) trajectory planning and decision-making models for networked multi-agent systems (MAS). We integrate flow-based encodings for standard and k-hop connectivity into MILP multi-vehicle maneuvering models that are widely used alongside receding horizon planning strategies. Their necessity and sufficiency is demonstrated, guaranteeing full coverage of potential network topologies. The flow formulation for standard connectivity decreases the growth of the required inequality constraints from exponential to polynomial w.r.t. the size of the MAS when compared to the state-of-the-art subtour elimination (SEC) method. The flow-based k-hop connectivity constraints decrease the number of required binary variables and decouple its growth from the number of hops. However, the impact of these formulations in performance is not straightforward due to the introduction of a substantial number of continuous flow optimization variables and, in the case of k-hop connectivity, additional inequality constraints. We investigate this trade-off through a statistical evaluation of costs and optimization times using a conventional branch-and-bound commercial solver and trials performed with randomized environments for increasingly larger MAS. The results show that the flow formulation outperforms SEC in standard connectivity problems, enabling the solutions to be computed for larger MAS considering the imposed optimization time limit. The reduction in number of binary variables enabled by the k-hop flow formulations decreases the theoretical worst-case number of iterations required by the branch-and-bound algorithm to compute the global optimal solution. Our results show that this advantage did not translate into improvements in the average performance when compared to the baseline.

### 28. MA-LIPP: Cooperative Multi-Agent Load-Aware Informative Path Planning for Heterogeneous Robot Teams
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-18T00:21:05+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.21167
- Summary: Field robotics missions often require physical samples to be returned to laboratories for analysis, making path planning inherently load-aware and order-dependent as accumulated samples increase payload and traversal energy costs. In single-robot Load-Aware Informative Path Planning (LIPP), this rigidly couples sensing with hauling: a solitary robot must transport every collected sample, forcing frequent depot returns that severely restrict its spatial coverage. Heterogeneous multi-robot teams can overcome this bottleneck by dividing labor---enabling high-precision samplers to collect while high-capacity carriers handle transport. However, this introduces a complex coordination challenge regarding when, where, what, and to whom handoffs should occur on top of the LIPP problem. To address this tightly coupled problem, we introduce Multi-Agent LIPP (MA-LIPP), which enables teams to cooperate through asynchronous "dead drops," allowing one robot to deposit samples for another to retrieve later without requiring synchronous rendezvous. We formulate MA-LIPP as an exact Mixed-Integer Quadratic Program (MIQP) alongside a scalable Pairwise Large-Neighborhood Search (LNS) heuristic for complex real-world applications. The heuristic matches exact optima in $95.5\%$ of certified cases and reduces weighted posterior variance by $16.1$--$19.8\%$ relative to a sequential baseline on larger instances of up to 12 robots, providing a robust framework for cooperative physical-sampling missions.

### 29. StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-17T17:53:48+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.20791
- Summary: Hierarchical planning frameworks combine skills from multiple robot control policies for long-horizon task execution, where determining when to terminate the current skill and advance to the next subtask is essential. Existing approaches often rely on pre-designed completion signal checkers that are hard to obtain in real-world execution. Large-scale vision-language models (VLMs) offer strong reasoning capabilities, but their decision boundaries are not inherently aligned with task completion criteria, while cloud deployment and lengthy reasoning introduce substantial latency, limiting real-time monitoring. We propose StageGuard, an agentic distillation framework for accurate and efficient stage-transition decisions. StageGuard combines teacher-model reasoning with demonstration trajectories to generate structured explanations of subtask completion and policy switching. A lightweight student VLM uses these explanations to generate compact self-explanations, which are used for supervised fine-tuning. We evaluate stage-transition prediction on trajectories from two benchmarks and assess closed-loop task success through integration into hierarchical robot control on BEHAVIOR-1K, with further validation on real robots. Results show substantial improvements in stage-transition prediction while supporting efficient online monitoring.

### 30. HEROIC: Heterogeneous Evidential Reasoning for Open-Vocabulary Identification and Cross-Robot Collaboration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-17T07:14:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.19803
- Summary: Multi-agent heterogeneous air-ground robot teams are attractive for open world search, with applications for reconnaissance, urban search and rescue missions (USAR), disaster response and recovery, and hazardous environments. These two platforms have different failure modes: aerial robots cover ground quickly but cannot resolve small or occluded targets from altitude, while ground robots can identify objects-of-interest, such as people or hazardous objects, at close range but cover less area. Existing language-tasked teams either have roles fixed prior, or have a language model assign them from hand-written capability tags, so the team is unable to know when within a mission an asset is no longer useful. We present HEROIC, a decentralized heterogeneous multi-agent open-vocabulary search coordination framework that requires agents to communicate in natural language only. HEROIC's initial agent role assignment is derived from sensor properties and a scale law to determine whether targets can be detected with a high confidence. From the mission's natural language prompt alone, this law assigns aerial flight altitudes and sweep spacing. When this calculated height falls below the altitude for safe flight, aerial agents re-task themselves from searcher to aerial triage, escort, and route guide for ground agents. Both robots maintain an evidential belief over the search area (bearing rays for positive evidence, a log-odds posterior for negative evidence) and gate any arrival on close-range verification. In full-stack experiments, HEROIC reaches the target 84% of the time across all 6 scenes, compares to 35-54% for vision-language frontier baselines, frontier-based search, lawnmower, and random-walk running the same perception, all while being 2-4x sooner to arrive at the target.
