# Product Market Feasibility Assessment — MyAI | Myagent

Run: `2026-11-24-myai-myagent` · Date: `2026-11-24` · Judge rounds: `2/10` · Ledger coverage: `0.86`

Synthesis of the G1 ledger. No new search. K1–K6 stay UNTESTED. A miss on an opened page is not a kill. An unpublished figure is not a pass. The user selects the scenario at the G2 packet. This document recommends one and does not record that selection as made.

---

## SECTION 1 — Executive Summary & Verdict

- **Verdict:** PROCEED WITH CONDITIONS. The recommendation is Scenario A. The selection is not made.
- **Headline finding:** No Customer Pain Index can be printed, because every anchor axis that would feed one is UNTESTED, and the only scored willingness-to-pay axis belongs to a different product.
- **Strongest evidence:** E-MKT-001, E-MKT-002, E-MKT-027, E-MKT-051, E-OSS-055.
- **Weakest link:** The price a bank pays to authenticate phone banking, and the retail price of the SMS OTP workaround, are unpublished, so the anchor value proposition has no CPI.
- **What would change our mind:** A T1 or T2 source that states what a bank pays for this Audio Signature design, together with a priced workaround, such that CPI-01 can be printed; a printed CPI-01 below 20 would drop the recommendation, and a printed CPI-05 of at least 35 while CPI-01 remained unprintable would move the recommendation to Scenario C. A text of the applicable banking control that accepts or refuses this design would also change the recommendation. No such text is in the ledger. K4 stays UNTESTED.

Conditions that travel with the verdict:

1. C-00 stays open. The ceiling, when cited, is both strictly under ₹0.30 per minute and the brief's 30 pence reading. They are not converted.
2. C-MKT-01, C-MKT-03, C-ACA-01, C-ACA-02, and the phrase "verification baseline" stay open.
3. The 1.5× CAC buffer is locked and has no payback input (E-MKT-057). The 12-month window and the 50% floor are not frozen and are not kill thresholds.
4. The five G1 gap clusters in Section 13 stay open. G4 is not open. No technical architecture is selected.
5. Forum quotes and synthetic interviews stay out of CPI and out of prices.

---

## SECTION 2 — Market Definition & Segmentation

**Category boundary.** The brief names an operator VAS and a subscriber voice agent, and it names one anchor use case: phone banking in the mobile app, with transaction authorization by Audio Signature and with no SMS OTP (E-USER-005). Phase 1, as locked, is that anchor. Cross-department coordination and subscriber verification are inside Phase 1 only as that use case needs them. The external P2P proxy and the general life knowledge base stay Phase 2 until a CPI is printed from evidence. None is printed. A generative voice clone is off the transaction path. The brief's phrase "verification baseline" is an open conflict and is not a second definition of Audio Signature.

**What this category is not, on the numbers that were opened.**

- The full-pipeline audio COGS is unpublished (E-OSS-055). K1 stays UNTESTED. The working ceiling is strictly under ₹0.30 per minute, and the brief also says 30 pence (E-USER-001). C-00 stays open.
- OneMeta's USD 0.30 to USD 0.36 per minute is the wholesale price of the Verbum interpretation product (E-OSS-055). It is a customer price for that product. It is not this pipeline's COGS.
- InferenceBench's $0.00007 USD per minute is one batch ASR write-up (E-OSS-006). The Stork.AI figures of about 1.4 and 0.8 US cents per minute are two TTS write-ups (E-OSS-019). They are not added to each other or to anything else, and they are not converted into ₹0.30 or into 30 pence.
- TRAI's "Upto Rs. 0.05" is the charge the terminating access provider may levy on the originating access provider for each transactional, service, and promotional SMS (E-MKT-070, E-MKT-039). The retail price a bank or a sender pays per OTP SMS is UNPUBLISHED (E-MKT-071). The India inbound voice price per minute is UNPUBLISHED (E-MKT-071).

**Segments.** Reachable-account counts are unpublished. No row states a count of Indian banks, a count of phone-banking users, or a count of wireless subscribers.

| Segment | Who | Count in the ledger | Money figure that is actually printed | Ledger ID |
| :--- | :--- | :--- | :--- | :--- |
| Banks under the 25 September 2025 authentication directions | Regulated entities originating domestic digital payments | UNPUBLISHED | None for this product | E-MKT-001 |
| Indian wireless VAS | The TRAI per-subscriber mix | Subscriber count UNPUBLISHED in this row | ₹1.20 per wireless subscriber per month in FY 2025-26, equal to 0.64% of per-subscriber revenue excluding GST. A revenue-mix share | E-MKT-051 |
| US financial-services contact center | One commissioned composite | One composite, not a census. 12 million inbound calls a year and 600 FTEs are attributes of that composite | $420,000 a year for TruValidate Inbound Authentication. Per-call rate UNPUBLISHED. Revenue of the composite $3 billion | E-MKT-027, E-MKT-028 |
| Contact-center software vendors | Five9's filed customer base | More than 3,000 customers, including banking and financial services. No customer above 10% of Five9's 2025 revenue | Company gross margin, not a contract for this product | E-MKT-047 |

**Buyer, user, and economic buyer.**

- In Scenario A the economic buyer is a bank subject to E-MKT-001. The user, on the brief's anchor, is the person doing phone banking in that bank's app (E-USER-005). The ledger does not count either role. Whether one person is both the telecom subscriber and the banking customer is a scoping assumption in the product-scope draft, not a market measurement.
- In Scenario B the economic buyer is an operator or a sender who would put a conversational session into the VAS catalogue. No such contract is in the ledger (E-MKT-059).
- In Scenario C the only buyer with a non-T4 annual figure is the composite in E-MKT-027. That buyer is not identified as a named bank.

**Why now.** Three structural texts are in the ledger, and a graveyard is in the ledger. Together they do not show a new empty market.

