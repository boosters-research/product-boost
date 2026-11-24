# OSS Scout retry 1 — operating points and NeMo Speech CVEs

**Agent:** g1r1-oss
**Run:** 2026-11-24-myai-myagent
**Retrieved:** 2026-11-24
**Units retried:** E-OSS-022, E-OSS-023, E-OSS-024, E-OSS-026, E-OSS-029, E-OSS-030, E-OSS-033, E-OSS-037, E-OSS-038

## Ledger entries written

E-OSS-040 through E-OSS-052. E-OSS-053 and E-OSS-054 were left unused. Shared `ledger/EVIDENCE.md` was not edited. K2 was not marked.

An equal-error rate was left as an equal-error rate. A missing FAR/FRR pair was recorded as a miss. A miss was not treated as a kill.

## What each retry opened

| Unit retried | New ID | What the new source prints | K2 pair |
|---|---|---|---|
| E-OSS-022 | E-OSS-040 | Journal article, Multimedia Tools and Applications, 3 December 2015. Replay FAR 78.36% male and 73.14% female for HMM-UBM at the baseline equal-error threshold (baseline EER 2.92% and 2.39%). Voice conversion is a later case study. Text-to-speech is not in that point. | No |
| E-OSS-023 | E-OSS-041 | Same journal. Replay FARs at that threshold are 65.28% to 78.36%. Baseline EERs that set the threshold are 2.39% to 4.01%. No row has FRR under 1% and FAR under 0.001%. | No |
| E-OSS-024 | E-OSS-042 | ICASSP 2022 AASIST PDF. Best single model min t-DCF 0.0275 and EER 0.83%. No FAR column and no FRR column. | No |
| E-OSS-026 | E-OSS-043 | WeSpeaker arXiv PDF, 1 November 2022. ResNet293 r-vector EER 0.447% and minDCF 0.043 on voxceleb1_O. The paper prints only EER and minDCF. | No |
| E-OSS-029 | E-OSS-044 | Applied Sciences PDF, 6 February 2024. TitaNet-Large FAR 1.91% and FRR 1.91% on 4,500 YouTube pairs. No replay, TTS, or voice conversion in that experiment. | No |
| E-OSS-030 | E-OSS-045 | NVIDIA NGC page, updated 4 April 2023. 25.3M parameters and 0.68% EER. The 23M / 0.66 EER% line is not on this page, and the page has no FAR/FRR pair. | No |
| E-OSS-033 | E-OSS-046 | Computer Speech and Language version. Table 6 is EER only: A16 64.52%, A17 3.92%. No numeric FAR/FRR pair. | No |
| E-OSS-038 | E-OSS-047 | wav2vec 2.0 paper at arXiv:2202.12233. EER and min t-DCF only. The string 38.57 and the name CD-ADD are not in the PDF, and the PDF gives no run date for that arena figure. | No |
| E-OSS-037 | E-OSS-048 to E-OSS-052 | NVD CVE 2.0 records exist for all five IDs. Each CVSS 3.1 object is Secondary, source psirt@nvidia.com. No Primary CVSS object was in the JSON. | Not a K2 measurement |

## NVD records opened for E-OSS-037

The vendor bulletin was not re-used as the source. The detail HTML for CVE-2026-65179 timed out. The NVD CVE 2.0 API returned `totalResults: 1` for each ID.

| ID | CVE | Published | Status | Secondary CVSS 3.1 | Vector | CWE |
|---|---|---|---|---|---|---|
| E-OSS-048 | CVE-2026-65179 | 2026-09-22 | Analyzed | 8.8 HIGH | AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | CWE-502 |
| E-OSS-049 | CVE-2026-24267 | 2026-09-22 | Analyzed | 7.8 HIGH | AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | CWE-502 |
| E-OSS-050 | CVE-2026-24239 | 2026-09-22 | Analyzed | 7.8 HIGH | AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | CWE-502 |
| E-OSS-051 | CVE-2026-65111 | 2026-09-22 | Analyzed | 7.8 HIGH | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | CWE-77 |
| E-OSS-052 | CVE-2026-65178 | 2026-09-22 | Analyzed | 7.8 HIGH | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | CWE-502 |

All five say NeMo Speech versions 0.0 to 2.9, with the CPE range ending before 3.0.0. The scores above are the Secondary objects in the NVD JSON. This retry did not add an NVD-assigned Primary score.

