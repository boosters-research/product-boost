# OSS Scout 1 — RQ-3 cost per audio minute and license

**Run:** 2026-11-24-myai-myagent
**Worker:** oss-scout-1
**Question:** Which open-weight streaming ASR, small language model, and streaming TTS or few-shot voice-clone projects publish a reproducible compute cost per audio minute, and what license does each use?
**Retrieved:** 2026-11-24
**Ledger:** E-OSS-001 through E-OSS-019 in `LEDGER-ROWS.md`. Speaker verification and anti-spoof stay with oss-2.

## Answer

Two opened write-ups state a currency cost per audio minute. Both are in US dollars. Neither is the project's own price list, neither covers the full audio pipeline, and neither states rupees or pence.

| Published per-minute figure | What it measures | Ledger |
|---|---|---|
| $0.00007 USD per minute of audio | openai/whisper-large-v3-turbo, one H100 SXM, Hugging Face Transformers, 120-second clips at 597× realtime, Lambda spot price stated as $2.49 per GPU-hour. The method table says the clips are synthetic sine waves. The narrative says recorded speech. The page says Whisper is a batch model. | E-OSS-006 |
| about 1.4 US cents per minute of speech for VoxCPM2, and about 0.8 US cents per minute for ZONOS3-Mini | NVIDIA A10 at a stated $1.10 per hour, model already loaded, 20–21 November 2026. The page says those figures ignore start-up and idle time. | E-OSS-019 |

Every other project page opened for this question leaves the compute cost per audio minute **UNPUBLISHED**. No ₹/min figure was invented. No USD figure was converted.

The working ceiling is ₹0.30 per minute. The brief also says 30 pence. Contradiction C-00 stays OPEN. K1 stays UNTESTED. A K1 measurement would be a sum of streaming ASR + SLM/LLM + TTS/clone + SIP/WebRTC, strictly under the ceiling, in one unit. These rows omit media transport, omit a full sum, and are not in either of the two ceiling units.

No stack is recommended.

## Ledger entries written

E-OSS-001 … E-OSS-019

## Candidate register

Stars are a descriptive count from the GitHub API or the repository HTML on 2026-11-24. They are not the verdict.

Viability = mean of the six scores. Scores are integers. A dimension that the rubric states only at 5, 3, and 1 is interpolated where the evidence sits between those anchors, and the reason is in the evidence table. **viability < 2.5: do not recommend as a core dependency.** License score 1 is a commercial flag, not by itself the viability decision.

