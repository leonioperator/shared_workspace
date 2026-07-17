# Blindspot Signals Report - 2026-07-17

- Source export: `/opt/apps/haier/exports/evolution_signals_20260717_020524.json`
- Total signals in export: 5000
- Agent-relevant signals: 541
- Novel vs previous reports: 314
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`

## New Signals Since Previous Reports

### 1. A multi-agent workflow converts CAR-T patient evidence into experimentally testable hypotheses
- Deep score: 0.2
- Date: 2026-07-16T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.15.738646
- Summary: The rapid expansion of chimeric antigen receptor (CAR) T cell studies has produced a fragmented evidence landscape linking publications, repository accessions, patient metadata and mechanistic observations. Here we present BioPathfinder, a multi-agent discovery engine for CAR-T research evidence construction, hypothesis generation and validation planning. Unlike existing LLM-based and agentic approaches centered on predefined CAR-T development tasks, BioPathfinder constructs a provenance-tracked resource linking scRNA-seq datasets from treated patients to their publications and uses it to generate diverse, falsifiable and dataset-aware mechanistic hypotheses prioritized for computational and experimental validation by role-specialized LLM reviewer subagents. Applied to the curated CAR-T-treated patient paper-dataset corpus, BioPathfinder nominated candidate mechanisms of CAR-T persistence, dysfunction and therapeutic resistance, including the hypothesis that genes associated with an NK-like transition program could be targeted to reduce CAR-T exhaustion and promote persistence. Patient scRNA-seq analysis showed that this NK-like transition-associated program was enriched in exhausted post-infusion CAR-T cell states. Virtual perturbation further prioritized transition-associated KLR-family receptor genes, including KLRC1, KLRD1 and KLRG1. Expert review selected KLRC1, encoding NKG2A, for experimental testing. In vitro and in vivo chronic-stimulation models showed that NKG2A marked CD8 CAR-T cells with activated and exhaustion-associated phenotypes. NKG2A blockade improved antitumour function and persistence-associated readouts in vivo. These results show that structured clinical single-cell evidence can be transformed by domain-specialized multi-agent systems into experimentally actionable CAR-T engineering hypotheses.

### 2. Medea: An AI agent for therapeutic reasoning across biological contexts
- Deep score: 0.2
- Date: 2026-07-16T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.01.16.696667
- Summary: Therapeutic hypotheses can transfer across diseases but their relevance depends on biological context. The same target, perturbation, or treatment can produce different effects across cell types, disease states, genetic backgrounds, and patients. Therapeutic reasoning therefore requires methods that preserve context, test when evidence supports transfer, and identify where context-specific effects limit it. Although AI agents can perform therapeutic analyses, existing systems often fail to preserve biological context over long workflows, verify intermediate computational steps, or reconcile conflicting evidence across datasets and literature. Here, we present Medea, an AI agent for therapeutic reasoning across biological contexts. Medea executes multi-step analyses using biological tools, machine learning models, and literature retrieval while enforcing verification during planning, execution, and evidence synthesis. We evaluate Medea across 5,673 open-ended analyses in three domains: cell type specific therapeutic target nomination in five diseases and 29 cell types, synthetic lethality prediction in 7 cancer cell lines, and immunotherapy response prediction from multimodal patient profiles. Using a previously unpublished epistatic miniarray profiling screen performed under two DNA-damaging treatments, we evaluate Medea on predicting synthetic lethality among 238,046 gene-gene pairs in yeast. Medea accurately predicts these experimentally measured synthetic lethal interactions, indicating that its performance reflects biological relevance rather than information leakage from benchmark datasets. Across these evaluations, Medea improves performance over large language models, reasoning models, biomedical agents, and specialized machine learning models while maintaining low failure rates and calibrated abstention. These results show that verifiable AI agents can perform therapeutic analyses across biological contexts.

### 3. Show HN: Libretto PR agents – Automatically fix failing playwright scripts
- Deep score: 0.1
- Date: 2026-07-16T20:21:27+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://libretto.sh/debug-agents
- Summary: Libretto PR agents is a free TypeScript library for maintaining Playwright browser automations. Add one line of code to your existing Playwright scripts and it lets an agent automatically open GitHub PRs fixing the script when it fails.<p>A few months ago we released Libretto, a CLI + coding-agent skill for building deterministic browser automations. The idea was that for many browser workflows, especially repetitive business workflows, you don’t need an AI agent making decisions at runtime. You want deterministic Playwright scripts that are inspectable, faster to run, and much cheaper than repeatedly calling an AI browser agent.<p>That helped us generate Playwright and network-request-based scripts, but websites can often change which breaks deterministic scripts. So maintaining a variety of scripts at scale is a headache. If you already have a bunch of functioning Playwright scripts, the last thing you want is to rewrite everything around a new runtime AI framework like browser-use or stagehand just to make maintenance easier.<p>The Libretto PR Agent pulls your code from GitHub and connects via CDP to the browser session that just failed. It has an exec tool for injecting Playwright and javascript into the page, and once its inspected the failure, it opens a PR to your repo with a proposed code fix.<p>You use it like this:<p><pre><code> try { await automationLogic(page); } catch (error) { await playwrightDebugger.debugFailure(error, page); throw error; } </code></pre> The agent is completely free and open source, lets you bring your own LLM provider API keys, and works with any browser provider (including self hosted).<p>The source code is here: <a href="https:&#x2F;&#x2F;github.com&#x2F;saffron-health&#x2F;libretto&#x2F;tree&#x2F;main&#x2F;packages&#x2F;playwright-debugger" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;saffron-health&#x2F;libretto&#x2F;tree&#x2F;main&#x2F;package...</a><p>We think this makes browser integrations much easier to …

### 4. Lineation.ai focuses on runtime security for autonomous AI agents - Help Net Security
- Deep score: 0.1
- Date: 2026-07-16T09:12:21+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiiAFBVV95cUxNdnV6N0dUdXM4eFpIOFBiV1N5NF9kYUhxOU9DcnFRZnNHRjJDS3pRLUZSY0NCNmxGUlpwcnVxTkNUTnNDRXlrQ3JJN3pSM2hfbm9VZV9KekdYalNvOGlXdjI5ZjZhbDVZa1ZtbW9fQnctRVU4NXRSY1ZBNURwSmlVU3pxYWE4V1Bm?oc=5
- Summary: Lineation.ai focuses on runtime security for autonomous AI agents&nbsp;&nbsp;Help Net Security

### 5. Kit For AI
- Deep score: 0.1
- Date: 2026-07-15T10:39:04+00:00
- Source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/kit-for-ai
- Summary: <p> The memory layer for AI agents </p> <p> <a href="https://www.producthunt.com/products/kit-for-ai?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1197148?app_id=339">Link</a> </p>

### 6. Manta AI
- Deep score: 0.1
- Date: 2026-07-13T12:00:36+00:00
- Source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/manta-ai
- Summary: <p> Your AI agent for autonomous web app testing </p> <p> <a href="https://www.producthunt.com/products/manta-ai?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1195155?app_id=339">Link</a> </p>

### 7. ENPIRE: Agentic Robot Policy Self-Improvement in the Real World
- Deep score: 0.1
- Date: 2026-06-18T09:21:27+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.19980
- Summary: Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering, which becomes a central bottleneck in the pursuit of general physical intelligence. Although emerging coding agents can generate code to automate algorithm search, their successes remain largely confined in digital environments. We conjecture that the missing abstraction to automate robotics research is a repeatable feedback loop for real-world policy improvement: reset the scene, execute a policy, verify the outcome, and refine the next iteration. To bridge this gap, we introduce ENPIRE, a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate policies with one or multiple physical robots operating in parallel, and an Evolution module (E) in which coding agents analyze logs, consult literature, improve training infrastructure and algorithm code to address failure modes. This closed-loop system transforms real-world manipulation learning into a controllable optimization procedure, minimizing human effort while allowing fair ablations across training recipe and agent variants. Powered by ENPIRE, frontier coding agents can autonomously train a policy to achieve a 99% success rate on challenging, dexterous manipulation tasks, such as organizing a pin box, fastening a zip tie, and tool use, a process that further accelerates when we dispatch an agent team on a robot fleet. Our results suggest a practical and scalable path toward deploying coding agents to autonomously advancing robotics in the physical world.

### 8. Get back hours every day with autonomous agents in Amazon Quick - Amazon Web Services (AWS)
- Deep score: 0.1
- Date: 2026-06-17T20:35:39+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMirwFBVV95cUxNNTBPMElPTW1nYXJMVXBqY293dldfNDVDaWhpcmV0ZU0waE1mVjZOTHR0ek1INVFqNmRBUml4bUJ0TnBNb2xJVGNMTDNMaFZrdlhOOE1BdHRHSGZTeUtXT0FweXVZZFpHenVWUW95UXAzeTRWOXlCMXBidHBsYjdzYnJWWC13a1ZvS09ORHJkN0ozYzNaWXp0RldnaHlQYWh3akNKRkVBSU5WWm1xaFBn?oc=5
- Summary: Get back hours every day with autonomous agents in Amazon Quick&nbsp;&nbsp;Amazon Web Services (AWS)

### 9. Show HN: Relaymux, a tmux-based meta-harness for local coding agents
- Deep score: 0.1
- Date: 2026-06-17T17:27:58+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/mupt-ai/relaymux
- Summary: Hey HN,<p>There’s been a lot of interest recently in meta-harnesses, loops, and multi-agent orchestration. Obviously, there are already a lot of good tools: Conductor, cmux, the native Codex &#x2F; Claude Code apps, etc.<p>For my own use cases, I’ve felt that the orchestration layer tends to feel overengineered. I mostly wanted a simple local harness (i.e Pi) for running and tracking CLI agents with the ability to hop in (via tmux). Relaymux is my opinionated attempt at that.<p>A few design principles:<p>- The frontend is just Telegram &#x2F; iMessage &#x2F; CLI. If I want more visibility, I hop into tmux.<p>- Subagents are normal interactive CLI agents running in tmux windows, usually with their own worktrees.<p>- The harness owns the tmux session, so each longer task becomes a named tab&#x2F;window. Subagents report back to the orchestrator via CLI when they’re blocked or done. Then the orchestrator just messages me on Telegram &#x2F; iMessage<p>- It works with any CLI agent that has an interactive terminal mode, so I don’t need special print-mode&#x2F;non-interactive support. This means I don’t need to stress about the Agent SDK &#x2F; claude -p billing limitations.

### 10. Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems
- Deep score: 0.1
- Date: 2026-06-17T09:12:50+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.18837
- Summary: Large Language Model (LLM)-based automatic Multi-Agent Systems (MAS) generation has become a crucial frontier for tackling complex tasks. However, existing methods face a dilemma between model capability and experience retention. Inference-time MAS leverages frozen frontier LLMs but repeats identical searches without learning from past experience. Conversely, Training-time MAS internalizes experience via gradient updates but is constrained by the low capability ceiling of smaller models, and is hard to scale to large frontier LLMs. To bridge this gap, we propose Skill-MAS, a novel third path that decouples experience retention from parametric updates by conceptualizing the high-level orchestration capability as an evolvable Meta-Skill. Skill-MAS refines this architectural knowledge through a closed optimization loop: (1) Multi-Trajectory Rollout samples a behavioral distribution for each task under the current Meta-Skill; and (2) Selective Reflection adaptively selects priority tasks and applies hierarchical contrastive analysis to distill systemic experience into generalizable, strategy-level principles. Extensive experiments across four complex benchmarks and four distinct LLMs demonstrate that Skill-MAS not only achieves remarkable performance gains but also maintains a favorable cost-performance trade-off. Further analysis reveals that the evolved Meta-Skills are highly robust and exhibit strong transferability across unseen tasks and different LLMs.

### 11. EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems
- Deep score: 0.1
- Date: 2026-06-17T04:07:41+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.18668
- Summary: In large-scale enterprise settings, centralized multi-agent systems (MAS) are increasingly adopted, in which a coordinator delegates user requests to lightweight, domain-specialized sub-agents. While this architecture improves modularity, scalability, and cost efficiency, its reliability depends not only on accurate routing but also on sub-agents' ability to calibrate their responses to capability constraints. In particular, sub-agents built on smaller fine-tuned models often struggle with such calibration, leading them to over-answer ambiguous, underspecified, misrouted, or unsupported requests and produce hallucinated outputs instead of actionable feedback. To address this challenge, we present EARS (Explanatory Abstention for Reliable Sub-Agent Modeling), a production-oriented framework that reframes sub-agent abstention as an inter-agent communication protocol: a sub-agent does not merely abstain, but exposes an actionable failure state to the coordinator. EARS curates human-agent interaction data using an ensemble of calibrated LLM-as-a-Judge models, producing structured abstention labels and rationales under a taxonomy of sub-agent failure modes. These data are used to fine-tune sub-agents to detect failure conditions and return rationales for coordinator-level clarification, rerouting, or fallback. We evaluate EARS in a large-scale production e-commerce assistant supporting enterprise business intelligence workflows. EARS improves the overall response pass rate from 68.5% to 78.9%, demonstrating that sub-agent-side explanatory abstention improves MAS reliability.

### 12. Neural mechanisms of handedness for precision drawing: hand-dependent engagement of cortical networks for bimanual control and tool use
- Deep score: 0.1
- Date: 2026-06-17T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, neural interfaces / AI agents
- URL: https://www.biorxiv.org/content/10.1101/2025.11.18.689091
- Summary: Neural mechanisms underlying handedness remain poorly understood. We used functional magnetic resonance imaging (fMRI) to study performance of a visually guided drawing task with each hand. We hypothesized that the left superior parietal lobule supports drawing with either hand, and individuals with chronic peripheral nerve injury (PNI) to the dominant hand use the same mechanism as healthy adults. Thirty-three right-handed adults (23 healthy, 10 patients) underwent fMRI while performing a precision drawing task, alternating between the right hand (RH) and left hand (LH). BOLD magnitude and functional connectivity (FC) modulation via generalized psychophysiological interaction were analyzed in 12 a priori regions of interest, followed by additional exploratory areas identified via whole brain magnitude analysis. During LH drawing (compared to RH drawing), contralateral primary motor cortex showed lower BOLD magnitude but greater FC with two networks: First, a left motor-premotor network with increased FC and equal-or-greater magnitude during LH drawing. Second, a right parietal network characterized by increased FC during LH drawing but increased magnitude during RH drawing. Exploratory whole-brain analyses supported and extended these motor and parietal networks, and additionally suggested that RH drawing may involve greater magnitude and FC within a bilateral parieto-premotor network centered on right paracingulate cortex. Patient group (PNI vs. control) did not interact with these effects. These results describe the first proposed mechanisms for LH precision drawing, both of which depend on differential engagement of bimanual control networks: a left hemisphere motor-premotor network for precision motor control, which engages intrahemispherically (directly) during RH drawing and interhemispherically (indirectly) during LH drawing; and a right hemisphere parietal network with greater distributed coordination during LH drawing. These mechanisms did not differ …

### 13. AI Governance Is the Legal Foundation: What Employers and Boards Need to Know in 2026 - Epstein Becker Green
- Deep score: 0.1
- Date: 2026-06-16T07:00:00+00:00
- Source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMiyAFBVV95cUxNNkpLSXdwcThDcnhuYTBnR3BuMnJpcS00dlg4d2ZGV1k2d3pQT004QXUyRHNnT3hTcFdNZUo1dWxuSVRXY0lFelNaSnFZOG5aWmpRVlhMUTdkc1djU2pVY2JNNndqX1lyeTRKY2YteEFfcUk4dXRKS0gwTmtzLXN0MmhTVjc3bG1WMzNmdkxfdEZnX2JHTThtUF9sZFl6bDltZTdJanVTZ1dqUkRvQXNzR2tjbEdKdUZjZEROV3YwRGRXXzF6RTVrTQ?oc=5
- Summary: AI Governance Is the Legal Foundation: What Employers and Boards Need to Know in 2026&nbsp;&nbsp;Epstein Becker Green

### 14. SKT Deploys Autonomous AI Agents Across Operations - Let's Data Science
- Deep score: 0.1
- Date: 2026-06-16T06:10:00+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMilwFBVV95cUxNS3JqWk9XNjdKXy1RUXJxVF8wcnJqWGpHSEFMN09OR1UzeTdNcDg2Wi1IcDVQM3pxMEVERXF2QjhHNkRiczQ5c1FNaUtObVZHeVprVXVUNnBmMHF0S1Mzb3d5bUZhS0VfUnFRb0NNcmVhUGM3aExOUUJES2tyWjA2Zl9LX0VMdkZqb3dYbHo1TlA0MG5nTlQ4?oc=5
- Summary: SKT Deploys Autonomous AI Agents Across Operations&nbsp;&nbsp;Let's Data Science

### 15. Insiders warn banks are ‘sleepwalking’ into an AI governance failure - QA Financial
- Deep score: 0.1
- Date: 2026-06-16T05:19:18+00:00
- Source: google_news
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://news.google.com/rss/articles/CBMilwFBVV95cUxQYW13b2tRZTRYSVpad0NXMXhvTk9sd2FJNFdGY3NOdENFRU9TNVVUVWFBTFhxM0RrOWhobm9GcVhmc3h0YnF6LWtPbnkySHRFVkoxbG9QMWw0YVdFY1haSHZZazFXVjljTXUzejd4aTRtLUhBenpYU1JJMUdPb3dEYy1iYkE4dF9UclpOb19EcEk2Szlham9F?oc=5
- Summary: Insiders warn banks are ‘sleepwalking’ into an AI governance failure&nbsp;&nbsp;QA Financial

### 16. Tech Talk | The AI Accountability Gap: Tethering Autonomous Agents to Human Owners - Redmondmag.com
- Deep score: 0.1
- Date: 2026-06-15T23:43:38+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMirAFBVV95cUxNMXZ1alVnZ01oYjVhczZabjhKWXJFOU52Q3RmWVY4VGdIcXNEbFZXUV9wSzQxbG1RRlpnQkJRT0c5bmJZeE5wVm0zNVV1akdDRndtLXVTYUpEZVYyRzlzZU5lcW1PN0wyRnpsclR3SnV2cVRPQWZZT2xrSWdLOWkxTlBqMnBoUklzUV8xSXoycGozNlZMSEpYUmtpYUpGYm55cG9IQ0VVdVVDMWZh?oc=5
- Summary: Tech Talk | The AI Accountability Gap: Tethering Autonomous Agents to Human Owners&nbsp;&nbsp;Redmondmag.com

### 17. Blockchain AI Integration and Autonomous Agents Guide - Blockchain Council
- Deep score: 0.1
- Date: 2026-06-15T08:40:17+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMimgFBVV95cUxNR2pPbUN2ZlVGUHlOSzl2dzhCSW05Z21uZXB5X09mYTNqY3ZFWFBYV091OENrQ3ppS1VSTGdSV1RYY3I3Qk5xajAwcnIyZ3ZrUEc4MWdTRHA3cHN5VHZpRGNsME5jYzFyV2N3T1dKX2tiYi1TMFVhUnZiRFJHQkxjeUZIMWpoWnh2X19qMU1oNjdIazZVUmp0VVB3?oc=5
- Summary: Blockchain AI Integration and Autonomous Agents Guide&nbsp;&nbsp;Blockchain Council

### 18. Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations
- Deep score: 0.1
- Date: 2026-06-14T16:32:15+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.15903
- Summary: Where an LLM sits in an agent memory pipeline -- between the recall plane that retrieves stored facts (extensively benchmarked) and the control plane that mutates them via supersede, release, purge (largely untested) -- shapes which forgetting failure modes the system recovers. Comparing thirteen system configurations on a 385-case adversarial surface, we observe three placement regimes with partly complementary coverage: deterministic primitives suffice for lexical/temporal categories but fail canonicalization (5% on identifier-obfuscation, 0% on cross-lingual); inscribe-time LLM recovers canonicalization (100%) but cannot help intent-aware deletion (0% on prefix-collision and compound-fact); a mutation-time hook recovers intent-aware deletion (78-85%) and brightens nearly all categories simultaneously (91.7-93.2% overall, $0.17 per 385-case run, 2.3s/case mutation latency vs. 64-191ms/case deterministic, recall path unchanged). We expose the trade-off via ForgetEval, a 1000-case templated suite plus a 385-case adversarial layer (132 hand-crafted + 253 LLM-drafted oracle-validated) scored by deterministic substring match, paired with a six-method Adapter Protocol with honest N/A scoring that lets heterogeneous memory stores enter in 130 lines. Admission is corroborated by 10-annotator IAA (Fleiss' kappa = 0.958) and a 77-case external-authored subset (four blind contributors) that replicates the canonicalization asymmetry and amplifies the joint-placement lift (+27.8 pt). Production failures are predominantly forgetting failures rather than recall failures, yet existing benchmarks measure only recall. ForgetEval and all adapters are released under MIT.

### 19. TencentCloud / TencentDB Agent Memory
- Deep score: 0.1
- Date: 2026-06-14T02:02:03.648769+00:00
- Source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/TencentCloud/TencentDB-Agent-Memory
- Summary: TencentDB Agent Memory delivers fully local long-term memory for AI Agents via a 4-tier progressive pipeline, with zero external API dependencies.

### 20. CoAgent: Concurrency Control for Multi-Agent Systems
- Deep score: 0.1
- Date: 2026-06-13T16:15:14+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.15376
- Summary: Multi-agent LLM systems -- coding agents, devops agents, document agents -- now routinely run several agents in parallel against the same git tree, Kubernetes cluster, or document. As soon as two of them mutate shared state, they enter the regime classical concurrency control has studied for decades, but classical mechanisms fit LLM agents poorly. A single agent transaction spans minutes of inference, read sets are broad and opaque rather than statically inferable, and the live state agents act on admits neither fork nor buffer, so writes take effect the moment they execute. Locks block long inference intervals; OCC abort-and-retry discards minutes of work on every conflict. This paper builds concurrency control on a capability classical transactions lack: the LLM inside each agent can judge whether a conflicting write invalidates its plan, and can repair exactly the operations that depended on it. Control therefore turns advisory: the runtime informs, the agent repairs. Our protocol, MTPO (Monotonic Trajectory Pre-Order), fixes a serialization order at launch, serves each read the order-filtered value, and applies writes speculatively in place; a one-way notification asks an affected reader to re-judge and patch its plan, while the framework mechanically undoes and reorders misplaced writes through the saga-style inverse each tool registers in advance. At quiescence the run is serializable in the pre-decided order. We realize MTPO as CoAgent, toolcall middleware whose privileged ToolSmith grows footprint-declared, undoable tools online. On ten contended workloads, CoAgent stays within 5\% of serial correctness at a $1.4\times$ speedup and near-serial token cost, where 2PL and OCC surrender nearly all concurrency gains; on a bash-only target system, it grows a 25-tool library online and lifts the task pass rate from 45/71 to 63/71 at $0.80\times$ the time and $0.86\times$ the cost.

### 21. Differentially Private Consensus for Time-Delay Multi-agent Systems
- Deep score: 0.1
- Date: 2026-06-13T05:51:41+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.15135
- Summary: This paper is concerned with the differentially private consensus problem for discrete-time multi-agent systems with communication delays. The purpose of the paper is to achieve differentially private consensus for such systems while protecting the entire delayed initial histories of all agents. A novel adjacency relation for delayed histories is introduced, and a Laplace-noise-based privacy mechanism is developed, where the noise variance is allowed to vary with time and even increase. By using the difference resolvent function method, decay estimates for the fundamental solutions of the delayed difference equations are derived. Based on these estimates and a backstepping technique, mean square weak consensus, mean square strong consensus, and almost sure strong consensus are established. The estimates for the fundamental solutions are also used to derive an explicit sensitivity bound. Furthermore, a constructive parameter design is provided to achieve a prescribed infinite-horizon $ε^\star$-differential privacy level. Numerical simulations illustrate the theoretical results.

### 22. DynaHMRC: Decentralized Heterogeneous Multi-Robot Collaboration for Dynamic Tasks with Large Language Models
- Deep score: 0.1
- Date: 2026-06-12T18:41:30+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.14882
- Summary: Large language models (LLMs) provide robots with richer task understanding and adaptability, making them promising for coordinating heterogeneous multi-robot systems in long-horizon tasks. Despite this potential, several challenges remain underexplored: (1) Centralized LLM schedulers scale poorly as team size and environmental complexity increase. A single model must process excessive contextual information, and long-context approximation may degrade reasoning quality; (2) Existing task formulations insufficiently consider dynamic settings, while robust adaptation to evolving task conditions is essential for real-world deployment; (3) Domain-specific data scarcity limits specialized robotic reasoning, making proprietary general-purpose models inefficient for expert tasks. To address these limitations, we propose DynaHMRC, a decentralized framework in which each robot acts as a role-aware LLM agent. This design mitigates the single-model context bottleneck and supports flexible collaboration across heterogeneous team configurations. DynaHMRC organizes collaboration as a four-stage closed-loop process: self-description, task allocation with leadership bidding, leader election, and reflective execution, supported by executable robot interfaces. We further develop a benchmark covering three task families, four dynamic variations, and six team configurations to systematically study dynamic task modeling. In addition, we conduct an empirical analysis to guide the construction of domain-specific expert datasets and fine-tune pretrained LLMs to improve specialized competence. Experiments show that DynaHMRC achieves higher success rates than strong baselines with fewer action and communication steps, while demonstrating promising scalability trends as team size grows within the evaluated settings.

### 23. Launch HN: BitBoard (YC P25) – Analytics Workspace for Agents
- Deep score: 0.1
- Date: 2026-06-12T16:58:03+00:00
- Source: hackernews
- Focus/tech: AI agents, robotics / AI agents
- URL: https://bitboard.work/
- Summary: We’re Connor and Ambar from BitBoard (<a href="https:&#x2F;&#x2F;bitboard.work">https:&#x2F;&#x2F;bitboard.work</a>). BitBoard is an agentic analytics workspace. We give you the infrastructure and visualization layer to analyze data with AI.<p>Today, we’re launching dashboards that you and your agents can work on together. You can connect your coding agent or AI chat to BitBoard and build live reporting. Here’s a demo: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=HPl0K565a7c" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=HPl0K565a7c</a>.<p>AI tools treat data analysis as ephemeral, making it hard to report or collaborate. Legacy BI tools weren’t intended for AI users, so they bolt on chatbots and can’t offer meaningful control to your agents. Software can now make far more of a business legible than BI ever could, but neither legacy BI nor chat bots are built to handle it.<p>Our original product was AI agents for administrative tasks in healthcare (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44237769">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44237769</a>), but customers kept pulling us toward their data analysis problems: queries scattered across disparate sources, spreadsheets floating everywhere. We kept building tooling for addressing that, and at a certain point those tools were becoming our product.<p>We ran into several problems. Agents made bad inferences because they had no context on the business. They couldn&#x27;t be trusted to make decisions because nothing checked their work. And anything one agent or one person figured out was invisible to everyone else. In BitBoard, humans and agents interact with the same data primitives but get tools designed for their own work.<p>We’re building dashboards to make the human reading experience better. These dashboards progressively use intelligence - starting from code or SQL queries and leading to full embedded apps. Humans and agents will need to agree on …

### 24. StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance
- Deep score: 0.1
- Date: 2026-06-12T15:48:43+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.14571
- Summary: A central role of personal-agent memory is to turn stored information and prior interactions into future-oriented assistance. In daily use, useful cues come from what the agent observes and how the user interacts with the agent, and the agent must carry them forward from the current request to similar future tasks. Existing memory benchmarks usually test dialogue recall or task improvement in isolation, leaving the trajectory from streaming observations to later assistance largely untested. We introduce StreamMemBench, a streaming benchmark that constructs a two-step task sequence around each evidence anchor from EgoLife egocentric streams. The initial task tests evidence use, while the follow-up task tests whether feedback and interaction experience are reused. Four metrics diagnose evidence recall, initial evidence use, feedback incorporation, and follow-up reuse. Experiments with eight memory systems across two backbones show that current systems often fail to use observed evidence or turn feedback into reliable follow-up behavior, even when evidence is stored or feedback is incorporated locally. StreamMemBench is publicly available at https://github.com/landian60/StreamMemBench.

### 25. Coinbase Opens Door for AI Agents to Trade Crypto Autonomously - FinanceFeeds
- Deep score: 0.1
- Date: 2026-06-12T07:46:17+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMikgFBVV95cUxON21RdGZHbzFsSjgtRnp1WG1TTVdoZzN3SVlSV0ZwdFRXdDhKWVBkRzdWdHNTRmJWN3Q3bVM5NkcxeC1sN3Y3RTdBMWxROG4yOERGdXV3Y3kybW90NnRERzNRU2hhTGgwYk82bE9HeGVtZmVMdl9yWGRVYlVjUENOaWFocERBQWd3cmQ3eExWUWgwUQ?oc=5
- Summary: Coinbase Opens Door for AI Agents to Trade Crypto Autonomously&nbsp;&nbsp;FinanceFeeds

### 26. Bodhiorchard
- Deep score: 0.1
- Date: 2026-06-11T12:33:55+00:00
- Source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/bodhiorchard
- Summary: <p> Vibe-code your whole project with 12 autonomous AI agents </p> <p> <a href="https://www.producthunt.com/products/bodhiorchard?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1169323?app_id=339">Link</a> </p>

### 27. Show HN: OpenYabby, voice-controlled multi-agent orchestrator for Claude Code
- Deep score: 0.1
- Date: 2026-06-09T20:08:06+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/OpenYabby/OpenYabby
- Summary: No summary.

### 28. JPMorgan Chase plans autonomous AI agents for 2026 - qz.com
- Deep score: 0.1
- Date: 2026-06-09T16:24:05+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMib0FVX3lxTFBWS2paWmxsSmwzQlg5RHdwblJPQnB5WDcwcUQ2dEw4cU5SQ1BMZ08zd1E4bnV0NjlFZzhlaml5Q2U4LWo4aFZ3SDNicVkxdktYMVBmVzdkM2NXUlFvMURBUGRUaWliVk5ReXFEc0VKdw?oc=5
- Summary: JPMorgan Chase plans autonomous AI agents for 2026&nbsp;&nbsp;qz.com

### 29. Build a Basic AI Agent from Scratch: Long Task Planning
- Deep score: 0.1
- Date: 2026-06-09T14:29:34+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://medium.com/@rogi23696/build-a-basic-ai-agent-from-scratch-long-task-planning-14e803f9bd6d
- Summary: No summary.

### 30. Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory
- Deep score: 0.1
- Date: 2026-06-09T10:31:51+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.10677
- Summary: Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for collecting related evidence, preserving metadata, and revising facts over time. New observations are first staged in a buffer and periodically consolidated into coherent textual contexts. At inference time, an agentic retrieval procedure lets the LLM read memory through iterative tool calls rather than a single retrieval step. On MemoryAgentBench, Infini Memory achieves 64.7% overall score. Ablations show that topic-structured maintenance and iterative evidence inspection improve complementary aspects of long-term memory use.

## Top Signals By Deep Score (including already-seen)

### 1. Toward Human-Centered Multi-Agent Systems: Integrating Cognition, Culture, Values, and Cooperation in AI Agents
- Deep score: 0.6
- Date: 2026-06-06T17:40:21+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2606.08274
- Summary: The emergence of large language model (LLM)-based agents and multi-agent systems has enabled a shift from narrow task automation to more autonomous decision-making. Despite progress in language generation, planning, tool use, and coordination, most agents still treat intelligence as prediction, optimization, and task completion. Human environments are social and normative, where people reason under bounded rationality, communicate in culturally situated language, and make decisions guided by values, beliefs, trust, and social norms. This survey argues that future AI agents, especially those acting on behalf of humans, must move beyond task competence toward human-centered capabilities. We review research across six areas: (1) evolution of intelligent agents, (2) human cognition and decision-making, (3) language, culture, and social context, (4) human values and belief systems, (5) human-agent collaboration, and (6) multi-agent coordination and modeling of human characteristics. We synthesize work from cognitive science, sociolinguistics, computational social science, and AI alignment, along with recent advances in LLM agents, cultural alignment benchmarks, preference learning, explainability, and agent societies. We identify a key gap: existing systems do not provide a unified framework integrating cognition, culture, values, and social behavior into autonomous agents. We conclude with directions for building culturally aware, value-aligned, cognitively grounded, and cooperative multi-agent systems.

### 2. Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive Benchmark
- Deep score: 0.5
- Date: 2026-06-17T00:00:00+00:00
- Source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2606.18648
- Summary: Deep research agents are Large Language Model (LLM)-based systems designed for autonomous, multi-step scientific reasoning, and they hold immense potential for accelerating research in the physical sciences. However, comprehensive and in-depth evaluations of their capabilities within this domain remain lacking. To address this gap, we introduce PhySciBench, a benchmark highly relevant to physical science research, comprising 200 expert-curated questions, balanced between physics and chemistry, across six task categories that reflect real-world scientific workflows. Evaluations of state-of-the-art models and agent systems on PhySciBench reveal limited performance; even the strongest baseline, Gemini Deep Research, achieves an accuracy of only 33.5%. Analysis of failure cases identifies three recurrent deficiencies: fragility in extended reasoning chains, limited knowledge transfer across steps, and a lack of physics-grounded self-verification. Motivated by these findings, we develop DelveAgent, a modular multi-agent framework equipped with an adaptive planning loop, dual-granularity memory, and a hierarchical physics-grounded reflection mechanism. Across four scientific benchmarks, DelveAgent improves accuracy by up to 7.5 percentage points while reducing inference costs to approximately one-third of the strongest baseline. These results establish the significance of PhySciBench as a critical benchmark for evaluating AI systems in the physical sciences and demonstrate that architectural specialization can effectively enhance the reliability of autonomous scientific research.

### 3. DARRMS -- An Efficient Algorithm for Dynamic Attention Radius in Resource-Constrained Multi-Agent Systems
- Deep score: 0.5
- Date: 2026-06-10T19:14:56+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.12614
- Summary: Multi-agent systems are integral tools for various domains such as robotics, cybersecurity, and autonomous vehicle planning. These types of systems often have constraints on the computational resources, leading to a need for efficient lightweight algorithms. Traditional decision making frameworks often assume ideal conditions, such as full observability and unlimited computational capacity, which do not align with real-world challenges. In this paper, we introduce a new algorithm that allows for reduced demand on computational resources without a large cost of other performance metrics. Agents will limit their observability to some attention radius, which intentionally allows them to ignore parts of the environment that might be unnecessary for action planning. By optimizing both the attention radius and decision-making, our approach enhances coordination and scalability in uncertain environments. Through both theoretical analysis and empirical validation, we demonstrate the effectiveness of adaptive observation in improving system performance and maintaining robust decision-making strategies in resource-constrained systems.

### 4. A Sheaf Framework for Strategic Multi-Agent Systems: From Consensus to Nash Equilibria
- Deep score: 0.5
- Date: 2026-06-01T04:17:57+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.01663
- Summary: The coordination of heterogeneous autonomous agents in dynamic, adversarial environments requires simultaneous satisfaction of geometric constraints, logical consistency, temporal reasoning, and strategic optimization. Existing sheaf- and topos-theoretic frameworks provide powerful tools for geometric consensus, knowledge alignment, and causal planning, but lack explicit models for value, reward, and strategic choice. This report presents a unified categorical framework that integrates event calculus, SCEL-like ensemble formation, and game-theoretic reward structures into a single Grothendieck topos of time-space histories. We introduce the notion of a \emph{game sheaf} whose stalks contain utility functions and policy distributions, and restriction maps encode both parallel transport and best-response dynamics. We prove that Nash equilibria correspond to global sections of a derived best-response correspondence sheaf, while cohomological obstructions classify failures of strategic consistency. A detailed case study of an immunological ``bastion defense'' scenario -- heterogeneous agents forming attack/defense ensembles under resource constraints -- demonstrates the framework's expressiveness. This synthesis provides a rigorous foundation for verifiable, autonomic, and economically rational multi-agent systems.

### 5. A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation
- Deep score: 0.4
- Date: 2026-07-08T04:23:41+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2607.06990
- Summary: Multi-robot systems provide the parallelism and redundancy necessary for long-horizon tasks, while Large Language Models (LLMs) offer the reasoning capabilities to decompose these objectives into actionable plans. However, effectively grounding this high-level reasoning in physical multi-robot execution remains an open challenge. Existing LLM-based approaches fall mainly into two categories: Single-robot methods achieve robust contact-rich manipulation but lack the coordination mechanisms required for tasks spanning multiple workspaces. Current multi-robot frameworks focus on high-level planning, often treating manipulation as an idealized primitive that fails to account for real-world execution uncertainties. To address this, we propose a hierarchical closed-loop agentic LLM-based framework to ensure robust multi-robot manipulation. Our system consists of three specialized agents: the Planning Agent decomposes instructions into allocated sub-tasks, the Manipulation Agent for each robot executes actions via adaptive tool use, and the Verification Agent closes the loop by monitoring physical outcomes and feeding back semantic corrections. Extensive real-world experiments demonstrate that our framework achieves superior success rates, ensures robust adaptability ranging from single to cross workspace manipulation, and offers a generalizable approach for diverse manipulation tasks.

### 6. Trust Between AI Agents: Measuring Formation, Breakage, and Recovery, with Implications for Governing Multi-Agent Systems
- Deep score: 0.4
- Date: 2026-06-12T19:58:26+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.14923
- Summary: As language-model agents increasingly work in teams, each agent must decide how much to trust its teammates. Yet we lack a standard way to measure trust between AI agents. We propose a behavioral measure based on costly verification. In a cooperative survival game, checking a teammate's work consumes resources, while trusting a wrong answer can be fatal. Relative to a memoryless version of the same model, reduced verification provides an observable measure of trust. Using this framework, we study trust formation, breakage, and recovery across six frontier model snapshots. When paired with a consistently reliable teammate, four snapshots (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.1, and Gemini 3.1 Pro) reduce verification by roughly 60-85%, whereas two smaller snapshots show little or no such adjustment. Failures reverse this discount, but models differ in how they respond. Some concentrate renewed scrutiny on the culprit, while others become more cautious toward the entire team. Recovery is slower than formation, and clustered failures sustain suspicion far longer than the same number of failures spread apart. These differences have practical consequences. Models that form trust verify less, decide more quickly, and achieve higher payoffs in our environment. By contrast, persistent over-verification is associated with indecision rather than safety. Our results show that trust dispositions can be measured before deployment and suggest that calibration, rather than maximal suspicion, should be the central concern in the governance of multi-agent AI systems.

### 7. Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction
- Deep score: 0.4
- Date: 2026-06-10T10:37:27+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.11909
- Summary: Benchmarks are essential for evaluating embodied spatial intelligence, yet their construction is labor-intensive, hard to reuse, and difficult to maintain. Existing embodied benchmarks are often static and may quickly become saturated as models improve, limiting their ability to distinguish new capabilities. We propose Embodied-BenchClaw, an autonomous agentic system for constructing embodied spatial intelligence benchmarks. Given a user-specified evaluation intent, Embodied-BenchClaw automatically produces a complete and continually updatable benchmark package through a five-stage pipeline: intent blueprinting, data collection, structuring and cleaning, benchmark synthesis, and evaluation reporting. The pipeline is coordinated by three agents for planning, construction, and evaluation. To improve reusability and reliability, Embodied-BenchClaw introduces an extensible Skill Library and process quality control, enabling benchmark construction to be composable, verifiable, and repairable. We instantiate multiple benchmarks covering indoor spatial reasoning, outdoor spatial reasoning, robotic manipulation, quadruped robot navigation, UAV/aerial-view understanding, and static benchmark enhancement. These benchmarks span diverse embodied carriers, data sources, and spatial capabilities. Experiments with human evaluation, judge-based assessment, consistency checks, cost analysis, and ablations show that Embodied-BenchClaw can construct verifiable, executable, maintainable, and diagnostically useful embodied spatial benchmarks with reduced manual effort.

### 8. ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems
- Deep score: 0.4
- Date: 2026-06-07T15:59:15+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.08702
- Summary: Recent advances have improved the adaptive capabilities of LLM-based multi-agent systems (MAS) through memory-, skill-, and learning-based approaches, yet these approaches remain challenged by noisy trajectories, insufficient modeling of memory-skill relations, and reliance on additional training or high-quality supervision. To address these limitations, we propose ConMem, a relation-aware and training-free framework that enables efficient multi-agent adaptation through cross-experience coordination. Specifically, ConMem distills historical interaction trajectories into structured memory cards to capture reusable strategies and cues, organizing them into a relation-aware memory graph. At runtime, ConMem retrieves cards according to task needs and coordinates them through the card graph to resolve strategy conflicts and recover their dependencies. Combined, these modules yield structured and relation-aware guidance, enabling robust, lightweight adaptation in multi-agent systems without additional training. Extensive experiments across multiple benchmarks and mainstream MAS architectures show consistent gains over existing memory architectures, with improved inference-time efficiency through pruning more than 50% of expanded candidates and reducing planning overhead by over 80%. Our codes are available at https://anonymous.4open.science/r/ConMemCode

### 9. DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning
- Deep score: 0.4
- Date: 2026-06-05T14:10:48+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.07299
- Summary: Deep Research (DR) has emerged as a new agentic paradigm to tackle complex, open-ended research tasks, demanding systems that can iteratively frame problems, acquire evidence, verify sources, and synthesize long-form reports. In practice, however, current DR systems are constrained by four interrelated limitations: long-horizon planning over an underspecified scope, the bottleneck of decomposing and scheduling such tasks within a single agent, hallucination risk in long-form synthesis, and limited process auditability. This technical report presents DuMate-DeepResearch, a multi-agent DR framework built on the Qianfan Agent Foundry. The framework decouples the Agent Core, which handles task understanding, planning, and scheduling, from an extensible Tool Ecosystem for retrieval, evidence acquisition, and report rendering, making every intermediate decision and tool invocation explicitly traceable. Building on this infrastructure, DuMate-DeepResearch further introduces three mechanisms: (i) a graph-based dynamic planning strategy expands the research roadmap coarse-to-fine and continuously revises it through reflection, re-planning, backtracking, and parallel branching; (ii) a recursive two-level execution design delegates each complex search sub-task to an inner Search Agent that runs its own planning loop, isolating noisy retrieval and stabilizing long-horizon execution; (iii) a rubric-based test-time optimization mechanism dynamically generates task-specific quality criteria and uses them as live reasoning scaffolds for evidence-grounded synthesis and adaptive stopping. Across two deep research benchmarks, DuMate-DeepResearch establishes new state-of-the-art results: the best overall score (58.03%) on DeepResearch Bench, and the best overall score (61.95%) on DeepResearch Bench II while ranking first in information recall and analysis.

### 10. AI-IoT-Robotics Integration: Survey of Frameworks, Emerging Trends, and the Path Toward Connected Robotics
- Deep score: 0.4
- Date: 2026-05-31T05:10:34+00:00
- Source: arxiv
- Focus/tech: robotics, AI decision delegation / robotics
- URL: https://arxiv.org/abs/2606.01015
- Summary: The convergence of Artificial Intelligence, the Internet of Things, and Robotics is no longer a futuristic vision; it is rapidly becoming the foundation of real-time, intelligent, and context-aware systems. AI enables perception and reasoning, IoT provides scalable sensing and communication, and robotics delivers embodied actuation. Despite significant progress in pairwise combinations such as AIoT and the Internet of Robotic Things (IoRT), there remains a lack of unified design frameworks that fully integrate all three. This survey synthesizes the state-of-the-art across these domains, emphasizing the emerging role of Small Language Models (SLMs) at the edge and Large Language Models (LLMs) in the cloud for distributed cognition and autonomous decision-making. We propose a modular system architecture that aligns with these trends, analyze persistent gaps in interoperability and feedback control, and classify existing work by integration depth. Our review highlights how hybrid SLM-LLM systems, when coupled with IoT infrastructure and robotic agents, can address challenges in real-time adaptation, scalability, and reliability. This work offers a conceptual and technical roadmap for designing next-generation AI-IoT-Robotic ecosystems that are modular, interpretable, and capable of learning within dynamic environments, paving the way for the emerging paradigm of Connected Robotics and Physical AI.

### 11. MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models
- Deep score: 0.3
- Date: 2026-07-14T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.05.11.723319
- Summary: Constraint-based metabolic modeling is a powerful way to study the mechanistic basis of cellular states and disease, but its effective use demands substantial computational expertise and careful coordination of multi-step analyses. We developed MechAInistic to lower this barrier and enable researchers to ask complex biological questions in natural language. Harnessing large language models, MechAInistic is a multi-agent system organized around an Architect-Reviewer pattern that transforms a natural-language question into an executable, model-grounded workflow and generates a structured report. The system supports a variety of tasks, including pathway comparison, perturbation analysis, drug-target exploration, and literature-grounded interpretation across paired metabolic model states. We tested MechAInistic on two drug-repurposing use cases. For Naive B cells from Rheumatoid Arthritis (RA) paired with healthy controls, the system quantified the metabolic rewiring driving disease, prioritized candidate reactions using topological hub filtering and robustness analysis, and surfaced Devimistat as a potential repurposing candidate acting through 2-oxoglutarate dehydrogenase in the TCA cycle. In a paired CD4+ Th17 cell study from Multiple Sclerosis (MS) and healthy controls, the same workflow identified NADP-dependent isocitrate dehydrogenase as the optimal single target and proposed ivosidenib as an FDA-approved repurposing candidate. Together, these results show that MechAInistic interfaces directly with mechanistic modeling and turns large language model reasoning into reproducible biological discovery. MechAInistic is accessible at https://mechainistic.dtih.org.

### 12. EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery
- Deep score: 0.3
- Date: 2026-07-13T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.08.737358
- Summary: Motivation: As biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers. Result: EcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAI's multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimer's Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

### 13. Autonomous computational prioritisation of colorectal cancer vulnerabilities via multi-scale AI swarms
- Deep score: 0.3
- Date: 2026-07-10T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, human augmentation / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.05.736565
- Summary: The acceleration of automated scientific discovery has been fundamentally bottlenecked by the epistemic gap between the semantic reasoning of large language models (LLMs) and the complex, non-linear reality of mammalian biology. While recent multi-agent frameworks have achieved autonomous hypothesis generation and in vitro experimental analysis, they frequently lack the rigorous statistical constraints required for multi-scale clinical translation. Furthermore, while algorithmic clinical digital twins successfully forecast biological states, they often rely on opaque latent spaces, sacrificing mechanistic interpretability for predictive accuracy. Here, we introduce the Multi-Scale Autonomous Discovery Engine (Octopus), a neuro-symbolic framework that unites a fully localised, privacy-preserving multi-agent swarm with regularised predictive algorithmic environments. Rather than stopping at isolated cellular assays, the system autonomously prioritises therapeutic hypotheses against in vitro CRISPR dependency data (CCLE), traces feature attribution cascades using XGBoost SHAP vectors, and orthogonally translates emergent vulnerabilities in silico to predict in vivo mammalian tumour trajectory (PDX) and human overall survival (Marisa). In a fully unsupervised sweep of colorectal cancer transcriptomes, the pipeline autonomously prioritised Insulin-like Growth Factor 2 (IGF2) as a significant candidate vulnerability to 5-Fluorouracil resistance. The discovery maintained significance after rigorous Benjamini-Hochberg false discovery rate correction (q = 0.0292, Log-Rank p = 0.0007) and successfully predicted significant in vivo tumour volume shrinkage in an independent mouse cohort (Mixed-Effects LMM p = 0.0373). By bridging agentic hypothesis generation with statistically bounded clinical survival, this framework establishes a verifiable, local paradigm for the automated computational prioritisation of biomedical discoveries.

### 14. CellPilot: an agentic framework that pilots small language models through autonomous single-cell annotation
- Deep score: 0.3
- Date: 2026-07-10T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.06.736807
- Summary: Large language models can annotate cell types from marker gene lists, but they typically operate after preprocessing and clustering are complete, treating annotation as a terminal labeling step rather than controlling the analytical decisions that produce the evidence for cell identity. We present CellPilot, an agentic framework that guides a locally deployable small language model through the full single-cell analysis workflow, from raw count matrices to cluster-level annotation. CellPilot combines standard single-cell analysis tools with structured workflow control and observation-guided reasoning, allowing the model to plan analyses, execute tools, inspect intermediate results and revise decisions within a traceable session. On GTEx, structured workflow orchestration raised the same 8B model from 0.39 in a prompt-only setting to 0.89, closing most of the gap to GPT-4o (0.92) within the same framework; the framework gain was substantially larger for the smaller backbone across datasets (+0.35 versus +0.19). Across GTEx, Tabula Sapi- ens, and Mouse Cell Atlas, CellPilot achieves cluster-level annotation accuracies of 0.891, 0.750, and 0.773, outperforming representative reference-based, marker-based, and LLM-based methods. CellPilot confidence scores were associated with annotation correctness and supported post hoc filtering, while complete execution traces were retained for each analysis. These results suggest that structured workflow orchestration can be a critical determinant of performance in multi-step single-cell analysis, enabling locally deployable small language models to approach larger proprietary models while preserving transparency and practical usability.

### 15. Towards Agentic AI Governance: A Preliminary Assessment
- Deep score: 0.3
- Date: 2026-07-08T16:29:18+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.07612
- Summary: Artificial intelligence is rapidly evolving from generative systems to agentic AI capable of autonomously planning and executing tasks. Widely characterized as the Year of Agentic AI, 2025 marked accelerated development and deployment, introducing new ethical and governance challenges. This paper presents a systematic review of the emerging literature on agentic AI governance. Our analysis identifies features that distinguish agentic AI from traditional systems and why it warrants targeted governance attention. We synthesize prevailing governance priorities, proposed mechanisms, and stakeholder roles shaping this evolving domain. As an initial scholarly effort, this review lays the preliminary groundwork for developing a structured roadmap to guide responsible and adaptive agentic AI governance.

### 16. Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation
- Deep score: 0.3
- Date: 2026-07-08T16:26:06+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.07608
- Summary: Mainstream Vision-Language-Action (VLA) models predict actions primarily from the current observation under a Markovian assumption, thus struggling with long-horizon, temporally dependent tasks. Existing memory-augmented VLAs either expand the observation window or retrieve history from the memory bank as auxiliary policy-side context. However, they leave memory outside the native latent embedding space of VLA reasoning, preventing historical experience from being fluidly interleaved with multimodal reasoning and action formation. To this end, we introduce LaMem-VLA, a latent-memory-native framework that reconstructs historical experience into latent memory tokens and directly interweaves them with VLA reasoning. At its core, LaMem-VLA introduces four coordinated components: (i) a curator that organizes historical experience into two complementary short-term and long-term memory vaults; (ii) a seeker that queries both vaults using the multimodal cognition to retrieve context-relevant evidence; (iii) a condenser that reconstructs the retrieved evidence into compact short-term and long-term latent memory tokens; and (iv) a weaver that injects these memory tokens with the current observation and instruction into one continuous embedding sequence. By representing, retrieving, and consuming historical experience entirely in the same continuous latent space, LaMem-VLA enables memory to directly participate in VLA reasoning and guide action generation under a bounded context. Extensive experiments on SimplerEnv and LIBERO demonstrate the superiority of our LaMem-VLA.

### 17. Multi-Agent Robotic Control with Onboard Vision-Language Models
- Deep score: 0.3
- Date: 2026-07-08T13:37:31+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.07403
- Summary: Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial warehouse, fulfilling five task categories: safety inspection, warehouse maintenance, warehouse search, package quality verification, and responding to human requests. Compact VLMs (3-20B parameters) are used throughout, with fine-tuning applied to improve package inspection accuracy. A novel "Megamind" orchestration agent mitigates context retention issues inherent to long-horizon planning with smaller models. The system was validated in a hardware-in-the-loop simulation using an AMD Ryzen(TM) AI mini PC. Results demonstrate that a fully onboard MAS architecture is a viable, cost-efficient alternative to cloud-dependent deployments, with strong potential for real-world transfer. The simulation environment has been released as open source under the Apache 2.0 licence.

### 18. Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses
- Deep score: 0.3
- Date: 2026-07-06T13:10:13+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.05029
- Summary: Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals. We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA's attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent's retrieved content but also the integrity of its reasoning history.

### 19. Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory
- Deep score: 0.3
- Date: 2026-07-06T00:00:00+00:00
- Source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2607.05511
- Summary: Agentic video understanding equips models with long-term memory to autonomously process and respond to continuous, long-horizon multimodal streams. However, advanced video agents often rely on ``detective-style'' iterative reasoning for action control (e.g., search) and evidence aggregation, incurring prohibitive costs and latency. We argue that such heavy reasoning primarily compensates for the lack of global context and semantic misalignment in retrieval. This paper introduces Light-Omni, a multimodal agent framework for reflexive and lightweight video understanding. It achieves this through dual contextual states that instantly build the required context in a single forward pass. First, we maintain a global state, a finite-sized multimodal script continuously consolidated from episodic memory, serving as the global context for Light-Omni. Through hierarchical merging, it preserves recent details while summarizing past events. Second, conditioned on this global context, we generate a parametric latent state that directly drives autonomous actions and produces retrieval embeddings, with minimal latency. Benefiting from this coupled design, Light-Omni achieves semantically aligned retrieval and reflexive responses while avoiding iterative reasoning. Extensive experiments validate the effectiveness of Light-Omni across multiple video benchmarks. Notably, it outperforms M3-Agent with an average 2.4% accuracy gain, a 12.1times speedup, and a 2.6times improvement in GPU memory efficiency. Furthermore, it serves as a memory system to enhance both the performance and efficiency of existing MLLMs. Project page: https://clare-nie.github.io/Light-Omni.

### 20. A Common Neural Signal of Evidence Accumulation for Perceptual and Mnemonic Decisions
- Deep score: 0.3
- Date: 2026-07-06T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://www.biorxiv.org/content/10.1101/2025.11.13.688140
- Summary: Humans frequently make decisions based on sensory input from the external environment or information retrieved from memory. The centro-parietal positivity (CPP), an event-related EEG potential, has recently been identified as a neural correlate of sensory evidence accumulation during perceptual decision-making tasks. However, it remains unclear whether this component also reflects the accumulation of evidence in service of decisions grounded in semantic and episodic long-term memory. Across two experiments, we investigated whether the CPP serves as a domain-general neural signal of evidence accumulation. In Experiment 1, participants completed 2AFC perceptual and semantic memory tasks with varying levels of evidence strength. Perceptual judgements involved luminance discrimination of alphanumeric strings with three luminance difference levels controlling perceptual evidence strength. Semantic memory judgements involved discriminating population differences between U.S. states with census data used to define three bins of memory evidence strength. A CPP component was observed in both tasks whose build-up rate (i.e., slope) scaled with evidence strength, response time, and confidence in both stimulus- and response-locked analyses. Extending these findings to episodic memory, participants in Experiment 2 completed a two-alternative forced-choice word recognition task with target words varying in exposure frequency during learning to control episodic memory strength. Again, we found that CPP slopes scaled with memory strength, response time, and confidence. Together, these findings support the CPP as a domain-general neural signature of evidence accumulation across perceptual, semantic, and episodic mnemonic decisions.

### 21. AGL-1: The Enterprise AI Governance Layer as a Control Plane for Trusted Enterprise Intelligence
- Deep score: 0.3
- Date: 2026-07-03T17:42:08+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.03516
- Summary: Enterprise artificial intelligence is moving from isolated experimentation toward operational dependency across copilots, retrieval-augmented generation systems, autonomous agents, and AI-enabled business workflows. As this transition accelerates, the primary enterprise challenge is no longer only model access or inference scale. It is governed intelligence operations: the ability to enforce authorization, preserve contextual lineage, control persistent memory, detect stale or conflicting knowledge, constrain agentic execution, and produce audit-ready evidence across distributed AI estates. This paper introduces AGL-1, the Enterprise AI Governance Layer, as a vendor-neutral reference model for the control plane that should operate across foundation models, retrieval systems, orchestration frameworks, enterprise memory, policy engines, observability systems, tools, APIs, and business applications. Building on governed knowledge-system principles introduced in GKS-5, AGL-1 generalizes the governance problem from retrieval-specific controls to full AI execution-path governance. It identifies recurring failure modes such as unauthorized retrieval, stale grounding, unmanaged memory, weak provenance, policy drift, fragmented observability, and uncontrolled autonomous execution. It then defines seven governance domains: identity-aware retrieval, policy enforcement, provenance management, memory governance, knowledge integrity monitoring, agentic execution control, and trust observability. The central claim is that durable enterprise value from AI will increasingly depend on the ability to govern intelligence at scale. In complex enterprises, trust is not a property of the model alone. It is a property of the system around the model: identity, knowledge, policy, memory, tools, human oversight, and evidence working together as a managed control plane.

### 22. MemSyco-Bench: Benchmarking Sycophancy in Agent Memory
- Deep score: 0.3
- Date: 2026-07-01T15:30:33+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.01071
- Summary: Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of factual accuracy or objective reasoning. Despite this emerging risk, existing memory benchmarks primarily evaluate whether memories are correctly stored, retrieved, or updated, while overlooking how retrieved memories influence downstream reasoning and decision-making. To bridge this gap, we propose MemSyco-Bench, a comprehensive benchmark for evaluating memory-induced sycophancy in agent systems. MemSyco-Bench measures when memory should influence a decision and how valid memory should be used. Specifically, it covers five tasks that assess whether agents can reject memory as factual evidence, respect its applicable scope, resolve conflicts between memory and objective evidence, track memory updates, and use valid memory for personalization. All related resources are collected for the community at https://github.com/XMUDeepLIT/MemSyco-Bench.

### 23. Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems
- Deep score: 0.3
- Date: 2026-06-30T08:41:00+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.31339
- Summary: Agentic artificial intelligence is increasingly used to decompose industrial tasks, propose robot actions, and adapt execution plans in dynamic cyber-physical environments. However, autonomous proposal generation alone does not guarantee that multi-robot industrial systems preserve task dependencies, resource ownership, safety holds, or repair boundaries during long-horizon execution. This paper introduces a verification-gated agentic mission-state governance framework for intelligent industrial multi-robot systems. The framework maintains two synchronized state objects: an evolving task forest for persistent hierarchy, delayed grounding, and repairable substructures; and a governed blackboard for online execution state, robot traces, resource locks, world beliefs, proposals, verification records, and scene-temporary constraints. From each forest--blackboard snapshot, a derived execution coupling topology exposes cross-branch dependencies for proposal verification, parallel-commit eligibility, and bounded repair. Candidate assignments, repairs, deferrals, and constraint updates may be generated by heuristic, optimization, or agentic reasoning modules, but they can update the committed mission state only after deterministic verification and atomic commit. We evaluate the framework in an indoor factory multi-robot scenario, 30-seed remote-construction stress benchmarks, structural ablations, and scalability probes. The results show improved verified and safety-audited mission-state progress with fewer invalid commitments, lock conflicts, duplicate assignments, abandoned nodes, and disruptive repairs under modeled mission predicates. The study positions agentic AI as a proposal-generating layer governed by inspectable mission-state verification rather than as an unchecked execution authority.

### 24. Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation Threats
- Deep score: 0.3
- Date: 2026-06-29T13:07:41+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.30259
- Summary: In contemporary societies, the threat of disinformation has reached alarming levels, exacerbated by the proliferation of electronic communication, social media, and advancements in artificial intelligence. As a result, there is an urgent need to develop effective countermeasures to mitigate this menace. However, the sheer scale of the problem renders manual fact-checking and human-based verification inadequate, underscoring the necessity for automated methods to detect and debunk disinformation. This article proposes a novel approach based on a multi-agent system that emulates the decision-making processes of human annotators engaged in disinformation detection tasks. By incorporating a consensus mechanism, diversity in cognition and diversity in knowledge, and also hierarchical structure, inspired by human annotators' behavior, the proposed method achieves superior results compared to individual Large Language Models (LLMs), including GPT 4 and GPT 3.5. The system leverages open models (e.g., LLaMA, Kimi, Qwen, Deepseek and LLaMA-Nemotron) to ensure greater transparency. The evaluation of the proposed method encompasses datasets in languages with varying resource availability, including English (high-resource), Polish (medium-resource), Slovak (low-resource) and Bulgarian (low-resource). Experiments were conducted on tasks such as direct disinformation detection, identification of texts worthy of verification, and detection of texts containing verifiable factual claims.

### 25. A Multi-Agent system for Multi-Objective constrained optimization
- Deep score: 0.3
- Date: 2026-06-18T13:47:28+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.20236
- Summary: Many decision-making problems in computing and networking systems can be naturally formulated as cost-minimization problems under performance constraints. In dynamic environments, reinforcement learning (RL) is often used to solve such problems at runtime by embedding both costs and constraint violations into a single scalar reward through weighted penalty terms, following a Lagrangian-inspired formulation. However, in this context the behavior of the learned policy critically depends on the choice of these weights, which are typically selected manually. This makes it difficult to identify an appropriate trade-off between optimizing the primary objective and effectively avoiding constraint violations, particularly in non-stationary environments where their relative importance may change. This paper presents MAMO (Multi-Agent system for Multi-Objective constrained optimization), an approach to tackle this balancing problem through multi-agent RL. MAMO decouples task execution from objective design by formulating the selection of reward weights as a learning problem, providing a !rst step towards more autonomous and robust RL-based solutions for constrained optimization problems in dynamic environments.

### 26. GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning
- Deep score: 0.3
- Date: 2026-06-16T03:45:24+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.17480
- Summary: Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Second, the original KnowledgeBank mainly retrieves semantically similar snippets and appends new knowledge, which makes it difficult to control memory quality, conflicts, confidence, and geometric relevance. To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance. To address the second challenge, we upgrade KnowledgeBank into a governed long-term memory system with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while reducing AS by 4.95% and 5.65%, respectively. Code: https://github.com/AIGeeksGroup/GeneralVLA-2. Website: https://aigeeksgroup.github.io/GeneralVLA-2.

### 27. Misinformation Propagation in Benign Multi-Agent Systems
- Deep score: 0.3
- Date: 2026-06-15T13:40:01+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.16710
- Summary: Multi-agent systems, in which multiple large language model agents solve problems through turn-based interaction, are increasingly deployed in high-stakes settings such as medical diagnosis, legal analysis, and forensic decision-making. Their reliability can be at risk when single agents reason from incorrect or misleading context, e.g., from tool calls, since errors may propagate through agent interactions. This work studies this risk by injecting intent-based misinformation into benign single-agent and multi-agent systems across reasoning, knowledge, and alignment tasks. We find that misinformation can degrade single-agent performance and persists across multi-agent debate, with agents often retaining answers introduced by misinformed peers. Nevertheless, multi-agent debate reduces the resulting performance degradation compared to single-agent prompting, especially when most agents are not exposed to misinformation. Robustness depends on group composition and decision protocol. Consensus can be more stable than voting under peer pressure, while majorities can often steer misinformed agents back toward correct answers. Our results show that misinformation robustness in multi-agent systems depends on the underlying model and also on how agents exchange information and aggregate decisions.

### 28. Decentralized Multi-Agent Systems with Shared Context
- Deep score: 0.3
- Date: 2026-06-09T10:13:07+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.10662
- Summary: Multi-agent systems (MAS) can scale large language model reasoning at test time by decomposing complex problems into parallel subtasks. However, most existing MAS rely on centralized orchestration, where a main agent assigns work, collects outputs, and merges results. As the number of subtasks grows, this controller becomes a communication and integration bottleneck. We propose Decentralized Language Models (DeLM), a MAS framework that decentralizes coordination through parallel agents, a shared verified context, and a task queue. Agents asynchronously claim subtasks, read accumulated progress, perform local reasoning, and write back compact verified updates. The shared context acts as a common communication substrate, enabling agents to build on one another's verified progress without routing every update through a central controller. Empirically, DeLM improves both software-engineering test-time scaling and long-context reasoning. On SWE-bench Verified, DeLM achieves the best performance across Avg.@1, Pass@2, and Pass@4, with gains of up to 10.5 percentage points over the strongest baseline, while reducing cost per task by roughly 50%. On LongBench-v2 Multi-Doc QA, DeLM achieves the highest average accuracy across four frontier model families, improving over the strongest baseline by up to 5.7 percentage points. The code is available on our project website at https://yuzhenmao.github.io/DeLM/.

### 29. Distilling LLM Reasoning into an Interpretable Policy Tree for Human-AI Collaboration
- Deep score: 0.3
- Date: 2026-06-07T12:20:32+00:00
- Source: arxiv
- Focus/tech: cognitive outsourcing, AI agents / cognitive outsourcing
- URL: https://arxiv.org/abs/2606.08596
- Summary: Constructing efficient and reliable policies to assist humans is indispensable for human-AI collaboration. Existing methods mainly follow two lines of work. Most prior work relies on multi-agent reinforcement learning (MARL) to learn black-box policies, which limits interpretability and raises safety concerns. Recent methods query large language models (LLMs) at each decision step, causing slow responses and high inference costs. We propose Collaboration Policy Tree (Co-pi-tree), a closed-loop method that learns an executable policy tree consisting of a partner-behavior prediction tree and an agent-action selection tree. Co-pi-tree constructs a policy by distilling LLM reasoning into policy tree code. It then evaluates the policy through partner interaction, obtains feedback, and uses natural language to summarize the interaction feedback to improve problematic branches. Experiments in Overcooked-AI show that Co-pi-tree improves average reward by 35.4% over the baseline average, while reducing the number of LLM queries by 77.7% and test-time latency by 97.1%. Project page: https://beiwenzhang.github.io/Co-pi-tree/

### 30. Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems
- Deep score: 0.3
- Date: 2026-06-04T05:10:20+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.05711
- Summary: Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. The dominant communication protocol in such systems is natural language: agents exchange messages token-by-token, verbalising their internal reasoning so that peers can read, verify, and respond. While convenient and interpretable, this protocol suffers from three structural drawbacks -- high inference cost, irreversible information loss during discretization, and ambiguity/redundancy of natural language. A growing body of work therefore explores an alternative protocol -- latent communication -- in which agents exchange continuous representations (embeddings, hidden states, or KV-caches) directly, bypassing the bottleneck of text generation. This paper presents a unified framework for organising the rapidly expanding literature on latent communication. We analyse existing methods along three orthogonal axes: (1) WHAT information is communicated (Embeddings, Hidden States, KV-Caches, or other continuous state); (2) WHICH sender-receiver alignment is used (latent-space alignment and layer alignment); and (3) HOW the communicated information is fused into the receiver (concatenation, prepending, mathematical operations, cross-attention, or cache restoration). Under this 3-axis framework, we systematically categorise eighteen representative methods proposed between 2024 and 2026, identify five major design patterns, and surface a set of open challenges -- including cross-architecture alignment, security of latent channels, compression for edge deployment, and the relationship between latent communication and latent chain-of-thought. We hope that this framework both lowers the barrier to entry for new researchers and provides a vocabulary for comparing future work.
