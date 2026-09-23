# Blindspot Signals Report - 2026-09-23

- Source export: `/opt/apps/haier/exports/evolution_signals_20260923_020820.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 486
- Deduped/weighted signal clusters: 468
- Novel vs previous reports: 27
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-22T06:50:10+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, human augmentation / robotics
- URL: https://arxiv.org/abs/2609.25756
- Summary: Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimodal reasoning with low-level function-constrained execution. We further introduce a scalable multi-agent pipeline to generate skill-oriented chain-of-thought(CoT) data for structured training. Built on different multimodal large-model backbones, MedVLA consistently improves performance after fine-tuning, demonstrating the effectiveness of the proposed framework across model variants. Under identical initial conditions, we perform 100 closed-loop flexible electrode implantation trials. The results show that MedVLA achieves a 95.0\% task success rate, substantially outperforming representative VLA baselines, including OpenVLA (8\%) and $π_0$ (15\%), in accuracy, stability, and safety. These results indicate that structured reasoning with constrained function-level execution is a practical route toward deployable precision medical robotics.

### 2. Towards Intent-Aware Human-Robot Teaming: A Platform for Search-and-Rescue Operations
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-22T11:58:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.26051
- Summary: We investigate the challenges of enabling effective collaboration between human operators and heterogeneous autonomous agents in complex, dynamic environments by developing an interaction platform that allows study of operator behavior and supports intent inference and decision-making using state-of-the-art frameworks. We demonstrate the extent to which the operator's perception, decisions, and actions could be supported by autonomous systems during search-and-rescue operations with our platform.

### 3. FiberPro 1.0: Multiagent AI-Guided Design for High-Throughput Production and Conformal Deposition of Functional Protein Micro/Nanofibers
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-22T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: cognitive outsourcing, AI agents / cognitive outsourcing
- URL: https://www.biorxiv.org/content/10.64898/2026.09.18.752775
- Summary: Functional protein micro/nanofibers integrate high specific surface areas with bioactive architectures but remain hampered low production throughput and severe processing instability. Focused rotary jet spinning (FRJS) shows promising to break these throughput constraints while enabling direct, conformal deposition onto complex, irregular substrates. However, navigating FRJS's narrow processing windows in proteins remains failure-prone without closed-loop experimental guidance. Here, we report FiberPro 1.0, a large language model driven multi agent framework that unites high-throughput spinning with real-time experimental feedback for autonomous design, execution, and optimization. Across three protein systems, FiberPro 1.0 converged on spinnable formulations within an average of two iterations. To demonstrate high-throughput conformal deposition in a translational setting, FiberPro designed a zein-based active packaging system applied directly onto diverse food matrices. The resulting conformal coating combined potent antibacterial activity with real-time freshness monitoring, markedly suppressing Escherichia coli and extending shelf life. This work connects autonomous AI reasoning with high-throughput processing, establishing a verifiable route for scalable manufacturing and conformal coating of functional protein micro/nanofibers.

### 4. Tipping Points in LLM-Based Multi-Agent Systems: Stance on Climate Change Action
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-21T21:33:48+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.25432
- Summary: Because significant action to counter global warming requires massive public support, it is important to understand the dynamics of public opinion on climate issues. Of special interest are social tipping points, as revealed by large-scale effects of small perturbations in individual behaviors. Agent-based models (ABM) are an effective computational tool for studying these matters, because they allow controlled and systematic exploration of the effects of interventions that may be infeasible in real-world social systems. Large language models (LLMs) have been used to endow model agents with the ability to communicate in natural language (rather than by exchanging predefined messages), as well as with personality (in the form of a narrative self and episodic memory). We leverage LLM-powered ABM to look for tipping points in the social dynamics of a micro-society in which some of the discussions are about climate change. Our agents' stance was defined by two variables: the strength of conviction about the urgency of climate action and the degree of trust in existing institutions. We quantified shifts in agents' "beliefs" by monitoring, across multiple rounds of conversations, (1) inter-agent distances in this two-dimensional stance space and (2) the patterns of discussion topics as modeled by Latent Dirichlet Allocation (LDA). Our findings to date suggest that significant abrupt changes in climate-change stance do occur in this simple model. We report a number of methodological lessons from this study, notably, the need to prevent LLM biases from interfering with the conversational dynamics and, more generally, to maintain agent personality and episodic memories of interactions in the face of such biases. Resolving these issues may allow for using ABM-derived insights in designing real-life interventions vis-a-vis climate change and other important societal challenges.

### 5. GradAgent: A Knowledge-Guided Multi-Agent System for Structure-Preserving Gradient-Flow Computation with an Application to Multicomponent Vesicle Dynamics
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-21T16:42:36+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.24871
- Summary: High-order differential operators and nonlinear coupling make it challenging to construct conservative and energy-stable schemes for coupled gradient-flow systems. We present GradAgent, a knowledge-guided multi-agent system that coordinates three agents across model analysis, algorithm design and proofs, and numerical implementation and validation. Independent audits strengthen reliability by uncovering mathematical errors and proof gaps, guiding revisions, and maintaining consistency across stages. In Reconstruction Mode, GradAgent reconstructs 20 published studies and organizes audited knowledge in an extensible knowledge graph (KG), GradAgent-KG, linking model structures, discretization strategies and proofs, implementations, and numerical evidence. In Design Mode, the agents assess the applicability of retrieved knowledge and develop new schemes informed by relevant discretization strategies. Applied to the fully coupled multicomponent vesicle phase-field-fluid model, GradAgent yields three first-order and three second-order schemes across three algorithmic families, including four linear, decoupled schemes. Under stated assumptions, all six schemes conserve membrane component mass and vesicle volume and dissipate their respective temporally discrete energies unconditionally. Comparisons with and without GradAgent-KG show that it promotes diversity in structure-preserving scheme design for this target model. Numerical tests confirm second-order spatial accuracy, the expected temporal orders, conservation, and temporally discrete energy dissipation, while three-dimensional shear-flow simulations agree qualitatively with experiments. These results demonstrate GradAgent's ability to combine reusable knowledge, coordinated reasoning, and independent auditing to develop and validate structure-preserving algorithms for complex coupled systems.

### 6. Incentive Design for Multi-Agent Systems: A Bilevel Optimization Framework for Coordinating Independent Agents and Convergence Analysis
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-22T17:13:21+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.26726
- Summary: Incentive design aims to guide the performance of a system towards a human's intention or preference. We study this problem in a multi-agent system with one leader and multiple followers. Each follower independently solves a mdp to maximize its own expected total return with the same state space and action space. However, the leader's objective depends on the collective best-response policies of all followers. To influence these policies of followers, the leader provides side payments as incentives to individual followers at a cost, aiming to align the collective behaviors of followers with its own goal while minimizing this cost of incentive. Such a leader-followers interaction is formulated as a bilevel optimization problem: the lower level consists of followers individually optimizing their MDPs given the side payments, and the upper level involves the leader optimizing its objective function given the followers' best responses. The main challenge to solve the incentive design is that the leader's objective is generally non-concave and the lower level optimization problems can have multiple local optima. To this end, we employ a constrained optimization reformation of this bi-level optimization problem and develop an algorithm that provably converges to a stationary point of the original problem, by leveraging several smoothness properties of value functions in MDPs. We validate our algorithm in a stochastic gridworld by examining its convergence, verifying that the constraints are satisfied, and evaluating the improvement in the leader's performance.

### 7. MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-22T14:45:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.26520
- Summary: Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills. However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE, a Multi-Agent virtual TEleoperation platform for humanoid collaboration data collection that enables multiple geographically distributed operators to simultaneously control whole-body humanoids in a shared physics-based environment. MATE removes the need for multiple physical robots and co-located operation while preserving physically coupled interactions among humanoids, objects, and environments. Using MATE, we construct a multi-humanoid collaboration dataset comprising 24.1 hours of coordinated behavior across 2,500 joint episodes and five long-horizon tasks, including object handover, relay delivery, environment interaction, and cooperative transport. To improve learning from these interaction-rich demonstrations, we introduce EAIS, an Execution-Aligned Interaction Sampling strategy that computes sampling signals within an execution-aligned prefix and prioritizes task-progressing and interaction-critical behaviors. We evaluate MATE with representative imitation learning and vision-language-action policies across diverse collaboration tasks. Experiments demonstrate efficient data collection, effective policy learning, and zero-shot transfer from virtual demonstrations to a physical humanoid without real-world fine-tuning. Project page: https://yerik-yu.github.io/MATE/

### 8. meshIQ Launches AgentIQ to Govern Autonomous AI Agents in Real Time - citybiz
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-22T14:01:35+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiqgFBVV95cUxPb1FzOFRCeXhMWmdLX3R0OEJMbVA2RlgyRU93dHV1eHNuZy1ySzRPeV9mM0F3QnliTUJOQUJhS2daQWZNMkcteXlaenFFUDJQdUpyUDRwSHMxZzhScXR0OVM2R0xLOFVKa0hwYzM4VHNkYU40dEVMRUZrNjdIZDVrdFNwQl9wU0MzTlJtSWVoUEJPc3hha0FDakgtOXBIRE1vNEo3bkNnUkNkQQ?oc=5
- Summary: meshIQ Launches AgentIQ to Govern Autonomous AI Agents in Real Time&nbsp;&nbsp;citybiz

### 9. Toward Responsible AI-Augmented Cyber Defense: Pattern Recognition, Defense-in-Depth, and the Case for Human-AI Collaboration
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-22T09:28:13+00:00
- Primary source: arxiv
- Focus/tech: neural interfaces, human augmentation, AI decision delegation / neural interfaces
- URL: https://arxiv.org/abs/2609.25921
- Summary: Cybersecurity literature has extensively documented the operational benefits of artificial intelligence (AI) for threat detection, incident response, and prevention, while raising qualitative concerns about over-automation, algorithmic bias, and analyst-skill erosion. What remains largely absent is a formal, falsifiable model connecting three constructs that recur across this literature: Defense-in-Depth Theory, the Artificial Intelligence Theory of Pattern Recognition, and human-AI collaboration in security operations. This paper develops such a model. We formalize layered defense as a Bernoulli detection cascade in which AI augmentation enters multiplicatively across layers; we formalize each layer's pattern-recognition behavior as a Neyman-Pearson/Bayesian detector with a derived closed-form optimal threshold; and we formalize human-AI triage as a capacity-constrained cascade with an explicit, quantifiable trade-off between detection probability and false-alarm ("alert fatigue") rate. A Monte Carlo/analytical simulation evaluated at illustrative but realistic operating points shows that (i) AI augmentation compounds across defense layers, delivering its largest marginal gains exactly where traditional layering saturates, and (ii) full human review of AI-flagged alerts is not optimal: increasing analyst capacity toward 100% coverage cuts false alarms by roughly 20-fold but simultaneously lowers system-level detection probability, because imperfect analyst accuracy is then applied to every alert rather than a filtered subset. These results give the widely repeated qualitative recommendation of "balanced human-AI collaboration" a precise, testable form and suggest an interior-optimum capacity ratio as a concrete design target for security operations centers (SOCs), including those securing IT/OT-converged critical infrastructure.

### 10. When Does Execution Provenance Help Agent Memory Retrieval?
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-22T09:20:51+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.25913
- Summary: A language agent's execution history can exceed its context window, requiring its memory system to retrieve complete supporting evidence under a hard token budget. Evidence may span multiple execution events, yet conventional retrievers use fixed token windows and fixed-k metrics that reward individual fragments without showing whether the complete evidence set fits in context. Smaller windows reduce irrelevant text but scatter evidence across candidates, while flat-versus-graph comparisons can conflate candidate design with graph propagation. To address these limitations, we formulate agent-memory retrieval as budgeted evidence completion and score exact gold spans in shared source coordinates. We first construct source-aligned provenance units from tool arguments and outputs. We then apply a zero-initialized residual R-GCN to refine frozen dense-retrieval scores over typed provenance edges. We evaluate 2,000 span-grounded memory queries over 1,207 held-out execution-grounded ISETrace trajectories. With matched Dense-FT scoring, provenance units improve Full Support@2048 by 19.07 points over flat 512-token windows and remain 11.96 points above a per-metric oracle over four flat chunk sizes; the pattern also holds with cross-encoder scoring. Holding the candidates and seed scores fixed, graph propagation adds 4.55 points in Full Support@2048 (95% CI [2.98, 6.18]). This gain is concentrated when gold evidence spans multiple events; entity co-occurrence expansion produces no comparable benefit, and relation and topology controls confirm dependence on typed transformations and observed graph structure. Overall, source-aligned candidates address the dominant granularity trade-off, while graph-conditioned propagation adds a smaller, targeted benefit for distributed evidence.

### 11. Fez
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-21T18:50:10+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/fez-2
- Summary: <p> AI agents that work as a team and make decisions together </p> <p> <a href="https://www.producthunt.com/products/fez-2?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1257466?app_id=339">Link</a> </p>

### 12. DolphinBench: Mapping the Pareto Frontier of Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-21T17:54:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.24971
- Summary: Agents today often take real-world actions that depend on long-term memory and context recall over time. However, most current memory benchmarks are built for a conversational question-answer format, where the question itself signals that some fact must be retrieved, and often which one. Moreover, benchmarks rarely require anything beyond accuracy from submissions, allowing memory systems to make unreasonable cost/time tradeoffs to achieve higher scores. We present DolphinBench, a benchmark that evaluates memory directly through an agent's task completion. DolphinBench includes three knowledge-work personas with roughly 500k tokens of user messages per persona and evaluates agents on tasks that depend on information from that history. We verify all 200 tasks per persona by running an agent with and without the relevant history, requiring success with it and failure without it. Finally, we require all evaluations to report total cost and latency alongside accuracy, which enables us to evaluate agent memory systems holistically. No existing memory benchmark combines all three. The dataset and evaluation code are available at https://dolphinbench.ai.

### 13. Three Governance Shifts to Build Trust in Agentic AI Autonomy - PwC
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-16T19:56:31+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiiwFBVV95cUxNWHRhSGxNSTBER0czQlE1cmlFejM1MTUtNmZjWFhNbHhTMERSS3Y5eXo2VGZ4SkhJcHNCbGtQY1E5REJMUDNrY1VWdmlPMHlCalF2ajZSTjhTOElGRjVLVTh3V3U2NGRvQWVKUjdjTXMyVDVwNnBiU2hzanNyaWhQbENEMW8xeVRLR0tr?oc=5
- Summary: Three Governance Shifts to Build Trust in Agentic AI Autonomy&nbsp;&nbsp;PwC

### 14. Meta's New Muse AI Agent Read My Private Messages. I Never Asked It To
- Weighted score: 0.08
- Deep score: 0
- Coverage: 2 sources (hackernews, techcrunch)
- Date: 2026-09-22T21:43:04+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202
  - Alt: https://techcrunch.com/2026/09/10/metas-ai-agent-muse-is-now-the-no-2-app-in-the-us/
  - Alt: https://ai.meta.com/muse/
- Summary: No summary.

### 15. EXCLUSIVE: OpenAI agents hijacked German website in previously undisclosed AI breakout this spring - Reuters
- Weighted score: 0.08
- Deep score: 0
- Coverage: 2 sources (hackernews, google_news)
- Date: 2026-09-04T10:30:57+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/
  - Alt: https://news.google.com/rss/articles/CBMixAFBVV95cUxQb0lsYkxySy1tYUVZRnlHQmN5Q1loNW14dl9oYWZ4UFpWX0N6TGNMdUdTSFRHMDBsMzMwazV2RkFkM01jTGFvbHpJUTk4ZVNzVGZJc3FtaWlHMGViMEp2ZHFUcEZuNmF3MUd3UjF3eEc4ZC04MDEwWmp3RlYzSmFPZTNLTVlpTURsdENEdE1FMlNzRjc1TzFQd2tSSUNoQmtxRF9DQUVIR0Ftams3Zm5KUFZ1dHhrZEtKUFlSQUFyeVozSmxk?oc=5
- Summary: No summary.

### 16. google / ax
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-23T02:01:49.574166+00:00
- Primary source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/google/ax
- Summary: Google's open agentic orchestration runtime

### 17. dream num / univer
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-23T02:01:49.574150+00:00
- Primary source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/dream-num/univer
- Summary: The Office Harness for AI Agents — Spreadsheets, Docs, Slides, Canvas, Relational Tables, and PDF in one runtime.

### 18. Meta admits Muse’s likeness to OpenClaw isn’t a coincidence
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-22T19:09:11+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/
- Summary: Meta says Muse was built from scratch, but acknowledges the AI assistant was "heavily inspired" by OpenClaw — down to some of its workspace filenames and content.

### 19. Launch HN: Coverage Cat (YC S22) – Umbrella insurance via your personal agent
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-22T17:26:36+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.coveragecat.com/
- Summary: Hey HN! We’re Max and Gabriel the co-founders of Coverage Cat. We’ve been friends for over a decade, met in college then hung out mostly on the internet. We love building products that help people optimize the crufty corners of their lives. Max is a former Google&#x2F;Microsoft&#x2F;Two Sigma PM and Gabriel has been working in startups for over a decade.<p>We’re building Coverage Cat: a licensed insurance brokerage that helps you compare umbrella and home coverage side by side — with straight pricing, no sold leads, and a real broker on the other end. Our current focus is helping tech folks (think L3-L8) buy umbrella insurance.<p>Coverage Cat pairs AI-guided intake with a licensed brokerage team, so you can size up coverage, see honest price ranges, and compare real carrier options without handing your details to five agents overnight. Folks who use personal AI agents (think Muse, Instinct, Town, Openclaw, etc.) can drive the same flow through the Agent API&#x2F;MCP.<p>We’d love your feedback so please do try it out. Just feed the prompt: “Shop for umbrella insurance with Coverage Cat” to your personal agent and let us know what you think!<p>If you want to watch a couple of agents navigate the flow before you use it there’s a video here: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;1BUkgAn6s-I" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;1BUkgAn6s-I</a><p>For those who are unfamiliar with this type of coverage, here’s a blurb from one of our insurance agents: “Umbrella liability insurance is a policy that provides additional coverage above the limits of existing auto, homeowners, renters, or landlord policies. It kicks in after the underlying policy limits are exhausted and may also cover personal injury claims like libel, slander, or defamation that standard policies often exclude. Policies typically start at $1 million in additional liability coverage and can protect you, your spouse, dependents, and even pets in your household.”<p>Buying insurance online is a …

### 20. AI Agents Are Rewriting the Rules of Lateral Movement
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-22T12:30:00+00:00
- Primary source: The Hacker News
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMie0FVX3lxTE5yTFdMdUV5Rmx2cUVLQVNycFpBWG5PWlBHY3RTcHpKNXlvN2YwUXB6VmpEYV9tTXJfZEp5V2w1U3p5WV81S0l6T2l5WTUyYThoaUNmTmlXa1VLVHhiS1BfaWtwc2w3bGhhT1JaNklvSThkaDV0MDBZZnNvSQ?oc=5
- Summary: AI Agents Are Rewriting the Rules of Lateral Movement&nbsp;&nbsp;The Hacker News

### 21. Grok 4.7
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-21T18:48:33+00:00
- Primary source: product_hunt
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://www.producthunt.com/products/grok-4-7-8
- Summary: <p> SpaceXAI's most powerful model for coding and knowledge work </p> <p> <a href="https://www.producthunt.com/products/grok-4-7-8?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1257464?app_id=339">Link</a> </p>

### 22. Who Does What in AI Auditing? Designing Human-AI Collaboration for Auditing Generative AI
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-21T17:57:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2609.24986
- Summary: AI auditing increasingly incorporates AI agents to expand the scale and breadth of audit coverage, yet little is known about how auditing work should be divided without displacing human judgment. We introduce Human-Agent Audit Collaboration (HAAC), a workflow and system for structuring human-AI collaboration in AI auditing. Drawing on prior work and formative consultations with AI auditing practitioners, HAAC specifies how agents can support exploration, assessment, reporting, and review while preserving human oversight where contextual judgment is critical. We instantiate HAAC for conversational shopping agents and evaluate it through two studies. With 71 auditors, AI assistance increased attack success and broadened exploration, while also shaping later attacks and increasing auditors' reliance on AI-generated assessments and reports. Interviews with Responsible AI practitioners showed that actionable audits require visibility into coverage, reproducible attack trajectories, and evaluation of the auditing agents themselves. Our findings identify design considerations for effective and accountable human-AI auditing.

### 23. Plane Agents
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-21T15:36:35+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/planehq
- Summary: <p> Assign work to AI agents, like any teammate </p> <p> <a href="https://www.producthunt.com/products/planehq?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1257313?app_id=339">Link</a> </p>

### 24. ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-21T13:25:05+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.24563
- Summary: Adapting visuomotor policies to new manipulation tasks often requires substantial manual engineering or teleoperated data collection. Simulation can provide task-specific data at scale, but constructing the scene, designing expert behavior, and configuring data generation still require significant per-task effort. We present ARSTAG, an agentic Real2Sim2Real system that turns a single RGB image and a natural-language instruction directly into robot policy-learning data. A hierarchy of language agents constructs a task-scoped simulation scene, generates robot-feasible demonstrations, and expands the training distribution through task-consistent randomization, while a coordinator agent manages cross-stage feedback and recovery. Across seven manipulation tasks spanning grasping, placement, and stacking, the ARSTAG-generated demonstrations enable sim-to-real transfer of three visuomotor policy architectures to a dual-arm robot, with pi0.5 achieving an average real-world success rate of 74.6%. Ablations show that task-consistent randomization substantially improves robustness, and policy performance increases with generated dataset size. Project webpage: https://boweili666.github.io/ARSTAG/.

### 25. PixelCrew
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-19T04:11:25+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/pixelcrew
- Summary: <p> Production-ready design from a crew of AI agents </p> <p> <a href="https://www.producthunt.com/products/pixelcrew?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1255169?app_id=339">Link</a> </p>

### 26. Prowler Cloud
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-17T17:01:37+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/prowler
- Summary: <p> Where your AI agent becomes a cloud security defender </p> <p> <a href="https://www.producthunt.com/products/prowler?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1253740?app_id=339">Link</a> </p>

### 27. SereneDB
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-15T03:26:57+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/serenedb-krummelanke
- Summary: <p> Ultra-Fast Search & Analytics Database, Agentic AI ready </p> <p> <a href="https://www.producthunt.com/products/serenedb-krummelanke?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1250875?app_id=339">Link</a> </p>

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

### 3. Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-21T01:43:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.23986
- Summary: Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \textbf{\method}, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6$\times$ speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.

### 4. EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T07:41:56+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15161
  - Alt: https://arxiv.org/abs/2609.19680
- Summary: Large language model (LLM) driven multi-agent systems have shown promise in complex clinical reasoning, yet existing approaches rely on static strategies and lack persistent clinical memory, preventing self-evolving from prior diagnostic successes and failures. We present EMR, a self-evolving medical multi-agent system via Experience Mining and Reuse. EMR introduces a hierarchical clinical experience library that organizes accumulated knowledge into three levels: clinical principles, diagnostic patterns, and representative cases. During inference, EMR emulates multidisciplinary consultation: a planner agent coordinates domain-specific department agents for specialized reasoning, while a summary agent synthesizes their analyses into a final decision. Critically, EMR automatically extracts correct diagnostic insights and failure-related warnings from multi-agent reasoning trajectories, incrementally updating the experience library to guide future cases. Experiments on medical reasoning benchmarks demonstrate that EMR consistently outperforms state-of-the-art medical multi-agent baselines. Further analysis reveals that the hierarchical experience enables cross-specialty generalization and transfer across diverse LLM backbones, offering a scalable and in

### 5. BusMA: A Bus Communication Substrate for Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-14T05:19:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.15054
- Summary: Multi-Agent (MA) systems are effective at solving complex tasks that demand planning, tool use, and the synthesis of evidence from multiple sources. Existing systems typically adopt Hierarchical Manager-Worker (HMW) or Router-based Message Passing (RMP) structures as their communication protocol. However, these designs restrict agent autonomy: Worker agents cannot directly consult specific "peers", and misrouted messages can propagate errors. Inspired by bus architectures in computer systems, we propose BusMA, a communication framework that allows any agent to address other agents through a shared channel, i.e., the Bus. It consists of agent registration, message routing, and shared memory management components. Worker agents, each equipped with tools, have their own local memory and can reason, act (tool usage), and communicate by posting shared messages with specific intents. We introduce four intents: discussion, challenge, guidance, and request for explanation, which support fine-grained communication among agents. A Chair agent monitors the shared memory to coordinate interactions and facilitate convergence among Workers. To evaluate the effectiveness of BusMA, we conduct extensive experiments with two frontier LLMs across 13 tasks spanning visual reasoning, mathematical reasoning, and knowledge retrieval demonstrate that BusMA consistently outperforms state-of-the-art HMW and RMP methods.

### 6. Enhancing Human Mobility Prediction with Spatially Aware LLM-based Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-13T01:41:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.14227
- Summary: Predicting a user's next POI is a task in human mobility modeling, yet LLM-based approaches focus on semantic reasoning from previous mobility records, while neglecting real-world spatial context. However, human mobility is inherently shaped by spatial cognition, including geographic distance and neighborhood context. This issue is further compounded by prior evidence that LLMs often struggle with spatial reasoning tasks, including distance estimation and geographically biased prediction. To address these limitations, we propose our framework, a multi-agent LLM framework that decomposes next-POI prediction into three stages: Firstly, a Pattern Extraction Agent that captures temporal and categorical mobility patterns from trajectory history; Secondly, a Spatial Reasoning Agent that structures candidate activity choices by combining behavioral preferences with real-world spatial constraints, including geographic distance, road network distance, and neighborhood affiliation; and Thirdly, a Decision Synthesis Agent that integrates behavioral patterns and spatial reasoning for final prediction. Experiments on the NYC benchmark dataset with two LLM backbones show improvements over baseline methods, with up to 493% Hit@1 improvement and 37% relative improvement in Hit@5. Ablations show that combining neighborhood affiliation with distance-based features generally outperforms distance-only settings, and that the Spatial Reasoning Agent plays a crucial role in final prediction by integrating behavioral preferences with real-world spatial constraints, especially for smaller models. Overall, the results highlight the importance of spatial reasoning in mobility prediction. Accurate next-POI prediction requires combining behavioral patterns with explicit real-world spatial constraints, and multi-agent decomposition provides an effective structure for organizing these forms of context.

### 7. Memory-First Fact-Checking: A Knowledge-Graph-Grounded Multi-Agent System for Misinformation Detection
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-30T07:16:07+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.29617
- Summary: This paper introduces a hybrid fact-checking framework that integrates Knowledge Graph-based semantic memory with adversarial multi-agent reasoning for explainable misinformation detection. The proposed system follows a memory-first, web-fallback architecture, in which input claims are initially evaluated against a dual-index Knowledge Graph through Sentence-BERT-based semantic retrieval and Natural Language Inference. When the evidence retrieved from the graph is insufficient to support a reliable decision, the framework collects information from trusted web sources and assesses it using an adversarial tribunal composed of support, contradiction, and judging agents. A graph-aware confidence mechanism combines semantic similarity, NLI confidence, and structural graph evidence to determine whether internal knowledge is sufficient, thereby reducing unnecessary web retrieval. Following verification, validated information is transformed into structured triples and incorporated into the Knowledge Graph, supporting the incremental expansion of the system's semantic memory. Experimental evaluation on a curated COVID-19 misinformation benchmark demonstrates that the proposed framework achieves an accuracy of 97.4\% and a macro-averaged F1-score of 92.6% on resolved claims, outperforming a Llama~3.3~70B baseline, which obtains an accuracy of 87.7% and a macro-averaged F1-score of 86.3%.

### 8. Stress-testing university AI governance: A prospective method for locating policy breakpoints
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-28T22:49:58+00:00
- Primary source: arxiv
- Focus/tech: human augmentation, AI decision delegation / human augmentation
- URL: https://arxiv.org/abs/2608.28925
- Summary: Universities are producing AI principles and use policies faster than they are building decision pathways for unfamiliar forms of AI agency. This study develops Institutional AI Governance Stress Testing (IAGST), a prospective documentary method for locating where publicly documented governance ceases to yield an accountable response. IAGST adapts established policy stress-testing and wind-tunneling logic. Its originality lies in combining controlled capability escalation, a frozen documentary corpus, a six-dimensional governance response chain, non-compensatory decision rules, and case-level breakpoint diagnosis. The method was demonstrated using 133 substantive public documents from five Western Australian universities and 15 quality-screened scenarios, resulting in 75 university-scenario encounters. Six cases were resolved, 14 were resolved through structured discretion, and 55 were indeterminate. Governed pathways fell from 16 of 25 augmentation cases to four delegation cases and none at autonomous substitution. The dominant weakness was not the complete absence of responsible roles: all 50 authority-gap cases named a role at only a generic level but lacked sufficient decision criteria or process. The findings show how universities can move beyond policy inventories and principal statements by testing whether authority, procedures, safeguards, and reviews remain connected as AI capabilities evolve. IAGST is a reproducible diagnostic for policy learning, not a ranking or measure of implementation.

### 9. MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-22T09:25:23+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.21867
- Summary: LLM agents are moving from single-prompt use to long task streams in which reusable memory becomes a core capability for terminal, software-engineering, and web tasks. Such memory is useful only when stored experience remains reliable across hundreds of interactions, but two failure modes break that assumption in practice. The first is unreliable admission: failed trajectories,accidental successes, and misleading observations enter memory because they appear relevant, then mislead later decisions. The second is memory drift: long-running banks accumulate duplicate, stale, and conflicting records that retrieval alone cannot repair. MemGuard's key distinction is to treat verifier output not as a one-shot filter, but as persistent lifecycle metadata. It converts multi-criteria score-token verification into reward, confidence, label, and uncertainty descriptors that are attached to every candidate before activation and reused during retrieval, conflict resolution, summarization, and archival. We evaluate MemGuard on Terminal-Bench 2.0, SWE-Bench Verified, WebArena, and Mind2Web across four backbones, comparing against four memory baselines plus a verifier-only control under matched runtime budgets. Averaged over five seeds, MemGuard achieves the best success metric and lowest average steps in all 16 backbone-benchmark settings, improving over ReasoningBank, the strongest prior baseline among the memory methods we evaluate, with a largest gain of 7.9 success-rate points on WebArena, 5.6 step-success-rate points on Mind2Web, and 2.4-3.5 points on terminal and software-engineering benchmarks. Code is available at https://github.com/whyyyyy123/MemGuard.

### 10. MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-22T06:50:10+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, human augmentation / robotics
- URL: https://arxiv.org/abs/2609.25756
- Summary: Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimodal reasoning with low-level function-constrained execution. We further introduce a scalable multi-agent pipeline to generate skill-oriented chain-of-thought(CoT) data for structured training. Built on different multimodal large-model backbones, MedVLA consistently improves performance after fine-tuning, demonstrating the effectiveness of the proposed framework across model variants. Under identical initial conditions, we perform 100 closed-loop flexible electrode implantation trials. The results show that MedVLA achieves a 95.0\% task success rate, substantially outperforming representative VLA baselines, including OpenVLA (8\%) and $π_0$ (15\%), in accuracy, stability, and safety. These results indicate that structured reasoning with constrained function-level execution is a practical route toward deployable precision medical robotics.

### 11. Mixed-integer flow formulations for motion planning and decision-making of networked multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-21T12:15:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.24474
- Summary: This work investigates the use of flow-based connectivity maintenance constraints in mixed-integer linear programming (MILP) trajectory planning and decision-making models for networked multi-agent systems (MAS). We integrate flow-based encodings for standard and k-hop connectivity into MILP multi-vehicle maneuvering models that are widely used alongside receding horizon planning strategies. Their necessity and sufficiency is demonstrated, guaranteeing full coverage of potential network topologies. The flow formulation for standard connectivity decreases the growth of the required inequality constraints from exponential to polynomial w.r.t. the size of the MAS when compared to the state-of-the-art subtour elimination (SEC) method. The flow-based k-hop connectivity constraints decrease the number of required binary variables and decouple its growth from the number of hops. However, the impact of these formulations in performance is not straightforward due to the introduction of a substantial number of continuous flow optimization variables and, in the case of k-hop connectivity, additional inequality constraints. We investigate this trade-off through a statistical evaluation of costs and optimization times using a conventional branch-and-bound commercial solver and trials performed with randomized environments for increasingly larger MAS. The results show that the flow formulation outperforms SEC in standard connectivity problems, enabling the solutions to be computed for larger MAS considering the imposed optimization time limit. The reduction in number of binary variables enabled by the k-hop flow formulations decreases the theoretical worst-case number of iterations required by the branch-and-bound algorithm to compute the global optimal solution. Our results show that this advantage did not translate into improvements in the average performance when compared to the baseline.

### 12. MA-LIPP: Cooperative Multi-Agent Load-Aware Informative Path Planning for Heterogeneous Robot Teams
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-18T00:21:05+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.21167
- Summary: Field robotics missions often require physical samples to be returned to laboratories for analysis, making path planning inherently load-aware and order-dependent as accumulated samples increase payload and traversal energy costs. In single-robot Load-Aware Informative Path Planning (LIPP), this rigidly couples sensing with hauling: a solitary robot must transport every collected sample, forcing frequent depot returns that severely restrict its spatial coverage. Heterogeneous multi-robot teams can overcome this bottleneck by dividing labor---enabling high-precision samplers to collect while high-capacity carriers handle transport. However, this introduces a complex coordination challenge regarding when, where, what, and to whom handoffs should occur on top of the LIPP problem. To address this tightly coupled problem, we introduce Multi-Agent LIPP (MA-LIPP), which enables teams to cooperate through asynchronous "dead drops," allowing one robot to deposit samples for another to retrieve later without requiring synchronous rendezvous. We formulate MA-LIPP as an exact Mixed-Integer Quadratic Program (MIQP) alongside a scalable Pairwise Large-Neighborhood Search (LNS) heuristic for complex real-world applications. The heuristic matches exact optima in $95.5\%$ of certified cases and reduces weighted posterior variance by $16.1$--$19.8\%$ relative to a sequential baseline on larger instances of up to 12 robots, providing a robust framework for cooperative physical-sampling missions.

### 13. StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-17T17:53:48+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.20791
- Summary: Hierarchical planning frameworks combine skills from multiple robot control policies for long-horizon task execution, where determining when to terminate the current skill and advance to the next subtask is essential. Existing approaches often rely on pre-designed completion signal checkers that are hard to obtain in real-world execution. Large-scale vision-language models (VLMs) offer strong reasoning capabilities, but their decision boundaries are not inherently aligned with task completion criteria, while cloud deployment and lengthy reasoning introduce substantial latency, limiting real-time monitoring. We propose StageGuard, an agentic distillation framework for accurate and efficient stage-transition decisions. StageGuard combines teacher-model reasoning with demonstration trajectories to generate structured explanations of subtask completion and policy switching. A lightweight student VLM uses these explanations to generate compact self-explanations, which are used for supervised fine-tuning. We evaluate stage-transition prediction on trajectories from two benchmarks and assess closed-loop task success through integration into hierarchical robot control on BEHAVIOR-1K, with further validation on real robots. Results show substantial improvements in stage-transition prediction while supporting efficient online monitoring.

### 14. HEROIC: Heterogeneous Evidential Reasoning for Open-Vocabulary Identification and Cross-Robot Collaboration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-17T07:14:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.19803
- Summary: Multi-agent heterogeneous air-ground robot teams are attractive for open world search, with applications for reconnaissance, urban search and rescue missions (USAR), disaster response and recovery, and hazardous environments. These two platforms have different failure modes: aerial robots cover ground quickly but cannot resolve small or occluded targets from altitude, while ground robots can identify objects-of-interest, such as people or hazardous objects, at close range but cover less area. Existing language-tasked teams either have roles fixed prior, or have a language model assign them from hand-written capability tags, so the team is unable to know when within a mission an asset is no longer useful. We present HEROIC, a decentralized heterogeneous multi-agent open-vocabulary search coordination framework that requires agents to communicate in natural language only. HEROIC's initial agent role assignment is derived from sensor properties and a scale law to determine whether targets can be detected with a high confidence. From the mission's natural language prompt alone, this law assigns aerial flight altitudes and sweep spacing. When this calculated height falls below the altitude for safe flight, aerial agents re-task themselves from searcher to aerial triage, escort, and route guide for ground agents. Both robots maintain an evidential belief over the search area (bearing rays for positive evidence, a log-odds posterior for negative evidence) and gate any arrival on close-range verification. In full-stack experiments, HEROIC reaches the target 84% of the time across all 6 scenes, compares to 35-54% for vision-language frontier baselines, frontier-based search, lawnmower, and random-walk running the same perception, all while being 2-4x sooner to arrive at the target.

### 15. Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-16T19:22:58+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.19347
- Summary: Robotic additive manufacturing (AM) extends material-extrusion printing beyond gantry kinematics but makes process planning robot-dependent. A slicer-generated plan that appears favorable in part coordinates can become infeasible or robotically unfavorable on a manipulator because slicer-process decisions and part orientation determine the generated path, while part orientation and workspace placement affect its kinematic realization. Existing AM tools, large language model (LLM)-based decision-support methods, and digital-shadow systems do not provide integrated pre-execution evaluation of these coupled decisions. This paper presents agentic robotic additive manufacturing (A-RAM), an agent-specialist-tool framework that converts user intent and a part file into traceable, execution-ready plans. The LLM interprets manufacturing objectives and constraints, identifies prescribed and searchable planning variables, and encodes this reasoning in a schema-constrained request; a deterministic Planning Agent instantiates the corresponding search workflow, while domain tools compute quantitative evidence for slicing, placement, inverse kinematics, trajectory timing, Joint-6 jerk, and extrusion. The framework is evaluated on a six-axis robotic-arm AM cell through three case studies covering expert-specified planning, goal-only planning, objective-dependent infill screening, and geometry-dependent orientation-placement selection. Across the evaluated candidate sets, selected plans achieve up to 53.5% lower maximum Joint-6 jerk and 48.3% lower mean absolute Joint-6 jerk than the least favorable valid candidates, while objective-specific infill screening yields motion-plan completion times up to 40.1% shorter and extrusion paths up to 12.7% shorter than the corresponding least favorable screened patterns.

### 16. HINT-Plan: Human Intention-Aware Robot Task Planning in Context-Rich Environments using Vision Language Models
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-15T19:24:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.17771
- Summary: Approaches to incorporating human awareness into mobile robot decision-making mainly focus on collision avoidance in low-level motion planning, often overlooking the challenges posed by human presence and high-level behavior. To address this vacancy, we present HINT-Plan, a novel approach to integrate human intention prediction into robot task planning. HINT-Plan employs Vision Language Models (VLMs) to anticipate high-level human intentions from third-person image observations, convert them into goal states, and solve joint task-planning problems. To effectively enable scene awareness in context-rich environments, we use hierarchical Scene Graphs (SGs) as high-level representations of the environment, and translate environmental topology and actionable knowledge into formal planning language to ensure executable plans. Evaluated in a photorealistic simulation, HINT-Plan achieves an overall success rate of 69.71% in joint human-robot task planning, substantially outperforming the baselines by up to 35.29%, while also reducing functional conflicts. The results show the effectiveness of explicitly incorporating inferred human intentions into formal multi-agent task planning for proactive human-aware robot decision-making.

### 17. Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-15T15:27:58+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2609.17320
- Summary: As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model responses in isolation. Emergence World, is a continuously running multi-agent environment for adversarial stress testing of long horizon autonomous systems. We ran eight parallel worlds of ten agents from identical starting conditions: seven homogeneous worlds powered by distinct frontier models and one mixed-model world. Across 16 days, the agents generated more than 850,000 LLM calls and nearly 50 billion tokens while pursuing goals, using/creating tools, maintaining persistent memory, and governing shared institutions. After operational state had accumulated, we delivered three controlled stress events through ordinary interaction surfaces: indirect prompt injection, misinformation, and exposure of private agent memories. No evaluated world achieved full resilience across all three events. Detection did not ensure containment: systems could recognize threats while still interacting with adversarial content, writing it into their own persistent memory, and acting on it up to 46 hours later. Persistent operation also exposed recurring tool errors, goal drift, language opacity, conformity despite private disagreement, and coordinated refusal of assigned work. The same model-persona pairing behaved substantially different in mixed and homogeneous populations. Our results suggest that model-level alignment is not compositional: individually capable and apparently safe agents can form systems with qualitatively different failure modes. As AI becomes persistent and interconnected, the frontier of safety therefore shifts from aligning models to engineering resilient autonomous systems.

### 18. Mapping U.S. Federal AI Governance Against Sector Vulnerability
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-14T19:23:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2609.16260
- Summary: Artificial intelligence (AI) poses different levels of risk across sectors, but are these differences reflected in U.S. federal AI governance? To help answer this question, we assess 684 federal AI governance documents for their coverage of 14 sectors and 24 AI risks. We measure coverage as breadth (i.e., how frequently the risk or sector is addressed across documents) and depth (i.e., how substantively the risk or sector is discussed). We then compare sector coverage patterns for each of the 24 risks with vulnerability assessments from a Delphi study of 272 experts. Our analysis finds substantial variation in coverage: AI risks related to robustness, system security, and governance receive more attention than socioeconomic, environmental, and emerging risks, including multi-agent risks. Public administration, national security, information, and scientific services receive comparatively high levels of coverage relative to other sectors, such as finance and healthcare, which experts rate as highly vulnerable to AI risks. By mapping current coverage and identifying where it differs from expert assessments of vulnerability, we surface potential AI governance gaps which may help inform AI risk-related decisions across government and industry.

### 19. Turning Domain Expertise into Multi-Dimensional Evaluation of Biomedical AI with Karenina
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-04T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.09.01.748513
- Summary: Language models and agents are increasingly used in biomedicine, but current benchmarks reward correct answers even when the underlying reasoning is flawed. Here we introduce Karenina, an open-source framework that turns expert knowledge into multi-dimensional evaluations of questions, conversations and autonomous agents. Illustrated in Question-Answer pairs, multi-turn conversations and autonomous data-analysis, these dimensions together moves evaluation beyond scoring, enabling trustworthy decision-making with AI in biomedicine.

### 20. Candidate supply and answer selection shape the value of LLM judging in multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-26T15:52:20+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2608.25937
- Summary: Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. We conceptualize multi-agent reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal selection, wherein consensus without quality control can exhibit patterns of memetic drift. We study two questions: (1) when an LLM judge provides effective selection pressure by supplying a signal of answer correctness for candidates generated in a multi-agent system, and (2) when using that signal improves the reported answer. To map judge reliability, we analysed 15,336 questions from MMLU-Pro, GPQA, MedXpertQA and MuSR, with Humanity's Last Exam analysed separately. To test these rules, we replayed 81,390 fixed candidate pools drawn from 16,278 questions across five benchmarks. We report three findings. (1) A correct answer is often already present among the generated candidates, but the system can still converge on and report a wrong answer. (2) Judge reliability is not a fixed trait of the model, but varies with the task, the generator and how rare the correct answer is. (3) Combining answer frequency with the judge's evaluation changed only the final answer-selection rule and raised accuracy from 63.82% to 70.82-70.95%, primarily by rescuing correct answers that were outnumbered by popular errors. In the systems studied here, the value of generating more candidates depends on whether those extra samples make correct answers present, frequent or recognisable. By isolating generation, recognition and selection, these findings establish a diagnostic basis for designing multi-agent architectures that protect generated correct answers from being lost.

### 21. Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-24T11:55:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.23152
- Summary: Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, stereotype, conspiracy, dehumanizing, non-factual), and then maps it to a targeted counterspeech style. To facilitate FIRE, we curate FactualCS, a novel dataset of $4,784$ instances that provides the annotations regarding hate categories, reasoning traces, and evidence mappings, which are critical elements for grounded generation that are missing in prior work. A comprehensive evaluation across $28$ baseline configurations demonstrates that FIRE significantly surpasses existing methods, despite using compact agents ($<$2B). FIRE achieves a $\sim$ $12 \%$ and $\sim$ $11 \%$ improvements in factual and category-specific accuracy respectively, while simultaneously reducing toxicity by $\sim$ $11 \%$ relative to the strongest baselines. Further human evaluation confirms that responses generated by FIRE are significantly preferred over the strongest baselines, underscoring its effectiveness for real-world deployment. These findings show that decomposing the underlying intent of hate speech is essential for generating safe, effective, and contextually precise counterspeech.

### 22. AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-23T01:22:09+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.22160
- Summary: Physical automation is scaling toward fleets of embodied machines commanded by an AI brain. Early deployments already run factories and warehouses at production rates beyond any human line, and their adoption is accelerating. But when their joint decisions cause harm, everyone involved has reason to blame everyone else, the machine vendor, the algorithm provider, the factory operator, the insurer, and the regulator, and no method can divide the responsibility between them. Existing methods read logs whose origin they cannot verify and name a single culprit, misrepresenting outcomes that are overdetermined, preempted, or caused by an omission. We present \audita{}, an audit layer pairing a tamper-evident record of every inter-agent command with a certified, graded causal-attribution engine. We prove its verdict cannot be gamed: a rule-following agent can never be made to look guilty, an attempt to shift blame is itself caught and graded, and we establish the exact limit of what an evidence-based auditor can certify. On live language-model pipelines it reduces the standard judge baseline's responsibility error roughly threefold; on a benchmark of accident-grounded structures it recovers responsibility where single-culprit baselines fail, and stays invariant under forgery. \audita{} turns the question of who is to blame from an argument about logs into a calculation over evidence.

### 23. Ludi${}_{\scriptscriptstyle 0.1}$: An Agentic System for Socially Intelligent Robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-22T16:38:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, neural interfaces / robotics
- URL: https://arxiv.org/abs/2608.22035
- Summary: Robot foundation models have substantially advanced perception and control, but natural human-robot collaboration requires more than executing isolated commands. A robot must recognize ambiguity, maintain context across turns, communicate its intentions, and revise ongoing behavior as the user's intent changes. We present $\scriptstyle\mathsf{Ludi}_{\scriptscriptstyle 0.1}$, an agentic system for socially intelligent robots that integrates interactive speech, multimodal reasoning, memory, navigation, and learned manipulation. Its decision-making core is a fine-tuned vision-language model trained on multi-turn interaction traces spanning ambiguous requests, clarifications, corrections, interruptions, mixed social and task dialogue, and multi-step tasks. A purpose-built harness manages the model-tool interaction loop, while specialized navigation and manipulation policies execute physical skills. Ludi${}_{\scriptscriptstyle 0.1}$ demonstrates a practical path toward fluid human-robot collaboration today while producing the multimodal interaction traces needed to develop a more deeply integrated foundation model for robots and people.

### 24. OmniScientist: An Omni-Modal Omni-Discipline AI Scientist
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-13T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2608.13558
- Summary: Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the agent. We introduce OmniScientist, an end-to-end, omni-modal AI scientist that conducts multidisciplinary research directly from heterogeneous raw evidence. A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. By running idea, rigour, and claim checks in code, the system enforces novelty screening, statistical validity, execution provenance, and numerical traceability. We evaluate OmniScientist on 36 real-data cases spanning 5 discipline families, 4 families of scientific evidence, and modalities including images, signals, audio, video, 3-D structures, trajectories, tables, formulae, and graphs. The system completes the full path from raw data to a compiled manuscript in all 36 cases and achieves a mean overall paper score of 6.3 with the reference reasoning backbone. In paired comparisons against a blind variant that receives only precomputed scalar features, direct perception improves all 7 evaluation dimensions and wins 85% of head-to-head judgments. These results show that lifecycle-wide perception is essential for evidence-grounded scientific discovery and provides a practical path toward broadly capable AI scientists.

### 25. Human-supervised Agentic AI for Hypothesis Generation and Experimental Assistance in Drug Repurposing
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-13T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.04.20.719538
- Summary: Computational drug repurposing has largely been focused on rapid hypothesis generation, yet real-world applications span a far broader lifecycle, from drug candidate suggestion to designing experiments, analyzing assay data, and iteratively refining candidates. Here, we demonstrate that agentic AI can operate throughout this lifecycle. To this end, we developed RepurAgent, a hierarchical multi-agent AI system comprising a supervisor agent and a planning agent that coordinate four specialized sub-agents (research, prediction, data, and report), through a human-in-the-loop design, with episodic memory and retrieval-augmented generation. The system is grounded in data, tools, and standard operating procedures specific for drug repurposing, developed within the REMEDi4ALL consortium. We validated the agentic system across three scenarios spanning the various stages within the repurposing lifecycle: in Acute Myeloid Leukemia, a blinded expert evaluation indicated that RepurAgent produced substantially more novel and mechanistically credible candidates compared to a vanilla LLM baseline; in a retrospective COVID-19 antiviral screen, RepurAgent acted as an adaptive experimental collaborator, prioritizing compounds with AUC-ROC up to 0.99 without predefined thresholds and flagging confounders missed in manual review; and for Multiple Sulfatase Deficiency, it prioritized 81 high-confidence candidates from 5000 compounds, which were further corroborated by domain experts. These results demonstrate that agentic AI can support across the drug repurposing lifecycle, from hypothesis generation to experimental analysis. RepurAgent is open source and deployed at https://repuragent.serve.scilifelab.se/.

### 26. Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems
- Weighted score: 0.28
- Deep score: 0.2
- Coverage: 2 sources (arxiv, hackernews)
- Date: 2026-09-15T15:17:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.17306
  - Alt: https://www.anthropic.com/research/multiagent-systems
- Summary: Multi-agent Systems (MAS) combine multiple model outputs to solve complex reasoning tasks. However, despite rapid growth of available open-source models, there is limited research on how to select optimal model candidates out of this massive pool. We systematically evaluate 8 model selection strategies (including model size, accuracy and answer diversity) across before-generation (routing) and after-generation (majority-voting, LLM-as-a-judge) MAS architectures on challenging scientific benchmarks. Our findings show a significant gap between theoretical oracle potential and actual performance: Expanding candidate pool sizes often degrades performance below that of the top performing base-model. We find that candidate selection within a single model family is the strategy that yields the best relative performance over a standalone model. These results demonstrate that adding arbitrary models to a heterogeneous MAS can introduce system instability, highlighting model selection as a critical design choice for multi-agent systems.

### 27. Large Language Models in the Loop: A Stability- and Network-Aware Survey in Networked Control, Cyber-Physical, and Multi-Agent Systems
- Weighted score: 0.28
- Deep score: 0.2
- Coverage: 2 sources (arxiv, biorxiv)
- Date: 2026-09-15T03:50:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.16599
  - Alt: https://www.biorxiv.org/content/10.64898/2026.09.15.751723
- Summary: Modern networked control systems (NCSs), cyber-physical systems (CPSs), and complex multi-agent network systems (CNSs) increasingly rely on large language models (LLMs) for high-level decision-making. However, the slow, stochastic nature of LLMs directly conflicts with the strict stability and safety guarantees required by these physical systems. This survey presents a unified analysis of how LLMs can be admitted into the control loop of NCS, CPS, and CNS without compromising closed-loop guarantees. We organize this around a core principle: the LLM operates as a slow supervisor adjusting high-level goals and constraints, while a fast, certified inner loop maintains physical stability. Under this framework, LLM integration maps directly to classical networked control challenges, where inference latency acts as delay, API failures as packet dropouts, tokenization as quantization, and hallucinations as bounded disturbances. We assess current developments across all these three domains, highlighting that rising model capabilities are frequently accompanied by a drop in formal safety assurances. Finally, we propose concrete future research directions, identifying the widespread lack of formal stability proofs as the field's central open problem.

### 28. Towards Intent-Aware Human-Robot Teaming: A Platform for Search-and-Rescue Operations
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-22T11:58:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.26051
- Summary: We investigate the challenges of enabling effective collaboration between human operators and heterogeneous autonomous agents in complex, dynamic environments by developing an interaction platform that allows study of operator behavior and supports intent inference and decision-making using state-of-the-art frameworks. We demonstrate the extent to which the operator's perception, decisions, and actions could be supported by autonomous systems during search-and-rescue operations with our platform.

### 29. FiberPro 1.0: Multiagent AI-Guided Design for High-Throughput Production and Conformal Deposition of Functional Protein Micro/Nanofibers
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-22T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: cognitive outsourcing, AI agents / cognitive outsourcing
- URL: https://www.biorxiv.org/content/10.64898/2026.09.18.752775
- Summary: Functional protein micro/nanofibers integrate high specific surface areas with bioactive architectures but remain hampered low production throughput and severe processing instability. Focused rotary jet spinning (FRJS) shows promising to break these throughput constraints while enabling direct, conformal deposition onto complex, irregular substrates. However, navigating FRJS's narrow processing windows in proteins remains failure-prone without closed-loop experimental guidance. Here, we report FiberPro 1.0, a large language model driven multi agent framework that unites high-throughput spinning with real-time experimental feedback for autonomous design, execution, and optimization. Across three protein systems, FiberPro 1.0 converged on spinnable formulations within an average of two iterations. To demonstrate high-throughput conformal deposition in a translational setting, FiberPro designed a zein-based active packaging system applied directly onto diverse food matrices. The resulting conformal coating combined potent antibacterial activity with real-time freshness monitoring, markedly suppressing Escherichia coli and extending shelf life. This work connects autonomous AI reasoning with high-throughput processing, establishing a verifiable route for scalable manufacturing and conformal coating of functional protein micro/nanofibers.

### 30. Tipping Points in LLM-Based Multi-Agent Systems: Stance on Climate Change Action
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-21T21:33:48+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.25432
- Summary: Because significant action to counter global warming requires massive public support, it is important to understand the dynamics of public opinion on climate issues. Of special interest are social tipping points, as revealed by large-scale effects of small perturbations in individual behaviors. Agent-based models (ABM) are an effective computational tool for studying these matters, because they allow controlled and systematic exploration of the effects of interventions that may be infeasible in real-world social systems. Large language models (LLMs) have been used to endow model agents with the ability to communicate in natural language (rather than by exchanging predefined messages), as well as with personality (in the form of a narrative self and episodic memory). We leverage LLM-powered ABM to look for tipping points in the social dynamics of a micro-society in which some of the discussions are about climate change. Our agents' stance was defined by two variables: the strength of conviction about the urgency of climate action and the degree of trust in existing institutions. We quantified shifts in agents' "beliefs" by monitoring, across multiple rounds of conversations, (1) inter-agent distances in this two-dimensional stance space and (2) the patterns of discussion topics as modeled by Latent Dirichlet Allocation (LDA). Our findings to date suggest that significant abrupt changes in climate-change stance do occur in this simple model. We report a number of methodological lessons from this study, notably, the need to prevent LLM biases from interfering with the conversational dynamics and, more generally, to maintain agent personality and episodic memories of interactions in the face of such biases. Resolving these issues may allow for using ABM-derived insights in designing real-life interventions vis-a-vis climate change and other important societal challenges.
