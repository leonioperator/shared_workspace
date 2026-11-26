# Blindspot Signals Report - 2026-11-26

- Source export: `/opt/apps/haier/exports/evolution_signals_20261126_020506.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 591
- Deduped/weighted signal clusters: 558
- Novel vs previous reports: 18
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. Leto: Utility-Centric Agent Memory
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-24T17:30:06+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.33005
  - Alt: https://arxiv.org/abs/2611.21478
  - Alt: https://arxiv.org/abs/2611.03930
- Summary: Large language model (LLM) agents rely on external memory to retain and reuse information across interactions. Existing memory systems treat memory as a record of the past and evaluate it by fidelity to the conversation. However, the value of memory lies in whether it improves the agent's response. A memory system decides what to memorize and what to serve before that response exists, and fidelity checks neither decision against it. Faithful memory can therefore fail to improve the response. We instead view memory as a prediction problem and present \textbf{\emph{\leto{}}}, a memory system for LLM agents that focuses on the utility of memory to the future rather than on its fidelity to the past. Because future requests are unknown, \emph{\leto{}} preserves access to conversation details through memory indexing, allowing information to remain available through its sources. When a request arrives, memory replay draws on this index to anticipate and supply the context the agent needs beyond what the request explicitly states. The utility of the served context remains uncertain until the response is generated, motivating a utility loop that uses response outcomes to refine future memory selection. We evaluate our system against six memory systems on five benchmarks across three scenarios. In personalization, it outperforms the strongest compared memory system by 16.3 percentage points in accuracy on PrefEval and by 3.1 points in task completion on PERMA. For long-horizon tasks, it achieves the best overall performance on MemoryArena averaged over five environments with a gain that increases with the chain depth. In long-context understanding, it is on par with retrieval over the raw history while serving fewer context tokens.

### 2. RoboProbe: Benchmarking Physical Plausibility of Robot World Models
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-24T08:06:52+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.32152
- Summary: Evaluating the physical plausibility of generated videos is critical for reliable robotic planning with world models. These videos inform action proposal and assessment before real-world execution, so undetected physical violations can lead to erroneous assessments of action feasibility and safety. Yet current video generators often produce physically implausible interactions. Detecting such violations directly with vision-language models (VLMs) remains challenging as physical verification requires evidence-grounded spatiotemporal reasoning beyond high-level semantic understanding. We develop five law-specific metrics for evaluating physical plausibility by combining spatiotemporal evidence from segmentation, tracking, 3D geometry, or appearance comparisons with targeted VLM reasoning: Contact fidelity, Object persistence, Solidity, Robot deformation, and Object deformation. Building on this metric suite, we introduce RoboProbe, an agentic evaluation framework that coordinates metric execution and selectively refines evaluations through constrained actions. To evaluate the physical plausibility of robot world models, we further introduce RP-Bench, with 761 human-labeled generated videos and 130 real demonstrations of 239 manipulation tasks from 12 robot datasets. On RP-Bench, all five metrics achieve AUROCs above 0.85 and outperform the evaluated learned judges, prior evaluators, and a frames-only Gemini baseline. Applying these metrics to five video generators reveals distinct patterns of physical violations across models, in both violation types and frequencies.

### 3. RoboHarness-RL: Agentic Reinforcement Learning for VLM-Based Robot Manipulation
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-24T05:59:50+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.32016
  - Alt: https://arxiv.org/abs/2611.12885
- Summary: Agentic harnesses enable frontier vision-language models (VLMs) to manipulate robots through perception, planning, and control tools, yet achieving comparable performance with compact open-weight VLMs remains challenging. We present RoboHarness-RL, an agentic reinforcement learning framework for improving VLM-based robot manipulation through tool calls. Starting from supervised fine-tuning on successful teacher demonstrations, the VLM further improves through multi-turn reinforcement learning with task-outcome rewards, without relying on vision-language-action models or world action models. To support efficient multi-turn training, we develop LiteHarness, which uses hierarchical memory to keep interaction contexts compact while preserving task performance. With Qwen3.5-9B, RL raises success from 31.2% to 44.0% on RoboTwin 2.0 and from 57.8% to 73.3% on LIBERO-Pro; these gains extend to randomized RoboTwin scenes unseen during training (26.4% to 38.0%). Behavioral analysis further shows that RL reduces repetitive-call rates by up to $4\times$, shortens successful executions, and improves recovery from negative feedback. Project page: https://aim-uofa.github.io/RoboHarness-RL/

### 4. Valence-Based Memory Prioritization in Neural Networks
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-24T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.05.05.723022
- Summary: Improving long-term memory in neural networks remains an open challenge. Existing memory prioritization approaches tend to rely on unsigned importance signals that determine how strongly information should be remembered without representing whether its significance is positive or negative. Inspired by emotional valence in biological memory, we introduce a computational framework that integrates both the magnitude and sign of importance into neural network learning and attention. Our framework combines three mechanisms: (i) a valence-weighted cross-entropy loss that prioritizes salient information during learning; (ii) an amygdala-inspired module that learns structured valence embeddings encoding both magnitude and sign; and (iii) a hippocampus-inspired attention mechanism that incorporates these embeddings into queries and keys to enable valence-sensitive retrieval. We demonstrate generalization of our framework across episodic, spatial, and language-based memory tasks, improving long-term recall of high-salience information. In addition to improving long-term memory, we also show that our framework has the potential to improve memory-based decision-making in reinforcement learning and mitigate the ''lost-in-the-middle'' problem in language modeling. Taken together, we demonstrate a computational framework that integrates both the magnitude and sign of importance into neural network learning and attention, enabling models to prioritize salient information during learning while using valence-sensitive representations to guide memory retrieval.

### 5. Autonomous AI agents are giving everyday hackers ‘nation-state’ firepower, cyber expert reveals - Fox News
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-25T18:43:29+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMitgFBVV95cUxOZ180aXFlaEdQTE9FcGZkbTlWX25PSUFZTEVUS1FldkdiSmQ3RTVucU1iaU1WZS1DNlRfQmFZeC1fRzdLMXZjLXU5MWh0cVFFbktWYnZ6azYwejI3U0loODRzakpOTWlCaHdIelFCc0drS1BTRTFvQi1MYTdQWWdiNXV2LUQwS0JXb0lDclRudkNIR2xWS1JtU2s2S1FJSExjaDlHdlgxWVJkcU1va2RMR3JrXzJ0UdIBuwFBVV95cUxOYUVfbkM2UVhXLXpMdkF3OTlTcV9uSDRtUUl6Y1EyVm5rZnNJLWhzUTlNUjNnSGhtajZhamtuOFFud2xkVEhwZFVSdWFwZF8wek5FZUtKb00tVDdLeFRtblBvNUczSXdWNnFtcHdUOEd2T1pYUG9fR1FCZ2l5anRZRHNxbjktRndyNk5DRld0SG1NcWkxQ1FlRGMwSk1QdHU4WDlBQlFpcVdJSWZvYTZiaFZoT0hYZHpnM1NR?oc=5
- Summary: Autonomous AI agents are giving everyday hackers ‘nation-state’ firepower, cyber expert reveals&nbsp;&nbsp;Fox News

### 6. An Open, Evolving Brain and Cognitive Aging Simulator Enabled by Agentic Artificial Intelligence
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-25T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.24.769018
- Summary: An agentic AI simulator was built to advance our understanding about how the human brain and cognition change with age. The simulator generates worlds based on hypothesized age-linked cascades and then simulates studies across varied experimental designs and selection criteria. Each simulated world begins with 120,000 individual lives initiated by baseline parameters (e.g., genetic risk, birth year) and then changed by age-dependent cascades (e.g., amyloid-dependent, cardiovascular). Examples illustrate how the simulator predicts distinct data patterns in cross-sectional versus longitudinal designs, how alternative participant selection strategies emphasize baseline differences versus age-related decline, and how variable levels of association emerge between brain and cognition dependent upon design choices. Simulations of clinical trials provide information about design, power, and outcome considerations. Experiments on alternative simulated worlds evaluate how well hypothesized cascades accommodate real-world data patterns, capturing the insights and open puzzles inside the application. Most critically, the application is built to evolve. Its code contains a complete description of how to construct and update itself so that any person or AI agent can explore a new finding, recalibrate to emerging data, or build and simulate a novel future study. The simulator is offered as a tool for understanding data patterns, teaching, and generation of hypotheses to be tested in future studies using real-world data collection.

### 7. MemoryWorks
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-24T20:30:45+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/memoryworks
- Summary: <p> Company memory for people and AI agents </p> <p> <a href="https://www.producthunt.com/products/memoryworks?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1329703?app_id=339">Link</a> </p>

### 8. Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-24T17:32:00+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, neural interfaces / robotics
- URL: https://arxiv.org/abs/2611.33010
- Summary: Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introduce RoboDojo-Mirror, a benchmark built on RoboDojo that preserves task objectives, success criteria, and policy checkpoints while comparing a mirror-free baseline with single-mirror, dual-mirror, and mirrored-tabletop conditions. Across five policies spanning Vision-Language-Action models, World Action Models, and agentic policies, every mirror condition reduces aggregate success rates: averaged over the three conditions, the drop ranges from 10.8 to 56.7 percentage points across policies, and it reaches 62.5 points on the mirrored tabletop. Because a mirror is also a physical obstacle, we compare it against geometrically matched non-reflective panels; 50--88\% of mirror-specific failures occur without recorded robot--panel contact, so direct collisions alone do not explain the degradation. Trajectory and contact analyses instead reveal recurring behaviors consistent with phantom targeting of reflected objects and spatial mislocalization of real ones. Targeted diagnostics further characterize grasping near reflections, policy-dependent pushing progress, and physical-target interaction under main-camera occlusion. Real-robot experiments with $π_{0.5}$ and FastWAM also show lower overall success rates under the upright-mirror and mirrored-tabletop conditions. These findings reveal a shared vulnerability to reflective environments across diverse robot policies and motivate reflection-aware evaluation of embodied intelligence. Code is available at https://github.com/iPPLab/robodojo-mirror.

### 9. OVOK: A Recursive Self-Improving Agentic Framework for Video-Based Articulated Robot State Estimation
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-24T08:35:58+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.32185
- Summary: Recovering articulated robot state from video supports metric spatial sensing for manipulation, scene reconstruction, and action planning. Yet the problem is ill-posed: different intrinsics, camera-to-robot poses, and joint angles can explain similar observations. Prior task-specific regressors typically assume known intrinsics, fit one robot through laborious data collection and robot-specific training, and still transfer poorly across scenes. Foundation models apply to any robot zero-shot, but their estimates have large errors. We present OVOK (One Video to Kinetics), a recursive self-improving agentic framework for this task. Under a human-authored protocol, an agentic initializer constructs robot-specific OVOK-4k; a proposer--executor--verifier loop then jointly evolves tools and executable workflows from feedback. Updated tools and workflows are accepted only when the verifier judges a positive improvement. The retained workflow is frozen for accurate inference. Experiments demonstrate that the evolved workflow achieves state-of-the-art results on DREAM-V and RoboKeyGen-V, delivering robust and accurate estimates.

### 10. From hands to tools: evidence for evolutionary precursors of tool processing in macaque cortex.
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-24T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://www.biorxiv.org/content/10.64898/2026.11.24.768489
- Summary: In humans, hands are animate effectors and tools are visually dissimilar inanimate objects, yet the brain represents them in closely related cortical systems. Whether this coupling depends uniquely on human tool knowledge or reflects a conserved property of primate cortex is unknown. Using whole brain fMRI (0.22 cubic mm voxels) in macaques viewing images of hands, tools, and other objects, we found that inferotemporal cortex largely followed the animate/inanimate division, with only a few small hand-tool preferring sites. In contrast, parietal and prefrontal areas showed hand-tool representational similarities that were best matched by a neural-network model trained on fine-grained human hand-object interactions rather than by networks optimized for static object recognition or general action recognition. Volumetric functional ultrasound imaging (0.0023 cubic mm voxels) independently showed that tool responses were spatially aligned with human hand, but not monkey hand, responses in posterior parietal cortex. Macaque cortex thus represents tools in relation to the hand even without habitual tool use, consistent with an evolutionarily conserved action related scaffold that may be shaped by longterm visual exposure to human hand tool interactions.

### 11. ModFormer: A unified structure-aware model of transcriptome-wide A-to-I RNA editing
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-24T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.23.768611
- Summary: Adenosine-to-inosine (A-to-I) RNA editing can recode transcripts without permanently altering the genome. ADAR-catalyzed editing depends on both local sequence and RNA secondary structure, making it difficult to anticipate which sites will be edited or how mutations will change their activity. Moving from observing endogenous A-to-I editing to using it as a programmable molecular tool requires predicting how editing responds to sequence changes. Here, we present ModFormer, a model that integrates RNA sequence representations with predicted secondary structure to predict ADAR-mediated editing. Trained on human data, ModFormer predicts editing sites and rates across substrates and species unseen during training, recovers established sequence and pairing preferences, and anticipates experimentally measured responses to RNA mutations. These predictions prioritize responsive sites in mutational screens and guide an autonomous AI agent toward candidate RNA designs. ModFormer provides a framework for predicting how sequence changes reshape RNA editing and can be adapted to new substrates with limited experimental data.

### 12. Multi-agent System for Automatic Discovery of Pareto-optimal Meta-solvers for PDEs
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-23T21:55:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.31611
- Summary: Designing linear solvers for discretized partial differential equations requires problem-specific expertise. We present a multi-agent framework, in which language-model agents propose, critique, implement, and evaluate solver configurations assembled from Krylov methods, preconditioners, block factorizations, and neural operators. Inside the proposing agent, a non-dominated sorting genetic evolutionary algorithm evolves the population of meta-solvers toward the Pareto front of six measured quantities, so that one run returns a front of trade-offs rather than a single tuned solver. The system runs on small open-weight language models served on a single laptop, and we compare it with a single agent on four problems. For three-dimensional acoustic scattering and elasticity, it delivers 47 and 48 convergent hybrid solvers out of 60 candidates. Relative to the Jacobi-preconditioned Krylov baselines, the best of the discovered solvers reduce the iteration counts by factors of 4.7 and 60 and the online solve time by factors of 2.3 and 3.0, whereas the single agent produces no executable plan. For coupled dynamic thermoelasticity in two and three dimensions, where the baselines fail, it completes 98 of 100 transient candidates and, compared with the single agent, reaches a given accuracy 15 times faster in two dimensions and a displacement error 20 times lower in three dimensions.

### 13. Amazon and Meta reportedly in talks to lift blockade on AI agent Muse
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-25T14:10:18+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/25/amazon-and-meta-reportedly-in-talks-to-lift-blockade-on-ai-agent-muse/
- Summary: Amazon and Meta are discussing a potential deal that would end a two-month-long blockade of Muse.

### 14. OpenEight
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-25T06:58:59+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/openeight
- Summary: <p> The deterministic control layer for AI agents </p> <p> <a href="https://www.producthunt.com/products/openeight?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1330145?app_id=339">Link</a> </p>

### 15. Qube
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-24T17:55:06+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/qube-6
- Summary: <p> An AI agent for anyone </p> <p> <a href="https://www.producthunt.com/products/qube-6?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1329544?app_id=339">Link</a> </p>

### 16. Hai
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-24T11:19:56+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/hai-4
- Summary: <p> Your AI assistant that actually makes the phone call </p> <p> <a href="https://www.producthunt.com/products/hai-4?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1329023?app_id=339">Link</a> </p>

### 17. Show HN: An agent skill that optimizes code with falsifiable hypotheses
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-23T14:02:15+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://chszlab.github.io/AgenticAlgorithmEngineering/
- Summary: Hi all, I am a professor in algorithm engineering. In our field we use a method of falsifiable hypothesis testing to improve algorithms. More precisely, this is a cycle consisting of designing an algorithm, analyzing the algorithm, then implementing it and lastly testing it using experiments on real-world instances which leads to designing new algorithms based on the current observations.<p>We put this methodology into an AI skill which runs in an infinite loop. This skill first creates a performance profile, then produces a hypothesis which is implemented and tested automatically using an AI agent. If the change improved the performance and tests negotiated with the user verify it, the change is kept, if not it is discarded. Everything is tracked via version control.<p>Part of the output is a pdf report which documents all the code changes and progress over time as well as individual patches to only merge specific patches if one chooses to do so. Moreover, this comes with a knowledge-base in which we collect global optimization knowledge, thereby improving the skill over time.<p>We ran this on a wide range of public code bases, e.g. our KaHIP graph partitioning toolkit, which improved running time by 3.9x, or our VieCut minimum cut solver, where the skill improved the running time of the system by 8.9x; I do believe the skill is very easy to use and hence am sharing this here. Let me know what you think!

### 18. CodeRabbit Verify
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T16:26:36+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/coderabbit
- Summary: <p> AI agent that tests your running app on every pull request </p> <p> <a href="https://www.producthunt.com/products/coderabbit?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1321904?app_id=339">Link</a> </p>

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
