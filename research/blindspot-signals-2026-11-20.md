# Blindspot Signals Report - 2026-11-20

- Source export: `/opt/apps/haier/exports/evolution_signals_20261120_020321.json`
- Total signals in export: 5000
- Agent-relevant raw signals: 625
- Deduped/weighted signal clusters: 594
- Novel vs previous reports: 25
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`
- Deduping: same-event headlines across multiple sources are clustered once; source coverage boosts weighted score.

## New Signals Since Previous Reports

### 1. Accurate and interpretable protein complex stoichiometry prediction through agentic AI with StoiAgent
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-18T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.17.767325
- Summary: Accurate protein complex structure modeling requires knowledge of complex stoichiometry, yet the copy numbers of individual subunits are often unknown. Consequently, predicting protein complex stoichiometry has emerged as a major challenge in recent years. Here, we present StoiAgent, a large language model (LLM)-powered AI agent that automates the retrieval and integration of sequence, structural, and literature evidence to predict stoichiometry while preserving interpretable reasoning traces (chain of thoughts) of its evidence assessment and ranking decision. An open-weight LLM model, Qwen3.6-27B, is used by StoiAgent as the LLM backbone to combine sequences, structural templates, AlphaFold3 structure predictions, and literature evidence, and perform stoichiometry candidate generation and ranking. On 56 CASP17 protein complex targets, it achieves top-1 accuracy of 75.0%, which represents a 23.2 percentage-point improvement over PreStoi with AlphaFold3 ranking (51.8%) and matches the top-1 accuracy of StoPred. Moreover, StoiAgent has a higher top-3 and top-5 accuracy than StoPred (85.7% versus 80.4% and 87.5% versus 85.7%, respectively). Furthermore, it outperforms general-purpose frontier LLMs, including ChatGPT and Gemini, in stoichiometry prediction. Case studies further illustrate how StoiAgent evaluates competing assembly hypotheses by integrating complementary evidence, with recorded reasoning traces documenting its decision-making process. Overall, StoiAgent demonstrates the potential of LLM-powered AI agents to improve protein complex stoichiometry prediction through the automated integration of diverse sources of evidence while providing interpretable explanations to guide downstream structure modeling.

### 2. SPIDER: Contextualizing Biomedical Knowledge for Evidence-Grounded Scientific Reasoning
- Weighted score: 0.20
- Deep score: 0.2
- Date: 2026-11-18T00:00:00+00:00
- Primary source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.11.11.765839
- Summary: Aggregated relations in biomedical knowledge graphs can obscure evidence and study conditions, complicating the distinction between scientific disagreement and contextual differences. Here we introduce SPIDER, a multi-agent framework grounding biomedical relations in literature evidence and extracting study conditions for interpretation. Applied to a graph integrating 48 databases and ontologies, SPIDER analyzed 1.95 million PubMed abstracts, adding 2.31 million previously unrepresented, literature-supported entity pairs to construct SPIDER-KG. Daily updates incorporate relations and evidence from newly indexed PubMed records. Across 89,937 evidence-supported comparisons of potentially incompatible relations, SPIDER classified 79.0% as contextual differences, and 6.1% as genuine disagreement, achieving 80.3% macro-F1 averaged across both categories against expert annotations. On SPIDER-Bench and four biomedical reasoning benchmarks, SPIDER-KG improved large language models' interpretation of evidence-supported biomedical relationships. Retrospective analysis of newly reported gene--disease relationships further demonstrated how evidence-linked knowledge can contextualize emerging discoveries. SPIDER-KG provides a reusable, incrementally extensible evidence layer for biomedical reasoning.

### 3. Report: Apple job listings detail plans for autonomous AI agents - 9to5Mac
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-19T22:21:00+00:00
- Primary source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMimwFBVV95cUxNNWJ3VnhPQ0NGd0w0SUxVbGhZT0VGMkFua1A4SnF1TEZwT21TMW1KTUkydWpzODRUdkM1cTgwTTZhaFhqYW93eWpOeWFMZmZMdDhWYUdOUkdGNDRCQ3V4RmxMVkcyWWxDMXhOREpvV19oMUFBbzRwd1gxUWt6c1poYTQwQWxZOXV0SGlUQlhDWEpqbWJBMWFMQkFHYw?oc=5
- Summary: Report: Apple job listings detail plans for autonomous AI agents&nbsp;&nbsp;9to5Mac

### 4. From dialogue to delivery: making AI governance work in Southeast Asia - OECD AI Policy Observatory
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-19T14:24:10+00:00
- Primary source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMimAFBVV95cUxNVjBDSU9VUWFxTUt5YkVyZm9pSkFMWkFoWnpOTTFFcndTbTZ2Tmo5eWhOTzdYRTlLTklESnNuSTdNejhyNHlxM0ZCRFlJNlJjR2VEX3dtMDVYZVV2SWIyd01zZWc4Wmo0MzlLX2p4X1ZIUy1hQjk4OW5lU0NvbGV5S0hWZHM0VjVISUVTUGFTaHJQbjU2aE5SQQ?oc=5
- Summary: From dialogue to delivery: making AI governance work in Southeast Asia&nbsp;&nbsp;OECD AI Policy Observatory

### 5. UK insurers lag on AI governance, Sapiens study finds - IT Brief UK
- Weighted score: 0.10
- Deep score: 0.1
- Date: 2026-11-19T09:30:00+00:00
- Primary source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMihwFBVV95cUxPb2VPZTlsTi1WM2Y0Z04tR2pTOUMzVnUyUlEtMi1yWktGUFlicWFJdzVSWE00N2xiZkRhY2J5ZW5xcHBCMF91WTh6VHRlVHNuSEk3Z2JJMnktSVQtUUZqTkZCclNTeUxmOEFiTkd2X18tUFkxWnlfLWJZRTlCcUw5clUtNkxhWkU?oc=5
- Summary: UK insurers lag on AI governance, Sapiens study finds&nbsp;&nbsp;IT Brief UK

### 6. Apple may be developing its own AI agent that runs your Mac
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-20T00:56:01+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/19/apple-may-be-developing-its-own-ai-agent-that-runs-your-mac/
- Summary: The iPhone maker appears to be building agents that can compete with the likes of Meta Muse, Instinct, Claude, and OpenAI Dots.

### 7. These tech outages are giving Y2K, AI agent style
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-19T21:42:31+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/19/these-tech-outages-are-giving-y2k-ai-agent-style/
- Summary: Are the recent outages in the airline booking systems, banking platforms, and productivity platforms really a coincidence? There's actually likely something deeper going on, cybersecurity experts say.

### 8. Google gives Gemini the ability to use your Mac for you
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-19T18:09:11+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/
- Summary: Google's latest update to Gemini brings an AI agent to the Mac that can organize files, fill out forms, and tackle multistep workflows.

### 9. Meta’s AI agent Muse is mixing up conversations and could be exposing private data, report says
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-19T17:38:40+00:00
- Primary source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/
- Summary: In some of these instances, employees said Muse surfaced messages about childcare requests they never made, career advice they never asked for, product orders they never placed, and bank account balances that didn't belong to them.

### 10. Show HN: AgentMall – Let your AI agent buy groceries
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-19T16:46:14+00:00
- Primary source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://getagentmall.com
- Summary: Hey HN, we’re Nel and Kosi.<p>We noticed personal agents like Instinct, Muse were terrible at buying stuff. Most of the time the checkout would fail.<p>So we built reliable automations for agents to checkout at 9 leading grocery merchants.<p>We grapple with anti bot, logins, OTP codes, and changing checkout structures.<p>Loved revisiting this stuff given our backgrounds sneaker-botting and building computer use models. Honestly full circle haha.<p>It currently works on these sites with ~70% checkout success rate:<p>- Walmart - Albertsons - Ocado - Wegmans - FreshDirect - Best Buy - Instacart<p>Our goal is to hill climb to 90%+ across each.<p>Test keys are free and run the real flow without placing an order.<p>New accounts get 10 free completed orders.<p><a href="https:&#x2F;&#x2F;docs.getagentmall.com&#x2F;quickstart" rel="nofollow">https:&#x2F;&#x2F;docs.getagentmall.com&#x2F;quickstart</a>

### 11. Tecla
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-19T03:05:34+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/tecla-3
- Summary: <p> A proactive AI agent whose interface is a TODO list </p> <p> <a href="https://www.producthunt.com/products/tecla-3?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1322379?app_id=339">Link</a> </p>

### 12. Adside
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-19T00:52:42+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/adside
- Summary: <p> A team of specialized AI agents that manage paid ads for you </p> <p> <a href="https://www.producthunt.com/products/adside?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1322288?app_id=339">Link</a> </p>

### 13. RoboBuilder: Agentic Robot Co-Design with Real-world Video Feedback in the Loop
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-18T05:02:07+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2611.23855
- Summary: Can AI agents design robots that work in the real world? We introduce RoboBuilder, a benchmark in which coding agents co-design a robot's hardware and program from standard parts, motors and a custom 3D-printed part, and every design that passes in simulation is built and tested on a physical course. Simulation alone is not enough: under public part data, none of 15 initial passing designs crossed the real course, so an agent learns the simulator from measurements it requests and videos of real runs. Across four frontier coding agents, ten obstacles at three difficulty levels, 16,427 simulations of 12,774 distinct robots and 135 physical robots built in an estimated 240 hours, agents solve nearly all easy obstacles and invent mechanisms our search baselines do not reach, but falter at harder levels, when one robot must cross every obstacle, and in the real world, where 66% of simulated passes hold across all levels. Closing the loop helps: shown a video of its real failure, an agent redesigns the robot, sometimes correcting its simulator, and removes 72% of level-1 and level-2 failures. RoboBuilder measures progress toward agents that engineer real machines. Project Page: https://ghadinehme.com/robobuilder.github.io/

### 14. Microsoft IQ
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-17T19:34:13+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/microsoft-365
- Summary: <p> Give AI agents a shared understanding of your business </p> <p> <a href="https://www.producthunt.com/products/microsoft-365?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1320750?app_id=339">Link</a> </p>

### 15. AI Canvas
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-17T15:46:37+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/ai-canvas-2
- Summary: <p> A design system for AI agents to design badass interfaces </p> <p> <a href="https://www.producthunt.com/products/ai-canvas-2?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1320481?app_id=339">Link</a> </p>

### 16. InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-17T11:07:45+00:00
- Primary source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2611.22584
- Summary: Existing agentic manipulation systems treat pretrained vision-language-action (VLA) policies as opaque, language-only primitives: when a policy call fails under unfamiliar instructions or scene perturbations, the agent cannot steer its behavior and is forced into futile retries or costly manual takeover. We present InteractVLA, a framework that turns pretrained flow-based VLAs into geometrically steerable and inspectable tools through a bidirectional geometric interface with vision-language agents. In the forward direction, test-time geometric guidance translates an agent-specified end-effector target into input gradients through the action expert via a differentiable command-to-pose mapping, while soft-time target alignment treats arrival time as a latent execution index to match the target pose without distorting the policy's approach motion. In the reverse direction, action-informed agentic refinement exposes generated action chunks and calibrated camera reprojections back to the agent, allowing it to diagnose spatial discrepancies, revise targets for subsequent VLA calls, or locally adjust motion segments on top of the guided trajectory. Making the VLA controllable not only boosts online agentic tool use, but also unlocks effective recursive self-improvement (RSI), achieving state-of-the-art performance of 99.4\% on LIBERO-Plus, 48.62\% on RoboDojo, and 89.4\% on RoboCasa365. Project page: https://lingwupro.github.io/InteractVLA/.

### 17. Beacon
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-17T10:45:51+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/beacon-26
- Summary: <p> Give your AI agent the browser you're already signed into </p> <p> <a href="https://www.producthunt.com/products/beacon-26?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1320163?app_id=339">Link</a> </p>

### 18. Vanira
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-17T08:08:38+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/vanira
- Summary: <p> Voice, video & multimodal AI agent infrastructure </p> <p> <a href="https://www.producthunt.com/products/vanira?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1319962?app_id=339">Link</a> </p>

### 19. KaDeep AI
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-17T08:00:01+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/kadeep-ai
- Summary: <p> Agentic QA, localization & accessibility: know when to ship </p> <p> <a href="https://www.producthunt.com/products/kadeep-ai?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1319952?app_id=339">Link</a> </p>

### 20. LinkBit
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-17T07:57:08+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/linkbit
- Summary: <p> Free URL shortener your AI agent can use (MCP + API) </p> <p> <a href="https://www.producthunt.com/products/linkbit?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1319947?app_id=339">Link</a> </p>

### 21. Ody Ai Business Phone
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-16T18:36:57+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/ody-ai-business-phone
- Summary: <p> Shared workspace + manageable AI agents </p> <p> <a href="https://www.producthunt.com/products/ody-ai-business-phone?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1319278?app_id=339">Link</a> </p>

### 22. S.Space
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-15T13:26:16+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/s-space
- Summary: <p> Your team and everyone's AI agents, in one workspace </p> <p> <a href="https://www.producthunt.com/products/s-space?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1317562?app_id=339">Link</a> </p>

### 23. Mermaid Flow
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-11T20:24:56+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/mermaid-chart
- Summary: <p> The visual builder for agentic workflows </p> <p> <a href="https://www.producthunt.com/products/mermaid-chart?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1313286?app_id=339">Link</a> </p>

### 24. Teaflask
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-09T16:27:48+00:00
- Primary source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/teaflask
- Summary: <p> Self-improving AI copilot for your app. No backend changes. </p> <p> <a href="https://www.producthunt.com/products/teaflask?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1310284?app_id=339">Link</a> </p>

### 25. Waldo by Wherobots
- Weighted score: 0.00
- Deep score: 0
- Date: 2026-11-05T15:23:12+00:00
- Primary source: product_hunt
- Focus/tech: AI agents, robotics / AI agents
- URL: https://www.producthunt.com/products/waldo-by-wherobots
- Summary: <p> The AI agent that accelerates engineering with spatial data </p> <p> <a href="https://www.producthunt.com/products/waldo-by-wherobots?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1305594?app_id=339">Link</a> </p>

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