- The Reserve Bank of India (Authentication mechanisms for digital payment transactions) Directions, 2025, dated 25 September 2025, require every domestic digital payment transaction, unless exempted, to be authenticated by at least two distinct factors, and require that for transactions other than card-present at least one factor be dynamically created or proven. Paragraph 3 requires compliance by 1 April 2026 (E-MKT-001). The run date is 2026-11-24, which is after that printed date. The directions do not say which institutions are inside the requirement today. They are silent on whether voice biometrics may replace SMS OTP. Paragraph 5(f) lists SMS-based OTP and device-native or Aadhaar biometrics and does not name voice. The introduction says the ecosystem has primarily adopted SMS-based OTP as the additional factor (E-MKT-002). The 18 February 2021 Digital Payment Security Controls directions are also silent on voice replacing SMS OTP, and they say regulated entities may consider alternatives to SMS-based OTP where the additional factor and the mobile application reside on the same device (E-MKT-003). Silence is not an acceptance of this Audio Signature. K4 stays UNTESTED. A Philippines circular that lists voice recognition is not that control (E-MKT-066).
- The Telecom Commercial Communications Customer Preference (Third Amendment) Regulations, 2026, dated 18 September 2026, define an A2P call to include artificial voice technologies and require every sender to declare A2P use in advance. An undeclared A2P call is treated as unsolicited commercial communication (E-MKT-013). The same instrument does not prohibit a subscriber voice clone from placing a call as that subscriber. K6 stays UNTESTED.
- The Digital Personal Data Protection Rules, 2025, dated 13 November 2025, set a minimum retention of one year for personal data, associated traffic data, and other logs of processing, for the purposes in the Seventh Schedule (E-MKT-014). That rule does not name transactional SMS or call transcripts. The Act states no number for those classes (E-MKT-008). GDPR states no number for them either, and Article 9(1) prohibits processing biometric data for unique identification unless an Article 9(2) condition applies (E-MKT-009, E-MKT-010). No row shows that a condition has been met for this design.

The graveyard in Section 4 is the other half of why-now. Voice authentication for phone banking and for contact centers has already been sold, and named products have stopped taking customers or have removed the feature. The market has not been sitting untouched until these 2025–2026 texts.

---

## SECTION 3 — Demand Evidence & Customer Pain Index

### Verbatim buyer language

Every voice-of-customer row in the ledger is T4. None is an input to a CPI axis or to a price. India customer quotes on voice authentication in that set: 0. Caller-tune charge quotes dated on or after 2024-11-24: 0. Synthetic interviews (`E-SIM-001` through `E-SIM-019`) are not buyer evidence.

The table records that the quotes exist and that they are excluded.

| Quote | Persona | Source tier | Ledger ID |
| :--- | :--- | :--- | :--- |
| Excluded. Ledger paraphrase: an RBS telephone-banking reviewer wrote that the line had become a robot and wrote "If they don't improve fast im moving to another bank." | UK bank telephone customer, one review | T4, excluded | E-VOC-006 |
| Excluded. "I am still not receiving OTP from SBI in USA." | One Reddit account, India bank, overseas number | T4, excluded | E-VOC-009 |
| Excluded. Ledger paraphrase: First Direct voice ID denied access often enough, including with a cold, that the writer had it removed | UK forum, one writer | T4, excluded | E-VOC-016 |
| Excluded. Ledger paraphrase: a self-described Airtel subscriber wrote that toll-free menus had no customer-service choice | One Reddit account | T4, excluded | E-VOC-028 |
| Excluded. Ledger paraphrase: a 2023 Vodafone India subscriber described a caller tune activated without a request they recognised | One Reddit account, before 2024-11-24 | T4, excluded | E-VOC-034 |

### CPI ledger

Scored rows live in `ledger/CPI.md`. The arithmetic is the P2 formula. A missing axis blocks the product. No row clears 35, and no row is placed in a band. The anchor USP therefore cannot yet be tied to a CPI of 35 or higher. That failure is reported here. It is not repaired by a substitute number.

| VP / Feature | Persona | Freq | Sev | WQ | WTP | CPI | Band | Evidence IDs | Confidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CPI-01 Phone banking + Audio Signature | Bank under the 25 September 2025 directions. Count UNPUBLISHED | UNTESTED | UNTESTED | UNTESTED | UNTESTED | — | — | E-MKT-001, E-MKT-002, E-MKT-003, E-MKT-071 | Axes not scored |
| CPI-02 Cross-department resolution | UNCONFIRMED | UNTESTED | UNTESTED | UNTESTED | UNTESTED | — | — | E-MKT-028 does not describe this pain | Axes not scored |
| CPI-03 Personal KB + voice clone | UNCONFIRMED. Clone off the transaction path | UNTESTED | UNTESTED | UNTESTED | UNTESTED | — | — | E-MKT-010 | Axes not scored |
| CPI-04 External P2P voice proxy | UNCONFIRMED | UNTESTED | UNTESTED | UNTESTED | UNTESTED | — | — | E-MKT-013 | Axes not scored |
| CPI-05 Inbound caller authentication, other product | US FS composite, one study | UNTESTED | UNTESTED | UNTESTED | 3 | — | — | E-MKT-027 | WTP axis 0.64. CPI not printed. ± band not applied |

CPI-05 is scored 3 on willingness to pay only: the composite is modeled as paying $420,000 a year for TruValidate Inbound Authentication, on a price-per-call structure, and the study does not publish the per-call rate (E-MKT-027). The ledger marks that figure ASSUMPTION if reused. It is reused here only as evidence that an annual figure exists in that category. It is not divided by 12 million calls. The risk-adjusted year-1 fee of $441,000 is in the same note and is not a second price. This is not a 4. Disclosed unit prices on vendor cards are T4 and are excluded. This is not CPI-01.

Workaround quality is unscored on every row. The protocol requires the incumbent to be named with a price. SMS OTP is named (E-MKT-002). Its retail price is UNPUBLISHED (E-MKT-071).

### Market sizing — arithmetic exposed

| Layer | Formula | Inputs (IDs) | Value | Confidence |
| :--- | :--- | :--- | :--- | :--- |
| TAM | No row states a category revenue for phone-banking voice agents, operator voice-agent contracts, or inbound voice biometrics | E-MKT-051 prints a per-subscriber mix and withholds a subscriber count. E-MKT-059 states that no opened filing states a contract margin for one telecom VAS contract or one banking voice-agent contract | UNPUBLISHED | — |
| SAM | Reachable banks × paid authentication | Bank count UNPUBLISHED. Price UNPUBLISHED | UNPUBLISHED | — |
| SOM | (reachable accounts) × (attach rate) × (ACV) | Each term UNPUBLISHED. E-MKT-053 and E-MKT-057: CAC payback and new-customer ARR for this class of contract are unpublished | UNPUBLISHED | — |
| Not a TAM. TRAI mix | Printed per subscriber. Not multiplied | ₹1.20 per wireless subscriber per month; 0.64% of per-subscriber revenue excluding GST | The printed mix only | 0.90, E-MKT-051 |
| Not a TAM. One composite | Stated attributes. Not multiplied | 12 million inbound calls; $1.00 per minute and 5 minutes are labeled assumptions; $420,000 a year; per-call rate unpublished | The printed attributes only. $420,000 / 12,000,000 is not a rate the study states | 0.64, E-MKT-027, E-MKT-028 |

