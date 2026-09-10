# Protocol P3 — Judge Quadrant & Adversarial Loop

**Binding on:** judge-pessimist, steelman, orchestrator.
**File:** `run/<run-id>/ledger/JUDGE-LOG.md`

Replaces the "correct 30% of the work" quota with a mechanical elimination rule. Quotas force fake edits when the work is sound; the quadrant kills only what fails on evidence.

---

## 1. The unit of judgment

A **written unit** = one claim, one CPI row, one scenario assumption, one financial input, or one technical assertion. Not a paragraph, not a section. Every unit traces to an Evidence Ledger ID (Protocol P1) or it is automatically Q3.

---

## 2. The two axes

**X — Evidence Strength** = Ledger `confidence` (0.0–1.0). Threshold **0.60**.
**Y — Claim Materiality** = does the decision change if this unit is false? Threshold: **material** vs **incidental**.

Materiality test — a unit is *material* if it is true of any one of:
- It is an input to the revenue model, valuation, or CAC/breakeven math.
- It is a `WTP_Signal` or `Workaround_Quality` score in the CPI ledger.
- It is the reason a technology path was selected or rejected.
- It is a Kill Criterion status.
- Removing it changes a Phase-1 roadmap commitment.

Everything else is incidental.

---

## 3. The quadrants

```
                       Material
                          ▲
        Q2  RE-SCOUT      │      Q1  KEEP
        weak + matters    │      strong + matters
        → retry, hard     │      → verify, ship
   ───────────────────────┼───────────────────────►  Evidence
        Q3  ELIMINATE     │      Q4  DEMOTE          strength
        weak + trivial    │      strong + trivial
        → delete outright │      → footnote, not body
                          │
                     Incidental
```

| Q | Condition | Judge action |
|---|---|---|
| **Q1** | conf ≥0.60 AND material | Keep. Spot-verify one source per 10 units. |
| **Q2** | conf <0.60 AND material | **Retry.** Task returns to a *fresh* worker with different queries (§5). |
| **Q3** | conf <0.60 AND incidental | **Eliminate.** Strike from the document. No retry — it is not worth the round. |
| **Q4** | conf ≥0.60 AND incidental | Demote to appendix/footnote. Must not occupy body text or influence conclusions. |

**"Eliminate the lower quadrant" = delete all Q3, and retry all Q2.**

---

## 4. Pessimist mandate

The judge-pessimist must, per document, produce at minimum:

- A quadrant classification for **every** written unit.
- ≥3 **falsification attempts** — a specific search designed to *disprove* the strongest claim in the doc. Log the query and the result even when it fails to disprove.
- A **survivorship-bias check**: which companies/projects/papers would be missing from this analysis because they failed and stopped publishing?
- A **base-rate check**: what fraction of comparable products succeeded at this? If the doc implies better than base rate, it must justify why.
- A named list of **agents it wants spawned** to close gaps (Orchestrator may approve or deny; denial is logged with reason).

The pessimist has no authority to add content. Only to classify, demand, and strike.

---

## 5. Retry rules (Q2)

1. Retry goes to a **fresh worker instance** — never the agent that produced the unit. Authors defend; strangers re-examine.
2. Retry must use **different query strings** than the original (checked against `ledger/QUERIES.md`).
3. Retry must attempt a **different source class** — if the original was trade press, try filings, papers, pricing pages, job postings, or patent records.
4. **Maximum 2 retries per unit.** After the second failed retry the unit is marked `UNRESOLVED-GAP`:
   - It is removed from the body of the document.
   - It is listed in the deliverable's **Known Gaps** section with the queries attempted.
   - It is escalated to the user as an open question (Protocol P4 format) asking them to supply knowledge or accept the gap.
   - Any conclusion that depended on it is downgraded to a stated hypothesis.

---

## 6. Steelman counterweight

A lone pessimist systematically destroys good asymmetric bets. For every document the Judge processes, the **steelman** agent runs in parallel and produces:

- The strongest defensible case for the *lowest-scoring surviving* scenario.
- The disconfirming-evidence-for-the-pessimist pass: where is the pessimist's skepticism itself unevidenced?
- An explicit "what would have to be true" list for the optimistic case.

Orchestrator reconciles. Where pessimist and steelman disagree on a **material** unit, that disagreement is surfaced to the user in the Gate Packet as a decision point — it is not resolved silently by the machine.

---

## 7. Loop control

- **Hard cap: 10 rounds** per phase (a round = judge pass + retries + re-judge).
- **Early exit** when all three hold: no Q2 units remain, coverage ≥0.70 (P1 §5), and zero unadjudicated pessimist/steelman conflicts on material units.
- **Round 8 warning:** Orchestrator notifies the user that convergence is at risk and presents the residual gap list.
- **Round 10 forced convergence:** the document ships with a mandatory `## Convergence Failure` section listing every unresolved unit, its quadrant, retry history, and the decision it blocks.
- Rounds are counted per phase and logged: round number, units in each quadrant, coverage delta, retries dispatched. Coverage must improve by ≥0.03 per round or the Orchestrator declares stall and escalates early rather than burning rounds.
