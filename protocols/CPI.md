# Protocol P2 — Customer Pain Index (CPI)

**Binding on:** market-scout, market-feasibility, investment-analyst, reconciliation, roadmap.
**File:** `run/<run-id>/ledger/CPI.md`

CPI is the framework's single prioritisation instrument. Every Value Proposition, every feature, and every roadmap item inherits a CPI score. When two things compete for a slot, higher CPI wins and the doc must say so explicitly.

---

## 1. Formula

```
CPI_raw = Frequency × Severity × (6 − Workaround_Quality) × WTP_Signal
CPI     = round( CPI_raw / 7.5 , 1 )        # normalised to 0–100
```

Each input is scored **1–5**. `(6 − Workaround_Quality)` inverts it: a *good* existing workaround suppresses pain.

Max raw = 5 × 5 × 5 × 5 = 625 → CPI 83.3. Practical ceiling ~85; anything above 70 is a strong pain.

---

## 2. Input rubrics

### Frequency — how often the pain occurs for the persona
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Annually or less | Quarterly | Monthly | Weekly | Daily / continuous |

### Severity — cost of one occurrence
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Mild annoyance, no measurable cost | <30 min lost or <$100 | Hours lost, single-person blocking | Multi-person blocking, revenue at risk | Revenue loss, compliance breach, or customer churn |

### Workaround Quality — how well the pain is already solved
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| None exists | Painful manual hack | Manual but tolerable | Decent tool, imperfect fit | Incumbent solves it well |

### WTP Signal — evidence people pay to remove this pain
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| No evidence | Stated intent only (survey) | Budget line exists in category | Competitors monetising it today at disclosed prices | Buyers switching/paying premium; documented deal sizes |

---

## 3. Evidence requirement

**Every one of the four scores must cite ≥1 Evidence Ledger ID.** An uncited CPI is invalid and the Judge kills it on sight.

WTP_Signal specifically may not rest on T4 evidence alone — it feeds the revenue model.

---

## 4. Ledger table format

| VP / Feature | Persona | Freq | Sev | WQ | WTP | CPI | Evidence IDs | Confidence |
|---|---|---|---|---|---|---|---|---|
| Unified inbox across channels | RevOps lead | 5 | 4 | 3 | 4 | 32.0 | E-MKT-014, E-MKT-031, E-MKT-044, E-FIN-002 | 0.72 |

`Confidence` = mean confidence of the cited entries. Report CPI as `32.0 ± band` where band widens as confidence drops:
- confidence ≥0.8 → ±5
- 0.6–0.8 → ±10
- <0.6 → ±15, and the item **cannot** be a Phase-1 roadmap commitment.

---

## 5. Interpretation bands

| CPI | Band | Consequence |
|---|---|---|
| ≥ 55 | **Acute** | Anchor the value prop here. Must appear in Phase 1. |
| 35–54 | **Real** | Supporting feature. Phase 1 or 2. |
| 20–34 | **Latent** | Phase 2+. Do not build for it in MVP. |
| < 20 | **Noise** | Explicitly out of scope. Named in the Scoping Matrix negative column. |

---

## 6. Anti-gaming rules

1. A scenario may not score >2 VPs as Acute without T1/T2 evidence for each. Everything-is-urgent is the standard failure mode.
2. `Workaround_Quality` must be scored against the *actual* incumbent, named, with pricing. "No good alternative exists" requires a competitor sweep proving it.
3. If two VPs share the same persona and the same evidence IDs, they are one VP. Merge them.
4. CPI is recomputed after every Judge round. Score drift >15 points between rounds triggers a mandatory note explaining what evidence changed.
