# Blindspot Signals Report - 2026-10-22

- Source export: `/opt/apps/haier/exports/evolution_signals_20261022_020451.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 605
- Deduped/weighted signal clusters: 565
- Novel vs previous reports: 31
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-10-21T10:49:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.29560
- Summary: Vision-language-action (VLA) models achieve strong performance across embodied manipulation tasks by unifying visual understanding, language conditioning, and action generation. However, long-horizon tasks can involve non-Markovian dependencies: successful decisions may require retaining task progress and past interaction outcomes, while partial observability and execution errors compound over time. Existing work has begun to address these challenges by augmenting foundation-model policies with memory and by introducing hierarchical architectures that separate high-level planning from low-level execution. We organize the high-level VLM as a robotic agent through an editable harness to maintain task context and improve planning through execution experience. We instantiate this approach as SERA (Self-Evolving Robotic Agent), with a fixed VLA executor providing low-level control. The harness maintains and updates task context using observations and execution feedback to guide subsequent planning. Self-evolution uses environment rollouts to propose and evaluate harness revisions, with the selected configuration fixed before held-out testing. On RoboMME, SERA achieves 51.38% overall success with autonomous selection, compared with 44.38% without self-evolution. Our exploration suggests that agentic planning is a promising direction for history-dependent robotic manipulation.

### 2. Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-20T14:15:04+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.28259
- Summary: Recent advances in visuospatial understanding and agentic reasoning enable direct robotic manipulation with general-purpose multimodal models, but their embodied capabilities remain poorly understood. This paper systematically evaluate GPT-6 Astra for closed-loop robotic manipulation using a lightweight agent execution framework. We first probe three fundamental embodied capabilities-depth perception, embodied in-context learning, and tactile understanding-and demonstrate that the model can exploit depth information, acquire simple manipulation strategies from contextual demonstrations, and use tactile feedback to correct its actions. We then evaluate GPT-6 Astra across five established manipulation benchmarks along six capability dimensions. Despite competitive performance on several benchmarks-26.92\% success on RoboDojo and 76.0\% on RoboTwin 2.0-our analysis reveals a pronounced gap between semantic reasoning and physical execution, particularly in consequence-aware action planning, precision, and complex motion coordination. To further examine these limitations, we introduce LIBERO-GeoMotion, a new benchmark of geometry-constrained tasks that require precise pose alignment, coordinated translation and rotation, and anticipation of physical action consequences. GPT-6 Astra achieves only 11.1\% zero-shot success, exposing the difficulty of translating spatial understanding into physically feasible motion. Real-world experiments corroborate these findings: zero-shot execution is feasible for simple tasks, yet persistent deficits remain in motion feasibility, precise control, and physical safety, while substantial inference latency further hinders practical deployment. Overall, our results characterize the emerging embodied capabilities of general-purpose multimodal models and delineate the key challenges toward safe, efficient, and reliable robotic manipulation.

### 3. Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-10-19T17:30:35+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.27039
- Summary: Foundation models offer a promising basis for robotic agents, but long-horizon tasks require them to sustain coherent reasoning and reliable physical execution across interdependent stages. We introduce Embodied Playground, a benchmark for evaluating how foundation-model agents coordinate physical, strategic, and spatial reasoning throughout such tasks. Agents must track task progress, satisfy intermediate constraints, and revise their plans using execution feedback as earlier actions shape subsequent decisions. The playground comprises 410 task environments spanning basic manipulation, sequential puzzles, and multi-stage household activities, with variations in planning depth, geometric constraints, and physical execution demands. We curate EP-100, a representative selection of 100 tasks across five suites and 16 task types, together with the EP-Easy and EP-Hard difficulty splits and the compact EP-20 selection. A shared protocol specifies observation and tool access, resource budgets, repeated trials, and independent checks of goal completion, task-rule compliance, and physical validity. Embodied Playground provides a unified framework for studying whether foundation-model agents can sustain effective reasoning and action over extended task horizons. https://winniechen2002.github.io/Agent-bench-website/

### 4. From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-21T17:11:52+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.30051
- Summary: Recent advances in frontier AI models have demonstrated remarkable capabilities in visual understanding, reasoning, planning, and tool use, raising the possibility of using general-purpose AI models for robot manipulation without task-specific training. However, their manipulation capabilities have not been systematically evaluated on standardized robotics benchmarks. In this report, we present a unified closed-loop manipulation framework for evaluating frontier AI models on the LIBERO-10 benchmark. Our framework enables models to control a robot directly through visual observations, robot proprioception, and structured tool calls, primarily by specifying target end-effector poses and gripper commands, without task-specific fine-tuning or pretrained manipulation skills. We evaluate six frontier AI models, including GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna, Claude Opus 5, Claude Opus 5.5, and Gemini-4 Argon, across three reasoning effort levels, resulting in 18 configurations and 1,800 evaluation episodes. Our results show that GPT-6 Astra achieves the highest success rate of 44%, followed by Gemini-4 Argon at 43%. Increasing reasoning effort generally improves manipulation performance, but the benefits vary across models and come at additional inference cost. We also observe substantial differences across tasks, with models performing relatively well on object placement tasks but struggling with precise spatial arrangements and complex multi-step interactions. These findings demonstrate both the potential and limitations of frontier AI models for robot manipulation, highlighting the challenges of translating reasoning capabilities into reliable physical actions. We release our evaluation framework and experimental results to support reproducible benchmarking and future research on reasoning-based robot manipulation.

### 5. Show HN: Omnara – Open-Source Alternative to Claude Managed Agents
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-21T16:44:53+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/omnara-ai/omnara
- Summary: Hey y&#x27;all, Kartik from Omnara (<a href="https:&#x2F;&#x2F;omnara.com">https:&#x2F;&#x2F;omnara.com</a>) here. We&#x27;re building an open-source API for running durable agents. You create an agent with an API call, and Omnara runs the agent loop, gives the agent sandboxes to run commands in, and handles secrets, permissions, and RBAC. Each agent&#x27;s state is stored in Postgres, so agents survive restarts and cost nothing while idle. You can message them and stream their events over the API.<p>You may remember us from our early days, when we made a remote-control phone app for Claude Code and Codex. Since the harness ran on a laptop back then, we had to build a relay to reach it, it stopped when the laptop closed, and moving it to a cloud sandbox meant syncing code and agent state between machines. We didn&#x27;t think remote-controlling a local agent was end-game for how people would run agents, so we built a new product where the agent runs in the cloud, any client can talk to it through an API, and it can still use your laptop as one of its machines.<p>Anthropic and OpenAI are building hosted versions of this, like Claude Managed Agents and the OpenAI Agents API. Omnara is an open-source version you can run on your own servers and use your own models. It&#x27;s basically a harness server like the opencode or codex servers, but durable, scalable, with the usual harness features like file and shell tools, subagents, compaction, permission prompts, MCP, skills, memory, yada yada yada.<p>Here&#x27;s some interesting architectural decisions we made while building this out:<p>Most harnesses, like Claude Code, Codex, OpenCode, Pi, Goose, etc, run the agent loop in one long-lived process that keeps its log in a JSONL or SQLite file. In Omnara, the log is an append-only event log in Postgres, with inputs, model outputs and tool calls stored as typed rows in their own tables. The loop runs on stateless workers in the control plane. A worker runs one iteration of …

### 6. Observer-Based Control for Multi-Agent Systems under Communication-Task Graph Mismatch and Directed Switching Topologies
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-20T12:10:02+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.28094
- Summary: This paper addresses decentralized estimation and control of heterogeneous multi-agent systems communicating over directed switching topologies. The objective is to satisfy cooperative tasks that require coordination among agents according to a time-invariant task graph. To address the potential mismatch between the communication and task graphs, each agent is equipped with a k-hop Prescribed Performance State Observer (k-hop PPSO) to estimate the states of agents up to k communication hops away using only information exchanged with its 1-hop neighbors. A novel prescribed performance funnel construction is developed to account for the switching communication topology, and a sufficient lower bound on the dwell-time is derived to guarantee the prescribed performance specifications under topology variations. Further analysis shows that, if the desired control objective is achieved with exact knowledge of the required nonlocal states and the resulting closed-loop system is uniformly set-ISS with respect to the state estimation error, then replacing these states with their estimates guarantees convergence to a neighborhood of the desired set. The size of this neighborhood can be made arbitrarily small by appropriately selecting the observer performance bounds. A simulation study demonstrates task satisfaction under directed switching topologies.

### 7. JARVIS: From Visual Manuals to Autonomous Robotic Assembly
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-20T04:32:37+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.27618
- Summary: Visual manuals communicate procedural knowledge through stepwise diagrams, but translating these instructions into reliable long-horizon robotic execution remains challenging. We introduce JARVIS, a method-agnostic benchmark for autonomous visual-manual-guided execution without additional language instructions. JARVIS comprises 236,679 LEGO assembly tasks across 8,987 scenes, with a carefully curated JARVIS-v1 suite of 50 tasks for interactive robotic evaluation. Tasks span varying initial structural complexities and assembly horizons, requiring agents to interpret manuals, ground actions in an evolving workspace, and execute the intended procedure. A structure-aware evaluation protocol captures geometric accuracy, structural relations, construction order, partial progress, and completion. We further introduce JARVIS-agentic, a tool-grounded embodied agent that composes robot primitives into executable programs and uses execution feedback for verification and recovery, without task-specific action trajectories or model parameter updates. Across nine multimodal and reasoning models, task-oriented primitives increase the average assembly score. Performance nevertheless declines sharply with assembly horizon, and execution errors remain difficult to correct. Prior-task experience improves initial performance, while repeated reflection provides inconsistent benefits, highlighting persistent limitations in connecting visual procedural reasoning with reliable physical execution.

### 8. CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-10-19T17:59:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.26852
- Summary: Reinforcement learning enables mobile robots to make fast and scalable navigation decisions in constrained human-shared environments. However, directly extending single-robot approaches to multi-robot settings often fails to ensure safety and efficiency, especially under occlusions and out-of-distribution (OOD) scenarios, where individual robots may overlook potential risks or make inaccurate predictions. Leveraging cooperation effectively for both prediction and navigation remains a major challenge. We propose CoopUQ, a multi-robot social navigation framework that bridges uncertainty-aware cooperative occupancy forecasting and robust decision making. CoopUQ predicts future occupancy grid maps through cross-robot spatiotemporal feature fusion and further leverages forecasts and their uncertainty to guide policy via constrained multi-agent reinforcement learning, where the cost penalizes navigation through regions predicted to be occupied or highly uncertain. This design enables the policy to adapt its risk sensitivity under distribution shifts. Experimental results across multiple Unity3D-based simulation environments with both in-distribution and OOD settings, including diverse layouts, pedestrian densities, and rushing behavior, demonstrate improved prediction performance and safety over representative baselines. Real-robot experiments further demonstrate its robustness across various scenes. Our code and videos are available at https://coopuq.github.io/.

### 9. Chopin: A real-time multiplayer, agentic planning environment
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T21:57:38+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://githubnext.com/projects/chopin/
- Summary: No summary.

### 10. What Enterprises Need to Govern Before Giving the Keys to Autonomous Agents - BizTech Magazine
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T20:34:47+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMipAFBVV95cUxOLW9Cd1dQTVFZTzY5Y0drNmRNeHQ0MFg0Zld3M1RnVkkxNy1SSEVURzZaRTJPLTAwRWkzMTF6UDBkb3JleVRKbmFjdEZEakZYcjVneFFHcFZuY09wck5LTUFEYmlWcTdiaFFKcGZJeXRha29PbE9LSzNib3JUR1VGYklaUl90ZzZYT2Z5YlpLcGVjVzJqVkZiMXJya0dud2tvV0c2Qg?oc=5
- Summary: What Enterprises Need to Govern Before Giving the Keys to Autonomous Agents&nbsp;&nbsp;BizTech Magazine

### 11. Red Hat and Nvidia expand their partnership to secure autonomous AI agents - SiliconANGLE
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T15:25:00+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMisAFBVV95cUxQRllNeEU1LWFYdEp5RTFPX1lSRUJ2TlRLd1hMUzJoMkU1Y0xNQks5ek5RTDRxbGhJWFZFZV9NYTVNVWpiQUxtUHdaeUxCTmJlSXRWZl9xOHM3MkI1VVlUc05UaEUyY3I3MDZ2NjkyRUFKcUx6NElWc3B5bjVqSy1LNmdrd0Ntd1VWRk1KOWw5ZHpIcXRHeUVPVmZYMTJaaWJ1U3N2X2dvdkVkdW9Gb0xlMQ?oc=5
- Summary: Red Hat and Nvidia expand their partnership to secure autonomous AI agents&nbsp;&nbsp;SiliconANGLE

### 12. MemoryTax: The Bitter Lesson of Agent Memory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T14:46:27+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.29823
- Summary: Agent memory systems such as Mem0 and Zep decide what to keep before any question arrives; coding agents keep the raw history and let the model search it with its own tools. We ask whether designed memory still helps once the model is strong enough to search for itself. On one LoCoMo conversation (419 turns, 152 questions), we run four memory methods (full context, BM25, Mem0, Zep) and three coding agents (Pi, Codex, Claude Code), each with GPT-4o-mini, GPT-6 Luna and Claude Opus 5.5, and record what every rollout costs. This is a short empirical study, with one conversation and one run per cell. Agent memory is a costly patch for a weak model: Mem0 beats full context only with GPT-4o-mini, and its build alone costs more than a whole full-context rollout. Agent memory also has a ceiling, set by the model that writes it: a stronger reader does not recover what a weaker writer left out. With Claude Opus 5.5, Pi tops the cost-accuracy frontier, scoring 99% for less than half the cost of full context; its one miss is a wrong answer key. Part of that lead comes from photo captions that only the agents could read: on the 88 questions whose evidence has no photo, Pi and full context differ by one answer.

### 13. Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T12:48:10+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.29671
- Summary: Long-term agent memory is shifting from predefined workflows toward learnable policies for memory construction and retrieval. Existing learning-based methods either optimize construction alone or combine retrieval-side online reinforcement learning (RL) with offline construction supervision, limiting co-adaptation between the two stages. In this paper, we explore end-to-end online RL for a unified memory manager (Uni-Mem) that learns both capabilities under a shared policy. However, joint optimization with existing RL algorithms such as GRPO faces confounded group comparisons and sparse feedback over long memory-management trajectories. To this end, we propose Stage-Decoupled GRPO, which alternates construction and retrieval optimization while controlling variation from the other stage within each rollout group, yielding stage-specific learning signals. We further introduce Event-Wise Credit Assignment (ECA), which localizes feedback to responsible events and propagates event-level advantages to their constituent operations. Experiments on LoCoMo and LongMemEval show that Uni-Mem outperforms the strongest RL-based memory, demonstrating the effectiveness of jointly learning memory construction and retrieval via Stage-Decoupled GRPO and ECA.

### 14. Singapore’s CSA and Google identify safeguards and access controls to address autonomous AI agent risks - Industrial Cyber
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T12:43:25+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMi3wFBVV95cUxNTHVnX1dhMDRLd0QteTQ3TWZGMnhWOGQ4U3ZzZGY3cUgyUld6N01XZTJPODJldU91bjNWbGhSR0JFa0pJb2kyZm82Q2w5bzN0YmZrWXc5b3dFMFBMQnl4NzJmYnJhb3B6OU1yVzM3ZE5mTUpTLVZXNUdwdk1zYUVfdkdaMlN1cS1KeDJQRXU0U3JYWkxCdUhMVFBtT2RMdUs5cVhkRDNVdzl1Rml1bWJ1cC1DWTNrSGZJUXlNLVIwOHRGSHRuZy1yQmVkQXd6eUxwT2dRUlVBdXB4a0J2SDRj?oc=5
- Summary: Singapore’s CSA and Google identify safeguards and access controls to address autonomous AI agent risks&nbsp;&nbsp;Industrial Cyber

### 15. SuperCom Unveils SafeGenie for Real-Time Monitoring and Control of Autonomous AI Agents - PR Newswire
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T12:30:00+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMi2wFBVV95cUxNc1FKWjlodWZacmw4Y2NGUWVnbFdETHd6X29oaDFWZHg5Rjh1Y1lNN2VMSk9Dc3E1LXRMbEEyMFhKOFVpRVdsSm5tQ0ZNWlRaanI2UnhiNW1sbXZJQkZIQnVIbFpwUWdwTDJFT2tVXzVKRHpnSk5fZ2Q1SEp5R2RBVnk0amw2UDNabDIxSlZ3QjZsbDRQTXdRRDFCWmphME1wU3p5c28tWVZlOEFmX1BJYWlrMlZhNWtPQnU5emJVejBOb0RxcXVpaVoxcXpSb0ZLSWZTNm9vMXhuclE?oc=5
- Summary: SuperCom Unveils SafeGenie for Real-Time Monitoring and Control of Autonomous AI Agents&nbsp;&nbsp;PR Newswire

### 16. Credit Where Credit Is Due: Contrastive Attribution Topology Search for Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T06:46:11+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.29292
- Summary: An LLM multi-agent system (MAS) is only as good as the agents it chooses to trust: its accuracy and cost hinge on its topology, meaning which agents are included and how they communicate. A single task score, however, does not reveal which agents help or hinder performance. We propose Contrastive Attribution Topology Search (CATS), which searches for compact teams within a fixed supergraph of specialized agents. An LLM attributer compares execution traces across candidate topologies and assigns credit to individual agents. CATS uses these credits to update supergraph edges while progressively pruning weak edges and agents, yielding a small team for deployment. With small open-weight models and matched candidate evaluations, CATS improves mean accuracy on BigCodeBench by 5.3 percentage points over score-only heuristic search while using 54\% fewer deployment tokens. On MBPP, CATS matches the strongest baselines with fewer tokens than the other searches. In a HotpotQA prompt-poisoning stress test, CATS excludes all adversarially prompted agents in all three runs, whereas random search retains some at comparable accuracy. Per-agent credit thus supports both team optimization and the pruning of potentially harmful agents.

### 17. Design and Tuning of Multi-Agent Systems Using Bayesian Evolutionary Optimization
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-21T06:31:27+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.29276
  - Alt: https://arxiv.org/abs/2609.26726
- Summary: Designing effective multi-agent systems (MAS) remains a challenging and resource-intensive task. We propose a Bayesian Evolutionary Optimization framework for automatically discovering task-specific MAS topologies. The approach combines evolutionary operators to generate diverse workflow graphs with Bayesian optimization to focus cost intensive evaluations on promising candidates. In contrast to LLM-based candidate selection, our approach uses a graph-aware Gaussian Process and Expected Improvement to provide an explicit selection criterion during evolutionary search. We evaluate the method on BigCodeBench for code generation and on a tabular preprocessing benchmark using TabPFN. On BigCodeBench, evolved architectures achieve the highest overall performance among the evaluated agent systems. On temporal tabular datasets, optimized MAS preprocessing improves over the default TabPFN model on several tasks, while remaining competitive on IID datasets. Overall, the results demonstrate the potential of Bayesian selection for guiding evolutionary MAS search under expensive evaluation budgets.

### 18. Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-20T22:32:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.28966
- Summary: Large language model (LLM) agents are increasingly deployed in multi-agent systems (MAS) to accomplish complex tasks. Prior black-box red-teaming attacks mainly focus on single agents, but we find that these methods are far less effective in MAS, where multiple sub-agents may not directly interact with the user. Therefore, we introduce ReMAS, the first reinforcement learning-based red-teaming framework tailored to MASs, which fine-tunes attacker LLMs to generate effective adversarial prompts for system prompt extraction. The framework follows a two-step process: first, a rewrite stage refines base attack prompts to increase extraction success, and second, a template generation stage constructs attack templates that improve the likelihood of invoking specific sub-agents and thus revealing their system prompts. Extensive experiments show that our method substantially improves attack success rates compared to existing black-box attacks, with transferability across different backend LLMs and MAS structures. These results underscore the vulnerabilities of multi-agent systems and the importance of developing stronger defenses against adaptive black-box adversaries.

### 19. Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-20T17:58:32+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.28624
- Summary: Warehouse robot fleets continuously observe operational conditions, but preserving these observations as reusable semantic memory incurs substantial computation, communication, and storage costs. For example, explaining recurring aisle blockages can require reviewing video from multiple robots across several shifts. We present IndustrialRemembr, a shared spatiotemporal memory system that extends NVIDIA ReMEmbR to robot fleets and reduces server-side computation by generating scene descriptions only on demand. On each robot, an NVIDIA Jetson encodes video clips into retrieval embeddings with Cosmos-Embed1, vision tokens with Cosmos3-Edge, and reconstruction latents with the Wan2.2 VAE, without uploading raw camera frames. The encoding models are re-used to detect people in image patches, zeroing them out to support PII abstraction for GDPR-compliant deployments. We split Cosmos3-Edge at its vision-language boundary, placing the vision encoder on the robot and the language decoder on an on-premises server. A Nemotron agent retrieves memories by content, position, and time and queries the decoder using cached vision tokens. This design eliminates caption generation at write time, while cached-token decoding reproduces the unsplit model's output in all 450 tested decodes.

### 20. AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-20T17:41:09+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2610.28589
- Summary: Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memory, but relies on powerful closed-source models as planners and does not improve the planners' own capabilities. In contrast, coding agents have improved substantially by post-training the model itself. We therefore investigate whether post-training can also improve robot planners. However, applying it across robot harnesses requires accommodating different execution mechanisms, including VLA skill invocation and control-code generation. To this end, we introduce AgenticRoboRL, a framework for post-training robot planners across different harnesses. The training recipe combines supervised fine-tuning with multi-turn reinforcement learning. To accommodate different execution mechanisms, harness-specific adapters connect recorded planner interactions with task outcomes, enabling a common RL training pipeline while keeping execution components fixed. On LIBERO-PRO, AgenticRoboRL raises the success rate of a 9B-parameter planner from 18.1% to 71.0% without external memory, approaching the 72.1% achieved by Codex (GPT-5.5) with external memory. These results demonstrate post-training as an effective approach for improving robot planners. We will release the framework and trained planner checkpoints.

### 21. LatBridge: Efficient and Stable Model Replacement in Latent-Communication Multi-Agent Systems
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-20T08:06:13+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.27813
- Summary: Multi-agent systems rely on communication to complete tasks, and latent communication passes continuous representations to reduce text generation and re-encoding. However, multi-agent systems must reconfigure agent models, whereas existing latent-communication methods are built for fixed model combinations, so their interfaces may fail after replacement. Our pilot study confirms this interface failure and identifies the requirement for interface reuse after model replacement. We present LatBridge, which connects agent models through a shared Bridge and separate interfaces under a shared latent-communication protocol. After agent model replacement, LatBridge reuses unchanged interfaces, selects matching low-rank interfaces, and combines them through the Bridge, training only missing ones with all models frozen. The Bridge processes source representations in the basic mode and constructs target input without autoregressive generation in the accelerated mode. Experiments support effective communication after model replacement, with mean basic-mode accuracies of 14.8% on MATH and 27.3% on ALFWorld next-action prediction across eight small-model configurations. Analyses examine the factors supporting task accuracy and communication efficiency.

### 22. The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-19T13:56:49+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2610.26433
- Summary: We study whether geometric relationships between conversation turns, memory texts, and queries can predict answer correctness before generation. We evaluate four memory implementations with dense or hybrid retrieval and one observation-summary comparator. We embed these texts in a shared space. A logistic classifier uses 25 features describing query proximity, memory-conversation correspondence, and conversation structure. On LongMemEval-small, pooled AUROC is 0.640 over 2,367 question-system pairs, below a question-difficulty baseline of 0.655. Performance varies by question type: geometry reaches 0.841 on single-session-assistant questions, but system identity alone reaches 0.826. After controlling for difficulty and identity, geometry adds no statistically established pooled improvement (delta = +0.002, 95% CI [-0.010, 0.014]). A fixed-store context-selection experiment finds higher accuracy with proximity-ranked memories than with random subsets, consistent with ordinary retrieval relevance. On LoCoMo, nearest-turn similarity has modest predictive value for single-hop questions and near-chance estimates for several other categories. Training uses correctness labels; prediction uses pre-answer features and no additional LLM generation call. The results characterize associations between memory representations and correctness, rather than establish a reliable deployment diagnostic. In particular, embedding proximity does not verify fact coverage or distinguish memory-construction, retrieval, and generation errors.

### 23. A GPU-Resident Pipeline for Multi-Robot 3D Inspection with Limited Perception
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-10-19T10:02:12+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2610.26106
- Summary: We present a complete, GPU-resident pipeline for multi-robot 3D inspection of underwater structures. Given a triangle mesh and a fleet of $K$ robots, each carrying a short-range, limited field-of-view camera, the pipeline computes 6-DOF trajectories that jointly cover a target fraction of the surface while minimizing a linearly interpolated makespan/total-cost objective. The joint problem is NP-hard, so we decompose it into five core stages - candidate viewpoint generation, visibility computation, set cover, min-max vehicle routing solved as a mixed integer program (MIP) with lifted Miller-Tucker-Zemlin subtour elimination, and priority-based multi-agent path finding with continuous-time inter-robot conflict checking - flanked by mesh loading and surface sampling as preprocessing and by trajectory smoothing as postprocessing. Our contributions are: an end-to-end GPU-accelerated integration of the five stages, with its kernel design documented; a GPU batch adaptation of Lien's $\varepsilon$-visibility with four custom CUDA kernels; a $β$-aware per-vehicle tour upper bound derived from the interpolated objective, supplementing the Desrochers-Laporte coefficient lift with forbidden-pair cuts; a 4D space-time extension of Zhou and Zeng's GPU parallel-frontier A*; and an experimental evaluation on 14 meshes (up to $7.2$M faces) that ablates the routing cuts and the parallel-frontier search, audits collision freedom and waypoint attainment \emph{after} trajectory smoothing, and measures the end-to-end gap against analytical and LP-relaxation lower bounds. Code and raw results are publicly available.

### 24. While Amazon blocks AI agents, Walmart rolls out the welcome mat
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-21T19:30:00+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/
- Summary: As Amazon blocks AI agents from shopping on its site, Walmart is taking the opposite approach, introducing new technology that lets AI agents make purchases on customers' behalf, with controls over spending and transaction approvals.

### 25. AI agent fixed the bug, but what else did it change?
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-21T16:03:32+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/
- Summary: No summary.

### 26. Using thousands of AI agents to uncover new leads in biological data
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-21T13:37:00+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://openai.com/index/scaling-ai-research-for-complex-biological-data/
- Summary: No summary.

### 27. hvantk: an agentic multi-omics framework for variant annotation and analysis
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-21T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.19.760196
- Summary: Large-scale genetic variant analysis involves multiple computational steps, data formats, gene and variant annotation sources and compute requirements. Some of the steps like joint calling for large cohorts are run on large compute clusters, while gene/variant classification algorithms can be run in a desktop computer. At the same time, variant annotations such as gene expression and gene constraints metrics from gnomAD are provided in different formats, by resources that frequently change their versions. Here, we present hvantk, a framework that provides a common data model for large-scale annotation and analysis of genetic variants, by extending popular data formats such as Hail MatrixTable and AnnData. hvantk agentically integrates 21 public multi-omic data providers as plugins that a developer, bioinformatician or an AI agent can author without modifying the framework's core, drives analysis workflows using agent skills, and scales from single desktop computers to high-performance computing clusters. We used hvantk for reanalysing three case-control cohorts, comprising congenital heart disease (CHD), developmental and epileptic encephalopathy (Epi25) and schizophrenia (SCHEMA). Re-ranking of gene-based burden testing results using multi-omic annotations improved the recovery of curated disease genes from 26% to 49% in CHD, 40% to 48% in Epi25 and 51% to 54% in SCHEMA, among the top decile re-ranked genes. Expression at bulk and single-cell levels were the features contributing the most over a baseline of burden, gene constraint and publication count.

### 28. GENOAR: Global Engine for Navigating the Omnicell space via Agent-based Research
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-21T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.10.15.759380
- Summary: Although generative models have revolutionized many fields, including genomics, building a scalable dataset compatible with artificial intelligence (AI) is essential yet underexplored. Here, we developed a Global Engine for navigating the Omnicell space via Agent-based Research (GENOAR) that covers approximately 54 million cells for diverse downstream tasks using AI agents and parallel computing. GENOAR outperforms in three parts. Parallel computations accelerated the preprocessing of single-cell transcriptomic data; the other components enabled agent-assisted data storage and exploration for both AI models and humans. GENOAR involves two AI agents: an AI nomenclaturist ordered the unstructured labels of the single-cell transcriptomic profiles, and an AI librarian retrieved data. GENOAR presents transcriptomic profiles from more than 54 million cells from humans and mice in an analysis-ready format for humans and AI agents. AI agents in GENOAR exhibited successful retrieval performance compared with human experts. Using GENOAR, we elucidated progenitor cell-associated transcriptional signatures in native retinoblastoma and organoid environments. GENOAR was released and validated for the on-demand construction of single-cell atlases for metazoa. In conclusion, using GENOAR, the development of a single-cell transcriptomic atlas compatible with both AI systems and human researchers is feasible, scalable, and reproducible.

### 29. Searchtok
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-19T18:05:33+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/searchtok
- Summary: <p> Make TikTok and Instagram searchable for your AI agent </p> <p> <a href="https://www.producthunt.com/products/searchtok?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1285747?app_id=339">Link</a> </p>

### 30. Beam
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-10-06T00:17:47+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/beam-13
- Summary: <p> Highly efficient agentic 501B parameter open model </p> <p> <a href="https://www.producthunt.com/products/beam-13?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1271076?app_id=339">Link</a> </p>

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
