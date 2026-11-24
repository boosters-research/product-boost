# OSS Scout 2 — Speaker verification and anti-spoof

**Run:** 2026-11-24-myai-myagent
**Agent:** oss-scout-2
**Retrieved:** 2026-11-24
**Question:** Which open-source speaker-verification and anti-spoof toolkits publish a license and an evaluation that reports FAR and FRR, and do any of those numbers reach FAR < 0.001% at FRR < 1.0% under replay, TTS, and voice conversion together?
**K2:** This file does not mark K2 clear. K2 stays UNTESTED. No stack is selected.

## Ledger entries written

E-OSS-020 … E-OSS-039 (20 rows) in `LEDGER-ROWS.md`. Shared ledger files were not edited.

## Answer

Two kinds of publication showed up.

**FAR and FRR are printed, and they miss the joint target.** Brydinskyi et al., *Applied Sciences* 2024, Table 3, prints FAR and FRR for pretrained ECAPA, TitaNet-Large, PyAnnote, and two WavLM speaker models. The tightest pair on that table is ECAPA at FAR 1.73% and FRR 1.68% (EER 1.71%) on 4,500 zero-effort pairs from 50 YouTube speakers. That pair sits on the equal-error point. The experiment section describes same-speaker and different-speaker pairs. It does not describe replay, TTS, or voice conversion. FAR 1.73% is 1,730 times the 0.001% line.

VoiceWukong Table 3 prints FAR and FRR on a replay subset at the equal-error threshold of the full set. The lowest English-replay FAR in that table is AASIST2 at FAR 5.62% with FRR 72.59%. The English-replay rows whose FRR is 0.00% are OC-Softmax at FAR 99.47% and Raw PC-DARTS at FAR 99.65%. Those rows are one attack class, at one threshold, and they are not a joint pass under replay, TTS, and voice conversion.

**The toolkit’s own results table prints EER, sometimes with minDCF or min t-DCF, and does not print a FAR/FRR pair.** That list is at the end of this file. An EER near 1%, including the SASV 2022 top submission at SASV-EER 0.13% and the open-source SASV baselines at 19.31%, 1.71%, and 6.54%, is not a measurement of FAR < 0.001% at FRR < 1.0%.

## Candidate register

Scores are 0–5. `viability = mean(six scores)`. Star counts are from the GitHub API on 2026-11-24 and are not the viability finding. Contributor-graph calls returned HTTP 403 after the repo metadata calls, so bus factor uses the names on pages that did load. No stack is recommended as the Audio Signature.

| Project | Capability covered | Stars | Bus | Recency | License | Sec | Fork | Release | Viability | Ledger ID |
|---|---|---|---|---|---|---|---|---|---|---|
| SpeechBrain | Speaker embedding and VoxCeleb verification recipe. Published metric is EER. | 11951 | 4 | 3 | 5 | 3 | 3 | 5 | 3.83 | E-OSS-025, E-OSS-036 |
| NVIDIA NeMo (TitaNet) | Speaker embedding. Published metric is EER and MinDCF. | 18783 | 5 | 5 | 5 | 3 | 3 | 4 | 4.17 | E-OSS-029, E-OSS-030, E-OSS-031, E-OSS-037 |
| pyannote.audio | Speaker diarization. Own benchmark is DER. A third-party paper prints FAR/FRR for a model it calls PyAnnote. | 10838 | 3 | 4 | 5 | 3 | 3 | 3 | 3.50 | E-OSS-021 |
| WeSpeaker | Speaker embedding, VoxCeleb and NIST SRE16 recipes. Published metrics are EER and minDCF. | 1476 | 3 | 3 | 5 | 3 | 3 | 3 | 3.33 | E-OSS-026, E-OSS-027 |
| 3D-Speaker | Supervised speaker verification recipes. Published metric is EER. | 3225 | 3 | 2 | 5 | 3 | 3 | 2 | 3.00 | E-OSS-028 |
| Kaldi | x-vector ASV used as the ASVspoof 2019 fixed backend. Published metric in that paper is EER. | 15518 | 3 | 1 | 5 | 3 | 3 | 2 | 2.83 | E-OSS-032, E-OSS-033 |
| AASIST (clovaai/aasist) | Anti-spoof countermeasure. Published metric is EER and min t-DCF. | 316 | 1 | 1 | 5 | 2 | 3 | 1 | 2.17 | E-OSS-024 |
| SSL_Anti-spoofing | XLS-R + AASIST countermeasure. Third-party arena prints EER only. | 186 | 1 | 1 | 5 | 2 | 3 | 1 | 2.17 | E-OSS-038 |
| SASV2 baseline | Joint spoofing-aware speaker verification baseline. Published metric is SASV-EER, SV-EER, SPF-EER. | 29 | 2 | 1 | 5 | 2 | 3 | 1 | 2.33 | E-OSS-034 |

