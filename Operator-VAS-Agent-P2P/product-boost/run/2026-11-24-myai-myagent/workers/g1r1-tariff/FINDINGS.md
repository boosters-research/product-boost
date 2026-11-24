# Market Scout g1r1-tariff — retry 1 of 2

Assignment: re-read E-MKT-023, E-MKT-026, E-MKT-031, E-MKT-032, E-MKT-035, E-MKT-036, E-MKT-037, E-MKT-055, and E-MKT-056 on a source class other than the exhausted page. This pass logs facts. It does not write a scenario, pick a price, convert a currency, or mark K1 or K5.

## Ledger entries written

E-MKT-070 through E-MKT-084.

## Pricing and WTP

| Signal | Amount | Buyer type | Source tier | Ledger ID |
|---|---|---|---|---|
| TRAI, 12 February 2025 notification, regulation 35 insert, explained as a terminating-access-provider charge on the originating access provider | Up to Rs. 0.05 per transactional SMS, and the same ceiling restated for transactional, service, and promotional SMS | Access provider to access provider | T1 | E-MKT-070 |
| Retail price a bank or sender pays per India OTP SMS, in that notification | Unpublished | Bank or enterprise sender | T1 for the absence | E-MKT-071 |
| India inbound voice per minute, in that notification | Unpublished | Caller or enterprise | T1 for the absence | E-MKT-071 |
| Jio Postpaid Plan 449, file named Postpaid-Plans-Sep-2025.pdf | Local voice Free; national-roaming incoming voice Free; local and national SMS Re 1/SMS; international SMS Rs 5/SMS. Personal-use plan. | Consumer mobile subscriber | T3 | E-MKT-072 |
| Enterprise OTP SMS and enterprise inbound voice per minute on that Jio file | Unpublished | Enterprise | T3 for the absence | E-MKT-072 |
| Twilio Form 10-K, year ended 31 December 2025 | $0.095 per second unpublished; $0.07 per minute unpublished. Voice described as fees for minutes of call duration, with no rate. | Filing, not a rate card | T1 | E-MKT-073 |
| Twilio 2025 annual report | ConversationRelay named. $0.07 per minute unpublished. $0.095 per second unpublished. | Filing | T1 | E-MKT-074 |
| Alphabet Form 10-K, year ended 31 December 2025 | $0.001 per second voice price unpublished. $0.001 is stock par value. Dialogflow absent. | Filing | T1 | E-MKT-075 |
| Alphabet Form 10-K, year ended 31 December 2024 | Dialogflow absent. 0.001 per second absent. | Filing | T1 | E-MKT-076 |
| Genesys S.A. Form 20-F, year ended 31 December 2005, and the EDGAR registrant search for Genesys Cloud Services | USD 0.02 per minute for bring-your-own voice unpublished. No customer contract with that rate was opened. | Filing set | T1 | E-MKT-077, E-MKT-078 |

C-MKT-03 stays open. The Rs. 0.05 line is the inter-operator ceiling. It is a separate object from a retail OTP price and from an inbound voice minute. C-MKT-01 stays open. The Twilio filing and the Alphabet filing do not contain the two per-second prices or the $0.07 per minute price, and this pass does not choose between the rate cards.

## Switching and product status

| Trigger event | Decision maker | Incumbent lock-in | Switching cost | Ledger ID |
|---|---|---|---|---|
| Speech SDK 1.47, November 2025, removes speaker recognition support and samples and attributes the removal to service retirement. The notes print no calendar day. | Microsoft Speech service release notes | The 30 September 2025 day is unpublished on this page. | Not a price. | E-MKT-079 |
| Speaker-recognition overview URL and the Azure Updates id for the retirement, fetched 2026-11-24 | The overview text is a general Azure Speech page. The updates page returned an empty list. | The retirement date is unpublished in both fetched texts. | Not a price. | E-MKT-080 |
| HKMA-hosted HSBC account-opening releases from 2018, 2019, 2020, and 2022 | Those releases do not state an end of phone-banking Voice ID. | No regulator notice of the 18 August 2024 ending, and no separate HSBC PDF of it, was opened. | Not a K4 measurement. | E-MKT-081 |

## Sizing arithmetic

No new sizing. The margin and payback figures under retry have no primary table with a sample size.

| Layer | Formula | Inputs (with IDs) | Value | Confidence |
|---|---|---|---|---|
| Voice-AI median gross margin 60%, top quartile 70%, Replicant 74%, CAC payback 9, 5, and 3.8 months | No formula was opened with a sample size. | E-MKT-082, E-MKT-083 | Unpublished as a primary table | 0.38 |
| April 2021 Forrester TEI of Replicant Voice | Named TEI of one customer organization. Payback printed as under 6 months. | E-MKT-082 | Payback under 6 months; ROI 110%; NPV $6.57 million. A count of interviewees is not printed. | 0.38 |
| Gnani.ai gross margin above 80% | No filing states the percent or the year. | E-MKT-084 | Unpublished in the opened filing set | 0.55 |

## Graveyard

| Company/product | What they attempted | Why it ended | Lesson | Ledger ID |
|---|---|---|---|---|
| Azure Speech speaker recognition, as described in the Speech SDK 1.47 notes | Speaker recognition support and samples in the Speech SDK | The November 2025 notes say the removal is due to the service retirement and print no day. | The Q&A date was not re-read. The lifecycle date is unpublished on the Microsoft pages that loaded. | E-MKT-079, E-MKT-080 |
| HSBC Hong Kong phone-banking Voice ID, regulator or PDF notice | A regulator notice or a separate bank PDF that the service ended | The opened HKMA-hosted releases are account-opening announcements and do not contain that ending. | The 18 August 2024 date is unpublished in that regulator-hosted set. | E-MKT-081 |

## CPI input candidates

None. A T4 rate card was not replaced by a filing rate. The Rs. 0.05 ceiling is an inter-operator SMS charge. Jio's printed lines are a personal postpaid plan. Neither is a willingness-to-pay observation for this product, and revealed preference is not in this set.

## What this does not decide

C-MKT-01 stays open. C-MKT-03 stays open. K1 is not marked. K5 is not marked. E-MKT-081 is not a K4 measurement. No rupee figure was produced by converting a dollar figure, and no dollar figure was produced by converting a rupee figure.
