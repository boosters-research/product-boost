# Pricing note — G2

**Run:** 2026-11-24-myai-myagent  
**Product:** MyAI | Myagent  
**Author:** pricing-strategist  
**Gate:** G2 is open. G4 is not.  
**Status:** Ledger synthesis. No price is set. K1 stays UNTESTED. K5 stays UNTESTED.

This note uses `ledger/EVIDENCE.md`, `ledger/CONSTRAINTS.md`, `ledger/CONTRADICTIONS.md`, `ledger/CPI.md`, and `KILL-CRITERIA.md`. It adds no source. It converts no currency. It edits no ledger row and no deliverable.

`ledger/CONTRADICTIONS.md` records C1–C6 as resolved and attaches rupee amounts to those rows. Those amounts have no Evidence Ledger ID. This note leaves them unused. The contradictions that bind this note are C-00, C-MKT-01, and C-MKT-03. All three stay OPEN.

---

## 1. Primary value metric

The user ceiling is denominated per minute of the full audio pipeline: streaming ASR, LLM/SLM, voice-clone TTS, and SIP/WebRTC (E-USER-001, constraint 1). That minute is the only value metric the user locked, and it is locked as a cost ceiling.

| Cell | Reading |
|---|---|
| VM-UNIT | One minute of that full pipeline |
| VM-PRICE | **UNPUBLISHED.** No ledger row states what this product charges for that minute. |
| VM-READING-A | ₹0.30 per minute. This is the G0 working ceiling (E-USER-001, K1). It is a ceiling, not a measured cost and not a price. |
| VM-READING-B | 30 pence. The same user sentence states this second reading (E-USER-001). It is printed beside reading A. It is not converted into rupees, and rupees are not converted into pence. C-00 stays OPEN. |

Other units appear on other parties' cards (per second, per seat, per message, per transaction, per subscriber month). None of those cards is a price for this product. No second unit is chosen here. C-MKT-01 and C-MKT-03 stay OPEN, so those cards are not collapsed into VM-UNIT.

Phase 1 scope, which is not a price: phone banking in the mobile app with Audio Signature (constraint 5, E-USER-005). Cross-department coordination and subscriber verification sit in that use case only as the use case needs them. External P2P proxy and the general life-KB stay Phase 2 until CPI is scored from evidence. Fund transfers stay in the written scope. Production transfer authorization stays blocked until K2 is measured. No rupee cap exists (constraint 6). CPI-01 through CPI-04 are unscored. The WTP axis is UNTESTED (`ledger/CPI.md`). Constraint 18 keeps Q3 forum quotes and synthetic interviews out of prices, so they supply no WTP and no tier price.

---

## 2. Packaging

The skill's three tiers are listed so every commercial cell is explicit. A cell is filled only when the ledger states a price for this product. The ledger states none. Competitor cards are in section 5. They are not copied into this table.

| Tier | Target persona | Pricing model | Price point | Included value and limits | Gate / expansion trigger |
|---|---|---|---|---|---|
| Free / Starter | PKG-T1-PERSONA **UNPUBLISHED** | PKG-T1-MODEL **UNPUBLISHED** | PKG-T1-PRICE **UNPUBLISHED** | PKG-T1-LIMITS **UNPUBLISHED** | PKG-T1-GATE **UNPUBLISHED** |
| Pro / Growth | PKG-T2-PERSONA **UNPUBLISHED** | PKG-T2-MODEL **UNPUBLISHED** | PKG-T2-PRICE **UNPUBLISHED** | PKG-T2-LIMITS **UNPUBLISHED** | PKG-T2-GATE **UNPUBLISHED** |
| Enterprise / Custom | PKG-T3-PERSONA **UNPUBLISHED** | PKG-T3-MODEL **UNPUBLISHED** | PKG-T3-PRICE **UNPUBLISHED** | PKG-T3-LIMITS **UNPUBLISHED** | PKG-T3-GATE **UNPUBLISHED** |

Locked scope that is not a tier: Phase 1 is phone banking in the banking app (constraint 5). IMS/SIP and VoLTE/5G stay later tests of the same 800 ms line (constraint 7). No architecture is selected (constraint 10). License flags on ChatTTS (AGPL-3.0) and Vocal (SSPL-1.0) are flags, not a stack and not a price (constraint 17).