| Project | Capability covered | Stars | Bus | Recency | License | Sec | Fork | Release | Viability | Cost per audio minute | Ledger ID |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Moonshine streaming STT | Streaming ASR. English and the streaming checkpoints are MIT. | 11592 | 3 | 5 | 5 | 3 | 3 | 4 | 3.83 | UNPUBLISHED | E-OSS-001 |
| faster-whisper | Whisper runtime. MIT. Streaming is left to other projects. | 26971 | 4 | 5 | 5 | 3 | 3 | 3 | 3.83 | UNPUBLISHED | E-OSS-002 |
| parakeet-tdt-0.6b-v3 | Multilingual ASR weights, CC-BY-4.0. Card documents chunked streaming. | — | 3 | 1 | 4 | 3 | 3 | 3 | 2.83 | UNPUBLISHED | E-OSS-003 |
| sherpa-onnx | Streaming and non-streaming ASR runtime. Code Apache-2.0. | 16189 | 1 | 5 | 5 | 3 | 3 | 4 | 3.50 | UNPUBLISHED | E-OSS-004 |
| whisper-large-v3-turbo | Batch ASR weights. MIT. | — | 3 | 1 | 5 | 3 | 3 | 3 | 3.00 | UNPUBLISHED on the card. A third party states $0.00007 USD/min for a batch run. | E-OSS-005, E-OSS-006 |
| Qwen3-TTS | Streaming TTS and 3-second clone, as the README describes it. Apache-2.0. | 14618 | 3 | 2 | 5 | 3 | 3 | 1 | 2.83 | UNPUBLISHED | E-OSS-007 |
| CosyVoice | Zero-shot multilingual clone. README describes bi-streaming. Apache-2.0. | 24491 | 4 | 2 | 5 | 3 | 3 | 1 | 3.00 | UNPUBLISHED | E-OSS-008 |
| F5-TTS | Few-shot TTS. Code MIT. Weights CC-BY-NC. | 15646 | 4 | 5 | 1 | 3 | 3 | 4 | 3.33 | UNPUBLISHED | E-OSS-009 |
| Chatterbox | Few-shot TTS. MIT. README says retired August 2026. | 28066 | 1 | 1 | 5 | 3 | 3 | 2 | 2.50 | UNPUBLISHED | E-OSS-010 |
| ChatTTS | Dialogue TTS. README marks streaming generation done. Code AGPL-3.0. Weights CC BY-NC 4.0. | 40035 | 3 | 2 | 1 | 3 | 3 | 2 | 2.33 | UNPUBLISHED | E-OSS-011 |
| XTTS-v2 | Few-shot clone from a short clip. Coqui Public Model License 1.0.0. | 46272 (coqui-ai/TTS) | 1 | 1 | 1 | 3 | 3 | 1 | 1.67 | UNPUBLISHED | E-OSS-012 |
| Vocal | Self-hosted STT/TTS server, not a model. SSPL-1.0. | 2 | 1 | 5 | 1 | 3 | 3 | 4 | 2.83 | UNPUBLISHED | E-OSS-013 |
| Phi-4-mini-instruct | Text SLM, about 3.8B. MIT. | — | 3 | 2 | 5 | 3 | 3 | 3 | 3.17 | UNPUBLISHED | E-OSS-014 |
| Qwen2.5-3B-Instruct | Text SLM. Qwen Research License, non-commercial. | — | 3 | 1 | 1 | 3 | 3 | 3 | 2.33 | UNPUBLISHED | E-OSS-015 |
| Qwen3-4B-Instruct-2507 | Text SLM. Apache-2.0. | — | 3 | 1 | 5 | 3 | 3 | 3 | 3.00 | UNPUBLISHED | E-OSS-016 |
| Llama-3.2-3B-Instruct | Text SLM. Llama 3.2 Community License. | — | 3 | 1 | 1 | 3 | 3 | 3 | 2.33 | UNPUBLISHED | E-OSS-017 |
| gemma-3-4b-it | Text and image-text SLM. Gemma terms. | — | 3 | 1 | 1 | 3 | 3 | 3 | 2.33 | UNPUBLISHED | E-OSS-018 |
| VoxCPM2 and ZONOS3-Mini | TTS / clone benchmarks only. Six-dimension score withheld. | — | — | — | — | — | — | — | not scored | about 1.4 and about 0.8 US cents, model already loaded | E-OSS-019 |

Arithmetic, viability = sum / 6:

| Project | Sum | Mean |
|---|---|---|
| Moonshine streaming | 3+5+5+3+3+4 = 23 | 3.83 |
| faster-whisper | 4+5+5+3+3+3 = 23 | 3.83 |
| parakeet-tdt-0.6b-v3 | 3+1+4+3+3+3 = 17 | 2.83 |
| sherpa-onnx | 1+5+5+3+3+4 = 21 | 3.50 |
| whisper-large-v3-turbo | 3+1+5+3+3+3 = 18 | 3.00 |
| Qwen3-TTS | 3+2+5+3+3+1 = 17 | 2.83 |
| CosyVoice | 4+2+5+3+3+1 = 18 | 3.00 |
| F5-TTS | 4+5+1+3+3+4 = 20 | 3.33 |
| Chatterbox | 1+1+5+3+3+2 = 15 | 2.50 |
| ChatTTS | 3+2+1+3+3+2 = 14 | 2.33 |
| XTTS-v2 | 1+1+1+3+3+1 = 10 | 1.67 |
| Vocal | 1+5+1+3+3+4 = 17 | 2.83 |
| Phi-4-mini-instruct | 3+2+5+3+3+3 = 19 | 3.17 |
| Qwen2.5-3B-Instruct | 3+1+1+3+3+3 = 14 | 2.33 |
| Qwen3-4B-Instruct-2507 | 3+1+5+3+3+3 = 18 | 3.00 |
| Llama-3.2-3B-Instruct | 3+1+1+3+3+3 = 14 | 2.33 |
| gemma-3-4b-it | 3+1+1+3+3+3 = 14 | 2.33 |

## How the six scores were assigned