Company revenues in Section 4 are the reporting entity's revenue. They are not a SAM.

---

## SECTION 4 — Competitive Landscape

The status quo is a named competitor. T4 list prices are shown so the open contradictions stay visible. They are not prices of this product and they are not CPI inputs. No winner is chosen on C-MKT-01 or C-MKT-03.

| Competitor | Type | Positioning | ICP | Pricing | Stage | Weakness | Ledger ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SMS OTP as the adopted additional factor | Status quo | The factor the Indian payments ecosystem is described as having adopted | Banks under the 2025 directions | Retail OTP price UNPUBLISHED. Inter-operator ceiling up to Rs 0.05 per transactional SMS, charged between access providers | In use, on the regulator's description | The 2025 directions do not name voice and do not say this factor fails | E-MKT-002, E-MKT-070, E-MKT-071 |
| Human inbound handling | Status quo | Contact-center minute | The US composite's 600 FTEs | Assumption in that study: $1.00 per minute and 5 minutes average handle time. BLS May 2025 median wage for customer service representatives $21.53 per hour. Commercial-bank wage UNPUBLISHED. Do not divide the wage by 60 | The study's baseline | The minute is an assumption, not an invoice | E-MKT-028, E-MKT-029 |
| Do nothing beyond the two factors already required | Status quo | Stay on a dynamic factor the directions already exemplify, including SMS OTP | The same banks | No incremental product price is stated | The directions' own examples | Does not test Audio Signature | E-MKT-001, E-MKT-002 |
| TruValidate Inbound Authentication | Named product in a commissioned study | Inbound authentication, price-per-call | One US FS composite, $3 billion revenue | $420,000 a year modeled. Per-call rate UNPUBLISHED. Pricing may vary. A separate risk-adjusted year-1 figure of $441,000 is in the note | Modeled, not a contract in this ledger | Commissioned composite. Not this Audio Signature | E-MKT-027 |
| Amazon Connect Voice ID | Cloud voice biometrics, end of support documented | Identity verification and fraud check on Connect | Connect customers | Support ends 20 May 2026. New customers stopped 20 May 2025. Transition options named: Pindrop, or an SMS one-time PIN. Pindrop price UNPUBLISHED. The $0.025 per transaction figure is T4 and is not used | End of support | The commercial reason is not stated beyond the stop and the end date | E-MKT-022. Price card E-MKT-021 is T4 |
| Microsoft speaker recognition | Cloud feature removal | Speaker recognition inside Speech | Speech SDK users | Speech SDK 1.47, November 2025, removed the samples and the support. The date 30 September 2025 is UNPUBLISHED | Removed, on the release notes | Cause beyond "retirement" is unpublished in the notes that were opened | E-MKT-079, E-MKT-080 |
| Five9 | Contact-center platform, filed company | Cloud contact center, customers include banking | More than 3,000 customers | GAAP gross margin 55.1% on revenue of $1,149.088 million for 2025. No customer above 10%. Seat prices on the marketing page are T4 and are not used. No contract margin for a banking voice agent | Public company | Company margin is not a contract margin | E-MKT-047, E-MKT-059. T4 card E-MKT-034 excluded |
| NICE | Filed company, customer engagement and financial crime | Consolidated cloud and license | Not a named bank contract | Total gross profit 66.4% of revenue ($1,956.1 million on $2,945.4 million). Cloud gross profit 65.6% of cloud revenue | Public company | Same limit: company, not contract | E-MKT-048, E-MKT-059 |
| SoundHound AI | Filed company | Voice AI, after the Amelia and Interactions acquisitions | Not a named bank contract | Gross margin 42% on the company's statement, 42.4% on $71.551 million gross profit and $168.920 million revenue. No audio-minute count | Public company | Not this pipeline's COGS | E-MKT-049, E-OSS-055 |
| LivePerson | Filed company | Conversational platform; named markets include telecommunications and financial services | Not a counted pipeline for this product | Revenue $243.742 million. Gross-margin percent UNPUBLISHED. CAC payback UNPUBLISHED. This assessment does not derive a margin from the cost lines | Public company | The filing withholds the percent | E-MKT-050 |
| OnMobile | Filed VAS company | Mobile entertainment, not one voice-agent contract | India revenue from operations INR 834.43 million inside the audited total | Deck: FY26 gross margin 52.7% on gross revenue INR 5,245 million. Audited revenue from operations INR 5,168.50 million, derived ratio 51.9%. Both stay. Product margin of 21% and 11% is a different, undefined KPI | Public company | Not a contract margin. The two company ratios are not reconciled | E-MKT-040, E-MKT-041, E-MKT-042 |
| Tanla | Filed CPaaS company | Enterprise communications and digital platforms | Not a voice-agent contract | Gross margin 26.6% on revenue INR 44,177 million. Derived platform ratio 98.5% and derived enterprise-communications residual 19.5% are marked derived in the ledger | Public company | Not a voice-agent margin | E-MKT-044, E-MKT-045 |
| Sinch | Filed CPaaS company | Messaging and voice at company level | Regional, not this contract | Gross margin 34.8% on net sales SEK 27,080 million. The company says the measure is not IFRS | Public company | Not a contract margin | E-MKT-046, E-MKT-059 |
| Twilio US Voice card and Google voice Flows card | T4 rate cards, contradiction open | Usage voice and dialog agents | US list prices | Twilio card: Conversation Relay $0.07 per minute, and Dialogflow CX at $0.095 per second. Google card: voice Flows $0.001 per second and voice Playbooks $0.002 per second. Filings opened do not contain those voice rates. No winner | Cards are T4 at confidence 0.30 | C-MKT-01 stays open. Excluded from every price in this document | E-MKT-031, E-MKT-032, E-MKT-073, E-MKT-074, E-MKT-075 |
| Unnamed India enterprise estimates and one CPaaS card | Trade press and a T4 card | Enterprise voice and OTP SMS | Not a named invoice | 60 paise a minute and 11 paise an SMS are unnamed estimates. 2Factor's card is T4 (OTP SMS ₹0.12–₹0.17; inbound IVR ₹0.35–₹0.60 per minute). Jio Postpaid Plan 449 prints consumer voice as Free and consumer SMS as Re 1, and states no enterprise OTP price and no enterprise inbound voice price | Unreconciled | C-MKT-03 stays open. Excluded from every price in this document | E-MKT-036, E-MKT-037, E-MKT-072, E-MKT-071 |

