# Academic Scout g1r1-latency — cascade p95, Moshi percentile, Freeze-Omni first-audio p95

Retry 1 of 2. Units retried: E-ACA-022, E-ACA-030, E-ACA-032, E-ACA-038. The anonymous OpenReview PAVO PDF, the kyutai README, the Moshi paper's 160/200 ms frame claim, and Table 4 of arXiv:2411.00774 are not the measurements below.

K3 is not marked. C-ACA-02 stays OPEN. No winner is picked against the 1.67 s mean.

## Ledger entries written

E-ACA-075 … E-ACA-084

## Ranked findings

Citation counts were not on the Semantic Scholar pages returned on 2026-11-24. Influence is unscored rather than filled with a zero. Months are from the paper date to 2026-11-24. Venue multipliers are the ones that would apply if a count is later retrieved.

| # | Paper / report | Venue | Date | Citations | Cit/mo | Influence | Relevance to scope | Ledger ID |
|---|---|---|---|---|---|---|---|---|
| 1 | Ahmer, streaming speech-to-speech RAG thesis | University of Twente MSc (multiplier not in the protocol table) | 2026-07 | not retrieved | — | unscored | Named author, dated cascade P95, 165 turns, clock stops at first chunk ready for playback. Every measured P95 is above 800 ms. | E-ACA-075 |
| 2 | Mathur, Lipka, Jin, Manocha, DuplexSpeechBench-Document Grounding | arXiv, under submission at EACL 2027 (preprint 0.6 if still unreviewed) | 2026-09-29 | not retrieved | — | unscored | Named authors, dated cascade p95 of 61,563 ms. Appendix H stops at the first audio unit. The metrics sentence says first output token. | E-ACA-076 |
| 3 | Streaming-speech handbook, chapter 18 | Web handbook, author not printed on the opened pages (0.6) | UNKNOWN | not retrieved | — | unscored | Cascade voice-to-voice p95 on one RTX 4090, clock stops at the first audible sample. Lowest p95 is 856 ms. Not dated and not named on the page. | E-ACA-077 |
| 4 | Mathur et al., Moshi rows of the same benchmark | arXiv preprint (0.6) | 2026-09-29 | not retrieved | — | unscored | Moshi p95 and one A100-SXM4-80GB. Turn count is not printed. Tier T3 p95 is 895 ms. Does not pass 800 ms and does not close C-ACA-02. | E-ACA-078 |
| 5 | Soltani and Boulianne, French full-duplex benchmark | EMNLP 2026 Industry Track (solid peer-reviewed, 1.0) | 2026-09-09 | not retrieved | — | unscored | Freeze-Omni on one A40 48GB. Six latency figures, none labeled a p95. 0.890 s is not a pass. | E-ACA-081 |
| 6 | Yan et al., URO-Bench v3 | arXiv, no proceedings venue in the API record (0.6) | 2025-08-10 | not retrieved | — | unscored | Freeze-Omni first packet 3,675.47 ms and 4,647.90 ms on one A40. Not labeled a percentile. | E-ACA-082 |
| 7 | Jung and Choo, MuDuSi | KAIST technical report (0.8, the authors built the simulator) | 2026-10-13 | not retrieved | — | unscored | Moshi handler p95 on B200. The paper says this is not end-to-end response latency. | E-ACA-079 |
| 8 | Nishi, spurious onsets | arXiv preprint (0.6) | 2026-09-16 | not retrieved | — | unscored | Moshi 95th-percentile decision time 45.60 ms on one RTX PRO 6000, over 1,000 forward steps. Not a turn. | E-ACA-080 |

## Technique → OSS pairings

| Technique (paper) | Applies to (OSS project) | Expected gain | Implementation difficulty | Evidence |
|---|---|---|---|---|
| Stop the cascade clock at the first playback chunk, and do not add overlapping stages | A streaming ASR + LLM + TTS loop of the kind Ahmer instrumented (Deepgram, an LLM, Cartesia) | The thesis shows stages overlap, so a sum of stage times is not the end-to-end P95. It does not show a P95 under 800 ms. | The measurement is one author's pilot calls in eu-west-1, not a packaged patch. | E-ACA-075 |
| Read a full-duplex frame budget separately from handler time | kyutai-labs/moshi | MuDuSi's 26 ms handler p95 does not replace a speech-to-speech percentile. Nishi's 45.60 ms is compute inside one 80 ms frame. | Both are external harnesses, not a Moshi latency patch. | E-ACA-079, E-ACA-080 |

No pairing is a path under 800 ms p95 on the Phase-1 channel.

## Negative results / known failure modes

| Finding | Impacts which FR/NFR | Severity | Ledger ID |
|---|---|---|---|
| The dated named-author cascade P95s that were opened are 2.93 s and higher (Ahmer) and 61.4 s (Mathur et al., API stalls included). The unsigned RTX 4090 chapter's lowest voice-to-voice p95 is 856 ms. | Speech-to-speech p95 under 800 ms | The opened cascade tails sit above the line. None of them is the Phase-1 channel, so K3 stays untested. | E-ACA-075, E-ACA-076, E-ACA-077 |
| No Moshi speech-to-speech percentile was opened that also states a turn count and a GPU. | The same latency line, and the conflict between the 160/200 ms frame claim and the 1.67 s mean | C-ACA-02 stays OPEN. A 737 ms FTED p95 without a turn count does not pick a winner. | E-ACA-078, E-ACA-084 |
| No Freeze-Omni first-audio p95 on a named GPU was opened outside Table 4, and Table 4 is a 90th percentile of 1,020 ms. | The same latency line | The A40 figures are not a p95. K3 is not marked, and the search is not a breach. | E-ACA-081, E-ACA-082, E-ACA-083 |

## Reception & replication

| Paper | Community signal | Replication status | Ledger ID |
|---|---|---|---|
| Ahmer thesis | Opened as the university PDF. No citation count retrieved. | Single-author instrumentation of 23 calls. The 3.87 s figure is the author's arithmetic, not a remeasurement. | E-ACA-075 |
| Mathur et al. | arXiv comment says under submission at EACL 2027. Citation count not retrieved. | One benchmark. Table 7 and Table 23 both print Moshi p95, and they are not the same number (737 ms pooled; tier p95s 612–895 ms). Both are reported. | E-ACA-076, E-ACA-078 |
| Soltani and Boulianne | EMNLP 2026 Industry Track, pp. 2302–2310. Citation count not retrieved. | The paper says its English Freeze-Omni results are generally consistent with FDB v1.0. That sentence is not a p95. | E-ACA-081 |
| Nishi | Code repository named in the paper. Citation count not retrieved. | The 45.60 ms figure is the author's own forward-step benchmark. | E-ACA-080 |
| Spheron and fal.ai | Opened and rejected. Spheron uses tildes. fal.ai says "about one second" on one clip. | Not a replication of a percentile. | E-ACA-084 notes |

## Dead ends

Queries and pages that did not produce the missing measurement are in `QUERIES.md`. The short list:

- No opened Moshi speech-to-speech percentile states both a turn count and a GPU.
- No opened Freeze-Omni first-audio p95 on a named GPU exists outside the excluded Table 4, which is a 90th percentile.
- The Spheron ~250 ms H100 cell and the fal.ai "about one second" H100 note were opened and are not percentiles with a turn count.
- A cascade-realtime-gateway README p95 appeared only as a search snippet and was not opened.
