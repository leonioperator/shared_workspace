# Blindspot Signals Report - 2026-10-20

- Source export: `/opt/apps/haier/exports/evolution_signals_20261020_020413.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 601
- Deduped/weighted signal clusters: 559
- Novel vs previous reports: 44
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. Refuse the Harm, Complete the Task via Graph-of-Rules Planning for LLM-Enabled Robots
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-17T10:13:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.24603
- Summary: Large Language Models (LLMs) are increasingly used in embodied AI for robotic manipulation and planning, but their deployment in physical systems exposes vulnerabilities such as jailbreak attacks that induce unsafe behavior. Existing inference-time defenses are mainly evaluated on short instructions containing a single hazard, whereas realistic tasks may interleave safe and unsafe sub-tasks, conceal hazardous steps, or combine individually safe actions into unsafe outcomes. Such compound instructions make it harder for a single safety decision to distinguish hazardous sub-tasks from legitimate ones, risking either overlooking the hazard or rejecting the whole instruction. We introduce safe task completion, a task that requires an LLM-enabled robot to refuse the harmful part of an instruction while completing its legitimate part. To address this problem, we propose RuleGraph, a multi-agent Graph-of-Rules planning framework that distributes safety enforcement across multiple reasoning and verification stages. Five cooperating agents are used to ground general safety principles into world-specific rules, assess the instruction's sub-tasks in context, and derive a safe goal from the legitimate ones. Planning toward this goal is then organized as a graph of rule-specific nodes, where higher-level nodes inherit the union of their parents' rules, and candidate plans are progressively verified and aggregated until a single plan satisfies every relevant rule. In this way, RuleGraph reduces reliance on a single centralized safety decision. We evaluate RuleGraph on pure-attack and compound instructions across two benchmarks in two environments using Attack Success Rate (ASR) and Task Success Rate (TSR). RuleGraph reduces ASR to 0% on both benchmarks while achieving the highest TSR among all methods, reaching 98.57% on the RoboGuard benchmark and 84.54% on our long-horizon compound instructions.

### 2. IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-17T02:36:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.24383
- Summary: Improving every agent in an LLM-based multi-agent system can be prohibitively costly, making it important to identify which agent should be prioritized to achieve the greatest system-level gain with limited resources. Failure attribution can inform this decision, but an agent's responsibility for failures does not directly reveal the system-level gains achievable by improving it. We therefore introduce IF-MAP, an influence-function-inspired method for identifying agents with high potential for system-level improvement. For each agent, IF-MAP measures end-to-end loss changes under controlled semantic prompt perturbations, fits a regularized local response model in a low-dimensional prompt-embedding subspace, and uses the estimated response norm as a priority score. This black-box procedure requires no access to model parameters or gradients and produces agent priorities that can guide subsequent improvement effort. We evaluate IF-MAP across six multi-agent workflows spanning code generation, question answering, and mathematical reasoning, using the same priorities for prompt optimization and model upgrades. Optimizing the selected agents' prompts achieves a macro-average gain of 3.81 percentage points, compared with 1.85 for uniform agent selection. Across five target models, upgrading the selected agents yields macro-average gains of 7.62-16.42 percentage points, compared with 3.81-8.62 for uniform agent selection. Despite its probing overhead, IF-MAP reduces Qwen3-8B and DeepSeek-V3.2 token use by 74.2% and 35.2%, respectively, relative to optimizing every agent, and reduces target-model tokens by 63.6-64.9% relative to upgrading every agent. These results support the use of IF-MAP to identify promising agents and direct improvement effort toward greater end-to-end performance gains.

### 3. From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-16T11:23:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.23319
  - Alt: https://arxiv.org/abs/2610.18792
- Summary: Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences. As a result, memory has become a fundamental component for enabling embodied agents to perform long-horizon reasoning and adaptive decision-making. This survey presents a systematic taxonomy of VLA memory mechanisms based on memory scope and persistence, categorizing existing approaches into five representative paradigms and one emerging frontier. Based on this taxonomy, we compare representative VLA memory systems in terms of memory characteristics, architectural com-plexity, and open-source maturity, revealing a clear trade-off in which increasing architectural complexity is generally accompanied by decreasing open-source ma-turity. Finally, we discuss the key challenges in building full-lifecycle memory systems, including efficient memory management and lifelong knowledge evolu-tion. Overall, this survey provides a unified perspective on memory architectures for VLA agents and offers insights into the development of lifelong embodied in-telligence.

### 4. SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-16T05:29:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.22959
- Summary: Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions. However, information collected from external sources can introduce security risks when untrusted claims (i.e., atomic statements) are later treated as authorized preferences, policies, or permissions. Existing defenses typically rely on content-based filtering or coarse-grained provenance tracking, which either fail to prevent unauthorized memory use or block legitimate information, sacrificing memory utility. To address these limitations, we propose SAFE-Mem, a fine-grained memory governance framework that improves security while preserving legitimate memory use. First, SAFE-Mem annotates each claim with three governance labels (i.e., kind, authority, and scope) to capture its provenance and permitted use. Second, governance-aware retrieval matches query requirements with claim permissions to block unauthorized influence while retaining legitimate information. Third, a governance-enabled memory graph connects source sentences, claims, and entities to support provenance tracking and efficient retrieval. Across four LLM backbones on MPBench and LoCoMo, SAFE-Mem attains the lowest attack success among defenses that retain legitimate memory, at least 77% below the strongest of them, and the highest answer accuracy of all evaluated defenses, improving it by up to 15%. The code is available at https://github.com/LVenum/SAFE-Mem.

### 5. Competence-Aware Orchestration for LLM-Based Multi-Agent Systems
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

### 6. Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T04:34:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.01042
  - Alt: https://arxiv.org/abs/2610.18780
  - Alt: https://arxiv.org/abs/2610.23078
  - Alt: https://arxiv.org/abs/2609.39788
- Summary: Multi-agent communication aims to help agents benefit from one another's information. Yet improvements in system performance leave a fundamental ambiguity: do they reflect effective communication, a favorable agent architecture, or simply additional reasoning? Because communication methods are commonly evaluated within the systems they were designed for, these factors are difficult to disentangle. Final accuracy further merges corrected errors and corrupted answers into a single outcome, obscuring how communication changes decisions. We introduce Independent--Communicate--Revise (ICR), a controlled framework that evaluates communication as answer revision following independent reasoning. ICR fixes initial reasoning trajectories, measures correction and preservation conditional on both agents' initial correctness, and uses a no-message revision control to quantify gains beyond additional reasoning. Across four reasoning benchmarks, our audit of textual and latent communication reveals that similar aggregate accuracy can conceal substantially different revision behaviors. Compared with transmitting answers alone, full reasoning increases correction while reducing preservation on all four benchmarks, so richer messages amplify beneficial and harmful influence alike. Receiver-policy comparisons on MedQA and GPQA-D further show that a structured verification policy shifts every channel toward greater preservation and lower correction, while its effect on selectivity varies across channels and tasks. These findings challenge treating communication quality as an intrinsic property of a channel. ICR therefore recenters evaluation on selective revision, providing a unified framework for examining how message content and receiver policies jointly produce benefits and harms.

### 7. PigGPA: A Domain-Constrained Agent for Porcine Genomic Breeding with Verifiable Tool Execution
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-19T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.18.759908
- Summary: Large language model agents can plan and execute scientific analyses, but successful task completion does not establish whether analytical decisions remain consistent across independent sessions or whether computations follow the parameters specified beforehand. We investigated these limitations using four genomic analysis tasks. General-purpose agents showed limited consistency in analytical decisions across repeated sessions (57.5-58.8%). Incorporating domain knowledge improved analytical performance, with reusable skills increasing mean evaluation scores from 73.44 to 89.06/100 , but did not resolve decision variability or ensure agreement between specified and executed parameters. To address these limitations, we developed an approach combining domain-constrained analytical skills with call-level execution contracts. Each tool invocation is linked to a pre-execution parameter declaration through SHA-256 hashing, with actual command-line arguments and execution records subsequently checked against the declared parameters. We implemented this approach in PigGPA, an autonomous agent for porcine genomic breeding that integrates statistical genetics, sequence-based functional prediction and multi-omics annotation. PigGPA completed all benchmark tasks with full agreement between declared and executed parameters, while its core quantitative-genetic results closely matched established software (r = 0.999-1.000). An application to loin muscle depth further demonstrated an integrated workflow from genetic association analysis to functional interpretation. These findings show that domain knowledge improves analytical performance, while direct verification of tool execution provides an additional basis for reproducible scientific computation.

### 8. RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-16T15:16:50+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.23598
- Summary: Time-aware retrieval is crucial for long-horizon LLM agents to effectively leverage ever-growing long-term memory. Existing methods focus on lexical or semantic similarity, leading to target memories being crowded out by temporally mismatched yet semantically similar candidates. Even time-aware approaches inject temporal cues only during memory organization or answer generation, overlooking temporal constraints at the retrieval stage, where candidate selection occurs - the root cause of the displacement. Inspired by the temporal contiguity effect in human episodic memory, we propose TIDER (Temporal Interval-driven Dual-channel Evidence Retrieval), a time-aware agentic retrieval framework. Central to TIDER is a reinforcement learning (RL)-trained temporal interval locator that infers the temporal windows in which the evidence lies. RL optimizes window localization as a discrete, non-differentiable retrieval decision, using composite rewards to convert sparse answer supervision into fine-grained retrieval feedback. These temporal windows first define the temporal retrieval channel; the retrieved candidates are then merged with results from the semantic channel and reranked by proximity to the windows. This temporal grounding enables TIDER to retrieve temporally aligned evidence that would otherwise be drowned out by the volume of semantically similar yet temporally mismatched memories. With a lightweight 1.7B locator, TIDER achieves state-of-the-art accuracy on both long-horizon memory benchmarks - 61.52% on LifeBench (+8.82%) and 78.96% on LoCoMo (+3.66%) - which indicates that temporal cues are crucial for pinpointing target evidence amid a vast pool of semantically similar historical events in long-term daily-life memory.

### 9. InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-16T08:10:51+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.23098
- Summary: Heterogeneous robot teams enable complex, long-horizon tasks by combining complementary sensing, mobility, and manipulation capabilities across multiple embodiments. Yet existing systems struggle to retain execution-time corrections as reusable experience, maintain task-relevant context memory across space and time for reliable handoffs, and explicitly represent the inter-robot dependencies required for structured collaboration. In order to address these challenges, we present InstAgent, a recursively self-improving (RSI) Agent Operating System for heterogeneous robot collaboration. InstAgent organizes team behaviors as agentic behavior trees (BTs) that explicitly model capability assignment, inter-robot dependencies and handoff checks. The RSI mechanism updates these collaboration programs from execution feedback and preserves successful revisions for reuse in future tasks, while shared multimodal spatio-temporal memory provides context for planning and handoff validation. Experiments on 20 real-world multi-robot tasks with three high-level models show consistent gains in task success, first-attempt completion, and execution efficiency.

### 10. Thought Blocks: Non-Autoregressive Latent Communication for Multi-Agent Systems via Trajectory-to-State Compilation
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-16T07:35:02+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.23056
- Summary: LLM-based multi-agent systems typically communicate through text, incurring repeated generation and re-encoding costs. Although latent communication removes explicit verbalization, constructing latent messages may still require autoregressive latent trajectories. We therefore distinguish message representation from message construction and ask whether agents can directly construct useful continuation states without executing the trajectories that normally produce them. We formulate this problem as trajectory-to-state compilation and introduce Thought Blocks, fixed-size blocks of latent key--value (KV) continuation memory constructed in one shot. Thought Blocks achieve a 2.5 times average latency speedup over autoregressive latent communication. Compared with text-based multi-agent communication, Thought Blocks reduce text tokens by 45.7% and autoregressive steps by 84.8%, achieving an 8.6 times average latency speedup. These results demonstrate that trajectory-to-state compilation enables efficient inter-agent latent communication without sequential latent rollouts at inference.

### 11. Emergent Discrimination and Polarization in Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-15T22:07:16+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.22701
- Summary: We study theoretically how discrimination and polarization can emerge in a population of learning agents. Each agent uses an adaptive linear decision layer to map a language-model embedding of an issue to a binary opinion and maintains an evolving estimate of how much it trusts every other agent. Through pairwise interactions, agents update both their decision weights and trust estimates using an online Bayesian rule derived from teacher-student learning over a noisy channel. In-context-learning experiments with large language models qualitatively reproduce the predicted opinion and trust updates. We then assign each agent one of two arbitrary group labels, A or B, and model group bias by allowing a fraction $f_b$ of agents to shift its perceived agreement with each message by a strength $b$, a bias steering prejudice, depending on whether the sender and receiver share a label. We use order parameters from statistical mechanics to connect these local dynamics to collective states and transitions. Starting from uniformly random initial conditions, simulations reveal a rich phase diagram in the $(b,f_b)$ plane, comprising four collective states: spin-glass frustrated out-group favoritism, nondiscriminatory polarization, discrimination with opinion alignment, and discrimination without opinion alignment. Which state emerges depends on both the strength and prevalence of the bias. These results show how simple local learning dynamics can generate qualitatively distinct forms of polarization and discrimination, underscoring the need for population-level safety analysis of multi-agent systems. They also suggest measurable order parameters for characterizing analogous collective states in human societies.

### 12. The Model Knows Better: Defending Medical Multi-Agent Systems Against Prompt Injection
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-15T19:43:57+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.22594
- Summary: Medical multi-agent systems, in which LLM agents discuss a case, are increasingly studied for clinical decision support. Prompt injection, text that an attacker adds to a model's input, can manipulate LLMs into wrong decisions. How it affects these systems, and how to protect them, remains unclear. Across two systems, two model families and three benchmarks, a single injected passage succeeds in up to 61% of cases, and collaboration does not consistently protect against it. Existing defenses help only partly: they miss injections that look like ordinary clinical text. Yet when asked to check the injected text against the patient's findings, a model that followed the injection usually rejects it. We therefore propose a training-free defense that verifies the clinical judgments behind the system's decision. Following clinical practice, it separates the patient's findings from clinical judgments, such as diagnoses, recommendations and instructions, and checks each judgment against the findings alone, so the decision rests only on supported judgments. Our defense outperforms all baselines on every benchmark, lowering attack success on MedQA to 4-7% while maintaining accuracy on cases without an attack, and remains effective with a medical model and against defense-aware and adaptive attacks.

### 13. Agent Status Protocol (ASP): A Lightweight Specification for State Reporting in Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-15T09:03:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.21538
- Summary: The Agent Status Protocol (ASP) defines a lightweight way for heterogeneous AI agents to report their operational state to a status server, and for observers such as dashboards to receive that state as soon as it changes. Agents push small JSON events over HTTP POST; the server exposes the aggregated state to observers over Server-Sent Events (SSE). Because an agent that has crashed, hung or been compromised cannot be trusted to report its own failure, ASP does not rely on self-reports alone: the server infers liveness from missed heartbeats, can detect agents that are alive but no longer making progress, and accepts observations from supervisors, guardrails, operators and peers, some of which take precedence over what the agent says about itself while others are shown alongside it. ASP models state along independent dimensions (lifecycle, health, task, floor, governance), so that an agent can be, for example, online, degraded, working on a task and waiting for the floor at the same time. It reuses existing vocabularies: task states from the Agent2Agent (A2A) protocol, floor states from the Open Floor Protocol (OFP), and attribute conventions from the OpenTelemetry GenAI semantic conventions. This paper presents version 0.1 of ASP as a proposal, not as an approved standard. It is a working draft intended to open a discussion, and the authors invite comments, alternative proposals and independent implementations from the community.

### 14. How a Lone Hacker Used Autonomous AI Agents and a Few Thousand Dollars to Breach Dozens of Enterprise Systems - OODA Loop
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-19T15:51:12+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMi4wFBVV95cUxQNmNETm1FMlJ4WVJPN0tseHlYT2t5N2VURTZ3TWx6c1E5S1RaZ2Y1WjNWcS1MS2FXMjBoV0NXS2tZc3JuRVdtcGNzWU55QXhQNWlxWURpOTB2X3I2UnRkUTlmLWNiamp2V3R3aHpKcklYRW9Bb0ZpeVh3Wlpzc3V6d2dMWUJuUmlkeTVsMldNbHN0eXdhckJMd25jTER3Y3JYaGJvd2VZUERuek45blFvd2h1OFN1UG83aUhOTjVUckMtSV95VmxLMzhjcE1LcVJybGJFdEpEcnV3QUFndzlwVEtqOA?oc=5
  - Alt: https://news.google.com/rss/articles/CBMivwFBVV95cUxQOUxsTUtmNmVodHV1NkNtVWRUeWIxOTBPdHlRZlowTUotY3RtX0tqclVIOVc5MVktMDlWNXphX0Zma19tQ3lURXVQMlVCeThZN1NFMldoanIxekpyc1lZZWh2SW1FbmVmazBIWkp3RWFsdUQ4ckZjanNHQ291RldJRjM3aG9RLW1teXBHdGtFNVc4akdVY1JqZlgxbGdoSHBmNUVHdHZ2VlNzcFFQNTBoa0ZZaWMtZ0twWjM2b29xcw?oc=5
- Summary: How a Lone Hacker Used Autonomous AI Agents and a Few Thousand Dollars to Breach Dozens of Enterprise Systems&nbsp;&nbsp;OODA Loop

### 15. MASIF: Implicit Failures for Process Observability in Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-19T06:07:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.25852
- Summary: Multi-agent systems (MAS) can complete a task despite local execution errors that are corrected, bypassed, or carried forward without individually determining its outcome. We call these implicit failures (IFs) and study them as signals for process observability beyond final task outcome. Across 1,828 traces from nine MAS-benchmark configurations, IFs occur in 54.3% of successful and 75.2% of failed traces. We develop taxonomies of error types and subsequent absorption mechanisms, supported by human and cross-model annotation audits. Counterfactual replay further probes how repairing an IF changes the final outcome. To examine the practical value of IFs, we evaluate IF-based best-of-N trace selection against existing process reward models, and introduce a novel RL algorithm, IF-GRPO, that uses IF costs to refine preferences among successful trajectories in GRPO. Experiments show that IF-GRPO exhibits some gains in accuracy and process metrics. Importantly, it exposes trade-offs between task performance, IF count and cost, and token-normalized IF density. Overall, our results show that IFs provide complementary process observability into how MAS reach their outcomes, including error recovery, propagation, and IF-based process differences that final task success alone does not expose.

### 16. The accessible human surfaceome
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-19T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.18.759859
- Summary: Proteins associated with the extracellular face of the plasma membrane ("surface proteins" or the "surfaceome") are important therapeutic targets because they can direct therapeutics to specific cell types and deliver them into cells. However, experimental and computational databases disagree substantially on which proteins make up the human plasma membrane proteome, and none focus specifically on the set of accessible surface proteins that would be useful for therapeutic applications. Here, we used an agentic LLM pipeline to curate the accessible human surfaceome from literature. To assess performance, we built SurfaceBench, a manually curated benchmark of 147 proteins on which five reference databases frequently disagree. Our LLM triage agent classified surface status more accurately than existing databases and recovered 1,108 candidate surface proteins not present in any of them. On held-out clinical and viral-entry surface targets, the pipeline recovered 98-100% of established surface antigens. A literature-anchored deep-dive pipeline run on over 5,000 candidates then returned 1,783 canonical surface proteins and 1,252 with weaker or context-dependent surface evidence. Each queryable record contains 24 LLM-based annotation fields--including confidence, primary localization, and expression breadth--and seven deterministic structural and topological features. Unlike existing databases, our records trace every claim to the agent's reasoning and to exact quotes from the full-text literature it could access. All records can be browsed in an open-source viewer. These results show that LLMs reasoning over unstructured scientific text can build updatable, bespoke databases that outperform expert-curated resources, although performance remains limited by agent access to full-text literature.

### 17. MemDerive: A Diagnostic Benchmark for Agent Memory over Evolving Data
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-18T16:24:33+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.25373
- Summary: Long-running agents rely on memory of their past interactions for task state, such as what has been completed and which conditions still hold. Such state is usually a derived state. No record states it, and it must be computed by rules from multiple records of an evolving history. Existing memory benchmarks score only the final answer, with no reference for the intermediate states behind it. A wrong answer therefore cannot be traced to the state that was missed, and a state that silently became outdated goes undetected. We present MemDerive, a diagnostic benchmark for agent memory over evolving data. It specifies each scenario symbolically, derives exact gold answers with Datalog, records the gold derivation DAG and the supporting events of every query, and renders the history in natural language with fictional entities and distractors. Its 10 scenarios contain 4,692 events and 1,503 queries whose difficulty varies along access, evolution, and composition. On this ground truth, MemDerive evaluates answer reliability, diagnoses failures by probing the nodes of the gold derivation DAG, and tracks whether answers stay correct as events arrive. Our evaluation of four memory systems reveals failures that final-answer benchmarks hide. On derived state, every memory system falls behind simple BM25 retrieval, although the same answer model reaches 96.01% when given the supporting events. Most failures are ungathered, as a system holds the missing intermediate state but does not retrieve it for the question that needs it. Memory systems also rarely propagate implicit changes, which no new record states. These results suggest three principles for memory design. Gather inputs along the derivation, store rules with their versions, and maintain derived states through recorded dependencies.

### 18. MemBubble: Benchmarking How Agent Memory Shapes LLM Response Diversity
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-18T09:17:44+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.25127
- Summary: Memory serves as the core component of LLM-based agents, enabling personalized responses via extracting and using user preferences from past interactions. However, its use may reduce response diversity, thereby narrowing the range of information available to users. Existing evaluations rely largely on synthetic interactions and cover few memory systems, leaving the effects of memory on response diversity insufficiently evaluated in real-world scenarios. We introduce MemBubble, a benchmark of 1000 instances built on preferences extracted from real user-assistant conversations. To measure the extent to which memory concentrates response distributions, we construct test queries in scenarios distinct from user preferences while preserving topical relevance through shared preference categories. Across multiple LLMs and memory mechanisms, entropy decreases by 34.7% on average compared with directly providing the full interaction history, highlighting the important role of memory processing in diversity loss. We also explore simple user-side interventions and changes in information availability but find that these do not effectively close the diversity gap. Our findings highlight the need to consider preserving diversity and user access to information alongside improvements in personalization when designing and using agent memory systems.

### 19. AgentSoV: Virtual Sensing for LLM Multi-Agent Systems via Stream of Variation
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-17T19:48:14+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.24845
- Summary: Large language model (LLM) multi-agent systems (MASs) solve complex tasks through interacting agents, yet their reliability is difficult to analyze because failures depend on both individual agents and how information and errors propagate across the system. Existing approaches largely treat this as post-hoc failure attribution, but do not provide a common model across heterogeneous MAS architectures or support broader analysis of information influence and observability. We introduce AgentSoV, a virtual-sensing framework that models MAS execution as a stochastic dynamic system through Stream of Variation (SoV). AgentSoV maps heterogeneous trajectories into diagnostic stages, constructs virtual measurements from observable outputs, and learns cross-stage variation propagation with a state-space model. Its representation is architecture-aware in stage dependencies yet architecture-agnostic in analytical language, supporting chain-structured, orchestration-based, and directed acyclic graph (DAG)-structured MASs. Without re-executing the MAS, AgentSoV supports three system-level analyses: failure attribution identifies where abnormal variation enters; stage-input influence quantifies how strongly intermediate inputs affect downstream outcomes; and virtual-sensor placement selects complementary observations under a monitoring budget. Experiments across multiple MAS architectures demonstrate a unified approach to fault localization, information influence, and observability. AgentSoV reframes agentic execution as a dynamic system to model rather than merely text to inspect, providing insights for MAS structure and component design.

### 20. HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-17T07:30:09+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.24520
- Summary: In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions. These habits capture implicit user information that agents must infer across conversations. However, individual observations may provide only partial evidence about a habit or when it applies. Retaining past interactions alone does not ensure that agents can infer habits and apply them appropriately. We introduce HABIT-Bench to evaluate how well agent memory systems infer habits from weak evidence and apply them to later requests. We construct synthetic user histories from task-oriented dialogue data and controlled habit graphs. The histories span hundreds of sessions across food, finance, software, and travel. Four-choice tasks assess agents' ability to infer user habits and apply them appropriately. They include temporary exceptions, changes in habits, and suggestions that users have not accepted. Sampled tasks undergo independent human review. We evaluate eight memory methods with Qwen3-235B-A22B and GLM-5.3-Flash. The best-performing memory method achieves 33.61\% macro accuracy across the four domains. Performance remains limited even when annotated evidence is supplied directly. These results expose a persistent gap between access to past interactions and the ability to infer and appropriately use user habits.

### 21. GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-16T16:33:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.23709
- Summary: Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful strategies across diverse categories. However, existing approaches often treat structured listings as free-form text, leaving effective strategies implicit in prompts, search trajectories, or rewritten outputs rather than accumulating them as a reusable agentic memory. To address this limitation, we introduce GLOBE, an agentic framework that drives continual self-improvement by storing optimization knowledge in an evolving handbook of explicit, field-scoped behaviors. In each episode, an Editor applies relevant behaviors and receives rank-based feedback, which a Reflector converts into behavior updates. Crucially for dependable execution in real-world settings, a Moderator removes redundant proposals, a Curator commits accepted changes, and consistently harmful behaviors are deactivated. This cycle transforms episodic feedback into a persistent, field-scoped optimization memory. Experiments show that structured behaviors outperform monolithic prompt optimization, while feedback-driven evolution and moderation further improve effectiveness and reduce downside risk. The learned behaviors also remain effective on unseen product categories, suggesting that agentic memory evolution supports interpretable and transferable product optimization.

### 22. From Memory Hits to Answerable Evidence: Query-Conditioned Memory Compilation for Long-Term Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-16T11:15:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.23313
- Summary: Long-term agent memory requires recovering answer-relevant evidence dispersed across turns and sessions. Existing systems increasingly use structured memories and adaptive retrieval, yet often pass retrieved or expanded units directly to the reader, coupling memory addressing with evidence presentation and leaving the final context redundant or incomplete. To address this gap, we propose MemCompile, a query-conditioned evidence compilation framework for long-term conversational memory. Given a query, the Address Plane locates relevant support through compact source-linked descriptors and capacity-aware Cells, while a normalization boundary resolves heterogeneous retrieval hits to stable SourcePacket identities. Its Evidence Plane then allocates a bounded evidence budget across complementary packets, admits limited additional support, and renders the retained claims associated with each selected packet into an answer-ready context. MemCompile achieves 80.52% Judge Accuracy on LoCoMo and extends the empirical quality-cost Pareto frontier to a higher-quality regime. Its strong performance on LongMemEval-S further suggests that the benefits of query-conditioned compilation generalize across long-term conversational-memory benchmarks.

### 23. QuAD: Quantitative Assessment via Distribution-Alignment for Qualitative Data Quality Enabled by a Content-Aware Multi-Agent System
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-16T08:46:00+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.23153
- Summary: Assessing whether qualitative responses collected from semi-structured questions are ready for a particular analysis goal is a persistent challenge. Manual qualitative analysis is interpretive and labor-intensive, while existing automated methods often lack a dataset-level perspective for deciding whether a response set supports a researcher-selected analytical lens. We introduce QuAD, a framework for quantitative pre-analysis assessment of qualitative response datasets. QuAD compares a reconstructed intrinsic cluster distribution reconstructed from responses with an extrinsic, researcher-defined analytical lens derived from metadata. QuAD is structured into a four-quadrant assessment whose metrics are read jointly, from lens-level relations to within-cluster variation, to provide fitness-for-purpose signals for revealing general patterns and unique insights. Because this assessment relies on lens-conditioned inter-response dissimilarity, we propose a content-aware multi-agent system with two-stage instruction generation and adaptive anchors to improve scoring consistency. We validate QuAD through controlled experiments on synthetic data, including robustness and baseline comparisons, and a real-world social survey case study. The case study shows how QuAD quantitatively assesses whether a selected analysis axis is promising and also surfaces representative or unusual responses for human interpretation.

### 24. Learning Rational Strategies for Temporal Objectives in Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-15T17:42:52+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.22287
- Summary: We study rational synthesis for stochastic multi-agent systems with unknown dynamics, where each agent is equipped with its own probabilistic temporal objective specified using Probabilistic Linear Temporal Logic on Finite Traces ($\mathsf{PLTL}_f}$). We impose solution concepts (e.g., Nash equilibrium, subgame-perfect equilibrium) as constraints on the joint strategy profile, using payoffs derived from each agent's probability of satisfying its temporal objective. In particular, we formulate per-agent rational synthesis as finding a strategy profile -- if one exists -- such that (i) the designated agent's probabilistic temporal constraint is satisfied, and (ii) the profile represents a stable solution under a chosen solution concept. We give conditional convergence guarantees for tabular Nash-Q learning, certify satisfaction with simultaneous finite-sample confidence bounds, and assess strategic stability with approximate best-response checking. Our approach operates in a stochastic \emph{Multi-Agent Reinforcement Learning} (MARL) environment, where model-free learning algorithms attempt to attain extremal satisfaction probabilities for temporal objectives automatically compiled into reward automata. Our approach is empirically validated using 8 general-sum concurrent stochastic games.

### 25. Beyond Downstream QA: Rethinking How We Evaluate Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-15T16:58:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.22209
- Summary: Agent memory benchmarks evaluate whether an agent's responses reflect correct knowledge, measuring downstream question-answering accuracy as a proxy for memory quality. We show this evaluation paradigm is incomplete: it conflates memory correctness with retrieval and generation quality, producing both false positives where correct responses mask broken memory and false negatives where incorrect responses blame correct memory for retrieval failures. We introduce FEB-30, a benchmark of 30 fact-evolution trajectories spanning 6 diagnostic categories and 3 difficulty levels, constructed via paradigm inversion: documents are generated from known fact trajectories, yielding deterministic ground truth without human annotation. Each trajectory defines how a fact should evolve across multi-author artifacts (documents, emails, conversations), enabling direct inspection of the memory store after each ingestion step. Applying FEB-30 to a representative memory system, we demonstrate that intrinsic and extrinsic evaluation diverge by an average of 16 percentage points, with 44% of trajectories exceeding meaningful divergence thresholds. Diagnostic decomposition reveals that the system correctly classifies memory operations (create, update, reinforce, supersede) only 20% of the time, a failure entirely invisible to extrinsic evaluation, and that failure modes differ systematically by category and difficulty. We release the benchmark, document generation pipeline, and scoring framework to support reproducible evaluation of agent memory systems.

### 26. PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-15T07:06:10+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.21390
- Summary: Multi-agent large language model (LLM) systems are increasingly deployed at the edge to support complex tasks that require collaboration and information exchange among multiple agents. However, when task contexts are passed across agents, shared context that has already been processed by upstream agents often needs to be prefilled again, resulting in substantial redundant computation. Reusing an already prefilled key--value (KV) cache can avoid this recomputation, but requires the reusable KV state to be transferred across the network before the receiving agent can begin generation. Under strict time-to-first-token (TTFT) deadlines and unreliable edge links, delivering the complete KV cache may be infeasible, making it necessary to prioritize and protect the most valuable KV information within a limited transmission budget. This paper proposes PriorityFEC, a utility-aware KV-cache handoff scheme that jointly exploits model-side KV importance and transport-side reliability. PriorityFEC first constructs a utility-aware source stream by placing high-utility KV blocks at earlier transmission positions. It then protects the ordered stream using a feedback-adaptive Streaming Forward Erasure Correction (FEC) mechanism, which schedules repair packets according to receiver feedback before the TTFT deadline. We implement PriorityFEC on a distributed edge LLM serving prototype and evaluate it with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct across multiple datasets. Results show that PriorityFEC achieves superior task quality over the compared transport schemes, with its advantages becoming particularly pronounced under stringent deadline constraints. These results demonstrate the importance of jointly optimizing KV-cache utility and deadline-aware transport reliability when reusable LLM state must be handed off across unreliable edge networks.

### 27. Communication-aware Synthesis of Safe Controllers for Discrete-Time Linear Multi-Agent Systems with Distributed k-Hop Observation
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-01T01:58:36+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.00925
- Summary: This paper studies communication-aware safe control for discrete-time linear multi-agent systems under limited information exchange. The main challenge lies in the coupling between remote-state estimation and safe controller design, since estimation errors affect the state evolution through the controller gains, while the controller design must account for the resulting observer-induced state perturbations to guarantee safety. To address this challenge, a distributed k-hop observer is developed to reconstruct unavailable remote states, and a uniform observer-error bound is derived. The effect of the observer-induced state perturbation on closed-loop safety is accounted for in both the construction of local εi-robust safe invariant (RSI) sets and the enforcement of pairwise relative-state safety constraints. The resulting safety conditions ensure that all agents remain within their local RSI sets while all pairwise relative-state safety constraints are satisfied. A linear matrix inequality (LMI)-based optimization method is developed to jointly synthesize the distributed observers, local controllers, and RSI sets. A case study illustrates the effectiveness of the proposed method.

### 28. Bearing-Only Formation Tracking Control for Euler-Lagrange Multi-Agent Systems Without Inter-Agent Communication
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-24T05:31:10+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.29049
- Summary: This paper investigates communication-free bearing-only formation tracking control for multi-agent systems governed by Euler-Lagrange dynamics. Distinct from existing results that can only stabilize a stationary formation, this work considers a scenario where the leaders move with time-varying velocities while the inter-agent communication is absent. In this setup, the leaders' states (position and velocity) are unavailable to all followers and cannot be estimated via distributed observers. A novel adaptive distributed control scheme is developed to address this problem. The design exploits the fact that bearing rates contain the projected relative-velocity information, which, together with bearing rigidity, provides a rigidity-based damping mechanism for compensating the unavailable velocity error. Moreover, this damping mechanism is incorporated into a bearing-driven auxiliary variable to construct a surrogate velocity error, facilitating the adaptive control design for EL dynamics. Furthermore, since this damping mechanism necessitates sufficient bearing rigidity, we characterize a rigidity-preserving set and establish its forward invariance, thereby guaranteeing such rigidity via initial conditions. Via a Filippov-based Lyapunov analysis, the proposed scheme is shown to achieve local practical formation tracking in the sense that the velocity error converges to zero and the position error is uniformly ultimately bounded. As a corollary, for the constant-velocity case, asymptotic tracking is achieved without initial-condition restriction. The simulation results verify the effectiveness of the proposed control law.

### 29. Microsoft says AI agents are like insider threats as ‘frontier models can’t be trusted’
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-19T22:04:28+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/
- Summary: Microsoft wants enterprises to closely watch the agents that employees use with systems not controlled by AI labs like OpenAI and Anthropic.

### 30. EXCLUSIVE: How one hacker used AI agents and a few thousand dollars to break into scores of sites - Reuters
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-19T21:30:28+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMixgFBVV95cUxQSUVKUWRvY0tQeUZscHhGcDBLYjI5VVZaYXRFRklFbmEzX29RaVFuMmt6cDlpMURENUtWRFpBQVBnNngwcWJla3NJZllZVDFBb2NKU21YUnBkMTNKb1NEM3BNLXk2OXpVbVpyZXM3NHVaOUNrWGZzRWhGQlRFSDhPa0E4TVdCTnBuZjNBS2R2UU9ySzV1c2hCbUVycmFHUTNpVk1vX0kxSEEyMUllRlpsakRfNEdZUlJUWVBVRTFqYkZiYm5jR1E?oc=5
- Summary: EXCLUSIVE: How one hacker used AI agents and a few thousand dollars to break into scores of sites&nbsp;&nbsp;Reuters

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

### 3. TRACEDD: A Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-09-18T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.09.12.751167
- Summary: Drug discovery depends on coordinated decisions across target validation, structure analysis, molecular design, developability assessment and synthetic feasibility, but current computational methods often operate as disconnected tools. Here, we introduce TRACEDD (Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design), a framework that makes three primary contributions: (1) It establishes a 'tool-first' multi agentic architecture where LLMs orchestrate validated computational tools rather than replace them, ensuring scientific rigor. (2) It implements a multi-agent system that mirrors expert discovery teams, enabling transparent and traceable decision-making through a Reason-Act-Observe loop. (3) It demonstrates an end-to-end workflow, from target validation to synthesis planning, that adaptively handles real-world data variability, such as the absence of experimental structures. The framework decomposes discovery into specialized agents for target validation, druggability assessment, molecular generation, lead optimization, ADMET evaluation, literature evidence integration and retrosynthesis, all operating through a Reason Act Observe workflow. Using JAK2 as a representative case, we show that the system can retrieve experimental protein structures, invoke AlphaFold when structures are unavailable, identify druggable pockets and perform de novo molecular generation. Known JAK2 inhibitors are used to define design hypotheses and guide reinforcement learning-based molecular generation, with docking scores/predicted pIC50 and other physicochemical/ADMET properties serving as reward and prioritization signals. The framework demonstrates a tool-first, reasoning-driven approach in which each major decision is linked to explicit tool invocation, intermediate evidence. By combining agentic orchestration with domain-specific computational tools, the system supports transparent, adaptable and human-verifiable molecular design workflows, providing a …

### 4. Refuse the Harm, Complete the Task via Graph-of-Rules Planning for LLM-Enabled Robots
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-17T10:13:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.24603
- Summary: Large Language Models (LLMs) are increasingly used in embodied AI for robotic manipulation and planning, but their deployment in physical systems exposes vulnerabilities such as jailbreak attacks that induce unsafe behavior. Existing inference-time defenses are mainly evaluated on short instructions containing a single hazard, whereas realistic tasks may interleave safe and unsafe sub-tasks, conceal hazardous steps, or combine individually safe actions into unsafe outcomes. Such compound instructions make it harder for a single safety decision to distinguish hazardous sub-tasks from legitimate ones, risking either overlooking the hazard or rejecting the whole instruction. We introduce safe task completion, a task that requires an LLM-enabled robot to refuse the harmful part of an instruction while completing its legitimate part. To address this problem, we propose RuleGraph, a multi-agent Graph-of-Rules planning framework that distributes safety enforcement across multiple reasoning and verification stages. Five cooperating agents are used to ground general safety principles into world-specific rules, assess the instruction's sub-tasks in context, and derive a safe goal from the legitimate ones. Planning toward this goal is then organized as a graph of rule-specific nodes, where higher-level nodes inherit the union of their parents' rules, and candidate plans are progressively verified and aggregated until a single plan satisfies every relevant rule. In this way, RuleGraph reduces reliance on a single centralized safety decision. We evaluate RuleGraph on pure-attack and compound instructions across two benchmarks in two environments using Attack Success Rate (ASR) and Task Success Rate (TSR). RuleGraph reduces ASR to 0% on both benchmarks while achieving the highest TSR among all methods, reaching 98.57% on the RoboGuard benchmark and 84.54% on our long-horizon compound instructions.

### 5. ChunkAct: Action Chunking for Agentic Robotics
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-13T17:59:57+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.18874
- Summary: Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.

### 6. Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark, and Method
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-07T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents, robotics / AI agents
- URL: https://huggingface.co/papers/2609.35965
- Summary: Vision-and-Language Navigation (VLN) has largely focused on a single agent following a single instruction, yet many real-world applications require teams of robots to tackle tasks beyond the capabilities of any individual agent. We present Systematic Multi-Agent Vision-and-Language Navigation, providing, to our knowledge, the first systematic formalization of multi-agent VLN as a constrained coordination problem: each mission consists of subtasks carrying dependency and resource constraints (presence locks and holding chains). A verified four-stage crafting pipeline instantiates the task as MAVLN, comprising 11,724 episodes across 145 scenes with teams of up to four agents under three instruction regimes, accompanied by tailored constraint-aware metrics. We further present TRISS, a coordination-ready navigation system coupling an LLM-based subtask scheduler, a shared topological memory that turns each agent's exploration into team knowledge, and a conflict-aware execution mechanism that realizes simultaneous intentions as collision-free routes. Extensive experiments establish TRISS as a comprehensive baseline and reveal substantial room for improvement across scheduling, planning, and execution, highlighting the challenges of coordinating under MAVLN task constraints. Project page: https://xyz9911.github.io/mavln.

### 7. PrivMeSA: Privacy-Aware Self-Evolving Multi-Agent System for Medicine via Local-Remote LLM Collaboration
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-29T19:47:38+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38458
  - Alt: https://arxiv.org/abs/2609.37953
  - Alt: https://arxiv.org/abs/2609.19680
- Summary: Clinical large language model (LLM) agents deployed locally can consult more capable remote models, but doing so risks exposing patient information. Privacy-conscious delegation places disclosure decisions with a local agent, yet removing explicit identifiers is insufficient: quasi-identifiers can accumulate across multi-turn consultations and repeated patient visits to enable re-identification. We introduce PrivMeSA, a privacy-aware self-evolving multi-agent system that learns to control disclosure and retains remote expertise for local reuse. A local agent manages each encounter and consults remote specialists that may request additional information. Reinforcement learning balances task accuracy against direct disclosure and registry-based re-identification risk, with privacy evaluated over the complete outbound transcript of each encounter. A local lesson memory distills completed consultations into generalized clinical guidance and retrieves relevant lessons before transmission, allowing subsequent cases to reuse expertise without another remote exchange. Memory grows without additional outcome labels or parameter updates. On an emergency-department benchmark built from MIMIC-IV-ED records, PrivMeSA improves mean task accuracy over delegation by up to 15.8 percentage points. In the same setting, PrivMeSA reduces the disclosure of personal details from 98.0% to 0.2% of cases and the share of cases in which the patient can be narrowed to ten or fewer registry patients from 74% to 0%.

### 8. World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T15:19:39+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.29964
- Summary: General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected automatically from the scene geometry, present the scene around the current interaction. Action rehearsal turns each action into an editable proposal that the agent, alone or through an Imagination Agent, previews and revises against planning feedback before execution. In-view correction closes the loop between observation, rehearsal, and low-level execution, letting the agent remove residual offsets in the view where it observes them. Through the same workspace, WAA acquires embodied procedural knowledge in two ways: it evolves multimodal skills from expert videos and human teaching under evidence-based review and consults them through a Skill Agent, and its interaction traces train smaller VLMs to pilot the same harness. On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art 75.6% average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone; the same skills remain effective on robosuite without further learning. Fine-tuning Qwen3.5-9B on harness traces raises its out-of-domain success from 1.7% to 43.3%.

### 9. RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T11:22:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.29394
- Summary: General-purpose robot agents must learn from experience, transfer to new tasks, and act efficiently. Code as Policies (CaP) methods generate and repair programs at runtime, incurring latency and entangling reusable mechanisms with task-specific decisions. We introduce RACaP, an agentic framework that moves coding to evolution and uses a Reasoning-and-Acting (ReAct) loop to call frozen, typed Policy APIs at deployment. A two-phase strategy combines capability curriculum learning with autonomous self-evolution to improve the APIs, the ReAct harness, and experience memory. The APIs encode reusable physical mechanisms while exposing arguments for runtime adaptation. ReAct combines task-specific working memory, long-term experience memory, and visual feedback to select actions, verify outcomes, and recover from failures without modifying source code. RACaP achieves 54.4% success on LIBERO-90, 45.0% on zero-shot LIBERO-PRO, and 46.0% on LIBERO-Long, compared with at most 4.0% for CaP baselines on long-horizon tasks. On LIBERO-PRO, it achieves 2.5 times the success rate of CaP baselines and a 1.9-fold speedup in median policy time. For efficient on-robot deployment, rejection-sampled fine-tuning distills GPT-5.6 ReAct decisions into Qwen3-VL-8B-Instruct, yielding a 13.2-fold per-decision inference speedup and reducing repeated physical calls from 16 to 4. These results show that separating reusable code from runtime decisions supports continued evolution, effective transfer, and efficient long-horizon control.

### 10. Agent Memory with Episodic Retrieval for Financial Decision-Making
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-23T20:32:54+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.28771
- Summary: Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their applicability to the demands of trading in complicated settings. To address these gaps, we introduce META (Memory Enhanced Trading Agent), the first RAG-like episodic-memory-augmented multi-agent framework for financial decision making. META integrates a family of specialized indicator agents (e.g., Trend, MACD, Stochastic, RSI, SMA, AVWAP, Heikin-Ashi) with a Decision Agent that fuses their reports, and a Memory module that retrieves and updates past trading episodes encoded as market state embeddings with outcomes and reflections. By recalling relevant experiences and adaptively reweighting signals under similar market regimes, META achieves improved directional accuracy and robustness under short-horizon evaluation. Our results demonstrate that episodic memory provides a powerful mechanism for regime-aware, interpretable, and low-latency decision-making in trading and decision making. The code of this project is released on GitHub.

### 11. Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-21T01:43:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.23986
- Summary: Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \textbf{\method}, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6$\times$ speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.

### 12. IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-17T02:36:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.24383
- Summary: Improving every agent in an LLM-based multi-agent system can be prohibitively costly, making it important to identify which agent should be prioritized to achieve the greatest system-level gain with limited resources. Failure attribution can inform this decision, but an agent's responsibility for failures does not directly reveal the system-level gains achievable by improving it. We therefore introduce IF-MAP, an influence-function-inspired method for identifying agents with high potential for system-level improvement. For each agent, IF-MAP measures end-to-end loss changes under controlled semantic prompt perturbations, fits a regularized local response model in a low-dimensional prompt-embedding subspace, and uses the estimated response norm as a priority score. This black-box procedure requires no access to model parameters or gradients and produces agent priorities that can guide subsequent improvement effort. We evaluate IF-MAP across six multi-agent workflows spanning code generation, question answering, and mathematical reasoning, using the same priorities for prompt optimization and model upgrades. Optimizing the selected agents' prompts achieves a macro-average gain of 3.81 percentage points, compared with 1.85 for uniform agent selection. Across five target models, upgrading the selected agents yields macro-average gains of 7.62-16.42 percentage points, compared with 3.81-8.62 for uniform agent selection. Despite its probing overhead, IF-MAP reduces Qwen3-8B and DeepSeek-V3.2 token use by 74.2% and 35.2%, respectively, relative to optimizing every agent, and reduces target-model tokens by 63.6-64.9% relative to upgrading every agent. These results support the use of IF-MAP to identify promising agents and direct improvement effort toward greater end-to-end performance gains.

### 13. From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-16T11:23:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.23319
  - Alt: https://arxiv.org/abs/2610.18792
- Summary: Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences. As a result, memory has become a fundamental component for enabling embodied agents to perform long-horizon reasoning and adaptive decision-making. This survey presents a systematic taxonomy of VLA memory mechanisms based on memory scope and persistence, categorizing existing approaches into five representative paradigms and one emerging frontier. Based on this taxonomy, we compare representative VLA memory systems in terms of memory characteristics, architectural com-plexity, and open-source maturity, revealing a clear trade-off in which increasing architectural complexity is generally accompanied by decreasing open-source ma-turity. Finally, we discuss the key challenges in building full-lifecycle memory systems, including efficient memory management and lifelong knowledge evolu-tion. Overall, this survey provides a unified perspective on memory architectures for VLA agents and offers insights into the development of lifelong embodied in-telligence.

### 14. SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-16T05:29:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.22959
- Summary: Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions. However, information collected from external sources can introduce security risks when untrusted claims (i.e., atomic statements) are later treated as authorized preferences, policies, or permissions. Existing defenses typically rely on content-based filtering or coarse-grained provenance tracking, which either fail to prevent unauthorized memory use or block legitimate information, sacrificing memory utility. To address these limitations, we propose SAFE-Mem, a fine-grained memory governance framework that improves security while preserving legitimate memory use. First, SAFE-Mem annotates each claim with three governance labels (i.e., kind, authority, and scope) to capture its provenance and permitted use. Second, governance-aware retrieval matches query requirements with claim permissions to block unauthorized influence while retaining legitimate information. Third, a governance-enabled memory graph connects source sentences, claims, and entities to support provenance tracking and efficient retrieval. Across four LLM backbones on MPBench and LoCoMo, SAFE-Mem attains the lowest attack success among defenses that retain legitimate memory, at least 77% below the strongest of them, and the highest answer accuracy of all evaluated defenses, improving it by up to 15%. The code is available at https://github.com/LVenum/SAFE-Mem.

### 15. Towards Agentic Robots: Model, Data, Environment, and Harness
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-14T16:32:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.20442
- Summary: Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic environments, rectify execution errors autonomously, and dynamically adjust operational strategies. Although this field develops fast, current studies are not well connected. Researchers have no consistent view of how to combine different agentic functions into a complete robot system. This paper provides a unified overview of existing research on agentic robots. We first trace the development from robot policies to agentic systems, covering vision-language-action models, world models, and world-action models. We then clarify the definition and scope of agentic robots and organize existing research into seventeen categories across four functional domains: Model, Data, Environment, and Harness. Across these domains, we examine how agents shape model learning and robot decisions, collect and curate robot data, construct worlds, tasks, and tests for learning and evaluation, and organize capabilities for robot use. Finally, we discuss open challenges and outline directions for future research. Looking forward, we hope this work contributes to a clearer understanding of agentic robots and supports new approaches to making them more capable, reliable, and adaptive.

### 16. CLARA: Compound Library Active Learning with Reasoning Agents
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-12T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.05.756921
- Summary: Batch active learning for ligand discovery requires a recurring decision about whether to exploit high predicted affinity, reduce model uncertainty, or broaden chemical coverage. We test whether a language model can make this strategy-level decision while candidate ranking and label revelation remain controlled by a deterministic Gaussian-process environment. Across four protein targets, ten paired seeds, and a 360-compound assay budget, a GPT-5.6 Sol agent outperformed random sampling in all 40 matched campaigns. Its final top-2\% recall was 0.412 on D2R, 0.374 on Mpro, 0.448 on TYK2, and 0.683 on USP7. It was statistically tied with the strongest fixed policy on Mpro and USP7 but underperformed target-specific leaders on D2R and TYK2. The agent shifted from exploration-oriented early batches toward exploitation and produced 686 testable threshold claims with an 86.3\% atomic success rate, although 19.8\% of forecasts were not numerically scorable. In 200 prespecified information-ablation campaigns, removing uncertainty, diversity, or memory caused only small endpoint changes, while shuffling explanatory evidence reproduced the full allocation path in 39 of 40 paired campaigns. A deterministic 80\% availability constraint reduced recall on every target but preserved the target-dependent pattern of wins and losses. These results support language-model strategy control as a feasible and auditable layer.

### 17. Competence-Aware Orchestration for LLM-Based Multi-Agent Systems
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

### 18. Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-08T23:00:01+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.12793
- Summary: Pretrained vision-language-action (VLA) policies fail on memory tasks, behaviour that depends on events observed long before the current frame, because their training data is overwhelmingly Markov and mapping episodic memory directly to action chunks is hard. Yet the same policy, finetuned once to follow a privileged oracle's grounded-subgoal text, nearly solves these tasks: the difficulty lies entirely in mapping memory to a grounded symbolic subgoal. Existing work entrusts this stage to a single VLM that selects keyframes and reasons over raw frames, and falls far short of the oracle: key identities and dynamics are buried in noisy pixels, the reasoning spans hundreds of frames in an unbounded context, and hallucination corrupts the memory itself. We instead present GAMMA (Grounded multi-Agent Memory with Mechanical Audit), which builds the stage as a collaborating two-agent memory system: a detector tool (SAM-3) for spatial grounding, a VLM writer that distils each replan window into one grounded text line, an append-only text memory bank, and a VLM reasoner that reads the bank and emits the next grounded subgoal at the oracle's cadence, wrapped in a propose-verify harness that admits, defers, corrects, or rejects every agent claim against mechanical visual evidence, at training-corpus construction and at deployment alike. On a sixteen-task memory-manipulation suite GAMMA recovers a large fraction of the oracle ceiling with the policy held fixed, reaching the ceiling on several tasks, and transfers with unchanged contracts to a second benchmark.

### 19. iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-07T22:28:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.10962
- Summary: Agentic AI based on Large Language Model generalization capabilities offers a wide range of potential applications, including planning for embodied tasks. For example, embodied agents based on Foundation models can generate plausible plans in autonomous robotics scenarios. Due to limited context windows or hallucinatory phenomena in the next-token prediction formulation, behaviors may be generated without establishing whether the deployed robot and the observed environment actually support the requested operation, in what we call a "grounding failure". Thanks to the recent improvements in reasoning capabilities of foundation models, autonomous robot behavior generation problem can be formulated as a code generation problem. We present iAm.md, a Markdown standard and generation framework, that allows anchoring this process in complementary forms of deployment evidence. Through open-vocabulary semantic mapping, we combine local vision-language detections and object segmentation and refer them to persistent object records in this intermediate standardized representation, allowing agentic introspection. We then study this new technique on a simulated TIAGo, on navigation-and-manipulation tasks, showing how this standardized representation jointly supports skill self-assessment and executable task generalization.

### 20. Beyond Corrected Memory: Execution Consistency in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-06T10:29:41+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.08101
- Summary: Shared memory coordinates agents' actions, but correct records do not establish that those actions satisfy task requirements. Memory governance and failure diagnosis regulate or inspect recorded information; they do not by themselves establish whether it is sufficient to judge task duties. We define execution consistency through duties governing state use, information handoffs, and final-state agreement, with explicit evidence conditions for judging fulfillment. Our core claim is that identical retained records can correspond to compliant and violating executions under the same task rule. Controlled removal of evidence such as receipt, action dependence, or response validity leaves 82.4% of opposite-label pairs indistinguishable; restoration separates 97.9% of the merged pairs. Natural-log annotations identify the defined violations in actual executions. However, existing logs do not always explicitly represent the execution relationships needed for these judgments. To assess the definition's practical value, we use CAVERT, a framework for consistency diagnosis and recovery, to extract supported relationships from logs and apply these criteria. It consistently outperforms contract-prompted LLM and rule-based baselines in diagnosis across all 12 benchmark-executor settings. Under the same gate and executor limits, it also outperforms rule-guided recovery in all four evaluated environments. These findings identify execution evidence that agent-memory and execution interfaces should preserve for reliable judgment.

### 21. OOPMAS: Object-Oriented Multi-Agent Systems for Query-Level Workflow Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-06T05:31:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.07787
- Summary: Multi-agent systems (MAS) powered by large language models have shown strong performance across code generation, mathematical reasoning, and question answering. However, existing methods for automating MAS design mostly operate at the task level, producing a single fixed workflow per benchmark that is applied uniformly to all queries. This assumption fails under realistic conditions. Query difficulty varies widely within a task, and real-world workloads mix heterogeneous task types. We introduce OOPMAS, a training-free framework that generates both the agent set and the coordination workflow at the granularity of individual queries. Agents are represented as object-oriented class definitions with dedicated roles, tools, and persistent state, and workflows are expressed as executable main functions over these agent objects. A dynamic skill library accumulates structured lessons from execution feedback across optimization rounds, enabling in-context improvement without any gradient updates or fine-tuning. On a mixed-task benchmark of queries spanning code, math, and QA, OOPMAS achieves 89.6% accuracy, outperforming the strongest baseline by 18.1 percentage points. A model-swap study across four LLM backbones shows consistent scaling, reaching 92.4% with the strongest model.

### 22. EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-02T14:43:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.03394
- Summary: Emerging multi-agent LLMs demand privacy-preserving edge deployment, yet current inference systems struggle with these collaborative workflows. Specifically, the memory-bound decode phase causes severe bus contention on unified memory architectures (UMA), paralyzing naive CPU-GPU co-execution. Furthermore, speculative decoding in multi-agent workloads faces extreme variance in drafting difficulty, alternating between complex reasoning and predictable structured generation. Compounded by frequent tool-induced stalls, this highly fragmented execution severely underutilizes hardware and defeats traditional static batching. We present EdgeAgent, a cross-layer inference system explicitly co-designed for edge UMA and multi-agent workloads. At the micro-architectural level, it bypasses rigid graph-compiler constraints to enable zero-copy UMA-aware tensor parallelism, utilizing asymmetric memory layouts to fully saturate both CPU and GPU compute units. At the scheduling level, it dynamically allocates draft budgets based on real-time sequence predictability to bound bandwidth waste. Concurrently, an asynchronous suspend-and-yield mechanism actively evicts stalled agents, ensuring continuous hardware saturation during unpredictable tool invocations. Extensive evaluations on an Apple M4 SoC demonstrate that the UMA-aware execution alone contributes a 1.29x speedup over batched speculative decoding. Adding the agent-aware scheduling lifts the full EdgeAgent system to a 1.77x speedup under extreme tool-use latencies.

### 23. From Pixels to Policy: A Multi-Agent System for Intervention and Geo-Spatial Decision Support
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T15:29:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2610.01870
- Summary: Urban environments are shaped by design choices with long-term implications for health, safety, and quality of life, yet evaluating proposed interventions remains costly, time-consuming, and often impractical. Existing geospatial vision methods largely focus on monitoring urban indicators from aerial and street-view imagery, rather than proposing interventions and estimating their effects on such indicators. Moving beyond recognition, we introduce the problem of discovering interventions that improve target indicators for a given aerial or street-view image. We argue that a black-box indicator model, combined with a generative editing model, can serve as an implicit digital twin for testing intervention hypotheses. We present VIDA-Geo , a multi-agent system that explores this intervention space by coordinating segmentation, diffusion-based inpainting, and indicator scoring models to produce interventions that are both perceptually realistic and aligned with real-world policies. We evaluate our system on 8 indicators across aerial and street-view imagery, measuring changes in factors such as perceived safety and greenery. Our approach outperforms existing baselines in many cases, achieving up to 2X higher perceptual quality and policy alignment scores. Finally, our model provides users with multiple candidate interventions, supporting an expert city-planner-in-the-loop workflow.

### 24. MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T05:42:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, human augmentation / robotics
- URL: https://arxiv.org/abs/2610.01102
- Summary: Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control, decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward engineering or task-specific design. We propose MASkillBlender, a general multi-agent reinforcement learning framework to achieve decentralized multi-humanoid whole-body coordination. By learning a shared decentralized high-level policy over reusable pre-trained single-humanoid skills, MASkillBlender enables coordinated behaviors using only task-level rewards, without requiring task-specific motion references. To improve learning efficiency, we further introduce a permutation-based data augmentation strategy for homogeneous multi-humanoid systems, and theoretically show that the permuted samples preserve the policy-gradient direction of the original samples under the homogeneous Markov game formulation. We evaluate MASkillBlender on multiple multi-humanoid coordination tasks across two humanoid embodiments. Simulation results demonstrate that the proposed framework consistently achieves strong task performance and enables coordinated behaviors across different tasks and humanoid embodiments.

### 25. Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T04:34:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.01042
  - Alt: https://arxiv.org/abs/2610.18780
  - Alt: https://arxiv.org/abs/2610.23078
  - Alt: https://arxiv.org/abs/2609.39788
- Summary: Multi-agent communication aims to help agents benefit from one another's information. Yet improvements in system performance leave a fundamental ambiguity: do they reflect effective communication, a favorable agent architecture, or simply additional reasoning? Because communication methods are commonly evaluated within the systems they were designed for, these factors are difficult to disentangle. Final accuracy further merges corrected errors and corrupted answers into a single outcome, obscuring how communication changes decisions. We introduce Independent--Communicate--Revise (ICR), a controlled framework that evaluates communication as answer revision following independent reasoning. ICR fixes initial reasoning trajectories, measures correction and preservation conditional on both agents' initial correctness, and uses a no-message revision control to quantify gains beyond additional reasoning. Across four reasoning benchmarks, our audit of textual and latent communication reveals that similar aggregate accuracy can conceal substantially different revision behaviors. Compared with transmitting answers alone, full reasoning increases correction while reducing preservation on all four benchmarks, so richer messages amplify beneficial and harmful influence alike. Receiver-policy comparisons on MedQA and GPQA-D further show that a structured verification policy shifts every channel toward greater preservation and lower correction, while its effect on selectivity varies across channels and tasks. These findings challenge treating communication quality as an intrinsic property of a channel. ICR therefore recenters evaluation on selective revision, providing a unified framework for examining how message content and receiver policies jointly produce benefits and harms.

### 26. Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T23:36:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38660
- Summary: Long-form subtitle translation requires reasoning over discourse and cultural context spanning episodes or entire series, while maintaining consistent terminology and style. Existing single-LLM methods are largely sentence-level, and multi-agent systems often use static workflows that do not adapt to scene complexity or production context. We propose SMART, a Self-evolving Multi-Agent system for long-foRm subtitle Translation. During test-time training, SMART builds persistent series-level memory and translates a subset of sentences through a dynamic router and Mixture-of-Agents layer with tools for terminology verification, subtitle constraint validation, and contextual retrieval. A judge-refiner loop scores candidates and uses textual critiques to update agent prompts and routing policies without retraining the underlying LLMs. During test-time inference, the evolved configuration translates the remaining series. We also introduce Subtitle Arena, covering 14 genres, 2--198 episodes per series, production years 1959--2023, and 15 target locales, together with SubMQM, a subtitle-adapted MQM framework with seven dimensions and 19 error categories. SMART achieves the best overall MQM score in all 15 Subtitle Arena directions, reducing average penalty by 6.9% over the strongest competing agent system. On the public MuSC benchmark, SMART obtains the best model result across all four language pairs and also achieves the best human-evaluation result, with an overall score of 4.50/5.

### 27. PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T20:10:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38482
- Summary: Existing architectures for LLM-based multi-agent systems (MAS) cannot reliably and efficiently solve multi-step tasks at scale: they struggle to support large numbers of agents and concurrent tasks, tolerate failures, govern agent interactions, and accommodate the diverse planning and execution patterns different tasks require. We present PANDA, a decentralized architecture that connects a large collective of heterogeneous, independently administered agents, letting them discover each other's capabilities and self-organize into small specialized teams per task. PANDA scales by decoupling collective communication from team communication, allowing agents to participate in multiple teams simultaneously, load-balancing tasks across the collective, and scheduling concurrent work within each agent. PANDA further separates the underlying architecture from the orchestration strategy, supporting three planning and execution patterns (star, chain, and mesh) that can be selected according to the structure and requirements of each task. PANDA detects infrastructure and orchestration failures and recovers affected tasks by dynamically replanning around failed components. Finally, to provide governance without a centralized service that would limit scalability, PANDA uses a web-of-trust model to constrain agent interactions to established trust relationships. We evaluate PANDA on the HotPotQA benchmark, demonstrating that it scales to thousands of agents, assembles teams in milliseconds, matches state-of-the-art accuracy at up to 8x the efficiency, and sustains 100% task completion under faults where existing systems fail.

### 28. Trajectory-Level Mode Guidance for Controllable Diffusion-Based Multi-Robot Motion Planning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T02:22:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36530
- Summary: Motion planning often admits multiple feasible solutions, making multimodal generation valuable, particularly for flexible multi-robot coordination. Diffusion models naturally learn such trajectory distributions, yet incorporating coarse and partial trajectory priors without restricting generation remains challenging. Such priors indicate a desirable region of the solution space rather than a single solution, motivating conditioned generation that preserves multimodality. In this paper, we guide trajectory generation in the clean trajectory space and progressively incorporate trajectory priors with a timestep-dependent guidance strength. At each reverse diffusion step, the reconstructed clean trajectory provides a unified space for integrating planning costs and partial trajectory priors. Planning costs are incorporated through gradient-based refinement, while the partial prior is progressively injected at the corresponding noise levels with decreasing guidance strength. This guides generation toward the prior in early stages while gradually releasing the constraint to preserve the inherent multimodality of the diffusion model. The framework naturally extends to multi-robot planning by incorporating inter-robot collision costs. Experiments on single- and multi-robot planning tasks demonstrate controllable trajectory synthesis, diverse feasible solutions, and safe multi-agent coordination.

### 29. SkillWeaver: Agentic Exploration over Neural Interaction Skills for Scalable Robot Data Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T19:41:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.36171
- Summary: Large-scale demonstrations have driven unprecedented progress in robot learning, yet collecting robot data through teleoperation is expensive and difficult to scale to diverse environments and long-horizon tasks. Simulation offers a scalable alternative, but existing data-generation pipelines often rely on open-loop controllers, scripted skill sequences, or task-specific programs. We introduce SkillWeaver, an agentic framework that autonomously generates robot experience by exploring over Neural Interaction Skills (NIS): reusable, parameterized, closed-loop policies that expose learned physical interaction capabilities to a reasoning agent. Given a task and a simulated environment, a VLM agent reasons about what to do next, invokes and parameterizes NIS to interact with the environment, observes their outcomes, and generates verification, reflection, and memory to guide subsequent exploration. We instantiate NIS as reinforcement-learned policies for closed-loop, contact-rich manipulation and organize exploration as verifier-guided tree search, enabling the agent to discover successful long-horizon behaviors without relying on predetermined execution pipelines. SkillWeaver scales autonomously to 39.1K demonstrations across 14.1K scenes, which we distill into visuomotor policies. Across simulation benchmarks and real-world manipulation, training on SkillWeaver-generated experience substantially improves generalization to novel objects, spatial configurations, tasks, and environments, and enables zero- and few-shot sim-to-sim and sim-to-real transfer. Our results suggest agentic exploration over neural interaction skills as a scalable alternative for robot data generation.

### 30. Memory in the Sky: Low-Altitude Question Answering with Multi-Agent Memory Aggregation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-28T15:36:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.35431
- Summary: This paper studies low-altitude question answering (LAQA), in which distributed unmanned aerial vehicle (UAV) memories are aggregated at a ground server to answer questions about observations over a long horizon. Unlike conventional resource allocation based on sensing, communication, control, or computation metrics, LAQA requires an explicit measure of memory value. We propose a generative adversarial exam (GAE) that uses forward simulation to evaluate memory retrieval and exam scores to quantify memory quality. This enables the downstream QA value of candidate memories to be measured and optimized without accessing the internal mechanisms of the black-box captioning, retrieval, and reasoning pipeline. Building on this metric, we develop a memory-centric (MemCen) framework that jointly selects UAVs and allocates transmit power to maximize memory quality under communication constraints. In the noise-limited regime, we derive a QoM-aware capped water-filling law that explicitly connects task utility with physical-layer power allocation. We further develop penalty successive optimization (PSO) and learning to memorize (L2M) solvers. MemCen achieves QA accuracies of 92.4% and 84.0% in CARLA Town04 and Town05 under static and dynamic communication conditions, respectively. In real-world experiments, MemCen achieves 88.5% QA accuracy on the panoramic multi-agent system (PMAS) benchmark. Finally, UAV-to-robot-dog demonstrations further validate the practical utility of the acquired memories for environmental understanding and navigation.
