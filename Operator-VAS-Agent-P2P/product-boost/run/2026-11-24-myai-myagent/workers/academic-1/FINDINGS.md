# Academic Scout 1 — RQ-1

Does any published speaker-verification plus anti-spoof evaluation report FAR < 0.001% (1 in 100,000) and FRR < 1.0% at the same operating point under replay, TTS/generative deepfake, and voice conversion together?

**Answer from documents opened on 2026-11-24:** No opened evaluation reports that pair. An equal-error rate is the point where FAR equals FRR. It is recorded below as a joint point, and it is not treated as a pass. K2 is not marked clear or breached in this file.

## Ledger entries written

E-ACA-001 … E-ACA-014

## The joint points

The lowest opened FAR and FRR at one threshold, for a system that is speaker verification plus a countermeasure, is the SASV 2022 evaluation winner:

- FAR = FRR = 0.13%
- Negative class: bona-fide impostors pooled with spoofs
- Spoof class: ASVspoof 2019 logical access (TTS, voice conversion, and hybrid TTS-VC)
- Replay: not in the protocol
- URL: https://arxiv.org/pdf/2203.14732
- Gap: FAR is 0.13 / 0.001 = 130 times the 0.001% line. FRR 0.13% is under 1.0% at this same equal-error point. The FAR that would meet 0.001% is not reported, so the FRR at that stricter threshold is unknown. E-ACA-001.

The opened evaluation whose test material contains replay, voice conversion, and TTS in one spoofing-aware speaker-verification protocol is VLSP 2025:

- Public-test SASV-EER 20.79%, so FAR = FRR = 20.79% at that threshold
- Private-test SASV-EER 17.78%, so FAR = FRR = 17.78%
- Public spoof counts: replay 150,000, voice conversion 55,099, adversarial 50,000, TTS 1,000 (256,099 spoof utterances). TTS is 0.39% of those spoof utterances.
- URL: https://aclanthology.org/2025.vlsp-1.10.pdf
- Gap at 17.78%: FAR is 17,780 times the 0.001% line, and FRR is 17.78 times the 1.0% line. The metric is one pooled equal-error rate, not a per-attack FAR at FRR < 1%. E-ACA-010.

The same-threshold comparison that names replay, speech synthesis, and voice conversion as separate columns, without a countermeasure, is Kucur Ergunay et al., IEEE BTAS 2015. At the male ISV natural-speech threshold (EER = FRR = 4.9%), spoof false-accept rates are 19.2% for the lowest replay condition on that system, 97.0% for logical-access speech synthesis, and 93.4% for logical-access voice conversion. URL: https://publications.idiap.ch/attachments/papers/2015/KucurErgunay_IEEEBTAS_2015.pdf. E-ACA-006.

## Ranked findings

Citation counts are unscored. A citation-index lookup returned both “cited by 4” and “cited by 56” for the SASV 2022 paper, so neither count is used. Influence = (citations / months) × venue multiplier is therefore not computed. Venue class is listed so a later worker can apply the multiplier once a count is opened.