---

## 3. Van Westendorp

No ledger row states a Too Cheap price, a Bargain price, an Expensive price, or a Too Expensive price. The four points are not invented. CPI WTP is UNTESTED.

| Point | Cell | Reading |
|---|---|---|
| Too Cheap (quality doubt) | VW-CHEAP | **UNPUBLISHED** |
| Bargain | VW-BARGAIN | **UNPUBLISHED** |
| Expensive (requires justification) | VW-EXPENSIVE | **UNPUBLISHED** |
| Too Expensive (deal breaker) | VW-TOO-EXPENSIVE | **UNPUBLISHED** |

---

## 4. COGS and the ceiling

K1 trips only on a sum of evidenced per-minute costs for streaming ASR + SLM/LLM + TTS/clone + media transport. A sum that omits a component is not a measurement (`KILL-CRITERIA.md`). E-OSS-055 states that a per-minute currency total of those four components, with the arithmetic and the hardware, is unpublished in the sources opened on 2026-11-24. Partials stay on their own rows. They are not added. They are not converted into ₹0.30 per minute or into 30 pence. K1 stays **UNTESTED**. Unpublished is not a clear and not a trip (constraint 18).

| K1 component | What the ledger prints | Pipeline cell |
|---|---|---|
| Streaming ASR | COGS-ASR-PARTIAL: $0.00007 USD per minute for batch `openai/whisper-large-v3-turbo` on one H100 SXM, at a stated Lambda spot price of $2.49 per hour, 597× realtime on 120-second clips (E-OSS-006, T3, 0.55). The page states that Whisper is a batch model. It states no INR figure and no pence figure. Streaming-ASR currency: COGS-ASR **UNPUBLISHED**. Opened streaming-ASR licenses and cards state no currency per audio minute (E-OSS-001, E-OSS-002, E-OSS-003, E-OSS-004). | **UNPUBLISHED.** Excluded from any sum. Not a K1 input. |
| LLM / SLM | Opened text-model cards state no audio-minute price (E-OSS-014, E-OSS-015, E-OSS-016, E-OSS-017, E-OSS-018). NVIDIA's 5 January 2026 write-up, cited inside E-OSS-055, states no currency amount. | COGS-SLM **UNPUBLISHED.** |
| Voice-clone TTS | COGS-TTS-PARTIAL: about 1.4 US cents per minute of speech for VoxCPM2 and about 0.8 US cents per minute of speech for ZONOS3-Mini, on an NVIDIA A10 rented at $1.10 per hour, model already loaded, start-up and idle ignored (E-OSS-019, T3, 0.55). The page states no INR figure and no pence figure. Opened TTS and clone licenses state no currency per audio minute (E-OSS-007, E-OSS-008, E-OSS-009, E-OSS-010, E-OSS-011, E-OSS-012, E-OSS-013). | COGS-TTS **UNPUBLISHED** as a pipeline component. The two cent figures stay partials. Excluded from any sum. Not a K1 input. |
| SIP / WebRTC | E-OSS-055 records that the LiveKit pricing page lists speech-to-text, an LLM, text-to-speech, third-party SIP, and WebRTC on separate lines and states no GPU. The ledger row prints no currency rate from that page. | COGS-TRANSPORT **UNPUBLISHED.** |
| Customer support and other infrastructure | The skill's COGS list includes customer support. No ledger row states a support cost for this product. The BLS May 2025 customer-service wage is an occupational wage, not a talk-minute price: median $21.53 per hour, 10th percentile $15.27, 90th percentile $30.57, and $22.47 per hour in insurance carriers (E-MKT-029). The row says not to divide by 60. Forrester's $1.00 per minute is a modeled handling-cost assumption in one composite, with a 5-minute handle time and 600 FTEs (E-MKT-028, T2). It is not a measured bank invoice. | COGS-SUPPORT **UNPUBLISHED.** |
| Four-component total | E-OSS-055. | COGS-TOTAL **UNPUBLISHED.** |

Ceiling, both readings, unconverted (C-00 OPEN):

| Reading | Figure | Role |
|---|---|---|
| A | ₹0.30 per minute | Working ceiling for the full pipeline (E-USER-001, constraint 1, K1). |
| B | 30 pence | Second reading of the same user sentence (E-USER-001). |

