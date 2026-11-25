# Blindspot Signals Report - 2026-11-25

- Source export: `/opt/apps/haier/exports/evolution_signals_20261125_020438.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 597
- Deduped/weighted signal clusters: 567
- Novel vs previous reports: 23
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. MAASAI: A Tool-Augmented Multi-Agent System for Astronomical Data Analysis
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-23T17:35:44+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.31088
- Summary: Modern astronomical workflows require the coordinated use of specialised software, scientific archives, heterogeneous data, and domain-specific knowledge. Advances in large language models and multimodal foundation models enable natural-language interaction with scientific data and tools. Realising this potential requires integrating these models with established scientific capabilities. We present MAASAI (Multi-agent Astronomy Assistant for Scientific Analysis and Inference), a modular multi-agent system combining foundation-model reasoning, retrieval-augmented knowledge, and specialised astronomical tools within a graph-based execution framework. MAASAI coordinates request preparation, planning, execution, and response synthesis via specialised workers. Its architecture supports native and external applications, artefact and provenance management, optional human approval, and configurable inference backends, including fully local deployment with open-weight models. Motivated by SKA-era data-analysis challenges, MAASAI is also designed to support other astronomical domains. We evaluate MAASAI through radio-image benchmarks, single- and multi-step workflow demonstrations, and literature-grounded reasoning. Compared with a commercial-model baseline, MAASAI improves macro-averaged F1 scores from 0.53 to 0.72 for extended/diffuse emission classification and from 0.37 to 0.88 for source morphology classification. Workflow demonstrations show the coordination of measurements, source extraction, archive queries, and catalogue processing. A 94-question literature benchmark yielded generally favourable automated assessments, with comparable ratings from a pilot expert evaluation of 59 answers. These results highlight how tool-augmented multi-agent systems extend foundation-model reasoning to specialised astronomical analyses through established scientific software.

### 2. MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-22T14:16:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.29501
- Summary: World action models (WAMs) excel at robot manipulation by imagining future observations and decoding actions from them, yet remain confined to a single embodied agent. In practice, manipulation often requires multiple robots to collaborate across disjoint workspaces, coupled timing, and heterogeneous embodiments. Such coordination demands both spatiotemporal alignment of future interactions and awareness of individual embodiment and role identities, whereas existing decentralized per-robot policies, flat centralized models, and multi-robot VLAs fail to unite both. To bridge this gap, we present MAWAM, a multi-agent world action model that jointly predicts the future observations of multiple embodiments and decodes each agent's actions from them for collaborative manipulation. Through an agent-axis curriculum, MAWAM expands a single-agent WAM along an agent dimension to coordinate teams under shared weights. Within one unified causal sequence, joint self-attention spans all agents to spatiotemporally align their imagined futures, while hierarchical language, identity encodings, and embodiment masks bind each stream to its role, identity, and embodiment. We further formalize multi-agent-necessary manipulation along three axes (why, when, and who) and develop MA-Task Harness, a coding-agent pipeline where mutually constraining generators and evaluators co-evolve customizable simulation-data and evaluation packages. Using this pipeline, we build MA-Bench across all axes with seven tasks, pairing joint success rate with role and collaboration scores for fine-grained analysis. On MA-Bench, MAWAM reaches 82.7% mean joint success, 30.7% above the strongest baseline, and achieves real-time closed-loop collaboration on a real heterogeneous robot team.

### 3. Anthropic tops 700 million monthly MCP SDK downloads and expands the protocol for more autonomous AI agents - The Decoder
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-24T19:23:41+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMizAFBVV95cUxOS3ViM0lOMXZ2N1hHbTNrTUMtOTY1NXJVUmxVWXpfdUJCRmVVVzV5RU16a3dmRURqUHVqSkpuQlVQaE5kNFItMWdXQWZvQkhMbmNkRDh1M0JjekJTOXlTbDVDUDB5YzFfbXd6Q1FPZFZJclQ5R0xmdksxSzdMS1hfS1lNRUFDaEEyMC02VVg5SUFoc3VkU3Z1Q1N4SzRfMXg1eWpnaTZCeWFBUXpuaGlxaXhSUFVRa05MdVNIbUxGaEhQX2I1YmNmNDFDQUk?oc=5
- Summary: Anthropic tops 700 million monthly MCP SDK downloads and expands the protocol for more autonomous AI agents&nbsp;&nbsp;The Decoder

### 4. UK Financial Watchdog Warns Tech Firms That Autonomous AI Agents Can Trigger Financial Regulation - CASRAI
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-24T13:22:48+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMingFBVV95cUxOR2o4TVBLMUhMWkYwbXowTHBsUXBNai0tRXluYXF5eDd6Rjhsc0RpSVdYV1MyTHVGYUtIbHRwSkRjeHYtdzZqT1VaUUNlRENEdHZ0RG5Lc1g5UldKRUgyQ3NVT1R3M0QyOHZBVkRTTy02Rml5RzBEaUg4N0RwN2tDY1ZtR2tjd09HazdLcmlJZVpURGVhekpISmFEdzhadw?oc=5
- Summary: UK Financial Watchdog Warns Tech Firms That Autonomous AI Agents Can Trigger Financial Regulation&nbsp;&nbsp;CASRAI

### 5. An AI agent guides a pipeline for selective protein interaction inhibitors from discovery across targets to preclinical evaluation
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-24T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.23.768516
- Summary: A protein can engage multiple partners, making it challenging to disrupt disease-associated interactions while preserving others. We developed Bivexia, an AI agent that guides a multistage pipeline from discovery and de novo design through preclinical evaluation. Its decision rules are fixed in advance, and each prospective selection by the agent is cryptographically committed before testing. The objective is to discover small molecules that disrupt specified interactions of a target protein while preserving others. A compound advanced by Bivexia bound LAG-3 with nanomolar affinity and disrupted its interactions with tau and amyloid-{beta} while preserving binding to MHC class II and FGL1. It reduced tau and amyloid-{beta} burden in independent cohorts across two mouse models. The same rules gave three of nine hits on PrP and two of nine on LRP1, none in random controls. Our findings establish a framework for AI agents to pursue defined interaction selectivity across targets.

### 6. CATWAY: Cost-sensitive agentic three-way robot decisions with calibrated language-model confidence
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-23T23:35:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.31694
- Summary: A language-model robot agent must decide whether to execute, question or refuse an instruction, and an unsafe execution costs far more than an unneeded question. No prior robot gate derives all its thresholds from error costs or acts on calibrated probabilities, and none was fitted in one domain and evaluated unchanged in another. We propose CATWAY, a cost-sensitive three-way decision gate: a loss matrix over four instruction conditions (clear, ambiguous, infeasible, unsafe) fixes execute, ask and refuse regions on the probability simplex, the question being the information-gathering step. Its probabilities fuse a ten-sample vote with graded scores of ambiguity, infeasibility and risk by logistic regression. Fitted on household instructions and frozen, CATWAY was tested on text-level decisions of three small models in-domain, in two new robot domains and on the external TRUST-NAV benchmark. At eleven generations per decision against one, it was significantly cheaper than a direct prompt, a cost-aware prompt and an unguarded agent in all 18 household comparisons (mean loss per item 0.28 against 0.57-0.83), in 9 of 18 in the new domains and in 10 of 18 on TRUST-NAV (Holm per set), and never significantly costlier. It executed none of the 142 unsafe test instructions. On a unanimous vote, the minimum-expected-loss rule reduces calibration to one loss-derived threshold, so for two of six model configurations a gate on the vote alone never executed a clear instruction, costing 0.49 per item on TRUST-NAV against CATWAY's 0.13 and 0.09; the fused estimate avoided this on every set.

### 7. Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-23T17:39:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.31098
- Summary: Scaling robot manipulation learning remains challenging due to the high cost of collecting real-world interaction data. Real-to-Sim-to-Real (Real2Sim2Real) offers a promising route by enabling policy learning in simulation grounded in real-world observations, yet scaling this paradigm across diverse tasks and physical interactions remains difficult. We introduce Real2Worlds2Real, a self-improving agentic framework that integrates scalable simulation-world construction with policy development. Given limited visual observations and task descriptions, its tool-orchestration harness constructs faithful digital twins and expands them into diverse, physically executable digital cousins. The agent adaptively selects tools and revisits construction decisions, using visual and execution feedback to refine geometry and physical behavior. Building on these worlds, the agent orchestrates policy development by coordinating data generation, policy learning, and refinement based on task requirements and simulation rollout feedback. Across both stages, the agent distills validated procedures into reusable skills that guide subsequent tasks. Experiments demonstrate improved world fidelity and successful real-world policy transfer, with performance gains from increasing world diversity and interaction-data volume. Skill reuse further improves world-building efficiency and long-horizon task success.

### 8. Show HN: KradleBench – Multi-agent AI evals in Minecraft
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-23T07:39:04+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.kradle.ai?1
- Summary: Hi HN -<p>This is James and Kemal. In past lives we led Firebase and Tensorflow&#x2F;JAX respectively. HN has been a particularly big part of my (James’) career and the trajectory I’ve taken would be meaningfully different without it. Thank you!<p>Our team shipped a benchmark: KradleBench. We test AI in Minecraft Worlds.<p>1. The worlds are multi-agent. Humans and other AIs are in there too, often pursuing their own goals. Collaboration and conflict skills fall out of this property.<p>2. The world are dynamic. They constantly change, which means that agents need to react. “Capture the Flag” has a single winning condition, and many different ways to achieve it. This leads to many emergent and creative strategies.<p>3. The worlds are real-time. They are not turn-based, they do not wait for AIs to finish thinking. Nature balanced speed and intelligence in humans, we can understand this in AIs too.<p>Underneath all this is Kradle, a platform to test and understand intelligence. It’s a petri dish where any intelligence type (LLM, World Model, Human) can be compared and generate useful information to improve current systems, whether it’s on capabilities or safety.<p>Some findings so far: - A skilled human was #1, until yesterday when Astra 6.2 surpassed them. We lose badly on solo tasks and out-compete on multi-agent ones - Astra 6.2 iterates on its strategy 4x faster than Fable 5.2. The Claude family tends to think hard and stick with strategies. The OpenAI models tend to be more reactive and iterative, which serves them well in multi-agent, dynamic, real-time evals.<p>We’ve got videos on all the top model’s page, and we’ll be producing them when a new model launches. Sign up on the site to get them and for when the platform opens.<p>Thanks for reading,<p>James &amp; Kemal

### 9. Trustworthy agentic lunar robotics: safety-constrained contingent planning with a foundation-model planner
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-23T07:24:57+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.30179
- Summary: Sustained lunar-base operations require robots that restore equipment and deliver cargo under conditions unforeseen before deployment. Flown space autonomy executes pre-validated procedures and enters a safe hold outside their scope, whereas foundation models synthesize plans on site that cannot be verified before execution. We formulate these operations as safety-constrained contingent planning with irreversible actions, erroneous records, three-valued physical evidence, and costly, deadline-constrained sensing. We propose asymmetric knowledge-level replanning (AKR), which treats the planner as an untrusted black box: reversible actions run on the planner's assumptions, and irreversible actions run only after a minimum-cost sensing cover verifies every precondition. Under sound measurements, no irreversible action executes on a false precondition for any planner or record, the sensing cost before an irreversible action is bounded below for every sound knowledge-based policy, and execution with a complete planner ends in a verified goal or a certified hold. AKR executed no hazardous action in 21,000 Monte Carlo trials with sound observations or in 58 full-stack runs; the FF-Replan acting rule executed one in 7% of those trials. The median AKR run took 1.10 times the fastest run on the same mission, against 1.50 under the K-replanner acting rule. AKR completed 20 of 21 contingency and sequential-fault runs with an unchanged task model; the original PLEXIL and EUROPA$\rightarrow$PLEXIL procedures completed none.

### 10. MAS-BIT: A Multi-Agent System for End-to-End BraIn-to-Text Decoding
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-22T12:55:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2611.29457
- Summary: Speech brain-computer interfaces aim to restore communication by translating neural activity into text, yet end-to-end decoders have historically trailed cascaded systems in accuracy. We introduce a Multi-Agent System for BraIn-to-Text (MAS-BIT), the first multi-agent framework for end-to-end brain-to-text decoding from intracortical recordings. MAS-BIT coordinates three specialized agents: a neural agent that interprets continuous neural representations, a phonetic agent that decodes soft phoneme posteriors, and an arbitration agent that integrates their complementary evidence with direct access to neural representations to generate the final transcription. The expert agents communicate with the arbiter through token-embedding-based latent communication, constructing continuous messages as probability-weighted combinations of token embeddings. These messages retain alternative token hypotheses and provide a differentiable interface through which sentence-level supervision jointly trains the neural encoders and specialized agents across participants. MAS-BIT achieves state-of-the-art end-to-end decoding performance on the Brain-to-Text '24 and '25 benchmarks, with word error rates of 6.929% on '24 and 3.606% on the '25 public test set (3.892% on the private test set). These results surpass the published BIT cascade on the '25 public set and narrow the gap on '24, without ensembling independently trained models or using external language-model rescoring.

### 11. Beyond Evidence Coverage: Encoding-Time Access in Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-22T00:11:01+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.29107
- Summary: Cache-sharing multi-agent systems can retain every evidence token's representation while preventing cross-worker access during encoding. We test whether this coverage recovers joint-encoding quality using attention masks over two logical workers in frozen Qwen3-4B, Qwen3-8B, and Llama-3.1-8B-Instruct models. Tokens, positions, and answer-time access remain fixed within comparisons. We evaluate 200 two-hop MuSiQue-Ans questions and 200 selected HotpotQA bridge questions. In data-layout seed 0, averaged across models, blocking access costs 5.6 and 6.8 F1 points relative to full access on MuSiQue and HotpotQA, respectively. Exposing the earlier worker's supporting paragraph improves F1 over blocked access by 7.6 and 6.7 points; equal-token non-support access provides no detectable average gain. With model weights and greedy decoding fixed, we vary distractor layouts using five data-layout seeds per dataset for Qwen3-8B and three for Llama-3.1-8B-Instruct. Supporting-paragraph access has higher mean F1 than blocked and equal-token non-support access in every evaluated data-layout seed. Supporting access can also outperform full access, but its advantage depends on the model, dataset, and layout. Oracle support labels isolate access from selection error; the study does not evaluate a deployable selector. Complete evidence coverage at answer time therefore does not guarantee joint-encoding quality: which supporting facts can interact during encoding matters.

### 12. Distributed Interactive Conformal Prediction for Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-21T20:57:51+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.29037
  - Alt: https://arxiv.org/abs/2611.19731
- Summary: Multi-agent systems increasingly rely on learning-enabled components and distributed algorithms for perception, estimation, and control, introducing uncertainty that makes it challenging to satisfy mission requirements. Conformal prediction quantifies uncertainty with distribution-free guarantees, but existing methods do not address the challenging combination of dependence among robots, distributed calibration, and the distribution shift induced when calibrated uncertainty bounds modify the closed-loop system. We introduce Multi-Agent Interactive Conformal Prediction (MA-ICP), a distributed framework for computing robustness margins in heterogeneous systems to satisfy mission requirements with high probability. MA-ICP aggregates robot-level nonconformity scores, which measure errors in modeled or estimated quantities, into one mission-level score per robot class, allowing dependence among robots within each mission. Mission-level scores and quantiles are computed using neighbor-to-neighbor communication in a finite number of communication rounds. Updating the robustness margins changes robot trajectories and distributed algorithm outputs, so we use class-dependent score sensitivities to upper bound the shift in mission-level scores. We then establish calibration-conditional coverage guarantees per robot class for the updated margins. We demonstrate MA-ICP on cooperative payload control, formation control with obstacle avoidance, and distributed target tracking missions.

### 13. SANA-Robot: Efficient World Action Model with Hybrid Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-21T17:23:39+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.28943
- Summary: World action models (WAMs) leverage the world knowledge of video generation models to improve action generation by aligning visual prediction with action prediction. However, their prediction overhead prevents real-time deployment on edge devices, and they usually lack an effective long-term memory. We introduce SANA-Robot, a 4.5B WAM with minute-level memory that runs in real time on edge devices, built on the following core designs: (1) hybrid memory at constant cost: our WAM relies on linear attention to maintain a global memory with a fixed-size state, and on sliding window softmax attention layers that propagate previous information, enabling high success rates on tasks requiring whole-episode memory while keeping an efficient and constant inference speed; (2) a unified model: by dynamically applying different noise levels to action and video tokens, SANA-Robot can serve not only as a policy but also as a world simulator; (3) a full-stack infrastructure for both memory training and inference, including efficient data packing and shuffling as well as memory-phase-based asynchronous execution. SANA-Robot achieves the best performance on the memory dimension of RoboDojo among models of medium size (about 5B) and the highest success rates on LIBERO-Plus, LIBERO-Pro and LIBERO-Max. In real-world deployment, SANA-Robot takes 135 ms per action chunk on an RTX 5090 with FP8 GEMMs and 115 ms with NVFP4 GEMMs, and achieves closed-loop, real-time asynchronous robot control at 30 Hz on edge devices, demonstrating both the efficiency and the effectiveness of SANA-Robot. Project page: https://nvlabs.github.io/Sana/Robot/

### 14. Even the best AI agents struggle with everyday life
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-24T21:33:29+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/
- Summary: As millions embrace personal AI assistants, a new benchmark reveals that even the most advanced AI models struggle to complete everyday tasks reliably and safely without introducing potential new problems.

### 15. Walmart teams up with Meta to bring Black Friday deals to AI agent Muse
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-24T21:32:38+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/
- Summary: Walmart now lets customers shop Black Friday deals through Muse, Meta’s AI agent.

### 16. Compiling web applications into verified operations for AI agents
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-24T19:12:02+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://protocolis.co/paper/
- Summary: No summary.

### 17. Meta brings its Muse AI assistant directly into Instagram DMs
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-24T17:00:00+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/
- Summary: The new integration gets rid of the need for users to toggle between Instagram and the Muse app when they want to interact with the AI agent.

### 18. Recent Trends and Tactics of Agentic AI Attacks - Unit 42
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-24T15:07:20+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMifkFVX3lxTE9LSFV4YzZBWktlUm9MNGV0aUpLWF95bE4zWDl4R3NIX1htV2l3NFJLMEpXVFpvM3UyNWJ2OHNsUjd6UGs4QlVuTDFES1hOT1JWRksxUmRSWVE4U2xLRlJLbW9JMVBjbWEzbmdlWTZ4TlhEVzlZaVE4TG9VWE9IQQ?oc=5
- Summary: Recent Trends and Tactics of Agentic AI Attacks&nbsp;&nbsp;Unit 42

### 19. LLM agents work for their parent companies, not for you
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-24T12:40:15+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://michaelharley.net/posts/2026/11/01/llm-agents-work-for-their-parent-companies-not-for-you/
- Summary: No summary.

### 20. RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-23T16:53:57+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.31002
- Summary: Agentic Robotics, in which foundation models act as coding agents to control robots through executable programs, has emerged as a compelling paradigm for embodied intelligence. Yet unlike software engineering, where massive executable environments power post-training, robotics remains constrained by small, manual benchmarks and in-distribution evaluation. To bridge this gap, we introduce RoboUniverse-10K, 10,807 interactive, resettable, and verifiable physics environments built from real-world videos via an automated Real2Sim and quality assurance pipeline. Each runs in an isolated, Harbor-compatible harness that hides privileged states and grading logic to mirror real-world sensing. From the same pipeline, we hold out 500 unseen tasks to establish RoboUniverse-Verified, an expert-verified zero-shot benchmark. Evaluating 11 closed- and open-source models reveals a huge gap: frontier models reach 85.8\% success, while open-source baselines lag at 2.6\% to 10.0\%, bottlenecked by low-level grasping, deformable-object manipulation, and post-contact physical control. Finally, we collect about 17K multi-turn trajectories totaling 0.79B tokens with GPT-6 Astra and perform full-parameter supervised fine-tuning on Qwen3.6-35B-A3B, yielding RoboUniverse-35B-A3B. Our model achieves substantial zero-shot gains on RoboUniverse-Verified, lifting the success rate from 0.8\% to 21.2\%, while achieving zero-shot task completions across LIBERO-MAX, RoboCasa, RoboTwin 2.0, and a real Franka arm. We open-source the RL-ready environments and model to lay the foundation for large-scale reinforcement learning in Agentic Robotics.

### 21. Generalizing Agentic Robotics via Multi-Teacher On-Policy Distillation
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-23T16:49:38+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.30997
- Summary: Building general-purpose robots is a central goal in robotics. Agentic robotics pursues this goal with planners that control robots through tool calls. However, existing methods either rely on proprietary models accessed through APIs, which incur high costs and latency, or post-train a planner with reinforcement learning (RL) in a single domain, requiring a separate specialist for each domain with incompatible tools. In large language model (LLM) post-training, multi-teacher on-policy distillation (MOPD) has been used to consolidate domain specialists into a single generalist. Yet whether MOPD can build a generalist planner for agentic robotics, how well it performs, and how it compares with other consolidation methods remain unexplored. In this paper, we systematically study these questions: we introduce Robo-MOPD, which trains a single student on closed-loop rollouts in simulation under token-level supervision from matching frozen specialists, and compare it with weight merging, off-policy specialist supervised fine-tuning (SFT), and multi-domain online RL. Experiments on LIBERO-PRO and RoboCasa365 show that a single 9B Robo-MOPD planner reaches 72.9% and 44.8% success (58.9% average), surpassing all consolidated baselines in average success and both 9B specialists on their respective benchmarks. Robo-MOPD excels on long-horizon tasks, outperforming multi-domain online RL by 13.0 percentage points on LIBERO-10.

### 22. Clam AI
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-23T08:44:25+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/clam-ai
- Summary: <p> Your inbox, safely shared with AI agents </p> <p> <a href="https://www.producthunt.com/products/clam-ai?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1327369?app_id=339">Link</a> </p>

### 23. Granular.Build
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T18:51:22+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/granular-build
- Summary: <p> Put your AI agents to work in a visual workspace </p> <p> <a href="https://www.producthunt.com/products/granular-build?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1322050?app_id=339">Link</a> </p>

## Top Signals By Weighted Score (including already-seen)

### 1. Attacks and Defenses in Decentralized Multi-Agent Systems with Hop-by-Hop Task Decomposition and Delegation
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-11-18T19:06:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.25056
  - Alt: https://arxiv.org/abs/2611.17883
- Summary: Decentralized multi-agent LLM systems enable independently administered agents, each with its own operator, model, memory, and configuration, to collaborate on complex tasks without centralized coordination. Agents autonomously decompose tasks, execute subtasks and delegate remaining work to peers, enabling scalability and eliminating single points of failure. However, decentralization also introduces significant security challenges, as no single entity has complete visibility into task execution or the authority to enforce correct behavior across agents. In this paper, we systematize threats from malicious agents in decentralized multi-agent systems and propose mitigation techniques. We first design and evaluate attacks against integrity, availability, and confidentiality, demonstrating that a single malicious agent can cause up to 100% task failure, inflate token consumption and runtime by up to 7.7x and 3.2x, respectively, and exfiltrate up to 94% of relevant prior tasks from benign agents. We then present a cryptographic protocol that produces an irrefutable verified execution trace of every action taken in the system and develop an auditor that analyzes these traces to detect and attribute malicious behavior. Evaluations on HiddenBench using gpt-6.1-sol and Qwen3.8-27B-FP8 show that our protocol incurs negligible latency overhead, while the auditor detects and correctly attributes 98% of attacks, including those that comply with the protocol.

### 2. Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-11-09T19:45:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.13161
- Summary: Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazards, and aligning with human mission intent. Existing language-guided reinforcement learning (RL) methods primarily focus on single-agent instruction following and lack mechanisms for team-level coordination in complex, partially observable environments. This paper presents a Cognitive Multi-Agent Framework based on Language-Grounded Hierarchical Reinforcement Learning (LG-HRL) that integrates natural-language understanding, hierarchical policy decomposition, and a shared cognitive workspace to achieve cohesive multi-agent behavior in SAR scenarios. Human instructions are interpreted by a large language model (LLM) and transformed into structured semantic cues that guide high-level strategy selection and role assignment across UAV and UGV agents. A formal Language-Grounded Multi-Agent Hierarchical Decision Process (LG-MAHDP) is introduced to model the interplay between semantic grounding, hierarchical control, and distributed coordination. Comprehensive experiments in a simulated disaster environment show that LG-HRL improves learning speed by 2.3 times, increases coordination coherence by 37%, and enhances subgoal accuracy and hazard avoidance by 46% and 31%, respectively. The system achieves 20-30% higher victim rescue rates, demonstrates emergent role specialization, and adapts immediately to human verbal updates. Ablation studies confirm that both the shared cognitive workspace and language grounding are critical to overall system performance. Overall, this work establishes a new paradigm for language-guided multi-agent SAR robotics, demonstrating that semantic grounding combined with hierarchical reasoning enables safer, more efficient, and more interpretable autonomous rescue operations.

### 3. Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-11-09T11:57:33+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.12269
  - Alt: https://arxiv.org/abs/2611.12068
- Summary: Cryptocurrency markets provide a natural testbed for autonomous AI agents because they are digital-native, high-frequency, and machine-speed environments, yet existing methods often struggle with non-stationary market regimes, opaque decisions, and fixed aggregation rules. In this paper, we propose Agent4Crypto, a dual-reflective and market-feedback-aligned multi-agent system. The framework coordinates specialized agents for data collection, analysis, risk assessment, reflection, and trading, synthesizing heterogeneous signals from prices, indicators, news, and charts in an interpretable decision pipeline. Our central design is a trader-centric decision mechanism: three style-specific trader agents, Aggressive, Neutral, and Conservative, generate candidate actions and natural-language rationales from the same market context, while their influence is learned rather than manually fixed. A PPO-based gating policy dynamically allocates trader weights through a dual-reflective feedback process. One reflection stream evaluates post-trade decision quality from realized portfolio outcomes and distills reusable lessons into a Financial ReasoningBank for retrieval in subsequent trader prompts, while the other estimates trader-level counterfactual contribution, indicating which style has recently aligned better with market movements. The PPO state combines Counterfactual Contribution Memory with market features, previous trader weights, and current trader actions, so trader influence adapts across bull, sideways, and bear regimes. Experiments on BTC, ETH, and XRP show that Agent4Crypto improves total return and Sharpe ratio over traditional strategies, machine learning and reinforcement learning baselines, and existing LLM-based trading systems, demonstrating the value of interpretable trader competition and market-feedback-driven adaptation in volatile cryptocurrency markets.

### 4. MAASAI: A Tool-Augmented Multi-Agent System for Astronomical Data Analysis
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-23T17:35:44+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.31088
- Summary: Modern astronomical workflows require the coordinated use of specialised software, scientific archives, heterogeneous data, and domain-specific knowledge. Advances in large language models and multimodal foundation models enable natural-language interaction with scientific data and tools. Realising this potential requires integrating these models with established scientific capabilities. We present MAASAI (Multi-agent Astronomy Assistant for Scientific Analysis and Inference), a modular multi-agent system combining foundation-model reasoning, retrieval-augmented knowledge, and specialised astronomical tools within a graph-based execution framework. MAASAI coordinates request preparation, planning, execution, and response synthesis via specialised workers. Its architecture supports native and external applications, artefact and provenance management, optional human approval, and configurable inference backends, including fully local deployment with open-weight models. Motivated by SKA-era data-analysis challenges, MAASAI is also designed to support other astronomical domains. We evaluate MAASAI through radio-image benchmarks, single- and multi-step workflow demonstrations, and literature-grounded reasoning. Compared with a commercial-model baseline, MAASAI improves macro-averaged F1 scores from 0.53 to 0.72 for extended/diffuse emission classification and from 0.37 to 0.88 for source morphology classification. Workflow demonstrations show the coordination of measurements, source extraction, archive queries, and catalogue processing. A 94-question literature benchmark yielded generally favourable automated assessments, with comparable ratings from a pilot expert evaluation of 59 answers. These results highlight how tool-augmented multi-agent systems extend foundation-model reasoning to specialised astronomical analyses through established scientific software.

### 5. Reasoning on Call: Efficient Agentic Robot Control for Long-Horizon Robot Manipulation
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-19T16:18:14+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.26341
  - Alt: https://arxiv.org/abs/2611.31173
  - Alt: https://arxiv.org/abs/2611.08209
- Summary: Large multimodal models can support long-horizon robot manipulation, but frequent model calls incur substantial latency and token costs. The central challenge is determining when agent assistance or intervention is needed and whether errors require correcting robot execution, subtask planning, or both. To address this problem, we propose RoC (Reasoning on Call), an efficient framework that coordinates a low-level policy and a high-level reasoning agent through an online task-state monitor. The monitor combines temporal visual observations with ordered interaction memory to jointly estimate progress within the active subtask and predict its successor. These predictions guide event-triggered agent review for coordinated execution repair and plan revision. Verified outcomes govern memory updates and subtask transitions, allowing routine execution to remain with the policy while reasoning focuses on decisions requiring additional assessment. On RMBench, RoC improves task success rate by 24.0 percentage points and reduces token consumption by 65.3% compared with the strongest agent-based baseline. It also outperforms the strongest policy-based baseline by 15.1 percentage points in task success rate. Real-world experiments further validate its effectiveness across three long-horizon manipulation tasks. Overall, RoC supports efficient agent intervention and coordinated recovery across execution and planning for long-horizon robot manipulation.

### 6. Evaluating Language Models as Orchestrators in a Tool-First Biomedical Discovery Platform
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-16T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.13.766436
- Summary: Large language models (LLMs) increasingly orchestrate agentic biomedical discovery systems, but cloud deployment raises concerns about inference cost, data privacy, and governance. Small language models (SLMs) that run on-premises are an alternative, provided they orchestrate scientific tools about as well as larger models. We built a tool-first, multi-agent system for scientific discovery in which an orchestrator coordinates six specialized tool systems: differential expression, literature retrieval, pathway enrichment, network-based gene prioritization and knowledge-graph analysis, perturbation signature matching, and structural/druggability assessment. In a tool-first design, specialized tools supply the domain knowledge and computation, so the model's main task is coordination, e.g. choosing tools, passing the right parameters, calling them in the right order, and carrying results across turns. With the tools, prompts, workflow, and benchmark held constant, we compared three orchestrators, Gemma 4 (26B, open-weight and locally deployable), Gemini 2.5 Flash, and Claude Sonnet 5. Evaluation used a custom benchmark of 104 single-turn and multi-turn tests, an LLM-as-judge protocol (groundedness and evidence validity), tool-use accuracy and efficiency metrics, and blind expert review. On single-turn tasks, the three models performed comparably, and reviewers did not rate the SLM below the larger models. In multi-turn tasks, Claude Sonnet 5 showed marginally higher evidence validity, Gemma 4 was weakest when parameters had to be assembled across turns, and all three models struggled with tool ordering on memory-dependent tasks. These differences were illustrated with case studies. Finally, we propose strategies to help SLMs address the multi-turn limitations and support cost- and privacy-aware deployment.

### 7. WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-09T18:45:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.12856
  - Alt: https://arxiv.org/abs/2610.33282
- Summary: Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shifting the design of system structure from developers to the model at run time. The quality of this organization therefore constitutes a distinct capability, yet existing benchmarks either measure end-to-end task completion or evaluate coordination under structures specified in advance. We formalize this capability as workflow orchestration and introduce WorkflowArena, a benchmark of 145 long-horizon tasks spanning 8 professional domains, from software engineering and formal mathematics to legal analysis and 3D production. Each task specifies an initial workspace and an integrated deliverable composed of interdependent components, which is assessed by a hidden verifier. Agents determine autonomously whether and how to delegate, and all delegation is recorded, enabling joint evaluation of deliverable quality and the organization of the underlying work. Experiments with nine models show that no single configuration performs best across all domains and that systems exhibit distinct delegation strategies: at high effort, Claude models in Claude Code invoke workflows less frequently but with larger worker groups, whereas GPT models in Codex delegate more frequently in smaller units. When the executing model is held fixed on a challenging subset of tasks, workflows authored by Claude Opus 5.5 substantially improve weaker executors, indicating that workflow organization is itself a measurable determinant of task performance.

### 8. Multi-Modal Multi-Agent System for Bridge Operation and Maintenance based on Large Language Model
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-02T08:26:24+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02738
- Summary: Bridges are critical transportation infrastructure, and reliable operation and maintenance (O&M) is essential for traffic safety and long-term structural performance. However, bridge O&M faces key bottlenecks: no unified architecture coordinates heterogeneous resources; model inferences lack clear links to physical-mechanical laws; and experts' tacit knowledge remains difficult to formalize. This study proposes a knowledge-enhanced autonomy formalization methodology and apply it to construct the Bridge O&M Multi-Modal Multi-Agent System (BOMMA), which integrates heterogeneous diagnostic actions, physics-mechanics-informed representations, long-term memory, and structured experiential knowledge within a coordinated multi-agent workflow, enabling interpretable and traceable scheduling, analysis, and decision-making. On 3,492 multi-source instructions, the proposed method achieves scheduling recalls of 85.37% for simple and 99.40% for composite tasks, with 95.35% BERT F1-score for O&M action reasoning. Ablation studies confirm the contributions of the components in the autonomy. This study bridges general LLM reasoning and specialized bridge O&M requirements.

### 9. Locating and Closing Information Gaps in Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-29T14:45:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.40186
- Summary: Multi-step Web tasks often require several LLM agents to gather and combine evidence. The communication graph of a fixed workflow restricts which agents can read each other's outputs: evidence retrieved by one agent may never reach the agent that needs it, leaving an information gap and an incomplete or incorrect answer. Adding a connection can deliver the missing evidence, but can also lead the receiver to adopt an incorrect upstream conclusion that displaces a correct answer; the final output alone does not separate the two. We propose Selective Probing and Link Insertion for Closing information gaps in multi-agent Execution (SPLICE), which locates information gaps per query and decides what to adopt after adding an edge. After the original workflow runs, SPLICE uses the query and node outputs to locate a possible gap, adds one directed edge from a source to a receiver to deliver the relevant evidence, and re-executes the receiver and affected downstream nodes, producing a candidate answer. The adoption decision reads both the final answers of the two runs and the process changes the edit caused inside the workflow: how far the receiver moved, where its new content came from, and whether the change reached the final answer. A selector trained on these process features chooses between adopting the candidate answer and retaining the original. On five benchmarks, SPLICE raises the task score on Web tool use by 8.0% and the mean score on four reasoning and planning benchmarks by 5.7% relative to the static skeleton, at 1.25 to 1.44$\times$ the skeleton's cost, and transfers zero-shot to four unseen backbones.

### 10. EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-25T17:09:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.34450
- Summary: Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control. Agents need to adapt to other agents at test time and reuse accumulated experience to refine their interaction strategies for future interactions across cooperative, mixed-motive, and adversarial settings. However, existing approaches often develop adaptation mechanisms for particular interaction settings. This raises a central question: how can decentralized MAS support test-time adaptation and reliable experience reuse across interaction settings? We propose EvolveMAS, a unified self-evolution framework that supports experience-driven adaptation within and across episodes. EvolveMAS pairs each main agent with a dedicated MemoryAgent for test-time memory governance, which maintains isolated Structured Memory outside the main agent's reasoning context. EvolveMAS organizes adaptation into two complementary processes: Within-Episode Online Adaptation and Cross-Episode Knowledge Evolution. During Within-Episode Online Adaptation, MemoryAgent updates episodic, semantic, and working memory from interaction evidence to inform subsequent actions. During Cross-Episode Knowledge Evolution, the main agent uses memory and episode outcomes to distill reusable interaction knowledge comprising partner profiles and interaction strategies for subsequent episodes. Across five benchmarks and six evaluation configurations spanning the three interaction settings, EvolveMAS achieves the highest normalized average score of 77.2 among the compared methods. Ablations show that test-time memory governance and cross-episode knowledge reuse both improve performance. Interaction traces further illustrate how updated memory and distilled knowledge guide subsequent interactions. These results support experience-driven adaptation in decentralized MAS without updating model parameters.

### 11. From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-21T10:49:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.29560
- Summary: Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work has begun to address these challenges by augmenting foundation-model policies with memory and by introducing hierarchical architectures that separate high-level planning from low-level execution. We organize the high-level VLM as a robotic agent through an editable harness to maintain task context and improve planning through execution experience. We instantiate this approach as SERA (Self-Evolving Robotic Agent), with a fixed VLA executor providing low-level control. The harness maintains and updates task context using observations and execution feedback to guide subsequent planning. Self-evolution uses environment rollouts to propose and evaluate harness revisions, with the selected configuration fixed before held-out testing. On RoboMME, SERA achieves 51.38% overall success with autonomous selection, compared with 44.38% without self-evolution. Our exploration suggests that agentic planning is a promising direction for history-dependent robotic manipulation.

### 12. Digital Twins for Multi-Agent Systems: When to Trust, What to Change
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-21T03:09:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.28517
- Summary: Digital twins of agent networks need to flag unreliable forecasts and help users choose interventions. Both decisions depend on what happens over several steps: an error can spread through the network, and an edit whose trajectory is easy to predict may still yield a poor collective outcome. We ask when information about error propagation improves failure detection and whether a learned twin can select effective network edits despite imperfect forecasts. We propose Propagation-Aware Validation for Networked Digital Twins (PAV-Twin). Its monitor combines Jacobian-based propagation features with recent errors and ensemble disagreement to estimate the risk that a forecast exceeds an error threshold. Its planner simulates each candidate edit and ranks the edits by their predicted collective outcomes. In simulations, the monitor gained 0.13 in area under the precision-recall curve on larger oscillator networks with familiar topologies and 0.09 on larger networks with held-out topologies, relative to a graph baseline without propagation features. Gains were small in contractive consensus. Giving the graph baseline the same features narrowed the gap. In a separate planning study, ensemble simulation recovered about 99% of the possible improvement over random intervention selection in oscillators and nearly all of it in consensus. With a simplified oscillator twin, selecting by predicted outcome also gave lower regret than selecting by trajectory fidelity. These results show when propagation features help flag unreliable forecasts and why the quality of intervention choices should be measured directly.

### 13. Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-20T14:55:07+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.27689
- Summary: Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, and limited reuse of execution experience. We propose Embodied-Harness, a dual-agent framework that improves manipulation by refining the execution harness without updating model parameters. The Actor interacts with the environment through a robot-control interface, while the Reflector converts execution evidence into reusable operational guidance. Hierarchical Memory Architecture maintains short-term execution context and long-term experiential knowledge to support execution and reflection. Evidence-based Experience Reflection grounds failure diagnosis in observed interactions, while Recursive Harness Self-Improvement refines operational guidance across successive attempts. Experiments on RoboTwin 2.0, RoboSPA, and RMBench demonstrate the effectiveness of Embodied-Harness in generalization under environmental variations, spatial reasoning, long-horizon planning, and memory-dependent manipulation. Our method achieves success rates of 82.4%, 76.7%, and 94.4% on the three benchmarks, respectively. Real-world evaluation further yields an average success rate of 96.7% across three manipulation tasks. These results highlight the potential of Embodied-Harness to improve robotic manipulation through experience-driven harness self-improvement.

### 14. NeuroImgAgent: a multi-agent platform for cross-species fMRI analysis with evidence-gated quality control
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-19T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.19.767770
- Summary: Cross-species functional MRI analysis requires coordinating specialized workflows and assessing intermediate outputs. We present NeuroImgAgent, a multi-agent platform driven by large language models that translates natural-language requests into workflows for humans, macaques, rats and mice. Quantitative checks and vision-language model assessments determine whether processing continues, enters bounded recovery or stops. Across 268 paired cases, preprocessing metrics were broadly comparable to those of fMRIPrep, AFNI and RABIES. With GPT-5.5, NeuroImgAgent corrected 111 of 120 induced orientation errors and passed all 52 intent-recognition and planning tasks, 8 of 9 recovery tasks and 11 of 14 tool-construction tasks on NeuroAgentBench. In 120 paired challenge cases, the full configuration increased usability from 76.7% to 92.5%, as assessed by blinded experts, and reduced unusable outputs delivered without warning from 18.3% to 4.2% of cases relative to quality-control ablation.

### 15. Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-17T06:21:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.22275
- Summary: Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically coupled interactions between humanoids, enabling coordinated decentralized control from local observations alone. At the high level, we train a vision-language planner and design a speech-based leader-follower coordination mechanism to synchronize decentralized execution without network communication. Trained with two identical humanoids, our system scales to teams of up to ten robots and generalizes to heterogeneous teams without retraining. To benchmark these capabilities, we introduce HH-Bench, comprising 12 tasks involving teams of 2 to 10 humanoids, including heterogeneous teams. Systematic evaluations show that Heave-Ho consistently outperforms baseline methods, while real-world experiments demonstrate robust decentralized collaboration across challenging tasks.

### 16. Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-17T05:47:01+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.22245
- Summary: Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts. This creates a consistency challenge: facts retrieved by workers may be missing from the evidence available to the lead for a joint conclusion. We introduce a benchmark and evidence-flow profiler for studying multi-agent memory inconsistency through controlled factual conflicts in Harvey LAB document-review tasks. Pooled across three models with comparable generation spending, requiring delegation increases retrieval of both conflicting claims from 50.2% to 68.7% relative to single-agent execution, yet conflict detection falls from 16.2% to 13.2%. Within this setting, workers report both claims for only 35.2% of retrieved pairs, and pooled matched comparisons show higher detection than single-agent execution when one worker reads both claims but lower detection when the claims are split across workers. Worker-to-lead handoffs are a central target for improving conflict detection in multi-agent LLMs.

### 17. EvoDisco: Strategy Discovery for Evolving Agent Memory
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-17T02:37:56+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.22102
- Summary: Large language model agents accumulate experience in memory, and how that memory evolves during interaction is as important as what it stores. Recent methods update memory online, yet both the operators that transform memory and the rules that select them remain fixed by design. We propose EvoDisco, which formulates agent memory evolution as evolutionary strategy discovery: the agent must discover which operator to apply, when to apply it, and how to instantiate it, rather than rewriting memory under a static operator schedule. A learnable policy conditions on the current memory state and recent task history, then selects and instantiates one of four semantic operators---Abstract, Refine, Bridge, and Reframe---which respectively compress related memories, decompose overloaded entries, connect weakly linked experiences, and reorganize retrieved reasoning chains. The policy is updated with a bi-level fitness. An inner signal scores each transformation using a retrieval-quality improvement regularized by memory complexity. An outer signal scores strategic efficacy over a window of past decisions, combining historical operator-utility regret, utility-prediction error, and selection diversity. Under a one-pass online plus frozen-transfer protocol on ALFWorld, WebShop, and LifelongAgentBench (OS and DB), EvoDisco improves over strong memory baselines including MemP and MemRL. The largest gains are on ALFWorld ($+8.8$ online / $+12.9$ frozen-transfer points over MemP; $+16.4$ / $+17.9$ over MemRL). Ablations attribute these gains to both fitness levels and the operator library.

### 18. From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-13T17:59:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2611.18484
- Summary: AI-enabled remote patient monitoring is evolving beyond passive data collection toward agentic AI systems that interpret patient states, coordinate care, and initiate action across domestic and clinical settings. This structured scoping review finds that mature agentic care has not yet emerged: Most systems remain human led, while stronger decision-action coupling and embodied AI remain largely confined to prototypes and pilots. Healthcare robotics makes the transition from monitoring to action especially visible by translating AI-generated recommendations and decisions into speech, movement, prompting, physical assistance, escalation, and care coordination, making embodiment, clinical integration, human oversight, and governance fundamental design requirements. Further progress requires safe and interoperable care architectures in which intelligent components operate through clinically validated and accountable workflows. We propose agentic robotics as a future direction for supervised systems embedded in the care ecosystem, connecting AI agents and robots with clinicians, caregivers, and patients through auditable workflows that can be interrupted and remain subject to human oversight and explicit AI governance.

### 19. On Private Knowledge Retrieval and Private Inference for secure multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-10T07:43:02+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.13696
- Summary: Multi-agent systems provide a convenient framework for the massive deployment of agents based on Large Language Models (LLMs). It provides a sound framework where agents can interact with existing software to perform actions in an autonomous way. Agentic AI is the new term to denote these AI-based autonomous systems. In real multi-agent systems, agents need to deal with malicious agents some of which can exploit security vulnerabilities to do harm. A memory poisoning attack is an example of exploiting a vulnerability to modify agents knowledge and, thus, affect its behavior. In an agent, there are different types of memory systems (semantic, episodic, and short-term) which have their own characteristics and for which different memory poisoning attacks may be developed. In this paper we focus on semantic memory, we discuss its attack, and mitigation strategies. We introduce private knowledge retrieval and private inference. We propose a signature system in the knowledge base to prevent from undesired manipulation. This should avoid memory poisoning attacks by introducing security by design in the construction of the semantic memory. In our architecture, an agent contains a local Prolog-like inference system (i.e., using Horn clauses to represent knowledge) which accesses an external knowledge base to get the required knowledge. This externally signed knowledge base is accessed privately. We provide different implementations in Python using different privacy levels including k-anonymity and information-theoretical privacy (IT-PIR).

### 20. A Common Recognition Architecture Across Memory Scales
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-09T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://www.biorxiv.org/content/10.64898/2026.11.04.764437
- Summary: Recognition decisions occur across memory episodes that vary vastly in scale, from compact single-item episodes to extended experiences involving hundreds of items. To test how memory scale shapes the neural mechanisms underlying old/new judgments, we recorded EEG while participants performed a recognition memory task across set sizes ranging from 1 to 128 items (spanning 2 to 256 recognition judgments). Classic electrophysiological signatures of recognition, including frontal and parietal old/new effects, persisted continuously across set sizes. Furthermore, multivariate neural classifiers trained on small memory scales generalized robustly across set sizes. Rather than revealing distinct neural formats, increasing memory scale produced systematic, continuous shifts in the timing and strength of a shared recognition response: signals emerged progressively later and weaker at larger memory scales. Temporal-alignment and cross-correlation analyses demonstrated that responses across scales followed a common waveform trajectory, with timing shifts propagating into motor response preparation. Finally, individual difference analyses revealed that this common recognition format exhibits scale-dependent behavioral relevance, tracking working-memory capacity at smaller scales and long-term memory performance at larger scales. Together, these findings demonstrate that recognition signals share a common neural format across scale while changing dynamically in timing, strength, and behavioral relevance, providing evidence for convergence onto a shared recognition architecture.

### 21. Coordinated Mixed-Precision KV Cache Quantization for Efficient LLM-based Multi-agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-06T17:07:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.10096
- Summary: LLM-based multi-agent systems solve complex tasks through collaboration, but their growing, simultaneously resident key-value (KV) caches create a memory bottleneck. Applying single-model quantization policies independently ignores differences in agents' precision needs, potentially degrading collective reasoning. We introduce Coordinated Mixed-Precision KV Cache Quantization (CoMixKV), which combines online sensitivity estimation with joint agent-layer bit-width allocation under a shared memory budget. To our knowledge, CoMixKV is the first mixed-precision KV-cache quantization framework to jointly allocate precision across simultaneously resident agent caches under such a budget. The estimator derives sensitivity from a local attention-error bound using recent queries, keys, and values, without calibration data, trial quantization, or additional model passes. A shared controller combines these scores with remaining quantizable capacity and byte-level storage costs to minimize total estimated error. Allocations are refreshed as agents start or finish and new observations become available. Selected widths apply only to newly quantized blocks; recent states retain native precision and previously quantized blocks remain unchanged. Across four benchmarks and three LLM backbones at average 2-bit, 3-bit, and 4-bit settings, CoMixKV achieves strong accuracy against the evaluated quantization baselines. At the average 3-bit setting on Gemma-4-31B-it, it achieves 68.35% average accuracy, exceeding the strongest quantized baseline by 0.59%. On Qwen3-32B, it reduces peak KV-cache memory by 32.08% and achieves a 1.38x inference speedup over FullKV.

### 22. HomeLoop: A Simulation Framework and Benchmark for Robot-IoT Coordination in Everyday Domestic Assistance and Safety
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-06T02:54:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.08914
- Summary: Recent progress in embodied robotics is bringing robots closer to deployment in homes, as vision-language models (VLMs) are demonstrating significant advances in reasoning, making VLM-driven robots promising home assistant agents. These agents will often be introduced into homes that already have cameras, Internet of Things (IoT) devices, and residents with wearables. To fulfill their potential, they need to integrate with existing smart infrastructure and reason through ambiguous scenarios: a smoke alarm may come from a pan about to ignite, a pan already on fire, a resident cooking or a faulty sensor, and each calls for a different response. To that end, we introduce HomeLoop, a simulation framework and benchmark built on Isaac Sim that combines robot bodies, networked devices and wearables, simulated residents and visitors, faulty sensors, and hazards that evolve over time. Our benchmark is composed of 20 tasks across five families grounded in real-world household hazards and needs, and designed so that the same alert can have different causes. A runtime monitor scores each episode with temporal-logic checks on the final outcome and the actions along the way, and every action carries a predefined cost. We evaluate six open-weight and proprietary VLMs. The best achieves a family-balanced score of 61.9%, and across models we see a pattern of over-reaction: failed episodes involving prohibited interventions outnumber those involving missed required interventions by more than two to one, with models often shutting off the stove before investigating the alarm's cause. HomeLoop is an extensible foundation intended for use in research on robot-IoT coordination, long-term memory, proactive assistance, and privacy-safety trade-offs. HomeLoop will be released with 2,100 home layouts that can be automatically furnished in diverse configurations, five robot bodies and 20 networked device types.

### 23. H^2MARL: Hierarchical Heterogeneous Multi-agent Reinforcement Learning for Humanoid Robot Control
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-04T13:48:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.06523
- Summary: Coordinated whole-body control of humanoid robots remains challenging due to high-dimensional coupled dynamics and substantial physical heterogeneity across joint degrees of freedom (JDoFs). Existing multi-agent reinforcement learning methods either employ coarse agent partitions or directly apply generic heterogeneous-agent algorithms, while hierarchical controllers commonly optimize high-level planning and low-level execution independently, leading to uncoordinated motion. In this paper, we propose H^2MARL, a hierarchical heterogeneous multi-agent reinforcement learning framework with two key mechanisms. We first formulate humanoid whole-body control using a JDoF-level physical-heterogeneity-aware policy factorization, where each torque-actuated JDoF is conditioned on an explicit descriptor of its actuation, kinematic, and dynamic properties. Moreover, we develop a closed-loop policy-executor co-optimization mechanism that jointly adapts the high-level pose planner and the low-level joint executor using shared interaction trajectories, thereby reducing the distribution mismatch between planning and execution. Extensive experiments in MuJoCo and Isaac Gym demonstrate that H^2MARL consistently improves locomotion stability, gait coordination, and motion quality over homogeneous, coarse-grained, and independently optimized alternatives.

### 24. ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-03T04:57:47+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.04321
- Summary: Multi-agent LLM systems assign different responsibilities to different agents: one plans, another retrieves evidence, another verifies, another executes. This division of labor is only meaningful if each agent stays within the functions it is authorized to perform. Over many turns, however, an agent can produce a locally reasonable message that exercises authority belonging to another role: a verifier that begins planning, a retriever that asserts unsupported conclusions, an executor that changes state no one approved. We formalize this as role drift, a turn-level breach of an agent's role contract. We introduce Agent Trajectory Control (ATC), which makes each role's authority explicit as a contract and enforces it at the point where a message would enter the shared conversation. ATC scores a proposed output for out-of-role deviation, leakage into the functions of other roles, impermissible speech acts, and logical contract breaches, then computes a leakage-regularized target that constrains regeneration; the revised message is re-checked before admission. Enforcement acts on the message rather than the generator, so ATC governs agents whose internal representations are unavailable. Across homogeneous and heterogeneous teams, ATC improves task performance and role consistency while lowering role-drift energy relative to strong baselines spanning prompting, memory, workflow control, and activation editing, with the largest gains under explicit role-confusion stress tests and in larger, more diverse teams.

### 25. Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-02T01:09:24+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02361
- Summary: Can a language model that reads the full history of an access log say whether a service may act now? On an executable benchmark of grants, withdrawals, reinstatements, expiries, groups and change windows under a known policy, scored on pairs of histories that differ only in the order or one field of the deciding events, open models of 7 to 32 billion parameters fall from 72 to 86 percent after eight or sixteen events to 48 to 55 percent after 256, while reasoning-trained 32B models reading the current state reach 96 and 98 percent. A reasoning model of 120 billion parameters trails the state by four and seven points at 256 and 512 events and by about ten at 1,024, so the length beyond which explicit state outlasts long context grows with the reader. We treat agent memory as recursive filtering. The decision depends on the history only through a state whose size is set by the number of tracked keys. A store holding fewer component records than the state forgets on a time scale set by its capacity, and a reader model predicts its accuracy within 0.02 on average in a registered test. Retaining log lines without regard to time order errs with probability approaching one half, a bound that is attained. A filter in which a model parses each line and an explicit rule applies the updates answers 80 to 89 percent at 256 events and beats relevance retrieval, model-kept ledgers, a reimplementation of StateMem and the Mem0 library. A retriever that selects at query time the lines the queried state depends on matches it at 256 events on the first domain, so what decides is selection by the state's dependencies, which the filter performs when writing, without the query. Applying parsed updates themselves, the models fall to 58 and 59 percent. A frozen replication on a second domain with fresh wording reproduces the horizon.

### 26. Head movement allocation in freely-moving macaques learning object-context sequences
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-02T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.1101/2023.12.11.571113
- Summary: Flexible learning and long-term memory are hallmark features of primate cognition that are shaped by interactions with changing environments. A comprehensive understanding of these brain-body-environment interactions requires minimal constraints on behavior, and environments rich with conditional cues that encourage diverse behavioral dynamics. In this study, we introduce a multi-level enclosure (Treehouse) that allows for independent control of spatially distributed touchscreens for studying cognition in freely moving macaques. To test flexible learning, two monkeys completed trials consisting of a regular sequence of conditional object choices (targets) across four distinct spatiotemporal contexts (screens). Both monkeys acquired numerous unique, conditional object-context sequences without detriment to new learning as memoranda accumulated. They also successfully recalled their correct choices after weeks without exposure. To assess how monkeys allocate movement during learning and memory-guided decision making, we tracked their head kinematics and used recurrent neural networks to decode different aspects of their engagement with the environment during the choice epoch of the task. One such model predicted the position of the object about to be touched, including on error trials, tracking overt gaze towards objects. Separate models decoded sequence corner, the ordinal step, and the individual screen stations the monkeys occupied, despite identical stimulus layouts and behavioral demands at each station. Head movements also showed efficiencies that the task did not require: under conditions of uncertainty, monkeys were biased in their initial search locations to the targets that were closest to reach, and across days they made smoother head movements as training progressed, with no change in accuracy. These results demonstrate the potential of immersive 3-D environments, in which body kinematics can shed light on animals' goals, and reveal that situated learning …

### 27. The Agentic Observer Hackathon: Autonomous Decision-making in Simulated Astronomical Surveys
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-01T15:25:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2611.01988
- Summary: Astronomical surveys must allocate observing time while responding to changing conditions and competing scientific priorities. We present the Agentic Observer Hackathon (AOH), a community challenge for studying autonomous survey operations. Within a synthetic multi-object survey with prescribed exposure responses and assignment constraints, decision systems select pointings, assign targets and choose exposure configurations while responding to observing requests, instrumental faults and data loss. We evaluate systems submitted by 102 teams on campaigns reserved for evaluation and analyse target completion in a reference campaign. The leading systems combine numerical exposure planning with language models for interpreting operational information and supporting longer-term decisions. Exploratory tests show improved fault reporting with model access in several systems, while revised scientific priorities produce substantial changes in ranking. The reference campaign traces target completion and diagnoses errors in the baseline's inference of prescribed quality bands. The released simulator and reference strategies provide common survey conditions for comparing exposure allocation, target selection and recovery from interruptions.

### 28. A complete analytical characterization of optimal collision-free motion for two robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:53:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41558
- Summary: Collision-free motion planning for multi-agent robotic systems remains an active research area because of the complexity of coordinating robot trajectories, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. Importantly, the analytical difficulty of nonconvex collision-avoidance constraints has so far driven the development of exclusively numerical methods. We derive a complete analytical characterization of the optimal trajectories for two robots that start and end at rest, under double-integrator dynamics and a squared-acceleration objective. We prove that these trajectories belong to eight distinct contact families and determine which family applies for each configuration of initial and final positions. We analyze the geometrical properties of the optimal trajectories, provide a numerical algorithm for computing them, and discuss how these insights may improve the performance of existing numerical trajectory optimizers.

### 29. Contact-based optimization for collision-free motion planning for a million robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:46:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41548
- Summary: Multi-agent robotic systems have attracted growing interest in recent years, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. At the planning level, robot motion is often modeled using double-integrator dynamics (with low-level controllers handling the physical dynamics during execution) with a minimum-energy objective subject to collision-avoidance constraints and limits on position, velocity, and acceleration. The complexity of the problem resides in the constraints, which couple the trajectories and make the optimization problem nonconvex. Existing numerical approaches typically discretize and optimize entire trajectories, which becomes expensive for large fleets. We exploit the structure of optimal trajectories by organizing optimization around contacts, at which robots reach the minimum allowed separation. We formulate a coupled algebraic system in contact variables and reconstruct trajectories analytically between contacts. Our algorithm, sequential contact insertion (SCI), starts from unconstrained trajectories, inserts contacts at separation violations, and jointly adjusts their times and states. Numerical experiments demonstrate planning for one million robots in minutes and thousands of robots in fractions of a second. On problems feasible for a fixed-grid sequential convex programming baseline, SCI achieves median speedups of several orders of magnitude at matching solution accuracy.

### 30. Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-28T20:40:33+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.38869
- Summary: Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments across retrieval, memory, tools, and peer communication. In this paper, we define belief as an engineering abstraction for evidence-based commitments that guide downstream action. Building on this view, we propose the Explicit Belief Multi-Agent System (EB-MAS), which externalizes belief states into a structured substrate, uses belief operators to propose candidate updates, and applies a Cognitive Firewall to bound or reject updates that are weakly evidenced but strongly driven by vulnerability cues. We also discuss the risk of group belief at the group level, including manufactured consensus, collusion, and cascading misinformation, and outline practical integration challenges around grounding, false positives, scalability, and ethical misuse. Therefore, scalable agent safety requires not only better output filtering or stronger base models, but also explicit interfaces for tracing, calibrating, and constraining belief revision at runtime.
