# Product Research & Planning Agentic Framework — Running Brief

> Status: **BRIEF IN PROGRESS** — user still adding. Do not build until user says complete.
> Captured: 2026-09-06

---

## Brief Increment 1 (2026-09-06)

### Form factor
Markdown-based skill/agent framework. Each agent carries a system prompt + output template.

### Anchor artifact: Product Scope Document (7-pillar standard)
Template supplied verbatim by user — 7 pillars:
1. Executive Summary & Problem Space (problem, value prop, personas, metrics table w/ baseline/target/window)
2. Boundaries & Scoping Matrix (In Scope / Explicitly Out of Scope / Deferred Phase 2+)
3. Functional Requirements & User Journeys (Epics → FR-x.y → Gherkin Given/When/Then, happy path + fault tolerance)
4. Non-Functional Requirements (latency p95, RPS, scale, SLA, RPO/RTO, encryption, compliance, audit trails)
5. Technical Dependencies & Architecture Touchpoints (upstream, downstream, 3P vendors, infra footprint)
6. Assumptions, Risks & Mitigations (risk / impact H-M-L / probability H-M-L / mitigation)
7. Phasing & Milestone Breakdown (Phase 0 spike → Phase 1 MVP → Phase 2 GA/hardening)

### Scoping-agent system prompt (verbatim rules)
Persona: Expert Principal Technical Product Manager — Systems Scoping, Technical PRDs, Requirement Architecture.
1. **Ban Ambiguity** — no "fast", "intuitive", "user-friendly", "scalable" without concrete metrics.
2. **Strict Negative Scoping** — dedicated section on what is NOT in scope.
3. **Edge-Case Obsession** — happy path + ≥1 negative/boundary case per key FR.
4. **Actionable Acceptance Criteria** — Given/When/Then for all major functional points.
5. **Standard Output Structure** — the 7-pillar format above.

---

## Agent Roster (as briefed)

| # | Agent | Role |
|---|---|---|
| A1 | **Scoping Agent** | Works *with the user* to produce the Product Scope Document (7-pillar). Interactive. |
| A2 | **Orchestrator** | Spawns workers, routes all docs to the Judge, manages phase gating. |
| A3 | **Academic/Web Scraper Workers** (n) | Arxiv, Google Scholar, academic + industry research. Filter for *viral* work — high citation counts, public-forum reception, technical enhancements to candidate specs. |
| A4 | **GitHub Scraping Worker** | Find open-source projects that accelerate development. |
| A5 | **Market Feasibility Agent Set** | Market Feasibility Report — see below. |
| A6 | **Investment Analyst Agent** | Frames the product as a deal he might back. Identifies all KPIs/essential metrics relevant to *this* product; quantifies KPI → conservative business valuation. |
| A7 | **Judge (Pessimist)** | Receives every doc via Orchestrator. Can request creation of new agents to fill gaps. Must identify and correct **≥30%** of agent output. |
| A8 | **Technical Spec Agents (×3)** | Per feature, three alternative technology paths: (a) open source, (b) build from scratch, (c) off-the-shelf tools. Converge on the most optimal spec. Bias: prefer open source, improve it using academic research. |
| A9 | **Roadmap/Implementation Agent** | Implementation phases + project roadmap. |

## Market Feasibility Report — required contents
Section-breaker structure, detailed market research to establish Product-Market Fit.
Must present **2–3 distinct scenarios**, each with its own USP/Value Prop, Positioning, Revenue Model, and GTM.

Conclusion must deliver:
- Product Value Proposition
- Features Necessary
- Positioning
- Brand Philosophy ideas
- Possible GTM motions
- Revenue models
- Competitor research
- Barriers to entry
- Risk assessment

## Phase Gating (hard ordering)
1. **Product Research** must complete *before* Technical Feasibility begins.
2. **Technical Feasibility Assessment** — 3 specs per feature → optimal spec selection.
3. **Roadmap & Implementation Plan** — only after 1 and 2.

## Final Deliverables
1. Product Market Feasibility Assessment
2. Technical Feasibility Assessment
3. Roadmap and Implementation Plan

---

## Brief Increment 2 (2026-09-06) — Answers

### 1. Judge mechanics — quadrant elimination, not a 30% quota
- Judge scores every written unit on a **2×2 quadrant** (axes TBD in design: evidence strength × claim materiality).
- **Lower quadrant → eliminated**, task **retried** by a fresh worker.
- If the retry still yields nothing, **proceed with the gap explicitly flagged** and **ask the user to suggest improvements** in those areas.
- **Customer Pain Index (CPI)** maintained per Value Proposition — the prioritisation instrument across the whole framework.

### 2. Investment Analyst — valuation method
- **Multiples** or **Scorecard Method** for headline valuation.
- **DCF applied inside the Revenue Model**, requiring:
  - unit economics
  - number of customers needed to break even
  - CAC — **with a mandatory +50% buffer**

### 3. Research access
- **Web search only.** No MCP dependency. Do not stop on failure — keep searching.
- Append **`pdf`** as a search keyword to surface papers and research documents.

### 4. Scope
- **Generic framework.** Not Hashh-specific. (Hashh repo is only the authoring location.)
- Claude to propose improvements to the briefed design.

### 5. Gates
- **Every gate is manually approved by the user.**
- Every open question posed to the user must ship with:
  - **quantitative assessment**
  - **qualitative assessment**
  - **risk** attached to each option

### 6. Judge loop
- **Max 10 rounds**, then forced convergence with residual gaps recorded.
