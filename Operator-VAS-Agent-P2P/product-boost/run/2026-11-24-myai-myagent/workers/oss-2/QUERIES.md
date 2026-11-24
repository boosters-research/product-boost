# Queries — oss-scout-2

**Run:** 2026-11-24-myai-myagent
**Retrieved:** 2026-11-24
**Rule:** Every query used for E-OSS-020 through E-OSS-039. Dead ends are listed so a retry can change the string.

Framings: (1) insider capability terms, (2) buyer / commercial-alternative terms, (3) skeptic terms, production complaints and CVE or security advisories.

## Queries that returned pages used in the rows

| # | Framing | Query or fetch | Result used |
|---|---|---|---|
| 1 | Insider | `open source speaker verification anti-spoofing FAR FRR github license evaluation` | SASV2 baseline README (EER tables, MIT), SASV 2022 baseline repo, RawGAT-ST README (min t-DCF and EER, MIT), SpoofSV (plots spoof rate vs FRR; anti-spoof section of that repo says it is incomplete). |
| 2 | Buyer | `open source alternative Nuance voice biometrics speaker verification anti-spoof github Apache` | 3D-Speaker README EER table and Apache-2.0; WeSpeaker Apache-2.0; VoiceGuard README (EER only, and a held-out detection rate that is not FAR/FRR at the K2 point); RawGAT-ST MIT. |
| 3 | Skeptic | `SpeechBrain OR WeSpeaker OR NeMo OR AASIST speaker verification production problems limitations CVE security advisory` | CASE `docs/findings.md` playback EERs; NVD text for CVE-2026-10036; GitHub advisory GHSA-F54R-JQHG-Q7VG; NVIDIA NeMo Speech bulletin, September 2026. |
| 4 | Insider | `ASVspoof evaluation plan false acceptance false rejection rate OR FAR FRR pdf 2019 2021 2024` | ASVspoof 2019, 2021, and 5 plans. They define miss and false-alarm rates inside t-DCF, DCF, and a-DCF. The ranking metrics on those plans are the costs and EER, not a measured FAR < 0.001% at FRR < 1.0%. |
| 5 | Insider | `"false acceptance rate" "false rejection rate" speaker verification ECAPA OR x-vector OR wespeaker OR speechbrain github` | Brydinskyi et al. 2024 PDF, Table 3 FAR/FRR. SpeechBrain `metric_stats` can compute FAR and FRR; the published VoxCeleb table does not. |
| 6 | Insider | `wespeaker NIST SRE16 EER minDCF results github Pmiss Pfa` | WeSpeaker SRE16 commit: metric column is EER. `score_metrics.py` computes Pmiss and Pfa in order to derive EER and minDCF. NIST SRE16 plan defines Cdet from PMiss and PFalseAlarm. The WeSpeaker results table that was opened prints EER. |
| 7 | Skeptic | `AASIST anti-spoofing production failure OR "does not generalize" CVE OR advisory kaldi pyannote 3D-Speaker` | VoiceWukong arXiv HTML, Table 3 FAR/FRR on replay and EER on the full sets. Müller et al. generalization gaps are EER gaps. No CVE for AASIST on this query. |
| 8 | Skeptic | `"FRR" "FAR" speaker verification replay OR "voice conversion" OR TTS open source ECAPA OR "x-vector" pdf` | SASV 2022 PDF (primary metric SASV-EER). voice_match README says it has a FAR/FRR evaluator and that anti-spoof weights are disabled; it does not publish a measured pair. |
| 9 | Insider | `AASIST OR RawNet2 OR "XLS-R" ASVspoof "FAR" OR "false acceptance" OR APCER BPCER github license` | VoiceWukong FAR/FRR table confirmed. W2V2-AASIST Hugging Face card, EER by dataset. |
| 10 | Skeptic | `"false rejection rate" OR "FRR" "0.001%" OR "10^-5" OR "1e-5" speaker verification anti-spoof open source` | No open-source toolkit page returned a measured FRR or FAR at 0.001% or 1e-5. SASV 2022’s lowest listed figure on this query path is 0.13% SASV-EER. |
| 11 | Insider | `ASVspoof 2019 x-vector "Pfa" OR "false alarm" ASV EER logical access pdf Todisco` | arXiv 1911.01601 Tables 6, 7, and 8. Metric printed for the ASV baseline is EER. |
| 12 | Buyer | `NVIDIA NeMo TitaNet speaker verification EER VoxCeleb results documentation` | TitaNet paper Table 2 (EER and MinDCF). Hugging Face card 0.66 EER%. `voxceleb_eval.py` prints EER only. |
| 13 | Skeptic | `CVE kaldi-asr OR wespeaker OR pyannote OR AASIST OR "3D-Speaker" security advisory 2024 OR 2025 OR 2026` | No CVE record for those five names. The hit that did load was sherpa-onnx issue 3253 (heap-use-after-free report involving a pyannote segmentation model and a 3D-Speaker CAM++ ONNX file). GPT-SoVITS CVE coverage in the same results was not used; TTS licensing belongs to oss-1. |
| 14 | Skeptic | `speechbrain 1.1.1 release changelog CVE-2026-10036 site:github.com` | SpeechBrain releases page: v1.1.1 security note, v1.1.2 dated 14 Oct on that page. Advisory and the safeloader commit 22a6166. |

## Pages opened directly (raw or PDF), in addition to the search hits