**Bus.** 5 would require at least five active committers across two organizations. That bar was not shown for any row. sherpa-onnx's top account has 1696 contributions on the API page and the next has 18, so the score is 1. Vocal's commit feed entries that were read are by niradler, so the score is 1. Chatterbox and XTTS score 1 because the upstream maintainers have stopped: Chatterbox's README says Resemble AI no longer maintains it, and coqui-ai/TTS `dev` last updated 2024-02-10. Moonshine, ChatTTS, Qwen3-TTS, and the lab checkpoints score 3: more than one person or a publishing lab is visible, and five committers across two organizations were not counted. faster-whisper, CosyVoice, and F5-TTS score 4 because several people have double-digit contribution counts and at least one name sits outside the dominant account. Parakeet, Whisper, Phi, Qwen, Llama, and Gemma score 3 because the publisher is NVIDIA, OpenAI, Microsoft, Alibaba, Meta, or Google, and this worker did not enumerate committers on those checkpoints.

**Recency.** Anchor 5 is a commit in the last 30 days and a steady year. Anchor 3 is activity in the last 90 days. Anchor 1 is a last commit older than 12 months, or an archived project.

| Project | Date used | Score |
|---|---|---|
| Moonshine | Commit 2026-11-06; release v0.1.6 on 2026-11-06 | 5 |
| faster-whisper | Commit 2026-11-12; default branch pushed 2026-11-23 | 5 |
| parakeet-tdt-0.6b-v3 | Card line "Huggingface 08/14/2025" | 1 |
| sherpa-onnx | Commit 2026-11-24; release v2.0.3 on 2026-11-22 | 5 |
| whisper-large-v3-turbo | Model lastModified 2024-10-04 | 1 |
| Qwen3-TTS | Code commit 2026-03-17; base-model card lastModified 2026-01-29 | 2 |
| CosyVoice | Code commit 2026-05-25; Fun-CosyVoice3 card lastModified 2026-02-03 | 2 |
| F5-TTS | Commit 2026-11-03 | 5 |
| Chatterbox | README retirement commit 2026-11-04; the text says maintenance has stopped | 1 |
| ChatTTS | Commit feed updated 2026-04-10 | 2 |
| XTTS-v2 / coqui-ai/TTS | `dev` feed updated 2024-02-10 | 1 |
| Vocal | Commit feed updated 2026-11-21, with earlier entries through 2026-04-08 | 5 |
| Phi-4-mini-instruct | lastModified 2025-12-10 | 2 |
| Qwen2.5-3B-Instruct | lastModified 2024-09-25 | 1 |
| Qwen3-4B-Instruct-2507 | lastModified 2025-09-17 | 1 |
| Llama-3.2-3B-Instruct | lastModified 2024-10-24 | 1 |
| gemma-3-4b-it | lastModified 2025-03-21 | 1 |

**License.** MIT or Apache-2.0 scores 5. CC-BY-4.0 scores 4: commercial use with attribution, and it is not in the MIT/Apache/BSD cell of the rubric. AGPL, SSPL, and custom or non-commercial terms score 1. The score of 1 is a flag. It is not, by itself, a viability rejection.

**Security.** GitHub's public security-advisory list was empty, and `SECURITY.md` returned HTTP 404, for Moonshine, faster-whisper, sherpa-onnx, Qwen3-TTS, CosyVoice, F5-TTS, and Chatterbox. No open critical advisory was in those responses, and no security policy file was found, so the score is 3 and not 5. Vocal, ChatTTS, Coqui, and the Hugging Face checkpoints did not get a SECURITY.md check after the API limit. Their security score is also 3, with that gap stated here. This pass did not read a CVE database.

**Fork.** No opened page showed a fork with more current activity than upstream. The score is 3. A streaming fork of Chatterbox was named in search and its commit history was not compared, so Chatterbox stays at 3 on this dimension. The retirement is already in the recency and bus scores.

**Release.** Moonshine v0.1.6 and sherpa-onnx v2.0.3 are recent tagged releases, without an LTS statement read here, so they score 4. F5-TTS tag 1.1.22 was published 2026-07-23, score 4. faster-whisper's latest tag in the API response is v1.2.1 on 2025-10-31 while main moved in November 2026, score 3. Vocal's 2026-11-21 commit message says "Release v0.4.1", score 4. Qwen3-TTS and CosyVoice returned no GitHub release in the API response, score 1. Chatterbox's latest tag in the API response is v0.1.2 on 2025-06-13, score 2. ChatTTS had no release object retrieved, score 2. XTTS's code line has had no commit on `dev` since 2024-02-10, score 1. Named model checkpoints score 3.

