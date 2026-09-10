# Technical Feasibility Assessment — [Product Name]

Run: `<run-id>` · Date: `<ISO>` · Judge rounds: `<k>/10` · Approved scenario: `<name>`

---

## 1. Executive Summary & Selected Architecture
- **Verdict:** [FEASIBLE / FEASIBLE WITH CONDITIONS / NOT FEASIBLE AS SCOPED]
- **Selected approach:** [per cluster, one line each]
- **24-month TCO:** `$X` · **Gross margin at approved price:** `X%`
- **Critical technical risk:**
- **What would change the selection:**

## 2. Weighting Rationale *(declared before scoring)*
| Criterion | Weight | Deviation from default | Justification |
| :--- | :--- | :--- | :--- |

## 3. Per-Cluster Decision Matrices

### Cluster: [name]
| Criterion | Weight | P-OSS | P-BUILD | P-BUY | P-COMPOSE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| NFR satisfaction | 25% | | | | |
| 24-month TCO | 20% | | | | |
| Time to Phase 1 | 15% | | | | |
| Reversibility | 10% | | | | |
| Team feasibility | 10% | | | | |
| Risk profile | 10% | | | | |
| Gross-margin impact | 10% | | | | |
| **Weighted total** | | | | | |

- **Selected:** · **Fallback:** · **Switch trigger:**
- **Disqualified:** [path — NFR failed]
- **Ideas adopted from rejected paths:**

*(Repeat per cluster.)*

## 4. Integrated Architecture

```mermaid
graph TD
```

### Cross-cluster seams
| Seam | Clusters | Mechanism | Risk | Cost |
| :--- | :--- | :--- | :--- | :--- |

### Cross-cluster optimisations
[Shared runtime / data store / deployment savings taken, and what they cost locally.]

## 5. Consolidated FR Coverage
| FR | Cluster | Path | How satisfied | Confidence | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 6. NFR Compliance
| NFR | Target | Delivered | Evidence | Margin | Risk if missed |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 7. Academic Improvements Adopted
| Technique | Paper | Applied to | Gain | Cost | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 8. Cost Model
| Line | Build (eng-wks) | Run/mo @100 | @1k | @10k |
| :--- | :--- | :--- | :--- | :--- |

- **COGS per unit:** @100 `$X` · @1k `$X` · @10k `$X`
- **Gross margin at approved price:** @100 `X%` · @1k `X%` · @10k `X%`
- **Feedback to Investment Analyst:** [does this break the DCF's margin assumption? Y/N — if Y, escalate]

## 9. Build Plan
| Cluster | Phase 0 | Phase 1 | Phase 2 | Total eng-weeks |
| :--- | :--- | :--- | :--- | :--- |

## 10. Technical Risk Register
| Risk | Impact | Prob | Mitigation | Leading indicator | Owner role |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 11. Phase 0 Spikes
| # | Spike | Question | Duration | Cost | Pass criterion | Decision it unblocks |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

## 12. What We Rejected and Why
| Path | Cluster | Weighted score | Primary reason rejected | Ideas we kept |
| :--- | :--- | :--- | :--- | :--- |

## 13. Known Gaps & Convergence Notes
| Unresolved unit | Why | Retries | What it blocks |
| :--- | :--- | :--- | :--- |
