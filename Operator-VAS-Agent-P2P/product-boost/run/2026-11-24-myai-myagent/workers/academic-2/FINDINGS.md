# Academic Scout 2 — RQ-2 speech-to-speech tail latency

**Run:** 2026-11-24-myai-myagent
**Agent:** academic-scout-2
**Question:** What p95 or equivalent tail latencies are reported for streaming ASR + a small language model + streaming TTS? Metric: milliseconds, the percentile, the hardware, and whether the path is lab, app, or cellular/VoLTE.
**Line:** p95 < 800 ms. This file does not loosen it. **K3 stays UNTESTED.** No row is a measurement on the Phase-1 channel (the mobile banking app). No stack is selected.

## Ledger entries written
E-ACA-020 … E-ACA-038 (19 rows). IDs E-ACA-039 is unused.

## What the opened pages actually support

A labeled **p95** of an ASR + language-model + TTS pipeline, when the page prints one, is **above 800 ms**. Figures under 800 ms that were opened are a mean, a median, a single measured time-to-first-audio, a first-chunk mean, an architectural frame delay, or a vendor p95 whose mouth-to-ear boundary is not stated.

| Clock | Lowest opened figure | Above or below 800 ms | Why it is not a K3 pass |
|---|---|---|---|
| E2E pipeline P95, lab GPU | 1,449 ms, PAVO Table 4, H100, Whisper-tiny + Gemma2 2B (E-ACA-022) | Above | PDF does not say first audio versus full-utterance completion. Lab, not the banking app, not VoLTE. |
| Caller-stop to first agent audio, p95, phone recording | 1,768 ms, ElevenLabs row (E-ACA-035) | Above | First audio, not the end of the spoken reply. Model size and GPU unstated. Path is Plivo to Telnyx/Twilio, not named VoLTE. |
| Client first audible chunk, P95 | 2,407 ms, Doubao mobile app (E-ACA-020) | Above | First chunk. Acoustic playback into the app, not a cellular call. |
| On-device cascade TTFA p95 | 11.92 s, Galaxy S26 Ultra (E-ACA-026) | Above | Includes remote tool calls. Audio injected into the phone, not VoLTE. |
| Partial clock, 90th percentile, not p95 | 1,020 ms, Freeze-Omni statistical total (E-ACA-032) | Above | Starts at “LLM interrupted,” ends at first PCM. Endpoint wait and network are extra allowances. Not the cascade. |
| Vendor footnote p95 | 713 ms, Twilio ConversationRelay (E-ACA-034) | Numeral below | Page does not say mouth-to-ear, hardware, or sample size. Same page’s mouth-to-ear **target** median is 1,115 ms. |

## Ranked findings

Citation counts are Semantic Scholar values retrieved on 2026-11-24, or “not retrieved” after HTTP 429. Months use the paper date below. Influence = (citations / months) × venue multiplier. A blank citation count is not scored.