*Must include the status quo.* It is the first three rows.

### Graveyard — who tried this and failed

| Company | Attempt | Why it ended | Does the cause apply to us? | Ledger ID |
| :--- | :--- | :--- | :--- | :--- |
| Amazon Connect Voice ID | Phone and contact-center voice identity. New customers stopped 20 May 2025. Support ends 20 May 2026. The named replacements include an SMS one-time PIN | The documentation states the stop and the end of support. It does not state a measured false-accept rate for the withdrawal | UNTESTED. A return path toward SMS OTP is evidence that this category has already been exited by a scaled vendor. It is not a reading of K4 | E-MKT-022 |
| Microsoft Speech speaker recognition | Speaker recognition in the Speech service | SDK 1.47 removed the samples and the support because of the service retirement. The date 30 September 2025 is not on the pages opened in the retry | UNTESTED. The uncorroborated date is not used | E-MKT-079, E-MKT-080 |
| HSBC Hong Kong phone-banking Voice ID | A bank notice says Voice ID login ended and the replacement is a 6-digit Phone Banking PIN, reset with an ATM PIN plus SMS OTP or at an HSBC ATM in Hong Kong | The 18 August 2024 date is on that bank page. Four HKMA account-opening releases do not state it. No regulator notice of the ending was opened | The date is not applied. The notice is not an RBI decision. K4 stays UNTESTED | E-MKT-026, E-MKT-081 |
| OpenAI Voice Engine | A 15-second sample voice, previewed and not widely released on 29 March 2024 | The vendor encouraged phasing out voice-based authentication for bank accounts. The ledger says this is a recommendation, not evidence that banks stopped paying | The sentence is a warning from a synthesis vendor. It is not a central-bank refusal. Confidence 0.39 | E-MKT-038 |
| Nuance Gatekeeper, as reported | Reported off official sale since July 2024, still being bought, no end-of-life date | One trade article quoting one founder. A vendor press release (T4) says the same direction | Not applied. Confidence 0.47 on the article. Too weak to carry a scenario | E-MKT-024 |
| S Mobility, quarter dated September 2013 | Domestic VAS under the revenue-share versus minimum-guarantee shift that the company described | The company said domestic VAS was under severe stress. Gross margin in that communication was 56.1% | Not a current contract. Confidence 0.28. Not a K5 input | E-MKT-058 |

The literature misses on false-accept and false-reject rates are in Section 11. They are not a company graveyard, and they are not a K2 result. K2 stays UNTESTED.

---

## SECTION 5 — Scenario A: Bank app phone-banking signature

**USP / Value Proposition:** A bank authorizes phone-banking acts inside its own mobile app with an Audio Signature on the enrolled live voiceprint, and the generative clone is not that signature. Falsifier: a bank pays a disclosed price for that path and retires SMS OTP on it. CPI-01 is UNTESTED, so this sentence is not tied to a CPI of 35 or higher. The tie the protocol asks for is unmet.

**Target ICP:** A bank that originates domestic digital payments under the 25 September 2025 directions and that offers phone banking in its mobile app. Firmographic count: UNPUBLISHED. Behaviour on the regulator's text: the ecosystem has primarily adopted SMS-based OTP as the additional factor (E-MKT-002). Reachable-account count: UNPUBLISHED.

**Positioning:** Category entry, beside SMS OTP, into app-channel phone-banking authentication. Frame of reference: the dynamic second factor the 2025 directions already require (E-MKT-001). Point of difference claimed by the brief: a live-voiceprint signature synchronized with the banking app, with the clone off the path. Reason to believe: unmet in this ledger. K2 and K4 are UNTESTED. The best joint point opened under a replay condition is FAR 5.62% and FRR 72.59% (E-ACA-060). That miss is not a kill.

**Brand philosophy — 3 directions:**

1. The signature is the live voice in the app, and a clone is a different object.
2. The bank keeps a second factor the customer can complete without waiting on an SMS.
3. Refusal is the failure mode until a measured signature exists. No step-up is invented here.

These are candidate directions. They are not evidenced beliefs.

**Features necessary:**

| Feature | CPI row | Band | Why required for this scenario |
| :--- | :--- | :--- | :--- |
| Phone-banking conversation in the mobile app for inquiries, disputes, beneficiary registration, and fund transfers in the written scope | CPI-01 | — | Locked Phase-1 use case (E-USER-005). Production transfer authorization stays blocked while K2 is UNTESTED. No rupee cap is stated in the locked constraints |
| Audio Signature on the enrolled live voiceprint | CPI-01 | — | The anchor's authorization act. Targets remain FAR < 0.001% and FRR < 1.0% together under replay, generative deepfake, and voice conversion (E-USER-003). Unmeasured |
| A dynamic factor in the shape the 2025 directions describe | CPI-01 | — | The directions require one dynamic factor for non-card-present domestic payments (E-MKT-001). They do not name this design |
| Cross-department handling only where the phone-banking use case needs it | CPI-02 | — | Locked limit. CPI-02 is unscored, so this is not a general orchestration product |
| Enrollment slice of SMS and call history | CPI-03 | — | Only as enrollment needs. The general life knowledge base is outside this scenario |
| Generative clone | — | — | Out of this scenario. Off the transaction path. "Verification baseline" stays unreconciled |

**Revenue model:** Enterprise license to the bank. Pricing metric: UNPUBLISHED. Price point: UNPUBLISHED (E-MKT-053, E-MKT-059). Packaging: UNPUBLISHED. Expansion path: a later IMS/SIP test of the same latency line is a channel test, not a second price. The COGS ceiling is not a retail price. It remains strictly under ₹0.30 per minute, and the brief also says 30 pence (E-USER-001). C-00 stays open. The 1.5× CAC buffer has nothing to multiply (E-MKT-057).