| # | Paper / report | Venue | Date | Citations | Cit/mo | Influence | Relevance to scope | Ledger ID |
|---|---|---|---|---|---|---|---|---|
| 1 | SASV 2022 challenge results | Interspeech 2022 (top peer-reviewed; multiplier 1.3 if counted later) | 2022-09 | unscored | — | unscored | Lowest opened joint FAR = FRR for speaker verification plus anti-spoof: 0.13%. Logical-access TTS and voice conversion only. | E-ACA-001 |
| 2 | VLSP 2025 VSASV summary | VLSP 2025 proceedings (workshop; multiplier 1.0) | 2025 | unscored | — | unscored | Only opened SASV protocol whose test set contains replay, voice conversion, and TTS. Best pooled EER 17.78%. | E-ACA-010 |
| 3 | ASVspoof 5 challenge | ASVspoof Workshop 2024 (workshop; multiplier 1.0) | 2024-08 | unscored | — | unscored | Best tandem equal point is miss = non-target FA = spoof FA = 4.32%. Track 2 has no acoustic replay. Top CM Bayes point is spoof FAR 100% with miss rate 0. | E-ACA-002, E-ACA-003 |
| 4 | Sahidullah et al. | Interspeech 2016 (multiplier 1.3) | 2016-09 | unscored | — | unscored | Cascaded fusion prints known-attack FAR 0.00% at FRR 7.40%. Two-decimal 0.00% on 40,000 trials does not show FAR < 0.001%. Unknown-attack FAR is 0.34%. No replay. | E-ACA-004 |
| 5 | Martinek et al. | Interspeech 2025 (multiplier 1.3) | 2025-08 | unscored | — | unscored | States that FRR was computed at FAR = 0.001%. Retrieved text has no numeric FRR. Attacks are two TTS systems. | E-ACA-011 |
| 6 | Kucur Ergunay et al. | IEEE BTAS 2015 (multiplier 1.0) | 2015 | unscored | — | unscored | One threshold, all three attack families, no countermeasure. Lowest SFAR in the table is 11.1% at FRR 17.5%. | E-ACA-006 |
| 7 | Threshold-transfer audit | arXiv:2606.21584 (preprint, no traction counted; multiplier 0.6) | 2026-06 | unscored | — | unscored | Shows an in-domain EER of 0.21% beside a transferred point of FRR 78.7% and FAR 0.3%. Countermeasure only. | E-ACA-009 |
| 8 | Deepfake bypass test | arXiv:2601.02914 (preprint; multiplier 0.6) | 2026-01 | unscored | — | unscored | Zero-effort FAR set to 0.01%. Spoof bypass 43.1–82.7%. FRR not reported. No replay. | E-ACA-008 |
| 9 | Korshunov and Marcel | IEEE JSTSP 2017 (multiplier 1.3) | 2017 | unscored | — | unscored | Best opened cascaded presentation-attack cell: IAPMR 1.52%, FNMR 8.05%, FMR 9.45%. | E-ACA-005 |
| 10 | Alegre, Janicki, and Evans | EURECOM PDF (venue line not in the extract) | trials NIST 2006 | unscored | — | unscored | FRR fixed at 2.98%. Spoof FARs 80.86% replay, 84.67% voice conversion, 30.00% speech synthesis. | E-ACA-007 |
| 11 | ASVspoof 2021 evaluation plan | Organiser plan, 16 July 2021 (industry/consortium technical document; multiplier 0.8) | 2021-07-16 | unscored | — | unscored | Replay is a separate task from TTS and voice conversion. EER is legacy under the cited ISO/IEC rule. | E-ACA-012 |
| 12 | Sholokhov et al. | Computer Speech & Language 2019 (multiplier 1.3) | 2019 | unscored | — | unscored | Closest of 100,000 impostors: false-alarm probability 95–98% at minDCF1. Not a per-trial FAR of 0.001%. No spoof trials. | E-ACA-013 |
| 13 | NPS Nuance test | Thesis with a disclosed trial count (named-method primary research) | 2005-05 | unscored | — | unscored | Buyer-side FAR/FRR pair: FAR 1.2%, FRR 2.91%, n = 411. No anti-spoof condition. | E-ACA-014 |

## Technique → OSS pairings

No pairing is made. This scout does not select a model or an architecture.

| Technique (paper) | Applies to (OSS project) | Expected gain | Implementation difficulty | Evidence |
|---|---|---|---|---|
| — | — | — | — | Not selected. |

## Negative results / known failure modes

