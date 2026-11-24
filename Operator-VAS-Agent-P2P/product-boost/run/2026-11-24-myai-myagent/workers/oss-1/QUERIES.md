# Queries — oss-scout-1

**Run:** 2026-11-24-myai-myagent
**Question:** RQ-3 only. Open-weight streaming ASR, small language models, and streaming TTS or few-shot voice clone. Metric: cost per audio minute if a project or a reproducible benchmark states one; otherwise UNPUBLISHED. License name, with AGPL, SSPL, or other viral terms named explicitly.
**Retrieved:** 2026-11-24
**Not searched for this worker:** speaker verification and anti-spoof toolkits (oss-2, E-OSS-020+).

Three framings were used: the insider name of the component, the commercial incumbent plus an open-source alternative, and complaints or license traps. Pages below were opened on 2026-11-24. Search snippets alone are not ledger sources.

## Framing 1 — insider

| Query | Result used |
|---|---|
| `open weight streaming ASR github moonshine parakeet sherpa faster-whisper license 2026` | Named Moonshine, Parakeet, sherpa-onnx, faster-whisper. Led to license files opened in the fetch log. |
| `"cost per minute" OR "per audio minute" OR "$ per minute" self-hosted whisper OR moonshine OR parakeet ASR GPU benchmark` | InferenceBench states $0.00007 USD/min (ledgered). hireagentic.dev states estimated USD per audio hour, not a measured per-minute figure (not ledgered). Kernwerk states joules and seconds per sentence, not currency (not ledgered). |
| `open source streaming TTS few-shot voice clone github CosyVoice F5-TTS Kokoro Chatterbox license` | Named CosyVoice, F5-TTS, Qwen3-TTS, Chatterbox, VoXtream. Kokoro is not a clone and was not scored. |

## Framing 2 — buyer / incumbent

| Query | Result used |
|---|---|
| `open source alternative to Deepgram streaming ASR github self-hosted` | Named WhisperLiveKit, whisper.api, Coro, OASR as servers in front of Whisper, Parakeet, or Nemotron. Those servers were not scored. The models behind them were. |
| `open source alternative to ElevenLabs streaming voice clone TTS github` | Named Qwen3-TTS, Pocket TTS, Tontaube, a Chatterbox streaming fork. Qwen3-TTS was opened. Pocket TTS and Tontaube were not primary-read and are not scored. |
| `Phi-4-mini-instruct license MIT Llama-3.2-3B community license Qwen2.5-3B Apache gemma-3 license` | Pointed at the license files. The Qwen2.5 "Apache" description in a third-party dataset LICENSES.md is contradicted by the model LICENSE opened here (Qwen Research License). The third-party table was not used. |

## Framing 3 — complaints and license

| Query | Result used |
|---|---|
| `faster-whisper limitations problems production hallucination streaming` | Issue https://github.com/SYSTRAN/faster-whisper/issues/1179 (batched pipeline quality). Production notes at https://gods.dev/blog/faster-whisper-in-prod/ and https://www.spheron.network/blog/faster-whisper-gpu-cloud-production-deployment-guide/. Those blogs are not cost sources. |
| `CosyVoice OR Qwen3-TTS OR F5-TTS problems production license non-commercial complaints` | F5-TTS weights CC-BY-NC confirmed on the README. A 2026-06 Mac write-up describes a CosyVoice 3 Japanese-frontend bug: https://zenn.dev/mohhh_ok/articles/2026-06-cosyvoice-qwen3-tts-apache2-mac. A voice-agent hosting note describes Qwen3-TTS concurrency and says vLLM streaming serving was still maturing: https://softcery.com/lab/self-hosting-tts-for-voice-agents. Neither page states a project-published currency cost per minute. |
| `ChatTTS AGPL OR "SSPL" OR "AGPL-3.0" TTS OR "speech recognition" github license` | ChatTTS AGPL confirmed on the LICENSE file after the search. |
| `SSPL TTS OR ASR OR whisper OR "text-to-speech" license github -elasticsearch` | Hit niradler/vocal, SSPL-1.0. LICENSE and README opened. No other SSPL speech project was opened. |
| `Fish Speech license OR "Coqui Public Model License" XTTS OR OpenVoice MIT commercial restriction` | Led to the XTTS CPML file, which was opened. Fish Speech and OpenVoice license files were not opened, so those projects are not scored. |
| `"per minute" GPU cost TTS OR "voice clone" OR "small language model" open source inference dollars OR USD benchmark` | Stork.AI states about 1.4 and about 0.8 US cents per minute (ledgered). NexGPU derives a USD-per-audio-hour figure for CosyVoice from an L20 RTF and a different GPU price (not ledgered). gpuvault and a Ming 3.0 personal test were not used. |