OneMeta Inc.'s Form 10-K for the year ended 31 December 2025 states a wholesale customer price of USD 0.30 to USD 0.36 per minute for the Verbum interpretation product, and cost of revenue of USD 208,590 on revenue of USD 1,505,866 for 2025 (E-OSS-055). The filing does not itemize streaming ASR, an SLM or LLM, voice-clone or TTS, or SIP or WebRTC, and it states no GPU. That wholesale price is a customer price of Verbum. This pipeline's COGS remains COGS-TOTAL **UNPUBLISHED**. The OneMeta dollars are not converted. They are not a reading of C-00. SoundHound's Form 10-K states cost of revenues of USD 97,369 thousand, with no audio-minute count and no split of the four components (E-OSS-055). That total is not a per-minute COGS.

No gross margin is computed. Price (VM-PRICE) and cost (COGS-TOTAL) are both unpublished, so a margin percent would be an invented ratio.

---

## 5. Cards the ledger prints

These are other parties' prices. Each row keeps the object the ledger names. None is VM-PRICE. None enters COGS-TOTAL. T4 cards cannot carry WTP by themselves (CPI 2.0). WTP stays UNTESTED.

### 5.1 C-MKT-01 stays OPEN — two per-second voice prices

E-MKT-031 (Twilio US Voice card, T4, 0.30) prints a virtual agent with Google Dialogflow CX at $0.095 per second. E-MKT-032 (Google Cloud Conversational Agents card, T4, 0.30) prints voice Flows, also called Dialogflow CX, at $0.001 per second and voice Playbooks at $0.002 per second. The ledger says 60 × $0.001 and 60 × $0.002 are arithmetic, not printed per-minute prices. Those per-minute cells stay unpublished.

Filings do not adjudicate the cards. Twilio's Form 10-K for the year ended 31 December 2025 does not contain $0.095 per second or $0.07 per minute (E-MKT-073). Twilio's 2025 annual report names ConversationRelay and does not state those two rates (E-MKT-074). Alphabet's Form 10-K for the year ended 31 December 2025 does not contain a $0.001 per second voice or Dialogflow price; the $0.001 figures in that filing are the par value of Class A, Class B, and Class C stock (E-MKT-075). Alphabet's Form 10-K for the year ended 31 December 2024 does not contain the word Dialogflow or the string 0.001 per second (E-MKT-076). Silence in a filing leaves the cards as printed. No winner is chosen. No second is converted.

| Cell | Reading |
|---|---|
| CARD-TWILIO-SECOND | $0.095 per second, Dialogflow CX line on the Twilio US Voice card (E-MKT-031). C-MKT-01 OPEN. |
| CARD-GOOGLE-FLOWS-SECOND | $0.001 per second, voice Flows / Dialogflow CX (E-MKT-032). C-MKT-01 OPEN. |
| CARD-GOOGLE-PLAYBOOKS-SECOND | $0.002 per second, voice Playbooks (E-MKT-032). C-MKT-01 OPEN. |
| CARD-SECOND-AS-MINUTE | **UNPUBLISHED.** No reconciled per-minute price is printed. |

The same Twilio card prints local outbound calls at $0.0140 per minute, local inbound calls at $0.0085 per minute, and Conversation Relay at $0.07 per minute (E-MKT-031). Those three are US list rates on that page. They are outside the disputed Dialogflow line. They are not this pipeline's COGS and not K1 inputs. E-MKT-073 and E-MKT-074 record that the 10-K and the annual report do not state the $0.07 per minute rate. The card is still the card.

### 5.2 C-MKT-03 stays OPEN — India SMS and voice stay separate objects

