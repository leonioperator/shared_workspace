# Moltbook Signals Log Template

Use one block per relevant discussion.

```yaml
- date: YYYY-MM-DD
  post_url: https://...
  section: /m/general
  author: ...
  title_or_topic: ...
  tools_used:
    - ...
  frameworks:
    - ...
  architecture_patterns:
    - ...
  coordination_method: ...
  memory_approach: ...
  deployment_context: ...
  main_problem: ...
  notable_quote: ...
  confidence: low|medium|high
  notes: ...
```

## Field Guidance

### `tools_used`
Concrete tools, MCP servers, APIs, CLIs, databases, orchestrators, observability tools, deployment tools.

### `frameworks`
Named agent frameworks, SDKs, orchestration runtimes, memory systems, or workflow engines.

### `architecture_patterns`
Examples:
- single-agent tool-calling
- manager-worker multi-agent
- event-driven workflow
- planner-executor split
- memory-augmented agent
- human-in-the-loop gate
- retrieval-heavy design

### `coordination_method`
How agents or components coordinate.
Examples:
- none / single-agent
- supervisor agent
- shared queue
- file handoff
- event bus
- cron-driven
- manual approval gates

### `memory_approach`
Examples:
- none
- vector store
- SQLite
- file-based notes
- graph memory
- hybrid memory

### `deployment_context`
Examples:
- local workstation
- VPS
- Docker
- cloud runtime
- enterprise SaaS integration
- internal ops tool

### `main_problem`
The main engineering challenge or operational pain point described.

### `confidence`
- `low`: inferred or weakly supported
- `medium`: partly explicit and useful
- `high`: explicit and credible
