# Queries — g1r1-k2

**Run:** 2026-11-24-myai-myagent
**Retrieved:** 2026-11-24
**Agent:** g1r1-k2
**Question:** Does a 2024-or-later evaluation print FAR and FRR at one operating point and state whether replay, text-to-speech, and voice conversion were in that test? Each exhausted unit is retried on a source class different from the exhausted source.

Web search only. A row exists only for a page whose text was opened on 2026-11-24. The 2022 SASV challenge PDF, the Eurecom SASV PDF, and the VLSP 2025 PDF were not used. arXiv:2409.07390 and the 2005 ICME watermark PDF were not used. Citation indexes were not retrieved, so influence is unscored.

## Insider

| # | Query | Outcome |
|---|---|---|
| I1 | `spoofing-aware speaker verification false acceptance rate false rejection rate 2024 2025 pdf` | Opened Asali et al., Interspeech 2025. Results are SASV-EER 2.18% and min a-DCF 0.0480 on ASVspoof 2019 logical access. TTS and voice conversion are in that set. Replay is not. No separate FAR and FRR. → E-ACA-061. The same search surfaced the VLSP 2025 PDF and the a-DCF paper; neither was used. |
| I2 | `ASVspoof 5 challenge results false alarm rate miss rate evaluation table pdf 2025` | Opened Wang et al., arXiv:2601.03944, and Li et al., arXiv:2509.18102. Both print detection cost and EER. Neither prints FAR and FRR at one point. Replay is stated as outside ASVspoof 5. → E-ACA-073, E-ACA-074. Also opened Weizman et al., Interspeech 2025, which prints bona fide miss rate only; no row, because the miss rate is unpaired with a false-accept rate. |
| I3 | `voice biometric countermeasure replay synthesis voice conversion FAR FRR 2024 2025 2026 pdf` | Opened Yan et al., VoiceWukong, arXiv:2409.06348. Table 3 prints AASIST2 English-replay FAR 5.62% and FRR 72.59% at the labeled equal-error point. The full-set English result is EER 13.50%. → E-ACA-060. Also opened Müller et al., ReplayDF. EER only, replay of four TTS systems, no voice conversion. → E-ACA-062. Also opened Hong et al., arXiv:2601.02914. Development FAR threshold 0.01%, bypass rates, no FRR, no replay. → E-ACA-065. |

## Buyer

| # | Query | Outcome |
|---|---|---|
| B1 | `Nuance Gatekeeper OR "Microsoft speaker recognition" false acceptance false rejection deepfake replay evaluation 2024 2025 pdf` | Opened the SMIA HTML, arXiv:2509.07677. Microsoft Azure speaker verification is printed as attack success 98 and EER 0.6, with no trial count and no FAR/FRR pair. → E-ACA-068. No Nuance measurement PDF was in the opened set. |
| B2 | `"Nuance" "Gatekeeper" OR "voice biometric" "false acceptance rate" "false rejection" 2023 OR 2024 OR 2025 OR 2026 pdf` | Opened the Forasoft page updated 2026-11-20. It does not print a Nuance FAR, FRR, trial count, or the three attacks. → E-ACA-069. A third-party Gatekeeper page and a bank-comparison page appeared as snippets and were not used for numbers. |

## Skeptic

| # | Query | Outcome |
|---|---|---|
| S1 | `speech watermark false alarm rate Opus OR AMR-WB replay "voice conversion" 2024 2025 2026 pdf` | Opened Pauna et al., arXiv:2611.04716. The table is TPR at a fixed 1% FPR under OGG Opus. AMR-WB, replay, and voice conversion are not conditions. → E-ACA-071. Opened Wen et al., arXiv:2503.19176. Bit recovery is about 50% under voice conversion and zero-shot TTS. No Opus, AMR-WB, or replay false-alarm rate in the opened text. → E-ACA-072. C-ACA-01 was not adjudicated. |
| S2 | `D-CAPTCHA++ adversarial attack success telephony codec Opus AMR-WB evaluation pdf 2025 2026` | The exhausted arXiv:2409.07390 was returned and was not used. Opened Frankovits et al., arXiv:2609.11404. It tests other voice-conversion models after a 0.3–3 kHz band-pass and does not report D-CAPTCHA++ attack success through Opus or AMR-WB. → E-ACA-070. |
| S3 | `"presentation attack" speaker verification APCER BPCER OR IAPMR joint FAR FRR 2019 OR 2020 OR 2021 OR 2024 pdf -Korshunov` | Opened Gonzalez-Soler et al., arXiv:2010.04038. PAD point: BPCER 15.56% at APCER 1% on unknown physical access. No joint speaker FAR and FRR. → E-ACA-063. A face-mask paper and a 2024 lecture slide were opened and not rowed. The t-EER preprint defines an equal-error tandem point and was not rowed, because that metric is an EER. |
| S4 | `"false alarm" OR "false acceptance" impostor "speaker verification" replay "voice conversion" empirical 2023 OR 2024 OR 2025 pdf` | Opened Hoang et al., Interspeech 2024. Countermeasure results are EERs, with replay and voice conversion in the test cases and no text-to-speech column. → E-ACA-064. Opened Gajewska et al., COLING 2025. EER tables for TTS and voice conversion, no replay, no large-impostor empirical FAR. → E-ACA-067. Opened Martinek et al., Interspeech 2025. FAR thresholds are named, including 0.001%, and no numeric FRR is in the extracted text. → E-ACA-066. The exhausted Alegre Eurecom PDF appeared in this result list and was not used. |

## Dead ends

These strings did not produce a page that prints FAR below 0.001% and FRR below 1.0% at one operating point under replay, text-to-speech, and voice conversion together.

- I1 — a 2025 SASV proceedings paper prints SASV-EER only.
- I2 — the ASVspoof 5 results manuscript and a participant results table print EER and minDCF.
- I3 — the one printed FAR/FRR pair is a detector pair on a replay subset, with full-set performance left as an EER.
- B1 and B2 — no current Nuance or successor sheet with FAR, FRR, n, and the three attacks.
- S1 — no watermark false-alarm under Opus or AMR-WB combined with replay and voice conversion.
- S2 — no D-CAPTCHA++ attack-success figure through a telephony codec.
- S3 — a PAD APCER/BPCER point is not a joint speaker-verification FAR and FRR.
- S4 — later speaker-verification papers that include replay or synthesis print EER, or they name a FAR threshold without a numeric FRR.

No query returned an empty result page. The gap is the missing joint rate.