**GTM motion:** Sales-led to banks. The Phase-1 proof channel is the banking app (E-USER-005). First-100 plan: UNPUBLISHED. No row names 100 reachable banks. Five9's count of more than 3,000 customers is that company's base (E-MKT-047). CAC hypothesis: UNPUBLISHED, in currency, for a banking voice-agent contract (E-MKT-053). Sales cycle: UNPUBLISHED. This document does not import a cycle from outside the ledger.

**Competitive set in this scenario:** SMS OTP, the human phone-banking agent, and the do-nothing use of a factor the directions already list. TruValidate is the nearest disclosed authentication budget and it is a different object (E-MKT-027). Amazon Connect Voice ID is in the graveyard (E-MKT-022).

**PMF score:** NOT COMPUTED.

| Term | Weight | Input | Result |
| :--- | :--- | :--- | :--- |
| Pain acuteness | 30% | Max CPI. CPI-01 not printed | NOT COMPUTED |
| Pain breadth | 20% | Reachable accounts UNPUBLISHED × attach rate UNPUBLISHED | NOT COMPUTED |
| Workaround weakness | 20% | 5 − mean workaround quality. Workaround quality UNTESTED | NOT COMPUTED |
| WTP evidence strength | 20% | No non-T4 willingness to pay for this design | NOT COMPUTED |
| Timing / why-now | 10% | E-MKT-001 date is structural and is already past the run date; E-MKT-002 says SMS OTP is the adopted factor; graveyard in Section 4 | NOT COMPUTED as a single 0–100 score |
| Total | 100% | | NOT COMPUTED. Not presented as under 40, and not presented as a pass |

**Why this could fail:** The applicable control may never accept this signature. The ledger does not say that it will, and it does not say that it will not. K4 stays UNTESTED. Separately, CPI-01 may stay unprintable, in which case the value proposition has no scored pain. A printed CPI-01 below 20 would retire this scenario. Neither of those is a kill criterion being marked today.

---

## SECTION 6 — Scenario B: Declared operator conversational VAS

**USP / Value Proposition:** An operator sells a declared A2P conversational session as a VAS line, and the session does not place a subscriber clone on a payment path. Falsifier: a filed or contracted rev-share price for that session. CPI-04 is UNTESTED, so the CPI ≥ 35 tie is unmet.

**Target ICP:** A sender or an access provider already inside the TCCCPR A2P rule (E-MKT-013). Behaviour: VAS revenue in the TRAI indicators is ₹1.20 per wireless subscriber per month (E-MKT-051). Reachable subscribers: UNPUBLISHED, because that row does not state the subscriber count. This ICP is not the Phase-1 banking-app user.

**Positioning:** Bundling. The frame of reference is the existing operator VAS mix, not a new authentication category. Point of difference claimed: a conversational session the sender declares as A2P, against a catalogue whose public revenue mix is the ₹1.20 line. Reason to believe: the declaration rule is real (E-MKT-013). Demand for replacing caller tunes is not. Those quotes are T4, and the post-2024-11-24 count is 0.

**Brand philosophy — 3 directions:**

1. The carrier declares the machine voice before the call exists.
2. A VAS line is a catalogue item with a contract margin, and that margin is still unpublished.
3. The subscriber's clone is not the product being bundled.

Candidate directions, not evidenced beliefs.

**Features necessary:**

| Feature | CPI row | Band | Why required for this scenario |
| :--- | :--- | :--- | :--- |
| A2P declaration and an artificial-voice session that fits clause (ea) | CPI-04 | — | The 18 September 2026 regulation treats undeclared A2P as unsolicited commercial communication (E-MKT-013) |
| Rev-share metering against the operator | CPI-04 | — | The scenario's revenue model. The meter has no published price |
| Banking Audio Signature, IMS/SIP proof, subscriber clone | — | — | Outside this scenario. Phase-1 proof channel remains the banking app. The clone stays off any payment path |

**Revenue model:** Partner rev-share. Pricing metric: UNPUBLISHED. The ₹1.20 figure is a revenue-mix share per wireless subscriber, not this product's price and not a gross margin (E-MKT-051). Company gross margins for OnMobile, Tanla, and Sinch are not a contract margin (E-MKT-059, E-MKT-040, E-MKT-044, E-MKT-046). Packaging and expansion path: UNPUBLISHED. CAC payback for telecom VAS contracts is UNPUBLISHED (E-MKT-052). The 1.5× buffer is not applied (E-MKT-057).

**GTM motion:** Partner-led, through the operator. First-100 plan: UNPUBLISHED. CAC hypothesis: UNPUBLISHED (E-MKT-052). Sales cycle: UNPUBLISHED. This motion contradicts the locked Phase-1 channel if someone treats it as the first proof. The proof channel stays the banking app. IMS/SIP and VoLTE/5G stay later tests of the same p95 < 800 ms line (E-USER-002). K3 stays UNTESTED.

**Competitive set in this scenario:** The existing VAS catalogue represented by the TRAI mix, and the company-level VAS and CPaaS reporters (OnMobile, Tanla, Sinch). Not Five9's seat card. Not SMS OTP.

**PMF score:** NOT COMPUTED. Same five-term block as Scenario A. CPI-04 is unprinted, so pain acuteness, breadth, workaround weakness, and willingness to pay are NOT COMPUTED. Timing uses E-MKT-013 and is not collapsed into a 0–100 score. Total NOT COMPUTED.

**Why this could fail:** An undeclared automated voice becomes unsolicited commercial communication under the text that was opened (E-MKT-013). A declared one still has no evidenced price and no evidenced contract margin. Subscriber pain for caller tunes and IVR loops is T4 only and cannot carry the scenario.

---

## SECTION 7 — Scenario C: Inbound authentication as its own product

**USP / Value Proposition:** Sell inbound caller authentication into the category where one US financial-services composite is modeled at $420,000 a year, and do not claim the FAR < 0.001% Audio Signature. Falsifier: a published per-call rate, or a second buyer with an audited fee. CPI-05 has a willingness-to-pay axis of 3 and no printed CPI. The CPI ≥ 35 tie is unmet.

