# Blindspot Signals Report - 2026-07-20

- Source export: `/opt/apps/haier/exports/evolution_signals_20260720_020420.json`
- Total signals in export: 5000
- Agent-relevant signals: 513
- Novel vs previous reports: 217
- Filter: `focus_area` or `technology_type` contains `AI agents` or `AI decision delegation`

## New Signals Since Previous Reports

### 1. Hugging Face Says an Autonomous AI Agent Swarm Breached Its Systems Over a Weekend - Startup Fortune
- Deep score: 0.1
- Date: 2026-07-19T14:43:07+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMirwFBVV95cUxNN2xSVVRUUE03SDV1WXl1WldQTUc3SXV5bXJiOWNCclF6eGZBZkl5Ynhvd1I2ZEh3Z0UyN2xvVWdYVjBQTnNvaEpDWjZNajhkQ0JhRGdEZFBNbHFiMFlEdXRQd0dqdW9JY3oxMVRvV3BaMUtYVEsyeHlTT04wbERROWI1VVBXcXI4bEs4V19Cc2ttTVdVamMwMnNqUjRWd0p3LWp2ZzFUZTFLaXo1Vkpn?oc=5
- Summary: Hugging Face Says an Autonomous AI Agent Swarm Breached Its Systems Over a Weekend&nbsp;&nbsp;Startup Fortune

### 2. Canner / WrenAI
- Deep score: 0
- Date: 2026-07-20T02:01:45.866533+00:00
- Source: github_trending
- Focus/tech: AI agents / AI agents
- URL: https://github.com/Canner/WrenAI
- Summary: GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.

### 3. Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k
- Deep score: 0
- Date: 2026-07-12T18:25:51+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://systima.ai/blog/claude-code-vs-opencode-token-overhead
- Summary: This started based off of a hunch. We usually use OpenCode, but were &#x27;forced&#x27; to use Claude Code for a while due to issues with Meridian. In that time, we saw the usage meter rise much, much more quickly than when using OpenCode.<p>This was the initial anecdotal evidence, but we undertook this small study to collect empirical data:<p>We added logging between the agentic coding tool (Claude Code and OpenCode) and Anthropic&#x27;s endpoint, and captured all requests (and the returned usage blocks).<p>With one caveat (toward the end of the post) we found unambiguously that Claude Code was far more inefficient in terms of its cache strategy and its harness token usage than OpenCode.

### 4. Migrating a production AI agent to GPT-5.6: 2.2x faster, 27% cheaper
- Deep score: 0
- Date: 2026-07-12T17:13:07+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6
- Summary: No summary.

### 5. One Wikipedia page costs your AI agent 68,000 tokens
- Deep score: 0
- Date: 2026-07-11T00:12:26+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://news.ycombinator.com/item?id=48867021
- Summary: i use claude code daily and measured what pages cost it while doing research. an average wikipedia article, for instance, is 68,240 tokens of raw html (tiktoken); nike&#x27;s homepage is 353,000.<p>claude code&#x27;s built-in webfetch handles the easy case well. it summarizes wikipedia to about 950 tokens and clears cloudflare on some sites like indeed and ticketmaster. but, and there&#x27;s always a but, on js-rendered and some anti-bot pages it returns nothing.<p>quotes.toscrape.com&#x2F;js gives &quot;no quotes found&quot;; nike.com gives a 403. your agent then dumps the raw html back into context and still fails. (note: i have also had cases where i read through the chat at the end and saw that it failed and just pulled from either training data or stale caches from other sources)<p>so i worked on building an open-source stealth browser (recompiled chromium) that runs as an mcp for claude code, cursor, and claude desktop. essentially all i have to change form my end is add the mcp, and it returns the cleaned up tokens while also beating detection: the js quotes come back in 285 tokens, nike in about 700 instead of a 403.<p>there is still stuff i am actively working on: there&#x27;s no residential egress yet, and it won&#x27;t beat kasada-style walls. it&#x27;s for agents, qa, and research.<p>repo and the reproducible benchmark: https:&#x2F;&#x2F;github.com&#x2F;tiliondev&#x2F;fortress&#x2F;tree&#x2F;main&#x2F;mcp i&#x27;m the author and here for feedback.

### 6. NoMac.app
- Deep score: 0
- Date: 2026-07-10T21:07:45+00:00
- Source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/nomac
- Summary: <p> The headless iOS app publishing pipeline for AI agents. </p> <p> <a href="https://www.producthunt.com/products/nomac?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1193239?app_id=339">Link</a> </p>

### 7. Advancing from level II to level III AI agents in precision medicine - The Cancer Letter
- Deep score: 0
- Date: 2026-07-10T19:50:04+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMibEFVX3lxTE1TT0hXbmpLcmdNR2dSbW5BTVFweUx5YWJVZTN3M0JObkhVbnNpMnVnemhrdUFYdGpNV0ZfN3ExbXNhbkRHRjFaNUM0WS1rdHdVc01wOGlQTkFyR084WjVOam11STBtVFhadktlRQ?oc=5
- Summary: Advancing from level II to level III AI agents in precision medicine&nbsp;&nbsp;The Cancer Letter

### 8. Show HN: SubjectiveZero, an open-source agentic node editor for creative coding
- Deep score: 0
- Date: 2026-07-10T15:23:50+00:00
- Source: hackernews
- Focus/tech: AI agents, robotics / AI agents
- URL: https://sxp.studio/apps/subz
- Summary: Hey there,<p>My name is Clem, I&#x27;ve been a solo indie dev for a couple years now, exploring frontier tech like XR and agentic workflows in the context of creative &#x2F; interactive work.<p>I&#x27;ve been building creation tools for a while and some common design challenge is to figure out the right level of abstraction for your tool. You can always make it super advanced and complex with low level concepts (shader composition, actual code etc.) but then you get something with a high complexity &#x2F; learning curve. On the other hand, if you make your tool too high level, it might be easier to use at first, but people will most likely hit a wall eventually and start fighting with your tool to get their edge case done (you see that on mobile a lot actually).<p>With this prototype (called SubjectiveZero), I&#x27;d like to imagine that we can kind of move the &quot;slider&quot; on the abstraction layer, meaning that you can actually start with prompts that describe the goal, and you can go as high level (stay with abstract prompts) or low level as you&#x27;d like (more specific prompts, or even edit the generated code directly)! The agent orchestration actually understand your context and work along side with you to figure out what could be the best node graph structure for your project (that and some fun little procedural UI done at the node level).<p>If i had to pitch it in 30 seconds, I&#x27;d say &quot;Think TouchDesigner and friends but with agent orchestration&quot;.<p>When you use it, it will generate real native code (Swift&#x2F;Metal for now) that you can actually hot reload and iterate on either manually or through agents. It&#x27;s still an early prototype and macOS only for now, but I&#x27;d love to get genuine feedback that could help me drive where this project should go next (or not).<p>Lastly, I&#x27;m absolutely open and upfront on the fact that I used agentic coding for this, but as people say: &quot;kept on a short leash&quot;. The …

