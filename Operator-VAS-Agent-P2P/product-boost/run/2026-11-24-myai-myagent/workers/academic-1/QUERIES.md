# Queries — academic-scout-1 — RQ-1

**Run:** 2026-11-24-myai-myagent
**Retrieved:** 2026-11-24
**Question:** Does any published speaker-verification plus anti-spoof evaluation report FAR < 0.001% and FRR < 1.0% at the same operating point under replay, TTS/generative deepfake, and voice conversion together?

Every string below was sent to web search on 2026-11-24. Rows in `LEDGER-ROWS.md` use only URLs whose full text was retrieved that day. Snippets that were not retrieved as a document produced no row.

## Insider

| # | Query | Outcome |
|---|---|---|
| Q1 | `speaker verification anti-spoof FAR FRR operating point replay TTS voice conversion pdf` | Opened vulnerability papers. Usable joint point: Alegre et al., FRR fixed at 2.98% with spoof FARs of 80.86% (replay), 84.67% (voice conversion), and 30.00% (speech synthesis), no countermeasure. No K2 pass. → E-ACA-007. |
| Q2 | `ASVspoof SASV "false acceptance" "false rejection" spoofing-aware speaker verification pdf` | Opened SASV 2022 and ASVspoof 5. Primary metrics are SASV-EER, min a-DCF, and t-EER. Lowest opened joint equal-error point is FAR = FRR = 0.13% on ASVspoof 2019 logical access, which excludes replay. → E-ACA-001, E-ACA-002, E-ACA-003. |
| Q3 | `APCER BPCER voice spoofing replay TTS voice conversion speaker verification pdf` | Opened Korshunov and Marcel 2017. Best cascaded presentation-attack cell is IAPMR 1.52% with FNMR 8.05% and FMR 9.45%. Presentation attacks only. → E-ACA-005. |
| Q4 | `"false acceptance rate" "0.001%" OR "0.01%" OR "10^{-5}" speaker verification spoof replay deepfake pdf` | Opened the 2026 bypass study and Sahidullah et al. 2016. No printed FAR below 0.001% paired with FRR below 1.0%. → E-ACA-004, E-ACA-008. |
| Q5 | `spoofing-aware speaker verification SASV-EER 2024 2025 2026 evaluation results pdf` | Opened later SASV-EER reports (2.18%, 1.30%, 2.08%) and the VLSP 2025 challenge. The later numbers are equal-error rates, not a FAR of 0.001%. The VLSP protocol is the opened evaluation whose test material contains replay, voice conversion, and TTS together. → E-ACA-010. |

## Buyer

| # | Query | Outcome |
|---|---|---|
| Q6 | `voice biometric bank FAR 0.001% FRR deepfake replay voice conversion evaluation pdf` | Opened the 2026 bypass study (also Q4) and the Alegre PDF (also Q1). No bank evaluation with both rates under the three attacks. |
| Q7 | `voice biometric "false acceptance" "false rejection" banking Pindrop OR Nuance OR Phonexia evaluation report pdf` | Opened the Naval Postgraduate School thesis: FRR 2.91% and FAR 1.2% on 411 attempts, no spoof classes. Also opened the 2013 MOBIO speaker-recognition evaluation, which reports EER and HTER for zero-effort mobile verification and is not an anti-spoof result, so it has no ledger row. Pindrop’s “Testing Voice Biometric Security Against AI Deepfakes” page and the U.S. Bank 2014 slide deck appeared as search snippets only and were not retrieved as documents. No rows for those two. → E-ACA-014. |

## Skeptic

| # | Query | Outcome |
|---|---|---|
| Q8 | `"speaker verification" deepfake "equal error rate" does not report FAR FRR operating point limitations pdf` | Opened the ASVspoof 2021 evaluation plan. Logical access and physical access are separate tasks. EER is described as legacy because ISO/IEC deprecates it for this testing. → E-ACA-012. |
| Q9 | `speech deepfake detector threshold transfer FRR FAR HTER "does not" EER deployment pdf` | Opened the June 2026 threshold-transfer audit: in-domain EER 0.21%; transferred In-the-Wild point FRR 78.7% and FAR 0.3%. Countermeasure only. Also opened the August 2026 industry–academia deepfake-detection report. Its numeric codec examples are outside this scout’s question and were not given ledger rows. → E-ACA-009. |
| Q10 | `"no" voice biometric system achieves false acceptance deepfake replay "voice conversion" same threshold pdf` | Opened Kucur Ergunay et al., BTAS 2015. Same thresholds, all three attack families, spoof false-accept rates from 11.1% to 97.0%, no countermeasure. The query did not return a paper that states the K2 sentence in words. → E-ACA-006. |
| Q11 | `"1 in 100,000" OR "one in 100,000" voice biometric OR "speaker verification" false accept OR "false acceptance" pdf` | Opened Sholokhov et al. 2019. The 100,000 figure is a closest-impostor population, and the reported false-alarm probability at that population is 95–98% at minDCF1, with no spoof trials. Also opened Campbell’s 1997 speaker-recognition tutorial; it does not report this operating point, so it has no row. → E-ACA-013. |
| Q12 | `"false acceptance rate of 0.001%" OR "FAR of 0.001%" OR "FAR < 0.001%" speaker "false rejection" spoof pdf` | Opened Martinek et al., Interspeech 2025. They name FAR = 0.001% as a threshold at which FRR was computed. The retrieved text has no numeric FRR at that threshold. Synthetic attacks in the printed table are two TTS systems. Replay and voice conversion are absent. → E-ACA-011. |

## Not a research query

| # | Query | Outcome |
|---|---|---|
| Q13 | `SASV 2022 Jung Interspeech "cited by" spoofing-aware speaker verification` | Used only to look for a citation count. One retrieved index page said the Interspeech 2022 paper was cited by 4 works. Another retrieved page said cited by 56. The count is not used. Influence is unscored. |

## Nothing usable for the K2 pair

These strings did not return a document that prints FAR < 0.001% and FRR < 1.0% at one operating point under replay, TTS/generative deepfake, and voice conversion together.

- Q6 — no bank report with that pair.
- Q10 — high spoof false-accept rates, no statement of the K2 pair, and no countermeasure result at that pair.
- Q11 — no per-trial false-accept rate of 1 in 100,000.
- Q12 — the only paper that names FAR = 0.001% does not print the FRR, and its attacks are TTS only.
- Q7, for the Pindrop article `https://www.pindrop.com/resources/article/testing-voice-biometric-security-against-ai-deepfakes` and the U.S. Bank deck `https://opusresearch.net/pdfs/USBank_BethGallagher_VBCSF2014.pdf` — search snippets only. Not opened. Not cited.

No query returned an empty result page. The dead end is the absence of the joint rate, not an empty search.
