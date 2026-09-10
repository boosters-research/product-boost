# EXECUTION PLAN — Product Research & Planning Agentic Framework

**This plan runs identically on every product, every time.** The Orchestrator follows it start to finish. Deviations are logged in `ledger/JUDGE-LOG.md` with a reason.

---

## Invariants

| # | Rule |
|---|---|
| I1 | **Gate order is absolute.** G0 → G1 → G2 → G3 → G4 → G5. Technical feasibility never begins before the user approves G2. |
| I2 | **Every gate stops for the user.** No self-approval, ever. |
| I3 | **No claim in a deliverable without an Evidence Ledger ID.** |
| I4 | **Max 10 Judge rounds per phase.** Then forced convergence with a `## Convergence Failure` section. |
| I5 | **Parallel within a wave, serial across gates.** All workers in a wave dispatch in one message. |
| I6 | **Pessimist/steelman conflicts on material units go to the user.** The machine never picks a side silently. |
| I7 | **Max 5 open questions per gate.** More means the phase is unfinished. |
| I8 | **Every open question carries quant + qual + risk + a stated default.** |
| I9 | **Web search only.** No connector dependency. Append `pdf` when hunting research. Never stop on a failed search. |
| I10 | **Retries go to fresh workers with different queries and a different source class.** |

---

## Phase 0 · Setup

**Trigger:** user supplies a product idea.

1. Create `run/<YYYY-MM-DD>-<product-slug>/` with the full tree (Orchestrator skill §Run setup).
2. Write the user's idea verbatim to `BRIEF.md`.
3. Initialise empty ledgers.
4. Dispatch **scoping-agent** (interactive).

---

## Gate G0 · Scoping

**Agent:** scoping-agent (interactive, single agent — no parallelism, this is a conversation).

**Produces:**
- `deliverables/00-PRODUCT-SCOPE.md` — 7-pillar document
- `KILL-CRITERIA.md` — 3–6 falsifiable conditions, **never edited after this gate**
- Research Question List — tagged academic / oss / market, the dispatch input for W1

**Gate condition:** every metric has a baseline, target and window (or an explicit `UNKNOWN — establish in Phase 0`); every NFR is quantified; every Kill Criterion has a number and a testing phase; the Scoping Matrix has a populated *Explicitly Out of Scope* column.

**→ Gate Packet G0. STOP for user approval.**

---

## Gate G1 · Discovery

**Wave W1 — dispatch all 8 workers concurrently in one message:**

| Instance | Agent | Assignment |
|---|---|---|
| ×3 | academic-scout | Split by research question domain. Prefix `E-ACA-`. |
| ×2 | oss-scout | Split by capability cluster. Prefix `E-OSS-`. |
| ×3 | market-scout | Sweeps 1–2 / 3–4 / 5–6 (P2 §Six sweeps). Prefix `E-MKT-`. |

Each dispatch brief carries: skill path, four protocol paths, its specific research questions, its ID prefix, ledger paths, and the sibling coverage map so workers do not duplicate.

**Then:** Judge loop (W3) over the raw findings — pessimist + steelman in parallel, eliminate Q3, retry Q2, up to 10 rounds or early exit.

**Gate condition:** ledger coverage ≥0.70 on material claims; all contradictions either adjudicated by a tiebreak scout or carried as explicit ranges; CPI input candidates exist for every proposed value prop.

**→ Gate Packet G1. STOP.**

---

## Gate G2 · Market Feasibility

**Wave W2 — sequential, because the analyst consumes the feasibility output:**

1. **market-feasibility** → `deliverables/01-MARKET-FEASIBILITY.md`
   2–3 distinct scenarios (distinctness test: differ on ≥3 of persona / VP / positioning / revenue model / GTM / price magnitude), CPI ledger, PMF scoring, barriers both directions, risk assessment, 13 sections with breakers.
2. **investment-analyst** → `deliverables/02-INVESTMENT-ANALYSIS.md`
   KPIs derived for this product; unit economics with **mandatory ×1.5 CAC buffer**; customers-to-breakeven across slow/base/fast; DCF inside each revenue model with sensitivity and reverse-DCF; valuation via **Multiples and Scorecard**, both presented; KPI→valuation sensitivity table; investment memo verdict.

**Then:** Judge loop (W3), up to 10 rounds.

**Gate condition:** ≥2 genuinely distinct scenarios pass the distinctness test; every CPI row cites evidence on all four axes; every financial input is T1/T2 or labelled `ASSUMPTION` with a range; Kill Criteria K-refs testable at G2 have a reading.