**Issue lists.** The open-issue thread read in full is faster-whisper #1179. Other projects contributed an open-issue count from the API, not a reading of each thread. The skill says not to recommend a project whose issues, README, and last three months of commits were not read. This memo recommends no project.

## Coverage map — what each candidate does and does not do

Phase-1 functional requirements are in `deliverables/00-PRODUCT-SCOPE.md`. This worker does not cover Audio Signature (oss-2, RQ-1).

| FR from scope doc | Covered by | Coverage | Gap requiring custom work |
|---|---|---|---|
| FR-1.1 account inquiry, FR-1.2 fund transfer, FR-1.3 beneficiary registration, FR-1.4 disputes | Any ASR row plus any SLM row plus any TTS row would be a component pile, not a measured pipeline. | No opened project states a cost for streaming ASR + SLM + TTS + SIP/WebRTC together. | The sum K1 needs is unpublished. Speech-to-speech p95 is RQ-2, not this file. |
| FR-2.1–FR-2.3 Audio Signature | Out of scope for oss-1. | None claimed. | oss-2. |
| FR-3.4 zero-retention LLM gateway | None of these model repos is a gateway. | None. | A separate gateway. The model license still applies to whatever the gateway runs. |
| FR-4.3 voice clone for delegated speech | Qwen3-TTS, CosyVoice, F5-TTS, Chatterbox, XTTS-v2, and the Stork pair describe cloning from a short clip. ChatTTS describes streaming dialogue synthesis and a non-commercial model. | Component capability only. Phase 2 in the scope doc. | Consent, K6, and the rule that a clone is never an Audio Signature. No per-minute cost for that path was published by those projects. |

## What each row is, in deployment terms

| Project | Language / runtime | Footprint the opened page actually states | Data store | Extension model | Escape hatch |
|---|---|---|---|---|---|
| Moonshine | Python, JavaScript/WASM, and mobile/desktop bindings named in the README | README says on-device. No currency. No VRAM number used here. | None required by the README | One library, several language bindings | Weights and code can be forked. Streaming checkpoints are MIT. The legacy list in the LICENSE is not. TTS files in the repo are outside the MIT default. |
| faster-whisper | Python, CTranslate2 | README shows CPU int8 and GPU float16 / int8_float16. No currency. | None | Callers wrap it. The README points at speaches and Whisper-Streaming for streaming. | MIT code. Whisper weights are separately MIT (E-OSS-005). |
| parakeet-tdt-0.6b-v3 | NeMo / PyTorch | Card says 24 minutes of audio with full attention on an A100 80GB. No currency. | None | NeMo checkpoint. Card also links NVIDIA NIM for a different v2 model. | Weights are downloadable under CC-BY-4.0. NIM and Riva are separate NVIDIA product paths. |
| sherpa-onnx | C++, with Python, Java, Kotlin, Swift, C, Go, and WASM examples in the README | README includes phone and WASM examples. No currency per minute. | None | Pretrained ONNX bundles. Each bundle keeps its own model license. | Runtime code is Apache-2.0 and can be forked. A fork does not relicense the chosen checkpoint. Bus factor of the runtime is 1. |
| whisper-large-v3-turbo | Hugging Face Transformers in the InferenceBench write-up | That write-up says about 2 GB of model VRAM on an H100. | None | Checkpoint | MIT weights can be forked. The $0.00007 figure is one batch run, not a streaming service price. |
| Qwen3-TTS | Python. README says vLLM-Omni day-0 support was offline-only when that README was fetched. | No VRAM and no currency in the opened README. | None | Base, CustomVoice, and VoiceDesign checkpoints | Apache-2.0 code and the opened license file. Last code commit on the API snapshot is 2026-03-17. |
| CosyVoice | Python | README states no currency. A third-party page derived a per-hour price and was not used. | None | Fun-CosyVoice 3.0 checkpoint, Apache-2.0 in the Hugging Face metadata | Code can be forked. Open-issue count on the API snapshot was 623. |
| F5-TTS | Python | README states no currency. | None | MIT code. Weights CC-BY-NC-4.0 on the model card. | A commercial deployment cannot rely on the published pretrained weights. Training a new model is the escape hatch the README's license section leaves open, and this worker did not price that training. |
| Chatterbox | Python | README states no currency. | None | MIT code, frozen as an archive | The README says there is no support and no paid tier. Forking is legally available under MIT and is not a maintained upstream. |
| ChatTTS | Python | README states no currency. | None | AGPL-3.0 code. CC BY-NC 4.0 weights. | A network service that modifies the code inherits AGPL source obligations. The released weights are non-commercial. |
| XTTS-v2 | Coqui TTS (Python) | License file states no currency. | None | CPML weights | Non-commercial terms cover the model and its outputs. coqui-ai/TTS `dev` last updated 2024-02-10. |
| Vocal | Python server | README states no currency. | Local model cache described in the README | Optional backends, including models this worker scored separately | SSPL-1.0 section 8 requires the service source of the whole stack if Vocal is offered as a service. Self-hosting the unmodified program is described by the license as allowed. Bus factor is 1. |
| Phi-4-mini-instruct | Transformers text generation | Card states no audio-minute cost. | None | Weights | MIT weights can be forked. They do not consume audio minutes by themselves. |
| Qwen2.5-3B-Instruct | Transformers text generation | License states no audio-minute cost. | None | Weights | Research license. Commercial use requires a request to Alibaba Cloud. This is not the Apache-2.0 Qwen3-4B file. |
| Qwen3-4B-Instruct-2507 | Transformers text generation | License states no audio-minute cost. | None | Weights | Apache-2.0 weights can be forked. Card lastModified 2025-09-17. |
| Llama-3.2-3B-Instruct | Transformers text generation | License states no audio-minute cost. | None | Weights | Community license. The 700-million-MAU clause is in section 2. The gated model card returned HTTP 401. |
| gemma-3-4b-it | Transformers image-text-to-text | Terms page states no audio-minute cost. Card README returned HTTP 401. | None | Weights | Gemma terms, including the prohibited-use policy, pass to derivatives. Gemma 4's separate license page was not opened. |