Score inputs, so the means can be checked:

- SpeechBrain bus 4: the v1.1.2 release page names more than four people and does not list their organizations. Recency 3: `pushed_at` 2026-10-14, 41 days before retrieval, inside 90 days and outside 30 days. License 5: Apache-2.0 text opened. Security 3: CVE-2026-10036 is fixed in v1.1.1; the GitHub advisory page still says patched versions are unknown. Fork 3: 1,765 forks, no dominant hostile fork opened. Release 5: v1.1.1 (27 Aug 2026) and v1.1.2 (14 Oct 2026) with changelogs. Mean (4+3+5+3+3+5)/6 = 23/6 = 3.83.
- NeMo bus 5: the repository and the September 2026 bulletin are NVIDIA’s; the contributor list itself returned 403. Recency 5: `pushed_at` 2026-11-24. License 5: Apache-2.0 text opened. Security 3: five high CVEs, vendor says version 3.0 contains the fix; that tag was not opened. Fork 3: 3,700 forks. Release 4: the bulletin uses a 3.0 version line and the model card uses 1.10.0. Mean (5+5+5+3+3+4)/6 = 25/6 = 4.17.
- pyannote bus 3: recent citations on the README name Hervé Bredin and Alexis Plaquet. Recency 4: `pushed_at` 2026-11-19, benchmark table dated 2025-09. License 5: MIT text opened for the code. Security 3: no advisory for this repository was returned by the CVE query. Fork 3. Release 3: a changelog is linked; semver and LTS were not opened. Mean (3+4+5+3+3+3)/6 = 21/6 = 3.50.
- WeSpeaker bus 3: organization spread was not on the pages opened. Recency 3: `pushed_at` 2026-09-22. License 5. Security 3: no advisory returned. Fork 3: 212 forks. Release 3: tagged v1.0.0 exists (2022-11-12); later recipe notes land on master. Mean (3+3+5+3+3+3)/6 = 20/6 = 3.33.
- 3D-Speaker bus 3. Recency 2: `pushed_at` 2025-12-08, about 351 days, outside the 90-day bar and inside 12 months. License 5. Security 3: no advisory returned. Fork 3: 272 forks. Release 2: dated README notes, no semver tag opened. Mean (3+2+5+3+3+2)/6 = 18/6 = 3.00.
- Kaldi bus 3. Recency 1: `pushed_at` 2025-09-22, about 14 months. License 5: COPYING says Apache License v2.0. Security 3: no advisory returned. Fork 3: 5,337 forks. Release 2: release tags were not opened. Mean (3+1+5+3+3+2)/6 = 17/6 = 2.83.
- AASIST bus 1: last push 2023-06-25, and issue #7 “Can not reproduce result” has been open since 2022-04-23. Recency 1. License 5: MIT text opened. Security 2: no advisory and no security policy page opened. Fork 3: 85 forks. Release 1: the result is a README line, with no release tags opened. Mean (1+1+5+2+3+1)/6 = 13/6 = 2.17. Below 2.5, so it is not a core dependency.
- SSL_Anti-spoofing: same pattern as AASIST. Last push 2023-09-26. MIT text opened. Mean 2.17. Below 2.5.
- SASV2 baseline bus 2: challenge baseline, 29 stars, 0 open issues. Recency 1: `pushed_at` 2025-11-12. License 5: MIT on the API record. Security 2. Fork 3. Release 1. Mean (2+1+5+2+3+1)/6 = 14/6 = 2.33. Below 2.5.

pyannote viability in the table above is corrected here to **3.50**. The table cell was left as first-pass arithmetic; this paragraph is the one to use.

