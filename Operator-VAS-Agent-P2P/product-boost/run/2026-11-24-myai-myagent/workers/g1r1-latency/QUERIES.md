# Queries — g1r1-latency

Retry 1 of 2 for E-ACA-022, E-ACA-030, E-ACA-032, and E-ACA-038. Retrieved 2026-11-24. These strings were not the academic-2 query list. The anonymous OpenReview PAVO PDF, the kyutai Moshi README, the Moshi paper's 160/200 ms frame claim, and Table 4 of arXiv:2411.00774 were not reused as the measurement.

## Cascade speech-to-speech p95 (retries E-ACA-022)

| ID | Framing | Query | Outcome |
|---|---|---|---|
| Q-G1R1L-01 | Insider | `"95th percentile" OR p95 "first audio" cascaded ASR LLM TTS latency measurement pdf 2025` | Opened FireRedChat (already a kept ledger row; not recopied), the Twilio 2025-11-17 guide (already a ledger row; not recopied), and Shawaze Ahmer's July 2026 thesis. The thesis Table 5.1 is a dated, named-author cascade P95 and states that the clock stops at the first chunk ready for playback. E-ACA-075. |
| Q-G1R1L-02 | Buyer | `voice agent "time to first audio" p95 milliseconds cascade STT LLM TTS benchmark report pdf 2026` | Opened the Salesforce tutorial and the on-device cascade paper, both already ledger rows and not recopied. Opened Mathur et al., arXiv:2610.00316. Appendix H is a named-author cascade p95 that stops at the first emitted model audio unit. E-ACA-076. |
| Q-G1R1L-03 | Skeptic | `"mouth-to-ear" OR "end of user speech" "p95" milliseconds cascaded "ASR" "TTS" named measurement pdf 2025 2026` | Opened chapter 18 of the streaming-speech handbook. Voice-to-voice p95 on one RTX 4090, clock stops at the first audible sample. The opened chapter and the book index print no author name and no measurement date. E-ACA-077. A GitHub README snippet for cascade-realtime-gateway was not opened; its p95 is unused. |

## Moshi percentile with turn count and GPU (retries E-ACA-030 and E-ACA-038)

| ID | Framing | Query | Outcome |
|---|---|---|---|
| Q-G1R1L-04 | Insider | `Moshi "percentile" OR "95th" OR p95 response latency turns GPU benchmark pdf -readme` | Opened Nishi, arXiv:2609.13445 (decision-time p95, 1,000 forward steps, RTX PRO 6000; not a turn). E-ACA-080. Opened MuDuSi (handler p95 on B200; caption says this is not end-to-end response latency). E-ACA-079. Opened the Spheron cloud page; the Moshi p95 is printed with a tilde and no turn count, so it is not a ledger measurement. |
| Q-G1R1L-05 | Skeptic | `"Moshi" "response latency" distribution OR histogram OR "95th percentile" OR p95 turns evaluation arxiv pdf 2025` | No opened histogram or turn-counted speech-to-speech p95. Hits restated the 160/200 ms frame claim or pointed at the Nishi decision-time benchmark. The frame claim was not reused. |
| Q-G1R1L-06 | Buyer | `"Moshi" voice agent "p95" OR "95th percentile" milliseconds turns OR sessions GPU measured benchmark pdf` | Same Spheron page. Opened fal.ai's Moshi deploy note: one H100, reply delay described as about one second on a 27-second clip with three recorded questions. That is not a percentile. Opened the Nishi PDF again and confirmed 45.60 ms. The joint measurement (speech-to-speech percentile, turn count, and GPU) was not opened. E-ACA-084. |

The Mathur et al. Moshi rows were found from Q-G1R1L-02, then read in Appendix D and Appendix H. They supply a p95 and one A100-SXM4-80GB, and they do not print the turn count. E-ACA-078.

## Freeze-Omni first-audio p95 with a named GPU (retries E-ACA-032)