| # | Paper / report | Venue | Date | Citations | Cit/mo | Influence | Relevance to scope | Ledger ID |
|---|---|---|---|---|---|---|---|---|
| 1 | FireRedChat | arXiv 2509.06502 | 2025-09 (id) | not retrieved | — | not scored | Cascade P50 and P95, first audio chunk, all above 800 ms. Doubao row is the official mobile app. | E-ACA-020 |
| 2 | PAVO | Anonymous OpenReview PDF, double-blind | date not in PDF | not retrieved | — | not scored (T3) | Lowest labeled E2E P95 of an ASR+LLM+TTS table: 1,449 ms on H100. All four P95s above 800 ms. | E-ACA-022 |
| 3 | Openbenchmarks voice-agent latency | Public method + call recordings | 2026-08-01 | n/a | — | n/a | Phone-call TTFAB p95 1,768–2,259 ms. Stack and GPU not disclosed. Not VoLTE. | E-ACA-035 |
| 4 | On-device speculative cascade | arXiv 2610.07641 | 2026-10-06 | not retrieved | — | not scored | Phone SoC. TTFA p95 11.92 s with tools inside the clock. | E-ACA-026 |
| 5 | Freeze-Omni latency table | arXiv 2411.00774 | 2024-11 (id) | not retrieved | — | not scored | p90 1,020 ms to first PCM after interrupt. Not a cascade p95. | E-ACA-032 |
| 6 | Telecom voice-agent pipeline | arXiv 2508.04721 | 2025-08-05 | not retrieved | — | not scored | H100 lab. Mean TTFA 678 ms, max total 3.154 s. No percentile. Not VoLTE. | E-ACA-021 |
| 7 | Voice-Light | arXiv 2609.20995 | 2026-09 (id) | not retrieved | — | not scored | Cascade median 758 ms to first server audio. Authors refuse a p95. Browser render median 836 ms. | E-ACA-023 |
| 8 | Salesforce realtime tutorial | arXiv 2603.05413 | 2026-03 (id) | not retrieved | — | not scored | One measured TTFA 755 ms. Component P50 sums are not a measured p95. | E-ACA-024, E-ACA-025 |
| 9 | Twilio core-latency guide | Vendor blog | 2025-11-17 | n/a | — | n/a (T4) | Mouth-to-ear target median 1,115 ms. Footnote p95 713 ms, boundary unstated. | E-ACA-034 |
| 10 | LLaMA-Omni | ICLR (Semantic Scholar) | 2024-09-10 | 251 | 9.48 | 12.32 | 226.13 ms is time to start of speech at chunk size 10, not a percentile and not the cascade. | E-ACA-027 |
| 11 | VocalNet-M2 | ICASSP, DOI page | 2025-11-13 | 0 on the DOI page | 0 | 0 | First-chunk means on one L20. Three means under 800 ms, three over. Not p95. | E-ACA-028 |
| 12 | Moshi paper + README | arXiv 2410.00037; GitHub README | 2024-10 (id) | not retrieved | — | not scored | 160 ms theoretical, 200 ms practical, L4 only in the README. Not a p95. | E-ACA-030, E-ACA-038 |
| 13 | Full-Duplex-Bench v1.5 | arXiv HTML; Semantic Scholar lists ICASSP | 2025-07 (id) | 93 | 5.55 | 5.55 | Mean response latency 1.18–2.25 s. No percentile. Moshi mean 1.67 s. | E-ACA-031 |
| 14 | FD-Bench | Interspeech 2025 | 2025-07-25 | 33 | 2.06 | 2.06 | Median first-speech-emit and interruption delays on H20. Not an ordinary-turn p95. | E-ACA-033 |
| 15 | GLM-4-Voice | arXiv 2412.02612 | 2024-12-03 | not retrieved | — | not scored | Architectural minimum block 0.8 s. No measured p95. | E-ACA-029 |
| 16 | Qwen2.5-Omni technical report | Qwen team PDF | 2025-03-26 | not retrieved | — | not scored | Streaming design. No wall-clock milliseconds. | E-ACA-036 |
| 17 | Exotel SIP streaming post | Vendor blog | 2026-09-02 | n/a | — | n/a (T4) | Names VoLTE inside an unsourced 40–150 ms one-way range. No pipeline p95. | E-ACA-037 |

Months for cit/mo, counted to 2026-11-24: LLaMA-Omni 26.47 (from 2024-09-10); Full-Duplex-Bench 16.77 (from 2025-07-01); FD-Bench 16.01 (from 2025-07-25); VocalNet-M2 12.37 (from 2025-11-13). Venue multipliers: ICLR 1.3, ICASSP and Interspeech 1.0. 251/26.47×1.3 = 12.32. 93/16.77×1.0 = 5.55. 33/16.01×1.0 = 2.06. 0/12.37×1.0 = 0.

## Technique → OSS pairings

No stack is selected. The pairings below are observations about which clock the papers timed. They are not a recommendation.

| Technique (paper) | Applies to (OSS project) | Expected gain | Implementation difficulty | Evidence |
|---|---|---|---|---|
| Sentence-level overlap of ASR, a quantized LM, and TTS | Not selected | Papers report a lower **first-audio** mean than the sum of full-component times. They do not report a p95 of the finished spoken reply under 800 ms. | Not assessed | E-ACA-021, E-ACA-024 |
| End-to-end speech model with a codec-frame delay | Not selected | 160–226 ms figures are frame or first-chunk clocks. A later bench’s mean response latencies for the same model class are above 1 s. | Not assessed | E-ACA-027, E-ACA-030, E-ACA-031 |
| Speculative generation before final end-of-turn | Not selected | Voice-Light’s 36-turn median to first server audio is 758 ms. The authors say this is not a population p95. Median to browser render is 836 ms. | Not assessed | E-ACA-023 |

## Negative results / known failure modes

