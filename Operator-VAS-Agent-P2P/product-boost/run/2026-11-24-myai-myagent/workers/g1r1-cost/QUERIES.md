# Queries — g1r1-cost

Retrieved 2026-11-24. Web search only. InferenceBench and Stork.AI were treated as exhausted and were not opened as sources. A search that returned the InferenceBench URL is marked below. That page was not used.

## Insider term

1. `streaming ASR LLM TTS "per minute" GPU cost benchmark WebRTC OR SIP -InferenceBench -stork.ai`
   Hit blogs that assemble vendor rates (devManue, Trembit, Softcery, Sonex Labs). No filing and no single hardware run of all four components. Sonex Labs prices STT, TTS, and an LLM on separate lines. Dead end for a four-component hardware total.

2. `"cost per minute" "voice cloning" OR TTS "speech recognition" LLM OR SLM benchmark hardware dollars OR USD OR cents filetype:pdf`
   No PDF of a four-component hardware benchmark. Hits were calculators and TTS list-price roundups. Dead end.

3. `arxiv speech-to-speech inference cost per minute GPU H100 streaming ASR LLM TTS benchmark`
   Returned the exhausted InferenceBench URL in the result list. Not used. Also returned Spheron (GPU session rates for Moshi, transport discussed as milliseconds), ClusterBid (incomplete stage table), arXiv:2606.30944, and arXiv:2607.02119. Papers opened. They report timing, not a currency total.

4. `NVIDIA Riva "concurrent streams" ASR TTS performance benchmark H100 PDF 2025 OR 2026 -inferencebench`
   Opened https://huggingface.co/blog/nvidia/nemotron-speech-asr-scaling-voice-agents (5 January 2026). Throughput and latency only. NVIDIA Speech NIM release notes and a secondary Riva summary showed streams, not a four-component currency total.

5. `Kyutai Moshi technical report GPU realtime factor cost per minute WebRTC site:arxiv.org`
   Opened https://arxiv.org/html/2410.00037, https://arxiv.org/html/2611.01835, and the MoshiVis / DiffuPlex / MoshiRAG pages in the result set. Latency, CUDA time, or FLOPs. No currency per minute and no SIP or WebRTC price.

6. `Nemotron Voice Agent Blueprint 3x H100 Parakeet Magpie "per minute" OR cost OR price site:docs.nvidia.com OR site:github.com OR site:build.nvidia.com`
   No blueprint page stating a currency per minute for ASR + LLM + TTS + SIP or WebRTC. Side hits were GPU hourly price lists and a scraped vendor-price repo. Dead end for the required total.

## Buyer term

7. `site:sec.gov "per minute" speech-to-text text-to-speech cost of revenue voice AI 10-K`
   Opened OneMeta Inc. Form 10-K for the year ended 31 December 2025: https://www.sec.gov/Archives/edgar/data/1388295/000149315226016782/form10-k.htm
   Wholesale interpretation price only. Older Nuance, Avaya, and SoundBite filings do not state this pipeline. Dead end for the four components.

8. `SoundHound 10-K 2025 "per minute" OR "per query" voice AI cost of revenue site:sec.gov`
   Opened SoundHound AI, Inc. Form 10-K for the year ended 31 December 2025: https://www.sec.gov/Archives/edgar/data/1840856/000184085626000006/soun-20251231.htm
   Aggregate cost of revenues. No minute denominator. Also opened the 2025 quarterly filings and the statement of operations. Dead end for a per-minute split.

9. `"schedule of prices" OR "price schedule" OR "rate schedule" "per minute" "text-to-speech" "speech-to-text" SIP filetype:pdf`
   No contract PDF. Results were Talkif, LiveKit, Syllable, and Telnyx rate pages.

10. `"price schedule" OR "invoice" OR "rate schedule" "per minute" "speech-to-text" "text-to-speech" SIP OR WebRTC contract OR GSA`
    Same class of result: vendor rate cards. LiveKit's pricing page was opened: https://livekit.com/pricing.md
    It lists components separately and states no GPU. Not used as a pipeline total.

## Skeptic term

11. Pages already in hand were checked for a hidden total: OneMeta 10-K for a numeric OEM per-minute rate (the rate is described, the number is not stated); SoundHound 10-K for "per minute", "per query", GPU, WebRTC, and speech-to-text (usage and per-query revenue language, no minute cost); Moshi for a dollar figure or SIP/WebRTC (none); arXiv:2606.30944 and arXiv:2607.02119 for a currency amount (none).

## Not repeated

InferenceBench `whisper-large-v3-turbo-597x-realtime-asr-benchmark` and Stork.AI `voxcpm2-vs-zonos3-mini-open-tts-benchmark` were not queried as sources and were not added to any other figure.