**Target ICP:** Contact-center buyers of inbound authentication. The only described buyer is the commissioned composite: $3 billion revenue, 12 million inbound calls a year, 600 FTEs (E-MKT-027, E-MKT-028). That is one model, not a reachable-account count. Five9's more than 3,000 customers show that contact-center platforms already sell to banks (E-MKT-047). They are not this product's pipeline.

**Positioning:** Unbundling. Sell the authentication control alone. Frame of reference: TruValidate's price-per-call category and the human minute in the same study. Point of difference: none is evidenced against TruValidate, because this ledger has no second price. Reason to believe: a commissioned annual figure exists, and the unit price does not.

**Brand philosophy — 3 directions:**

1. Authenticate the caller the contact center already has on the line.
2. Publish the per-call rate or do not quote the annual figure as a price.
3. Leave Audio Signature, the clone, and the four pillars out of this offer.

Candidate directions, not evidenced beliefs.

**Features necessary:**

| Feature | CPI row | Band | Why required for this scenario |
| :--- | :--- | :--- | :--- |
| Inbound caller authentication as a metered control | CPI-05 | — | The only non-T4 category budget (E-MKT-027). WTP 3. CPI not printed |
| A reported per-call price | CPI-05 | — | The study says the structure is price-per-call and does not print the rate. The feature is the disclosure, and it is missing |
| Audio Signature at FAR < 0.001% and FRR < 1.0%, clone, cross-department agent, personal KB | — | — | Out of this scenario. Those claims are CPI-01 through CPI-04, all unprinted |

**Revenue model:** Usage, per call, because that is the structure the study names. Price point: UNPUBLISHED at the per-call level. The only annual figure is $420,000 for that composite, flagged ASSUMPTION if reused (E-MKT-027). This document does not compute $420,000 / 12,000,000. Packaging: UNPUBLISHED. Expansion path: UNPUBLISHED. General B2B SaaS medians of 81% subscription gross margin (N=76) and 77% total-revenue gross margin (N=196) are not this category, and the median payback months are not in the text layer (E-MKT-054). The April 2021 Replicant study's payback under 6 months is one commissioned customer and is not a voice-AI median and not a K5 input (E-MKT-082).

**GTM motion:** Sales-led to contact-center buyers. First-100 plan: UNPUBLISHED. CAC hypothesis: UNPUBLISHED (E-MKT-053, E-MKT-057). The 1.5× buffer stays unused. Sales cycle: UNPUBLISHED.

**Competitive set in this scenario:** TruValidate, the human agent at the study's assumed minute, and the contact-center platforms whose company margins are in Section 4. SMS OTP is not the frame, except where Amazon's own transition names an SMS one-time PIN as a way off Voice ID (E-MKT-022).

**PMF score:** NOT COMPUTED.

The willingness-to-pay rubric input is 3 out of 5, from E-MKT-027, confidence 0.64. Mapping that single input to 60 points and then weighting it by 20% would produce a partial 12 and would hide three unscored terms. The total is therefore NOT COMPUTED, including for this scenario. It is not presented as under 40, and it is not presented as the strongest PMF. It is the only scenario with a non-T4 money signal, and that signal is a commissioned composite for a different product.

**Why this could fail:** The annual figure may be an artifact of a vendor-commissioned composite. The ledger already says pricing may vary and that the per-call rate is unpublished. A buyer who wants the brief's Audio Signature is not the buyer in this scenario. Treating Scenario C's $420,000 as the price of Scenario A would merge two products the evidence keeps apart.

---

## SECTION 8 — Scenario Comparison & Recommendation

The three scenarios differ on persona, on the CPI row they would have used, on frame (category entry, bundling, unbundling), on revenue structure (license, rev-share, per-call), and on motion (bank sales, operator partner, contact-center sales). They do not differ by a demonstrated price order of magnitude. Every price point is unpublished. They are not three tones of one offer: A is the locked Phase-1 use case, B is an operator catalogue outside that channel, and C is a single control that drops the Audio Signature claim.

| Dimension | Scenario A | Scenario B | Scenario C |
| :--- | :--- | :--- | :--- |
| Max CPI | Not printed (CPI-01) | Not printed (CPI-04) | Not printed (CPI-05). WTP axis 3 only |
| PMF score | NOT COMPUTED | NOT COMPUTED | NOT COMPUTED |
| SOM | UNPUBLISHED | UNPUBLISHED. ₹1.20 per subscriber per month is a mix, not a SOM | UNPUBLISHED. $420,000 is one composite's modeled fee |
| Est. CAC (buffered) | UNPUBLISHED. 1.5× has no base (E-MKT-057) | UNPUBLISHED (E-MKT-052, E-MKT-057) | UNPUBLISHED (E-MKT-053, E-MKT-057) |
| Time to first revenue | UNPUBLISHED | UNPUBLISHED | UNPUBLISHED |
| Defensibility | Not scored. Moat note pending and not evidence | Not scored. Same | Not scored. Same |
| Evidence confidence | Regulatory texts 0.77–0.90. Pain unscored | E-MKT-013 at 0.90. Pain unscored | E-MKT-027 at 0.64 on the fee |

**Recommendation:** Scenario A — **because** it is the only scenario that stays inside the locked Phase-1 use case, phone banking in the mobile app with Audio Signature, while the clone stays off the transaction path — **and I would change my mind if** CPI-01 is later printed from T1 or T2 evidence and lands below 20, or if CPI-05 is printed at 35 or higher while CPI-01 is still unprintable, or if the applicable banking control's text is opened and refuses this design. The user has not selected Scenario A by reading this sentence. The G2 packet is where that selection happens.

Scenario B would become the recommendation if a contract-level VAS price and a contract margin were opened and CPI-04 printed at 35 or higher, and if the user moved the proof channel. Scenario C would become the recommendation under the CPI condition above. Neither condition is met.

---

## SECTION 9 — Product-Market Fit Assessment

The table is for the recommended scenario, Scenario A. The arithmetic is the weighted sum of five 0–100 dimension scores. The inputs those scores require are not in the ledger, so the sum is not produced.