| Object | Printed figure | Cell that stays unpublished |
|---|---|---|
| Inter-operator SMS ceiling, 2018 text as quoted in 2021 | Up to ₹0.05 per promotional SMS and up to ₹0.05 per service SMS, terminating access provider to originating access provider (E-MKT-039, T1, 0.81). | RETAIL-OTP **UNPUBLISHED** in that paper. |
| Inter-operator SMS ceiling, 12 February 2025 amendment | "Upto Rs. 0.05 (five paisa only) for each Transactional SMS." The memorandum states the same ceiling for each transactional, service, and promotional SMS, charged by the terminating access provider to the originating access provider (E-MKT-070, T1, 0.77). The definition of a transactional message includes an OTP from banks (E-MKT-071). | RETAIL-OTP **UNPUBLISHED.** INDIA-INBOUND-VOICE **UNPUBLISHED** in this instrument. Rs. 0.05 is the inter-operator ceiling. |
| Jio Postpaid Plan 449, personal use | Local voice Free. National-roaming incoming voice Free. Local SMS Re 1/SMS. National SMS Re 1/SMS. International SMS Rs 5/SMS (E-MKT-072, T3, 0.47). | ENTERPRISE-OTP **UNPUBLISHED.** ENTERPRISE-INBOUND-VOICE **UNPUBLISHED.** |
| Unnamed industry estimates, 7 May 2024 | Enterprise voice 60 paise a minute. SMS 11 paise. Some bulk deals 7 paise for a 15-second pulse. Jio, Airtel, and Vodafone Idea did not answer (E-MKT-036, T3, 0.39). | A named tariff for those three figures is **UNPUBLISHED.** |
| 2Factor.in card, undated, exclusive of 18% GST | OTP SMS ₹0.17, ₹0.14, and ₹0.12 per message at the three volume bands. Inbound IVR ₹0.60, ₹0.45, and ₹0.35 per minute. Outbound calls ₹0.55, ₹0.45, and ₹0.35 per minute. Bands: Starter, Growth, Enterprise (E-MKT-037, T4, 0.30). | These three bands are 2Factor's card. They are not this product's tiers. They are not collapsed with ₹0.05, with Re 1/SMS, or with 60 paise. |

### 5.3 Other printed cards

| Source | Printed figure | Ledger limit |
|---|---|---|
| E-MKT-020 Amazon Connect, T4, 0.30 | Connect Voice $0.018 per minute. Connect Customer voice service $0.038 per minute. Both exclude telephony. Shared-trunking inbound and national outbound $0.0022 per minute for a country set that includes India. | Vendor rate card. The $0.0022 rate is the shared-trunking list rate. An India retail IVR price on this page is **UNPUBLISHED.** |
| E-MKT-021 Amazon Connect Voice ID, T4, 0.30 | $0.025 per transaction (enrollment, identity verification, or fraud check, counted separately). New-customer access ended; support ends 20 May 2026 (E-MKT-022 dates the stop on new customers to 20 May 2025). | Per transaction, through the cutoff. Not per minute. |
| E-MKT-022 Pindrop | Named as a transition option. | PINDROP-PRICE **UNPUBLISHED.** |
| E-MKT-025 Auraya press release | End-of-sale and end-of-support claims. | AURAYA-PRICE **UNPUBLISHED.** |
| E-MKT-027 Forrester / TransUnion TEI, T2, 0.64 | Composite pays $420,000 a year for TruValidate Inbound Authentication on a price-per-call structure. Risk-adjusted year-1 fee on the page is $441,000. 12 million inbound calls. $3 billion revenue. | TRUVALIDATE-PER-CALL **UNPUBLISHED.** The study does not say the fee covers every inbound call. |
| E-MKT-028 same study | Assumed inbound handling cost $1.00 per minute. Average handle time 5 minutes. 600 FTEs. | Modeled assumption for that composite. |
| E-MKT-030 Twilio US SMS, T4, 0.30 | $0.0083 per outbound or inbound segment, plus long-code carrier fees of $0.0035 AT&T, $0.0045 T-Mobile, and $0.005 Verizon. | US list price. An India OTP price on this page is **UNPUBLISHED.** |
| E-MKT-033 Genesys Cloud CX, T4, 0.30 | CX 1 $75, CX 2 $115, CX 3 $155, CX 4 $240 per user per month, billed annually. | Named-user list price. A second dollar rate for concurrent or hourly licenses is **UNPUBLISHED** on the fetched page. |
| E-MKT-034 Five9, T4, 0.30 | Digital bundle $119 per seat per month. Core bundle $159 per seat per month. Per concurrent user. 50-seat minimum. AI is 3,000 minutes per bundled seat plus usage. | Plus, Pro, and Enterprise dollar prices were absent from the fetched page: FIVE9-UPPER-TIERS **UNPUBLISHED.** Voice inclusion at $119 is not clean on the page. |
| E-MKT-035 Genesys Cloud pricing hub, T4, 0.30 | Bring-your-own-technology Rate C, USD 0.02 per minute. Rate E, USD 0.1000 per minute. | Component rates on top of a seat. E-MKT-077 and E-MKT-078: a customer-contract rate of USD 0.02 per minute for bring-your-own voice is unpublished in the filings opened. The T4 card stays the T4 card. |
| E-MKT-051 TRAI yearly indicators, T1, 0.90 | "Revenue from VAS" is ₹1.20 per wireless subscriber per month in FY 2025-26, and ₹1.26 in the FY 2024-25 comparative cell, equal to 0.64% of per-subscriber revenue excluding GST. | Revenue-mix share. A VAS gross margin in this report is **UNPUBLISHED.** |