### 9. Fudge MCP
- Deep score: 0
- Date: 2026-07-10T14:06:45+00:00
- Source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/fudge-mcp
- Summary: <p> Give your AI agents design taste from existing websites </p> <p> <a href="https://www.producthunt.com/products/fudge-mcp?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1192979?app_id=339">Link</a> </p>

### 10. OpenAI says GPT 5.6 is the ‘preferred model’ for Microsoft Copilot 365 amid breakup chatter
- Deep score: 0
- Date: 2026-07-10T00:16:54+00:00
- Source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/07/09/openai-says-gpt-5-6-is-the-preferred-model-for-microsoft-copilot-amid-breakup-chatter/
- Summary: OpenAI's new family of models will continue to power Microsoft's suite of workplace and productivity apps.

### 11. AI Agent Raises Own $100M Round in Wild Fundraising First - The Tech Buzz
- Deep score: 0
- Date: 2026-07-09T22:46:00+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMikwFBVV95cUxOM1oya3RMN2ZWaTFJTzdINlZpWHoxRVpoRXhYZjRxdVpFUVlEMmV1djRaMlZtRDVFd2tzMFFhU2I3bkgyRDJmZDJnVVpIbVcxRDAycFptampUX2UtT09EU05ST3diOFMwcFpaVTVoWEcyYWg4WWJzYWlqZDAwSjdnbExvSTZPckN3UFZXTGM2V3NDUk0?oc=5
- Summary: AI Agent Raises Own $100M Round in Wild Fundraising First&nbsp;&nbsp;The Tech Buzz

### 12. An AI agent startup just let its agent run its $100M fundraise
- Deep score: 0
- Date: 2026-07-09T22:08:58+00:00
- Source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/07/09/an-ai-agent-startup-just-let-its-agent-run-its-100-million-fundraise/
- Summary: Lyzr, a startup that builds AI agents for enterprises, used its own AI agent to raise a $100 million round — proof, evidently, that the product actually works.

### 13. OpenAI is shutting down Atlas, but its AI browser ambitions are still growing
- Deep score: 0
- Date: 2026-07-09T22:03:54+00:00
- Source: techcrunch
- Focus/tech: AI agents, robotics / AI agents
- URL: https://techcrunch.com/2026/07/09/openai-is-shutting-down-atlas-but-its-ai-browser-ambitions-are-still-growing/
- Summary: OpenAI is sunsetting its AI-powered browser after less than a year. But it's moving some agentic browsing features to its desktop app and a Chrome extension.

### 14. UN digital tech agency launches initiative to improve trust in AI agents - Reuters
- Deep score: 0
- Date: 2026-07-09T21:17:34+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiuwFBVV95cUxOLW40R0Vic01SdnN0WVBwcV9xUGU5NDkyVUhmVFEtV05xRllhZUdIZEhUSWEwOEt6OUdFZnVheG8wMFh1eGo2QmxDLW5ZNmN5RHNPcm44VTJtZ1EzdzRVXy0yNFJaVWx2VnNMNUtTa2d4cHRHOHVfbkhBZzUxMUxERXNaS1BPVXFtQThJOHdqVzJoaVdIOUVhWEQzSFg3TUhxUUxvQVdxaWNxY195MHRMZ3MybFAyYzFLVXkw?oc=5
- Summary: UN digital tech agency launches initiative to improve trust in AI agents&nbsp;&nbsp;Reuters

### 15. Meta enters the crowded AI coding battle with Muse Spark 1.1
- Deep score: 0
- Date: 2026-07-09T19:40:45+00:00
- Source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/07/09/meta-enters-the-crowded-ai-coding-battle-with-muse-spark-1-1/
- Summary: Meta's pitch to users is Spark's ability to handle large agentic workloads, fix bugs, and help with large code migrations — the kind of automation that enterprises are increasingly turning to AI companies to provide.

### 16. Show HN: Reverse-engineering web apps into agent tools
- Deep score: 0
- Date: 2026-07-09T15:45:17+00:00
- Source: hackernews
- Focus/tech: AI agents, robotics / AI agents
- URL: https://news.ycombinator.com/item?id=48847834
- Summary: Hey HN! We built a browser-based agent that runs inside an authenticated web app, watches how the app calls its own APIs, and automatically turns those into agent tools. You can think of it as an auto-generated MCP server that self-updates as the host app changes.<p>The result is a skilled AI assistant that actually integrates deeply with any product (not just chat and RAG) with minimal effort.<p>Check out these short demos below that show the agent in software you&#x27;re probably familiar with:<p>- Jira: <a href="https:&#x2F;&#x2F;demo.frigade.com&#x2F;hn?skill=jira">https:&#x2F;&#x2F;demo.frigade.com&#x2F;hn?skill=jira</a><p>- Spotify: <a href="https:&#x2F;&#x2F;demo.frigade.com&#x2F;hn?skill=spotify">https:&#x2F;&#x2F;demo.frigade.com&#x2F;hn?skill=spotify</a><p>- Hacker News (lol): <a href="https:&#x2F;&#x2F;demo.frigade.com&#x2F;hn?skill=hackernews">https:&#x2F;&#x2F;demo.frigade.com&#x2F;hn?skill=hackernews</a><p>- Full Demo: <a href="https:&#x2F;&#x2F;demo.frigade.com&#x2F;hn?skill=full-demo">https:&#x2F;&#x2F;demo.frigade.com&#x2F;hn?skill=full-demo</a><p>As you can see in the examples, you can do way more (and faster) than what you normally would be able to via point and click. And we never even touched the source code of these products!<p>Why do this?<p>In an ideal world, every application has an MCP server or an easily-digestible API available for AI agents to feed from. In practice, we found that even very modern software tends to have a spider web of confusing APIs and services that AI agents simply cannot use out of the box. Security also becomes a huge issue as applications have different (often homebrewed) standards for how endpoints are secured (JWTs&#x2F;cookies&#x2F;mix of both). Finally, having an actual browser agent go in and use the application on behalf of the user (i.e. computer-use), is simply too brittle, slow, and burns a lot of tokens.<p>We took our existing browser agent that’s already trained to use and learn authenticated …

### 17. Altman: GPT-5.6 is 54% more token efficient on agentic coding
- Deep score: 0
- Date: 2026-07-09T14:25:13+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://www.cnbc.com/2026/07/09/open-ai-sam-altman-chatgpt-5-6-sol.html
- Summary: No summary.