| ID | Framing | Query | Outcome |
|---|---|---|---|
| Q-G1R1L-07 | Insider | `Freeze-Omni "p95" OR "95th percentile" OR "99th" first audio latency GPU benchmark pdf` | Opened arXiv:2411.00774 again, including the v3 HTML. Table 4 is a 90th percentile of 1,020 ms. The v3 HTML names one NVIDIA A100. That table was excluded. Opened URO-Bench: one NVIDIA A40, first-packet figures 3,675.47 ms and 4,647.90 ms, not labeled a percentile. E-ACA-082. |
| Q-G1R1L-08 | Skeptic | `"Freeze-Omni" "first packet" OR "first audio" latency A100 OR A40 OR H100 percentile OR mean samples pdf -2411.00774` | Opened Soltani and Boulianne, EMNLP 2026 Industry Track. Freeze-Omni on one NVIDIA A40 48GB. Six latency figures, none labeled a p95. E-ACA-081. Also opened the ICML 2025 PDF of Freeze-Omni; its Table 4 is the same 90th percentile and the caption does not name a GPU. Excluded. |
| Q-G1R1L-09 | Buyer | `voice agent "time to first audio" p95 milliseconds cascade STT LLM TTS benchmark report pdf 2026` | Same string as Q-G1R1L-02, read for a Freeze-Omni p95. None of the opened cascade benchmarks in that result is a Freeze-Omni first-audio p95. |

## Metadata fetch

| ID | Query | Outcome |
|---|---|---|
| Q-G1R1L-10 | `https://export.arxiv.org/api/query?id_list=2610.00316,2609.10765,2609.13445,2502.17810` | Dates used as as_of: 2610.00316 submitted 2026-09-29, comment "Under submission at EACL 2027"; 2609.10765 submitted 2026-09-09, EMNLP 2026 Industry Track pp. 2302–2310; 2609.13445 updated 2026-09-16; 2502.17810v3 updated 2025-08-10, no proceedings venue in the record. |
| Q-G1R1L-11 | `site:semanticscholar.org DuplexSpeechBench Mathur 2610.00316 citations` | The result pages did not show a citation count for 2610.00316, 2609.10765, 2609.13445, 2502.17810, the Twente thesis, or MuDuSi. Influence is unscored. Counts were not filled in. |

## Dead ends (do not treat as a p95)

| What was opened or seen | Why it is not the retried measurement |
|---|---|
| Spheron, "Real-Time Speech-to-Speech AI on GPU Cloud", https://www.spheron.network/blog/speech-to-speech-gpu-cloud-moshi-sesame-csm-hertz-dev/ | Prints Moshi TTFA p50 ~200 ms and p95 ~250 ms on an H100 SXM5, one session, and says the p95 rises to 350–500 ms at 3–4 sessions. Tildes, no turn count, no sample size. Cloud marketing page. Not a ledger measurement. A sub-800 ms tilde is not a pass of the 800 ms line. |
| fal.ai, https://fal.ai/docs/examples/audio-speech/deploy-realtime-voice-chat | One H100. "About one second" after the end of each question, network included, on a 27-second clip with three recorded questions. Not a percentile. |
| kyutai-labs/moshi issue 369, seen in a search highlight and not opened as a page | The visible text is a user report of Kyutai TTS time-to-first-byte on an L40S, not a Moshi speech-to-speech percentile. Numbers in the snippet are unused. |
| `https://github.com/rasonyang/cascade-realtime-gateway/blob/main/README.md` | Search snippet only. Not opened. Any p95 in the snippet is unused. |
| Full-Duplex-Bench v1's 0.265 s Moshi average, as quoted by the streaming-speech chapter | The chapter calls it an average. This retry did not open arXiv:2503.04721, so that number is not a new row. An average would not be a p95, and it would not pick a winner against the 1.67 s mean. |
| Q-G1R1L-05 | No Moshi response-latency histogram with a turn count and a GPU. |
| Q-G1R1L-07 and Q-G1R1L-08 | No Freeze-Omni first-audio p95 outside the excluded Table 4. |
