# Academic Scout g1r1-k2 — joint FAR and FRR under replay, TTS, and voice conversion

Retry 1 of 2. This worker did not write the rows it re-examined. Shared ledger, kill criteria, constraints, and contradictions were not edited.

## Ledger entries written

E-ACA-060 … E-ACA-074

## Ranked findings

Citation counts were not retrieved on 2026-11-24. Influence is unscored. Rank is by whether the opened page prints FAR and FRR at one threshold, then by date.

| # | Paper / report | Venue | Date | Citations | Cit/mo | Influence | Relevance to scope | Ledger ID |
|---|---|---|---|---|---|---|---|---|
| 1 | Yan, Zhao, and Wang, VoiceWukong | arXiv:2409.06348 | 2024-09-10 | unscored | unscored | unscored | Prints AASIST2 English-replay FAR 5.62% and FRR 72.59% at the labeled equal-error point. Full-set English result is EER 13.50%. Replay subset re-records 29 TTS systems and 5 VC systems. | E-ACA-060 |
| 2 | Asali, Ben-Shimol, and Lapidot, ATMM-SAGA | Interspeech 2025 | 2025-08 | unscored | unscored | unscored | SASV-EER 2.18% and min a-DCF 0.0480 on ASVspoof 2019 LA. TTS and VC are in the set. Replay is not. No separate FAR and FRR. | E-ACA-061 |
| 3 | Müller et al., ReplayDF | Interspeech 2025 | 2025-06-01 | unscored | unscored | unscored | Replay of four TTS systems. W2V2-AASIST EER 4.7% to 18.2%, then 11.09% after RIR retraining. No FAR/FRR pair. No VC in the attack list. | E-ACA-062 |
| 4 | Hoang et al., VSASV | Interspeech 2024 | 2024-09 | unscored | unscored | unscored | Fused ECAPA-TDNN and AASIST. EER 2.41% for bona fide plus replay plus VC. EER 8.27% when adversarial perturbation is added. No TTS column. No FAR/FRR pair. | E-ACA-064 |
| 5 | Wang et al., ASVspoof 5 evaluation | arXiv:2601.03944 | 2026-01 | unscored | unscored | unscored | 53 teams. Metrics are minDCF, actDCF, Cllr, EER, min a-DCF, min t-DCF, and t-EER. Attacks are TTS, VC, and adversarial. Sensor-level replay is outside the challenge. | E-ACA-073 |
| 6 | Li et al., XMUspeech ASVspoof 5 | arXiv:2509.18102 | 2025-09-05 | unscored | unscored | unscored | Track 1 fusion: open-condition minDCF 0.2245 and EER 9.36%; closed-condition minDCF 0.4783 and EER 20.45%. No FAR/FRR pair. | E-ACA-074 |
| 7 | Hong et al., deepfake bypass | arXiv:2601.02914 | 2026-01-06 | unscored | unscored | unscored | Development threshold set at FAR 0.01%. Bypass 56.2%, 82.7%, and 43.1% for two TTS systems and one VC system. No FRR. No replay. | E-ACA-065 |
| 8 | Martinek et al., flow of speech | Interspeech 2025 | 2025-08 | unscored | unscored | unscored | Names FRR at FAR 0.001% in a figure. Extracted text has no numeric FRR. Table 1 is EER. TTS only. | E-ACA-066 |
| 9 | Gajewska et al., Polish and English synthesis | COLING 2025 | 2025-01-19 | unscored | unscored | unscored | EER for TTS and VC. Close, middle, and far neighbors. 240 LibriSpeech speakers. No replay. No large-impostor empirical FAR. | E-ACA-067 |
| 10 | Gonzalez-Soler et al., texture PAD | arXiv:2010.04038 | 2020-10-08 | unscored | unscored | unscored | BPCER 15.56% at APCER 1% on unknown physical access. PAD rates, separate from logical-access TTS and VC. No joint speaker FAR and FRR. | E-ACA-063 |
| 11 | SMIA | arXiv:2509.07677 | 2025-09 | unscored | unscored | unscored | Microsoft Azure speaker verification: attack success 98, EER 0.6. No n. No FAR/FRR. No stated three-attack cell. | E-ACA-068 |
| 12 | Forasoft voice-biometrics guide | Trade blog | 2026-11-20 | unscored | unscored | unscored | No Nuance Gatekeeper FAR, FRR, n, or three-attack test. | E-ACA-069 |
| 13 | Frankovits et al., DF-CAPTCHA | arXiv:2609.11404 | 2026-09-10 | unscored | unscored | unscored | StarGANv2-VC fooled 46% of volunteers after a 0.3–3 kHz band-pass. No D-CAPTCHA++ result through Opus or AMR-WB. | E-ACA-070 |
| 14 | Pauna, Wang, and Juvela, cross-codec watermark | arXiv:2611.04716 | 2026-11 | unscored | unscored | unscored | TPR at a fixed 1% FPR under OGG Opus. No AMR-WB, replay, or voice-conversion false-alarm. | E-ACA-071 |
| 15 | Wen et al., audio-watermark SoK | arXiv:2503.19176 | 2025-03-27 | unscored | unscored | unscored | Bit recovery about 50% under VC and zero-shot TTS. No Opus or AMR-WB false-alarm. No replay. | E-ACA-072 |