| Finding | Impacts which FR/NFR | Severity | Ledger ID |
|---|---|---|---|
| Every labeled cascade P95 opened here is above 800 ms (1,449 ms and up in the lab; 1,768 ms and up on a recorded phone call; 2,407 ms and up for first audible chunk). | Speech-to-speech p95 < 800 ms. K3. | The line is missed by the tails that were actually labeled p95. K3 is still UNTESTED because none of these is the Phase-1 channel. | E-ACA-020, E-ACA-022, E-ACA-026, E-ACA-035 |
| Mean or single-run time-to-first-audio can sit under 800 ms while the same paper’s maximum, estimated tail, or full-component time sits over it. | Same NFR, if a mean is treated as a p95. | High, as a misreading risk. | E-ACA-021, E-ACA-024 |
| A 90th percentile of 1,020 ms is already over 800 ms on a clock that has not yet added endpointing or network. | Same NFR. | High. | E-ACA-032 |
| Authors of a 36-turn cascade study explicitly refuse a population p95. 21/36 turns were under 800 ms to first server audio; the median to the browser was 836 ms. | Same NFR. | High. A count of turns under 800 ms is not a p95. | E-ACA-023 |
| Qwen2.5-Omni’s own report gives no millisecond latency. A later ICASSP paper left it unmeasured because official streaming inference code was absent. | Same NFR. | Gap, not a pass. | E-ACA-036, E-ACA-028 |
| No opened source measures this pipeline’s p95 on VoLTE or a cellular air interface. | Brief latency sentence that names cellular/VoLTE, and the later re-test of the same 800 ms line. | The cellular sentence is unmeasured. | E-ACA-021, E-ACA-035, E-ACA-037 |

## Reception & replication

| Paper | Community signal | Replication status | Ledger ID |
|---|---|---|---|
| Moshi | README repeats “as low as 200 ms on an L4.” | Full-Duplex-Bench v1.5, a different clock, reports Moshi mean response latency 1.67±1.32 s on a local demo. FD-Bench median first-speech-emit delay after interruption is 2.0–4.2 s on one H20. The 200 ms figure was not reproduced as a turn-level percentile. | E-ACA-030, E-ACA-031, E-ACA-033, E-ACA-038 |
| Freeze-Omni | Paper’s own p90 to first PCM is 1,020 ms, and the text puts a real-scenario average near 1.2 s once endpointing and a network allowance are added. | Full-Duplex-Bench mean response latency 1.28±0.64 s. FD-Bench median interruption-response delay is 3.6–12.2 s. | E-ACA-032, E-ACA-031, E-ACA-033 |
| Twilio ConversationRelay | Marketing footnote p95 713 ms. | Openbenchmarks states Twilio’s agent product had not been dialled on that board. The phone-call p95s on that board are 1,768–2,259 ms. | E-ACA-034, E-ACA-035 |
| Qwen2.5-Omni | Technical report discusses initial packet latency and prints no milliseconds. | VocalNet-M2 excluded it from the first-chunk table. | E-ACA-036, E-ACA-028 |

## Dead ends

Queries and pages that must not be reused as a p95 of this pipeline:

- Qwen2.5-Omni technical report: opened, no wall-clock latency (E-ACA-036).
- VoLTE / cellular query: no ASR + SLM + TTS percentile on a VoLTE air interface. Exotel (2026-09-02) names VoLTE only inside an unsourced 40–150 ms one-way carrier range (E-ACA-037).
- `https://caller.digital/blog/openai-realtime-api-vs-voice-ai-platforms-india-2026` was opened. It asserts “900ms–1.4s p50 and 2s+ p95” on “real Indian PSTN legs” and mentions Jio VoLTE-to-2G handoffs as an audio problem. No sample size, no hardware, no table. Not ledgered.
- `https://www.testmuai.com/blog/voice-quality-testing/` was opened. It states “P50 of 1.4 to 1.7 seconds” and a “P95 under 3 to 5 seconds” target with no dataset. Not ledgered.
- `https://docs.cekura.ai/documentation/key-concepts/metrics/pre-defined-metrics` was opened. It defines percentile latency from stereo call audio and publishes no pipeline result.
- Deepgram, Ortavox, and Pazau appeared in search snippets with p95 numerals. Those pages were not opened. Their numerals are not in the ledger.
- Semantic Scholar returned HTTP 429 for Moshi, FireRedChat, arXiv:2508.04721, and GLM-4-Voice. Those citation counts are not invented. OpenAlex returned HTTP 403 for LLaMA-Omni.
- `https://github.com/kyutai-labs/moshi` returned an empty stub. The latency sentence was taken from the raw README, which was opened.