| Finding | Impacts which FR/NFR | Severity | Ledger ID |
|---|---|---|---|
| No opened speaker-verification-plus-anti-spoof evaluation prints FAR < 0.001% and FRR < 1.0% at one threshold under replay, TTS, and voice conversion together. | K2, Audio Signature FAR and FRR. This file does not mark K2. | The measurement the criterion asks for was not in the opened set. | E-ACA-001, E-ACA-010 |
| The best opened joint equal-error point on logical-access spoofs is FAR = FRR = 0.13%, which is 130 times the FAR line, and it omits replay. | K2. An equal-error rate near or below 1% is not the required false-accept rate. | FAR misses the line by two orders of magnitude at the point where FRR is under 1%. | E-ACA-001 |
| When replay, voice conversion, and TTS are in one SASV test, the opened pooled equal-error rates are 17.78% and 20.79%. | K2. | Both rates miss, and TTS is 0.39% of the public spoof utterances, so the pool is not a balanced three-class test. | E-ACA-010 |
| A printed known-attack FAR of 0.00% sits at FRR 7.40%, and 40,000 trials cannot show a rate below 0.001% (3/40000 = 0.0075% rule-of-three upper bound). Unknown-attack FAR at that point is 0.34%. | K2. A zero printed to two decimals is not 1 in 100,000. | FRR misses by 7.40 times; the unknown-attack FAR misses by 340 times. | E-ACA-004 |
| At a Bayes threshold, the top ASVspoof 5 open-condition countermeasure has spoof false-alarm rate 1 and bona-fide miss rate 0, while its EER is 2.59%. | K2. The equal-error point and the cost-defined point are different operating points. | The security side of the cost-defined point is a total miss. | E-ACA-003 |
| Transferring an LA equal-error threshold gives FRR 78.7% and FAR 0.3% on In-the-Wild, against an in-domain EER of 0.21%. | K2. A low equal-error rate does not survive a fixed threshold on other data. | FRR is 78.7 times the 1.0% line at the point where FAR is still 300 times the FAR line. | E-ACA-009 |
| Setting zero-effort FAR to 0.01% leaves TTS and voice-conversion bypass rates of 43.1% to 82.7%. | K2. A low impostor FAR is not a spoof FAR. | Spoof acceptance remains above 40% and FRR is unreported. | E-ACA-008 |
| Without a countermeasure, one threshold yields spoof false-accept rates of 11.1% to 97.0% across replay, synthesis, and voice conversion, at natural-speech EERs of 4.9% to 17.5%. | K2, the unprotected speaker-verification floor. | Every named cell misses both lines. | E-ACA-006, E-ACA-007 |
| A closest-of-100,000 impostor false-alarm probability of 95–98% is a different statistic from a per-trial FAR of 0.001%. | K2, how “1 in 100,000” has to be read. | The opened population test does not support the per-trial target, and it has no spoof trials. | E-ACA-013 |

## Reception & replication

| Paper | Community signal | Replication status | Ledger ID |
|---|---|---|---|
| SASV 2022 | The challenge paper calls the drop from 23.83% to 0.13% SASV-EER evidence that fused countermeasures and speaker verification are reliable. The opened text also says the DET curves differ away from the equal-error point and that the database is limited. | Later opened protocols do not report 0.13%. ASVspoof 5’s best opened t-EER is 4.32%. VLSP 2025’s best opened SASV-EER is 17.78%. These are different protocols, not a rerun of the 2022 evaluation set. | E-ACA-001, E-ACA-002, E-ACA-010 |
| ASVspoof 5 | The organisers report that systems which were strong on earlier ASVspoof sets land at EERs above 29% as baselines on the 2024 data, and that top actDCF values sit at 1.0 because scores are not calibrated log-likelihood ratios. | The calibration failure is measured on the challenge submissions, not reproduced by this scout. | E-ACA-002, E-ACA-003 |
| Martinek et al. 2025 | Cites the SASV 2022 figure of 0.13% and then evaluates read versus spontaneous speech. | Does not rerun the SASV 2022 protocol. The FRR-at-FAR=0.001% result is named and is not numeric in the retrieved text. | E-ACA-011 |

## Dead ends

Queries that did not produce a usable K2 measurement. Full log: `QUERIES.md`.

- `voice biometric bank FAR 0.001% FRR deepfake replay voice conversion evaluation pdf` — no bank report with both rates under the three attacks.
- `"no" voice biometric system achieves false acceptance deepfake replay "voice conversion" same threshold pdf` — high spoof false-accept rates only; no countermeasure at the K2 pair.
- `"1 in 100,000" OR "one in 100,000" voice biometric OR "speaker verification" false accept OR "false acceptance" pdf` — no per-trial FAR of 0.001% under spoofing.
- `"false acceptance rate of 0.001%" OR "FAR of 0.001%" OR "FAR < 0.001%" speaker "false rejection" spoof pdf` — one paper names the FAR threshold and does not print the FRR; attacks are TTS only.
- Pindrop, `https://www.pindrop.com/resources/article/testing-voice-biometric-security-against-ai-deepfakes`, and U.S. Bank, `https://opusresearch.net/pdfs/USBank_BethGallagher_VBCSF2014.pdf`, were search snippets only. They were not opened and they are not cited.

Latency, telephony-codec behaviour, watermarking, and challenge-response were left to the other academic scouts. No model or architecture is selected.