## License red flags

License score 1. Viral terms are named in the first rows. The later rows are custom or non-commercial and are not AGPL or SSPL.

| Project | License | Commercial constraint | Escalate at gate |
|---|---|---|---|
| ChatTTS code | AGPL-3.0 (README says AGPLv3+). Text: https://raw.githubusercontent.com/2noise/ChatTTS/main/LICENSE | Network copyleft. A modified program offered as a service must provide source under AGPL. | G2. Flag, not a silent accept. |
| ChatTTS weights | CC BY-NC 4.0, stated in the README: https://raw.githubusercontent.com/2noise/ChatTTS/main/README.md | Non-commercial. The README says educational and research use. | G2. |
| Vocal | SSPL-1.0. https://raw.githubusercontent.com/niradler/vocal/master/LICENSE and https://raw.githubusercontent.com/niradler/vocal/master/README.md | Section 8 and the README: offering the program as a managed service requires releasing the service source of the full stack under SSPL. | G2. This is the service-side viral term. |
| F5-TTS weights | CC-BY-NC, and the model card says cc-by-nc-4.0. https://raw.githubusercontent.com/SWivid/F5-TTS/main/README.md and https://huggingface.co/SWivid/F5-TTS/raw/main/README.md | Pretrained weights are non-commercial. The code license is MIT. The README badge and the weight license are different. | G2. |
| XTTS-v2 | Coqui Public Model License 1.0.0. https://huggingface.co/coqui/XTTS-v2/raw/main/LICENSE.txt | Non-commercial use of the model and its outputs. Payment arising from the model or its output is outside the grant. | G2. |
| Moonshine legacy list only | Moonshine Community License, inside https://raw.githubusercontent.com/moonshine-ai/moonshine/main/LICENSE | Free commercial grant ends above USD $1,000,000 annual revenue. The list is Arabic, Japanese, Korean, Mandarin, Spanish, Ukrainian, and Vietnamese legacy non-streaming sizes named in that file. Streaming models are MIT and are not in this row. | G2 if a build picks a model on that list. |
| Qwen2.5-3B-Instruct | Qwen Research License Agreement, 19 September 2024. https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/raw/main/LICENSE | Non-commercial purposes only. Commercial use requires a license request. This file is not Apache-2.0. | G2. |
| Llama-3.2-3B-Instruct | Llama 3.2 Community License. https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/resolve/main/LICENSE.txt | Section 2: above 700 million monthly active users on the 25 September 2024 release date, rights wait on a Meta grant. Acceptable-use policy is incorporated. | G2. |
| gemma-3-4b-it | Gemma terms, last modified 1 April 2026. https://gemma.ai/resources/terms/ | Prohibited-use policy is incorporated and passes to derivatives. | G2. |

