# Queries — g1r1-oss

**Run:** 2026-11-24-myai-myagent
**Retrieved:** 2026-11-24
**Agent:** g1r1-oss
**Rule:** Queries for the retry of E-OSS-022, E-OSS-023, E-OSS-024, E-OSS-026, E-OSS-029, E-OSS-030, E-OSS-033, E-OSS-037, and E-OSS-038. Strings differ from the exhausted pages named in the dispatch. Dead ends are listed so the next retry can change them.

Context.dev search was not available: the MCP server asked for interactive authentication, which this worker cannot complete. Searches and fetches below used the web search and page-fetch tools.

## Queries and fetches that produced a row

| # | Unit | Framing | Query or fetch | Result used |
|---|---|---|---|---|
| 1 | E-OSS-022 | Insider, journal | `replay attack speaker verification "false acceptance rate" "false rejection rate" journal pdf 2024 doi anti-spoofing` | Opened Wu and Li, Multimedia Tools and Applications, DOI 10.1007/s11042-015-3080-9. Replay FAR at the baseline EER threshold. E-OSS-040. |
| 2 | E-OSS-022 | Journal PDF | `https://link.springer.com/content/pdf/10.1007/s11042-015-3080-9.pdf` | HTTP 302. The article text from the DOI page was used instead. |
| 3 | E-OSS-022 | Second PDF, venue not a journal on the pages read | `https://www.eurecom.fr/publication/4441/download/mm-publi-4441.pdf` | Table 3 SFAR with the caption that FRR is set to the baseline EER. Used only as a second miss in E-OSS-041. The PDF does not name a journal. |
| 4 | E-OSS-023 | Skeptic, the joint bar | `replay "false rejection rate" under 1% "false acceptance rate" 0.001% OR "10^-5" speaker verification countermeasure evaluation table pdf 2024 2025` | APSIPA 2025 PDF prints EER, including 8.40% on ASVspoof 2017, and does not print a FAR/FRR pair. No opened replay row met both bars. E-OSS-041. |
| 5 | E-OSS-024 | Paper PDF | `AASIST: Audio Anti-Spoofing Jung ICASSP 2022 pdf FAR FRR t-DCF EER arxiv 2110.01200` then `https://mm.kaist.ac.kr/pubs/pdfs/jung22c.pdf` | ICASSP 2022 PDF. Metrics are min t-DCF and EER. E-OSS-042. The arXiv PDF at `https://arxiv.org/pdf/2110.01200` was also opened and agrees; the IEEE PDF is the cited source. |
| 6 | E-OSS-026 | 2022 paper | `Wespeaker "r-vector" ResNet293 0.447 EER paper pdf FAR FRR VoxCeleb Wang 2210.17016` then `https://arxiv.org/pdf/2210.17016` | v2 PDF dated 1 November 2022. Table 1 is EER and minDCF. E-OSS-043. |
| 7 | E-OSS-029 | Post-2022 paper | `TitaNet "false acceptance" OR FAR "false rejection" OR FRR speaker verification 2023 OR 2024 OR 2025 pdf -2110.04410` then `https://www.mdpi.com/2076-3417/14/4/1329/pdf` | Applied Sciences PDF, published 6 February 2024, Table 3 FAR and FRR. E-OSS-044. |
| 8 | E-OSS-030 | Primary page other than the card | `nvidia titanet_large 23M 0.66 EER% VoxCeleb speakerverification documentation FAR FRR site:docs.nvidia.com OR site:catalog.ngc.nvidia.com OR site:github.com/NVIDIA/NeMo` then `https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/titanet_large` | NGC page, updated 4 April 2023, 25.3M and 0.68% EER. E-OSS-045. |
| 9 | E-OSS-030 | Skeptic, the 0.66 figure off the card | `"0.66" TitaNet site:docs.nvidia.com OR site:github.com/NVIDIA/NeMo FAR OR FRR OR "false rejection"` | No results. Recorded in E-OSS-045 as the empty primary-page search. |
| 10 | E-OSS-033 | Journal version | `ASVspoof 2019 "Computer Speech and Language" A16 A17 EER pdf doi 10.1016/j.csl.2020.101114` then `https://aaltodoc.aalto.fi/server/api/core/bitstreams/d11fa80a-7e06-4c57-8328-12b84dcabfd3/content` | Peer-reviewed CSL version. Table 6 is EER only. E-OSS-046. |
| 11 | E-OSS-038 | Paper behind the card | `"38.57" CD-ADD EER anti-spoofing XLS-R AASIST paper pdf` then `https://arxiv.org/pdf/2202.12233` | The cited wav2vec 2.0 PDF. No 38.57, no CD-ADD, no FAR, no FRR. E-OSS-047. |
| 12 | E-OSS-037 | NVD record | `CVE-2026-65179 CVE-2026-24267 CVE-2026-24239 CVE-2026-65111 CVE-2026-65178 site:nvd.nist.gov` | The NVD search page listed CVE-2026-65179 and CVE-2026-65178 with descriptions and a 22 September 2026 date, and no CVSS score. Scores were taken only from the API records below. |
| 13 | E-OSS-037 | NVD API | `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-65179` | totalResults 1. Secondary CVSS 8.8. E-OSS-048. |
| 14 | E-OSS-037 | NVD API | `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-24267` | totalResults 1. Secondary CVSS 7.8. E-OSS-049. |
| 15 | E-OSS-037 | NVD API | `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-24239` | totalResults 1. Secondary CVSS 7.8. E-OSS-050. |
| 16 | E-OSS-037 | NVD API | `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-65111` | totalResults 1. Secondary CVSS 7.8. E-OSS-051. |
| 17 | E-OSS-037 | NVD API | `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-65178` | totalResults 1. Secondary CVSS 7.8. E-OSS-052. |