### 18. UN digital tech agency launches initiative to improve trust in AI agents - Yahoo
- Deep score: 0
- Date: 2026-07-09T13:29:42+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMilAFBVV95cUxQX2k5d3hoNFJYR05BWTYtNmFJSjBRUHNPaVlCVWthc0thU3ZkcVFDa1c3N0otZ1E0UllwY1RLRGwwRFpjOGRFcElHXzZEeW9FdkU1T2ZGeDRrSzRQWHhDN0NkRkRsbFY5dm9LRDR6bFB4VTBCeEc2S05rRTAzOWJZN1RkS2dUdnJybkhHN0dkZUJxZnQ3?oc=5
- Summary: UN digital tech agency launches initiative to improve trust in AI agents&nbsp;&nbsp;Yahoo

### 19. Show HN: FableCut – A browser video editor AI agents can drive (zero deps)
- Deep score: 0
- Date: 2026-07-09T13:23:10+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/ronak-create/FableCut
- Summary: No summary.

### 20. Mispher
- Deep score: 0
- Date: 2026-07-09T09:36:54+00:00
- Source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/mispher-agentic-transcription-for-mac
- Summary: <p> Dictate, rewrite, translate, and an agent in a single device </p> <p> <a href="https://www.producthunt.com/products/mispher-agentic-transcription-for-mac?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1191918?app_id=339">Link</a> </p>

### 21. Agentic test processes, LLM benchmarks, and other notes on agentic coding fr
- Deep score: 0
- Date: 2026-07-08T20:21:45+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://danluu.com/ai-coding/#llm-variance
- Summary: No summary.

### 22. SpaceXAI releases Grok 4.5, which Elon describes as an ‘Opus-class model’
- Deep score: 0
- Date: 2026-07-08T19:30:16+00:00
- Source: techcrunch
- Focus/tech: AI decision delegation / AI decision delegation
- URL: https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/
- Summary: Elon Musk's tech company released the newest version of Grok on Wednesday, promising a cheaper, more efficient alternative to other powerful AI models.

### 23. Ask HN: How you manage local long lived research projects and LLM's?
- Deep score: 0
- Date: 2026-07-08T19:23:27+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://news.ycombinator.com/item?id=48836288
- Summary: TLDR: Do you have a pattern or structure for doing long-lived research or non-coding projects using LLMs?<p>I was kind of inspired by this hacker news article where someone collected data to solve their fatigue problem: https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=48605117<p>A similar but smaller I did was to collect nut-free restaurants to eat in Chicago. So I had articles, reviews, emails, phone calls, all sorts of stuff. I found it very easy to just use Copilot as my interface and I just data into it over and over and asked it to organize it.<p>https:&#x2F;&#x2F;github.com&#x2F;joshuabremer&#x2F;chicago-allergy-eats<p>This seems like a common thing where people would be working on a longer-term research or data collection task where you use the LLM to answer questions or help you accept the data. Does anyone have a standard format for this? Or an example that is working for you?

### 24. Sim
- Deep score: 0
- Date: 2026-07-08T18:55:06+00:00
- Source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/sim-studio
- Summary: <p> Open-source workspace for AI agents and workflows </p> <p> <a href="https://www.producthunt.com/products/sim-studio?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1191413?app_id=339">Link</a> </p>

### 25. Campus
- Deep score: 0
- Date: 2026-07-08T16:46:51+00:00
- Source: product_hunt
- Focus/tech: AI agents / AI agents
- URL: https://www.producthunt.com/products/flutterflow
- Summary: <p> One project space for humans and AI agents </p> <p> <a href="https://www.producthunt.com/products/flutterflow?utm_campaign=producthunt-atom-posts-feed&amp;utm_medium=rss-feed&amp;utm_source=producthunt-atom-posts-feed">Discussion</a> | <a href="https://www.producthunt.com/r/p/1191307?app_id=339">Link</a> </p>

### 26. Prime Intellect raises $130M Series A to help enterprises build their own AI agents
- Deep score: 0
- Date: 2026-07-08T16:22:38+00:00
- Source: techcrunch
- Focus/tech: AI agents / AI agents
- URL: https://techcrunch.com/2026/07/08/prime-intellect-raises-130m-series-a-to-help-enterprises-build-their-own-ai-agents/
- Summary: Founded in 2024, Prime Intellect’s goal is to give organizations capabilities to train their own agentic systems without relying on frontier AI labs.

### 27. Show HN: Kastor – Terraform-style specs for AI agents
- Deep score: 0
- Date: 2026-07-08T15:25:09+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://github.com/weirdGuy/kastor
- Summary: No summary.

### 28. China's new AI rules: Ethics, AI agents and anthropomorphic AI - IAPP
- Deep score: 0
- Date: 2026-07-08T15:14:29+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMijAFBVV95cUxPU2czdUNBOG10eGtxZ1RoU3NIYm53emthSHRtMG5SMEo5VjlyWUhuM3h4aFlDejI2aklXXzBzekN1SG5CRnpsVDZfcFFYTmVtVlltaElVMjJQX2dyaFRQS1BYNGdjbTBHcF8tb24zcXBPUWpVOVF6UjBjU2dYNEwzczRRRGZsM1R0aV94Ug?oc=5
- Summary: China's new AI rules: Ethics, AI agents and anthropomorphic AI&nbsp;&nbsp;IAPP

### 29. Codenotary launches AI security platform that learns from AI agent behavior - Help Net Security
- Deep score: 0
- Date: 2026-07-08T08:33:38+00:00
- Source: google_news
- Focus/tech: AI agents / AI agents
- URL: https://news.google.com/rss/articles/CBMiuwFBVV95cUxNYTJENWN6UjVEQVpTQlFtWXlXSWFiTUlnWUFhYVM3bUpfZExDUC0wSk5BeWlJV2xCY1VUWWV1akNjTFREa2FpRENhSmpRVXh5UlcycS05bHRERVhkZi1qZVZCUXl2MEI4eEVva29lTXlsX3VsYkpYUmlrMFlWVzVCa3lCUk02RFNQLU5ZNVVDUm1xNmI5VGkyZk5ORUgtV3NqT25rVkpndmxGTmE5dVhHdWRzOW9lcHRDb29R?oc=5
- Summary: Codenotary launches AI security platform that learns from AI agent behavior&nbsp;&nbsp;Help Net Security

### 30. GitLost: We Tricked GitHub's AI Agent into Leaking Private Repos
- Deep score: 0
- Date: 2026-07-08T05:25:35+00:00
- Source: hackernews
- Focus/tech: AI agents / AI agents
- URL: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/
- Summary: No summary.

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