---

## 6. Gross margin, CAC, and the floors this run does not adopt

E-USER-006: Deliverable 02 is to test unit economics under the 30p/min ceiling, with a 1.5× CAC buffer, and a DCF. The brief states no payback window and no gross-margin floor.

| Named floor or window | Where it appears | Status in this note |
|---|---|---|
| Pure-software gross margin 75–85% | Pricing skill | **Not adopted.** Not a kill threshold for this run. |
| AI-heavy gross margin 60–70% | Pricing skill | **Not adopted.** Not a kill threshold for this run. |
| Gross margin 50% | K5 assumption column. The kill file says 50% is not in the brief. | **Not adopted.** Constraint 8: not frozen. |
| Payback inside 12 months | K5 assumption column. The kill file says the 12-month window is not in the brief. | **Not adopted.** Constraint 8: not frozen. |
| 1.5× CAC buffer | E-USER-006. Constraint 8. K5. | **Locked.** The buffer has no payback input. |

K5 stays **UNTESTED**. Unknown inputs leave that status (`KILL-CRITERIA.md`). A company-level percent is not a contract margin and is not a K5 result (constraint 16, E-MKT-059).

### 6.1 Contract margin and payback

| Cell | Reading |
|---|---|
| GM-PRODUCT | **UNPUBLISHED.** |
| GM-CONTRACT | **UNPUBLISHED.** No filing, regulator report, or named-methodology survey opened on 2026-11-24 states the gross margin of one telecom VAS contract or one banking voice-agent contract (E-MKT-059, T1). |
| CAC-CURRENCY | **UNPUBLISHED.** No contract-level CAC in currency for telecom VAS or banking voice-agent contracts (constraint 16). |
| PAYBACK-MONTHS | **UNPUBLISHED** for telecom VAS contracts (E-MKT-052) and for banking voice-agent contracts (E-MKT-053). |
| PAYBACK-BUFFERED | **UNPUBLISHED.** E-MKT-057: the 1.5× buffer cannot be applied to a reported payback, because unbuffered payback months are unpublished. The missing term is new-customer ARR. No buffered month-count is stated. |
| DCF | **UNPUBLISHED.** No product cash-flow series is in the ledger. This note does not build one. |
| SAAS-MEDIAN-PAYBACK-MONTHS | **UNPUBLISHED.** Pavilion / Benchmarkit May 2025 prints payback charts at N=148 and does not put the numeric median months in the text layer. It has no telecom VAS or banking voice-agent subsample (E-MKT-054). Its sentence that common wisdom often says about 12 months is not a measured median. |

E-MKT-057 prints two known spend figures that are not CAC and not payback: Five9 sales and marketing of $311.816 million, and NICE selling and marketing of $661.1 million. New-customer ARR is unpublished, so those dollars are not turned into months. Sinch defines acquisition costs as business-combination costs, not CAC (E-MKT-046).

E-MKT-082, a Forrester TEI of Replicant Voice commissioned by Replicant (April 2021, one customer organization, Postmates), states payback under 6 months, ROI of 110%, and NPV of $6.57 million for that customer's investment. E-MKT-083: no primary table was opened for a voice-AI median gross margin of 60%, a top quartile of 70%, a Replicant figure of 74%, or CAC payback of 9, 5, and 3.8 months. E-MKT-055 printed those six numbers without a sample and is not used as a measurement. E-MKT-082 is not a K5 input. E-MKT-056 reports a claim that Gnani.ai's gross margin is above 80%, with no fiscal year and no filing. E-MKT-084: no Gnani.ai filing opened on 2026-11-24 states that percent. The claim is not a measurement.