## Candidate register

This retry did not re-score a project for adoption. READMEs, issue lists, and the last three months of commits were not re-read, so no viability mean is reported and no project is recommended as a core dependency.

| Project | Capability covered | Stars | Bus | Recency | License | Sec | Fork | Release | Viability | Ledger ID |
|---|---|---|---|---|---|---|---|---|---|---|
| — | Not re-scored on this retry | — | — | — | — | — | — | — | — | — |

## Coverage map

| Asked measurement | Covered by | Coverage | Gap |
|---|---|---|---|
| Replay FAR and FRR at one threshold, and whether TTS and voice conversion share that point | E-OSS-040 | Replay FAR at the baseline equal-error threshold is printed. Voice conversion is a different case study. Text-to-speech is absent from the point. | The article does not print a replay-condition FRR separate from the baseline EER that defines the threshold. |
| Replay row with FRR under 1% and FAR under 0.001% | E-OSS-041 | The opened journal rows miss both bars. | No such row was found. The miss is not a kill. |
| AASIST FAR and FRR | E-OSS-042 | The paper prints EER and min t-DCF. | No FAR/FRR pair. 0.83% stays an EER. |
| r-vector FAR and FRR | E-OSS-043 | The paper prints EER and minDCF. | No FAR/FRR pair. |
| TitaNet FAR and FRR after 2022 | E-OSS-044 | FAR 1.91% and FRR 1.91% on 6 February 2024. | Same-speaker versus different-speaker YouTube clips. No replay, TTS, or voice conversion. |
| 23M / 0.66 EER% FAR and FRR off the model card | E-OSS-045 | The opened NGC page does not carry that figure. | No FAR/FRR pair for 0.66 was found on a primary NVIDIA page. |
| A16 and A17 FAR and FRR in the journal version | E-OSS-046 | The journal version still prints EER. | No FAR/FRR pair. |
| Run date and FAR/FRR for the 38.57% CD-ADD EER | E-OSS-047 | The cited paper does not contain that figure. | No run date and no FAR/FRR pair in the opened paper. |
| NVD entries for the five bulletin CVEs | E-OSS-048 to E-OSS-052 | All five IDs have NVD records. | Detail HTML timed out. Scores in the API are CNA Secondary scores. |

## Composition candidates

No stack is proposed. The opened operating points do not supply FAR under 0.001% and FRR under 1% at one threshold under replay, text-to-speech, and voice conversion together.

| Stack | Components | Integration seams | Seam risk | Net build saved (est.) |
|---|---|---|---|---|
| — | None recommended from this retry | — | — | — |

## License red flags

No license was re-opened on this retry.

| Project | License | Commercial constraint | Escalate at gate |
|---|---|---|---|
| — | — | — | — |

## Rejected candidates

Nothing new was rejected as a dependency. The rate rows below are rejected as a K2 operating point because the printed numbers are not FAR under 0.001% and FRR under 1% under the three attack classes together.

| Project or paper | Why it is not a K2 point | Ledger ID |
|---|---|---|
| Wu and Li 2015, replay at the baseline EER threshold | Replay FAR 65.28% to 78.36%, with baseline EER 2.39% to 4.01%. Voice conversion is separate. Text-to-speech is not in the point. | E-OSS-040, E-OSS-041 |
| AASIST, ICASSP 2022 | EER 0.83% and min t-DCF 0.0275. No FAR/FRR pair. | E-OSS-042 |
| WeSpeaker ResNet293 r-vector | EER 0.447% and minDCF 0.043. No FAR/FRR pair. | E-OSS-043 |
| TitaNet-Large, Applied Sciences 2024 | FAR 1.91% and FRR 1.91% on YouTube pairs, with no replay, TTS, or voice conversion. | E-OSS-044 |
| NGC TitaNet-L | 0.68% EER for the 25.3M model. No FAR/FRR pair, and not the 23M / 0.66 line. | E-OSS-045 |
| ASVspoof 2019, Computer Speech and Language | A16 EER 64.52% and A17 EER 3.92%. No FAR/FRR pair. | E-OSS-046 |
| Tak et al. wav2vec 2.0 PDF | EER and min t-DCF. The 38.57% CD-ADD figure is not in the paper. | E-OSS-047 |