## Pages opened (fetch log)

License, README, model card, benchmark, or commit feed. HTTP status is noted when it was not 200.

| URL | Why |
|---|---|
| https://raw.githubusercontent.com/moonshine-ai/moonshine/main/LICENSE | E-OSS-001 |
| https://raw.githubusercontent.com/moonshine-ai/moonshine/main/README.md | Cost absence and streaming description for Moonshine |
| https://raw.githubusercontent.com/SYSTRAN/faster-whisper/master/LICENSE | E-OSS-002 |
| https://raw.githubusercontent.com/SYSTRAN/faster-whisper/master/README.md | Cost absence; streaming left to other projects |
| https://github.com/SYSTRAN/faster-whisper/issues/1179 | Batched-pipeline complaint |
| https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3 | E-OSS-003 |
| https://raw.githubusercontent.com/k2-fsa/sherpa-onnx/master/LICENSE | E-OSS-004 |
| https://raw.githubusercontent.com/k2-fsa/sherpa-onnx/master/README.md | Streaming ASR; no currency per minute |
| https://huggingface.co/openai/whisper-large-v3-turbo/raw/main/README.md | E-OSS-005 |
| https://inferencebench.io/blog/whisper-large-v3-turbo-597x-realtime-asr-benchmark/ | E-OSS-006 |
| https://github.com/QwenLM/Qwen3-TTS/ | E-OSS-007 |
| https://raw.githubusercontent.com/QwenLM/Qwen3-TTS/main/LICENSE | Apache-2.0 text, copyright 2026 Alibaba Cloud |
| https://raw.githubusercontent.com/QwenAudio/CosyVoice/main/LICENSE | E-OSS-008 |
| https://raw.githubusercontent.com/QwenAudio/CosyVoice/main/README.md | Zero-shot clone, bi-streaming, no currency rate |
| https://huggingface.co/api/models/FunAudioLLM/Fun-CosyVoice3-0.5B-2512 | license apache-2.0, lastModified 2026-02-03, no price field |
| https://raw.githubusercontent.com/SWivid/F5-TTS/main/README.md | E-OSS-009 |
| https://huggingface.co/SWivid/F5-TTS/raw/main/README.md | license: cc-by-nc-4.0 |
| https://raw.githubusercontent.com/resemble-ai/chatterbox/master/README.md | E-OSS-010 |
| https://raw.githubusercontent.com/2noise/ChatTTS/main/README.md | E-OSS-011 |
| https://raw.githubusercontent.com/2noise/ChatTTS/main/LICENSE | AGPL-3.0 text |
| https://huggingface.co/coqui/XTTS-v2/raw/main/LICENSE.txt | E-OSS-012 |
| https://huggingface.co/coqui/XTTS-v2/raw/main/README.md | Card points at CPML; 6-second clone |
| https://raw.githubusercontent.com/niradler/vocal/master/README.md | E-OSS-013 |
| https://raw.githubusercontent.com/niradler/vocal/master/LICENSE | SSPL-1.0 section 8 |
| https://huggingface.co/microsoft/Phi-4-mini-instruct/raw/main/README.md | E-OSS-014 |
| https://huggingface.co/microsoft/Phi-4-mini-instruct/resolve/main/LICENSE | MIT text |
| https://huggingface.co/api/models/microsoft/Phi-4-mini-instruct | lastModified 2025-12-10, license mit |
| https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/raw/main/LICENSE | E-OSS-015 |
| https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/raw/main/README.md | license: other / qwen-research |
| https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/resolve/main/LICENSE | E-OSS-016 |
| https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/raw/main/README.md | license: apache-2.0 |
| https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/resolve/main/LICENSE.txt | E-OSS-017 |
| https://huggingface.co/google/gemma-3-4b-it/raw/main/README.md | HTTP 401. Card body not read. |
| https://gemma.ai/resources/terms/ | E-OSS-018 |
| https://huggingface.co/api/models/google/gemma-3-4b-it | license gemma, lastModified 2025-03-21 |
| https://www.stork.ai/blog/voxcpm2-vs-zonos3-mini-open-tts-benchmark | E-OSS-019 |
| https://huggingface.co/api/models/openbmb/VoxCPM2 | license apache-2.0, lastModified 2026-11-09. License file text not opened. |
| https://huggingface.co/api/models/Qwen/Qwen3-TTS-12Hz-0.6B-Base | license apache-2.0, lastModified 2026-01-29, no price field |
| https://github.com/2noise/ChatTTS/commits/main.atom | Last feed update 2026-04-10 |
| https://github.com/niradler/vocal/commits/master.atom | Last feed update 2026-11-21; author niradler on the entries read |
| https://github.com/coqui-ai/TTS/commits/dev.atom | Last feed update 2024-02-10 |
| https://gods.dev/blog/faster-whisper-in-prod/ | Production complaints. No currency per minute used. |
| https://www.spheron.network/blog/faster-whisper-gpu-cloud-production-deployment-guide/ | Chunking recipe. No project-published ₹/min. |
| https://zenn.dev/mohhh_ok/articles/2026-06-cosyvoice-qwen3-tts-apache2-mac | CosyVoice 3 frontend complaint |
| https://softcery.com/lab/self-hosting-tts-for-voice-agents | Qwen3-TTS concurrency note. Not used as a cost. |

