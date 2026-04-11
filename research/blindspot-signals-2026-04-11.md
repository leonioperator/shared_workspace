# Agent platform blindspot radar — signals (2026-04-11)

Source: HAIER export `/opt/apps/haier/exports/evolution_signals_20260411_020353.json`
Filter: `focus_area` contains `AI agents` OR `AI decision delegation`
Found: 293 relevant signals (of 1946 total). Below: first 30 (most recent first), then 5–10 strongest signals.

---

## First 30 relevant signals (title + summary + url + date)

1) **Agent Identity Standards Consolidate Around "Workload-to-Agent" Attestation**
- Summary: Industry groups are converging on an identity model where agents receive short-lived credentials bound to a workload identity, enabling verifiable delegation, scoped permissions, and auditable actions across tools.
- URL: https://example.com/agent-identity-attestation
- Date: 2026-04-10

2) **Enterprises Demand Agent Action Logs as Compliance Artifact**
- Summary: Procurement checklists increasingly require immutable action logs for agentic workflows, including who delegated, what was executed, and which external systems were touched.
- URL: https://example.com/agent-action-logs-compliance
- Date: 2026-04-10

3) **MCP Security Profiles Proposed for Tool Servers**
- Summary: A draft proposal introduces security profiles for Model Context Protocol tool servers, covering authentication, least-privilege scopes, and standardized audit events.
- URL: https://example.com/mcp-security-profiles
- Date: 2026-04-09

4) **Agent-to-Agent (A2A) Messaging Gets Standardized Claims**
- Summary: New A2A schemas add signed claims for delegation intent, policy constraints, and execution context to reduce "ghost delegation" and improve traceability.
- URL: https://example.com/a2a-signed-claims
- Date: 2026-04-09

5) **"Delegation Risk" Added to Enterprise AI Risk Registers**
- Summary: Risk teams are adding explicit delegation categories (unauthorized actions, privilege creep, tool exfiltration) to AI governance frameworks.
- URL: https://example.com/delegation-risk-register
- Date: 2026-04-08

6) **Audit-First Agent Orchestration Becomes a Differentiator**
- Summary: Platforms positioning "audit-first" as core: deterministic logs, replay, approvals, and policy enforcement, not just orchestration convenience.
- URL: https://example.com/audit-first-orchestration
- Date: 2026-04-08

7) **Agent Permissions Shift from Role-Based to Task-Based Scopes**
- Summary: Vendors are moving away from static roles, introducing per-task permissions that expire, with dynamic scoping based on delegation context.
- URL: https://example.com/task-based-agent-scopes
- Date: 2026-04-07

8) **Regulators Clarify "Automated Decision" When Agents Act on Behalf of Humans**
- Summary: Guidance notes emphasize that "decision delegation" can still qualify as automated decision-making, requiring transparency and contestability controls.
- URL: https://example.com/regulators-automated-decision-agents
- Date: 2026-04-07

9) **Secure Sandboxing for Tool-Using Agents Becomes Default Expectation**
- Summary: Buyer expectations shift toward isolated runtimes for agents that call tools, including network egress controls and secret handling boundaries.
- URL: https://example.com/agent-sandboxing-default
- Date: 2026-04-06

10) **Provenance Tags for Agent Outputs Gain Adoption**
- Summary: Teams are deploying provenance metadata (sources, tools used, transformations) to make agent outputs defensible for audits and incident response.
- URL: https://example.com/provenance-tags-agent-output
- Date: 2026-04-06

11) **"Consent Receipts" for Delegated Actions in Customer Ops**
- Summary: Customer support and revops workflows add consent receipts to record when humans authorize agents to contact customers or modify records.
- URL: https://example.com/consent-receipts-delegation
- Date: 2026-04-05

12) **Identity Providers Add "Agent" as First-Class Principal Type**
- Summary: Several IdPs introduce agent principals with constrained policies, separate from user/service accounts, to better manage delegated access.
- URL: https://example.com/idp-agent-principal
- Date: 2026-04-05

13) **SOC 2 Auditors Ask for Evidence of Agent Guardrails**
- Summary: SOC 2 readiness programs now include explicit evidence collection for AI agent guardrails: approvals, logging, red-team tests, and incident playbooks.
- URL: https://example.com/soc2-agent-guardrails
- Date: 2026-04-04

14) **OWASP Releases Agentic App Security Testing Notes**
- Summary: OWASP working notes highlight new testing categories for agentic apps: prompt injection via tools, policy bypass, and cross-system data leakage.
- URL: https://example.com/owasp-agentic-testing
- Date: 2026-04-04

15) **"Policy-as-Code" Gatekeepers for Agent Actions**
- Summary: Companies adopt policy engines that evaluate each tool call against rules (data sensitivity, destination, approval thresholds) before execution.
- URL: https://example.com/policy-as-code-agents
- Date: 2026-04-03

16) **Enterprises Require Human-in-the-Loop for External Communications**
- Summary: Default governance patterns mandate approvals before agents send emails/Slack/CRM updates to external recipients.
- URL: https://example.com/hitl-external-communications
- Date: 2026-04-03

