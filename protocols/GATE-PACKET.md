# Protocol P4 — Gate Packet & Open Questions

**Binding on:** orchestrator (author), all agents (contributors).
**File:** `run/<run-id>/gates/G<n>-PACKET.md`

Every gate is approved manually by the user. The user reads **one page**, not the full deliverable. The deliverable sits behind it.

---

## 1. Gate Packet structure (one page, hard limit)

```markdown
# Gate G<n> — <Phase Name>
Run: <run-id> · Date: <ISO> · Judge rounds used: <k>/10 · Ledger coverage: <0.xx>

## Recommendation
<One sentence. PROCEED / PROCEED WITH CONDITIONS / RE-SCOUT / KILL.>

## What changed since last gate
<3 bullets max. Only decision-relevant deltas.>

## Kill Criteria status
| Criterion (set at G0) | Threshold | Current reading | Status |
|---|---|---|---|
| ... | ... | ... | 🟢 clear / 🟡 near / 🔴 breached |

## Decisions you are approving
1. <Decision> — consequence if wrong: <...>
2. ...

## Open questions for you
<See §2 — each with quant / qual / risk.>

## Known gaps carried forward
| Unit | Why unresolved | Retries | Blocks |
|---|---|---|---|

## Behind this packet
- `deliverables/<file>.md` (<n> pages)
- `ledger/EVIDENCE.md` (<n> entries, <n> T1/T2)
- `ledger/JUDGE-LOG.md` (round-by-round)
```

If the packet exceeds one page, the Orchestrator has failed to decide something it should have decided.

---

## 2. Open Question format — mandatory quant + qual + risk

No open question may be posed to the user as bare prose. Every one uses this block:

```markdown
### OQ-<n>: <The question in one sentence>

**Why it matters:** <what downstream decision it gates>

| Option | Quantitative assessment | Qualitative assessment | Risk if chosen |
|---|---|---|---|
| A. <option> | <numbers: cost, time, TAM, latency, CPI delta, $ impact> | <fit, strategic posture, reversibility, team fit> | <named risk, impact H/M/L, probability H/M/L, mitigation> |
| B. <option> | ... | ... | ... |
| C. <option> | ... | ... | ... |

**Default if you don't answer:** <the option the Orchestrator will take, and why>
**Evidence behind these numbers:** E-xxx-nnn, E-xxx-nnn
**Confidence in this framing:** <0.xx> — <what would raise it>
```

**Rules**
- Quantitative column may never be empty. If no number exists, state the *range* and label it `ASSUMPTION`, with the basis.
- Risk column must name the risk, not describe unease. Impact and probability as H/M/L, plus a mitigation.
- There is always a stated **default**, so silence does not deadlock the run.
- Maximum **5 open questions per gate.** More than that means the phase was not actually finished — go back and scout.

---

## 3. The six gates

| Gate | Closes | User approves | Blocking condition |
|---|---|---|---|
| **G0** | Scoping | Product Scope Document + Kill Criteria + persona set | No research starts without signed Kill Criteria |
| **G1** | Discovery | Evidence base: academic, OSS, market, competitor sweeps | Coverage ≥0.70; contradictions adjudicated |
| **G2** | Market Feasibility | Market Feasibility Assessment (2–3 scenarios) + CPI ledger + Investment Analyst report | Scenario selection is a user decision, never automatic |
| **G3** | Reconciliation | Market↔Technical contradiction register, pre-technical | Any 🔴 contradiction must be resolved or accepted in writing |
| **G4** | Technical Feasibility | Technical Feasibility Assessment — 4 paths per feature, optimal selected | Every Phase-1 feature has a selected path with a named fallback |
| **G5** | Roadmap | Roadmap & Implementation Plan | Phase-1 scope fits stated capacity; no item below CPI 35 in Phase 1 |

**Ordering is hard.** G2 cannot open before G1 closes. Technical work (G4) cannot begin before G2 is user-approved. This is the brief's core sequencing rule and the Orchestrator enforces it.

---

## 4. User response handling

The user may reply to a gate with:

| Response | Orchestrator action |
|---|---|
| `APPROVE` | Close gate, open next phase, dispatch wave |
| `APPROVE WITH: <notes>` | Record notes as constraints in the ledger; they bind all downstream agents |
| `RE-SCOUT: <areas>` | Re-open the phase, dispatch fresh workers on named areas only, +1 round |
| `KILL` | Terminate run, write `POSTMORTEM.md` capturing why and what evidence drove it |
| Answers to OQ-n | Recorded as **T1 evidence** (user domain knowledge), flagged `USER-ASSERTED`, and usable in models |

`USER-ASSERTED` entries are T1 for confidence purposes but are tagged so the Judge can still flag when a whole conclusion rests on unverified user belief.