| Dimension | Weight | Score | Evidence | Weighted |
| :--- | :--- | :--- | :--- | :--- |
| Pain acuteness | 30% | NOT COMPUTED | Max CPI in the scenario. CPI-01 has no printed CPI | NOT COMPUTED |
| Pain breadth | 20% | NOT COMPUTED | Reachable accounts and attach rate UNPUBLISHED. E-MKT-051 has no subscriber count | NOT COMPUTED |
| Workaround weakness | 20% | NOT COMPUTED | 5 − mean workaround quality. Workaround quality UNTESTED because the retail OTP price is UNPUBLISHED (E-MKT-071) | NOT COMPUTED |
| WTP evidence strength | 20% | NOT COMPUTED | No non-T4 revealed price for this design. E-MKT-027 is Scenario C's category, and it is excluded here | NOT COMPUTED |
| Timing / why-now | 10% | NOT COMPUTED | Structural texts exist (E-MKT-001, E-MKT-013, E-MKT-014) and the graveyard exists (E-MKT-022). They point in different directions. No single score | NOT COMPUTED |
| **Total** | 100% | | | **NOT COMPUTED** |

Scenarios B and C are also NOT COMPUTED, for the term-by-term reasons in Sections 6 and 7. None is buried. None is given a courtesy score under 40.

---

## SECTION 10 — Barriers to Entry & Defensibility

Ratings are judgments on ledger facts. Where the ledger has no fact that can carry a 1–5 rating, the cell is UNTESTED. A moat note is being written in parallel under `workers/g2-moat`. That note is not in the ledger. This section does not use it. It is not evidence.

| Barrier type | Against us (1–5) | For us once in (1–5) | Notes | Ledger ID |
| :--- | :--- | :--- | :--- | :--- |
| Capital | UNTESTED | UNTESTED | The four-component per-minute total is unpublished. Partial ASR and TTS figures are not a capital estimate. OneMeta's USD 0.30–0.36 is not this COGS. Ceiling, if cited: strictly under ₹0.30 per minute, and 30 pence. C-00 open. K1 UNTESTED | E-OSS-055, E-OSS-006, E-OSS-019, E-USER-001 |
| Distribution | UNTESTED | UNTESTED | Phase-1 channel is the banking app. No reachable-bank count. Partner distribution for Scenario B is a different channel and is not Phase 1 | E-USER-005 |
| Data / network effects | UNTESTED | UNTESTED | No row measures a data advantage or a network effect for this product. The pending moat note is not a substitute | — |
| Switching costs | UNTESTED | UNTESTED | SMS OTP is the adopted factor, so a switch has a named incumbent. The cost of the switch is unpublished with the retail OTP price | E-MKT-002, E-MKT-071 |
| Regulatory | 4 | 2 | Against: Article 9(1) prohibits biometric identification unless an Article 9(2) condition applies, and no row shows a condition met; the RBI texts require two factors and do not name voice; A2P artificial voice must be declared. For us, once in: those texts do not grant an exclusive right. 2 is a reading of that absence of exclusivity, not a moat. K4 and K6 stay UNTESTED | E-MKT-010, E-MKT-001, E-MKT-002, E-MKT-013 |
| Technical | UNTESTED | UNTESTED | No architecture is selected. G4 is not open. Opened accuracy and latency pages miss the bars. A miss is not a rating of an unchosen path and is not a kill | E-ACA-060, E-ACA-001, E-OSS-039, E-USER-002 |
| Brand / trust | 4 | UNTESTED | Against: a scaled vendor has dated the end of Voice ID support and named an SMS one-time PIN as a transition, and a synthesis vendor has recommended phasing out voice authentication for bank accounts (confidence 0.39 on that post, so the rating is carried by E-MKT-022). For us: no trust asset is in the ledger | E-MKT-022, E-MKT-038 |

The pattern "easy to enter and impossible to defend" is not demonstrated. Entry is conditioned on the regulatory row and is untested on capital, distribution, data, switching cost, and the technical path. Defensibility is untested on every row except the regulatory reading that the statutes do not create a franchise. That is a thin position, and it is not a false-positive flag of an easy market. The moat note, when it is evidence, is the place that rating can move.

---

## SECTION 11 — Risk Assessment

Impact and probability are judgments. They do not change K1–K6, which stay UNTESTED.

| Risk | Impact | Prob | Mitigation | Leading indicator | Ledger ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Demand risk. The anchor pain has no printed CPI | H | H | Keep CPI-01 unprinted until each axis has a non-T4 ledger ID. Do not fill frequency from forum quotes | A T1 or T2 price a bank pays for this signature, and a retail OTP price | E-MKT-071, CPI-01 |
| Competitive-response risk. Vendors have left voice identity, and the adopted factor is still SMS OTP | H | M | Do not claim the category is empty. Treat Voice ID's end of support as a graveyard fact | A bank control that names voice, or a disclosed price for a live voice-biometric contract | E-MKT-022, E-MKT-002, E-MKT-038 |
| Channel risk. Scenario B uses the operator, while Phase 1 is the banking app | H | H if B is treated as Phase 1 | Keep the proof channel on the app until the user changes it. IMS/SIP remains a later test of the 800 ms line | A user selection at the G2 packet that names the channel | E-USER-005, E-USER-002 |
| Pricing risk. Unit prices that models want are unpublished or contradicted | H | H | Print both C-00 readings. Leave C-MKT-01 and C-MKT-03 open. Exclude T4 cards from prices | A filing or a tariff that states the retail OTP price, the India inbound voice price, and one of the two disputed per-second prices | E-MKT-071, E-MKT-031, E-MKT-032, E-USER-001 |
| Concentration risk. This product's account list does not exist | H | UNTESTED | Do not borrow Five9's customer count or the "no customer above 10%" line as our pipeline | A counted set of target banks | E-MKT-047, E-MKT-053 |
| Timing risk. The 1 April 2026 compliance date is before the run date, and the adopted factor is already SMS OTP | M | M | Do not describe the directions as an unopened window. Do not describe them as a mandate for voice | A later RBI text that names voice biometrics as acceptable or as refused | E-MKT-001, E-MKT-002 |
| Graveyard lesson. A deployed voice-ID product has a dated end of support and a named SMS fallback | H | M | The scenario that survives has to say what it does that Voice ID did not, with a measurement. This ledger does not contain that measurement | K2 and K4, which stay UNTESTED | E-MKT-022 |
| Unit-economics risk. The buffer has no payback input | H | H | Do not apply 1.5× to an unpublished CAC. Do not freeze 12 months or 50%. Company gross margins stay at company level | A contract margin and a CAC in currency for one banking voice-agent contract or one telecom VAS contract | E-MKT-057, E-MKT-059, E-USER-006 |
| Accuracy risk. Opened rates miss both bars | H | The miss is already on the page. It is not a probability that K2 has tripped | Report the opened points and leave K2 UNTESTED until the G4 path test. Do not cite 0.13% as 0.001% | An evaluation that prints FAR < 0.001% and FRR < 1.0% at one operating point under replay, generative deepfake, and voice conversion together | E-ACA-001, E-ACA-010, E-ACA-060, E-OSS-020, E-OSS-039 |
| Latency risk. No Phase-1 p95 | H | The absence is already recorded. It is not a K3 breach | Leave K3 UNTESTED. C-ACA-02 stays open. No architecture is chosen to "fix" it in this document | A speech-to-speech p95 on the banking-app channel | E-USER-002, E-ACA-084 |
| Clone-prohibition risk | H if a prohibition is later found | UNTESTED | Keep the clone off the transaction path. Do not read silence as permission | A sentence in a named statute that prohibits the subscriber clone call. The 10 February 2026 gazette was not opened | E-MKT-061, E-MKT-063, E-MKT-065, E-MKT-005 |