### 4. A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation
- Deep score: 0.4
- Date: 2026-07-08T04:23:41+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2607.06990
- Summary: Multi-robot systems provide the parallelism and redundancy necessary for long-horizon tasks, while Large Language Models (LLMs) offer the reasoning capabilities to decompose these objectives into actionable plans. However, effectively grounding this high-level reasoning in physical multi-robot execution remains an open challenge. Existing LLM-based approaches fall mainly into two categories: Single-robot methods achieve robust contact-rich manipulation but lack the coordination mechanisms required for tasks spanning multiple workspaces. Current multi-robot frameworks focus on high-level planning, often treating manipulation as an idealized primitive that fails to account for real-world execution uncertainties. To address this, we propose a hierarchical closed-loop agentic LLM-based framework to ensure robust multi-robot manipulation. Our system consists of three specialized agents: the Planning Agent decomposes instructions into allocated sub-tasks, the Manipulation Agent for each robot executes actions via adaptive tool use, and the Verification Agent closes the loop by monitoring physical outcomes and feeding back semantic corrections. Extensive real-world experiments demonstrate that our framework achieves superior success rates, ensures robust adaptability ranging from single to cross workspace manipulation, and offers a generalizable approach for diverse manipulation tasks.

### 5. Trust Between AI Agents: Measuring Formation, Breakage, and Recovery, with Implications for Governing Multi-Agent Systems
- Deep score: 0.4
- Date: 2026-06-12T19:58:26+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.14923
- Summary: As language-model agents increasingly work in teams, each agent must decide how much to trust its teammates. Yet we lack a standard way to measure trust between AI agents. We propose a behavioral measure based on costly verification. In a cooperative survival game, checking a teammate's work consumes resources, while trusting a wrong answer can be fatal. Relative to a memoryless version of the same model, reduced verification provides an observable measure of trust. Using this framework, we study trust formation, breakage, and recovery across six frontier model snapshots. When paired with a consistently reliable teammate, four snapshots (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.1, and Gemini 3.1 Pro) reduce verification by roughly 60-85%, whereas two smaller snapshots show little or no such adjustment. Failures reverse this discount, but models differ in how they respond. Some concentrate renewed scrutiny on the culprit, while others become more cautious toward the entire team. Recovery is slower than formation, and clustered failures sustain suspicion far longer than the same number of failures spread apart. These differences have practical consequences. Models that form trust verify less, decide more quickly, and achieve higher payoffs in our environment. By contrast, persistent over-verification is associated with indecision rather than safety. Our results show that trust dispositions can be measured before deployment and suggest that calibration, rather than maximal suspicion, should be the central concern in the governance of multi-agent AI systems.

### 6. Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction
- Deep score: 0.4
- Date: 2026-06-10T10:37:27+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2606.11909
- Summary: Benchmarks are essential for evaluating embodied spatial intelligence, yet their construction is labor-intensive, hard to reuse, and difficult to maintain. Existing embodied benchmarks are often static and may quickly become saturated as models improve, limiting their ability to distinguish new capabilities. We propose Embodied-BenchClaw, an autonomous agentic system for constructing embodied spatial intelligence benchmarks. Given a user-specified evaluation intent, Embodied-BenchClaw automatically produces a complete and continually updatable benchmark package through a five-stage pipeline: intent blueprinting, data collection, structuring and cleaning, benchmark synthesis, and evaluation reporting. The pipeline is coordinated by three agents for planning, construction, and evaluation. To improve reusability and reliability, Embodied-BenchClaw introduces an extensible Skill Library and process quality control, enabling benchmark construction to be composable, verifiable, and repairable. We instantiate multiple benchmarks covering indoor spatial reasoning, outdoor spatial reasoning, robotic manipulation, quadruped robot navigation, UAV/aerial-view understanding, and static benchmark enhancement. These benchmarks span diverse embodied carriers, data sources, and spatial capabilities. Experiments with human evaluation, judge-based assessment, consistency checks, cost analysis, and ablations show that Embodied-BenchClaw can construct verifiable, executable, maintainable, and diagnostically useful embodied spatial benchmarks with reduced manual effort.

### 7. ConMem: Structured Memory-Guided Adaptation in Training-Free Multi-Agent Systems
- Deep score: 0.4
- Date: 2026-06-07T15:59:15+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.08702
- Summary: Recent advances have improved the adaptive capabilities of LLM-based multi-agent systems (MAS) through memory-, skill-, and learning-based approaches, yet these approaches remain challenged by noisy trajectories, insufficient modeling of memory-skill relations, and reliance on additional training or high-quality supervision. To address these limitations, we propose ConMem, a relation-aware and training-free framework that enables efficient multi-agent adaptation through cross-experience coordination. Specifically, ConMem distills historical interaction trajectories into structured memory cards to capture reusable strategies and cues, organizing them into a relation-aware memory graph. At runtime, ConMem retrieves cards according to task needs and coordinates them through the card graph to resolve strategy conflicts and recover their dependencies. Combined, these modules yield structured and relation-aware guidance, enabling robust, lightweight adaptation in multi-agent systems without additional training. Extensive experiments across multiple benchmarks and mainstream MAS architectures show consistent gains over existing memory architectures, with improved inference-time efficiency through pruning more than 50% of expanded candidates and reducing planning overhead by over 80%. Our codes are available at https://anonymous.4open.science/r/ConMemCode

### 8. DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning
- Deep score: 0.4
- Date: 2026-06-05T14:10:48+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.07299
- Summary: Deep Research (DR) has emerged as a new agentic paradigm to tackle complex, open-ended research tasks, demanding systems that can iteratively frame problems, acquire evidence, verify sources, and synthesize long-form reports. In practice, however, current DR systems are constrained by four interrelated limitations: long-horizon planning over an underspecified scope, the bottleneck of decomposing and scheduling such tasks within a single agent, hallucination risk in long-form synthesis, and limited process auditability. This technical report presents DuMate-DeepResearch, a multi-agent DR framework built on the Qianfan Agent Foundry. The framework decouples the Agent Core, which handles task understanding, planning, and scheduling, from an extensible Tool Ecosystem for retrieval, evidence acquisition, and report rendering, making every intermediate decision and tool invocation explicitly traceable. Building on this infrastructure, DuMate-DeepResearch further introduces three mechanisms: (i) a graph-based dynamic planning strategy expands the research roadmap coarse-to-fine and continuously revises it through reflection, re-planning, backtracking, and parallel branching; (ii) a recursive two-level execution design delegates each complex search sub-task to an inner Search Agent that runs its own planning loop, isolating noisy retrieval and stabilizing long-horizon execution; (iii) a rubric-based test-time optimization mechanism dynamically generates task-specific quality criteria and uses them as live reasoning scaffolds for evidence-grounded synthesis and adaptive stopping. Across two deep research benchmarks, DuMate-DeepResearch establishes new state-of-the-art results: the best overall score (58.03%) on DeepResearch Bench, and the best overall score (61.95%) on DeepResearch Bench II while ranking first in information recall and analysis.