No opened ASR or TTS **model** license was SSPL. The only SSPL file opened is Vocal, which is a server. The only AGPL file opened is ChatTTS.

## Complaints that the first search pass does not show

| Project | What the complaint page says | URL |
|---|---|---|
| faster-whisper | Batched inference dropped or mistranslated segments on some files. Maintainers describe a domain-dependent tradeoff. | https://github.com/SYSTRAN/faster-whisper/issues/1179 |
| faster-whisper | One process should own the GPU model. Extra Uvicorn workers load extra copies. VAD defaults can clip onsets. Word timestamps add a second pass. | https://gods.dev/blog/faster-whisper-in-prod/ |
| faster-whisper | Whisper consumes fixed windows. A streaming setup is overlapping chunks, with `condition_on_previous_text=False`. | https://www.spheron.network/blog/faster-whisper-gpu-cloud-production-deployment-guide/ |
| whisper-large-v3-turbo | The same page that states $0.00007 USD/min says silence is hallucinated and that the model is a batch model. | https://inferencebench.io/blog/whisper-large-v3-turbo-597x-realtime-asr-benchmark/ |
| CosyVoice 3 | A 2026-06 test reports Japanese kanji routed through a Chinese text-normalization path. | https://zenn.dev/mohhh_ok/articles/2026-06-cosyvoice-qwen3-tts-apache2-mac |
| Qwen3-TTS | A hosting write-up measured clean concurrency through six streams on an A100-40GB and stalls at eight, and says day-zero vLLM support it used was offline-only. This worker did not re-run that bench and does not adopt its latency numbers as RQ-2. | https://softcery.com/lab/self-hosting-tts-for-voice-agents |
| F5-TTS | The README's own license section is the complaint: the MIT badge does not license the pretrained weights. | https://raw.githubusercontent.com/SWivid/F5-TTS/main/README.md |
| Chatterbox | The maintainer's README says the project is retired. | https://raw.githubusercontent.com/resemble-ai/chatterbox/master/README.md |

## Composition candidates

No stack is recommended. The task forbids one. A composition would also need a published per-minute cost for every component plus SIP/WebRTC, in one of the two ceiling units. That sum is unpublished.

| Stack | Components | Integration seams | Seam risk | Net build saved |
|---|---|---|---|---|
| None | — | — | — | Not estimated. |

## Rejected candidates

"Rejected" here means the viability gate or the project's own retirement notice. License score 1 on a project whose viability is at least 2.5 is in the flag table above and is not repeated as a rejection.

| Project | Why rejected | Ledger ID |
|---|---|---|
| ChatTTS | Viability 2.33. Below 2.5. AGPL-3.0 code and CC BY-NC 4.0 weights. | E-OSS-011 |
| XTTS-v2 | Viability 1.67. Below 2.5. CPML non-commercial, including outputs. coqui-ai/TTS `dev` last updated 2024-02-10. | E-OSS-012 |
| Qwen2.5-3B-Instruct | Viability 2.33. Below 2.5. Research license, not Apache-2.0. | E-OSS-015 |
| Llama-3.2-3B-Instruct | Viability 2.33. Below 2.5. Custom community license. | E-OSS-017 |
| gemma-3-4b-it | Viability 2.33. Below 2.5. Custom Gemma terms. | E-OSS-018 |
| Chatterbox | The README states it is retired research and no longer maintained. Viability is 2.50, so the <2.5 rule is not the reason. The retirement is. | E-OSS-010 |

sherpa-onnx's viability is 3.50 and its bus factor is 1. That is a maintenance liability on a runtime with 16189 stars. Stars are not a reason to ignore the bus factor. This memo still does not promote it to a stack.

## Projects named in search and not scored

Fish Speech, OpenVoice, Pocket TTS, Tontaube, Kokoro, Kyutai STT, Vosk, FunASR, Piper, and the NVIDIA streaming checkpoints other than parakeet-tdt-0.6b-v3. Their license files were not opened. VoxCPM2 and ZONOS3-Mini have a cost row and no six-dimension score, because the README, issue list, and three-month commit history were not read. ZONOS3-Mini's license file was not opened.

## K1 and C-00

K1 is UNTESTED. C-00 is OPEN. The ceiling to print, without converting either reading, is ₹0.30 per minute and 30 pence per minute.