## The 2024-or-later pair

VoiceWukong Table 3 is the opened evaluation that prints both rates at one labeled operating point.

- Rates: AASIST2, English replay subset, FAR 5.62% and FRR 72.59%.
- The same table prints the full English benchmark result for AASIST2 as EER 13.50%. That EER is left as an EER.
- Attack list for the printed pair: the replay subset, produced by re-recording the benchmark deepfakes. The paper counts those generators as 29 text-to-speech systems and 5 voice-conversion systems. The FAR/FRR columns are not split into a non-replay TTS cell and a VC cell.

The two rates are a deepfake-detector pair on replayed deepfakes. They are not a speaker-verification operating point with FAR below 0.001% and FRR below 1.0%.

## Technique → OSS pairings

| Technique (paper) | Applies to (OSS project) | Expected gain | Implementation difficulty | Evidence |
|---|---|---|---|---|
| Replay re-recording of commercial and open TTS/VC audio, scored at the detector equal-error threshold | AASIST-family countermeasures, including the AASIST2 checkpoint evaluated in VoiceWukong | The opened table shows the English replay cell at FAR 5.62% and FRR 72.59% for the system whose full-set English EER is 13.50%. The paper does not print a repaired checkpoint at the K2 pair. | The failure is in the replay condition of an already trained detector. A fix is a new training and threshold study, and this paper does not supply that threshold pair. | E-ACA-060 |
| Real loudspeaker-microphone replay of Bark, VITS, and XTTS, with room-impulse retraining | W2V2-AASIST and the other five open detectors in ReplayDF | EER moves from 4.7% to 18.2% under replay, and to 11.09% after RIR retraining. Both numbers are EERs. | The dataset and the RIR condition are specified. The paper does not print FAR and FRR, so the gain cannot be stated as a FAR/FRR move. | E-ACA-062 |
| Score-gated fusion of AASIST and ECAPA-TDNN (ATMM-SAGA) | ECAPA-TDNN speaker embeddings plus an AASIST countermeasure | Evaluation-set SASV-EER 2.18% and min a-DCF 0.0480 on ASVspoof 2019 logical access. | The training alternation is specified. The test has TTS and voice conversion and has no replay, and the metric is an EER. | E-ACA-061 |

## Negative results / known failure modes

