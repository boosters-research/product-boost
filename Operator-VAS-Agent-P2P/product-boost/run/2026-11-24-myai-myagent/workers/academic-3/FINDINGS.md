# Academic Scout 3 — Codec-condition detection for challenge-response liveness and acoustic watermarks

**Run:** 2026-11-24-myai-myagent
**Agent:** academic-scout-3
**Retrieved:** 2026-11-24
**Question:** Do published challenge-response voice-liveness tests and acoustic-watermark schemes report detection performance after telephony codecs (AMR-WB, Opus, or narrowband PSTN)? The metric is the reported false-accept and false-reject rates, the codec, and whether the paper includes replay or voice conversion.

This file does not answer the speaker-verification FAR question (academic-1) and does not answer the speech-to-speech latency question (academic-2). No algorithm is selected. K2 stays UNTESTED. A watermark true-positive rate of 1.00 at a 1% false-positive rate, a bit detection rate of 100%, and a challenge-response AUROC of 88.7% are each a different measurement from FAR < 0.001% and FRR < 1.0% at one operating point under replay, generative deepfake, and voice conversion together.

## Ledger entries written

E-ACA-040 … E-ACA-052 (13 rows). E-ACA-053 through E-ACA-059 are unused. Rows live in `LEDGER-ROWS.md` in this directory. The shared ledger was not edited.

## Answer in one paragraph

Opus is the only one of the three named codecs for which an opened paper prints a false-positive rate and a true-positive rate on an acoustic watermark. That result is O’Reilly et al. 2025 at Opus 24 kbps: false-positive rate fixed at 1%, true-positive rate 1.00 for four watermarks and 0.79 for a fifth (E-ACA-040). Narrowband PSTN appears as G.711 and G.729 bit detection rate, 100% and about 90% on 12 sentences (E-ACA-043), which is not a false-accept or false-reject rate. AMR-WB appears as a modem channel whose opened text prints no false-accept or false-reject rate (E-ACA-052). Every opened challenge-response paper (D-CAPTCHA, D-CAPTCHA++, PITCH) evaluates voice conversion on recordings that were not passed through AMR-WB, Opus, or a PSTN codec. D-CAPTCHA++ states that omission directly (E-ACA-047).

## Ranked findings

Citation counts were not retrieved. The Semantic Scholar graph API returned HTTP 429 on 2026-11-24, so citations per month and influence are not computed. Rank is by how close the opened result is to a false-accept and false-reject pair after one of the three named codecs.

| # | Paper / report | Venue | Date | Citations | Cit/mo | Influence | Relevance to scope | Ledger ID |
|---|---|---|---|---|---|---|---|---|
| 1 | Deep Audio Watermarks are Shallow | arXiv:2504.10782 | 2025-04-15 | not retrieved | — | not computed | Opus 24 kbps, TPR at a fixed 1% FPR. No AMR-WB, no PSTN, no replay, no voice conversion. | E-ACA-040 |
| 2 | AudioMarkBench | NeurIPS 2024 D&B | arXiv 2024-06 | not retrieved | — | not computed | Opus sweep; very high FNR at a clean-audio threshold. Per-bitrate FNR is a figure, not a printed number. | E-ACA-041 |
| 3 | StreamMark | arXiv:2604.11917 | 2026-04 | not retrieved | — | not computed | Opus 60 ms frames, message accuracy 0.99 / 0.57 / 0.85. Not FAR/FRR. FreeVC is a separate table. | E-ACA-042 |
| 4 | Formant-enhancement watermark | Interspeech 2014 | 2014-09 | not retrieved | — | not computed | G.711 BDR 100%, G.729 BDR about 90%, n=12. Not FAR/FRR. | E-ACA-043 |
| 5 | Formant watermark, journal | JIHMSP 2015 | 2015-11 | not retrieved | — | not computed | Same BDR; tandem G.729 can be mistaken for tampering. Same lab as #4. | E-ACA-044 |
| 6 | LSF tamper watermark | Math. Problems in Engineering 2019 | 2019 | not retrieved | — | not computed | G.711 and G.729 tested; blind BDR “dramatically reduced”; numbers are in a figure. | E-ACA-045 |
| 7 | D-CAPTCHA | ASIA CCS 2023 | 2023-07 | not retrieved | — | not computed | Challenge-response plus voice conversion. No telephony codec. Printed FPR string has no unit. | E-ACA-046 |
| 8 | D-CAPTCHA++ | arXiv:2409.07390 | 2024-09-11 | not retrieved | — | not computed | States the attack was not run over telephony, because a codec may strip the perturbation. | E-ACA-047 |
| 9 | PITCH | arXiv:2402.18085 v4 | 2025-05-26 | not retrieved | — | not computed | Challenge-response AUROC 88.7% against three voice-conversion models. No codec, no FAR/FRR. | E-ACA-048 |
| 10 | CRAW | arXiv:2609.03107 | 2026-09 | not retrieved | — | not computed | F1 at 1% FPR on neural codecs and MP3. No AMR-WB, Opus, or PSTN. | E-ACA-049 |
| 11 | Parametric watermark detector | ICME 2005 | 2005 | not retrieved | — | not computed | False-alarm rate under additive noise. No telephony codec. | E-ACA-050 |
| 12 | SpeechVerifier | arXiv:2505.23821 | 2025-05-28 | not retrieved | — | not computed | 100% TPR and 0% FPR on MP3 and 8 kHz resampling. Opus is named and not applied. | E-ACA-051 |
| 13 | VoLTE ASK modem | U.P.B. Sci. Bull. 2015 | 2015 | not retrieved | — | not computed | AMR-WB channel. BER is in a figure. No printed FAR/FRR. | E-ACA-052 |

