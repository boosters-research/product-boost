# EXECUTION PLAN — Product Research & Assessment Framework 2.0

**A gated, adversarial, evidence-first product research engine.**
One orchestrator, 20 specialized worker roles, 6 human-approved gates, 7 comprehensive deliverables.

---

## The 6 Invariants

| # | Rule |
|---|---|
| **I1** | **Gate order is absolute.** G0 → G1 → G2 → G3 → G4 → G5. Technical feasibility never begins before the user approves G2. |
| **I2** | **Every gate stops for the user.** No self-approval, ever. |
| **I3** | **No claim in a deliverable without an Evidence Ledger ID.** |
| **I4** | **Max 10 Judge rounds per phase.** Then forced convergence with a `## Convergence Failure` section. |
| **I5** | **Parallel within a wave, serial across gates.** All workers in a wave dispatch in one message. |
| **I6** | **Pessimist/steelman conflicts on material units go to the user.** The machine never picks a side silently. |

---

## The Pipeline & Waves

```
G0 Scoping ──▶ G1 Discovery ──▶ G2 Market & Money ──▶ G3 Reconcile ──▶ G4 Tech & AI ──▶ G5 Roadmap & GTM
   │                 │                    │                  │               │                 │
scoping-agent   3× academic          market-feasibility   reconciliation   4× tech-path       roadmap-agent
(interactive)   2× oss               investment-analyst   (C1–C6 audit)    per cluster        pricing-strategist
                3× market-scout      pricing-strategist                    tech-optimizer     gtm-growth
                2× voice-of-cust     moat-auditor                          ai-architect       compliance-risk
                1× persona-sim                                             compliance-risk
   │                 │                    │                  │               │                 │
   └─────────────────┴────────────────────┴──────────────────┴───────────────┴─────────────────┘
                judge-pessimist ‖ steelman · ≤10 rounds · every gate stops for user
```

---

## Detailed Gate Breakdown

### Gate G0 · Scoping & Kill Criteria
- **Agent:** `scoping-agent` (interactive).
- **Produces:** `deliverables/00-PRODUCT-SCOPE.md`, `KILL-CRITERIA.md` (3–6 numeric, falsifiable mortality tripwires), and the tagged Research Question List.
- **Gate Stop:** Gate Packet G0.

### Gate G1 · Multi-Domain Discovery
- **Wave W1 Dispatch:**
  - 3× `academic-scout` (Prefix `E-ACA-`)
  - 2× `oss-scout` (Prefix `E-OSS-`)
  - 3× `market-scout` (Prefix `E-MKT-`)
  - 2× `voice-of-customer` (Prefix `E-VOC-`)
  - 1× `persona-simulator` (Prefix `E-SIM-`)
- **Judge Loop:** Pessimist + Steelman in parallel. Eliminate Q3, retry Q2.
- **Gate Stop:** Gate Packet G1.

### Gate G2 · Market Feasibility, Moat & Unit Economics
- **Wave W2 Dispatch:**
  - `market-feasibility` (2–3 distinct scenarios, TAM/SAM/SOM, positioning)
  - `voice-of-customer` & `moat-auditor` (7-Powers defensibility, copy risk)
  - `investment-analyst` & `pricing-strategist` (Unit economics, 1.5x CAC buffer, DCF sensitivity, pricing tiers)
- **Judge Loop:** Adversarial scoring.
- **Gate Stop:** Gate Packet G2. **User selects the winning scenario.**

### Gate G3 · Cross-Domain Reconciliation
- **Wave W4 Dispatch:**
  - `reconciliation` checks C1–C6 contradictions (Price↔COGS, Promise↔Maturity, NFR↔Architecture, Timeline↔Scope, CAC↔Motion, License↔Revenue).
- **Gate Stop:** Gate Packet G3. Zero unadjudicated 🔴 contradictions.

### Gate G4 · Technical Architecture & AI Compute Feasibility
- **Wave W5 Dispatch:**
  - 4× `tech-path-agent` per feature cluster (OSS / Build / Buy / Compose).
  - `ai-systems-architect` (Token economics, LLM inference latency/cost, context window, RAG vs Fine-tune).
  - `compliance-risk` (GDPR, EU AI Act, SOC2, license audit).
  - `tech-optimizer` (Weighted scoring matrix, hybrid synthesis, 24-month TCO).
- **Gate Stop:** Gate Packet G4. Named fallback per cluster.

### Gate G5 · GTM Strategy, Compliance & Roadmap
- **Wave W6 Dispatch:**
  - `pricing-strategist` & `gtm-growth-strategist` (`templates/06-GTM-PRICING-SPEC.md`).
  - `compliance-risk` (`templates/07-COMPLIANCE-AUDIT.md`).
  - `roadmap-agent` (`deliverables/04-ROADMAP.md` CPI-ordered, 0.7x capacity check, P50/P80 estimates).
  - `assessment-engine` (`deliverables/ASSESSMENT-REPORT.md` scoring the full package against PAVR-10).
- **Gate Stop:** Gate Packet G5. Final user sign-off.
