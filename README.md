# Product Research & Planning Agentic Framework

A gated, adversarial, evidence-first research pipeline. One orchestrator, twelve worker roles, six manually-approved gates, three deliverables.

**Product-agnostic.** Nothing here is specific to any codebase or company.

---

## Start a run

Open `ORCHESTRATOR-KICKOFF.md`, copy the prompt block, fill in your product, send it in a fresh session.

---

## What it produces

1. **Product Market Feasibility Assessment** — 2–3 distinct scenarios, each a complete business (USP, positioning, brand philosophy, features, revenue model, GTM), scored by Customer Pain Index, with competitor analysis, barriers to entry both directions, PMF scoring and risk assessment.
2. **Technical Feasibility Assessment** — four independent specs per feature cluster (adopt OSS / build / buy / compose), scored on a declared weighted matrix, with the optimal selection, a named fallback per cluster, and a 24-month TCO.
3. **Roadmap & Implementation Plan** — CPI-ordered phases, capacity-checked, with a dependency graph, pre-scheduled decision points, leading indicators and P50/P80/downside timelines.

Plus: the Product Scope Document, the Investment Analysis, the full evidence ledger, and six Gate Packets recording every decision you made and why.

---

## The pipeline

```
G0 Scoping ──▶ G1 Discovery ──▶ G2 Market ──▶ G3 Reconcile ──▶ G4 Technical ──▶ G5 Roadmap
   │              │                │              │                │               │
scoping     3× academic      market-        reconciliation    4× tech-path      roadmap
  agent     2× oss           feasibility     (market vs        per cluster        agent
(you talk)  3× market        investment       technical)       tech-optimizer
                             analyst
   │              │                │              │                │               │
   └──────────────┴────────────────┴──────────────┴────────────────┴───────────────┘
              judge-pessimist ‖ steelman · ≤10 rounds · every gate
                        every gate stops for your approval
```

---

## The four protocols

| | | |
|---|---|---|
| **P1** | `protocols/EVIDENCE-LEDGER.md` | Every claim gets an ID, a source, a tier (T1–T4) and a computed confidence. Nothing enters a deliverable without one. Gate floor: 70% coverage on material claims. |
| **P2** | `protocols/CPI.md` | `CPI = Frequency × Severity × (6 − Workaround Quality) × WTP Signal`, normalised 0–100. The single prioritisation instrument — it orders value props, features and the roadmap. |
| **P3** | `protocols/JUDGE-QUADRANT.md` | Evidence strength × claim materiality. Weak-and-trivial is deleted, weak-and-material is retried by a fresh worker with different queries. Max 10 rounds, then declared convergence failure. |
| **P4** | `protocols/GATE-PACKET.md` | One page per gate. Every open question carries quantitative and qualitative assessment, a named risk, and a default. Max five per gate. |

---

## The agents

| | Agent | Skill |
|---|---|---|
| A0 | Orchestrator | `skills/orchestrator/` |
| A1 | Scoping Agent (interactive) | `skills/scoping-agent/` |
| A3 | Academic Scout ×3 | `skills/academic-scout/` |
| A4 | OSS Scout ×2 | `skills/oss-scout/` |
| A5 | Market Scout ×3 | `skills/market-scout/` |
| A6 | Market Feasibility | `skills/market-feasibility/` |
| A7 | Investment Analyst | `skills/investment-analyst/` |
| A8 | Judge — Pessimist | `skills/judge-pessimist/` |
| A9 | Steelman | `skills/steelman/` |
| A10 | Reconciliation | `skills/reconciliation/` |
| A11 | Tech Path Agent ×4 per cluster | `skills/tech-path-agent/` |
| A12 | Tech Optimizer | `skills/tech-optimizer/` |
| A13 | Roadmap & Implementation | `skills/roadmap-agent/` |

---

## Design decisions worth knowing

- **Kill Criteria are set at G0 and never edited.** Written before any research, so the run cannot quietly redefine success to match what it found.
- **The pessimist has a counterweight.** A lone pessimist systematically destroys good asymmetric bets, so the steelman runs in parallel every round and audits the pessimist's own unevidenced skepticism. Material disagreements go to you, not to the machine.
- **Reconciliation owns the gap nobody owns.** Market agents assume the thing is buildable; technical agents assume it's wanted. G3 exists to catch the contradiction — price against COGS, first and always.
- **CAC carries a mandatory 50% buffer.** Early CAC estimates are systematically optimistic; the buffer is the correction, and only the buffered figure flows downstream.
- **A fourth technical path: compose.** Stitching 2–3 OSS projects beats pure adopt/build/buy more often than any of them, so it gets its own agent and its own honest accounting of the integration seams.
- **Citations-per-month, not raw citations.** Raw counts structurally exclude everything from the last 18 months — usually the part that matters.
- **OSS scored on bus factor, not stars.** Star count is the single most misleading signal in open source.
- **Retries go to strangers.** Authors defend their work; a fresh worker re-examines it. Different queries, different source class, max two attempts, then it becomes a declared gap.

---

## Files

```
product-research-framework/
├── README.md
├── EXECUTION-PLAN.md          ← the runbook, runs identically every time
├── ORCHESTRATOR-KICKOFF.md    ← copy this to start
├── protocols/                 ← P1–P4, binding on all agents
├── skills/                    ← 13 agent skill definitions (orchestrator + 12 workers)
├── templates/                 ← 5 deliverable templates
└── run/<run-id>/              ← created per run: ledgers, gates, deliverables
```