Venue multipliers from the scout skill, recorded so a later citation lookup can finish the influence score: NeurIPS 1.3 (E-ACA-041); ASIA CCS, Interspeech, ICME, and the journals 1.0 (E-ACA-043, E-ACA-044, E-ACA-045, E-ACA-046, E-ACA-050, E-ACA-052); arXiv preprints 0.6 until traction is counted (E-ACA-040, E-ACA-042, E-ACA-047, E-ACA-048, E-ACA-049, E-ACA-051).

## Technique → OSS pairings

No pairing is selected. This scout does not choose a watermark, a liveness test, or an open-source stack.

| Technique (paper) | Applies to (OSS project) | Expected gain | Implementation difficulty | Evidence |
|---|---|---|---|---|
| None selected | — | — | — | K2 is UNTESTED. Selecting a scheme from these rows would treat a 1% false-positive watermark test, a bit detection rate, or an AUROC as the Audio Signature operating point. |

## Negative results / known failure modes

| Finding | Impacts which FR/NFR | Severity | Ledger ID |
|---|---|---|---|
| The only opened false-positive / true-positive pair after a named codec (Opus 24 kbps) is measured at a 1% false-positive rate. That operating point is 1 in 100, not 1 in 100,000. | Audio Signature FAR < 0.001% and FRR < 1% together (K2) | The published Opus detection point does not meet the false-accept line, and it covers none of the three K2 attacks. | E-ACA-040 |
| With the threshold frozen on clean audio, AudioMarkBench’s prose says Opus drives false-negative rate very high while quality (ViSQOL ≥ 3) holds. The per-bitrate number is in a figure. | Watermark survival after Opus | A clean-audio threshold does not transfer to the Opus sweep. | E-ACA-041 |
| In one 16-bit message-recovery table, AudioSeal’s Opus accuracy is 0.57 while Timbre and StreamMark print 0.99. | Acoustic watermark after Opus | Message recovery and presence detection are different metrics. E-ACA-040’s AudioSeal presence detection at Opus 24 kbps is a different setup. | E-ACA-042 |
| One G.729 encode/decode leaves formant-watermark bit detection around 90% (n=12). Two G.729 passes drop bit detection with no tamper and can be read as tampering. | Narrowband CELP path, tandem transcode | A PSTN or VoIP path that transcodes twice is outside the single-pass BDR. | E-ACA-043, E-ACA-044 |
| Blind LSF watermark detection after G.711 and after G.729 is described as dramatically reduced. Nonblind detection uses the original signal. | Any watermark that must be read without the original | A nonblind 100% bit detection rate is not an operating point for a phone call. | E-ACA-045 |
| D-CAPTCHA’s best printed challenge equal-error rate in Table 3 is 0.071, with no codec in the path. | Challenge-response liveness on a phone call | An equal-error rate near 7% is not FAR < 0.001% at FRR < 1%, and it is not a codec result. | E-ACA-046 |
| D-CAPTCHA++ states the adversarial attack was not evaluated over the telephony network, because codec compression and static interference might remove the perturbation. | Challenge-response over AMR-WB, Opus, or PSTN | The authors mark the codec path as unmeasured. | E-ACA-047 |
| PITCH’s 88.7% figure is an AUROC on desktop and smartphone recordings, against voice conversion, with no codec condition and no false-accept or false-reject pair. | Challenge-response on a carrier call | AUROC is not the K2 pair, and the channel is not the codec. | E-ACA-048 |
| Codec-robust watermark papers that post-date the Opus result (CRAW) measure neural codecs and MP3. The telephony codecs named in the question are absent. | AMR-WB and narrowband PSTN watermark detection | A neural-codec F1 does not measure AMR-WB or G.711. | E-ACA-049 |
| The opened parametric detector that prints a false-alarm rate near 10^−6 does so under additive noise, not after a codec. | Low false-alarm watermark claims | A noise-channel false-alarm rate is not a telephony result. | E-ACA-050 |
| SpeechVerifier’s 100% true-positive and 0% false-positive rates are on MP3 at 128 kbps and on resampling to 8 kHz. The introduction names Opus; the appendix does not apply it. | Opus / AMR-WB / G.711 watermark detection | An 8 kHz resample is not G.711 and not AMR-WB. | E-ACA-051 |
| The opened AMR-WB experiment is a data modem. The text layer prints no false-accept rate and no false-reject rate. | AMR-WB acoustic watermark or liveness | AMR-WB modem bit error is a different measurement. | E-ACA-052 |