## Other fetches opened and not turned into their own row

| URL | Why it was opened | Why it is not its own row |
|---|---|---|
| `https://arxiv.org/pdf/2110.01200` | AASIST preprint, checked against the ICASSP PDF. | Same EER and min t-DCF as E-OSS-042. The IEEE PDF is the source. |
| `https://link.springer.com/content/pdf/10.1186/s13636-024-00328-8.pdf` | 2024 EURASIP journal survey, Gupta, Patil, and Guido. | Defines FAR and FRR and surveys attacks. It does not print a replay FAR/FRR operating point used here. |
| `https://www.apsipa.org/proceedings/2022/APSIPA%202022/TuAM1-6/1570840525.pdf` | Replay-detection proceedings PDF. | Prints EER, including 1.72% and 1.86%. EER was not converted to FAR. |
| `https://www.osti.gov/servlets/purl/1140913` | i-vector paper with FRR 0.00% and FAR 1.74×10^−5 on clean WSJ. | Not replay. Two false accepts in 340×339 impostor tests is about 0.00174%, which is not under 0.001%, and synthetic-speech matched claims accepted are 22.9%. Not used as a K2 row. |
| `https://arxiv.org/pdf/2610.07216` | A 38.57 figure appeared in search. | That 38.57 is an average EER for XLS-R-SLS on FoR across codecs, not the CD-ADD EER. Not used. |
| `https://arxiv.org/pdf/2610.27459` | Another 38.57 figure. | Digital/call EERs of 38.57%/50.31% for XLSR-SLS. Not the CD-ADD figure, and still EER. Not used. |

## Dead ends

| Query or fetch | What happened |
|---|---|
| `https://nvd.nist.gov/vuln/detail/CVE-2026-65179` | Fetch timed out. The NVD CVE 2.0 API for the same ID returned a record. Do not repeat the detail HTML as the only attempt. |
| `https://link.springer.com/content/pdf/10.1007/s11042-015-3080-9.pdf` | HTTP 302. The DOI article text opened. A later retry that needs the PDF bytes should use a different host, not the same Springer content URL. |
| `"0.66" TitaNet site:docs.nvidia.com OR site:github.com/NVIDIA/NeMo FAR OR FRR OR "false rejection"` | No results. The 0.66 / 23M line was not found on those NVIDIA hosts. |
| `"CD-ADD" "38.57" anti-spoof OR deepfake detection paper OR benchmark date` | Hits were the model card and copies of the card. They still label the column EER and do not add a run date or a FAR/FRR pair. The card URL was not re-opened as a source. |
| `CVE-2026-24267 nvd.nist.gov NeMo`, `CVE-2026-24239 nvd.nist.gov`, `CVE-2026-65111 nvd.nist.gov` | Search snippets pointed at OSV, GitHub advisories, Tenable, and the vendor bulletin. Those pages were not used for the score. The NVD API records were opened instead. |
| Context.dev `web-search` | MCP authentication is interactive and was not available in this worker. |

## Not used

- `workers/prior-contaminated/` was not opened and is not cited.
- The VoiceWukong HTML, the AASIST README EER line, the 2022-10-31 WeSpeaker README note, Table 2 of arXiv:2110.04410, the Hugging Face TitaNet card, the ASVspoof 2019 arXiv PDF, the NeMo Speech vendor bulletin, and the W2V2-AASIST model card were not re-opened as sources.
