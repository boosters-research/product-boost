# Queries — academic-scout-3

**Run:** 2026-11-24-myai-myagent
**Date retrieved:** 2026-11-24
**Tool:** web search only. Each paper that became a ledger row was opened as a PDF or full HTML page on this date. URLs are in `LEDGER-ROWS.md`.

Three framings, each with `pdf` in the query or in the opened target: insider (codec and detector vocabulary), buyer (phone-call / banking authentication), skeptic (the scheme fails, or the codec path was never measured).

## Insider

| # | Query | Outcome |
|---|---|---|
| I1 | `challenge-response voice liveness detection AMR-WB OR Opus OR PSTN false accept false reject pdf` | Opened PITCH (E-ACA-048), VoiceLive, and VoiceGesture. SVeritas is speaker verification under AMR and Opus; left to academic-1. No challenge-response paper in this hit list had a codec false-accept/false-reject pair. |
| I2 | `acoustic watermark speech codec AMR-WB detection rate false positive pdf` | Opened AudioMarkBench (E-ACA-041), CRAW (E-ACA-049), and the MaskMark/O’Reilly watermark PDF. AMR hits were steganalysis of the AMR bitstream, not an acoustic watermark after decode. Those steganalysis papers were not rowed. |
| I3 | `"AMR-WB" speech watermark detection OR "bit error" OR BER pdf` | Opened Ciornei et al. 2015 (E-ACA-052) and 3GPP TR 26.976. TR 26.976 is speech-quality characterization, not a detector. No watermark false-accept rate after AMR-WB. |
| I4 | `AudioSeal WavMark Opus "false negative" OR FNR OR "TPR" watermark pdf arxiv` | Opened O’Reilly et al. 2025 (E-ACA-040), SpeechVerifier (E-ACA-051), and VoxWatermark. VoxWatermark lists Opus as a perturbation and the opened text does not print an Opus false-positive or false-negative rate, so it is not a row. |
| I5 | `"watermark" speech "AMR-WB" OR "G.711" OR "G.729" "false alarm" OR "bit error rate" OR "detection rate" pdf` | Opened Wang and Unoki, Interspeech 2014 (E-ACA-043), the 2015 journal version (E-ACA-044), the 2019 LSF paper (E-ACA-045), the EUSIPCO 2014 formant paper (same lab, same method, not a separate row), and Gurijala and Deller, ICME 2005 (E-ACA-050). |
| I6 | `"AMR-WB" OR "AMR WB" watermark speech "after" detection OR robustness OR "bit error" -steganalysis pdf` | Returned RFC 4352, AMR-WB error concealment, and TR 26.976 again. No acoustic-watermark detector after AMR-WB. |

## Buyer

| # | Query | Outcome |
|---|---|---|
| B1 | `voice biometric liveness phone call codec false acceptance watermark banking pdf` | Opened the Oakland 2023 over-telephony countermeasure paper (passive countermeasure; not rowed; academic-1 territory if it is an ASV result), ITU-T X.1097 (no codec FAR/FRR pair; not rowed), and an AudioAuth DOI abstract that was not opened as a PDF (not rowed). |
| B2 | `"challenge-response" voice liveness OR watermark "G.711" OR "G.729" OR "AMR-WB" OR Opus telephony pdf` | Opened the Journey.ai vendor white paper (T4, no rates, not rowed), an IRJET essay with no rates, an Opus Research vendor PDF with no codec rates, a caller-ID verification paper (DTMF and G.711, not a liveness or watermark detector), and a 2010 teleconference watermark protocol with no measured rates. None became a row. |
| B3 | `D-CAPTCHA deepfake challenge-response audio arxiv pdf Yasur codec OR Opus OR telephony` | Opened Yasur et al., ASIA CCS 2023 (E-ACA-046) and Nguyen-Le et al., arXiv:2409.07390 (E-ACA-047). |

## Skeptic

| # | Query | Outcome |
|---|---|---|
| S1 | `audio watermark destroyed OR fails AMR-WB OR narrowband OR Opus speech detection pdf` | Opened the NeurIPS AudioMarkBench PDF (E-ACA-041), O’Reilly et al. (E-ACA-040), VoxWatermark, a fragility-attack preprint, and an MDPI paper on double-compressed AMR detection. The MDPI paper is codec forensics, not a watermark detector, and was not rowed. |
| S2 | `"voice liveness" challenge-response replay "equal error" smartphone NOT codec pdf site:arxiv.org` | Opened VoiceGesture, VoiceLive, and MagLive. All three are on-device replay liveness with equal-error or false-accept figures and no telephony codec. They were not rowed, so an on-device equal-error rate is not reused as a codec result. ASVspoof replay and ReMASC were in the same list and were left as academic-1 material. |
| S3 | `"challenge-response" deepfake audio call detection codec OR telephony OR "not evaluated" AUROC pdf arxiv` | Pointed back at PITCH (E-ACA-048) and at the D-CAPTCHA++ limitation that the telephony path was not evaluated (E-ACA-047). |

## Follow-up opens that were not separate queries

These pages were opened from citations or secondary links inside the queries above.

| Page | Use |
|---|---|
| https://arxiv.org/html/2604.11917 StreamMark | Row E-ACA-042. Found while reading a citing page from the skeptic/watermark cluster. |
| https://arxiv.org/pdf/2406.06979v2.pdf AudioMarkBench arXiv | Same paper as the NeurIPS PDF used for E-ACA-041. |
| https://arxiv.org/html/2504.10782 O’Reilly HTML | Same paper as the PDF used for E-ACA-040. Used to check the TPR@1%FPR definition against the table caption. |
| https://www.eurasip.org/Proceedings/Eusipco/Eusipco2014/HTML/papers/1569924405.pdf | Same formant method and same laboratory as E-ACA-043. Not a second independent row. |
| Semantic Scholar graph API for arXiv 2406.06979, 2504.10782, 2301.03064, 2402.18085, 2409.07390, and a formant-watermark search | HTTP 429. Citation counts were not retrieved. Influence was not computed. |

## Do not repeat

- Do not score SVeritas, ASVspoof, or the Oakland 2023 telephony countermeasure paper inside E-ACA-040–059. Those are speaker-verification or passive-countermeasure results.
- Do not treat AMR bitstream steganalysis as an acoustic watermark after decode.
- Do not treat VoiceLive, VoiceGesture, or MagLive handset equal-error rates as post-codec rates.
- Do not convert StreamMark message accuracy, Interspeech bit detection rate, PITCH AUROC, or Ciornei modem bit error into a false-accept rate.
- Do not mark K2 clear from any of these rows.