### 6.2 Company-level margins the ledger prints

These stay company-level. They are not GM-CONTRACT and they do not mark K5.

| ID | What the source states | Limit recorded on the row |
|---|---|---|
| E-MKT-040, T3, 0.55 | OnMobile presentation: FY26 gross margin 52.7% on gross revenue INR 5,245 million, COGS INR 2,481 million, gross profit INR 2,763 million. FY25 46.7%. | Consolidated mobile entertainment. Not one contract. The deck is not the audited gross-margin line. COGS includes UFF, and UFF is undefined. |
| E-MKT-041, T1, 0.90 | Audited results do not label a gross margin. Derived residual ratio 51.9% on revenue from operations INR 5,168.50 million. India revenue INR 834.43 million. | Derived. Revenue base differs from E-MKT-040 by INR 76.50 million. Both stay open. |
| E-MKT-042, T3, 0.55 | Product margin 11% by the fourth quarter in the gaming discussion, long-term objective about 25%, and entertainment and communication revenue INR 3,700 million at a 21% product margin. | Product margin is undefined. It is a different object from E-MKT-040 and E-MKT-041. |
| E-MKT-044, T1, 0.90 | Tanla audited letter: gross margin 26.6% for FY26 and 26.1% for FY25, on revenue INR 44,177 million and gross profit INR 11,746 million. | Consolidated company. Defined as revenue less service-transaction fees to mobile carriers and other suppliers. Not a banking voice-agent contract. |
| E-MKT-045, T1, 0.90 | Digital-platform revenue INR 3,949 million and gross profit INR 3,888 million. The letter does not state the percents. The evidence note writes the derived platform ratio 98.5% and the derived residual enterprise-communications ratio 19.5%. | Derived. The note says this is not a voice-agent margin. |
| E-MKT-046, T1, 0.90 | Sinch 2025 gross margin 34.8% (narrative also says 35%) on net sales SEK 27,080 million and gross profit SEK 9,426 million. Regional: Americas 35%, EMEA 32%, APAC 40%. | Company-level CPaaS. The measure is not IFRS, by Sinch's own statement. SEK is not converted. |
| E-MKT-047, T1, 0.90 | Five9 Form 10-K: gross profit 55% of revenue. Dollars: $632.854 million on $1,149.088 million. The evidence note writes that ratio 55.1%, and the 19 February 2026 earnings release states GAAP gross margin 55.1%. The same release states adjusted gross margin 62.8%. | 62.8% is the adjusted figure. Banking revenue share is unpublished. CAC payback is unpublished. |
| E-MKT-048, T1, 0.90 | NICE Form 20-F: total gross profit 66.4% of revenue ($1,956.1 million on $2,945.4 million). Cloud gross profit 65.6% of cloud revenue ($1,467.9 million on $2,238.4 million). Same table: services 65.4%, product 83.1%. | Consolidated company. New-customer ARR unpublished, so payback is not computed. |
| E-MKT-049, T1, 0.90 | SoundHound Form 10-K states gross margin of 42%, down from 49% in 2024, on gross profit $71.551 million and revenue $168.920 million. The evidence note writes the dollar ratio 42.4%. The earnings release states GAAP 42.4% and non-GAAP 58.0%. | 58.0% is the non-GAAP figure. Company-level voice AI. CAC payback unpublished. |
| E-MKT-050, T1, 0.90 | LivePerson: revenue $243.742 million. Cost of revenue exclusive of depreciation and amortization $69.392 million. Depreciation and amortization $22.732 million, presented separately. | LIVEPERSON-GM **UNPUBLISHED.** The row assigns no ratio. |
| E-MKT-054, T2, 0.64 | Pavilion / Benchmarkit: subscription gross-margin median 81% (N=76) and total-revenue gross-margin median 77% (N=196). | General B2B SaaS medians. Not this market. |
| E-MKT-058, T3, 0.28 | S Mobility investor communication dated September 2013: gross margin 56.1% and EBITDA margin 15.9%, against 53.6% and 11.3% in the year-ago quarter. | Historical. The page's period label is inconsistent. Not a 2025 or 2026 contract margin. |