## Reception and replication

No Hacker News, Reddit, or practitioner-blog thread was opened for these papers on 2026-11-24. Replication status below is what the opened papers themselves say.

| Paper | Community signal | Replication status | Ledger ID |
|---|---|---|---|
| O’Reilly et al. 2025 | Not opened outside the paper | Re-measures AudioSeal, WavMark, Timbre, and MaskMark. Threshold policy differs from AudioMarkBench. | E-ACA-040 |
| AudioMarkBench | Not opened outside the paper | Benchmark of released watermark checkpoints. Opus FNR is plotted, not tabled. | E-ACA-041 |
| StreamMark | Not opened outside the paper | Re-measures AudioSeal and Timbre on the authors’ Opus setting. | E-ACA-042 |
| Wang and Unoki 2014 / 2015 | Not opened outside the papers | Journal paper repeats the conference bit detection rates and adds the tandem G.729 case. Same laboratory. | E-ACA-043, E-ACA-044 |
| D-CAPTCHA / D-CAPTCHA++ / PITCH | Not opened outside the papers | PITCH re-tests a D-CAPTCHA-style challenge set against FREE-VC and reports some of those tasks as weaker. That comparison is inside E-ACA-048. It is still not a codec test. | E-ACA-046, E-ACA-047, E-ACA-048 |

## Attacks with no opened paper

These are the attack-and-codec pairs for which this scout opened no paper that reports a false-accept rate and a false-reject rate.

| Attack | AMR-WB | Opus | Narrowband PSTN (G.711 or G.729) |
|---|---|---|---|
| Challenge-response liveness, false-accept and false-reject | No paper opened | No paper opened | No paper opened |
| Acoustic watermark, false-accept and false-reject | No paper opened | E-ACA-040 reports the pair at a 1% false-positive rate. No other opened paper does. | No paper opened. Opened PSTN papers report bit detection rate. |
| Replay, on either scheme | No paper opened | No paper opened | No paper opened |
| Voice conversion, on either scheme, with false-accept and false-reject | No paper opened | No paper opened. PITCH, D-CAPTCHA, and StreamMark include voice conversion without this codec, or with a different metric. | No paper opened |
| Replay and voice conversion and generative deepfake together | No paper opened | No paper opened | No paper opened |

## Dead ends

Queries and papers that were opened and then kept out of the ledger, so a retry does not repeat them. Full query log is `QUERIES.md`.

- SVeritas (arXiv:2509.17091) reports speaker-verification equal-error rate under AMR and Opus. That is academic-1’s speaker-verification question. It was not given an E-ACA-04x row.
- ASVspoof replay countermeasures and the Oakland 2023 over-telephony countermeasure attack are passive spoofing countermeasures, not challenge-response liveness and not acoustic watermarks.
- AMR pitch-delay and pulse-pair steganalysis detect bits hidden in the AMR bitstream. That is not an acoustic watermark measured after decode.
- Phase-feature detection of double-compressed AMR speech is codec forensics, not a watermark detector and not a liveness test.
- 3GPP TR 26.976 characterizes AMR-WB speech quality. It has no watermark detector and no liveness detector.
- VoiceLive, VoiceGesture, and MagLive report on-device replay liveness, including false-accept and equal-error figures, on a handset microphone. They are not challenge-response protocols and they do not pass AMR-WB, Opus, or PSTN. They were left out so this scout does not launder an on-device equal-error rate into a codec result.
- AudioAuth (IEEE DOI 10.1109/tbiom.2026.3679274) returned an abstract in search. The PDF was not opened. It is not a row.
- The Journey.ai deepfake-authentication white paper was opened and is a vendor page (T4). It says presentation-attack detection should be measured in-channel and it prints no false-accept or false-reject rate. It is not a row.
- ITU-T X.1097 was opened. It describes speaker recognition over telecommunications and prints no codec-condition false-accept or false-reject pair for a challenge-response test or a watermark.