| Finding | Impacts which FR/NFR | Severity | Ledger ID |
|---|---|---|---|
| The only opened 2024-or-later page that prints FAR and FRR at one labeled point prints 5.62% and 72.59% on a replay subset. | Audio-signature FAR below 0.001% and FRR below 1.0% at one operating point, under replay, generative deepfake, and voice conversion together. | The printed pair is far from both targets, and it is a detector pair on replayed deepfakes. K2 stays unmarked. | E-ACA-060 |
| A 2025 spoofing-aware speaker-verification system prints SASV-EER 2.18% on TTS and voice conversion, with no replay and no separate FAR and FRR. | Same joint operating point. | An EER is not the requested pair. | E-ACA-061 |
| Replaying four TTS systems raises a strong detector from EER 4.7% to EER 18.2%. | Anti-spoof defence against replay of synthetic speech. | The page does not print the joint FAR and FRR the 2015-era unit was missing. | E-ACA-062 |
| A fused countermeasure evaluated on replay and voice conversion together prints EER 2.41%, and 8.27% when adversarial perturbation is included. Text-to-speech is not in the table. | Countermeasure result on replay, synthesis, and voice conversion together. | The three named attacks are not in one printed FAR/FRR cell. | E-ACA-064 |
| ASVspoof 5 results are minDCF, a-DCF, t-DCF, and EER. The challenge text excludes sensor-level replay. | Published ASVspoof 5 result table with FAR and FRR at one point. | The result tables do not contain that pair. | E-ACA-073, E-ACA-074 |
| A 2026 speaker-verification test sets the development threshold at FAR 0.01% and prints TTS and VC bypass rates, with no FRR and no replay. | Spoof FAR while FRR is held under 1%. | The requested hold on FRR is not in the paper. | E-ACA-065 |
| A 2025 paper names FRR at FAR 0.001% and does not print the FRR. Synthetic trials are two TTS systems. | Same FRR-held-under-1% spoof FAR. | The number is not in the extracted text. | E-ACA-066 |
| A 2025 bilingual study prints EER for TTS and voice conversion and uses a few biometric neighbors, with no replay. | Empirical FAR against many impostors that also includes replay, TTS, and voice conversion. | No such empirical FAR is printed. | E-ACA-067 |
| A PAD paper prints BPCER 15.56% at APCER 1% on unknown replay. | Joint speaker-verification point. | The cell is a presentation-attack detection point. | E-ACA-063 |
| An attack paper prints Azure speaker-verification attack success 98 and EER 0.6, with no trial count. A 2026 blog prints no Nuance FAR/FRR test. | Current Nuance or successor FAR/FRR with n and the three attacks. | The requested sheet was not found. | E-ACA-068, E-ACA-069 |
| A 2026 challenge-response paper does not measure D-CAPTCHA++ through Opus or AMR-WB. | Attack success of D-CAPTCHA++ through a telephony codec. | The path remains unmeasured in the opened later paper. | E-ACA-070 |
| A 2026 watermark paper reports TPR at a fixed 1% FPR under Opus. A 2025 SoK reports about 50% bit recovery under VC and TTS. | Watermark false-alarm under Opus or AMR-WB with replay and voice conversion. | That combined false-alarm is not printed. C-ACA-01 stays open. | E-ACA-071, E-ACA-072 |

## Reception and replication

| Paper | Community signal | Replication status | Ledger ID |
|---|---|---|---|
| VoiceWukong | Citation count unscored. The paper publishes a leaderboard URL. | This pass did not rerun the detectors. The FAR and FRR are taken from the opened Table 3. | E-ACA-060 |
| ReplayDF | Citation count unscored. The authors release ReplayDF for non-commercial research. | This pass did not rerun W2V2-AASIST. The EER move is the authors' reported result. | E-ACA-062 |
| ASVspoof 5 evaluation manuscript | Citation count unscored. It summarises 53 participating teams. | This pass did not recompute minDCF or EER. No FAR/FRR table was in the opened results. | E-ACA-073 |
| Cross-codec watermark and the watermark SoK | Citation counts unscored. | This pass did not retrain a watermark. Neither opened text prints the codec-plus-replay-plus-voice-conversion false-alarm. | E-ACA-071, E-ACA-072 |

## Dead ends

Queries and opened pages that did not yield the requested pair are listed in `QUERIES.md`. The repeated gap is the same one: a page prints an EER, a detection cost, a bypass rate, or one side of the tradeoff, and it does not print FAR and FRR together under replay, text-to-speech, and voice conversion.

K2 is unmarked. C-ACA-01 stays open.
