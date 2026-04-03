Subject: Blindspot radar update (2026-04-03) — H24 Shadow AI governance + 2 new wedges

Tomi,

Ma a 2026-04-03 signal run alapján 3 új hypothesis került a listába (meglévők módosítása nélkül), és frissítettem a Top 3 opportunity + kísérlet részt.

Fájl frissítve:
- /home/leoni/shared_workspace/research/blindspot-radar-hypotheses.md
Forrás signal:
- /home/leoni/shared_workspace/research/blindspot-signals-2026-04-03.md

Delta (új hypothesis-ek)

1) H24 — Shadow AI / Unmanaged Agent Governance Plane [21/25]
- Lényeg: a „shadow AI” nem egyszerűen tool sprawl, hanem autonóm agent sprawl. Inventory + ownership + policy + kill switch + audit egy dedikált governance plane-ben.
- Miért fontos: KiloClaw explicit a shadow AI-t célozza (AI News, 2026-04-02). Ez kategória-nevesítés, ami ritka és erős signal.
- Kiegészítő signal: AWS agenteket pozicionál DevOps/SecOps munkára (Forbes, 2026-04-01). Ez azt jelzi, hogy a working agents enterprise-be mennek, ahol a shadow deployment természetes.

2) H25 — Developer Multi-Agent Workspace Orchestration [16/25]
- Lényeg: a dev pain nem a model, hanem a túl sok agent/worktree/session. Kell egy workspace control plane (státusz, log, diff review, lifecycle, limits, policy).
- Signal: Claude Code (Anthropic, 2026-04-02) + Baton (Show HN, 2026-04-01) együtt.

3) H26 — Vertical Agent Copilots in Legacy Plugin Ecosystems (WordPress wedge) [14/25]
- Lényeg: WordPress jellegű ökoszisztémákban az agent réteg gyors terjesztési wedge, de a hard part a secure action wrapper + audit + rollback.
- Signal: WP Copilot (Product Hunt, 2026-04-02).

Top 3 opportunity + javasolt kísérlet (2026-04-03)

#1: H22 (Adversarial Robustness) + H24 (Shadow AI governance) kombó
- Miért most: a DeepMind 6 trap taxonómia (H22) megadja a támadási specet, H24 pedig a buyer-nek (IT/Sec) azonnali, inventory jellegű problémát ad.
- Kísérlet: "Shadow Agent Exposure Scan" 10 EU enterprise-nek (2 hét). Deliverable:
  (1) agent inventory,
  (2) top 10 policy gap,
  (3) 6 DeepMind pattern exposure score,
  (4) quick fixes.
  Mérők: audit->pilot konverzió, budget range, top control request.

#2: H2 / H6 — Audit Trail + Policy Enforcement Runtime
- Miért most: EU AI Act Aug 2026 window zárul; vendor signal (AWS) jelzi az adoption gyorsulását.
- Kísérlet: 30 napos "Agent Governance Baseline" pilot 3 design partnernél: audit trail + policy violations report + remediation.

#3: H20 — Agent Platform as Regulated Infrastructure (packaging/positioning)
- Miért most: compliance-ready platform narratíva hamar standard lesz; a különbség a csomagolás és a kommunikáció.
- Kísérlet: 1 oldalas EU AI Act mapping checklist + 10 célzott outreach.

Ha akarod, a #1 kísérletet össze tudom rakni úgy, hogy a kimenet már egy termék-spec váz legyen (feature list + első pricing hipotézis + buyer persona).

Leoni