### 9. MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models
- Deep score: 0.3
- Date: 2026-07-14T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.05.11.723319
- Summary: Constraint-based metabolic modeling is a powerful way to study the mechanistic basis of cellular states and disease, but its effective use demands substantial computational expertise and careful coordination of multi-step analyses. We developed MechAInistic to lower this barrier and enable researchers to ask complex biological questions in natural language. Harnessing large language models, MechAInistic is a multi-agent system organized around an Architect-Reviewer pattern that transforms a natural-language question into an executable, model-grounded workflow and generates a structured report. The system supports a variety of tasks, including pathway comparison, perturbation analysis, drug-target exploration, and literature-grounded interpretation across paired metabolic model states. We tested MechAInistic on two drug-repurposing use cases. For Naive B cells from Rheumatoid Arthritis (RA) paired with healthy controls, the system quantified the metabolic rewiring driving disease, prioritized candidate reactions using topological hub filtering and robustness analysis, and surfaced Devimistat as a potential repurposing candidate acting through 2-oxoglutarate dehydrogenase in the TCA cycle. In a paired CD4+ Th17 cell study from Multiple Sclerosis (MS) and healthy controls, the same workflow identified NADP-dependent isocitrate dehydrogenase as the optimal single target and proposed ivosidenib as an FDA-approved repurposing candidate. Together, these results show that MechAInistic interfaces directly with mechanistic modeling and turns large language model reasoning into reproducible biological discovery. MechAInistic is accessible at https://mechainistic.dtih.org.

### 10. EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery
- Deep score: 0.3
- Date: 2026-07-13T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.08.737358
- Summary: Motivation: As biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers. Result: EcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAI's multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimer's Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

### 11. Autonomous computational prioritisation of colorectal cancer vulnerabilities via multi-scale AI swarms
- Deep score: 0.3
- Date: 2026-07-10T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, human augmentation / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.05.736565
- Summary: The acceleration of automated scientific discovery has been fundamentally bottlenecked by the epistemic gap between the semantic reasoning of large language models (LLMs) and the complex, non-linear reality of mammalian biology. While recent multi-agent frameworks have achieved autonomous hypothesis generation and in vitro experimental analysis, they frequently lack the rigorous statistical constraints required for multi-scale clinical translation. Furthermore, while algorithmic clinical digital twins successfully forecast biological states, they often rely on opaque latent spaces, sacrificing mechanistic interpretability for predictive accuracy. Here, we introduce the Multi-Scale Autonomous Discovery Engine (Octopus), a neuro-symbolic framework that unites a fully localised, privacy-preserving multi-agent swarm with regularised predictive algorithmic environments. Rather than stopping at isolated cellular assays, the system autonomously prioritises therapeutic hypotheses against in vitro CRISPR dependency data (CCLE), traces feature attribution cascades using XGBoost SHAP vectors, and orthogonally translates emergent vulnerabilities in silico to predict in vivo mammalian tumour trajectory (PDX) and human overall survival (Marisa). In a fully unsupervised sweep of colorectal cancer transcriptomes, the pipeline autonomously prioritised Insulin-like Growth Factor 2 (IGF2) as a significant candidate vulnerability to 5-Fluorouracil resistance. The discovery maintained significance after rigorous Benjamini-Hochberg false discovery rate correction (q = 0.0292, Log-Rank p = 0.0007) and successfully predicted significant in vivo tumour volume shrinkage in an independent mouse cohort (Mixed-Effects LMM p = 0.0373). By bridging agentic hypothesis generation with statistically bounded clinical survival, this framework establishes a verifiable, local paradigm for the automated computational prioritisation of biomedical discoveries.

### 12. CellPilot: an agentic framework that pilots small language models through autonomous single-cell annotation
- Deep score: 0.3
- Date: 2026-07-10T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.06.736807
- Summary: Large language models can annotate cell types from marker gene lists, but they typically operate after preprocessing and clustering are complete, treating annotation as a terminal labeling step rather than controlling the analytical decisions that produce the evidence for cell identity. We present CellPilot, an agentic framework that guides a locally deployable small language model through the full single-cell analysis workflow, from raw count matrices to cluster-level annotation. CellPilot combines standard single-cell analysis tools with structured workflow control and observation-guided reasoning, allowing the model to plan analyses, execute tools, inspect intermediate results and revise decisions within a traceable session. On GTEx, structured workflow orchestration raised the same 8B model from 0.39 in a prompt-only setting to 0.89, closing most of the gap to GPT-4o (0.92) within the same framework; the framework gain was substantially larger for the smaller backbone across datasets (+0.35 versus +0.19). Across GTEx, Tabula Sapi- ens, and Mouse Cell Atlas, CellPilot achieves cluster-level annotation accuracies of 0.891, 0.750, and 0.773, outperforming representative reference-based, marker-based, and LLM-based methods. CellPilot confidence scores were associated with annotation correctness and supported post hoc filtering, while complete execution traces were retained for each analysis. These results suggest that structured workflow orchestration can be a critical determinant of performance in multi-step single-cell analysis, enabling locally deployable small language models to approach larger proprietary models while preserving transparency and practical usability.

### 13. Towards Agentic AI Governance: A Preliminary Assessment
- Deep score: 0.3
- Date: 2026-07-08T16:29:18+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.07612
- Summary: Artificial intelligence is rapidly evolving from generative systems to agentic AI capable of autonomously planning and executing tasks. Widely characterized as the Year of Agentic AI, 2025 marked accelerated development and deployment, introducing new ethical and governance challenges. This paper presents a systematic review of the emerging literature on agentic AI governance. Our analysis identifies features that distinguish agentic AI from traditional systems and why it warrants targeted governance attention. We synthesize prevailing governance priorities, proposed mechanisms, and stakeholder roles shaping this evolving domain. As an initial scholarly effort, this review lays the preliminary groundwork for developing a structured roadmap to guide responsible and adaptive agentic AI governance.

### 14. Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation
- Deep score: 0.3
- Date: 2026-07-08T16:26:06+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.07608
- Summary: Mainstream Vision-Language-Action (VLA) models predict actions primarily from the current observation under a Markovian assumption, thus struggling with long-horizon, temporally dependent tasks. Existing memory-augmented VLAs either expand the observation window or retrieve history from the memory bank as auxiliary policy-side context. However, they leave memory outside the native latent embedding space of VLA reasoning, preventing historical experience from being fluidly interleaved with multimodal reasoning and action formation. To this end, we introduce LaMem-VLA, a latent-memory-native framework that reconstructs historical experience into latent memory tokens and directly interweaves them with VLA reasoning. At its core, LaMem-VLA introduces four coordinated components: (i) a curator that organizes historical experience into two complementary short-term and long-term memory vaults; (ii) a seeker that queries both vaults using the multimodal cognition to retrieve context-relevant evidence; (iii) a condenser that reconstructs the retrieved evidence into compact short-term and long-term latent memory tokens; and (iv) a weaver that injects these memory tokens with the current observation and instruction into one continuous embedding sequence. By representing, retrieving, and consuming historical experience entirely in the same continuous latent space, LaMem-VLA enables memory to directly participate in VLA reasoning and guide action generation under a bounded context. Extensive experiments on SimplerEnv and LIBERO demonstrate the superiority of our LaMem-VLA.

