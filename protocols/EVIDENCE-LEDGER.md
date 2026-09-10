# Protocol P1 — Evidence Ledger

**Binding on:** every agent that writes a factual claim.
**File:** `run/<run-id>/ledger/EVIDENCE.md` (append-only)

The Ledger is the spine of the framework. No claim survives a gate unless it is in the Ledger. The Judge scores the Ledger, not prose.

---

## 1. Entry format

Every claim gets one row. Append only — never edit a row; supersede it with a new row and mark the old `SUPERSEDED-BY`.

| Field | Rule |
|---|---|
| `id` | `E-<phase>-<nnn>` e.g. `E-MKT-014`, `E-TECH-003`, `E-FIN-021` |
| `claim` | One sentence. Falsifiable. No adjectives without numbers. |
| `tier` | T1–T4 (§2) |
| `source` | Full URL. For papers: title + venue + year + URL. |
| `retrieved` | ISO date the agent actually fetched it |
| `as_of` | Date the *underlying data* refers to (often ≠ retrieved) |
| `agent` | Which agent wrote it |
| `confidence` | 0.0–1.0, agent's own (§3) |
| `contradicts` | IDs of ledger entries this conflicts with, or `—` |
| `status` | `OPEN` / `VERIFIED` / `KILLED` / `SUPERSEDED-BY:<id>` |

Row template:

```
| E-MKT-014 | Mid-market RevOps teams run a median 4.2 disconnected outreach tools (n=310 survey) | T2 | https://... | 2026-09-06 | 2026-Q1 | market-scout-2 | 0.7 | — | OPEN |
```

---

## 2. Confidence tiers

| Tier | Definition | Examples |
|---|---|---|
| **T1** | Peer-reviewed, audited, or legally filed | Journal/conference papers, 10-K/S-1 filings, government statistics, audited financials |
| **T2** | Named-methodology primary research | Analyst reports with disclosed method, vendor-published benchmarks with reproducible setup, large-n surveys with published sampling |
| **T3** | Credible secondary reporting | Trade press, engineering blogs from the org that built the thing, conference talks, well-sourced newsletters |
| **T4** | Anecdote / unverified | Forum posts, Reddit/HN comments, review-site free text, single-user testimonials, vendor marketing pages |

**Rules**
- A T4 entry alone can never support a *material* claim (§ Judge Quadrant). It can support a *directional* claim if ≥3 independent T4 sources agree — record all three IDs.
- Any number that enters a financial model must be **T1 or T2**, or explicitly flagged `ASSUMPTION` with a stated range.
- Marketing pages of the subject product or its competitors are **T4**, always. No exceptions.

---

## 3. Confidence scoring

`confidence = tier_base × recency_factor × corroboration_factor`

| Component | Value |
|---|---|
| `tier_base` | T1 = 0.9, T2 = 0.75, T3 = 0.55, T4 = 0.3 |
| `recency_factor` | `as_of` within 12mo = 1.0; 12–24mo = 0.85; 24–48mo = 0.7; >48mo = 0.5 (0.9 if structural//slow-moving domain — state why) |
| `corroboration_factor` | 1 source = 1.0; 2 independent = 1.1; ≥3 independent = 1.2 (cap total at 1.0) |

Round to 2dp. Show the arithmetic in a `notes` column when it is non-obvious.

---

## 4. Contradiction handling

When an agent finds a source conflicting with an existing entry:

1. Log the new entry with `contradicts: E-xxx-nnn`.
2. Do **not** silently pick a winner.
3. Raise a `CONTRADICTION` item to the Orchestrator.
4. Orchestrator dispatches a **tiebreak scout** — one worker, one job: find a T1/T2 source that adjudicates.
5. If unresolved after tiebreak, both entries survive and the downstream doc must present the range, not a point estimate.

---

## 5. Coverage metric (gate condition)

Per phase:

```
coverage = (# material claims with ≥1 T1/T2 entry) / (# material claims)
```

**Gate floor: coverage ≥ 0.70 for material claims.** Below that, the phase does not present to the user — it re-scouts (subject to the 10-round cap, Protocol P3).

---

## 6. Search discipline (research agents)

- Web search is the only required data source. No connector dependency.
- **Append `pdf` as a keyword** when hunting papers, filings, or analyst reports: `"<topic>" benchmark pdf`, `"<topic>" survey 2026 pdf`.
- Run at minimum three query framings per research question: the *insider* term, the *buyer* term, and the *skeptic* term (e.g. `"agentic RAG latency"`, `"AI support bot slow"`, `"RAG doesn't work in production"`).
- Never stop on a failed search. Reformulate and continue. Log dead-end query strings in `ledger/QUERIES.md` so retries do not repeat them.
- Record the query string that produced each entry. Retries must use *different* queries.