**→ Gate Packet G2. STOP. The user selects the scenario — this is never automatic.**

---

## Gate G3 · Reconciliation

**Wave W4 — single agent, but it reads everything:**

**reconciliation** → `ledger/CONTRADICTIONS.md`
Cross-joins market commitments against technical constraints across the six classes (C1 price↔COGS, C2 promise↔maturity, C3 NFR↔architecture, C4 timeline↔build, C5 CAC↔motion, C6 licence↔revenue model). Every contradiction scored 🔴/🟡/🟢 with ≥2 resolution options.

**Gate condition:** zero unresolved 🔴 contradictions — each is either resolved or accepted by the user in writing.

**→ Gate Packet G3. STOP.**

> This gate is the framework's insurance policy. It is the cheapest place to discover that the plan is impossible.

---

## Gate G4 · Technical Feasibility

**Opens only after G2 is user-approved.** Enforced by the Orchestrator.

**Wave W5:**

1. Cluster the approved scenario's features into 2–5 **feature clusters**.
2. Per cluster, dispatch **4 tech-path-agents concurrently** — P-OSS, P-BUILD, P-BUY, P-COMPOSE. They do not consult each other before submitting. Each produces a full `templates/TECH-SPEC.md`.
3. **tech-optimizer** scores all specs on the weighted matrix (weights declared *before* scoring), selects per cluster, may build a hybrid, absorbs the best ideas from rejected paths, applies unincorporated academic improvements, and strips what the approved scenario does not need.
4. **reconciliation post-pass** — re-run C1, C3, C6 against the *selected* paths, not the candidates.

**Then:** Judge loop (W3), up to 10 rounds.

**Gate condition:** every Phase-1 FR has a selected path with a named fallback and switch trigger; every NFR figure has a benchmark/SLA/measured comparable; gross margin at the approved price point is stated at three volume tiers, and if it breaks the DCF assumption it is escalated rather than quietly re-forecast.

**→ Gate Packet G4. STOP.**

---

## Gate G5 · Roadmap & Implementation

**Wave W6:**

**roadmap-agent** → `deliverables/04-ROADMAP.md`
CPI-ordered backlog with deviations justified; Phase 0 spikes before their dependent phases; capacity checked against available × 0.7; dependency graph with critical path and choke points; pre-scheduled decision points; metrics with leading indicators; Kill Criteria re-check; P50/P80/downside timelines; cut list.

**Gate condition:** nothing below CPI 35 in Phase 1; nothing with confidence <0.6 as a Phase-1 commitment; Phase-1 eng-weeks ≤ capacity × 0.7; every Kill Criterion has a current status.

**→ Gate Packet G5. STOP. Run closes on approval.**

---

## Wave summary

| Wave | Gate | Agents | Mode |
|---|---|---|---|
| — | G0 | scoping-agent | Interactive |
| W1 | G1 | 3× academic, 2× oss, 3× market | Parallel |
| W2 | G2 | market-feasibility → investment-analyst | Sequential |
| W3 | every gate | judge-pessimist ‖ steelman + n× retry workers | Parallel, ≤10 rounds |
| W4 | G3 | reconciliation | Single |
| W5 | G4 | 4× tech-path per cluster → tech-optimizer → reconciliation post-pass | Parallel then sequential |
| W6 | G5 | roadmap-agent | Single |

---

## Judge loop (runs at every gate)

```
round = 1
while round <= 10:
    dispatch judge-pessimist ‖ steelman
    classify every written unit → Q1 / Q2 / Q3 / Q4
    delete Q3 · demote Q4 to appendix
    dispatch fresh retry workers for Q2   (max 2 retries per unit)
    recompute coverage
    if no Q2 remaining and coverage >= 0.70 and no unadjudicated material conflicts: break
    if coverage_delta < 0.03: declare STALL, escalate early
    round += 1
if round > 10: write "## Convergence Failure" into the deliverable
```

Units failing 2 retries become `UNRESOLVED-GAP`: struck from the body, listed in Known Gaps, escalated to the user as an open question, and any conclusion depending on them downgraded to a stated hypothesis.

---

## Final deliverables

1. `deliverables/01-MARKET-FEASIBILITY.md` — **Product Market Feasibility Assessment**
2. `deliverables/03-TECHNICAL-FEASIBILITY.md` — **Technical Feasibility Assessment**
3. `deliverables/04-ROADMAP.md` — **Roadmap and Implementation Plan**

Supporting: `00-PRODUCT-SCOPE.md`, `02-INVESTMENT-ANALYSIS.md`, the full ledger set, and six Gate Packets recording every decision the user made and why.