Viability under 2.5, which the scout protocol treats as “do not recommend as a core dependency”: AASIST 2.17, SSL_Anti-spoofing 2.17, SASV2 baseline 2.33. Kaldi at 2.83 is above that line and is still a poor Audio Signature candidate because its opened ASVspoof numbers are EERs from 2019 and the repository’s last push is 2025-09-22.

## What each project publishes

| Project | License opened | Evaluation that was opened | Rates on that page | Dataset and attack | Meets FAR < 0.001% and FRR < 1.0% together under replay, TTS, and voice conversion? |
|---|---|---|---|---|---|
| ECAPA, as measured by Brydinskyi et al. 2024 | The paper does not name the weight repository. SpeechBrain, a common ECAPA implementation, is Apache-2.0. | Table 3 prints FAR, FRR, and EER. | FAR 1.73%, FRR 1.68%, EER 1.71% | 4,500 zero-effort pairs, 50 YouTube speakers. No replay, TTS, or voice conversion in the experiment section. | No |
| TitaNet-Large, same paper | NeMo is Apache-2.0. | Table 3 | FAR 1.91%, FRR 1.91%, EER 1.91% | Same zero-effort set | No |
| PyAnnote, same paper | pyannote.audio code is MIT. | Table 3 | FAR 3.78%, FRR 3.82%, EER 3.8% | Same zero-effort set | No |
| AASIST2, RawNet2, AASIST, RawGAT-ST, and the other VoiceWukong detectors | AASIST, RawGAT-ST, RawNet, and SSL_Anti-spoofing licenses opened as MIT. AASIST2’s own license file was not opened. | Table 3 prints FAR and FRR on the replay subset at the equal-error point, plus EER on the full set. | Lowest English-replay FAR: AASIST2 FAR 5.62%, FRR 72.59%, English EER 13.50%. AASIST English EER 28.16%, English-replay FAR 17.88%, FRR 55.34%. | Replay is a laptop playback re-recorded at 1 m. TTS and voice conversion are in the corpus, and this FAR/FRR pair is the replay subset only. | No |
| SpeechBrain ECAPA-TDNN | Apache-2.0 | VoxCeleb recipe README | EER 0.80% with s-norm, 0.90% without, on VoxCeleb1+2. VoxCeleb2-only ECAPA: 1.30% / 1.98% / 3.62% on VoxCeleb1-O / E / H. | VoxCeleb1 official veri_test2 split. Zero-effort. | No. The table has no FAR or FRR column. |
| WeSpeaker | Apache-2.0 | README | 293-layer r-vector 0.447% EER and 0.043 minDCF on vox1-O-clean (note dated 2022-10-31). SRE16 after PLDA adaptation: EER 6.608% pooled, 10.01% Tagalog, 2.974% Cantonese (note dated 2023-07-14). | VoxCeleb1-O clean, and NIST SRE16 language trials. | No |
| 3D-Speaker | Apache-2.0 | README benchmark | ERes2Net-large EER 0.52% VoxCeleb1-O, 6.17% CNCeleb, 6.34% on the 3D-Speaker set. ECAPA-TDNN in the same table: 0.86% VoxCeleb1-O. | Fully supervised speaker verification. The attack is not stated as replay, TTS, or voice conversion. | No |
| NeMo TitaNet | Apache-2.0 | ICASSP/arXiv Table 2, and the Hugging Face card | Paper: TitaNet-L 25.3M, EER 0.68%, MinDCF 0.087, Ptarget = 0.01. Card: TitaNet-Large 23M, version 1.10.0, 0.66 EER% on the cleaned trial. | VoxCeleb1 cleaned trial. Zero-effort. These are two checkpoints, so 0.68 and 0.66 are both kept. | No |
| Kaldi x-vector ASVspoof 2019 backend | Apache License v2.0 in COPYING | Database paper Tables 6 and 8 | Bona fide imposter EER 2.43% dev / 2.48% eval. A16 eval EER 64.52%. A17 eval EER 3.92%. Pooled LA eval CM B1: min-tDCF 0.2366, EER 9.57%. | LA attacks are TTS, voice conversion, and hybrids. PA is replay. The printed ASV number is EER. A development CM EER of 0.00% on a known attack is still an EER, and the pooled evaluation EER is 9.57% and 8.09%. | No |
| AASIST | MIT, NAVER copyright 2021 | README eval line | EER 0.83%, min t-DCF 0.0275. AASIST-L: EER 0.99%, min t-DCF 0.0309. | README says train, validate, and evaluate on ASVspoof 2019 logical access. | No |
| SASV 2022 open-source baselines (ECAPA-TDNN + AASIST) | Code links in the paper: TaoRuijie/ECAPATDNN, clovaai/aasist (MIT), sasv-challenge/SASVC2022_Baseline | Challenge paper Table 2, primary metric SASV-EER | ASV subsystem 23.83%. B1 19.31%. B1-v2 1.71%. B2 6.54%. The paper also reports ECAPA SV-EER 1.63% with spoofed trials removed. | ASVspoof 2019 LA, target vs bona fide non-target and spoofed non-target. | No. 0.13% is the IDVoice submission’s SASV-EER. The paper cites ID R&D system descriptions for that team. That 0.13% figure is an EER, and this scout does not treat IDVoice as the open-source baseline. |
| XLS-R + AASIST arena card | MIT, pointing at TakHemlata/SSL_Anti-spoofing | Hugging Face card, EER only | ASVspoof2019_LA test EER 0.22% (71,237 trials). CD-ADD EER 38.57% (20,786 trials), described as modern neural TTS. SONAR EER 46.12% (3,948 trials). ASVspoof5 EER 16.25% (680,774 trials). | In-domain LA versus out-of-domain TTS, vocoder, and crowdsourced spoof sets. | No |
| pyannote.audio | MIT for the code | README benchmark dated 2025-09 | Diarization error rate, for example VoxConverse 11.2% for community-1. | Diarization, not a verification FAR/FRR trial. | No |
| ASVspoof 5 phase-2 plan | Organizer plan, not a toolkit license | Plan dated 28 June 2024 | Primary metrics are min DCF (Track 1) and min a-DCF (Track 2), with EER, Cllr, min t-DCF, and t-EER also defined. | The plan defines miss and false-alarm rates inside the cost. It does not publish a measured pair at FAR 0.001% and FRR 1%. | No |

