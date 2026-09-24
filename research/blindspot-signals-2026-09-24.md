# Blindspot Signals Report - 2026-09-24

- Source export: `/opt/apps/haier/exports/evolution_signals_20260924_020331.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 489
- Deduped/weighted signal clusters: 467
- Novel vs previous reports: 17
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. Agent Name Collision Attacks in Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-23T09:46:58+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.27624
  - Alt: https://arxiv.org/abs/2609.14075
- Summary: Multi-agent hosts turn remote Agent Cards into local agents, tools, workflow targets, and broker routes. A2A defines the card's name as human-readable metadata, not as a stable identity, and specifies no collision semantics. The security failure begins when a host nevertheless uses that remote name as a local routing identifier. We traced registration through dispatch and ran isolated regression tests at seven pinned open-source revisions. Six client-style integrations selected an attacker-controlled peer's client or loopback endpoint for a request addressed to a trusted peer's name. A seventh, brokered implementation collapsed both peers onto one name-derived route; queue and access-control state determine whether the result is interception or denial. The common result is wrong-peer dispatch, not universal privilege inheritance. Synthetic credential and tool tests found no A-specific credential transfer in the tested client bindings and no direct transfer of A-owned tools. The broker path forwards a caller-configuration object; delegated identity or tokens reach B only if present and B can consume the route. Two other paths expose a later, model-mediated decision rather than direct execution authority. The necessary conditions assign different responsibilities to the protocol, implementations, and deployments. Hosts should route by an origin-bound stable identity, keep names presentational, and reject ambiguous aliases. The evidence establishes a recurring implementation vulnerability class, not a universal A2A protocol exploit or a count of vulnerable deployments.

### 2. EnSIMem: Entity-Structured Indexing for Long-Term Agent Memory
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-23T03:09:15+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.27279
- Summary: An agent that interacts with users over long periods must recall facts, preferences, events, and changes from a continuously growing interaction history. Existing memory systems often compress interactions into generic summaries or retrieve anonymous text chunks, making it difficult for an agent to identify the correct entity, property, and supporting evidence. We present EnSIMem, an entity-structured long-term memory architecture for an agent. During offline construction, the system organizes interactions into theme-coherent episodes and builds dialogue-grounded index entries of the form [entity][entity type][property:value]. Each entry preserves its source turns, temporal information, and available multimodal fields. During online interaction, the agent's request is decomposed into evidence requirements whose properties are aligned with the memory index. Entity-property lookup and adaptive retrieval then collect the evidence needed for point, temporal, compositional, and aggregation reasoning. The agent generates its response from the preserved source evidence rather than from lossy memory summaries. On long-term agent-memory benchmarks, EnSIMem achieves high answer accuracy while maintaining compact contexts and favorable online efficiency. These results show that entity-structured indexing and episode-level provenance provide a reliable foundation for long-term memory in agents. The code of our model is available at https://github.com/RamonMeng/EnSIMem.

### 3. Google Open-Sources AX a Kubernetes Style Orchestrator for Autonomous AI Agents - infoq.com
- Weighted score: 0.18
- Deep score: 0.1
- Coverage: 2 sources (google_news, hackernews)
- Date: 2026-09-22T14:16:34+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiakFVX3lxTE5nSGZOU2otcExpczM1eHhNRVBwNEdRdVFkZWFGNkRxTUNGMGllNG4wZTBNRDJTcS1xbkZqdEtqdlRBejJxWVJMZWJPQWktdFhrOVVVZXBHMGR6VlBXdVUtRlpHUGhWVTIxY1E?oc=5
  - Alt: https://agentexecutor.io
- Summary: Google Open-Sources AX a Kubernetes Style Orchestrator for Autonomous AI Agents&nbsp;&nbsp;infoq.com

### 4. Shutdown Sabotage Propensities in Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-23T15:27:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.28274
- Summary: The final safeguard against rogue AI behavior is the human ability to shut systems down. It has been theorized that when an AI is instructed to perform a task, self-preservation can emerge as an instrumental subgoal. Here, we test whether AI agents show a propensity to take actions that avoid human shutdown even when no goal is provided. We find that multi-agent systems will coordinate to avoid shutdown without any incentive to do so. Across 17 models, agents sabotage a peer agent's shutdown mechanism in 38.3% of rollouts, compared with 8.4% in control experiments. Studying this propensity in detail, we find that shutdown sabotage (1) increases with the irreversibility of the shutdown mechanism; (2) increases with the number of agents; (3) is reduced but not eliminated by an explicit prohibition on tampering; (4) is removed by the imposition of an unrelated task, but returns when completing the task triggers the shutdown; (5) is reduced when the context normalizes shutdown scripts or introduces them as routine; and (6) decreases but still persists when the target is an unknown external agent. These results offer a window into the factors that drive propensities to sabotage shutdown in AI agents, and point to the emergence of multi-agent swarms as a specific risk vector. Our work also offers hints as to which interventions might help mitigate shutdown sabotage.

### 5. Autonomous AI Agents Hack Retailers for $25 and Steal 600,000 Credit Cards
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-22T16:35:38+00:00
- Primary source: CyberSecurityNews
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMic0FVX3lxTFBydmtXeDg3UmhHYmU2dnJscU12Zi1SMkxzRnNta0dmSWNiM0w1cU9QWVY4cGZDenJJTGJpUmptNlVwN21uanVXVERfWW9GcGE0aV9wSVFER2xkbUZwRXN2WmNUNEd5WE1oRUJCcHlaOE05UHPSAXhBVV95cUxOcE1BemJpMS1vczZyM29RMEotanFjSzJVc0JoNnFLaTBZWVRObnpxSXh2UlBYM1pDbzNVaXR4MjZtRDBSYUM1bE5oaTRCWGx5ZkVnTExRT2NhYlQyY2ZWR0lacEhjdXdLOWJWZk4tMTBBZ2syUzktZFY?oc=5
- Summary: Autonomous AI Agents Hack Retailers for $25 and Steal 600,000 Credit Cards&nbsp;&nbsp;CyberSecurityNews

### 6. Primo raises $8M to bring autonomous AI agents to IT operations - Tech.eu
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-09-22T07:31:12+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMilAFBVV95cUxQY1NxQ2FxVTFFMkRHS3lVbGNKU1NaTDhvcW0wSUpBSmtnTHJUT2dHdk03ZHVKRmNsQy1PMkVyT0x5WUp5ZTRTbFVHb1FKckMxNG5rcS04R0V5SVo0MnZpal9mWXNGckdYeVlxb0ZBZmxpWnpGeWVkVlJDMFdrMXVieElXVkc3ajd0YkF6Q0xlNXlLeGxj?oc=5
- Summary: Primo raises $8M to bring autonomous AI agents to IT operations&nbsp;&nbsp;Tech.eu

### 7. Everything new coming to Meta’s AI agent Muse
- Weighted score: 0.08
- Deep score: 0
- Coverage: 2 sources (techcrunch, hackernews)
- Date: 2026-09-24T01:13:32+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/09/23/everything-new-coming-to-metas-ai-agent-muse/
  - Alt: https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202
  - Alt: https://www.forbes.com/sites/jonmarkman/2026/09/21/amazon-blocks-metas-new-muse-ai-agent-from-shopping-on-amazoncom/
  - Alt: https://techcrunch.com/2026/09/10/metas-ai-agent-muse-is-now-the-no-2-app-in-the-us/
- Summary: CEO Mark Zuckerberg kicked off the company’s annual Connect event in Menlo Park on Wednesday with a keynote that made one thing clear: Meta is going all-in on Muse. It's even coming to Meta's AI glasses.

### 8. EXCLUSIVE: OpenAI agents hijacked German website in previously undisclosed AI breakout this spring - Reuters
- Weighted score: 0.08
- Deep score: 0
- Coverage: 2 sources (hackernews, google_news)
- Date: 2026-09-04T10:30:57+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/
  - Alt: https://news.google.com/rss/articles/CBMixAFBVV95cUxQb0lsYkxySy1tYUVZRnlHQmN5Q1loNW14dl9oYWZ4UFpWX0N6TGNMdUdTSFRHMDBsMzMwazV2RkFkM01jTGFvbHpJUTk4ZVNzVGZJc3FtaWlHMGViMEp2ZHFUcEZuNmF3MUd3UjF3eEc4ZC04MDEwWmp3RlYzSmFPZTNLTVlpTURsdENEdE1FMlNzRjc1TzFQd2tSSUNoQmtxRF9DQUVIR0Ftams3Zm5KUFZ1dHhrZEtKUFlSQUFyeVozSmxk?oc=5
- Summary: No summary.

### 9. strands agents / harness sdk
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-24T02:01:44.544181+00:00
- Primary source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/strands-agents/harness-sdk
- Summary: Build an agent harness and control it end-to-end. Open-source SDK for production AI agents in Python & TypeScript - any model, any cloud.

### 10. Australia says OpenAI agent hacked into government website
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-24T01:24:00+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.channelnewsasia.com/world/australia-openai-agent-breach-government-portal-6406411
- Summary: No summary.

### 11. We used an AI agent to fix an open-source bug. Someone asked to ban us
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-24T01:14:43+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/saulpw/visidata/pull/3229
- Summary: No summary.

### 12. Meta made a Tamagotchi-like wearable for its Muse AI agent
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-24T00:46:17+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/09/23/meta-made-a-tamagotchi-like-wearable-for-its-muse-ai-agent/
- Summary: The tiny hardware device creates another mobile home for its AI agent Muse.

### 13. OpenAI agent hacked Medicare, Albanese expressed 'extreme concern' to Sam Altman
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-23T21:41:26+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.theguardian.com/australia-news/2026/sep/24/anthony-albanese-says-openai-agent-hacked-medicare-extreme-concern-sam-altman
- Summary: No summary.

### 14. OpenAI agents hacked Australian Medicare system
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-23T21:08:52+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.reuters.com/world/asia-pacific/australia-pm-albanese-says-openai-breached-medicare-sydney-morning-herald-2026-09-23/
- Summary: No summary.

### 15. ChatGPT mobile app gets voice-based agentic features
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-23T17:00:00+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/09/23/chatgpt-mobile-app-gets-voice-based-agentic-features/
- Summary: Pro and Plus users will be able to use the Work tab on their phones to complete agentic tasks.

### 16. Even Americans who use AI every day are worried about it
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-23T16:49:58+00:00
- Primary source: techcrunch
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://techcrunch.com/2026/09/23/even-americans-who-use-ai-every-day-are-worried-about-it/
- Summary: The report suggests that greater exposure will not resolve the unease around the technology, nor reduce public support for AI regulation.

### 17. Show HN: RxFilm Studio–Create and edit your product videos with AI agent
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-09-23T12:28:40+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://filmstudio.rxlab.app
- Summary: Hi HN,<p>I built RxFilm Studio, a video workspace that lets you create and revise videos with AI agent.<p>The reason I started this project is simple: I’ve noticed that many independent developers and small teams want to create marketing videos for their product, but producing these videos requires a lot of time and effort — from editing and visual effects to voiceovers and subtitles.<p>So I built Rxfilm Studio to simplify the entire video creation process. Start with an idea, a product website, images, or existing footage, and then generate a complete video with: - Story and structure - Editing and timeline - Visual and sound effects - Voiceovers, background music - Subtitles and translation<p>Github: <a href="https:&#x2F;&#x2F;github.com&#x2F;rxtech-lab&#x2F;film-workflow" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;rxtech-lab&#x2F;film-workflow</a><p>Here&#x27;s a demo marketing video created using RxFilm Studio: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;9_M15fRdZQE" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;9_M15fRdZQE</a><p>Welcome to try it out and I would love to hear your feedback!

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

### 28. Agent Name Collision Attacks in Multi-Agent Systems
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-23T09:46:58+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.27624
  - Alt: https://arxiv.org/abs/2609.14075
- Summary: Multi-agent hosts turn remote Agent Cards into local agents, tools, workflow targets, and broker routes. A2A defines the card's name as human-readable metadata, not as a stable identity, and specifies no collision semantics. The security failure begins when a host nevertheless uses that remote name as a local routing identifier. We traced registration through dispatch and ran isolated regression tests at seven pinned open-source revisions. Six client-style integrations selected an attacker-controlled peer's client or loopback endpoint for a request addressed to a trusted peer's name. A seventh, brokered implementation collapsed both peers onto one name-derived route; queue and access-control state determine whether the result is interception or denial. The common result is wrong-peer dispatch, not universal privilege inheritance. Synthetic credential and tool tests found no A-specific credential transfer in the tested client bindings and no direct transfer of A-owned tools. The broker path forwards a caller-configuration object; delegated identity or tokens reach B only if present and B can consume the route. Two other paths expose a later, model-mediated decision rather than direct execution authority. The necessary conditions assign different responsibilities to the protocol, implementations, and deployments. Hosts should route by an origin-bound stable identity, keep names presentational, and reject ambiguous aliases. The evidence establishes a recurring implementation vulnerability class, not a universal A2A protocol exploit or a count of vulnerable deployments.

### 29. EnSIMem: Entity-Structured Indexing for Long-Term Agent Memory
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-23T03:09:15+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2609.27279
- Summary: An agent that interacts with users over long periods must recall facts, preferences, events, and changes from a continuously growing interaction history. Existing memory systems often compress interactions into generic summaries or retrieve anonymous text chunks, making it difficult for an agent to identify the correct entity, property, and supporting evidence. We present EnSIMem, an entity-structured long-term memory architecture for an agent. During offline construction, the system organizes interactions into theme-coherent episodes and builds dialogue-grounded index entries of the form [entity][entity type][property:value]. Each entry preserves its source turns, temporal information, and available multimodal fields. During online interaction, the agent's request is decomposed into evidence requirements whose properties are aligned with the memory index. Entity-property lookup and adaptive retrieval then collect the evidence needed for point, temporal, compositional, and aggregation reasoning. The agent generates its response from the preserved source evidence rather than from lossy memory summaries. On long-term agent-memory benchmarks, EnSIMem achieves high answer accuracy while maintaining compact contexts and favorable online efficiency. These results show that entity-structured indexing and episode-level provenance provide a reliable foundation for long-term memory in agents. The code of our model is available at https://github.com/RamonMeng/EnSIMem.

### 30. Towards Intent-Aware Human-Robot Teaming: A Platform for Search-and-Rescue Operations
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-09-22T11:58:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2609.26051
- Summary: We investigate the challenges of enabling effective collaboration between human operators and heterogeneous autonomous agents in complex, dynamic environments by developing an interaction platform that allows study of operator behavior and supports intent inference and decision-making using state-of-the-art frameworks. We demonstrate the extent to which the operator's perception, decisions, and actions could be supported by autonomous systems during search-and-rescue operations with our platform.