| URL | Why |
|---|---|
| https://www.mdpi.com/2076-3417/14/4/1329/pdf | Table 3 numeric FAR, FRR, EER. |
| https://arxiv.org/html/2409.06348 | VoiceWukong Table 3. |
| https://arxiv.org/pdf/1911.01601 | ASVspoof 2019 baseline EER tables. |
| https://arxiv.org/abs/2110.04410 | TitaNet Table 2. |
| https://www.eurecom.fr/publication/6852/download/sec-publi-6852.pdf | SASV 2022 Table 2. |
| https://www.asvspoof.org/file/ASVspoof5___Evaluation_Plan_Phase2.pdf | ASVspoof 5 metrics. |
| https://www.asvspoof.org/asvspoof2019/asvspoof2019_evaluation_plan.pdf | 2019 plan defines Pmiss and Pfa and ranks on min t-DCF and EER. |
| https://raw.githubusercontent.com/speechbrain/speechbrain/develop/LICENSE | Apache-2.0. |
| https://raw.githubusercontent.com/speechbrain/speechbrain/develop/recipes/VoxCeleb/SpeakerRec/README.md | EER table. |
| https://github.com/speechbrain/speechbrain/releases | v1.1.1 and v1.1.2 notes. |
| https://raw.githubusercontent.com/clovaai/aasist/main/README.md | EER 0.83%, min t-DCF 0.0275. |
| https://raw.githubusercontent.com/clovaai/aasist/main/LICENSE | MIT. |
| https://github.com/clovaai/aasist/issues | Open issues #7, #15, #16, #17. |
| https://raw.githubusercontent.com/wenet-e2e/wespeaker/master/README.md | EER and minDCF notes. |
| https://raw.githubusercontent.com/wenet-e2e/wespeaker/master/LICENSE | Apache-2.0. |
| https://raw.githubusercontent.com/modelscope/3D-Speaker/main/README.md | EER benchmark. |
| https://raw.githubusercontent.com/modelscope/3D-Speaker/main/LICENSE | Apache-2.0. |
| https://raw.githubusercontent.com/NVIDIA/NeMo/main/LICENSE | Apache-2.0. |
| https://raw.githubusercontent.com/kaldi-asr/kaldi/master/COPYING | Apache License v2.0. |
| https://raw.githubusercontent.com/pyannote/pyannote-audio/main/LICENSE | MIT. |
| https://raw.githubusercontent.com/pyannote/pyannote-audio/main/README.md | DER benchmark, HF conditions, hosted precision-2. |
| https://raw.githubusercontent.com/TakHemlata/SSL_Anti-spoofing/main/LICENSE | MIT. |
| https://raw.githubusercontent.com/TakHemlata/SSL_Anti-spoofing/main/README.md | Train and eval description. The portion read does not print a FAR/FRR pair. |
| https://huggingface.co/SpeechAntiSpoofingBenchmarks/W2V2-AASIST | Arena EER table. |
| https://raw.githubusercontent.com/gittb/case-benchmark/master/docs/findings.md | Playback EER table. |
| https://nvidia.custhelp.com/app/answers/detail/a_id/5885/~/security-bulletin%3A-nvidia-nemo-speech---september-2026 | Five high CVEs. |
| https://github.com/advisories/GHSA-F54R-JQHG-Q7VG | CVE-2026-10036. |
| https://api.github.com/repos/{speechbrain/speechbrain, wenet-e2e/wespeaker, NVIDIA/NeMo, NVIDIA-NeMo/Speech, modelscope/3D-Speaker, clovaai/aasist, kaldi-asr/kaldi, pyannote/pyannote-audio, TakHemlata/SSL_Anti-spoofing, eurecom-asp/RawGAT-ST-antispoofing, Jungjee/RawNet, sasv-challenge/SASV2_Baseline, microsoft/UniSpeech} | Stars, forks, license SPDX, pushed_at, archived flag. Retrieved 2026-11-24 before the rate limit. |

## Dead ends (do not repeat these strings unchanged)

| Query or fetch | What happened |
|---|---|
| `https://nvd.nist.gov/vuln/detail/CVE-2026-10036` fetched twice | Timed out both times. The record text had already come back through search and through the GitHub advisory. A retry should use a different NVD URL form or the VulnCheck advisory linked from the GitHub advisory: `https://www.vulncheck.com/advisories/speechbrain-arbitrary-code-execution-via-ckpt-yaml-parsing`. |
| `https://api.github.com/repos/.../commits?since=2026-08-24` and `.../releases` for the candidate repos | HTTP 403 rate limit after the per-repo metadata calls. Bus-factor org counts are therefore taken from release notes and READMEs, not from the contributor graph. A retry needs a different access path, not the same unauthenticated loop. |
| WebFetch of `https://github.com/speechbrain/speechbrain/blob/develop/recipes/VoxCeleb/SpeakerRec/README.md`, `https://github.com/clovaai/aasist`, `https://github.com/wenet-e2e/wespeaker`, `https://github.com/modelscope/3D-Speaker`, and `https://github.com/gittb/case-benchmark/blob/master/docs/findings.md` | HTML shells came back empty. The same documents loaded from `raw.githubusercontent.com`. |
| `https://github.com/LuiShek/gmm-ubm-speaker-verification` | Page shell only. The search snippet mentioned 0.98% EER and an incomplete anti-spoof note. The numeric claim was not in the fetched body, so it is not a ledger row. |
| `"false rejection rate" OR "FRR" "0.001%" OR "10^-5" OR "1e-5" speaker verification anti-spoof open source` | No page with an open-source FAR below 0.001% at FRR below 1.0%. |
| `CVE kaldi-asr OR wespeaker OR pyannote OR AASIST OR "3D-Speaker" security advisory 2024 OR 2025 OR 2026` | No advisory for those project names. Do not rerun the same OR-string; split by repository if a later scout needs a per-project NVD search. |

## Not used, on purpose

- `workers/prior-contaminated/` was not opened and is not cited.
- Streaming ASR, SLM, and TTS cost and licenses were left to oss-1. GPT-SoVITS CVE text that arrived inside query 13 was not turned into a row.
