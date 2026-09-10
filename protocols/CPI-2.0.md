# Protocol P2.1 — Customer Pain Index 2.0 (CPI 2.0)

**Binding on:** market-scout, voice-of-customer, market-feasibility, pricing-strategist, investment-analyst, roadmap-agent.
**File:** `run/<run-id>/ledger/CPI.md`

CPI 2.0 is the framework's single objective prioritisation instrument. It combines empirical severity, incumbent friction, pricing willingness, and verified Voice-of-Customer (VoC) sentiment.

---

## 1. The CPI 2.0 Formula

```
CPI_raw = Frequency × Severity × (6 − Workaround_Quality) × WTP_Signal × VoC_Multiplier
CPI     = min(100.0, round( CPI_raw / 7.5 , 1 ))
```

Where:
- **Frequency** (1–5): How often the pain occurs for the target persona.
- **Severity** (1–5): Measurable financial, time, compliance, or churn cost of one occurrence.
- **Workaround Quality** (1–5): How satisfactorily current market alternatives solve the pain (`(6 - WQ)` inverts it so poor workarounds increase pain).
- **WTP Signal** (1–5): Verified empirical evidence of willingness-to-pay (budget lines, competitor pricing, deal sizes).
- **VoC Multiplier** (0.8–1.2): Grounded sentiment adjustment from real customer reviews (G2, Capterra, Reddit, App Store) and user interviews:
  - `1.2`: High active desperation / viral churn complaints against incumbents.
  - `1.0`: Standard validated complaint frequency.
  - `0.8`: Passive preference / low switching motivation in user verbatims.

---

## 2. Input Rubrics

### Frequency (1–5)
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Annually or less | Quarterly | Monthly | Weekly | Daily / Continuous |

### Severity (1–5)
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Mild cosmetic annoyance | Minor friction (<30 min lost, <$100) | Hours lost, single-operator blocker | Team-wide blocker, revenue/deal at risk | Critical revenue loss, compliance breach, catastrophic downtime |

### Workaround Quality (1–5)
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| No workaround exists | Fragile, painful manual hack | Manual but tolerable workflow | Decent point solution, partial fit | Dominant incumbent solves it seamlessly |

### WTP Signal (1–5)
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| No willingness evidence | Stated interest / survey intent | Dedicated budget line exists | Direct competitors monetising at scale | High contract values, proven switching spend |

---

## 3. Evidence & Citation Standard

1. **Every axis must cite ≥1 Evidence Ledger ID (`E-MKT-`, `E-VOC-`, `E-FIN-`).**
2. An uncited CPI row is instantly marked **Q3 (Eliminated)** by the Judge loop.
3. WTP Signal and VoC Multiplier cannot rely exclusively on T4 evidence.

---

## 4. Interpretation Bands & Roadmap Impact

| CPI 2.0 Score | Pain Classification | Actionable Consequence |
|:---:|:---:|---|
| **≥ 55.0** | 🔥 **Acute Pain** | Core Value Proposition anchor. **Mandatory Phase 1 MVP item.** |
| **35.0 – 54.9** | ⚡ **Real Pain** | Supporting feature. Phase 1 fast-follow or Phase 2. |
| **20.0 – 34.9** | ⏳ **Latent Pain** | Phase 2+ backlog. Never build in initial MVP. |
| **< 20.0** | 🚫 **Noise / Trivial** | **Explicitly Out of Scope.** Place in Scoping Matrix negative column. |

---

## 5. Anti-Gaming Rules
1. **Max 2 Acute Claims without T1/T2 Proof:** No scenario may claim more than 2 Acute VPs unless backed by T1/T2 primary research.
2. **Incumbent Specification:** `Workaround_Quality` must explicitly name the competitor/tool being benchmarked.
3. **Score Drift Tracking:** If CPI changes by >10 points between judge rounds, a mandatory delta note must cite the newly discovered evidence.
