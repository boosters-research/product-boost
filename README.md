# Product Research & Assessment Engine 2.0

An enterprise-grade, gated, adversarial, evidence-first product research engine and automated viability evaluator.

Built upon the principles of [`boosters-research/product-boost`](https://github.com/boosters-research/product-boost) and expanded with **8 specialized skills**, **automated assessment engine CLI**, **AI token economics**, **Voice-of-Customer mining**, and a **10-dimension Product Viability Matrix (PAVR-10)**.

---

## What It Produces

1. **Product Viability Assessment Report** (`deliverables/ASSESSMENT-REPORT.md`) — Automated 10-dimension audit (0–100 score), radar chart, top 3 lethal red flags, and contradiction analysis.
2. **Product Scope Document & Kill Criteria** (`deliverables/00-PRODUCT-SCOPE.md`) — 7-pillar PRD with Gherkin acceptance criteria and 3–6 quantified mortality tripwires.
3. **Market Feasibility & Moat Assessment** (`deliverables/01-MARKET-FEASIBILITY.md`) — 2–3 distinct scenarios, 7-Powers defensibility audit, CPI 2.0 scoring, and PMF validation.
4. **Investment & Unit Economics Model** (`deliverables/02-INVESTMENT-ANALYSIS.md`) — LTV/CAC with mandatory 1.5x buffer, payback periods, DCF sensitivity, and valuation scorecard.
5. **Technical & AI Architecture Specification** (`deliverables/03-TECHNICAL-FEASIBILITY.md`) — 4-path comparison (OSS / Build / Buy / Compose), token inference unit cost model, latency SLA, and 24-month TCO.
6. **Product Roadmap & Implementation Plan** (`deliverables/04-ROADMAP.md`) — CPI-ordered backlog, capacity-checked (0.7x rule), dependency graph, and P50/P80 estimates.
7. **GTM, Pricing & Compliance Specs** (`templates/06-GTM-PRICING-SPEC.md` & `templates/07-COMPLIANCE-AUDIT.md`) — Packaging tiers, CAC by channel, EU AI Act, GDPR, and SOC 2 audits.

---

## Directory Structure

```
product-research-engine/
├── ASSESSMENT-KICKOFF.md             # Ingest & assess an existing draft or response
├── ORCHESTRATOR-2.0-KICKOFF.md       # Start a full multi-agent research run
├── EXECUTION-PLAN.md                 # Master stage-gate runbook
├── engine/
│   ├── assessment_engine.py          # Python assessment engine & CLI
│   └── test_assessment_engine.py     # Automated test suite
├── protocols/
│   ├── PRODUCT-ASSESSMENT-RUBRIC.md  # P5: 10-dimension viability rubric
│   ├── CPI-2.0.md                    # P2.1: Customer Pain Index with VoC
│   ├── COMPLIANCE-SAFETY-MATRIX.md   # P6: Regulatory & AI safety matrix
│   ├── EVIDENCE-LEDGER.md            # P1: Evidence tiering & confidence scoring
│   ├── JUDGE-QUADRANT.md             # P3: Adversarial elimination loop
│   └── GATE-PACKET.md                # P4: One-page decision packets
├── skills/
│   ├── assessment-engine/            # Automated evaluator
│   ├── voice-of-customer/            # Real-world customer review miner
│   ├── pricing-strategist/           # Pricing tiers & elasticity modeling
│   ├── compliance-risk/              # Legal, GDPR & EU AI Act officer
│   ├── gtm-growth-strategist/        # Distribution moats & channel CAC
│   ├── ai-systems-architect/         # Token economics & LLM infrastructure
│   ├── moat-auditor/                 # 7-Powers defensibility & copy resistance
│   ├── persona-simulator/            # Synthetic buyer interview simulator
│   ├── orchestrator/                 # Pipeline coordinator
│   ├── scoping-agent/                # Principal PM & PRD author
│   ├── academic-scout/               # SOTA academic & paper search
│   ├── oss-scout/                    # GitHub OSS & license audit
│   ├── market-scout/                 # 6-sweep market research
│   ├── market-feasibility/           # Scenario generator
│   ├── investment-analyst/           # Financial & unit economics modeler
│   ├── judge-pessimist/              # Adversarial falsification auditor
│   ├── steelman/                     # Asymmetric opportunity defender
│   ├── reconciliation/               # C1-C6 contradiction resolver
│   ├── tech-path-agent/              # 4-path tech spec author
│   ├── tech-optimizer/               # Weighted matrix & TCO calculator
│   └── roadmap-agent/                # CPI-ordered roadmap architect
└── templates/
    ├── ASSESSMENT-REPORT.md
    ├── PRODUCT-SCOPE-DOC.md
    ├── MARKET-FEASIBILITY.md
    ├── INVESTMENT-ANALYSIS.md
    ├── TECH-FEASIBILITY.md
    ├── TECH-SPEC.md
    ├── ROADMAP.md
    ├── 05-AI-COMPUTE-ARCH.md
    ├── 06-GTM-PRICING-SPEC.md
    └── 07-COMPLIANCE-AUDIT.md
```

---

## Quick Start Guide

### 1. Ingest & Assess an Existing Response / Draft
Run the assessment engine CLI directly:
```bash
uv run python engine/assessment_engine.py --file path/to/previous_response.md
```
Or evaluate directly in chat using the prompt in `ASSESSMENT-KICKOFF.md`.

### 2. Calculate Customer Pain Index (CPI 2.0)
```bash
uv run python engine/assessment_engine.py --cpi --freq 5 --sev 4 --wq 2 --wtp 4 --voc 1.2
```

### 3. Start a Full Research Run
Copy `ORCHESTRATOR-2.0-KICKOFF.md` into your agent session and supply your product brief.