### 15. Multi-Agent Robotic Control with Onboard Vision-Language Models
- Deep score: 0.3
- Date: 2026-07-08T13:37:31+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / robotics
- URL: https://arxiv.org/abs/2607.07403
- Summary: Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial warehouse, fulfilling five task categories: safety inspection, warehouse maintenance, warehouse search, package quality verification, and responding to human requests. Compact VLMs (3-20B parameters) are used throughout, with fine-tuning applied to improve package inspection accuracy. A novel "Megamind" orchestration agent mitigates context retention issues inherent to long-horizon planning with smaller models. The system was validated in a hardware-in-the-loop simulation using an AMD Ryzen(TM) AI mini PC. Results demonstrate that a fully onboard MAS architecture is a viable, cost-efficient alternative to cloud-dependent deployments, with strong potential for real-world transfer. The simulation environment has been released as open source under the Apache 2.0 licence.

### 16. Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses
- Deep score: 0.3
- Date: 2026-07-06T13:10:13+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.05029
- Summary: Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals. We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA's attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent's retrieved content but also the integrity of its reasoning history.

### 17. Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory
- Deep score: 0.3
- Date: 2026-07-06T00:00:00+00:00
- Source: huggingface
- Focus/tech: AI agents / AI agents
- URL: https://huggingface.co/papers/2607.05511
- Summary: Agentic video understanding equips models with long-term memory to autonomously process and respond to continuous, long-horizon multimodal streams. However, advanced video agents often rely on ``detective-style'' iterative reasoning for action control (e.g., search) and evidence aggregation, incurring prohibitive costs and latency. We argue that such heavy reasoning primarily compensates for the lack of global context and semantic misalignment in retrieval. This paper introduces Light-Omni, a multimodal agent framework for reflexive and lightweight video understanding. It achieves this through dual contextual states that instantly build the required context in a single forward pass. First, we maintain a global state, a finite-sized multimodal script continuously consolidated from episodic memory, serving as the global context for Light-Omni. Through hierarchical merging, it preserves recent details while summarizing past events. Second, conditioned on this global context, we generate a parametric latent state that directly drives autonomous actions and produces retrieval embeddings, with minimal latency. Benefiting from this coupled design, Light-Omni achieves semantically aligned retrieval and reflexive responses while avoiding iterative reasoning. Extensive experiments validate the effectiveness of Light-Omni across multiple video benchmarks. Notably, it outperforms M3-Agent with an average 2.4% accuracy gain, a 12.1times speedup, and a 2.6times improvement in GPU memory efficiency. Furthermore, it serves as a memory system to enhance both the performance and efficiency of existing MLLMs. Project page: https://clare-nie.github.io/Light-Omni.

### 18. A Common Neural Signal of Evidence Accumulation for Perceptual and Mnemonic Decisions
- Deep score: 0.3
- Date: 2026-07-06T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents, neural interfaces / neural interfaces
- URL: https://www.biorxiv.org/content/10.1101/2025.11.13.688140
- Summary: Humans frequently make decisions based on sensory input from the external environment or information retrieved from memory. The centro-parietal positivity (CPP), an event-related EEG potential, has recently been identified as a neural correlate of sensory evidence accumulation during perceptual decision-making tasks. However, it remains unclear whether this component also reflects the accumulation of evidence in service of decisions grounded in semantic and episodic long-term memory. Across two experiments, we investigated whether the CPP serves as a domain-general neural signal of evidence accumulation. In Experiment 1, participants completed 2AFC perceptual and semantic memory tasks with varying levels of evidence strength. Perceptual judgements involved luminance discrimination of alphanumeric strings with three luminance difference levels controlling perceptual evidence strength. Semantic memory judgements involved discriminating population differences between U.S. states with census data used to define three bins of memory evidence strength. A CPP component was observed in both tasks whose build-up rate (i.e., slope) scaled with evidence strength, response time, and confidence in both stimulus- and response-locked analyses. Extending these findings to episodic memory, participants in Experiment 2 completed a two-alternative forced-choice word recognition task with target words varying in exposure frequency during learning to control episodic memory strength. Again, we found that CPP slopes scaled with memory strength, response time, and confidence. Together, these findings support the CPP as a domain-general neural signature of evidence accumulation across perceptual, semantic, and episodic mnemonic decisions.

### 19. AGL-1: The Enterprise AI Governance Layer as a Control Plane for Trusted Enterprise Intelligence
- Deep score: 0.3
- Date: 2026-07-03T17:42:08+00:00
- Source: arxiv
- Focus/tech: AI agents, AI decision delegation / AI agents
- URL: https://arxiv.org/abs/2607.03516
- Summary: Enterprise artificial intelligence is moving from isolated experimentation toward operational dependency across copilots, retrieval-augmented generation systems, autonomous agents, and AI-enabled business workflows. As this transition accelerates, the primary enterprise challenge is no longer only model access or inference scale. It is governed intelligence operations: the ability to enforce authorization, preserve contextual lineage, control persistent memory, detect stale or conflicting knowledge, constrain agentic execution, and produce audit-ready evidence across distributed AI estates. This paper introduces AGL-1, the Enterprise AI Governance Layer, as a vendor-neutral reference model for the control plane that should operate across foundation models, retrieval systems, orchestration frameworks, enterprise memory, policy engines, observability systems, tools, APIs, and business applications. Building on governed knowledge-system principles introduced in GKS-5, AGL-1 generalizes the governance problem from retrieval-specific controls to full AI execution-path governance. It identifies recurring failure modes such as unauthorized retrieval, stale grounding, unmanaged memory, weak provenance, policy drift, fragmented observability, and uncontrolled autonomous execution. It then defines seven governance domains: identity-aware retrieval, policy enforcement, provenance management, memory governance, knowledge integrity monitoring, agentic execution control, and trust observability. The central claim is that durable enterprise value from AI will increasingly depend on the ability to govern intelligence at scale. In complex enterprises, trust is not a property of the model alone. It is a property of the system around the model: identity, knowledge, policy, memory, tools, human oversight, and evidence working together as a managed control plane.

### 20. MemSyco-Bench: Benchmarking Sycophancy in Agent Memory
- Deep score: 0.3
- Date: 2026-07-01T15:30:33+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2607.01071
- Summary: Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of factual accuracy or objective reasoning. Despite this emerging risk, existing memory benchmarks primarily evaluate whether memories are correctly stored, retrieved, or updated, while overlooking how retrieved memories influence downstream reasoning and decision-making. To bridge this gap, we propose MemSyco-Bench, a comprehensive benchmark for evaluating memory-induced sycophancy in agent systems. MemSyco-Bench measures when memory should influence a decision and how valid memory should be used. Specifically, it covers five tasks that assess whether agents can reject memory as factual evidence, respect its applicable scope, resolve conflicts between memory and objective evidence, track memory updates, and use valid memory for personalization. All related resources are collected for the community at https://github.com/XMUDeepLIT/MemSyco-Bench.