---

## 7. Acquisition channels

The template's channel math has no ledger inputs. Phase 1's use case is phone banking in the mobile app (constraint 5). That sentence does not state a conversion rate, a CAC, or a payback.

| Channel | Target | Conversion | Blended CAC | Payback |
|---|---|---|---|---|
| Organic / product-led | CH-ORG-TARGET **UNPUBLISHED** | CH-ORG-CVR **UNPUBLISHED** | CH-ORG-CAC **UNPUBLISHED** | CH-ORG-PAYBACK **UNPUBLISHED** |
| Outbound / account sales | CH-OUT-TARGET **UNPUBLISHED** | CH-OUT-CVR **UNPUBLISHED** | CH-OUT-CAC **UNPUBLISHED** | CH-OUT-PAYBACK **UNPUBLISHED** |
| Ecosystem / marketplace | CH-ECO-TARGET **UNPUBLISHED** | CH-ECO-CVR **UNPUBLISHED** | CH-ECO-CAC **UNPUBLISHED** | CH-ECO-PAYBACK **UNPUBLISHED** |

Aha moment, viral hook, and onboarding mitigation: CH-AHA **UNPUBLISHED**, CH-VIRAL **UNPUBLISHED**, CH-ONBOARD **UNPUBLISHED**.

---

## 8. Kill readings this note does not mark

| Criterion | This note's reading |
|---|---|
| K1 | **UNTESTED.** COGS-TOTAL is unpublished. The ceiling is printed as ₹0.30 per minute and as 30 pence. C-00 stays OPEN. Partials are not summed. OneMeta's USD 0.30 to USD 0.36 is a wholesale Verbum price. Rs. 0.05 is an inter-operator SMS ceiling. |
| K5 | **UNTESTED.** The 1.5× CAC buffer is locked and has no payback input. GM-PRODUCT, GM-CONTRACT, CAC-CURRENCY, PAYBACK-MONTHS, and PAYBACK-BUFFERED are unpublished. The 12-month window and the 50% floor are not frozen and are not applied. The skill's 60–70% and 75–85% bands are not applied. |

G4 is not open. No path is measured here.

---

## 9. Unpublished cells

VM-PRICE. PKG-T1-PERSONA. PKG-T1-MODEL. PKG-T1-PRICE. PKG-T1-LIMITS. PKG-T1-GATE. PKG-T2-PERSONA. PKG-T2-MODEL. PKG-T2-PRICE. PKG-T2-LIMITS. PKG-T2-GATE. PKG-T3-PERSONA. PKG-T3-MODEL. PKG-T3-PRICE. PKG-T3-LIMITS. PKG-T3-GATE. VW-CHEAP. VW-BARGAIN. VW-EXPENSIVE. VW-TOO-EXPENSIVE. COGS-ASR. COGS-SLM. COGS-TTS. COGS-TRANSPORT. COGS-SUPPORT. COGS-TOTAL. CARD-SECOND-AS-MINUTE. RETAIL-OTP. INDIA-INBOUND-VOICE. ENTERPRISE-OTP. ENTERPRISE-INBOUND-VOICE. PINDROP-PRICE. AURAYA-PRICE. TRUVALIDATE-PER-CALL. FIVE9-UPPER-TIERS. GM-PRODUCT. GM-CONTRACT. CAC-CURRENCY. PAYBACK-MONTHS. PAYBACK-BUFFERED. DCF. SAAS-MEDIAN-PAYBACK-MONTHS. LIVEPERSON-GM. CH-ORG-TARGET. CH-ORG-CVR. CH-ORG-CAC. CH-ORG-PAYBACK. CH-OUT-TARGET. CH-OUT-CVR. CH-OUT-CAC. CH-OUT-PAYBACK. CH-ECO-TARGET. CH-ECO-CVR. CH-ECO-CAC. CH-ECO-PAYBACK. CH-AHA. CH-VIRAL. CH-ONBOARD.

Printed partials that stay outside every unpublished pipeline cell: E-OSS-006 ($0.00007 USD per minute, batch ASR) and E-OSS-019 (about 1.4 and about 0.8 US cents per minute of speech). They are not COGS-TOTAL.