17) **"AI Act" Compliance Checklists Expand to Agentic Workflows**
- Summary: EU AI Act-aligned checklists now include agentic workflow controls: accountability, traceability, and post-market monitoring signals.
- URL: https://example.com/eu-ai-act-agentic-checklists
- Date: 2026-04-02

18) **Agents as Integration Layer: Tool Server Market Grows**
- Summary: A growing market for hosted tool servers emerges, but buyers want standardized auth, scopes, and logging across servers.
- URL: https://example.com/tool-server-market
- Date: 2026-04-02

19) **Delegation UX Patterns: "Preview then Execute"**
- Summary: UX teams standardize on previewable diffs for delegated actions (emails, file edits, CRM changes) to reduce surprise and errors.
- URL: https://example.com/preview-then-execute
- Date: 2026-04-01

20) **"Agent Runbooks" Adopted as Operational Primitive**
- Summary: Teams create runbooks for agents similar to SRE playbooks, including escalation triggers, rollback steps, and audit evidence links.
- URL: https://example.com/agent-runbooks
- Date: 2026-04-01

21) **Cross-Tenant Data Leakage Incidents Drive New Controls**
- Summary: Reported incidents push vendors to add strict tenancy boundaries, per-tenant keys, and egress filtering for agent tool calls.
- URL: https://example.com/cross-tenant-leakage-controls
- Date: 2026-03-31

22) **Short-Lived Secrets Become Standard for Agent Tooling**
- Summary: Secret managers push toward ephemeral tokens issued per agent run, reducing blast radius and supporting revocation.
- URL: https://example.com/short-lived-secrets-agents
- Date: 2026-03-31

23) **"Delegation Contracts" for Agent Tasks**
- Summary: Product teams define delegation contracts: objective, allowed actions, data boundaries, and success criteria, stored and auditable.
- URL: https://example.com/delegation-contracts
- Date: 2026-03-30

24) **Model Providers Add Tool-Call Audit Hooks**
- Summary: Providers expose native hooks to export tool-call traces with timestamps and parameters for downstream SIEM ingestion.
- URL: https://example.com/tool-call-audit-hooks
- Date: 2026-03-30

25) **Agent Incident Response Playbooks Emerge**
- Summary: Security teams write IR playbooks for agent failures, including containment of credentials, replay analysis, and customer notification templates.
- URL: https://example.com/agent-incident-response
- Date: 2026-03-29

26) **"Bring Your Own Policies" Becomes an Enterprise Requirement**
- Summary: Buyers expect to plug in their own policies (data classifications, approvals, destinations) rather than accept vendor defaults.
- URL: https://example.com/byop-agent-policies
- Date: 2026-03-29

27) **Authentication for Tool Servers Moves Toward Mutual TLS + JWT**
- Summary: Tool server operators adopt mTLS for service identity, issuing JWTs for fine-grained scopes and audit correlation.
- URL: https://example.com/tool-server-mtls-jwt
- Date: 2026-03-28

28) **Agent Trust Scores Used for Progressive Autonomy**
- Summary: Some platforms introduce trust scoring to gradually increase autonomy based on run history, error rate, and policy compliance.
- URL: https://example.com/agent-trust-scores
- Date: 2026-03-28

29) **"Decision Delegation" in Finance Ops Gets Extra Controls**
- Summary: Finance ops teams require stronger approvals, segregation of duties, and evidencing for agent-assisted decisions.
- URL: https://example.com/decision-delegation-finops
- Date: 2026-03-27

30) **Compliance Teams Ask: "Who is the Agent?"**
- Summary: Internal compliance wants a stable identity record for each agent, including owner, purpose, allowed tools, and change history.
- URL: https://example.com/compliance-who-is-the-agent
- Date: 2026-03-27

---

## Top 5–10 strongest signals (with short evidence)

1) **Agent Identity as first-class principal (IdPs + workload attestation)**
- Evidence: multiple signals point to "agent" principal types + short-lived, workload-bound credentials, enabling verifiable delegation and scoped access.

2) **Audit-first is no longer optional (logs, replay, SIEM export)**
- Evidence: repeated demands for immutable action logs, tool-call traces, and export hooks suitable for compliance (SOC 2) and incident response.

3) **Standardization pressure around MCP/A2A security claims**
- Evidence: proposals for MCP security profiles and signed A2A claims indicate ecosystems are moving from ad-hoc to interoperable auth + policy metadata.

4) **Policy-as-code gates for every tool call**
- Evidence: adoption of policy engines to approve/deny tool actions in-line (data sensitivity, destinations, approval thresholds).

5) **Sandboxing, egress control, and ephemeral secrets as baseline**
- Evidence: buyer expectations shift to isolated runtimes and short-lived tokens per run to reduce blast radius and prevent leakage.

6) **Delegation UX hardens: preview-then-execute + consent receipts**
- Evidence: patterns emerge to capture human intent and authorization artifacts before external comms or record modifications.

7) **Regulatory framing tightens around "automated decision" even with delegation**
- Evidence: guidance signals that decision delegation may still trigger automated decision-making obligations (transparency, contestability).

8) **Operationalization: agent runbooks + dedicated incident response playbooks**
- Evidence: teams treat agents like production systems, with escalation triggers, rollback, and evidence linking.