### 21. Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems
- Deep score: 0.3
- Date: 2026-06-30T08:41:00+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.31339
- Summary: Agentic artificial intelligence is increasingly used to decompose industrial tasks, propose robot actions, and adapt execution plans in dynamic cyber-physical environments. However, autonomous proposal generation alone does not guarantee that multi-robot industrial systems preserve task dependencies, resource ownership, safety holds, or repair boundaries during long-horizon execution. This paper introduces a verification-gated agentic mission-state governance framework for intelligent industrial multi-robot systems. The framework maintains two synchronized state objects: an evolving task forest for persistent hierarchy, delayed grounding, and repairable substructures; and a governed blackboard for online execution state, robot traces, resource locks, world beliefs, proposals, verification records, and scene-temporary constraints. From each forest--blackboard snapshot, a derived execution coupling topology exposes cross-branch dependencies for proposal verification, parallel-commit eligibility, and bounded repair. Candidate assignments, repairs, deferrals, and constraint updates may be generated by heuristic, optimization, or agentic reasoning modules, but they can update the committed mission state only after deterministic verification and atomic commit. We evaluate the framework in an indoor factory multi-robot scenario, 30-seed remote-construction stress benchmarks, structural ablations, and scalability probes. The results show improved verified and safety-audited mission-state progress with fewer invalid commitments, lock conflicts, duplicate assignments, abandoned nodes, and disruptive repairs under modeled mission predicates. The study positions agentic AI as a proposal-generating layer governed by inspectable mission-state verification rather than as an unchecked execution authority.

### 22. Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation Threats
- Deep score: 0.3
- Date: 2026-06-29T13:07:41+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.30259
- Summary: In contemporary societies, the threat of disinformation has reached alarming levels, exacerbated by the proliferation of electronic communication, social media, and advancements in artificial intelligence. As a result, there is an urgent need to develop effective countermeasures to mitigate this menace. However, the sheer scale of the problem renders manual fact-checking and human-based verification inadequate, underscoring the necessity for automated methods to detect and debunk disinformation. This article proposes a novel approach based on a multi-agent system that emulates the decision-making processes of human annotators engaged in disinformation detection tasks. By incorporating a consensus mechanism, diversity in cognition and diversity in knowledge, and also hierarchical structure, inspired by human annotators' behavior, the proposed method achieves superior results compared to individual Large Language Models (LLMs), including GPT 4 and GPT 3.5. The system leverages open models (e.g., LLaMA, Kimi, Qwen, Deepseek and LLaMA-Nemotron) to ensure greater transparency. The evaluation of the proposed method encompasses datasets in languages with varying resource availability, including English (high-resource), Polish (medium-resource), Slovak (low-resource) and Bulgarian (low-resource). Experiments were conducted on tasks such as direct disinformation detection, identification of texts worthy of verification, and detection of texts containing verifiable factual claims.

### 23. A Multi-Agent system for Multi-Objective constrained optimization
- Deep score: 0.3
- Date: 2026-06-18T13:47:28+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.20236
- Summary: Many decision-making problems in computing and networking systems can be naturally formulated as cost-minimization problems under performance constraints. In dynamic environments, reinforcement learning (RL) is often used to solve such problems at runtime by embedding both costs and constraint violations into a single scalar reward through weighted penalty terms, following a Lagrangian-inspired formulation. However, in this context the behavior of the learned policy critically depends on the choice of these weights, which are typically selected manually. This makes it difficult to identify an appropriate trade-off between optimizing the primary objective and effectively avoiding constraint violations, particularly in non-stationary environments where their relative importance may change. This paper presents MAMO (Multi-Agent system for Multi-Objective constrained optimization), an approach to tackle this balancing problem through multi-agent RL. MAMO decouples task execution from objective design by formulating the selection of reward weights as a learning problem, providing a !rst step towards more autonomous and robust RL-based solutions for constrained optimization problems in dynamic environments.

### 24. GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning
- Deep score: 0.3
- Date: 2026-06-16T03:45:24+00:00
- Source: arxiv
- Focus/tech: AI agents, robotics / AI agents
- URL: https://arxiv.org/abs/2606.17480
- Summary: Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Second, the original KnowledgeBank mainly retrieves semantically similar snippets and appends new knowledge, which makes it difficult to control memory quality, conflicts, confidence, and geometric relevance. To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance. To address the second challenge, we upgrade KnowledgeBank into a governed long-term memory system with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while reducing AS by 4.95% and 5.65%, respectively. Code: https://github.com/AIGeeksGroup/GeneralVLA-2. Website: https://aigeeksgroup.github.io/GeneralVLA-2.

### 25. Misinformation Propagation in Benign Multi-Agent Systems
- Deep score: 0.3
- Date: 2026-06-15T13:40:01+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.16710
- Summary: Multi-agent systems, in which multiple large language model agents solve problems through turn-based interaction, are increasingly deployed in high-stakes settings such as medical diagnosis, legal analysis, and forensic decision-making. Their reliability can be at risk when single agents reason from incorrect or misleading context, e.g., from tool calls, since errors may propagate through agent interactions. This work studies this risk by injecting intent-based misinformation into benign single-agent and multi-agent systems across reasoning, knowledge, and alignment tasks. We find that misinformation can degrade single-agent performance and persists across multi-agent debate, with agents often retaining answers introduced by misinformed peers. Nevertheless, multi-agent debate reduces the resulting performance degradation compared to single-agent prompting, especially when most agents are not exposed to misinformation. Robustness depends on group composition and decision protocol. Consensus can be more stable than voting under peer pressure, while majorities can often steer misinformed agents back toward correct answers. Our results show that misinformation robustness in multi-agent systems depends on the underlying model and also on how agents exchange information and aggregate decisions.

### 26. Decentralized Multi-Agent Systems with Shared Context
- Deep score: 0.3
- Date: 2026-06-09T10:13:07+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.10662
- Summary: Multi-agent systems (MAS) can scale large language model reasoning at test time by decomposing complex problems into parallel subtasks. However, most existing MAS rely on centralized orchestration, where a main agent assigns work, collects outputs, and merges results. As the number of subtasks grows, this controller becomes a communication and integration bottleneck. We propose Decentralized Language Models (DeLM), a MAS framework that decentralizes coordination through parallel agents, a shared verified context, and a task queue. Agents asynchronously claim subtasks, read accumulated progress, perform local reasoning, and write back compact verified updates. The shared context acts as a common communication substrate, enabling agents to build on one another's verified progress without routing every update through a central controller. Empirically, DeLM improves both software-engineering test-time scaling and long-context reasoning. On SWE-bench Verified, DeLM achieves the best performance across Avg.@1, Pass@2, and Pass@4, with gains of up to 10.5 percentage points over the strongest baseline, while reducing cost per task by roughly 50%. On LongBench-v2 Multi-Doc QA, DeLM achieves the highest average accuracy across four frontier model families, improving over the strongest baseline by up to 5.7 percentage points. The code is available on our project website at https://yuzhenmao.github.io/DeLM/.

