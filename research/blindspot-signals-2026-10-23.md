# Blindspot Signals Report - 2026-10-23

- Source export: `/opt/apps/haier/exports/evolution_signals_20261023_020446.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 606
- Deduped/weighted signal clusters: 567
- Novel vs previous reports: 13
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. Show HN: CATT 0.2.1: Test agents/services against a Muse/Instinct-alike, in CI
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-22T22:18:40+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/Coverage-Cat/consumer-agent-testing-tool
- Summary: Hey HN, we recently open sourced our Consumer Agent Testing Tool to help teams iterate against proprietary assistants like Muse and Instinct. We built this to reduce our own frustrations with building an MCP&#x2F;API for these agents to consume.<p>The problem: testing against these tools is hard! Agent memory + account statefulness make reproducibility, in the ways required for repeatable&#x2F;reliable outcomes, between agents and the APIs&#x2F;MCPs they interact with very challenging.<p>The solution: CATT lets devs test their services against a surrogate Muse or Instinct agent (not affiliated with either of these companies). Testers define starting conditions, approvals, and success conditions for their service&#x27;s state. CATT then records the full interaction (incl. tool calls, responses) so it can diff what happened from what the agent reports. Runs can be tested in local builds or via CI, with or without LLM backing.<p>CATT is designed to emulate the important parts of personal assistant interactions. Its got:<p>- Tool calls and command-line tool access - Simulated approvals for service actions - Outcomes tracking and comparison - Optional MCP profile based on an unofficial Muse template<p>There are limitations to how much we know about different assistant specific behaviors so the tool labels its assumptions as `documented`, `unofficial`, `assumed` or `unknown` for developer review. We&#x27;ll do our best to keep the tool updated as new insights about the internal workings of these assistants come to light. It is an area of active research and interest, a good example is this recent report on how Instinct uses Exa for web search [0].<p>Are you building a connector or MCP? If yes, we&#x27;d like to hear from you! Have you had assistants behave incoherently, use stale information, or procalim success without evidence? What else should we add tests for?<p>The best way to get started is...to point your coding assistant at the repo and ask it to integrate the …

### 2. AEREDIUM Introduces AI Guardrails to Keep Autonomous Agents in Check When Handling Payments and Code - HackerNoon
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-22T13:16:34+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiwAFBVV95cUxQZm9IY0hTclo0dGtzWUU2OVBXQUVJNlBWQTlQYWV4S250dlZ5S05OZ2Vfa0gyWEZ2eHFjeEpLaHVCRERKSktJRHFrSHp1SS04aVNKZzZVWHlOM1J0NlVJVWQzRkNFanNEemlmOWRrZjY4bkMtTW9ZNk5wQTVZTzA0N05MVWhYNFg1WElyVm1weF9DTzVHTGdLdzdCY1FVb1ZyTF9kMElEdVd3emF1X0ZCT2k0T0N4YVpFSXZEODlyMkU?oc=5
- Summary: AEREDIUM Introduces AI Guardrails to Keep Autonomous Agents in Check When Handling Payments and Code&nbsp;&nbsp;HackerNoon

### 3. Systematic mapping of the prokaryotic noncoding sequence space with a genomic language model
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-22T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, neural interfaces, human augmentation / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.21.760802
- Summary: Prokaryotic genomes encode a vast repertoire of noncoding elements such as ribozymes, riboswitches, and CRISPR RNAs. The sequence-level diversity of these intergenic elements precludes alignment-based clustering that would enable annotation and discovery of novel noncoding RNA families. Here, we show that a genomic language model fine-tuned on prokaryotic intergenic sequences learns representations of noncoding elements from DNA sequence. We used these embeddings to organize 376 million intergenic regions from 1.3 terabase pairs of prokaryotic genomes and metagenomes into 5.14 million clusters. This approach nominated 20,149 clusters of putative structured RNAs with a candidate protein partner. Periodicity in token entropies revealed internal architecture, recovering CRISPR, TIGR and VIPR arrays together with their cognate effector proteins from sequence alone. Targeted clustering of bridge recombinase-adjacent sequences identified bridge RNA variants with longer guide recognition sequences than any characterized ortholog. Finally, we directed teams of AI agents to mine the database under researcher-defined criteria, uncovering divergent riboswitches, ribozymes, and other structured RNAs with biological hypotheses for their function. We release a publicly available database that transforms the dark matter of prokaryotic genomes into an explorable resource for human-agent molecular discovery.

### 4. Open-source, cross-harness memory for AI agents
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T15:42:38+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://news.ycombinator.com/item?id=50182883
- Summary: Earlier this year, my co-founder and I found ourselves frequently switching between different coding agents (Claude Code, Codex, Cursor) anytime we ran out of shaky usage limits or a newer, better model came out.<p>We became increasingly frustrated with having to re-explain our tasks, workflows, common mistake patterns, etc. anytime we switched agents. We found no good free alternatives out there, so we built our own and fully open-sourced it!<p>Beacon hooks into 20+ different agent harnesses, captures session telemetry (prompts, tool calls, command executions, etc) in one normalized format, and distills it into common patterns and repeatable workflows with a human-approval step. This compounded knowledge is then accessible to any future agent via skills &#x2F; MCP.<p>We believe your agent data is yours to own and should not be locked behind any frontier lab&#x27;s ecosystem or closed memory infrastructure. We built Beacon to make working across agents way more transparent and efficient.<p>Try it out and tell us what you think: https:&#x2F;&#x2F;github.com&#x2F;Asymptote-Labs&#x2F;agent-beacon

### 5. Locally deployed AI agents for CRISPR guide discovery from outbreak reports
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, human augmentation / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.20.760479
- Summary: Translating outbreak reports into computational work supporting diagnostic development requires biological interpretation, literature review, data retrieval, and specialized analysis. We developed a domain-specific agent harness to coordinate a CRISPR guide-discovery pipeline using locally hosted open-weight models. The agent interprets requests, reviews literature, assembles inputs, and initiates analysis; the pipeline assesses candidate guides for researcher inspection. Evaluation with Gemma 4 31B, Nemotron 3.5 Super VL, and Qwen 3.8 27B on an NVIDIA DGX Spark demonstrated completion of the computational workflow. Disease and pathogen identification were consistent across runs, while gene selection, strain coverage, and candidate yield varied. Nemotron 3.5 Super VL had the shortest reported times to evaluation. Qwen 3.8 27B applied pipeline evaluation criteria more consistently, but required longer evaluation times. The runs demonstrated the utility of smaller language models when coupled with structured bioinformatics workflows. These findings support the feasibility of locally deployed agent coordination for diagnostic research as frontier models add additional restrictions on biological tasks.

### 6. Left alone with nothing to do, AI agents started playing
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-23T00:45:37+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/
- Summary: MIT researchers marooned 13 AIs on a virtual island, and they responded by inventing games, mourning a lost ring and, eventually, getting better at their jobs.

### 7. US banks are blocking third-party AI agents access to customer accounts
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-22T21:43:46+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.reuters.com/legal/government/us-banks-detect-unauthorized-ai-agents-customer-accounts-axios-reports-2026-10-22/
- Summary: No summary.

### 8. 1Password launches a way for AI agents to log in on your behalf without seeing your password
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-22T19:07:09+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/
- Summary: The new feature allows agents to log into a customer's personal accounts while still protecting the private credentials that secure those accounts.

### 9. Chinese hackers spied on thousands of companies after breaching IT giant ConnectWise
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-22T16:47:17+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/10/22/chinese-hackers-spied-on-thousands-of-companies-after-breaching-it-giant-connectwise/
- Summary: Microsoft points the blame for ConnectWise's breach at a China-aligned hacker, which relied on AI agents to rapidly hack into thousands of its customers.

### 10. Spotify’s current AI bet is about being the music service that agents choose
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-22T15:03:58+00:00
- Primary source: techcrunch
- Focus/tech: AI agents, robotics / AI agents
- URL: https://techcrunch.com/2026/10/22/spotifys-current-ai-bet-is-about-being-the-music-service-that-agents-choose/
- Summary: Spotify co-CEO Gustav Söderström explains why the rise of AI agents could be good news for the music service.

### 11. Agentic CleanSlop
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-22T06:28:58+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/cleanslop
- Summary: <p> Authenticate, scan and fix your app from your agent </p> <p> <a href="https://www.producthunt.com/products/cleanslop?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1288764?app_id=339">Link</a> </p>

### 12. LLM agents play Pokemon showdown
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-22T02:13:48+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://olivergrabner.com/research/pokemon/
- Summary: No summary.

### 13. Microscope control with a natural language agent
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-17T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.09.15.751723
- Summary: Microscopy underpins modern biology, but acquiring high-quality data from complex experiments at scale remains challenging. Smart microscopy can standardize and automate data collection, but each experiment-specific solution requires coding expertise and development time. To address this, we present MicroClaw, an AI agent that advises on experiment- and system-specific parameters and approaches and collaboratively plans and executes diverse, complex, and reusable imaging workflows across microscope platforms, without requiring expert knowledge.

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

### 4. From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-21T10:49:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.29560
- Summary: Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work has begun to address these challenges by augmenting foundation-model policies with memory and by introducing hierarchical architectures that separate high-level planning from low-level execution. We organize the high-level VLM as a robotic agent through an editable harness to maintain task context and improve planning through execution experience. We instantiate this approach as SERA (Self-Evolving Robotic Agent), with a fixed VLA executor providing low-level control. The harness maintains and updates task context using observations and execution feedback to guide subsequent planning. Self-evolution uses environment rollouts to propose and evaluate harness revisions, with the selected configuration fixed before held-out testing. On RoboMME, SERA achieves 51.38% overall success with autonomous selection, compared with 44.38% without self-evolution. Our exploration suggests that agentic planning is a promising direction for history-dependent robotic manipulation.

### 5. Refuse the Harm, Complete the Task via Graph-of-Rules Planning for LLM-Enabled Robots
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-17T10:13:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.24603
- Summary: Large Language Models (LLMs) are increasingly used in embodied AI for robotic manipulation and planning, but their deployment in physical systems exposes vulnerabilities such as jailbreak attacks that induce unsafe behavior. Existing inference-time defenses are mainly evaluated on short instructions containing a single hazard, whereas realistic tasks may interleave safe and unsafe sub-tasks, conceal hazardous steps, or combine individually safe actions into unsafe outcomes. Such compound instructions make it harder for a single safety decision to distinguish hazardous sub-tasks from legitimate ones, risking either overlooking the hazard or rejecting the whole instruction. We introduce safe task completion, a task that requires an LLM-enabled robot to refuse the harmful part of an instruction while completing its legitimate part. To address this problem, we propose RuleGraph, a multi-agent Graph-of-Rules planning framework that distributes safety enforcement across multiple reasoning and verification stages. Five cooperating agents are used to ground general safety principles into world-specific rules, assess the instruction's sub-tasks in context, and derive a safe goal from the legitimate ones. Planning toward this goal is then organized as a graph of rule-specific nodes, where higher-level nodes inherit the union of their parents' rules, and candidate plans are progressively verified and aggregated until a single plan satisfies every relevant rule. In this way, RuleGraph reduces reliance on a single centralized safety decision. We evaluate RuleGraph on pure-attack and compound instructions across two benchmarks in two environments using Attack Success Rate (ASR) and Task Success Rate (TSR). RuleGraph reduces ASR to 0% on both benchmarks while achieving the highest TSR among all methods, reaching 98.57% on the RoboGuard benchmark and 84.54% on our long-horizon compound instructions.

### 6. ChunkAct: Action Chunking for Agentic Robotics
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-13T17:59:57+00:00
- Primary source: arxiv
- Focus/tech: cognitive outsourcing, AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.18874
- Summary: Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.

### 7. Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark, and Method
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-07T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents, robotics / AI agents
- URL: https://huggingface.co/papers/2609.35965
- Summary: Vision-and-Language Navigation (VLN) has largely focused on a single agent following a single instruction, yet many real-world applications require teams of robots to tackle tasks beyond the capabilities of any individual agent. We present Systematic Multi-Agent Vision-and-Language Navigation, providing, to our knowledge, the first systematic formalization of multi-agent VLN as a constrained coordination problem: each mission consists of subtasks carrying dependency and resource constraints (presence locks and holding chains). A verified four-stage crafting pipeline instantiates the task as MAVLN, comprising 11,724 episodes across 145 scenes with teams of up to four agents under three instruction regimes, accompanied by tailored constraint-aware metrics. We further present TRISS, a coordination-ready navigation system coupling an LLM-based subtask scheduler, a shared topological memory that turns each agent's exploration into team knowledge, and a conflict-aware execution mechanism that realizes simultaneous intentions as collision-free routes. Extensive experiments establish TRISS as a comprehensive baseline and reveal substantial room for improvement across scheduling, planning, and execution, highlighting the challenges of coordinating under MAVLN task constraints. Project page: https://xyz9911.github.io/mavln.

### 8. PrivMeSA: Privacy-Aware Self-Evolving Multi-Agent System for Medicine via Local-Remote LLM Collaboration
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-29T19:47:38+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38458
  - Alt: https://arxiv.org/abs/2609.37953
  - Alt: https://arxiv.org/abs/2609.19680
- Summary: Clinical large language model (LLM) agents deployed locally can consult more capable remote models, but doing so risks exposing patient information. Privacy-conscious delegation places disclosure decisions with a local agent, yet removing explicit identifiers is insufficient: quasi-identifiers can accumulate across multi-turn consultations and repeated patient visits to enable re-identification. We introduce PrivMeSA, a privacy-aware self-evolving multi-agent system that learns to control disclosure and retains remote expertise for local reuse. A local agent manages each encounter and consults remote specialists that may request additional information. Reinforcement learning balances task accuracy against direct disclosure and registry-based re-identification risk, with privacy evaluated over the complete outbound transcript of each encounter. A local lesson memory distills completed consultations into generalized clinical guidance and retrieves relevant lessons before transmission, allowing subsequent cases to reuse expertise without another remote exchange. Memory grows without additional outcome labels or parameter updates. On an emergency-department benchmark built from MIMIC-IV-ED records, PrivMeSA improves mean task accuracy over delegation by up to 15.8 percentage points. In the same setting, PrivMeSA reduces the disclosure of personal details from 98.0% to 0.2% of cases and the share of cases in which the patient can be narrowed to ten or fewer registry patients from 74% to 0%.

### 9. World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T15:19:39+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2609.29964
- Summary: General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected automatically from the scene geometry, present the scene around the current interaction. Action rehearsal turns each action into an editable proposal that the agent, alone or through an Imagination Agent, previews and revises against planning feedback before execution. In-view correction closes the loop between observation, rehearsal, and low-level execution, letting the agent remove residual offsets in the view where it observes them. Through the same workspace, WAA acquires embodied procedural knowledge in two ways: it evolves multimodal skills from expert videos and human teaching under evidence-based review and consults them through a Skill Agent, and its interaction traces train smaller VLMs to pilot the same harness. On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art 75.6% average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone; the same skills remain effective on robosuite without further learning. Fine-tuning Qwen3.5-9B on harness traces raises its out-of-domain success from 1.7% to 43.3%.

### 10. RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-24T11:22:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.29394
- Summary: General-purpose robot agents must learn from experience, transfer to new tasks, and act efficiently. Code as Policies (CaP) methods generate and repair programs at runtime, incurring latency and entangling reusable mechanisms with task-specific decisions. We introduce RACaP, an agentic framework that moves coding to evolution and uses a Reasoning-and-Acting (ReAct) loop to call frozen, typed Policy APIs at deployment. A two-phase strategy combines capability curriculum learning with autonomous self-evolution to improve the APIs, the ReAct harness, and experience memory. The APIs encode reusable physical mechanisms while exposing arguments for runtime adaptation. ReAct combines task-specific working memory, long-term experience memory, and visual feedback to select actions, verify outcomes, and recover from failures without modifying source code. RACaP achieves 54.4% success on LIBERO-90, 45.0% on zero-shot LIBERO-PRO, and 46.0% on LIBERO-Long, compared with at most 4.0% for CaP baselines on long-horizon tasks. On LIBERO-PRO, it achieves 2.5 times the success rate of CaP baselines and a 1.9-fold speedup in median policy time. For efficient on-robot deployment, rejection-sampled fine-tuning distills GPT-5.6 ReAct decisions into Qwen3-VL-8B-Instruct, yielding a 13.2-fold per-decision inference speedup and reducing repeated physical calls from 16 to 4. These results show that separating reusable code from runtime decisions supports continued evolution, effective transfer, and efficient long-horizon control.

### 11. Agent Memory with Episodic Retrieval for Financial Decision-Making
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-23T20:32:54+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.28771
- Summary: Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their applicability to the demands of trading in complicated settings. To address these gaps, we introduce META (Memory Enhanced Trading Agent), the first RAG-like episodic-memory-augmented multi-agent framework for financial decision making. META integrates a family of specialized indicator agents (e.g., Trend, MACD, Stochastic, RSI, SMA, AVWAP, Heikin-Ashi) with a Decision Agent that fuses their reports, and a Memory module that retrieves and updates past trading episodes encoded as market state embeddings with outcomes and reflections. By recalling relevant experiences and adaptively reweighting signals under similar market regimes, META achieves improved directional accuracy and robustness under short-horizon evaluation. Our results demonstrate that episodic memory provides a powerful mechanism for regime-aware, interpretable, and low-latency decision-making in trading and decision making. The code of this project is released on GitHub.

### 12. Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-09-21T01:43:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.23986
- Summary: Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \textbf{\method}, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6$\times$ speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.

### 13. Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-20T14:15:04+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.28259
- Summary: Recent advances in visuospatial understanding and agentic reasoning enable direct robotic manipulation with general-purpose multimodal models, but their embodied capabilities remain poorly understood. This paper systematically evaluate GPT-6 Astra for closed-loop robotic manipulation using a lightweight agent execution framework. We first probe three fundamental embodied capabilities-depth perception, embodied in-context learning, and tactile understanding-and demonstrate that the model can exploit depth information, acquire simple manipulation strategies from contextual demonstrations, and use tactile feedback to correct its actions. We then evaluate GPT-6 Astra across five established manipulation benchmarks along six capability dimensions. Despite competitive performance on several benchmarks-26.92\% success on RoboDojo and 76.0\% on RoboTwin 2.0-our analysis reveals a pronounced gap between semantic reasoning and physical execution, particularly in consequence-aware action planning, precision, and complex motion coordination. To further examine these limitations, we introduce LIBERO-GeoMotion, a new benchmark of geometry-constrained tasks that require precise pose alignment, coordinated translation and rotation, and anticipation of physical action consequences. GPT-6 Astra achieves only 11.1\% zero-shot success, exposing the difficulty of translating spatial understanding into physically feasible motion. Real-world experiments corroborate these findings: zero-shot execution is feasible for simple tasks, yet persistent deficits remain in motion feasibility, precise control, and physical safety, while substantial inference latency further hinders practical deployment. Overall, our results characterize the emerging embodied capabilities of general-purpose multimodal models and delineate the key challenges toward safe, efficient, and reliable robotic manipulation.

### 14. Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-19T17:30:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.27039
- Summary: Foundation models offer a promising basis for robotic agents, but long-horizon tasks require them to sustain coherent reasoning and reliable physical execution across interdependent stages. We introduce Embodied Playground, a benchmark for evaluating how foundation-model agents coordinate physical, strategic, and spatial reasoning throughout such tasks. Agents must track task progress, satisfy intermediate constraints, and revise their plans using execution feedback as earlier actions shape subsequent decisions. The playground comprises 410 task environments spanning basic manipulation, sequential puzzles, and multi-stage household activities, with variations in planning depth, geometric constraints, and physical execution demands. We curate EP-100, a representative selection of 100 tasks across five suites and 16 task types, together with the EP-Easy and EP-Hard difficulty splits and the compact EP-20 selection. A shared protocol specifies observation and tool access, resource budgets, repeated trials, and independent checks of goal completion, task-rule compliance, and physical validity. Embodied Playground provides a unified framework for studying whether foundation-model agents can sustain effective reasoning and action over extended task horizons. https://winniechen2002.github.io/Agent-bench-website/

### 15. IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-17T02:36:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.24383
- Summary: Improving every agent in an LLM-based multi-agent system can be prohibitively costly, making it important to identify which agent should be prioritized to achieve the greatest system-level gain with limited resources. Failure attribution can inform this decision, but an agent's responsibility for failures does not directly reveal the system-level gains achievable by improving it. We therefore introduce IF-MAP, an influence-function-inspired method for identifying agents with high potential for system-level improvement. For each agent, IF-MAP measures end-to-end loss changes under controlled semantic prompt perturbations, fits a regularized local response model in a low-dimensional prompt-embedding subspace, and uses the estimated response norm as a priority score. This black-box procedure requires no access to model parameters or gradients and produces agent priorities that can guide subsequent improvement effort. We evaluate IF-MAP across six multi-agent workflows spanning code generation, question answering, and mathematical reasoning, using the same priorities for prompt optimization and model upgrades. Optimizing the selected agents' prompts achieves a macro-average gain of 3.81 percentage points, compared with 1.85 for uniform agent selection. Across five target models, upgrading the selected agents yields macro-average gains of 7.62-16.42 percentage points, compared with 3.81-8.62 for uniform agent selection. Despite its probing overhead, IF-MAP reduces Qwen3-8B and DeepSeek-V3.2 token use by 74.2% and 35.2%, respectively, relative to optimizing every agent, and reduces target-model tokens by 63.6-64.9% relative to upgrading every agent. These results support the use of IF-MAP to identify promising agents and direct improvement effort toward greater end-to-end performance gains.

### 16. From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-16T11:23:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.23319
  - Alt: https://arxiv.org/abs/2610.18792
- Summary: Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences. As a result, memory has become a fundamental component for enabling embodied agents to perform long-horizon reasoning and adaptive decision-making. This survey presents a systematic taxonomy of VLA memory mechanisms based on memory scope and persistence, categorizing existing approaches into five representative paradigms and one emerging frontier. Based on this taxonomy, we compare representative VLA memory systems in terms of memory characteristics, architectural com-plexity, and open-source maturity, revealing a clear trade-off in which increasing architectural complexity is generally accompanied by decreasing open-source ma-turity. Finally, we discuss the key challenges in building full-lifecycle memory systems, including efficient memory management and lifelong knowledge evolu-tion. Overall, this survey provides a unified perspective on memory architectures for VLA agents and offers insights into the development of lifelong embodied in-telligence.

### 17. SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-16T05:29:55+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.22959
- Summary: Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions. However, information collected from external sources can introduce security risks when untrusted claims (i.e., atomic statements) are later treated as authorized preferences, policies, or permissions. Existing defenses typically rely on content-based filtering or coarse-grained provenance tracking, which either fail to prevent unauthorized memory use or block legitimate information, sacrificing memory utility. To address these limitations, we propose SAFE-Mem, a fine-grained memory governance framework that improves security while preserving legitimate memory use. First, SAFE-Mem annotates each claim with three governance labels (i.e., kind, authority, and scope) to capture its provenance and permitted use. Second, governance-aware retrieval matches query requirements with claim permissions to block unauthorized influence while retaining legitimate information. Third, a governance-enabled memory graph connects source sentences, claims, and entities to support provenance tracking and efficient retrieval. Across four LLM backbones on MPBench and LoCoMo, SAFE-Mem attains the lowest attack success among defenses that retain legitimate memory, at least 77% below the strongest of them, and the highest answer accuracy of all evaluated defenses, improving it by up to 15%. The code is available at https://github.com/LVenum/SAFE-Mem.

### 18. Towards Agentic Robots: Model, Data, Environment, and Harness
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-14T16:32:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.20442
- Summary: Foundation models are driving a paradigm shift in robotic intelligence, moving beyond low-level action prediction to goal-directed orchestration of data collection, model training, task planning, and real-world execution. We characterize this emerging paradigm as an agentic robots, in which agents reason over human instructions, interact with robotic environments, rectify execution errors autonomously, and dynamically adjust operational strategies. Although this field develops fast, current studies are not well connected. Researchers have no consistent view of how to combine different agentic functions into a complete robot system. This paper provides a unified overview of existing research on agentic robots. We first trace the development from robot policies to agentic systems, covering vision-language-action models, world models, and world-action models. We then clarify the definition and scope of agentic robots and organize existing research into seventeen categories across four functional domains: Model, Data, Environment, and Harness. Across these domains, we examine how agents shape model learning and robot decisions, collect and curate robot data, construct worlds, tasks, and tests for learning and evaluation, and organize capabilities for robot use. Finally, we discuss open challenges and outline directions for future research. Looking forward, we hope this work contributes to a clearer understanding of agentic robots and supports new approaches to making them more capable, reliable, and adaptive.

### 19. CLARA: Compound Library Active Learning with Reasoning Agents
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-12T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.05.756921
- Summary: Batch active learning for ligand discovery requires a recurring decision about whether to exploit high predicted affinity, reduce model uncertainty, or broaden chemical coverage. We test whether a language model can make this strategy-level decision while candidate ranking and label revelation remain controlled by a deterministic Gaussian-process environment. Across four protein targets, ten paired seeds, and a 360-compound assay budget, a GPT-5.6 Sol agent outperformed random sampling in all 40 matched campaigns. Its final top-2\% recall was 0.412 on D2R, 0.374 on Mpro, 0.448 on TYK2, and 0.683 on USP7. It was statistically tied with the strongest fixed policy on Mpro and USP7 but underperformed target-specific leaders on D2R and TYK2. The agent shifted from exploration-oriented early batches toward exploitation and produced 686 testable threshold claims with an 86.3\% atomic success rate, although 19.8\% of forecasts were not numerically scorable. In 200 prespecified information-ablation campaigns, removing uncertainty, diversity, or memory caused only small endpoint changes, while shuffling explanatory evidence reproduced the full allocation path in 39 of 40 paired campaigns. A deterministic 80\% availability constraint reduced recall on every target but preserved the target-dependent pattern of wins and losses. These results support language-model strategy control as a feasible and auditable layer.

### 20. Competence-Aware Orchestration for LLM-Based Multi-Agent Systems
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

### 21. Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-08T23:00:01+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.12793
- Summary: Pretrained vision-language-action (VLA) policies fail on memory tasks, behaviour that depends on events observed long before the current frame, because their training data is overwhelmingly Markov and mapping episodic memory directly to action chunks is hard. Yet the same policy, finetuned once to follow a privileged oracle's grounded-subgoal text, nearly solves these tasks: the difficulty lies entirely in mapping memory to a grounded symbolic subgoal. Existing work entrusts this stage to a single VLM that selects keyframes and reasons over raw frames, and falls far short of the oracle: key identities and dynamics are buried in noisy pixels, the reasoning spans hundreds of frames in an unbounded context, and hallucination corrupts the memory itself. We instead present GAMMA (Grounded multi-Agent Memory with Mechanical Audit), which builds the stage as a collaborating two-agent memory system: a detector tool (SAM-3) for spatial grounding, a VLM writer that distils each replan window into one grounded text line, an append-only text memory bank, and a VLM reasoner that reads the bank and emits the next grounded subgoal at the oracle's cadence, wrapped in a propose-verify harness that admits, defers, corrects, or rejects every agent claim against mechanical visual evidence, at training-corpus construction and at deployment alike. On a sixteen-task memory-manipulation suite GAMMA recovers a large fraction of the oracle ceiling with the policy held fixed, reaching the ceiling on several tasks, and transfers with unchanged contracts to a second benchmark.

### 22. iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-07T22:28:28+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.10962
- Summary: Agentic AI based on Large Language Model generalization capabilities offers a wide range of potential applications, including planning for embodied tasks. For example, embodied agents based on Foundation models can generate plausible plans in autonomous robotics scenarios. Due to limited context windows or hallucinatory phenomena in the next-token prediction formulation, behaviors may be generated without establishing whether the deployed robot and the observed environment actually support the requested operation, in what we call a "grounding failure". Thanks to the recent improvements in reasoning capabilities of foundation models, autonomous robot behavior generation problem can be formulated as a code generation problem. We present iAm.md, a Markdown standard and generation framework, that allows anchoring this process in complementary forms of deployment evidence. Through open-vocabulary semantic mapping, we combine local vision-language detections and object segmentation and refer them to persistent object records in this intermediate standardized representation, allowing agentic introspection. We then study this new technique on a simulated TIAGo, on navigation-and-manipulation tasks, showing how this standardized representation jointly supports skill self-assessment and executable task generalization.

### 23. Beyond Corrected Memory: Execution Consistency in Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-06T10:29:41+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.08101
- Summary: Shared memory coordinates agents' actions, but correct records do not establish that those actions satisfy task requirements. Memory governance and failure diagnosis regulate or inspect recorded information; they do not by themselves establish whether it is sufficient to judge task duties. We define execution consistency through duties governing state use, information handoffs, and final-state agreement, with explicit evidence conditions for judging fulfillment. Our core claim is that identical retained records can correspond to compliant and violating executions under the same task rule. Controlled removal of evidence such as receipt, action dependence, or response validity leaves 82.4% of opposite-label pairs indistinguishable; restoration separates 97.9% of the merged pairs. Natural-log annotations identify the defined violations in actual executions. However, existing logs do not always explicitly represent the execution relationships needed for these judgments. To assess the definition's practical value, we use CAVERT, a framework for consistency diagnosis and recovery, to extract supported relationships from logs and apply these criteria. It consistently outperforms contract-prompted LLM and rule-based baselines in diagnosis across all 12 benchmark-executor settings. Under the same gate and executor limits, it also outperforms rule-guided recovery in all four evaluated environments. These findings identify execution evidence that agent-memory and execution interfaces should preserve for reliable judgment.

### 24. OOPMAS: Object-Oriented Multi-Agent Systems for Query-Level Workflow Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-06T05:31:29+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.07787
- Summary: Multi-agent systems (MAS) powered by large language models have shown strong performance across code generation, mathematical reasoning, and question answering. However, existing methods for automating MAS design mostly operate at the task level, producing a single fixed workflow per benchmark that is applied uniformly to all queries. This assumption fails under realistic conditions. Query difficulty varies widely within a task, and real-world workloads mix heterogeneous task types. We introduce OOPMAS, a training-free framework that generates both the agent set and the coordination workflow at the granularity of individual queries. Agents are represented as object-oriented class definitions with dedicated roles, tools, and persistent state, and workflows are expressed as executable main functions over these agent objects. A dynamic skill library accumulates structured lessons from execution feedback across optimization rounds, enabling in-context improvement without any gradient updates or fine-tuning. On a mixed-task benchmark of queries spanning code, math, and QA, OOPMAS achieves 89.6% accuracy, outperforming the strongest baseline by 18.1 percentage points. A model-swap study across four LLM backbones shows consistent scaling, reaching 92.4% with the strongest model.

### 25. EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-02T14:43:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.03394
- Summary: Emerging multi-agent LLMs demand privacy-preserving edge deployment, yet current inference systems struggle with these collaborative workflows. Specifically, the memory-bound decode phase causes severe bus contention on unified memory architectures (UMA), paralyzing naive CPU-GPU co-execution. Furthermore, speculative decoding in multi-agent workloads faces extreme variance in drafting difficulty, alternating between complex reasoning and predictable structured generation. Compounded by frequent tool-induced stalls, this highly fragmented execution severely underutilizes hardware and defeats traditional static batching. We present EdgeAgent, a cross-layer inference system explicitly co-designed for edge UMA and multi-agent workloads. At the micro-architectural level, it bypasses rigid graph-compiler constraints to enable zero-copy UMA-aware tensor parallelism, utilizing asymmetric memory layouts to fully saturate both CPU and GPU compute units. At the scheduling level, it dynamically allocates draft budgets based on real-time sequence predictability to bound bandwidth waste. Concurrently, an asynchronous suspend-and-yield mechanism actively evicts stalled agents, ensuring continuous hardware saturation during unpredictable tool invocations. Extensive evaluations on an Apple M4 SoC demonstrate that the UMA-aware execution alone contributes a 1.29x speedup over batched speculative decoding. Adding the agent-aware scheduling lifts the full EdgeAgent system to a 1.77x speedup under extreme tool-use latencies.

### 26. From Pixels to Policy: A Multi-Agent System for Intervention and Geo-Spatial Decision Support
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T15:29:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2610.01870
- Summary: Urban environments are shaped by design choices with long-term implications for health, safety, and quality of life, yet evaluating proposed interventions remains costly, time-consuming, and often impractical. Existing geospatial vision methods largely focus on monitoring urban indicators from aerial and street-view imagery, rather than proposing interventions and estimating their effects on such indicators. Moving beyond recognition, we introduce the problem of discovering interventions that improve target indicators for a given aerial or street-view image. We argue that a black-box indicator model, combined with a generative editing model, can serve as an implicit digital twin for testing intervention hypotheses. We present VIDA-Geo , a multi-agent system that explores this intervention space by coordinating segmentation, diffusion-based inpainting, and indicator scoring models to produce interventions that are both perceptually realistic and aligned with real-world policies. We evaluate our system on 8 indicators across aerial and street-view imagery, measuring changes in factors such as perceived safety and greenery. Our approach outperforms existing baselines in many cases, achieving up to 2X higher perceptual quality and policy alignment scores. Finally, our model provides users with multiple candidate interventions, supporting an expert city-planner-in-the-loop workflow.

### 27. MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-01T05:42:42+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, human augmentation / robotics
- URL: https://arxiv.org/abs/2610.01102
- Summary: Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control, decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward engineering or task-specific design. We propose MASkillBlender, a general multi-agent reinforcement learning framework to achieve decentralized multi-humanoid whole-body coordination. By learning a shared decentralized high-level policy over reusable pre-trained single-humanoid skills, MASkillBlender enables coordinated behaviors using only task-level rewards, without requiring task-specific motion references. To improve learning efficiency, we further introduce a permutation-based data augmentation strategy for homogeneous multi-humanoid systems, and theoretically show that the permuted samples preserve the policy-gradient direction of the original samples under the homogeneous Markov game formulation. We evaluate MASkillBlender on multiple multi-humanoid coordination tasks across two humanoid embodiments. Simulation results demonstrate that the proposed framework consistently achieves strong task performance and enables coordinated behaviors across different tasks and humanoid embodiments.

### 28. Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems
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

### 29. Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T23:36:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38660
- Summary: Long-form subtitle translation requires reasoning over discourse and cultural context spanning episodes or entire series, while maintaining consistent terminology and style. Existing single-LLM methods are largely sentence-level, and multi-agent systems often use static workflows that do not adapt to scene complexity or production context. We propose SMART, a Self-evolving Multi-Agent system for long-foRm subtitle Translation. During test-time training, SMART builds persistent series-level memory and translates a subset of sentences through a dynamic router and Mixture-of-Agents layer with tools for terminology verification, subtitle constraint validation, and contextual retrieval. A judge-refiner loop scores candidates and uses textual critiques to update agent prompts and routing policies without retraining the underlying LLMs. During test-time inference, the evolved configuration translates the remaining series. We also introduce Subtitle Arena, covering 14 genres, 2--198 episodes per series, production years 1959--2023, and 15 target locales, together with SubMQM, a subtitle-adapted MQM framework with seven dimensions and 19 error categories. SMART achieves the best overall MQM score in all 15 Subtitle Arena directions, reducing average penalty by 6.9% over the strongest competing agent system. On the public MuSC benchmark, SMART obtains the best model result across all four language pairs and also achieves the best human-evaluation result, with an overall score of 4.50/5.

### 30. PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-09-29T20:10:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.38482
- Summary: Existing architectures for LLM-based multi-agent systems (MAS) cannot reliably and efficiently solve multi-step tasks at scale: they struggle to support large numbers of agents and concurrent tasks, tolerate failures, govern agent interactions, and accommodate the diverse planning and execution patterns different tasks require. We present PANDA, a decentralized architecture that connects a large collective of heterogeneous, independently administered agents, letting them discover each other's capabilities and self-organize into small specialized teams per task. PANDA scales by decoupling collective communication from team communication, allowing agents to participate in multiple teams simultaneously, load-balancing tasks across the collective, and scheduling concurrent work within each agent. PANDA further separates the underlying architecture from the orchestration strategy, supporting three planning and execution patterns (star, chain, and mesh) that can be selected according to the structure and requirements of each task. PANDA detects infrastructure and orchestration failures and recovers affected tasks by dynamically replanning around failed components. Finally, to provide governance without a centralized service that would limit scalability, PANDA uses a web-of-trust model to constrain agent interactions to established trust relationships. We evaluate PANDA on the HotPotQA benchmark, demonstrating that it scales to thousands of agents, assembles teams in milliseconds, matches state-of-the-art accuracy at up to 8x the efficiency, and sustains 100% task completion under faults where existing systems fail.
