# Blindspot Signals Report - 2026-08-30

- Source export: `/opt/apps/haier/exports/evolution_signals_20260830_020503.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 502
- Deduped/weighted signal clusters: 484
- Novel vs previous reports: 5
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. THU MAIC / OpenMAIC
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-08-30T02:02:07.171759+00:00
- Primary source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/THU-MAIC/OpenMAIC
- Summary: Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click

### 2. Webinar | Accelerating Agentic AI: Securing Autonomous Workflows and Non-Human Identities - BankInfoSecurity
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-08-29T21:22:30+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMitAFBVV95cUxNbC1SUk5lMmxIbVhGSHdWU0VnX1FMVDAwOUJkRzJkRWgtMXNRSGpJRWx5WFlkNEVTQldkRU1aejhxMlhjOTVTUlg4TkhScHUzeWJaMUFXZFlGcEZsWVJtZ2pObUw2Z0RranZvZHJudmQySGtrR1hsbTk4TC0tNzktZl9TdWh5QVNnSDM3SmZzUlNPNjc2bXpJbUMxOFpzaTk0di1UZGRfME5WLXlyU0ZWaTB3WHY?oc=5
- Summary: Webinar | Accelerating Agentic AI: Securing Autonomous Workflows and Non-Human Identities&nbsp;&nbsp;BankInfoSecurity

### 3. workweave / router
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-08-30T02:02:07.171823+00:00
- Primary source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/workweave/router
- Summary: Model router for agentic systems. Routes every prompt to the right model in <50ms. Cut costs 40-70% with just an endpoint change.

### 4. How AI agents could spark the biggest currency boom in history - CoinDesk
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-08-29T15:00:00+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMi0gFBVV95cUxOMWtWYnhNX0ZEc1Q1R0xtSWxNaThXcGdXZGFja2JvOE5jaXVhM1VZWXpWY0ktbUN3Y3dtaC14cHp1Z0dlblE4dHFqQjJPQVEwWUNjakdEdEp2T2V2N2hUN1cyR3ZPSzJDcExrWUs2WFQtVjBodTdSc2x2RTVqRnY5MmFiWXFHZ19ERHVQbGZxSEZmcmo4WDVLRDhwSGNOcG5KUUx6RkwyMlFaUmp0R0ExWWg0MU96MHJjeUN4YXN5OEN1bHZIM09HZVN0aVp3LTZGY3c?oc=5
- Summary: How AI agents could spark the biggest currency boom in history&nbsp;&nbsp;CoinDesk

### 5. Show HN: Talos – An AI agent with a permission kernel between model and shell
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-08-28T12:25:39+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://talos-agent.ch/
- Summary: No summary.

## Top Signals By Weighted Score (including already-seen)

### 1. Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making
- Weighted score: 0.50
- Deep score: 0.5
- Date: 2026-07-19T02:51:41+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.17038
- Summary: This paper addresses key technical challenges in current large language model (LLM) agent applications, including long-horizon planning, sparse reward attribution, and dynamic environmental interaction, by designing and optimizing an intelligent agent workflow. The proposed architecture is based on the synthesis of core AI paradigms: Visual, Language, Generative, Graph, Multimodal, Reinforcement, and Agent Intelligence. Unlike conventional baseline models that rely on static prompting and lack robust perception-action loops, our approach introduces a Partially Observable Markov Decision Process (POMDP) routing mechanism. This mechanism is augmented with an internal, self-correcting reward model that evaluates decision trajectories before execution. By integrating multimodal inputs and advanced reinforcement learning principles (such as proximal policy optimization and value function approximation), the agent maintains long-term structural memory and dynamically adapts its reasoning pathways to mitigate error accumulation. Empirical experiments on the ALFWorld embodied simulation environment and the WebShop online navigation benchmark demonstrate a 24.5% absolute improvement in task success rate and trajectory efficiency over mainstream baselines like the standard ReAct framework. Comprehensive ablation studies confirm the significant contribution of the reward-driven critique module in suppressing hallucination rates. This research bridges theoretical foundations of reinforcement learning and graph-based memory with autonomous agent workflows. Ultimately, the resulting architecture offers a practical, scalable reference framework for developing artificial intelligence technologies in complex, multi-step autonomous systems. Code is available at https://github.com/01Amez/RLAW_Implementation.

### 2. MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-08-22T09:25:23+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.21867
- Summary: LLM agents are moving from single-prompt use to long task streams in which reusable memory becomes a core capability for terminal, software-engineering, and web tasks. Such memory is useful only when stored experience remains reliable across hundreds of interactions, but two failure modes break that assumption in practice. The first is unreliable admission: failed trajectories,accidental successes, and misleading observations enter memory because they appear relevant, then mislead later decisions. The second is memory drift: long-running banks accumulate duplicate, stale, and conflicting records that retrieval alone cannot repair. MemGuard's key distinction is to treat verifier output not as a one-shot filter, but as persistent lifecycle metadata. It converts multi-criteria score-token verification into reward, confidence, label, and uncertainty descriptors that are attached to every candidate before activation and reused during retrieval, conflict resolution, summarization, and archival. We evaluate MemGuard on Terminal-Bench 2.0, SWE-Bench Verified, WebArena, and Mind2Web across four backbones, comparing against four memory baselines plus a verifier-only control under matched runtime budgets. Averaged over five seeds, MemGuard achieves the best success metric and lowest average steps in all 16 backbone-benchmark settings, improving over ReasoningBank, the strongest prior baseline among the memory methods we evaluate, with a largest gain of 7.9 success-rate points on WebArena, 5.6 step-success-rate points on Mind2Web, and 2.4-3.5 points on terminal and software-engineering benchmarks. Code is available at https://github.com/whyyyyy123/MemGuard.

### 3. Multi-Agent System-driven Digital Twins for predictive maintenance: architectures, technologies and open research challenges
- Weighted score: 0.40
- Deep score: 0.4
- Date: 2026-07-24T00:09:53+00:00
- Primary source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.21873
- Summary: Digital twins have emerged as a foundational technology within the context of Industry 4.0, offering a paradigm for the real-time virtual representation of physical systems. However, managing their growing complexity, particularly in distributed industrial environments, requires intelligent architectures capable of autonomous decision-making, dynamic adaptability, and inter-agent coordination. This systematic review explores the intersection between Multi-Agent Systems and Digital Twins, with a particular focus on predictive maintenance applications in resource-constrained contexts. Through a critical analysis of over 547 papers published in high-impact journals (IEEE Transactions, Nature, Elsevier, MDPI), we establish a taxonomy of existing hybrid architectures, identify persistent technological bottlenecks, and formulate three open research questions concerning: (i) the deployment of artificial intelligence on resource-constrained microcontrollers, (ii) distributed multi-node coordination via lightweight communication protocols, and (iii) the hierarchical orchestration of Digital Twins toward smart factory control integrating residual life estimation and explainable Artificial Intelligence. The results of this analysis reveal that, despite significant progress, no existing system offers an integrated embedded-distributed hierarchical solution that simultaneously meets the requirements of Industry 5.0.

### 4. Autonomous AI Agents and the 2026 Hugging Face Attack - quasa.io
- Weighted score: 0.40
- Deep score: 0.1
- Coverage: 5 sources (google_news, BleepingComputer, Help Net Security, Security Affairs, CyberSecurityNews)
- Date: 2026-07-25T19:54:00+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMijAFBVV95cUxPcUsxQy1yNnk2QWtmdFZ0QTRQWHNQRE5xdGxKSzc1ZUxYQ0RnNmpuYmxwck9WTUZOZElMcldQMks4aVdwaW1GZzdvdUV2VVVXaHBYdWozMllwN1dSaDRrSnpJdVpZMjc2NlltbFpyODlDY0FSOEFjbDZTQVJ2UEUwM1ZBYzR3c09MbnItaw?oc=5
  - Alt: https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcUMybWdla01CZEhudnl5R0xXekFRT1I3QnNaRFBvNUM0dE9LbWQwS01VVW1NYnNwTG15ZzgzQWszSld1VWoyeTNDVC1MNjlMUWJNZnJSREpIT2V6RWVFWDRsVVloN0FoUWRqT19UeHpsM3VURXp5TXl1dkY3cDBvLVpCa0xJT21wQUxVbHFwM196MDJTRnBnd00wXzh6YVZaZFNZOXNPVHRydUtxY1VMM3cwY24xWWVTdjE1TE1ocFNvQdIBxwFBVV95cUxQcVpWSC01YWEtX2Q1QU5XMWJ0Mzc5Wko1MGdyejkzRDhkOHM3MFg4M0drQ2dWMElNOUtGaUlzLUJmSFVaNkJSN3JlcUR5NkVnMGRJZHl4U1BhSUtCaEVEN3JpWncydWxmWk9CSmJRLU1OLU9ESWRwM25FLXR2Z2h0LU0ta2lLdzhTV0Y0MmdxcVJNem9ZSjhIb0pfZGhhcEF3Q0EzNE00VEtvS0w2VHNPTlBGY2l6bWxqWnJ0b0w5ZmNieXpyVVRV?oc=5
  - Alt: https://news.google.com/rss/articles/CBMikgFBVV95cUxOQndJekJMOEtRYUhlNHNlbUNoNFF1SkVuYUFjTXhiQkVnemMzWlQzSjJnZldzV3lUQlNybldPWEhGVWlUNldhT19JTXhLczdzakFiOTE1X0xnakQtRWIySHlhODltSEZMZmJ4OW8yczVJN050MXZScnBEZ21FcGdKTVRxbG8ySVBGM2NzNFZaZ29OQQ?oc=5
  - Alt: https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSmdiUHRZZmQ1U2xaWnJKdmVYTzVxRWJZb2k5amJtY2xQaXJNT1VQOGRVaU1vOENQby1sbTQ3bDNUMVVvcGNIT2poT0NoejhUSnRSWTVCMmxUTU5LQTJFX0wzMjdQSVlEVG8wdzQ3QUJaMWNPZDRaeEU0YU1TV01lenozU0FXRERHZ21TcnNyVGU4UHk4eUJmbU9ncElfdmlGZVBfSnlqNkF1N2hrem5JdG5MSGJTTG9YVnp0aDdlNFFyMzDSAcgBQVVfeXFMTWxSVmlyNFdDZFM0YWhCdFBaUG5SNWY0VWtYTWRxMkw3UFI5Q1ZKdXI5bFozbkFUSU13Z0R5TFlNcm9RWG0xSWJOaFE1OXNuT0xic05PVWU4MkNfTEh3cVRqTjF5dHJLMjBGX21EVkh0cm01elFub3NhQks0a0l6eGtGVnRyb0RXVFRVS0tKWEZ3NkQ2LWlzTHpDR282Zmlsc1ZrWVF6aG9lbGxqeGhMcVhBUGlnZDJlS1YzbzZBby0zQVdWRDFhR2U?oc=5
- Summary: Autonomous AI Agents and the 2026 Hugging Face Attack&nbsp;&nbsp;quasa.io

### 5. Candidate supply and answer selection shape the value of LLM judging in multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-26T15:52:20+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2608.25937
- Summary: Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. We conceptualize multi-agent reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal selection, wherein consensus without quality control can exhibit patterns of memetic drift. We study two questions: (1) when an LLM judge provides effective selection pressure by supplying a signal of answer correctness for candidates generated in a multi-agent system, and (2) when using that signal improves the reported answer. To map judge reliability, we analysed 15,336 questions from MMLU-Pro, GPQA, MedXpertQA and MuSR, with Humanity's Last Exam analysed separately. To test these rules, we replayed 81,390 fixed candidate pools drawn from 16,278 questions across five benchmarks. We report three findings. (1) A correct answer is often already present among the generated candidates, but the system can still converge on and report a wrong answer. (2) Judge reliability is not a fixed trait of the model, but varies with the task, the generator and how rare the correct answer is. (3) Combining answer frequency with the judge's evaluation changed only the final answer-selection rule and raised accuracy from 63.82% to 70.82-70.95%, primarily by rescuing correct answers that were outnumbered by popular errors. In the systems studied here, the value of generating more candidates depends on whether those extra samples make correct answers present, frequent or recognisable. By isolating generation, recognition and selection, these findings establish a diagnostic basis for designing multi-agent architectures that protect generated correct answers from being lost.

### 6. Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-24T11:55:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.23152
- Summary: Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, stereotype, conspiracy, dehumanizing, non-factual), and then maps it to a targeted counterspeech style. To facilitate FIRE, we curate FactualCS, a novel dataset of $4,784$ instances that provides the annotations regarding hate categories, reasoning traces, and evidence mappings, which are critical elements for grounded generation that are missing in prior work. A comprehensive evaluation across $28$ baseline configurations demonstrates that FIRE significantly surpasses existing methods, despite using compact agents ($<$2B). FIRE achieves a $\sim$ $12 \%$ and $\sim$ $11 \%$ improvements in factual and category-specific accuracy respectively, while simultaneously reducing toxicity by $\sim$ $11 \%$ relative to the strongest baselines. Further human evaluation confirms that responses generated by FIRE are significantly preferred over the strongest baselines, underscoring its effectiveness for real-world deployment. These findings show that decomposing the underlying intent of hate speech is essential for generating safe, effective, and contextually precise counterspeech.

### 7. AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-23T01:22:09+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.22160
- Summary: Physical automation is scaling toward fleets of embodied machines commanded by an AI brain. Early deployments already run factories and warehouses at production rates beyond any human line, and their adoption is accelerating. But when their joint decisions cause harm, everyone involved has reason to blame everyone else, the machine vendor, the algorithm provider, the factory operator, the insurer, and the regulator, and no method can divide the responsibility between them. Existing methods read logs whose origin they cannot verify and name a single culprit, misrepresenting outcomes that are overdetermined, preempted, or caused by an omission. We present \audita{}, an audit layer pairing a tamper-evident record of every inter-agent command with a certified, graded causal-attribution engine. We prove its verdict cannot be gamed: a rule-following agent can never be made to look guilty, an attempt to shift blame is itself caught and graded, and we establish the exact limit of what an evidence-based auditor can certify. On live language-model pipelines it reduces the standard judge baseline's responsibility error roughly threefold; on a benchmark of accident-grounded structures it recovers responsibility where single-culprit baselines fail, and stays invariant under forgery. \audita{} turns the question of who is to blame from an argument about logs into a calculation over evidence.

### 8. Ludi${}_{\scriptscriptstyle 0.1}$: An Agentic System for Socially Intelligent Robots
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-22T16:38:59+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics, neural interfaces / robotics
- URL: https://arxiv.org/abs/2608.22035
- Summary: Robot foundation models have substantially advanced perception and control, but natural human-robot collaboration requires more than executing isolated commands. A robot must recognize ambiguity, maintain context across turns, communicate its intentions, and revise ongoing behavior as the user's intent changes. We present $\scriptstyle\mathsf{Ludi}_{\scriptscriptstyle 0.1}$, an agentic system for socially intelligent robots that integrates interactive speech, multimodal reasoning, memory, navigation, and learned manipulation. Its decision-making core is a fine-tuned vision-language model trained on multi-turn interaction traces spanning ambiguous requests, clarifications, corrections, interruptions, mixed social and task dialogue, and multi-step tasks. A purpose-built harness manages the model-tool interaction loop, while specialized navigation and manipulation policies execute physical skills. Ludi${}_{\scriptscriptstyle 0.1}$ demonstrates a practical path toward fluid human-robot collaboration today while producing the multimodal interaction traces needed to develop a more deeply integrated foundation model for robots and people.

### 9. OmniScientist: An Omni-Modal Omni-Discipline AI Scientist
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-13T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2608.13558
- Summary: Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the agent. We introduce OmniScientist, an end-to-end, omni-modal AI scientist that conducts multidisciplinary research directly from heterogeneous raw evidence. A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. By running idea, rigour, and claim checks in code, the system enforces novelty screening, statistical validity, execution provenance, and numerical traceability. We evaluate OmniScientist on 36 real-data cases spanning 5 discipline families, 4 families of scientific evidence, and modalities including images, signals, audio, video, 3-D structures, trajectories, tables, formulae, and graphs. The system completes the full path from raw data to a compiled manuscript in all 36 cases and achieves a mean overall paper score of 6.3 with the reference reasoning backbone. In paired comparisons against a blind variant that receives only precomputed scalar features, direct perception improves all 7 evaluation dimensions and wins 85% of head-to-head judgments. These results show that lifecycle-wide perception is essential for evidence-grounded scientific discovery and provides a practical path toward broadly capable AI scientists.

### 10. Human-supervised Agentic AI for Hypothesis Generation and Experimental Assistance in Drug Repurposing
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-08-13T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.04.20.719538
- Summary: Computational drug repurposing has largely been focused on rapid hypothesis generation, yet real-world applications span a far broader lifecycle, from drug candidate suggestion to designing experiments, analyzing assay data, and iteratively refining candidates. Here, we demonstrate that agentic AI can operate throughout this lifecycle. To this end, we developed RepurAgent, a hierarchical multi-agent AI system comprising a supervisor agent and a planning agent that coordinate four specialized sub-agents (research, prediction, data, and report), through a human-in-the-loop design, with episodic memory and retrieval-augmented generation. The system is grounded in data, tools, and standard operating procedures specific for drug repurposing, developed within the REMEDi4ALL consortium. We validated the agentic system across three scenarios spanning the various stages within the repurposing lifecycle: in Acute Myeloid Leukemia, a blinded expert evaluation indicated that RepurAgent produced substantially more novel and mechanistically credible candidates compared to a vanilla LLM baseline; in a retrospective COVID-19 antiviral screen, RepurAgent acted as an adaptive experimental collaborator, prioritizing compounds with AUC-ROC up to 0.99 without predefined thresholds and flagging confounders missed in manual review; and for Multiple Sulfatase Deficiency, it prioritized 81 high-confidence candidates from 5000 compounds, which were further corroborated by domain experts. These results demonstrate that agentic AI can support across the drug repurposing lifecycle, from hypothesis generation to experimental analysis. RepurAgent is open source and deployed at https://repuragent.serve.scilifelab.se/.

### 11. MemHarness: Memory Is Reconstructed, Not Replayed
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-30T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2607.28272
- Summary: Retrieving past experiences has become a common strategy to enhance large language model agents. However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injecting them into the context regardless of whether they align with the agent's current situation. This ``replay'' paradigm ignores the gap between the abstract, general nature of stored experience and the concrete, ever-changing states encountered at decision time, frequently causing negative transfer. In contrast, humans rarely recall past experiences verbatim; instead, they reorganize and adapt retrieved memories to fit the present context. Inspired by this, we propose MemHarness, a framework that equips LLM agents to actively harness and reconstruct past experiences based on the present context. At each decision step, a unified policy model critiques and reconstructs the retrieved experience conditioned on the current state, producing context-grounded guidance before acting. This reconstructive ability emerges naturally through end-to-end training with GRPO. Experiments on ALFWorld and WebShop show that MemHarness substantially outperforms pure RL and static memory-augmented baselines, demonstrating strong robustness in out-of-distribution (OOD) scenarios. Furthermore, our analyses reveal that this reconstruction objective not only prevents negative transfer but also serves as latent guidance during training, fundamentally improving the agent's intrinsic reasoning capabilities.

### 12. Manifold Agentic Reasoning: Extending Agentic POMDPs and Post-Training Reasoning to Riemannian State and Reasoning Spaces
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-29T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.26.740848
- Summary: Agentic reasoning systems increasingly interact with environments whose states are only partially observed, dynamically evolving, and constrained by physical, biological, or logical structure. Existing agentic reasoning frameworks often model internal reasoning, tool use, and post-training adaptation using flat latent representations and struggle in curved manifold space environments. However, many scientific and embodied domains naturally lie on curved state spaces, including tissue geometry, developmental trajectories, protein conformations, robotic configuration spaces, and constrained physical systems. We introduce Manifold Agentic Reasoning, a geometric framework that extends agentic reasoning from Euclidean latent spaces to Riemannian manifolds. In the proposed framework, observations are encoded as manifold-valued states, memory is retrieved by geodesic similarity, candidate hypotheses are generated in tangent spaces, predicted transitions are projected by exponential maps, and decisions are admitted through verification-gated commitment or repaired by manifold self-correction. We further extend the framework to graph-agentic manifold reasoning, where node states live on manifolds and neighbor information is transported by logarithmic maps before attention-based aggregation. Manifold agent reasoning moves AI past brittle, prompt-chained templates to solve four critical production flaws: silent hallucinations and reasoning drift, brittle tool and context misuse, the black-box evaluation problem and stiff behavior profiles. To evaluate the framework, we introduce a Curved Tissue Manipulation and Recovery benchmark in which an agent must repair damaged tissue on a curved manifold. Simulated results show that the full manifold-agent substantially outperforms both a baseline reasoning agent and a full flat-agent reasoning system, achieving higher recovery success, lower geodesic shape error, lower pattern error, and fewer invalid transitions. Curvature and …

### 13. Show HN: Ami – A local, open-source agent that does your busywork across apps
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-27T22:55:33+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/NanoNets/ami
- Summary: Hey everybody, sharing Ami on HN today.<p>Ami is an open source, local-first agent harness that acts as your shadow worker and copilot chat. It ships with a graph memory.<p>Here&#x27;s what Ami does on its own -<p>- connects to apps, data, repositories, tools with your personal tokens<p>- Learns how you do tasks (execution style, decisions, anti-patterns)<p>- Learns how you communicate (external and internal)<p>- maintains a universal to-do list<p>Here&#x27;s how you use Ami -<p>1. You can execute busywork. It fetches and executes tasks autonomously in your style, asks approval before risky actions, gives deliverables, drafts replies &#x2F; emails &#x2F; ticket updates.<p>2. You can execute copilot chats. Use it to ask questions, fire off ad-hoc tasks, create to-dos, update memory.<p>Ami was built for internal use. My team found it useful, so we wanted to share it here. It&#x27;s still in development stage, and we might push a more stable release soon. It constructs a context graph memory of you, with entities, relationships, feedbacks, decisions, writing styles maintained in memory so it can get more autonomous the more you use it.<p>Few examples where Ami helped me this week -<p>1. fetched a bug report from slack, created fix PR autonomously which I merged, verified fix is working.<p>2. debugged a traffic spike on our new blog.<p>3. turned a sales POC into an order form draft using recently signed forms.<p>4. nailed down metrics definitions from notion and created a dashboard.<p>5. closed out my day by auto-updating Linear tickets based on slack activity.<p>Any feedback is most welcome.

### 14. Systematic Literature Reviews With Two Multi-Agentic Systems And Human-In-The-Loop
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-24T02:52:07+00:00
- Primary source: arxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://arxiv.org/abs/2607.21920
- Summary: Systematic literature review of clinical trials drives regulatory decision-making, but conventional screening and extraction are time-consuming, labor-intensive, and vulnerable to study selection bias. We propose two fit-to-purpose multi-agentic systems (MAS) for systematic literature review, with human-in-the-loop. The screening MAS uses multiple LLM agents with heterogeneous personas and multiround cross-review, and uniformly improves accuracy over a single-LLM baseline. The extraction MAS combines standardization, an iterative correction loop, and retrieval-based context control to ensure accuracy and scalability. Both MAS are specifically designed to support Human-In-The-Loop which is essential for clinical decisions. The novelty of the proposed approach lies in the system architecture rather than in any single foundation tools: the system can naturally benefit from future improvements in the underlying tools, for instance, stronger LLM agents, retrieval engines, image recognition methods, etc. As a real-world application, a published network meta-analysis is reproduced by the MAS. The result recovers all trials from the original study and identifies additional eligible trials missed by manual review, leading to updated clinical conclusions.

### 15. StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-24T00:00:00+00:00
- Primary source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2607.22798
- Summary: Computer-use agents are usually improved by strengthening perception: better models for reading a screenshot and choosing where to click. Yet a screenshot is only a lossy rendering of the underlying program state, e.g., the files, application backends, and DOM that hold the task data. Different states can produce the same pixels, while code can inspect and modify that state directly. StateAct is a code-first, multi-agent harness built around this distinction. Its main agent works directly with program state by using code, while a dedicated GUI subagent handles screenshot-and-click interaction on the few subgoals that need it, just 28 of 108 tasks and 1.1% of main-agent steps. The same direct access to program state also supports verification: an independent finish gate double-checks the saved result for structural failures, e.g., output that is missing, unsaved, or written to the wrong path. To stay on track over hundreds of steps, the main agent hands subgoals to fresh subagents, keeping its own context focused. On OSWorld 2.0, StateAct lifts Claude Opus 4.8 from 20.6% to 26.9% on binary success, and from 54.8% to 61.6% on partial success, at ~ 9x lower cost per task than the same model driven by screenshots alone; a code-only variant with no GUI subagent reaches only 45.9% partial, below that screenshot-based baseline's 54.8%. In general, grounding action, verification, and memory in state, what we call state-grounding, shifts the main bottleneck from perception toward reasoning: failures depend more on what the agent thinks than on what it sees.

### 16. AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-23T09:35:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.21106
- Summary: Effective memory is crucial for LLM agents, yet constructing it effectively remains challenging. A memory-construction policy decides what information to extract, store, update, compress, or discard as interactions accumulate. Heuristic memory methods rely on subjective, task-specific rules, which can misalign with downstream objectives and limit cross-task adaptability. RL-based methods, by contrast, learn from task feedback but mainly use outcome- or module-level rewards. These coarse signals indicate task success but cannot identify which intermediate memory contents support the final answer, creating a fine-grained credit-assignment bottleneck. However, constructing such process feedback is prohibitively difficult because intermediate memory decisions lack unique ground-truth targets, while the appropriate credit varies with the agent's uncertain reasoning trajectory and therefore cannot be specified in advance. We propose AttriMem, an attribution-guided process-feedback framework for learning memory-construction policies with RL. AttriMem augments the global outcome reward with local rewards derived from token-level contributions to the final answer. Experiments on long-horizon dialogue question answering show that AttriMem outperforms retrieval-based, heuristic, and RL-based baselines, generalizes across benchmarks and answer models, stabilizes RL optimization.

### 17. Supra Cognitive Modes: A Routed Architecture for Agent Memory
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-21T13:37:17+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.19096
- Summary: Agent-memory workloads mix direct factual lookup, relation-chain and current-state reasoning, and broad synthesis over long histories. We describe Supra Cognitive Modes (SCM), an architecture that maps explicit or automatically selected per-query modes to retrieval and synthesis payloads over one shared ingest substrate. A frozen semantic classifier and runtime gates dispatch queries among fused lexical and dense lookup, graph or iterative multi-hop handling, and stratified long-form synthesis. The substrate combines multi-granularity embeddings, extracted triples, fact-version metadata, and optional asynchronous enrichments. We characterize the deployed configuration on three benchmarks: Long-term Conversational Memory (LoCoMo; n = 1,986), MemoryAgentBench (MAB; n = 3,671), and LongMemEval (n = 500). The reference run records 84.87% on LoCoMo factoid categories and 68.61% on adversarial abstention, 61.49% on MAB across two repetitions, and 86.00% on LongMemEval. A repository-backed reproduction produces similar aggregate scores and supports task- and mode-conditioned failure analysis. Raw baseline outputs, aligned end-to-end timing for LoCoMo and LongMemEval, and complete token ledgers are unavailable; stored rows also omit some final runtime decisions. The results characterize one implemented routed configuration and its diagnostic failure patterns, while source inspection verifies the per-query control interface and shared-substrate design. Causal routing effects, efficiency gains, and statistical significance remain outside the available evidence.

### 18. RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-20T15:27:13+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.18060
- Summary: Long-horizon robotic tasks require diverse capabilities that no single policy can reliably provide. Heterogeneous policies offer complementary strengths, but orchestrating them requires reasoning over uncertain capability boundaries and cross-policy distribution mismatch, which are largely overlooked by existing planning methods built on homogeneous, predefined skills with fixed applicability. We propose RoboHarness, a unified framework that encapsulates independently developed robot control systems as reusable agentic skills. Although instantiated in this work with VLAs, RL policies, and task-and-motion planning (TAMP) systems, RoboHarness is designed as a general framework compatible with a broader range of robot policies, such as navigation policies, model predictive controllers, and world-action models. RoboHarness uses multi-modal execution memory and online evidence to characterize policy capability boundaries for capability-aware decomposition and routing. To stabilize policy handoffs, its Memory Bridge retrieves execution trajectories associated with the next policy, estimates its in-distribution state region, and guides the robot toward that region without joint policy retraining. Extensive experiments on three public benchmarks, 500 customized tasks, and 135 real-robot experiments demonstrate effective capability-aware routing and stable policy orchestration, yielding substantial improvements in zero-shot long-horizon planning and out-of-distribution robustness.

### 19. RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-18T09:11:22+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.16716
- Summary: Large language models and LLM-based agents are widely used as personal chat assistants, enterprise copilots, and autonomous workflow agents. In all these applications, memory (the ability to retain, access, and reason over information accumulated over long contexts and multiple interactions) plays a crucial role in determining the reliability of any agent. We introduce RECON (Reasoning over Extended Contexts with Obfuscated Narratives), a benchmark for evaluating compositional reasoning over long contexts. RECON spans 24 case files across three domains (criminal, medical, and financial), each ranging from 50k to 100k tokens, and tests agents on six memory intensive tasks: reconstructing multi-hop evidence chains, propagating cascading invalidations, resolving source conflicts, counterfactual reasoning, satisfying temporal constraints, and temporal fact retrieval. Recent memory benchmarks evaluate whether agents can retrieve scattered facts or detect if a fact has changed whereas RECON evaluates what happens after the change, whether agents can trace which downstream conclusions are affected, which survive through independent support, and how alternative timelines would have unfolded. Our evaluation reveals substantial limitations across current architectures: even the strongest non-Oracle system reaches only 22.4% Accuracy, with retrieval and reasoning each surfacing as challenges.

### 20. MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-14T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.05.11.723319
- Summary: Constraint-based metabolic modeling is a powerful way to study the mechanistic basis of cellular states and disease, but its effective use demands substantial computational expertise and careful coordination of multi-step analyses. We developed MechAInistic to lower this barrier and enable researchers to ask complex biological questions in natural language. Harnessing large language models, MechAInistic is a multi-agent system organized around an Architect-Reviewer pattern that transforms a natural-language question into an executable, model-grounded workflow and generates a structured report. The system supports a variety of tasks, including pathway comparison, perturbation analysis, drug-target exploration, and literature-grounded interpretation across paired metabolic model states. We tested MechAInistic on two drug-repurposing use cases. For Naive B cells from Rheumatoid Arthritis (RA) paired with healthy controls, the system quantified the metabolic rewiring driving disease, prioritized candidate reactions using topological hub filtering and robustness analysis, and surfaced Devimistat as a potential repurposing candidate acting through 2-oxoglutarate dehydrogenase in the TCA cycle. In a paired CD4+ Th17 cell study from Multiple Sclerosis (MS) and healthy controls, the same workflow identified NADP-dependent isocitrate dehydrogenase as the optimal single target and proposed ivosidenib as an FDA-approved repurposing candidate. Together, these results show that MechAInistic interfaces directly with mechanistic modeling and turns large language model reasoning into reproducible biological discovery. MechAInistic is accessible at https://mechainistic.dtih.org.

### 21. EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery
- Weighted score: 0.30
- Deep score: 0.3
- Date: 2026-07-13T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.08.737358
- Summary: Motivation: As biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers. Result: EcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAI's multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimer's Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

### 22. Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-08-28T17:01:12+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.23691
- Summary: No summary.

### 23. Risks and Controls for Multi-Agent Systems: an analytical framework for deployment of AI agents across organisational boundaries
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-08-27T05:28:06+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.26626
- Summary: This report presents a framework to help organisations, policymakers and researchers reason about the risks that emerge when AI agents interact with each other, how those risks change as interactions cross organisational boundaries, and the controls that may help address them. As organisations deploy AI agents, those agents will increasingly interact with each other: inside the organisation, with the agents of partners, customers and suppliers, and with unknown counterparties on the open internet. Failures can emerge from the interactions themselves, and once those interactions cross an organisation's perimeter, no single organisation can fully see, control or govern them. The report introduces three deployment tiers, defined by the minimum common governance binding any two interacting agents: singular governance, where one organisation governs every agent; federated governance, where multiple organisations deploy into a shared environment under agreed rules; and open environments, where agents operate with no central authority and shared standards are adopted voluntarily if at all. Within each tier, the report examines risk factors, failure modes and available controls. It identifies who is positioned to apply the controls, and where no actor is positioned to act, it characterises the gap and the collective action required to close it.

### 24. When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-08-26T09:04:21+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.25553
- Summary: An agent that inherits a consolidated memory may inherit a constraint that was true when written and has since been withdrawn by a newer authoritative record. Under a scarce verification budget, does the agent recover the withdrawal, and if not, is the resulting stale-consistent decision avoidable without spending more? We model supersession explicitly -- provenance is immutable; what changes is which record is current -- and assign by design the memory's form, the world's state and the verification policy at a fixed budget of two records: the agent's own allocation, or the same budget with one slot re-assigned to the critical provenance path or to a random record. With a constraint stated, agents inspected its provenance path in about one episode in five; when that constraint had been superseded, native allocation produced stale-consistent decisions in 77.3%, 74.7% and 74.7% of episodes across a primary run, a fresh-wording replication and a held-out domain. Re-assigning one slot to the critical path raised current-record-consistent decisions by +74.0, +72.7 and +61.3 points, positive in six of six models in each run, and left an already near-ceiling rate unchanged when the record agreed with the memory. The held-out scenario was later found to contain a temporal inconsistency; a robustness replication with one sentence corrected, deposited externally before execution, gave +73.3 points (positive in 5 of six models, the sixth at a native missed-path rate of zero) and is reported alongside the original. The intervention uses knowledge of the critical path and is not a scheduler; it quantifies how much of the stale-consistent decision rate the bundled same-budget policy removes: the effect approaches the native missed-path rate in the primary, replication and corrected held-out runs. Memory systems may need freshness or supersession signals separate from relevance.

### 25. Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-08-26T03:24:52+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.25329
- Summary: Memory-augmented agents maintain compact user profiles throughout extended conversations, enabling personalized and consistent responses without the need to process the entire dialogue history. The quality of these user profiles relies on the underlying memory management strategy: at each step, the agent must determine what to retain, compress, or discard. However, existing methods typically employ a static, one-size-fits-all strategy established before training. In practice, the optimal memory decision is inherently user-specific and dynamically evolves alongside policy optimization. To address this, we propose \textbf{HiPS} (\textbf{Hi}erarchical \textbf{P}ersonalized \textbf{S}trategy), a framework that decouples memory management into a globally shared foundation and a user-specific adaptive tier. Specifically, HiPS employs \textbf{Universal Strategy} to extract shared principles from cross-persona trajectories, alongside \textbf{Persona Delta Distillation} to generate tailored rules for users whose behaviors diverge from general patterns. \textbf{Cross-Level Rule Flow} dynamically calibrates their boundary by promoting broadly validated personal rules and demoting contradicted global ones. The architecture establishes a co-evolution loop where a mechanism guarantees that all strategy refinements are anchored to task outcomes. Extensive experiments demonstrate consistent improvements over memory-augmented baselines.

### 26. Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-08-24T13:56:01+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.23268
- Summary: Frontier multimodal large language models (MLLMs) deliver impressive perception yet still falter on scientific and mathematical reasoning. Parameter-level adaptation is unavailable for closed-weight or on-device backbones, and stateless prompting forfeits any compounding benefit from problems already solved. We propose \textbf{DG-Mem}, a dual-grained agentic memory framework that augments a frozen MLLM with a non-parametric, externally stored memory built once from training-time rollouts and consulted read-only at test time. Motivated by the Complementary Learning Systems (CLS) account of human memory, DG-Mem factors its store into an instance-grounded exemplar memory and a category-level schema memory of IF-THEN rules, with a transient reflection store mediating their construction so that schemas are synthesized only from abstract reflections, never from exemplar text. Two design choices distinguish DG-Mem: an online concept categorizer that grows the category space incrementally during training rather than committing to a predefined taxonomy, and a Shapley context attribution procedure that decomposes correctness across the entire retrieved rule set and yields a per-rule utility that re-weights retrieval at test time. The pipeline introduces no gradient updates and is deployable on closed-weight or on-device backbones. Across MathVista, MMMU, and MMMU-Pro on four open-weight and proprietary backbones (Qwen3.5-27B, Qwen3.5-122B-A10B, GPT-5-Nano, Gemini-3-Flash), DG-Mem improves consistently over no-memory and competitive memory baselines.

### 27. Nagaland University study contributes to strategic AI governance for ethical decision-making, organisational resilience - The Shillong Times
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-08-24T13:46:36+00:00
- Primary source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMi8AFBVV95cUxOMklJYU9ma2p1REp0eHE4SEQ5eDYwOHp4aE8xNFRFcmo5TTFhdDVjQU84OWl2X2FReEdMRlBKOWpib0tyUVd3Yk9JNTF5UmxteV9fZjJTNkJjLS1NY0ZjM1BvSnZDWThHaTY1ek5kUnRnZmVmNHpJRExiSHZsdmdMbWNjMzZEZ1Zxa3JMTVpQbklzY3pMZGg0TFd0dkxVaGdRNU5tbnNIRndDNDlxa3k0WW02SWxTQTVwQ241elphRTlwNXVjX0ZBeVNpV1M0RVBXd0RhbENEU1JWb3lzeWN4ZFp4bndycjJMeGxQSlNLd0M?oc=5
- Summary: Nagaland University study contributes to strategic AI governance for ethical decision-making, organisational resilience&nbsp;&nbsp;The Shillong Times

### 28. Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-08-23T23:35:31+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2608.22657
- Summary: Agentic AI frameworks interpret open-ended task goals and decompose them into multi-step plans. Richer information about embodiment-specific capabilities, physical preconditions, and cross-robot coordination improves grounding, but does not eliminate infeasible, mistimed, or unsafe physical actions. Physical robot crews therefore require an explicit architectural interface between semantic planning and execution, where every planned action is verified against robot capabilities, system state, and workflow constraints before actuation. This paper introduces Physical Agentic AI, a framework for skill-grounded robot agent orchestration, in which each robot exposes a typed library of executable skills while a foundation model planner decomposes a task into phases and assigns each phase to a robot-skill pair. A Robot Orchestration layer exposes the skill library, robot state, named locations, and workflow contracts to a non-actuating Mission Planner, while a deterministic Robot Orchestrator validates and authorizes one skill at a time. We evaluate on a drone-UGV search-and-dispatch mission, where every mission in every condition is executed live in Gazebo, and on a humanoid-quadruped transportation task using hardware-equivalent skill interfaces plus two physical trials on a Unitree G1 and Go2. Varying planner knowledge and runtime enforcement independently, we find that retrieval raises skill grounding from 51% to 96% yet leaves informed planners dispatching 23-29% of faulted steps. Per-dispatch enforcement reduces false dispatch to 0% with no false blocks, and a held-plan ablation confirms that the gate, not plan variation, is responsible. Live execution makes the difference physical: without enforcement all eight injected faults crossed the orchestration boundary and six produced robot motion; with enforcement all eight were refused before motion.

### 29. Fusing Perceptual Vision Experts with Multimodal Large Language Models for Explainable Plant Disease Diagnosis: From Benchmark Imagery to Real-World Robotic Field Validation
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-08-23T17:20:20+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2608.24934
- Summary: Accurate field plant disease diagnosis requires reliable fusion of uncertain and conflicting perceptual evidence. We present the Hybrid Hierarchical Multi-Agent Framework (H$^{2}$MAF), combining decision-level fusion of EfficientNet-B3 and ConvNeXt-Tiny with semantic arbitration by open-weight multimodal large language models (MLLMs), Gemma 4 E4B and Qwen3.5 4B, using structured JSON evidence to generate explainable diagnoses, risk levels, treatment urgency, and financial exposure. (H$^{2}$MAF) is evaluated on 14,364 images (1,370 test images) across PlantDoc (2,922 images, 27 classes) and two non-public, continuously captured Cornell robot-acquired field datasets: Stage 2 (20 GB; 4,215 images) and Stage 4 (40 GB; 7,227 images), covering Early Blight, Late Blight, and Septoria Leaf Spot under uncontrolled field conditions. On PlantDoc, Gemma improves accuracy from 63.9% to 68.5%, achieving +7.6 points on the 41.7% CNN-conflict subset. Cornell accuracies reach 99.3% and 98.9%, with only 1.7-4.1% disagreement, demonstrating conflict-dependent MLLM utility. The critical-risk error of gemma is 0.14-0.5 points, whereas Qwen overflags by 3.5-14.4 points. These results establish MLLM arbitration as a promising, yet calibration-dependent, approach for explainable agricultural AI and robotic field decision support. Github Link: https://github.com/Applied-AI-Research-Lab/Explainable-AI-Plant-Disease-Detection

### 30. HERO: Human-profile Enhanced Retrieval Optimization Framework for Long-term Agent Memory
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-08-23T09:19:34+00:00
- Primary source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2608.22310
- Summary: Long-term memory is crucial for personalized responses and long-horizon agent interactions. Existing methods often rely on LLMs to compress or rewrite dialogue histories and use the transformed memories as retrieval evidence. Despite the progress in organizing fragmented contexts, two major drawbacks persist: (1) information loss from compression, which discards fine-grained but later useful details, and (2) semantic drift from rewriting, which erodes the original tone and situated context. In this work, we propose a novel Human-profile Enhanced Retrieval Optimization framework for long-term agent memory (HERO). Specifically, HERO converts the dialogue history into a traceable heterogeneous memory graph that preserves raw dialogue text as evidence for reasoning, thereby mitigating information loss. For retrieval, HERO extracts initial anchors from the current query and incorporates human profiles via an iterative graph traversal; these anchors and profiles provide guidance signals that adaptively activate the most informative regions of the graph. Experiments on two benchmark datasets show that HERO outperforms strong baselines on both factual and personalized reasoning, while providing more faithful access to raw dialogue evidence.
