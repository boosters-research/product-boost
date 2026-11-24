# Cost scout g1r1-cost — full-pipeline per-minute figure

Retry 1 of 2. The job was to open a filing, an invoice schedule, or a named-method benchmark, other than InferenceBench and Stork.AI, that states one per-minute figure for streaming ASR, an SLM or LLM, voice-clone or TTS, and SIP or WebRTC transport, in the source currency, with the arithmetic and the hardware.

## Ledger entries written

E-OSS-055

E-OSS-056 through E-OSS-064 were not used. The unpublished result is one finding.

## Result

That complete figure is unpublished in the sources opened on 2026-11-24. No total is printed here. A figure that omits a component is not a measurement of the ceiling. K1 is not marked. C-00 stays open. Nothing was converted to rupees or to pence.

## Components each opened source actually priced

| Source | Class | What it priced or measured | Absent from that source |
|---|---|---|---|
| OneMeta Inc. Form 10-K, year ended 31 December 2025. https://www.sec.gov/Archives/edgar/data/1388295/000149315226016782/form10-k.htm | Filing | Wholesale customer price of USD 0.30 to USD 0.36 per minute for the Verbum real-time interpretation product. Cost of revenue USD 208,590 and revenue USD 1,505,866 for 2025. An October 2024 NICE OEM credit of USD 700,000 is recognized in part on a per-minute rate; the filing text does not state that rate. | No itemized streaming ASR, SLM or LLM, voice-clone or TTS, or SIP or WebRTC compute price. No GPU. The wholesale range is a customer price for an interpretation product, not a four-component pipeline cost. Minutes sold are not stated, so cost of revenue was not divided into a per-minute cost. |
| SoundHound AI, Inc. Form 10-K, year ended 31 December 2025, auditor's report dated 2 March 2026. https://www.sec.gov/Archives/edgar/data/1840856/000184085626000006/soun-20251231.htm | Filing | Cost of revenues of USD 97,369 thousand for 2025, in statements presented in thousands of USD. The narrative describes hosting, data-center electricity, content fees, related personnel, and amortization of acquired developed technology. Revenue of USD 168,920 thousand. | No audio-minute count, so no per-minute quotient. No split across streaming ASR, an SLM or LLM, voice-clone or TTS, and SIP or WebRTC. No GPU model in a per-minute arithmetic. |
| NVIDIA, "Scaling Real-Time Voice Agents with Cache-Aware Streaming ASR", 5 January 2026. https://huggingface.co/blog/nvidia/nemotron-speech-asr-scaling-voice-agents | Vendor benchmark with a named setup | Streaming ASR: Nemotron Speech ASR, 560 concurrent streams on one H100 at a 320 ms chunk. A Modal load used 127 WebSocket clients, 560 ms mode, one H100, a 3-minute stream, median delay 182 ms. A Daily pipeline names that ASR, Nemotron 3 Nano 30B, and Magpie TTS (7 languages, 5 voices) and states voice-to-voice latency under 900 ms on Modal, DGX Spark, and RTX 5090. | No currency amount. No SIP price. No WebRTC price. The WebSocket figure is a client count, not a transport tariff. Magpie is not described there as a measured voice-clone cost. |
| Moshi, arXiv:2410.00037. https://arxiv.org/html/2410.00037 | Named-method technical report | A speech-to-speech model that replaces a cascaded ASR, text dialogue, and TTS pipeline. Theoretical latency 160 ms. Practical latency 200 ms. Training on H100 GPUs. | No currency amount. No rental rate. No SIP or WebRTC price. Latency is not a per-minute cost. |
| arXiv:2606.30944. https://arxiv.org/html/2606.30944 | Named-method preprint | Real-time factor and throughput for speech-to-speech systems on 1 NVIDIA H100, including Qwen2.5-Omni-7B. | No currency amount. No SIP or WebRTC price. |
| arXiv:2607.02119. https://arxiv.org/html/2607.02119v1 | Named-method preprint | Decode tokens per second and model-FLOPs utilization on one H100 80GB for Bagpiper, OpusLM, and OpusLM-Dialogue. | No currency amount per audio minute. No SIP or WebRTC price. |
| arXiv:2611.01835. https://arxiv.org/html/2611.01835 | Named-method preprint | Percent of CUDA execution time saved for Moshi-family models on NVIDIA A100-40GB GPUs. "GPU cost" in that paper is elapsed CUDA time. | No currency amount. No SIP or WebRTC price. |
| LiveKit pricing page. https://livekit.com/pricing.md | Vendor rate card | Separate list prices for speech-to-text, LLM tokens, text-to-speech characters, third-party SIP minutes, WebRTC participant minutes, and US local telephony. The page also shows calculator assumptions. | No GPU. This page is not a filing, an invoice schedule, or a named-method hardware benchmark. Its phone example uses a US local telephony line. That line is not the page's third-party SIP line and not its WebRTC line. The example sum is not copied into the ledger. |

## Pages seen and not used as the figure

Search results also returned vendor price pages and cost blogs, including Telnyx, SignalWire, Talkif, Syllable, Sonex Labs, Softcery, and Spheron. Those pages are not a filing, an invoice schedule, or a named-method benchmark of one measured run on stated hardware. Where a blog printed a stack sum, a component was missing from that sum, or the transport line was a separate carrier rate. Those sums are not repeated here.

InferenceBench and Stork.AI were not opened as sources. Their per-minute figures were not added to anything.

No public contract exhibit retrieved by the invoice-schedule queries itemized all four components with hardware arithmetic. The hits were vendor rate cards.

## What this does not decide

K1 stays untested. C-00 stays open. The OneMeta wholesale range is USD. It is not a reading of the ceiling, and it was not converted.