### 27. Distilling LLM Reasoning into an Interpretable Policy Tree for Human-AI Collaboration
- Deep score: 0.3
- Date: 2026-06-07T12:20:32+00:00
- Source: arxiv
- Focus/tech: cognitive outsourcing, AI agents / cognitive outsourcing
- URL: https://arxiv.org/abs/2606.08596
- Summary: Constructing efficient and reliable policies to assist humans is indispensable for human-AI collaboration. Existing methods mainly follow two lines of work. Most prior work relies on multi-agent reinforcement learning (MARL) to learn black-box policies, which limits interpretability and raises safety concerns. Recent methods query large language models (LLMs) at each decision step, causing slow responses and high inference costs. We propose Collaboration Policy Tree (Co-pi-tree), a closed-loop method that learns an executable policy tree consisting of a partner-behavior prediction tree and an agent-action selection tree. Co-pi-tree constructs a policy by distilling LLM reasoning into policy tree code. It then evaluates the policy through partner interaction, obtains feedback, and uses natural language to summarize the interaction feedback to improve problematic branches. Experiments in Overcooked-AI show that Co-pi-tree improves average reward by 35.4% over the baseline average, while reducing the number of LLM queries by 77.7% and test-time latency by 97.1%. Project page: https://beiwenzhang.github.io/Co-pi-tree/

### 28. Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems
- Deep score: 0.3
- Date: 2026-06-04T05:10:20+00:00
- Source: arxiv
- Focus/tech: AI agents / AI agents
- URL: https://arxiv.org/abs/2606.05711
- Summary: Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. The dominant communication protocol in such systems is natural language: agents exchange messages token-by-token, verbalising their internal reasoning so that peers can read, verify, and respond. While convenient and interpretable, this protocol suffers from three structural drawbacks -- high inference cost, irreversible information loss during discretization, and ambiguity/redundancy of natural language. A growing body of work therefore explores an alternative protocol -- latent communication -- in which agents exchange continuous representations (embeddings, hidden states, or KV-caches) directly, bypassing the bottleneck of text generation. This paper presents a unified framework for organising the rapidly expanding literature on latent communication. We analyse existing methods along three orthogonal axes: (1) WHAT information is communicated (Embeddings, Hidden States, KV-Caches, or other continuous state); (2) WHICH sender-receiver alignment is used (latent-space alignment and layer alignment); and (3) HOW the communicated information is fused into the receiver (concatenation, prepending, mathematical operations, cross-attention, or cache restoration). Under this 3-axis framework, we systematically categorise eighteen representative methods proposed between 2024 and 2026, identify five major design patterns, and surface a set of open challenges -- including cross-architecture alignment, security of latent channels, compression for edge deployment, and the relationship between latent communication and latent chain-of-thought. We hope that this framework both lowers the barrier to entry for new researchers and provides a vocabulary for comparing future work.

### 29. A multi-agent workflow converts CAR-T patient evidence into experimentally testable hypotheses
- Deep score: 0.2
- Date: 2026-07-16T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.07.15.738646
- Summary: The rapid expansion of chimeric antigen receptor (CAR) T cell studies has produced a fragmented evidence landscape linking publications, repository accessions, patient metadata and mechanistic observations. Here we present BioPathfinder, a multi-agent discovery engine for CAR-T research evidence construction, hypothesis generation and validation planning. Unlike existing LLM-based and agentic approaches centered on predefined CAR-T development tasks, BioPathfinder constructs a provenance-tracked resource linking scRNA-seq datasets from treated patients to their publications and uses it to generate diverse, falsifiable and dataset-aware mechanistic hypotheses prioritized for computational and experimental validation by role-specialized LLM reviewer subagents. Applied to the curated CAR-T-treated patient paper-dataset corpus, BioPathfinder nominated candidate mechanisms of CAR-T persistence, dysfunction and therapeutic resistance, including the hypothesis that genes associated with an NK-like transition program could be targeted to reduce CAR-T exhaustion and promote persistence. Patient scRNA-seq analysis showed that this NK-like transition-associated program was enriched in exhausted post-infusion CAR-T cell states. Virtual perturbation further prioritized transition-associated KLR-family receptor genes, including KLRC1, KLRD1 and KLRG1. Expert review selected KLRC1, encoding NKG2A, for experimental testing. In vitro and in vivo chronic-stimulation models showed that NKG2A marked CD8 CAR-T cells with activated and exhaustion-associated phenotypes. NKG2A blockade improved antitumour function and persistence-associated readouts in vivo. These results show that structured clinical single-cell evidence can be transformed by domain-specialized multi-agent systems into experimentally actionable CAR-T engineering hypotheses.

### 30. Medea: An AI agent for therapeutic reasoning across biological contexts
- Deep score: 0.2
- Date: 2026-07-16T00:00:00+00:00
- Source: biorxiv
- Focus/tech: AI agents / AI agents
- URL: https://www.biorxiv.org/content/10.64898/2026.01.16.696667
- Summary: Therapeutic hypotheses can transfer across diseases but their relevance depends on biological context. The same target, perturbation, or treatment can produce different effects across cell types, disease states, genetic backgrounds, and patients. Therapeutic reasoning therefore requires methods that preserve context, test when evidence supports transfer, and identify where context-specific effects limit it. Although AI agents can perform therapeutic analyses, existing systems often fail to preserve biological context over long workflows, verify intermediate computational steps, or reconcile conflicting evidence across datasets and literature. Here, we present Medea, an AI agent for therapeutic reasoning across biological contexts. Medea executes multi-step analyses using biological tools, machine learning models, and literature retrieval while enforcing verification during planning, execution, and evidence synthesis. We evaluate Medea across 5,673 open-ended analyses in three domains: cell type specific therapeutic target nomination in five diseases and 29 cell types, synthetic lethality prediction in 7 cancer cell lines, and immunotherapy response prediction from multimodal patient profiles. Using a previously unpublished epistatic miniarray profiling screen performed under two DNA-damaging treatments, we evaluate Medea on predicting synthetic lethality among 238,046 gene-gene pairs in yeast. Medea accurately predicts these experimentally measured synthetic lethal interactions, indicating that its performance reflects biological relevance rather than information leakage from benchmark datasets. Across these evaluations, Medea improves performance over large language models, reasoning models, biomedical agents, and specialized machine learning models while maintaining low failure rates and calibrated abstention. These results show that verifiable AI agents can perform therapeutic analyses across biological contexts.
