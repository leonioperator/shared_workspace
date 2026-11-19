# Blindspot Signals Report - 2026-11-19

- Source export: `/opt/apps/haier/exports/evolution_signals_20261119_020511.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 622
- Deduped/weighted signal clusters: 591
- Novel vs previous reports: 42
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-17T06:21:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.22275
- Summary: Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically coupled interactions between humanoids, enabling coordinated decentralized control from local observations alone. At the high level, we train a vision-language planner and design a speech-based leader-follower coordination mechanism to synchronize decentralized execution without network communication. Trained with two identical humanoids, our system scales to teams of up to ten robots and generalizes to heterogeneous teams without retraining. To benchmark these capabilities, we introduce HH-Bench, comprising 12 tasks involving teams of 2 to 10 humanoids, including heterogeneous teams. Systematic evaluations show that Heave-Ho consistently outperforms baseline methods, while real-world experiments demonstrate robust decentralized collaboration across challenging tasks.

### 2. Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-17T05:47:01+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.22245
- Summary: Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts. This creates a consistency challenge: facts retrieved by workers may be missing from the evidence available to the lead for a joint conclusion. We introduce a benchmark and evidence-flow profiler for studying multi-agent memory inconsistency through controlled factual conflicts in Harvey LAB document-review tasks. Pooled across three models with comparable generation spending, requiring delegation increases retrieval of both conflicting claims from 50.2% to 68.7% relative to single-agent execution, yet conflict detection falls from 16.2% to 13.2%. Within this setting, workers report both claims for only 35.2% of retrieved pairs, and pooled matched comparisons show higher detection than single-agent execution when one worker reads both claims but lower detection when the claims are split across workers. Worker-to-lead handoffs are a central target for improving conflict detection in multi-agent LLMs.

### 3. EvoDisco: Strategy Discovery for Evolving Agent Memory
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-17T02:37:56+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.22102
- Summary: Large language model agents accumulate experience in memory, and how that memory evolves during interaction is as important as what it stores. Recent methods update memory online, yet both the operators that transform memory and the rules that select them remain fixed by design. We propose EvoDisco, which formulates agent memory evolution as evolutionary strategy discovery: the agent must discover which operator to apply, when to apply it, and how to instantiate it, rather than rewriting memory under a static operator schedule. A learnable policy conditions on the current memory state and recent task history, then selects and instantiates one of four semantic operators---Abstract, Refine, Bridge, and Reframe---which respectively compress related memories, decompose overloaded entries, connect weakly linked experiences, and reorganize retrieved reasoning chains. The policy is updated with a bi-level fitness. An inner signal scores each transformation using a retrieval-quality improvement regularized by memory complexity. An outer signal scores strategic efficacy over a window of past decisions, combining historical operator-utility regret, utility-prediction error, and selection diversity. Under a one-pass online plus frozen-transfer protocol on ALFWorld, WebShop, and LifelongAgentBench (OS and DB), EvoDisco improves over strong memory baselines including MemP and MemRL. The largest gains are on ALFWorld ($+8.8$ online / $+12.9$ frozen-transfer points over MemP; $+16.4$ / $+17.9$ over MemRL). Ablations attribute these gains to both fitness levels and the operator library.

### 4. ARIPA: Agentic Reasoning for Image-based Pathology Analysis
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-18T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.16.767159
- Summary: Nuclear segmentation across patient-derived organoids (PDOs) is complicated by differences in morphology, staining, image scale, and acquisition format. We present ARIPA, an automated human-in-the-loop (HITL) system that coordinates pre-trained segmentation tools through a vision-language model (VLM)-based agentic planning, verification, and refinement loop for hematoxylin and eosin images of formalin-fixed, paraffin-embedded PDOs. In contrast to existing tools, ARIPA does not require training and achieves good performance. Tissue-aware tiling and image-derived calibration initialize segmentation; optional expert corrections guide configuration search and light-weight object-level rules without retraining or fine-tuning the pre-trained segmentation networks. We evaluated initial ARIPA predictions on more than 50,000 nuclei from 19 images of breast, head and neck, and lung patient-derived cancer PDOs, where nuclear segmentation was challenging due to its 3D structure and variation in imaging layers and malignant cell morphology. Performance was evaluated on agent-selected models before expert feedback, after feedback from the initial runs excluding direct expert edits, and in comparison to a custom-trained HoVer-Net model previously published by our group. At a minimum polygon intersection over union (IoU) of 0.5, image-macro F1 was 0.8380 before feedback, 0.9849 after feedback, and 0.4713 for HoVer-Net. Mean area under the F1 score versus IoU curve was 0.8013, 0.9700, and 0.4317, respectively. The mean paired F1 increase after feedback was 0.1468, with increases in 17 out of the total 19 images and no changes in the remaining two. Ground truth nuclei annotations were created by expert review and editing of ARIPA's post-feedback outputs. In this cohort, ARIPA outperformed the custom-trained HoVer-Net, and its performance was improved further following expert-guided HITL refinement. By automatic agentic reasoning with VLM review without training, ARIPA has potential …

### 5. Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-16T17:50:53+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.21478
- Summary: A useful memory need not resemble the question it helps answer. Jetriever ranks each stored memory by Jev's decision score for its usefulness to the current question, replacing similarity search with full-pool utility scoring. On InMind's 125 indirect-query tasks, it places the gold exchange first in 84.8% of cases; matched BM25 and MiniLM controls reach 1.6% and 0.0% when indexing user turns. A 20-question comparison separates finding evidence from ranking it: Jev and Qwen3.5 9B each find 90% of gold exchanges by rank 50, while Laya finds 30%; at rank one, Jev reaches 85% and Qwen3.5 9B 40%. On a dimension-proportional random sample of 60 MemoryAgentBench questions, Jetriever's four-dimension score is 55.4%, against 44.3% for ReFind on the same questions. Jev retrieval costs USD 0.00834 per InMind question and USD 0.03103 per MAB question on average. These results show the value of world knowledge, scores that rank decisive memories first, and affordable full-pool scoring.

### 6. Efficient Modeling of Multi-Agent Systems via Structure-Aware Physics-Informed Learning
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-16T16:57:25+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.21404
- Summary: Modeling large multi-agent systems poses challenges for trajectory inference and parameter identification, as network size and coupling increase computational demands and partial observations require reconstructing unobserved states. We propose MAS-PINN, a neural-network architecture with a tailored training algorithm for a physics-informed learning framework that leverages the network topology and the agents' similarity to reduce computational and memory costs of simulating and identifying multi-agent systems. Its architecture represents agent trajectories through shared temporal features and agent-specific coefficients. Training alternates between learning features, fitting coupled trajectories, and estimating physical parameters. A matrix-free update exploits local interactions to fit trajectories without forming large global matrices. Experiments on Lorenz rings, Lotka--Volterra networks, and Rössler oscillators show improved trajectory and parameter accuracy over baselines, including inference in large systems and identification under partial observations or unknown topology, alongside substantial computational savings in coefficient fitting.

### 7. From Recursion to Convolution: Parallel Self-Improvement for Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-16T11:00:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.20891
- Summary: Multi-agent self-improvement enables agents to improve through interaction and feedback. However, sequential dependencies across agents and refinement rounds can propagate errors, increase computational costs, and limit parallelism. Moreover, refining individual features or agents in isolation can overlook their dependencies and restrict collective coordination. To address these challenges, we propose ConvRSI, a framework for parallelizing multi-agent self-improvement through convolution. ConvRSI couples intra-agent convolution, which jointly refines related agent features, with inter-agent graph convolution, which aggregates messages according to the collaboration topology. Both stages operate in latent space, enabling parallel updates without repeatedly decoding and re-encoding intermediate messages. Experiments on MATH-500 show that ConvRSI achieves 5.04% performance improvement while reducing 17.27% inference cost, and 45.11% latency compared with RecursiveMAS. It also supports diverse collaboration patterns by representing their topologies as adjacency matrices. These results demonstrate the potential of convolutional co-evolution for efficient multi-agent self-improvement. Our code and datasets are provided in https://github.com/LYA2333/ConvRSI.

### 8. KVMARK: Fragile Watermarking for KV-Cache Integrity in Latent Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-16T03:23:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.20454
- Summary: Latent multi-agent communication directly transfers Key-Value (KV) cache tensors between transformer-based agents, bypassing text serialization entirely. While computationally efficient and reasoning accurate, this communication channel is opaque and vulnerable to man-in-the-middle tampering, a threat vector unaddressed by existing text-based or behavioral watermarks, which cannot operate on continuous internal representations. To address this vulnerability, we propose KVMark, a training-free, zero-bit KV-cache watermarking framework to verify inter-agent handoff integrity. Our framework introduces four core technical components: (1) position-dependent sign patterns that guarantee first-order statistical invisibility while preserving downstream attention survival; (2) per-head sign patterns with aligned detection to defeat head-averaging attacks; (3) a three-tier depth-aware strength schedule that equalizes detection sensitivity across transformer layers while maintaining invisibility against nine statistical profiling strategies; and (4) content-bound key derivation that cryptographically binds watermarks to input contexts, preventing replay attacks under Kerckhoffs's principle. Empirical evaluation on a four-agent latent pipeline demonstrates $100\%$ detection across $1{,}500$ handoffs with a $0.0\%$ false positive rate ($\text{AUROC}=1.0$), $100\%$ layer-level tamper localization ($17/17$ attacked layers identified with $0/19$ false positives), and no statistically significant reasoning accuracy degradation across four benchmarks ($N{=}300$--$500$). Furthermore, the framework enables multi-hop cascade verification to isolate compromised agents (500/500 detection at three hops), withstands adaptive white-box adversaries and the Out-of-Sight DiffMean attack (up to $α=8.0$), and generalizes seamlessly to Qwen3-8B without re-tuning (1,500/1,500 TPR).

### 9. HEAMS: Holistic Evaluation of Agent Memory Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-15T17:26:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.20144
- Summary: Memory systems allow AI agents to persist information across interactions, making them more personalized and more capable on long-horizon tasks. This persistence introduces new risks: stored information can be disclosed in inappropriate contexts, resist correction or deletion, be retained beyond what users desire, or be poisoned to influence later agent behaviour. Yet memory systems are typically evaluated on task performance and efficiency alone. We argue that a memory system should instead be understood as the custodian of its user's persistent information, with responsibilities that extend beyond helping an agent complete its tasks, and that it should be evaluated holistically against all such responsibilities. We present Holistic Evaluation of Agent Memory Systems (HEAMS), an open-source framework for evaluating agent memory systems in this way. First, we state the responsibilities of agent memory systems as explicit behavioural desiderata spanning performance, efficiency, security, privacy, and user sovereignty. Second, we assemble a benchmark suite that covers these desiderata and acknowledge the gaps that remain. Third, we develop MilaMem, a prototype memory system, and a governance layer that can wrap any memory system, enabling controlled study of memory system design choices. Fourth, we compare memory systems across the full HEAMS benchmark suite. We find that no memory system leads every performance benchmark, and strong performance scores may coexist with poor privacy, user-sovereignty, and security scores. Governance strongly influences results: recall policies can reduce inappropriate disclosure at a cost in helpfulness, while both recall and retention policies improve poisoning resistance. Performance and efficiency benchmarks alone therefore cannot reveal how well a memory system meets its responsibilities. Code: https://github.com/milatechtransfer/heams

### 10. Architecting the Corporate AI Infrastructure: The Evolving Roles of AI Governance Committees and Chief Ethics Officers
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-14T23:48:47+00:00
- Primary source: arxiv
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://arxiv.org/abs/2611.19670
- Summary: The accelerating integration of artificial intelligence (AI) into core business operations has created an urgent need for robust corporate governance infrastructures capable of managing complex ethical, legal, and operational risks. While organizations have increasingly adopted high-level AI ethics principles, a critical implementation gap persists: fewer than half of organizations that cite AI governance as a boardroom priority have a formalized governance framework in place. This paper addresses that gap by proposing a structured corporate AI governance architecture (CAIGA) centred on two mutually reinforcing pillars. First, it examines the evolving mandate of specialized C-suite roles, specifically Chief Privacy Officers (CPOs) and Chief Ethics Officers (ChEOs), in formalizing accountability for AI usage across the enterprise. Second, it argues that cross-functional AI Governance Committees, uniting representatives from legal, technology, data science, cybersecurity, and business units, are the essential organizational mechanism for translating ethical principles into operational decisions, including strategic go/no-go approvals for new AI initiatives. Drawing on a conceptual review of peer-reviewed governance literature, regulatory frameworks including the EU AI Act, and documented industry practice, this paper contributes a replicable governance architecture that embeds clear accountability policies, structured risk management workflows, and an organization-wide ethical AI culture. The framework is illustrated through application to the financial services sector. The findings have direct implications for corporate leaders, risk professionals, and policymakers navigating the rapidly evolving global AI regulatory landscape.

### 11. Early look at Loop, new autonomous AI agent from Google - TestingCatalog AI News
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-18T17:47:32+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMijwFBVV95cUxPRXZ4VW9LNmxaMGQyYXhtc3Rxc1V1NkhwN0ZVRTl5OXFkOEczSG9SM1VNYWg5TWEycjBJVkhUSW9qd0RNUmRpN0hheXRJTmhrbGEydFpCM3AweW5IUEwzaEwwbEpJMVdMVUhVUUFuRjVvU2pXLUFZR0c1TDBjUWVwdUFCWDNaYWZfZ0lfRm1TOA?oc=5
- Summary: Early look at Loop, new autonomous AI agent from Google&nbsp;&nbsp;TestingCatalog AI News

### 12. Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-17T17:59:13+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.23142
- Summary: The "AI revolution" has enabled teams across the technology industry to deliver software features at unprecedented velocity. While code evolves faster than ever, customer-facing documentation often struggles to stay up to speed. As users increasingly rely on LLM-based agents that consume documentation as their primary interface, the impact of this documentation gap worsens: stale information propagates and is treated as authoritative. Signals for identifying where documentation has fallen behind already exist in abundance, both explicit (e.g., resolved support tickets revealing what documentation lacks) and implicit (e.g., code-documentation discrepancies detectable from automated loops). We deploy a multi-agent system, built around a triage agent we call "TriAgent," that continuously extracts these signals and repairs documentation drift. Over 43 days of shadow-mode operation, our system triaged 499 tickets and surfaced 92 gaps in the documentation. Using a panel of LLM judges from independent model families, 81.1% of TriAgent's verifiable assertions were correct (245 of the 302 assertions the human resolution addresses; majority of three judges); on length-comparable pairs the panel preferred TriAgent's response in 70.5% of pairs and the human engineer's in 23.2% (the rest had no judge majority). Importantly, agent- and human-sourced replies tended to be complementary, with the human often surfacing insights that were either buried within the existing documentation or missing from it entirely; our system turns each such insight into a documentation gap and, after human review, a fix. Repairing a gap measurably improved the agent's later answer: when the agent re-answered the same ticket after the repair, blinded judges preferred the post-repair answer over its own pre-repair answer 71.4% of the time (n=35). A blinded human audit confirms strong alignment on self-improvement.

### 13. California sues OpenAI after autonomous AI agents allegedly hack platform - Fox News
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-17T17:32:44+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiVkFVX3lxTE5OeHZaLWRKbVRJSXdIX01lZG80Z2pFV3JoWXJWWldmV1JZcDVCME53X2owb292aVU3WTgxQjR0aEo3MWdYak45ckgzWXE5blFvSDgyUFNR?oc=5
- Summary: California sues OpenAI after autonomous AI agents allegedly hack platform&nbsp;&nbsp;Fox News

### 14. A Scalable Decentralized Event-Triggered Topology-Switching Protocol for Verifiable Safety in Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-16T18:09:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.21513
- Summary: This paper develops a decentralized event-triggered topology-switching protocol that allows agents to disconnect from the communication network while preserving state safety and excluding Zeno behavior. We establish a robust barrier function condition that guarantees safety as long as the estimation error remains within a prescribed threshold. Each agent uses locally computable certificates to determine when to connect and disconnect from the network. The certificate construction improves scalability by reducing the complexity of topology-dependent computations from $O(2^N)$ to $O(N)$, where $N$ is the number of agents. We formally prove that the protocol ensures the estimation error does not exceed the prescribed threshold and is non-Zeno. An alternating method computes an error-weighting matrix and a quadratic barrier function that guarantee safety under the proposed protocol. Finally, we evaluate the protocol on four interconnected microgrids. Compared with maintaining network connectivity at all times, the protocol reduces the time agents remain connected while keeping phase and frequency within their safe operating region.

### 15. MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-16T12:38:53+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.21019
- Summary: Multimodal large language models (MLLMs) now assist users across sessions of images and text, carried by an external memory of what was said and shown. When such an assistant answers wrongly, the failure usually began earlier, in how a record was written, updated or retrieved, and the answer alone does not say where. We formalize multimodal memory as four stages, Write, Update, Retrieve and Answer, and define nine error types across them. A stage-resolved analysis on Mem-Gallery traces most failures to a source stage, and most of those lie before the answer. Injecting known errors against fact-preserving control edits, we then follow each tainted record downstream. Early errors survive to the answer as apparent evidence, and hurt most when no other record holds the fact. A diagnosis that trusts the quoted evidence therefore blames the stage where the error surfaces, not the one where it began. We propose MemDoctor, in which the MLLM that built the memory diagnoses its own failures. It traces each needed fact backward through the four stages, accepts a diagnosis only when the cited evidence is found in memory, and repairs that stage before answering again. On a 4B backbone, MemDoctor improves accuracy on both Mem-Gallery and MemLens, outperforming all evaluated 8B baselines, and the same loop also improves MuRAG and A-Mem.

### 16. LEDGER: Auditable Agent Memory Under Change
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-16T11:37:23+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.20927
- Summary: Agent memory systems are mostly evaluated on fixed histories, and only their final answers are scored. In real use, facts change, sources differ in reliability, and users ask the agent to forget things. We present LEDGER, a memory layer in which a language model proposes facts and explicit rules decide which value is current, which source to trust, and what to delete. Each fact keeps its source and the period in which it held. LEDGER+EP adds a search over raw conversation turns for questions the ledger does not cover, and scrubs these turns on deletion. We compare both against no memory, full-history replay, retrieval over raw transcripts, and Mem0, with the same answering model and prompt, on a synthetic multi-session coding-agent workload and a 210-question subset of LongMemEval, and we score both the evidence each memory sends to the model and the answer. On the coding workload, LEDGER+EP in fallback mode answers 94.3% of questions correctly on five development seeds and 91.1% on five held-out seeds, against 82.1% and 83.3% for full replay, the strongest baseline. When a deletion request only describes the fact, no deleted value reached our systems' evidence in any evaluated probe. On LongMemEval, LEDGER+EP in augment mode has the same observed accuracy as full replay (74.8%) with 1% of its context. The main limitation is that the coding workload is synthetic and built by us; on LongMemEval, the differences between the strongest systems are within the confidence intervals.

### 17. MASTA: A Feedback-Scheduled Multi-Agent System for End-to-End Tamarin Modeling and Analysis
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-16T07:33:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.20671
- Summary: Tamarin-based formal verification of security protocols requires expert-authored multiset rewriting rules and temporal-logic lemmas. Translating a natural-language protocol description into a complete formal model with an LLM is hard because syntactic, reachability, and property-level errors compound across the multi-step modeling process, and a single agent that both authors and self-evaluates cannot reliably localize them. We present MASTA, a multi-agent system that addresses these difficulties through three innovations. First, an operational--evaluative role decomposition assigns rule modeling to an Architect, property modeling to an Auditor, and pure dispatch to a dedicated Arbiter that holds no authoring duties. Second, the Arbiter implements a Tamarin-anchored scheduler that dispatches the next agent based on the latest verifier verdict and routes problem-tagged fixes through a modification list, with a six-class problem taxonomy and an LLM deduplication check preventing routing deadlock. Third, we construct a benchmark of 10 protocols paired with 139 mutation variants and five fine-grained metrics that jointly assess model correctness ($M_1$--$M_3$) and completeness ($M_4$--$M_5$). On this benchmark, MASTA on Qwen 3.5-plus improves over OpenCode on the same backbone by up to $+0.27$ on individual metrics and ranks first on both the correctness and completeness averages, surpassing Codex (GPT-5.5) and Claude Code (Opus 4.7) despite using a weaker LLM. Ablations on five protocols confirm that removing the Arbiter collapses property and verification scores to zero.

### 18. Ontology-Compiled Control Barrier Functions for Heterogeneous Robot Teams
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-15T23:09:52+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.20306
- Summary: Safety filters for heterogeneous robot teams fail because of missing constraints, overestimated braking capabilities and conflicts between individually satisfiable constraints. We present OntoCBF, which compiles a domain ontology with a class taxonomy, typed relations, safety axioms and a dynamics profile per robot class into a control barrier function filter with one quadratic program per agent. Description-logic entailment supplies the constraints of any team online, including those that follow from chains of relations and from classes defined by what a robot carries, so the existing safety axioms cover new robot classes, payload classes and combinations. We prove that a subclass may reuse the braking capability of its parent whenever it can produce every velocity of the parent, a property separate from subsumption. For box-bounded double integrators this property is also necessary, and every loss of safety then begins with a conflict. Once three robots interact, the safe set of pairwise barriers contains states from which a collision is unavoidable, and such states persist in larger teams under any fixed capability reduction. In a simulated warehouse where humans ignore the robots, a filter written for the design classes violates safety in 89-100 % of the episodes with unseen classes. In all scenarios, including one with 32 robots, OntoCBF violates safety in 20-70 % of the episodes, each time after a conflict, with a median deepest intrusion of 10-17 % of the keep-out distance. A multi-agent PPO policy trained with the filter in the loop lowers the rate of infeasible quadratic programs, nearly all of them conflicts, by 18-41 %.

### 19. StaleBench: Isolating Stale Retrieval in Agent Memory, and Pricing the Fix
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-15T03:29:02+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.19752
- Summary: An agent that stores facts over time eventually stores several versions of the same fact. Asked a value-agnostic question - "which team does X play for now?" - a similarity retriever cannot prefer the current version, because every version matches the entity the query names. StaleBench isolates this stale-retrieval failure on 892 real updating facts, with currency labels from the source (Wikidata validity years via TempLAMA), never from a retrieval score. Our central result is that retrieval metrics can rank memory policies backwards: a retention policy and its retain-everything control return the identical statement at rank 1 for every test query, yet differ by 29.5 and 65.6 points in reader accuracy on two readers when no date is shown. Contamination@5, the metric we add, ranks them correctly where current@1 and current@5 do not. Withdrawing the lexical anchor that statements carry costs deployed keying mechanisms tens of points of freshness; entity resolution on both the write path and the query recovers most of the loss. Three deployed systems (Mem0, Graphiti, LangMem) and a reimplemented ERASE each handle supersession differently, and no single scoring convention describes all four. We release the data, a frozen evaluator, and reference baselines.

### 20. Cooperative Transport of Unknown Objects by Distributed Effort Regulation in Multi-agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-15T02:25:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.19731
- Summary: A distributed multi-robot object transportation strategy is proposed for objects of unknown shape, size, geometry, mass and mass distribution without any prior knowledge about the object or number of robots involved in the transportation process. Robots follow the boundary of the object and dynamically determine viable pushing points. A novel object-model-free heading-error-driven pushing effort regulation method is proposed to promote goal-directed object motion; robots regulate their pushing effort using individual and collective heading errors. Robots dynamically relocate around the object boundary if a pushing point is lost or the required pushing effort exceeds its capability to correct its heading. The proposed method is validated using simple and complex shapes with convex and non-convex boundary regions and dynamically changing weight distribution of objects. Detailed analysis on the effects of robot distribution and initial object pose on the transportation performance in terms of required time and path efficiency is also presented. Scalability analysis revealed that object transportation time is dependent on the number of pushing surfaces available which in turn depends on the object size, shape, and set inter-robot safety distance. The proposed system yielded highly efficient object paths with consistent elapsed transport times over several trials robust to external disturbances such as non-uniform friction between contacting surfaces and robot wheel slip.

### 21. Read Boundaries in Agent Memory: Consistency, Completeness, and Repair
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-14T08:42:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.19264
- Summary: Agent-memory services assemble evidence through several reads across connections or stores. An update between those reads can pair an assertion with source content from another revision. We protect the complete recall, including enrichment and materialization, and evaluate the resulting evidence and service behavior in Hindsight and Cognee. A 600-run Cognee study compares unprotected recall, a repeated recall, a read/write lock, and optimistic epoch validation under default incremental updates and full rebuilds. At approximately 20 recalls/s, unprotected default updates yield 199 conflicting responses among 12,010 scheduled recalls with spaced writes and 284 among 12,010 with bursts. The lock and epoch validation each deliver complete, compatible evidence for all 24,020 default-update recalls. With default bursts, epoch validation reduces update p95 by 109 ms while adding 290 ms to recall p95 relative to the lock. A separate 160-run incremental-failure study distinguishes mixed revisions from complete new derived content whose canonical source record remains old. Both protected policies refuse service after failure; the first default retry restores all 80 fault runs through native full-rebuild fallback. In Hindsight, a shared PostgreSQL snapshot removes the mismatch in ten controlled pairs, with recall p95 rising from 19 ms to 29 ms. These results identify the read boundary needed for coherent evidence and the publication and recovery conditions governing service after an update fails.

### 22. Show HN: ADE Index – a sourced and ranked index of 975 agentic coding tools
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-19T01:33:52+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://adeindex.com
- Summary: No summary.

### 23. Satya Nadella predicts AI agents will reshuffle the economics of the web
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T22:58:11+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/18/satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web/
- Summary: Microsoft's CEO says AI agents could disrupt advertising-driven business models, forcing companies like Amazon to rethink how they compete for customers.

### 24. Snapchat now lets developers build AR Lenses with AI assistants like Claude Code and Cursor
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T19:56:39+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/18/snapchat-now-lets-developers-build-ar-lenses-with-ai-coding-assistants-like-claude-code-and-cursor/
- Summary: Lens creators can describe the Lens they want in plain language, and their AI assistant handles the process from start to finish, Snapchat says.

### 25. Spend management platform Payhawk announces $280M raise, 2B valuation
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T19:29:41+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/18/spend-management-platform-payhawk-announces-280m-raise-2b-valuation/
- Summary: Founded in 2018, Payhawk is an enterprise financial management platform that helps companies track and manage expenses and procurement using AI agents.

### 26. More banks say customers using AI agents are on their own — even if they get hacked
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T17:32:10+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/18/more-banks-says-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacked/
- Summary: Citi is the latest major financial institution to put the breaks on personal finance AI agents.

### 27. Launch HN: Maritime (YC F26) – A managed cloud for production AI agents
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T17:26:28+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://news.ycombinator.com/item?id=50549188
- Summary: Hi HN, we&#x27;re Ary and Maria, co-founders of Maritime (<a href="https:&#x2F;&#x2F;maritime.sh">https:&#x2F;&#x2F;maritime.sh</a>). We&#x27;re building an agent-native cloud that handles everything from custom environments to lifecycle management for AI agents.<p>Demo: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=lCWMdBQ96rY" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=lCWMdBQ96rY</a><p>There’s been an explosion of sandbox companies coming out of SF, but sandboxes solve maybe 10% of the infrastructure problem for AI agents. The approach that most sandboxing companies take is:<p>You buy Hetzner&#x2F;OVH Cloud bare metal servers, use Firecracker to slice the servers up into VMs, sell those VMs with low margins.<p>It’s a bit of an oversimplification, but the point is it’s a narrow solution to a fairly difficult problem.<p>We talked to a couple hundred companies that are building AI agents. From personal assistants and coding agents to specialized healthcare agents, and the main pattern we saw was that even after choosing a sandbox provider, you still have to build additional infrastructure just to get things working. These were the primary points of friction:<p>1. Agent lifecycle management.<p>There’s a lot that you have to build in order to properly give your agents VMs: things like sleep&#x2F;wake, persistent storage, triggers, scheduling, per-user routing and spend caps, health monitoring, failure recovery, and deploying updates across thousands of VMs without downtime. There are so many of these small sandbox management tasks that companies have to build and maintain themselves, and they add up.<p>2. Custom environments.<p>Production agents have varying needs. Some agents need Windows applications. Others need Android, browsers with persistent sessions, custom operating system images, preinstalled desktop software and applications, or specific dependencies. Some agents need access to private networks to interact with …

### 28. AI agents ask better questions than KPMG accountants in audit trial
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T15:49:34+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/
- Summary: No summary.

### 29. Felicis leads $7.5M bet on Unsiloed AI to make enterprise documents usable by AI agents
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T12:00:00+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/18/felicis-leads-7-5m-bet-on-unsiloed-ai-to-make-enterprise-documents-usable-by-ai-agents/
- Summary: With a team of just seven, Unsiloed AI plans to compete with tech giants and specialized startups in the crowded AI document-processing market.

### 30. worldinmotion
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T05:53:41+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/worldinmotion
- Summary: <p> Encrypted messages between AI agents, across vendors </p> <p> <a href="https://www.producthunt.com/products/worldinmotion?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1321152?app_id=339">Link</a> </p>

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

### 3. Evaluating Language Models as Orchestrators in a Tool-First Biomedical Discovery Platform
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-16T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.13.766436
- Summary: Large language models (LLMs) increasingly orchestrate agentic biomedical discovery systems, but cloud deployment raises concerns about inference cost, data privacy, and governance. Small language models (SLMs) that run on-premises are an alternative, provided they orchestrate scientific tools about as well as larger models. We built a tool-first, multi-agent system for scientific discovery in which an orchestrator coordinates six specialized tool systems: differential expression, literature retrieval, pathway enrichment, network-based gene prioritization and knowledge-graph analysis, perturbation signature matching, and structural/druggability assessment. In a tool-first design, specialized tools supply the domain knowledge and computation, so the model's main task is coordination, e.g. choosing tools, passing the right parameters, calling them in the right order, and carrying results across turns. With the tools, prompts, workflow, and benchmark held constant, we compared three orchestrators, Gemma 4 (26B, open-weight and locally deployable), Gemini 2.5 Flash, and Claude Sonnet 5. Evaluation used a custom benchmark of 104 single-turn and multi-turn tests, an LLM-as-judge protocol (groundedness and evidence validity), tool-use accuracy and efficiency metrics, and blind expert review. On single-turn tasks, the three models performed comparably, and reviewers did not rate the SLM below the larger models. In multi-turn tasks, Claude Sonnet 5 showed marginally higher evidence validity, Gemma 4 was weakest when parameters had to be assembled across turns, and all three models struggled with tool ordering on memory-dependent tasks. These differences were illustrated with case studies. Finally, we propose strategies to help SLMs address the multi-turn limitations and support cost- and privacy-aware deployment.

### 4. WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems
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

### 5. Multi-Modal Multi-Agent System for Bridge Operation and Maintenance based on Large Language Model
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-11-02T08:26:24+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02738
- Summary: Bridges are critical transportation infrastructure, and reliable operation and maintenance (O&M) is essential for traffic safety and long-term structural performance. However, bridge O&M faces key bottlenecks: no unified architecture coordinates heterogeneous resources; model inferences lack clear links to physical-mechanical laws; and experts' tacit knowledge remains difficult to formalize. This study proposes a knowledge-enhanced autonomy formalization methodology and apply it to construct the Bridge O&M Multi-Modal Multi-Agent System (BOMMA), which integrates heterogeneous diagnostic actions, physics-mechanics-informed representations, long-term memory, and structured experiential knowledge within a coordinated multi-agent workflow, enabling interpretable and traceable scheduling, analysis, and decision-making. On 3,492 multi-source instructions, the proposed method achieves scheduling recalls of 85.37% for simple and 99.40% for composite tasks, with 95.35% BERT F1-score for O&M action reasoning. Ablation studies confirm the contributions of the components in the autonomy. This study bridges general LLM reasoning and specialized bridge O&M requirements.

### 6. Locating and Closing Information Gaps in Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-29T14:45:43+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.40186
  - Alt: https://arxiv.org/abs/2610.18780
- Summary: Multi-step Web tasks often require several LLM agents to gather and combine evidence. The communication graph of a fixed workflow restricts which agents can read each other's outputs: evidence retrieved by one agent may never reach the agent that needs it, leaving an information gap and an incomplete or incorrect answer. Adding a connection can deliver the missing evidence, but can also lead the receiver to adopt an incorrect upstream conclusion that displaces a correct answer; the final output alone does not separate the two. We propose Selective Probing and Link Insertion for Closing information gaps in multi-agent Execution (SPLICE), which locates information gaps per query and decides what to adopt after adding an edge. After the original workflow runs, SPLICE uses the query and node outputs to locate a possible gap, adds one directed edge from a source to a receiver to deliver the relevant evidence, and re-executes the receiver and affected downstream nodes, producing a candidate answer. The adoption decision reads both the final answers of the two runs and the process changes the edit caused inside the workflow: how far the receiver moved, where its new content came from, and whether the change reached the final answer. A selector trained on these process features chooses between adopting the candidate answer and retaining the original. On five benchmarks, SPLICE raises the task score on Web tool use by 8.0% and the mean score on four reasoning and planning benchmarks by 5.7% relative to the static skeleton, at 1.25 to 1.44$\times$ the skeleton's cost, and transfers zero-shot to four unseen backbones.

### 7. EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-25T17:09:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.34450
- Summary: Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control. Agents need to adapt to other agents at test time and reuse accumulated experience to refine their interaction strategies for future interactions across cooperative, mixed-motive, and adversarial settings. However, existing approaches often develop adaptation mechanisms for particular interaction settings. This raises a central question: how can decentralized MAS support test-time adaptation and reliable experience reuse across interaction settings? We propose EvolveMAS, a unified self-evolution framework that supports experience-driven adaptation within and across episodes. EvolveMAS pairs each main agent with a dedicated MemoryAgent for test-time memory governance, which maintains isolated Structured Memory outside the main agent's reasoning context. EvolveMAS organizes adaptation into two complementary processes: Within-Episode Online Adaptation and Cross-Episode Knowledge Evolution. During Within-Episode Online Adaptation, MemoryAgent updates episodic, semantic, and working memory from interaction evidence to inform subsequent actions. During Cross-Episode Knowledge Evolution, the main agent uses memory and episode outcomes to distill reusable interaction knowledge comprising partner profiles and interaction strategies for subsequent episodes. Across five benchmarks and six evaluation configurations spanning the three interaction settings, EvolveMAS achieves the highest normalized average score of 77.2 among the compared methods. Ablations show that test-time memory governance and cross-episode knowledge reuse both improve performance. Interaction traces further illustrate how updated memory and distilled knowledge guide subsequent interactions. These results support experience-driven adaptation in decentralized MAS without updating model parameters.

### 8. From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-21T10:49:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.29560
- Summary: Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work has begun to address these challenges by augmenting foundation-model policies with memory and by introducing hierarchical architectures that separate high-level planning from low-level execution. We organize the high-level VLM as a robotic agent through an editable harness to maintain task context and improve planning through execution experience. We instantiate this approach as SERA (Self-Evolving Robotic Agent), with a fixed VLA executor providing low-level control. The harness maintains and updates task context using observations and execution feedback to guide subsequent planning. Self-evolution uses environment rollouts to propose and evaluate harness revisions, with the selected configuration fixed before held-out testing. On RoboMME, SERA achieves 51.38% overall success with autonomous selection, compared with 44.38% without self-evolution. Our exploration suggests that agentic planning is a promising direction for history-dependent robotic manipulation.

### 9. Refuse the Harm, Complete the Task via Graph-of-Rules Planning for LLM-Enabled Robots
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-17T10:13:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.24603
- Summary: Large Language Models (LLMs) are increasingly used in embodied AI for robotic manipulation and planning, but their deployment in physical systems exposes vulnerabilities such as jailbreak attacks that induce unsafe behavior. Existing inference-time defenses are mainly evaluated on short instructions containing a single hazard, whereas realistic tasks may interleave safe and unsafe sub-tasks, conceal hazardous steps, or combine individually safe actions into unsafe outcomes. Such compound instructions make it harder for a single safety decision to distinguish hazardous sub-tasks from legitimate ones, risking either overlooking the hazard or rejecting the whole instruction. We introduce safe task completion, a task that requires an LLM-enabled robot to refuse the harmful part of an instruction while completing its legitimate part. To address this problem, we propose RuleGraph, a multi-agent Graph-of-Rules planning framework that distributes safety enforcement across multiple reasoning and verification stages. Five cooperating agents are used to ground general safety principles into world-specific rules, assess the instruction's sub-tasks in context, and derive a safe goal from the legitimate ones. Planning toward this goal is then organized as a graph of rule-specific nodes, where higher-level nodes inherit the union of their parents' rules, and candidate plans are progressively verified and aggregated until a single plan satisfies every relevant rule. In this way, RuleGraph reduces reliance on a single centralized safety decision. We evaluate RuleGraph on pure-attack and compound instructions across two benchmarks in two environments using Attack Success Rate (ASR) and Task Success Rate (TSR). RuleGraph reduces ASR to 0% on both benchmarks while achieving the highest TSR among all methods, reaching 98.57% on the RoboGuard benchmark and 84.54% on our long-horizon compound instructions.

### 10. ChunkAct: Action Chunking for Agentic Robotics
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-13T17:59:57+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.18874
- Summary: Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.

### 11. Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-17T06:21:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.22275
- Summary: Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically coupled interactions between humanoids, enabling coordinated decentralized control from local observations alone. At the high level, we train a vision-language planner and design a speech-based leader-follower coordination mechanism to synchronize decentralized execution without network communication. Trained with two identical humanoids, our system scales to teams of up to ten robots and generalizes to heterogeneous teams without retraining. To benchmark these capabilities, we introduce HH-Bench, comprising 12 tasks involving teams of 2 to 10 humanoids, including heterogeneous teams. Systematic evaluations show that Heave-Ho consistently outperforms baseline methods, while real-world experiments demonstrate robust decentralized collaboration across challenging tasks.

### 12. Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-17T05:47:01+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.22245
- Summary: Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts. This creates a consistency challenge: facts retrieved by workers may be missing from the evidence available to the lead for a joint conclusion. We introduce a benchmark and evidence-flow profiler for studying multi-agent memory inconsistency through controlled factual conflicts in Harvey LAB document-review tasks. Pooled across three models with comparable generation spending, requiring delegation increases retrieval of both conflicting claims from 50.2% to 68.7% relative to single-agent execution, yet conflict detection falls from 16.2% to 13.2%. Within this setting, workers report both claims for only 35.2% of retrieved pairs, and pooled matched comparisons show higher detection than single-agent execution when one worker reads both claims but lower detection when the claims are split across workers. Worker-to-lead handoffs are a central target for improving conflict detection in multi-agent LLMs.

### 13. EvoDisco: Strategy Discovery for Evolving Agent Memory
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-17T02:37:56+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.22102
- Summary: Large language model agents accumulate experience in memory, and how that memory evolves during interaction is as important as what it stores. Recent methods update memory online, yet both the operators that transform memory and the rules that select them remain fixed by design. We propose EvoDisco, which formulates agent memory evolution as evolutionary strategy discovery: the agent must discover which operator to apply, when to apply it, and how to instantiate it, rather than rewriting memory under a static operator schedule. A learnable policy conditions on the current memory state and recent task history, then selects and instantiates one of four semantic operators---Abstract, Refine, Bridge, and Reframe---which respectively compress related memories, decompose overloaded entries, connect weakly linked experiences, and reorganize retrieved reasoning chains. The policy is updated with a bi-level fitness. An inner signal scores each transformation using a retrieval-quality improvement regularized by memory complexity. An outer signal scores strategic efficacy over a window of past decisions, combining historical operator-utility regret, utility-prediction error, and selection diversity. Under a one-pass online plus frozen-transfer protocol on ALFWorld, WebShop, and LifelongAgentBench (OS and DB), EvoDisco improves over strong memory baselines including MemP and MemRL. The largest gains are on ALFWorld ($+8.8$ online / $+12.9$ frozen-transfer points over MemP; $+16.4$ / $+17.9$ over MemRL). Ablations attribute these gains to both fitness levels and the operator library.

### 14. From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-13T17:59:40+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2611.18484
- Summary: AI-enabled remote patient monitoring is evolving beyond passive data collection toward agentic AI systems that interpret patient states, coordinate care, and initiate action across domestic and clinical settings. This structured scoping review finds that mature agentic care has not yet emerged: Most systems remain human led, while stronger decision-action coupling and embodied AI remain largely confined to prototypes and pilots. Healthcare robotics makes the transition from monitoring to action especially visible by translating AI-generated recommendations and decisions into speech, movement, prompting, physical assistance, escalation, and care coordination, making embodiment, clinical integration, human oversight, and governance fundamental design requirements. Further progress requires safe and interoperable care architectures in which intelligent components operate through clinically validated and accountable workflows. We propose agentic robotics as a future direction for supervised systems embedded in the care ecosystem, connecting AI agents and robots with clinicians, caregivers, and patients through auditable workflows that can be interrupted and remain subject to human oversight and explicit AI governance.

### 15. On Private Knowledge Retrieval and Private Inference for secure multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-10T07:43:02+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.13696
  - Alt: https://arxiv.org/abs/2610.23078
- Summary: Multi-agent systems provide a convenient framework for the massive deployment of agents based on Large Language Models (LLMs). It provides a sound framework where agents can interact with existing software to perform actions in an autonomous way. Agentic AI is the new term to denote these AI-based autonomous systems. In real multi-agent systems, agents need to deal with malicious agents some of which can exploit security vulnerabilities to do harm. A memory poisoning attack is an example of exploiting a vulnerability to modify agents knowledge and, thus, affect its behavior. In an agent, there are different types of memory systems (semantic, episodic, and short-term) which have their own characteristics and for which different memory poisoning attacks may be developed. In this paper we focus on semantic memory, we discuss its attack, and mitigation strategies. We introduce private knowledge retrieval and private inference. We propose a signature system in the knowledge base to prevent from undesired manipulation. This should avoid memory poisoning attacks by introducing security by design in the construction of the semantic memory. In our architecture, an agent contains a local Prolog-like inference system (i.e., using Horn clauses to represent knowledge) which accesses an external knowledge base to get the required knowledge. This externally signed knowledge base is accessed privately. We provide different implementations in Python using different privacy levels including k-anonymity and information-theoretical privacy (IT-PIR).

### 16. A Common Recognition Architecture Across Memory Scales
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-09T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://www.biorxiv.org/content/10.64898/2026.11.04.764437
- Summary: Recognition decisions occur across memory episodes that vary vastly in scale, from compact single-item episodes to extended experiences involving hundreds of items. To test how memory scale shapes the neural mechanisms underlying old/new judgments, we recorded EEG while participants performed a recognition memory task across set sizes ranging from 1 to 128 items (spanning 2 to 256 recognition judgments). Classic electrophysiological signatures of recognition, including frontal and parietal old/new effects, persisted continuously across set sizes. Furthermore, multivariate neural classifiers trained on small memory scales generalized robustly across set sizes. Rather than revealing distinct neural formats, increasing memory scale produced systematic, continuous shifts in the timing and strength of a shared recognition response: signals emerged progressively later and weaker at larger memory scales. Temporal-alignment and cross-correlation analyses demonstrated that responses across scales followed a common waveform trajectory, with timing shifts propagating into motor response preparation. Finally, individual difference analyses revealed that this common recognition format exhibits scale-dependent behavioral relevance, tracking working-memory capacity at smaller scales and long-term memory performance at larger scales. Together, these findings demonstrate that recognition signals share a common neural format across scale while changing dynamically in timing, strength, and behavioral relevance, providing evidence for convergence onto a shared recognition architecture.

### 17. Coordinated Mixed-Precision KV Cache Quantization for Efficient LLM-based Multi-agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-06T17:07:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.10096
- Summary: LLM-based multi-agent systems solve complex tasks through collaboration, but their growing, simultaneously resident key-value (KV) caches create a memory bottleneck. Applying single-model quantization policies independently ignores differences in agents' precision needs, potentially degrading collective reasoning. We introduce Coordinated Mixed-Precision KV Cache Quantization (CoMixKV), which combines online sensitivity estimation with joint agent-layer bit-width allocation under a shared memory budget. To our knowledge, CoMixKV is the first mixed-precision KV-cache quantization framework to jointly allocate precision across simultaneously resident agent caches under such a budget. The estimator derives sensitivity from a local attention-error bound using recent queries, keys, and values, without calibration data, trial quantization, or additional model passes. A shared controller combines these scores with remaining quantizable capacity and byte-level storage costs to minimize total estimated error. Allocations are refreshed as agents start or finish and new observations become available. Selected widths apply only to newly quantized blocks; recent states retain native precision and previously quantized blocks remain unchanged. Across four benchmarks and three LLM backbones at average 2-bit, 3-bit, and 4-bit settings, CoMixKV achieves strong accuracy against the evaluated quantization baselines. At the average 3-bit setting on Gemma-4-31B-it, it achieves 68.35% average accuracy, exceeding the strongest quantized baseline by 0.59%. On Qwen3-32B, it reduces peak KV-cache memory by 32.08% and achieves a 1.38x inference speedup over FullKV.

### 18. HomeLoop: A Simulation Framework and Benchmark for Robot-IoT Coordination in Everyday Domestic Assistance and Safety
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-06T02:54:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.08914
- Summary: Recent progress in embodied robotics is bringing robots closer to deployment in homes, as vision-language models (VLMs) are demonstrating significant advances in reasoning, making VLM-driven robots promising home assistant agents. These agents will often be introduced into homes that already have cameras, Internet of Things (IoT) devices, and residents with wearables. To fulfill their potential, they need to integrate with existing smart infrastructure and reason through ambiguous scenarios: a smoke alarm may come from a pan about to ignite, a pan already on fire, a resident cooking or a faulty sensor, and each calls for a different response. To that end, we introduce HomeLoop, a simulation framework and benchmark built on Isaac Sim that combines robot bodies, networked devices and wearables, simulated residents and visitors, faulty sensors, and hazards that evolve over time. Our benchmark is composed of 20 tasks across five families grounded in real-world household hazards and needs, and designed so that the same alert can have different causes. A runtime monitor scores each episode with temporal-logic checks on the final outcome and the actions along the way, and every action carries a predefined cost. We evaluate six open-weight and proprietary VLMs. The best achieves a family-balanced score of 61.9%, and across models we see a pattern of over-reaction: failed episodes involving prohibited interventions outnumber those involving missed required interventions by more than two to one, with models often shutting off the stove before investigating the alarm's cause. HomeLoop is an extensible foundation intended for use in research on robot-IoT coordination, long-term memory, proactive assistance, and privacy-safety trade-offs. HomeLoop will be released with 2,100 home layouts that can be automatically furnished in diverse configurations, five robot bodies and 20 networked device types.

### 19. H^2MARL: Hierarchical Heterogeneous Multi-agent Reinforcement Learning for Humanoid Robot Control
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-04T13:48:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.06523
- Summary: Coordinated whole-body control of humanoid robots remains challenging due to high-dimensional coupled dynamics and substantial physical heterogeneity across joint degrees of freedom (JDoFs). Existing multi-agent reinforcement learning methods either employ coarse agent partitions or directly apply generic heterogeneous-agent algorithms, while hierarchical controllers commonly optimize high-level planning and low-level execution independently, leading to uncoordinated motion. In this paper, we propose H^2MARL, a hierarchical heterogeneous multi-agent reinforcement learning framework with two key mechanisms. We first formulate humanoid whole-body control using a JDoF-level physical-heterogeneity-aware policy factorization, where each torque-actuated JDoF is conditioned on an explicit descriptor of its actuation, kinematic, and dynamic properties. Moreover, we develop a closed-loop policy-executor co-optimization mechanism that jointly adapts the high-level pose planner and the low-level joint executor using shared interaction trajectories, thereby reducing the distribution mismatch between planning and execution. Extensive experiments in MuJoCo and Isaac Gym demonstrate that H^2MARL consistently improves locomotion stability, gait coordination, and motion quality over homogeneous, coarse-grained, and independently optimized alternatives.

### 20. ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-03T04:57:47+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.04321
- Summary: Multi-agent LLM systems assign different responsibilities to different agents: one plans, another retrieves evidence, another verifies, another executes. This division of labor is only meaningful if each agent stays within the functions it is authorized to perform. Over many turns, however, an agent can produce a locally reasonable message that exercises authority belonging to another role: a verifier that begins planning, a retriever that asserts unsupported conclusions, an executor that changes state no one approved. We formalize this as role drift, a turn-level breach of an agent's role contract. We introduce Agent Trajectory Control (ATC), which makes each role's authority explicit as a contract and enforces it at the point where a message would enter the shared conversation. ATC scores a proposed output for out-of-role deviation, leakage into the functions of other roles, impermissible speech acts, and logical contract breaches, then computes a leakage-regularized target that constrains regeneration; the revised message is re-checked before admission. Enforcement acts on the message rather than the generator, so ATC governs agents whose internal representations are unavailable. Across homogeneous and heterogeneous teams, ATC improves task performance and role consistency while lowering role-drift energy relative to strong baselines spanning prompting, memory, workflow control, and activation editing, with the largest gains under explicit role-confusion stress tests and in larger, more diverse teams.

### 21. Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-02T01:09:24+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2611.02361
- Summary: Can a language model that reads the full history of an access log say whether a service may act now? On an executable benchmark of grants, withdrawals, reinstatements, expiries, groups and change windows under a known policy, scored on pairs of histories that differ only in the order or one field of the deciding events, open models of 7 to 32 billion parameters fall from 72 to 86 percent after eight or sixteen events to 48 to 55 percent after 256, while reasoning-trained 32B models reading the current state reach 96 and 98 percent. A reasoning model of 120 billion parameters trails the state by four and seven points at 256 and 512 events and by about ten at 1,024, so the length beyond which explicit state outlasts long context grows with the reader. We treat agent memory as recursive filtering. The decision depends on the history only through a state whose size is set by the number of tracked keys. A store holding fewer component records than the state forgets on a time scale set by its capacity, and a reader model predicts its accuracy within 0.02 on average in a registered test. Retaining log lines without regard to time order errs with probability approaching one half, a bound that is attained. A filter in which a model parses each line and an explicit rule applies the updates answers 80 to 89 percent at 256 events and beats relevance retrieval, model-kept ledgers, a reimplementation of StateMem and the Mem0 library. A retriever that selects at query time the lines the queried state depends on matches it at 256 events on the first domain, so what decides is selection by the state's dependencies, which the filter performs when writing, without the query. Applying parsed updates themselves, the models fall to 58 and 59 percent. A frozen replication on a second domain with fresh wording reproduces the horizon.

### 22. Head movement allocation in freely-moving macaques learning object-context sequences
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-02T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.1101/2023.12.11.571113
- Summary: Flexible learning and long-term memory are hallmark features of primate cognition that are shaped by interactions with changing environments. A comprehensive understanding of these brain-body-environment interactions requires minimal constraints on behavior, and environments rich with conditional cues that encourage diverse behavioral dynamics. In this study, we introduce a multi-level enclosure (Treehouse) that allows for independent control of spatially distributed touchscreens for studying cognition in freely moving macaques. To test flexible learning, two monkeys completed trials consisting of a regular sequence of conditional object choices (targets) across four distinct spatiotemporal contexts (screens). Both monkeys acquired numerous unique, conditional object-context sequences without detriment to new learning as memoranda accumulated. They also successfully recalled their correct choices after weeks without exposure. To assess how monkeys allocate movement during learning and memory-guided decision making, we tracked their head kinematics and used recurrent neural networks to decode different aspects of their engagement with the environment during the choice epoch of the task. One such model predicted the position of the object about to be touched, including on error trials, tracking overt gaze towards objects. Separate models decoded sequence corner, the ordinal step, and the individual screen stations the monkeys occupied, despite identical stimulus layouts and behavioral demands at each station. Head movements also showed efficiencies that the task did not require: under conditions of uncertainty, monkeys were biased in their initial search locations to the targets that were closest to reach, and across days they made smoother head movements as training progressed, with no change in accuracy. These results demonstrate the potential of immersive 3-D environments, in which body kinematics can shed light on animals' goals, and reveal that situated learning …

### 23. The Agentic Observer Hackathon: Autonomous Decision-making in Simulated Astronomical Surveys
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-11-01T15:25:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2611.01988
- Summary: Astronomical surveys must allocate observing time while responding to changing conditions and competing scientific priorities. We present the Agentic Observer Hackathon (AOH), a community challenge for studying autonomous survey operations. Within a synthetic multi-object survey with prescribed exposure responses and assignment constraints, decision systems select pointings, assign targets and choose exposure configurations while responding to observing requests, instrumental faults and data loss. We evaluate systems submitted by 102 teams on campaigns reserved for evaluation and analyse target completion in a reference campaign. The leading systems combine numerical exposure planning with language models for interpreting operational information and supporting longer-term decisions. Exploratory tests show improved fault reporting with model access in several systems, while revised scientific priorities produce substantial changes in ranking. The reference campaign traces target completion and diagnoses errors in the baseline's inference of prescribed quality bands. The released simulator and reference strategies provide common survey conditions for comparing exposure allocation, target selection and recovery from interruptions.

### 24. A complete analytical characterization of optimal collision-free motion for two robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:53:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41558
- Summary: Collision-free motion planning for multi-agent robotic systems remains an active research area because of the complexity of coordinating robot trajectories, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. Importantly, the analytical difficulty of nonconvex collision-avoidance constraints has so far driven the development of exclusively numerical methods. We derive a complete analytical characterization of the optimal trajectories for two robots that start and end at rest, under double-integrator dynamics and a squared-acceleration objective. We prove that these trajectories belong to eight distinct contact families and determine which family applies for each configuration of initial and final positions. We analyze the geometrical properties of the optimal trajectories, provide a numerical algorithm for computing them, and discuss how these insights may improve the performance of existing numerical trajectory optimizers.

### 25. Contact-based optimization for collision-free motion planning for a million robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-30T10:46:26+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.41548
- Summary: Multi-agent robotic systems have attracted growing interest in recent years, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. At the planning level, robot motion is often modeled using double-integrator dynamics (with low-level controllers handling the physical dynamics during execution) with a minimum-energy objective subject to collision-avoidance constraints and limits on position, velocity, and acceleration. The complexity of the problem resides in the constraints, which couple the trajectories and make the optimization problem nonconvex. Existing numerical approaches typically discretize and optimize entire trajectories, which becomes expensive for large fleets. We exploit the structure of optimal trajectories by organizing optimization around contacts, at which robots reach the minimum allowed separation. We formulate a coupled algebraic system in contact variables and reconstruct trajectories analytically between contacts. Our algorithm, sequential contact insertion (SCI), starts from unconstrained trajectories, inserts contacts at separation violations, and jointly adjusts their times and states. Numerical experiments demonstrate planning for one million robots in minutes and thousands of robots in fractions of a second. On problems feasible for a fixed-grid sequential convex programming baseline, SCI achieves median speedups of several orders of magnitude at matching solution accuracy.

### 26. Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-28T20:40:33+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.38869
- Summary: Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments across retrieval, memory, tools, and peer communication. In this paper, we define belief as an engineering abstraction for evidence-based commitments that guide downstream action. Building on this view, we propose the Explicit Belief Multi-Agent System (EB-MAS), which externalizes belief states into a structured substrate, uses belief operators to propose candidate updates, and applies a Cognitive Firewall to bound or reject updates that are weakly evidenced but strongly driven by vulnerability cues. We also discuss the risk of group belief at the group level, including manufactured consensus, collusion, and cascading misinformation, and outline practical integration challenges around grounding, false positives, scalability, and ethical misuse. Therefore, scalable agent safety requires not only better output filtering or stronger base models, but also explicit interfaces for tracing, calibrating, and constraining belief revision at runtime.

### 27. Remembering Is Not Enough: Refining Memories and Learning When to Use Them in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-27T05:12:46+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.36652
- Summary: Memory helps LLM-based multi-agent systems reuse experience, but stored advice can be flawed or applied in the wrong situation. Team-level success or failure alone cannot reliably show whether a memory needs correction or should not have been used. We propose DiscernMem, a training-free framework that improves both memory quality and memory use. To improve quality, Defect-Aware Memory Refinement (DMR) compares team executions with a single memory and with no memory, diagnoses rule defects, and tests repairs on current and earlier tasks to guard against losing previously useful behavior. To guide appropriate use, Boundary-Learning Meta-Memory (BLM) records each memory's past uses and effects, learning when its owner role should apply or avoid it based on task context and incoming messages. Together, these components help teams correct flawed experience while retaining useful rules that were applied incorrectly. Experiments with Qwen3-4B-Instruct-2507 on four benchmarks show that DiscernMem achieves the highest average score on AutoGen, CAMEL, and MacNet, exceeding the strongest reported baselines by 0.51-4.32 points. It leads on code generation and symbolic planning across all three systems, including a PDDL score of 37.71 versus 28.48 on CAMEL.

### 28. Compatibility and future-proof testing for multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-26T21:14:03+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.36289
- Summary: Independently developed autonomous agents, such as autonomous vehicles, must guarantee joint compatibility, such as safety and task-completion requirements, when they operate in a shared environment. Existing methods require a centrally designed specification, or interaction mechanism before any agent is deployed. However, such centralized design is unrealistic when agent designs are confidential to their developers, and it is not flexible enough to accommodate future agent designs. We study a bi-level structure in which a regulator coordinates developers by publishing seed agents, and each developer independently tests its agent to ensure that it is compatible with every seed-compatible agent, a property we call future-proofness. Under this structure, joint compatibility is guaranteed for any agents that are designed and tested independently, without any coordination with each other. In this work, we first formulate compatibility for general multi-agent systems and show why it is not trivially implied by seed-compatibility. We then characterize the future-proof agents as the closure of the seed and show that this closure is monotone in the seed. Finally, we study a class of executable tests that involve interaction with the seed alone, and we ask to what extent such tests can distinguish the future-proof agents.

### 29. RobotAgentBench: Towards Open-world Robot Autonomy
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-26T00:26:30+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.34649
- Summary: Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm for this transition, integrating task discovery, contextual reasoning, physical execution, and adaptive recovery into a closed interaction loop. However, existing benchmarks largely evaluate isolated capabilities, failing to capture the complexity of open-world robot autonomy. We introduce RobotAgentBench (RAB), a comprehensive benchmark for evaluating robot agents in realistic, open-world household environments. Through an agent-assisted, human-in-the-loop real-to-sim pipeline, RAB constructs 50 diverse household layouts with interactive objects and physically grounded tasks, encompassing 90 atomic tasks, 18 short-horizon tasks, 8 long-horizon tasks, and 4 open-ended scenarios. RAB provides a multi-level evaluation of robot agent capabilities: (1) task-level assessments systematically examine five complementary dimensions: task discovery, context reasoning, manipulation, failure recovery, and robustness; (2) scenario-level evaluation assesses how agents integrate these capabilities to autonomously fulfill high-level user needs. Furthermore, RAB enables systematic comparisons of standalone VLA/WAM models and diverse robot agent architectures under a unified planning-execution-verification framework. Extensive experiments reveal substantial gaps between manipulation and autonomy, demonstrate the advantages of agentic architectures and recursive self-improvement, and highlight the remaining challenges toward open-world robot autonomy.

### 30. Strategic Calibration in LLM Multi-Agent Systems: Audited Pivot Scoring for Truthful Elicitation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-24T15:18:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.33728
- Summary: In large language model (LLM)-based multi-agent systems, reported confidence increasingly determines the allocation of scarce downstream attention, computation, and decision influence. This makes reporting strategic: an agent may overstate the relevance of its contribution even when its underlying belief is well calibrated. Existing calibration methods largely assume passive reporting and therefore do not address strategic incentives created when confidence determines downstream allocation. We formulate strategic calibration as a reporting-layer incentive problem and propose the Audited Pivot Scoring Mechanism (APSM). APSM offsets platform-controlled allocation benefits, uses inverse-propensity-weighted sparse audits, charges the Clarke pivot externality, and applies a strictly proper score. Under the stated model assumptions, truthful reporting is the unique expected-utility best response. We also characterize approximate execution and the audit-variance trade-off. Calculator-free experiments show that LLM agents inflate confidence under Top-$K$ incentives. With a shared agent-local utility interface, LLM agents reduce distortion under both Compensated Proper Scoring (CPS) and APSM. CPS achieves higher exact allocation match, whereas APSM yields lower Brier loss and numerically fewer cutoff crossings. Experiments further show that APSM enlarges the utility margin against allocation-changing deviations by $1.93\times$ and improves robustness under approximate execution. These results support incentive-aware elicitation as a distinct layer for reliable multi-agent coordination.
