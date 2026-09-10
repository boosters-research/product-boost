# Protocol P5 — Product Assessment & Viability Rubric (PAVR-10)

**Binding on:** assessment-engine, orchestrator, market-feasibility, investment-analyst, tech-optimizer.
**File:** `run/<run-id>/ledger/ASSESSMENT-SCORECARD.md`

The PAVR-10 rubric provides an objective, evidence-backed evaluation standard to score any product research brief, existing PRD, or research output.

---

## 1. The 10 Dimensions of Product Viability

Every product is evaluated across 10 core dimensions, scored **0 to 10** points each (Total 0–100):

| Dim | Dimension | Core Question | Primary Metric / Proof Standard | Weight |
|:---:|---|---|---|:---:|
| **D1** | **Problem Urgency & Customer Pain** | Is this a burning migraine or a mild itch? | CPI 2.0 Score (≥55 Acute), qualitative VoC verbatims | 15% |
| **D2** | **TAM, SAM & Market Dynamics** | Is the addressable market large, growing, and accessible? | Top-down TAM >$1B or Bottom-up SAM >$100M with >15% CAGR | 10% |
| **D3** | **Competitive Moat & Defensibility** | Can incumbents or fast-followers copy this in 90 days? | ≥1 validated 7-Powers moat (Switching cost, Network effect, Data gravity) | 10% |
| **D4** | **Value Proposition & Positioning** | Is differentiation sharp and instantly understandable? | Passes 3-point Distinctness Test vs direct incumbents | 10% |
| **D5** | **Unit Economics & Financial Viability**| Is gross margin healthy and CAC payback sustainable? | Payback <12mo (with 1.5x CAC buffer), Gross Margin ≥70% (SaaS) / ≥50% (AI) | 15% |
| **D6** | **Technical Feasibility & Architecture**| Can it be built reliably within timeline & budget? | Clear 4-path evaluation (OSS/Build/Buy/Compose), named fallbacks | 10% |
| **D7** | **AI & Compute Economics** *(if AI)* | Are inference costs, latency, and context budgets sustainable? | Cost per active user/session modeled at scale, <20% of ARPU | 10% |
| **D8** | **GTM Velocity & Distribution Moat** | How does the product acquire users efficiently? | Clear beachhead persona, organic/PLG viral loop or repeatable outbound CAC | 10% |
| **D9** | **Regulatory, Compliance & Safety** | Are privacy, legal, and compliance blockers mitigated? | GDPR/CCPA, SOC2, EU AI Act risk tier identified, audit timeline defined | 5% |
| **D10**| **Kill Criteria & Falsifiability** | Are mortality risks identified with hard tripwires? | 3–6 quantified, phase-tested Kill Criteria with zero active breaches | 5% |

---

## 2. Scoring Rubric per Dimension (0–10 Scale)

- **9–10 (World-Class / Production-Ready)**: Fully validated with T1/T2 evidence, clear quantitative metrics, deep competitor/technical benchmarks, no unmitigated risks.
- **7–8 (Strong / Actionable)**: Solid rationale with verified secondary evidence (T2/T3), minor gaps in edge cases or secondary assumptions.
- **5–6 (Moderate / Hypothesis-Heavy)**: Plausible logic but heavily reliant on T4 evidence or unvalidated assumptions. Requires active scouting.
- **3–4 (Weak / High-Risk)**: Significant blind spots, generic positioning, vague unit economics, or unquantified technical barriers.
- **0–2 (Critical Failure / Fatal Flaw)**: Contradicts empirical market reality, unviable unit economics, unmitigated compliance breach, or Kill Criterion breached.

---

## 3. Overall Viability Score & Verdict

$$\text{Viability Score} = \sum_{i=1}^{10} (\text{Score}_i \times \text{Weight}_i)$$

| Weighted Score | Classification | Gate Action |
|:---:|---|---|
| **85 – 100** | 🟢 **Greenlight (Invest / Build)** | Proceed to MVP execution / Sprint planning |
| **70 – 84** | 🟡 **Conditional Proceed** | Address named Q2 gaps in targeted re-scout, then proceed |
| **50 – 69** | 🟠 **Substantial Rework Required** | Major pivot on positioning, pricing, or architecture needed |
| **< 50** | 🔴 **Kill / Do Not Build** | Breaches core viability thresholds; write `POSTMORTEM.md` |

---

## 4. Assessment Output Structure

The Assessment Engine outputs `run/<run-id>/deliverables/ASSESSMENT-REPORT.md` containing:
1. Executive Summary & Viability Score (0-100)
2. Radar Chart / Dimension Breakdown Table
3. Critical Vulnerabilities & Red Flags (Top 3 Lethal Risks)
4. Evidence Coverage & Hallucination Audit
5. Contradiction Matrix (C1–C6 check)
6. Prescriptive Step-by-Step Remediation Plan