## Coverage map — what each candidate does and does not do

| FR from scope doc | Covered by | Coverage | Gap requiring custom work |
|---|---|---|---|
| FR-2.1 Enroll the live voiceprint | SpeechBrain, WeSpeaker, NeMo TitaNet, 3D-Speaker, Kaldi x-vector | These projects train or ship a speaker embedding and a similarity or PLDA score. | The enrollment quality bar is UNKNOWN in the scope. None of the opened tables states an enrollment threshold whose FRR stays under 1.0% while impostor FAR stays under 0.001%. |
| FR-2.2 Authorize with voiceprint, liveness, and watermark | No opened toolkit implements the three checks together. | Speaker score and, separately, a spoof score exist in the SASV baselines. | The acoustic watermark synchronized to the banking app is outside this scout. Score fusion in the opened SASV baselines is still reported as EER. |
| FR-2.3 Reject replay, generative deepfake, and voice conversion | AASIST, RawGAT-ST, RawNet2, SSL_Anti-spoofing, and the ASVspoof / SASV baselines | Countermeasure code and challenge protocols exist for these attack names. | The opened numbers are EER, min t-DCF, a-DCF, or FAR/FRR at an equal-error threshold. VoiceWukong’s replay FAR/FRR pair does not also carry TTS and voice conversion at that same threshold. No opened page is a K2 measurement. |

## Composition candidates

No stack is selected. These are seams only. Every row leaves K2 unmeasured.

| Stack | Components | Integration seams | Seam risk | Net build saved (est.) |
|---|---|---|---|---|
| Embedding plus a separate countermeasure | One of SpeechBrain ECAPA, WeSpeaker ResNet, or NeMo TitaNet, plus AASIST or SSL_Anti-spoofing | Two scores have to be fused. SASV 2022 already did this with ECAPA-TDNN and AASIST. The open baselines land at SASV-EER 19.31% (B1), 1.71% (B1-v2), and 6.54% (B2). | High. The fusion papers report EER. A low EER does not locate the FAR < 0.001% point, and the countermeasure repos last moved in 2023. | The training and scoring code for an embedding and a countermeasure. It does not supply the operating point FR-2.3 requires. |
| Kaldi or WeSpeaker SRE-style detector plus an ASVspoof countermeasure | Kaldi x-vector or WeSpeaker SRE16, plus the ASVspoof CM | NIST-style detection cost uses Pmiss and Pfa inside a cost. The opened WeSpeaker SRE16 table prints EER only. The ASVspoof 2019 paper prints EER and min-tDCF. | High. SRE16 pooled EER is 6.608%. ASVspoof LA pooled CM EER on the evaluation set is 9.57% (B1) and 8.09% (B2). | Recipes and scoring scripts. The banking threshold is still unmeasured. |
| pyannote.audio as the verifier | pyannote embedding or community-1 | The maintained benchmark is diarization error rate. precision-2 runs on pyannoteAI servers. community-1 requires accepting Hugging Face user conditions; that conditions text was not opened. | High for this use case. Diarization error rate is a different metric, and the hosted pipeline is not an escape hatch that stays on-device. | A diarization pipeline. It does not cover FR-2.3. |

