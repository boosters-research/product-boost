# Queries — academic-scout-2 (RQ-2)

**Run:** 2026-11-24-myai-myagent
**Date searched:** 2026-11-24
**Rule:** Web search only. Three framings plus `pdf`. Retries must use a different string. Shared `ledger/QUERIES.md` was not edited.

## Framing 1 — insider (streaming ASR + LM + TTS, percentile, paper)

| Query ID | Query string | Outcome |
|---|---|---|
| Q-ACA2-01 | `"speech-to-speech" latency p95 OR "95th" streaming ASR TTS LLM arxiv pdf` | Opened FireRedChat Table 4 (P95 2.407–4.649 s, first audio chunk). Also surfaced Twilio. E-ACA-020, E-ACA-034. |
| Q-ACA2-02 | `Moshi speech-to-speech "theoretical latency" OR "160 ms" OR "200 ms" Kyutai arxiv pdf` | Opened Moshi arXiv HTML and PDF. Theoretical 160 ms; abstract “200 ms in practice.” No percentile. E-ACA-030. |
| Q-ACA2-03 | `LLaMA-Omni "latency" 226ms OR "response latency" speech arxiv pdf Freeze-Omni latency milliseconds` | Opened LLaMA-Omni PDF (226.13 ms at chunk 10, not a percentile) and Full-Duplex-Bench HTML (means 1.18–2.25 s). E-ACA-027, E-ACA-031. |
| Q-ACA2-04 | `Qwen2.5-Omni "first packet" OR "latency" milliseconds technical report pdf GLM-4-Voice latency` | Opened Qwen2.5-Omni PDF (no wall-clock ms), VocalNet-M2 DOI page (first-chunk means), GLM-4-Voice PDF (b = 0.8 s). E-ACA-028, E-ACA-029, E-ACA-036. |
| Q-ACA2-05 | `Freeze-Omni "latency" milliseconds OR "response delay" arxiv pdf 2411.00774 speech-to-speech` | Opened Freeze-Omni abs HTML, Table 4 p90 1,020 ms to first PCM. Opened FD-Bench PDF, medians on H20. E-ACA-032, E-ACA-033. |

## Framing 2 — buyer (production voice-agent milliseconds)

| Query ID | Query string | Outcome |
|---|---|---|
| Q-ACA2-06 | `voice agent "end-to-end latency" milliseconds p95 streaming ASR TTS production benchmark 2025 pdf` | Opened arXiv:2508.04721 (H100, mean TTFA 0.678 s, no percentile) and the PAVO OpenReview PDF (E2E P95 1,449–1,651 ms). E-ACA-021, E-ACA-022. Twilio already opened. |
| Q-ACA2-07 | `"p95" TTFAB OR "time to first audio" phone call voice agent ElevenLabs Retell benchmark milliseconds` | Opened https://openbenchmarks.com/voice-agent-latency . Phone-call TTFAB p95 1,768–2,259 ms. Not labeled VoLTE. E-ACA-035. |

## Framing 3 — skeptic (first chunk versus full turn; cellular / VoLTE)

| Query ID | Query string | Outcome |
|---|---|---|
| Q-ACA2-08 | `"time to first audio" OR "first packet" OR TTFA cascaded ASR LLM TTS "not" full speech-to-speech latency pdf` | Opened the Salesforce tutorial PDF (measured TTFA 755 ms, not a p95), Voice-Light PDF (median 758 ms, authors refuse a p95), and the on-device cascade PDF (p95 11.92 s). E-ACA-023, E-ACA-024, E-ACA-025, E-ACA-026. |
| Q-ACA2-09 | `VoLTE OR cellular "speech-to-speech" OR "voice agent" latency p95 milliseconds ASR LLM TTS pdf` | No paper with a VoLTE air-interface p95 of ASR + SLM + TTS. Hits were the H100 telecom-titled lab paper, the phone-call board, and vendor budgets. |
| Q-ACA2-10 | `"VoLTE" "speech-to-speech" OR "voice agent" OR "ASR" LLM TTS latency milliseconds p95 measurement pdf` | Opened Exotel 2026-09-02. VoLTE appears only inside an unsourced 40–150 ms one-way carrier range. E-ACA-037. Caller Digital and TestMu pages were opened and rejected (no sample, no hardware, no table). Cekura docs define percentiles and publish no pipeline number. |

## Pages opened and used

- https://arxiv.org/pdf/2509.06502
- https://arxiv.org/pdf/2508.04721
- https://openreview.net/notes/edits/attachment?id=lnMHH8rkJx&name=pdf
- https://arxiv.org/pdf/2609.20995v1.pdf
- https://arxiv.org/pdf/2603.05413
- https://arxiv.org/pdf/2610.07641
- https://arxiv.org/pdf/2409.06666
- https://doi.org/10.1109/icassp55912.2026.11461309
- https://arxiv.org/pdf/2412.02612
- https://arxiv.org/html/2410.00037v2
- https://arxiv.org/html/2507.23159v1
- https://arxiv.org/abs/2411.00774
- https://arxiv.org/pdf/2507.19040
- https://www.twilio.com/en-us/blog/developers/best-practices/guide-core-latency-ai-voice-agents
- https://openbenchmarks.com/voice-agent-latency
- https://raw.githubusercontent.com/QwenLM/Qwen2.5-Omni/main/assets/Qwen2.5_Omni.pdf
- https://exotel.com/blog/sip-voice-streaming/
- https://raw.githubusercontent.com/kyutai-labs/moshi/main/README.md

## Dead ends (do not repeat as if they produced a p95)

| Query or URL | Why it is a dead end |
|---|---|
| `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2410.00037` and the same API for 2509.06502, 2508.04721, and 2412.02612 | HTTP 429 on 2026-11-24. Citation counts for Moshi, FireRedChat, the H100 telecom paper, and GLM-4-Voice were not retrieved and were not filled in. |
| `https://api.openalex.org/works/https://doi.org/10.48550/arxiv.2409.06666` | HTTP 403. |
| `https://api.semanticscholar.org/graph/v1/paper/batch` | HTTP 404. |
| `https://github.com/kyutai-labs/moshi` | Page body was an empty stub (0 stars). The L4 sentence is from the raw README only. |
| `https://caller.digital/blog/openai-realtime-api-vs-voice-ai-platforms-india-2026` | Asserts 900 ms–1.4 s p50 and 2 s+ p95 on Indian PSTN legs, and mentions Jio VoLTE-to-2G handoffs, with no n, no hardware, and no table. Not a ledger row. |
| `https://www.testmuai.com/blog/voice-quality-testing/` | States a P50 of 1.4–1.7 s and a P95 target of 3–5 s with no dataset. Not a ledger row. |
| `https://docs.cekura.ai/documentation/key-concepts/metrics/pre-defined-metrics` | Method only. No measured pipeline percentile. |
| Deepgram, Ortavox, and Pazau URLs that appeared in search snippets | Not opened. Any p95 in those snippets is unused. |
| Q-ACA2-09 and Q-ACA2-10 | No measured p95 of streaming ASR + a small language model + streaming TTS on a VoLTE or cellular air interface. |