Opened accuracy points, so the miss is specific and is not a kill: SASV 2022 prints FAR = FRR = 0.13% on TTS and voice conversion, without replay (E-ACA-001). VLSP 2025 prints equal-error rates of 17.78% and 20.79% on a protocol that includes voice conversion, replay, and the other spoof classes in that table (E-ACA-010). VoiceWukong prints FAR 5.62% and FRR 72.59% at the equal-error point of the English replay subset (E-ACA-060). The YouTube-pair row prints FAR 1.73% and FRR 1.68% (E-OSS-020). E-OSS-039 states that none of the opened OSS documents in that range is the three-attack joint point under both bars. The 0.13% figure is not an open-source toolkit result and is not the 0.001% bar.

---

## SECTION 12 — Conclusions

- **Product Value Proposition:** Scenario A is the recommendation and is not the selection. The proposition is app-channel phone banking authorized by a live-voiceprint Audio Signature, with the clone off the path. It is not tied to a CPI of 35 or higher, because CPI-01 is unprinted.
- **Features Necessary:** The Phase-1 set is the app-channel phone-banking acts, the live-voiceprint signature, enrollment as that signature needs it, and cross-department handling only as that use case needs it. Production transfer authorization stays blocked while K2 is UNTESTED. The external proxy, the general life knowledge base, and the clone are outside that set. No feature has a CPI band.
- **Positioning:** Category entry beside SMS OTP, which the 2025 directions' introduction describes as the adopted additional factor. The reason to believe is unmeasured.
- **Brand Philosophy:** The live voice in the app is the signature. The clone is a different object. "Verification baseline" stays unreconciled and is not adopted as the signature.
- **GTM:** Sales-led to banks, on the banking-app channel. First-100, CAC, and sales cycle are UNPUBLISHED. The 1.5× CAC buffer is locked and unused.
- **Revenue Model:** An enterprise license whose price is UNPUBLISHED. The ceiling is a cost ceiling, printed as both strictly under ₹0.30 per minute and 30 pence, and it is not a price. C-00 stays open. A pricing note is being written in parallel under `workers/g2-pricing`. That note is not in the ledger. This section does not use it. It is not evidence. No price here is taken from it.
- **Competitors:** The status quo is SMS OTP, the human agent, and doing nothing beyond a factor the directions already list. The graveyard includes Amazon Connect Voice ID's end of support. Company gross margins are context for the vendors and are not our contract margin.
- **Barriers to Entry:** Regulatory entry is conditioned (Article 9, the RBI factor rule, the A2P declaration). Capital, distribution, data, switching cost, technical path, and post-entry brand are UNTESTED, except the regulatory "for us" reading of 2. The moat note under `workers/g2-moat` is pending and is not evidence.
- **Risk Summary:** The demand, price, and payback inputs this category needs are unpublished. The accuracy and latency bars are unmet on the pages that were opened, and those misses are not kills. K1–K6 stay UNTESTED.

---

## SECTION 13 — Known Gaps & Convergence Notes

The G1 packet carried five clusters. They are copied here with the packet's retry count. This assessment does not close them. The judge loop stopped at round 2 of 10 because coverage moved from 0.85 to 0.86, a gain of 0.01 against a required gain of 0.03. Round 3 was not spent. The four denied searches stay denied. A convergence-failure section is not required, because the loop did not hit 10 rounds.

| Unresolved unit | Why | Retries | Queries exhausted | What it blocks |
| :--- | :--- | :--- | :--- | :--- |
| Accuracy pair | Opened rates miss the bars, or the page prints only an equal-error rate | 1 of 2 | The four G1 round-3 searches were denied. This cluster was not given a further query in this pass | K2, until G4. K2 stays UNTESTED |
| Pipeline cost | The four-component total is unpublished | 1 of 2 | Same denial. This pass did not search | K1, until the G2 model and the G4 measurement. K1 stays UNTESTED. E-OSS-055 |
| India tariffs and vendor cards | Retail OTP, inbound voice, and the two per-second prices are unpublished in the filings opened | 1 of 2 | Same denial | C-MKT-01, C-MKT-03. Both stay open. E-MKT-071, E-MKT-031, E-MKT-032 |
| Phase-1 latency | No p95 on the banking-app channel | 1 of 2 | Same denial | K3, until G4. K3 stays UNTESTED |
| Clone sentence | The opened offence sections do not contain it. The 10 February 2026 gazette was not opened | 1 of 2 | Same denial | K6, until the G2 reading. K6 stays UNTESTED. This market document does not supply that reading |

Also open, and not resolved here: C-00 (₹0.30 per minute and 30 pence), C-ACA-01 (no watermark false-alarm rate under the named codecs together with replay and voice conversion), C-ACA-02 (speech-to-speech percentiles that do not share a turn count and a GPU with the conflicting mean), and the phrase "verification baseline."

`ledger/CONTRADICTIONS.md` contains adjudication language, prices, and a component stack. This assessment does not adopt that language. G4 is not open. No architecture is selected. The contradictions named in this section stay open.

The 53 Q2 rows remain known gaps. They are not deleted, and they are not treated as passes or as kills.