## License red flags

| Project | License | Commercial constraint | Escalate at gate |
|---|---|---|---|
| SpeechBrain, WeSpeaker, 3D-Speaker, NeMo, Kaldi | Apache-2.0 | Permissive code license. NeMo Speech versions 0.0 through 2.9 are in the September 2026 bulletin; the vendor points operators to 3.0. | Security maintenance, not a copyleft flag. |
| AASIST, RawGAT-ST, RawNet, SSL_Anti-spoofing, pyannote.audio code, SASV2 baseline | MIT | Permissive code license. | None on the license text that was opened. |
| pyannote community-1 weights | MIT code. Weight terms are a separate click-through that this scout did not open. | The README requires accepting Hugging Face user conditions before `Pipeline.from_pretrained("pyannote/speaker-diarization-community-1")`. | Open question for legal review before any weight is shipped. The code license score stays 5 because the LICENSE file is MIT. |
| pyannote precision-2 | Hosted pyannoteAI service called from the same library | The README’s precision-2 path sends audio to pyannoteAI. That path is a hosted dependency. | Do not treat precision-2 as self-hosted open source. |
| IDVoice SASV submission | Not established as an open-source license in the challenge paper | The 0.13% SASV-EER row is a participant result cited to ID R&D system descriptions. | Do not adopt that number as an OSS result. |

No AGPL, SSPL, or BUSL relicensing was found in the license files opened for these repositories. That is not a K2 finding.

## Production complaints and security advisories

Three framings were run: the capability terms, the commercial-alternative terms, and the complaint / CVE terms. The complaint pages that loaded:

- CASE benchmark `docs/findings.md` prints equal error rates, not FAR/FRR. On its playback chain (codec, then loudspeaker, then room, then microphone) it lists WeSpeaker ResNet34 0.58% clean and 8.57% playback, SpeechBrain ECAPA 0.56% and 9.37%, NeMo TitaNet-L 0.66% and 12.61%, and a pyannote embedding 1.68% and 11.22%. The file does not date itself and does not state the trial count. Playback here is a channel stress test, not the VoiceWukong spoof-replay protocol.
- VoiceWukong’s own summary says the best EER it measured for the 12 open detectors is AASIST2 at 13.50% English and 13.54% Chinese, against 0.82% EER on that detector’s original set. The in-domain to replay FAR/FRR split is in E-OSS-022.
- The Speech Anti-Spoofing Arena card for the MIT XLS-R + AASIST checkpoint prints 0.22% EER on ASVspoof 2019 LA and 38.57% EER on CD-ADD, which the card describes as modern neural TTS.
- AASIST issues, opened 2026-11-24: #7 “Can not reproduce result” has been open since 2022-04-23. #17 “The prediction of the pre-trained AASIST” was opened 2026-08-30. The repository `pushed_at` is 2023-06-25. These are single-thread reports (T4). They support a maintenance finding. They are not an error rate.
- sherpa-onnx issue #3253, opened in search results on 2026-11-24, reports an access violation and a later comment describes a heap-use-after-free in offline diarization when the segmentation model is pyannote and the embedding is a 3D-Speaker CAM++ ONNX file. That is a runtime crash report (T4), not a FAR/FRR result, and it is not a CVE record for 3D-Speaker or pyannote.
- CVE-2026-10036, SpeechBrain before 1.1.1: arbitrary code execution from a crafted `CKPT.yaml` parsed with PyYAML’s unsafe loader during checkpoint enumeration. GitHub Advisory Database lists CVSS 8.7 high. The v1.1.1 release notes include the safeloader fix. NVD’s HTML page timed out on two direct fetches; the advisory text was retrieved through search and through the GitHub advisory page.
- NVIDIA security bulletin, NeMo Speech, revision 1.0.0 dated 22 September 2026: CVE-2026-65179 (CVSS 8.8), CVE-2026-24267 (7.8), CVE-2026-24239 (7.8), CVE-2026-65111 (7.8), and CVE-2026-65178 (7.8). Affected versions on that page: 0.0 to 2.9. Updated version named on that page: 3.0. A direct API read of `NVIDIA-NeMo/Speech` returned the same star count, creation date, and `pushed_at` as `NVIDIA/NeMo`, so a separate Speech repository object was not confirmed.