GitHub API `https://api.github.com/repos/{owner}/{repo}` was opened on 2026-11-24 for moonshine-ai/moonshine, SYSTRAN/faster-whisper, k2-fsa/sherpa-onnx, QwenLM/Qwen3-TTS, QwenAudio/CosyVoice, SWivid/F5-TTS, and resemble-ai/chatterbox before the IP was rate-limited. Later calls to 2noise/ChatTTS, niradler/vocal, and coqui-ai/TTS returned 403. Commit dates for those three came from the atom feeds above.

## Dead ends (do not repeat these as if they were measurements)

| Query or page | Why it is not a per-minute cost |
|---|---|
| https://hireagentic.dev/tools/self-hosted-speech-to-text-cost-calculator | Publishes estimated USD per audio hour. Non-A100 RTFx is marked as a bandwidth estimate. This worker did not divide by 60. |
| https://www.assemblyai.com/blog/open-source-speech-to-text-cost | Competitor marketing page. Not used as a model cost. |
| https://nexgpu.net/en/models/cosyvoice/ | Derives about $0.030 per audio-hour by applying an L20 RTF to a different GPU's rental price. Not a per-minute figure and not the project's own price. |
| https://gpuvault.io/model/kokoro-82m/ | Host marketing page. Kokoro is not a voice-clone model. Not scored. |
| https://softreviewed.com/ming-3-tts-free-voice-cloning/ | One person's Modal arithmetic, including cold start. Not used. |
| https://kernwerk.org/blog/speech-to-text-edge-jetson/ | Joules and seconds per sentence. No currency per minute. |
| `SSPL` search | Only Vocal's SSPL-1.0 file was opened. No second SSPL ASR or TTS license file was found and opened. |
| Fish Speech, OpenVoice, Pocket TTS, Tontaube, Kyutai STT, Vosk, FunASR, Piper | Named in search. License files not opened. Not scored. |
| nvidia/parakeet_realtime_eou_120m-v1 and nemotron streaming checkpoints | A third-party license table named NVIDIA Open Model License and OpenMDW 1.1. Those model cards were not opened. E-OSS-003 does not cover them. |
| Gemma 4 license link on https://gemma.ai/resources/terms/ | Not opened. E-OSS-018 is Gemma 3 only. |
| ZONOS3-Mini upstream license file | Not opened. E-OSS-019 quotes the benchmark's license sentence only. |
| GitHub API burst after the first seven repositories | `You have triggered an abuse detection mechanism` and then `API rate limit exceeded`. Retries of that burst will fail until the limit resets. Use raw README, LICENSE, and `commits/*.atom` instead. |