The CVE query did not return an advisory for Kaldi, WeSpeaker, pyannote.audio, AASIST, or 3D-Speaker. Absence from one query is not a claim that no advisory exists.

## Rejected candidates

| Project | Why rejected | Ledger ID |
|---|---|---|
| Any stack as the Audio Signature | No opened evaluation is FAR < 0.001% and FRR < 1.0% at one operating point under replay, TTS, and voice conversion. K2 stays UNTESTED. | E-OSS-039 |
| IDVoice 0.13% SASV-EER | The figure is an equal error rate. The paper treats it as a participant system and cites ID R&D descriptions. The open baselines on the same table are 19.31%, 1.71%, and 6.54% SASV-EER. | E-OSS-034 |
| AASIST as a core dependency | Viability 2.17. Last push 2023-06-25. Open issue #7 since 2022-04-23 says the result could not be reproduced. The README metric is EER 0.83% and min t-DCF 0.0275. | E-OSS-024 |
| SSL_Anti-spoofing as a core dependency | Viability 2.17. Last push 2023-09-26. The arena card that reprints the checkpoint is EER-only and shows 38.57% EER on the modern-TTS set it names. | E-OSS-038 |
| SASV2 baseline as a core dependency | Viability 2.33. The README table opened via search prints SASV-EER, SV-EER, and SPF-EER. Stage-1 ECAPA-TDNN on that page is SASV-EER 20.66, SV-EER 0.74, SPF-EER 27.30. | E-OSS-034 |
| A development-set CM EER of 0.00% on ASVspoof 2019 | Table 7 prints EER 0.00 for several known development attacks. Table 8 pooled evaluation EER is 9.57% (B1) and 8.09% (B2). A 0.00 EER on a known attack is not FAR < 0.001% at FRR < 1.0%. | E-OSS-033 |
| GPT-SoVITS CVE writeups | Returned by the CVE query and left unused. Voice-clone TTS licensing and cost belong to oss-1. | — |

## Kits whose opened evaluation reports EER (or EER plus a cost) and does not report a FAR/FRR pair

SpeechBrain VoxCeleb recipe. WeSpeaker VoxCeleb and SRE16 recipes. 3D-Speaker supervised benchmark. NeMo TitaNet paper, Hugging Face card, and `voxceleb_eval.py` (the script prints one EER percentage). AASIST README. RawGAT-ST README, which says to compute min t-DCF and EER. SASV 2022 and the SASV2 baseline README. ASVspoof 2019 database paper. ASVspoof 5 phase-2 plan, as the ranking metrics. Speech Anti-Spoofing Arena card for W2V2-AASIST. CASE benchmark findings. pyannote.audio README, which reports diarization error rate rather than EER or FAR/FRR.

SpeechBrain’s `metric_stats.summarize` API can compute FAR and FRR if a caller passes a threshold. The VoxCeleb results table that was opened does not publish those rates.

## Runtime notes

SpeechBrain, WeSpeaker, NeMo, 3D-Speaker, AASIST, and pyannote.audio are Python and PyTorch. Kaldi is C++ with its own recipes. WeSpeaker documents ONNX and TensorRT export. NeMo TitaNet-Large is about 23M–25.3M parameters depending on the page. The XLS-R + AASIST card states 317.84M parameters and a fixed 64,600-sample window. None of these pages states a per-minute compute cost. Cost and ASR/TTS licenses stay with oss-1.

Escape hatch: the Apache-2.0 and MIT code repositories can be forked. pyannote precision-2 cannot; that path is the vendor API. community-1 runs locally after the Hugging Face conditions are accepted, and those conditions were not read here.
