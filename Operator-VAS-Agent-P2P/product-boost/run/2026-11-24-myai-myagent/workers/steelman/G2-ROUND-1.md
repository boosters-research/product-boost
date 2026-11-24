# Steelman Pass — G2 market feasibility and investment analysis — Round 1/10

Run: `2026-11-24-myai-myagent` · Gate: G2 · Round: 1/10 · Date: 2026-11-24

Sources opened for this pass: `deliverables/01-MARKET-FEASIBILITY.md`, `deliverables/02-INVESTMENT-ANALYSIS.md`, `ledger/CPI.md`, `ledger/CONSTRAINTS.md`, `ledger/CONTRADICTIONS.md`, `KILL-CRITERIA.md`, `workers/g2-moat/MOAT.md`, `workers/g2-pricing/PRICING.md`. No new search. No ledger row appended. The G2 pessimist pass was not read.

This pass selects no scenario, marks no kill criterion, and resolves no contradiction. C-00 stays OPEN. K1–K6 stay UNTESTED. G4 is not open. No architecture is selected. No PAVR score is assigned. No CPI is printed. The investment model is blank. A blank price leaves the sale untested. A blank model leaves the value unpublished. Neither blank is a valuation.

---

## Steelmanned scenario: none selected (PMF NOT COMPUTED for A, B, and C)

No lowest-scoring surviving scenario exists to name. Scenario A, Scenario B, and Scenario C each have PMF **NOT COMPUTED**. The feasibility assessment states that none is buried and that none is given a courtesy score under 40. Naming one of them as the underdog would be a selection. The user selects at the G2 packet. This pass does not.

The case that is under-weighted is the case that can be built without a score: an unprinted CPI and an unpublished price are unscored axes, and an unscored axis is not a measured zero. That case applies to every scenario still in the packet. It is a case for leaving the sale untested. It is not a case that any scenario has earned capital.

### The strongest case

The strongest case the opened record will bear has three parts. Each part stops where the record stops.

**The locked use case is a real object, and it is unpriced.** Phase 1, as locked, is phone banking in the mobile app with Audio Signature, and the generative clone is off the transaction path (E-USER-005, constraints 4 and 5). The feasibility assessment recommends Scenario A because it is the only scenario that stays inside that locked use case, and it states that the selection is not made. The investment memo records that recommendation and does not adopt it as an underwriting case. Both sentences can stand. The recommendation is a scope fact. The refusal to underwrite is a model fact. The model has no price to enter as ARPA for A, for B, or for C.

**Low evidence is sitting in the cells that a score would have used.** CPI-01 through CPI-04 are UNTESTED on frequency, severity, workaround quality, and willingness to pay. CPI-05 is UNTESTED on the first three and is 3 on willingness to pay, from E-MKT-027 only, on TruValidate Inbound Authentication for one US composite. That axis is a different product. No CPI is printed. The formula blocks a row with any axis UNTESTED. The anchor value proposition therefore has no CPI. That is a report of missing axes. It is not a measurement that the pain frequency is zero, that the severity is zero, or that willingness to pay is zero.

**The structural texts are in the ledger, and they do not close the design.** The Reserve Bank of India authentication directions of 25 September 2025 require two distinct factors for domestic digital payment transactions unless exempted, and they require a dynamically created or proven factor for transactions other than card-present. Paragraph 3's compliance date is 1 April 2026, which is before the run date 2026-11-24 (E-MKT-001). The feasibility assessment's account of the introduction is that the ecosystem has primarily adopted SMS-based OTP (E-MKT-002). The moat note's account of the same introduction adds that no specific factor was mandated. Paragraph 5(f) lists SMS-based OTP and device-native or Aadhaar biometrics and does not name voice. The 18 February 2021 directions are silent on voice replacing SMS OTP, and they say regulated entities may consider alternatives to SMS-based OTP where the additional factor and the mobile application reside on the same device (E-MKT-003). Phase 1 is in the mobile app. That same-device sentence is the strongest structural text beside the design. It does not name this Audio Signature. Silence is not an acceptance. K4 stays UNTESTED.

Entries that support a scenario while sitting under a different label:

| Entry | Where the record files it | Re-weight this pass will defend | Limit of the re-weight |
| :--- | :--- | :--- | :--- |
| E-MKT-003, same-device alternatives to SMS OTP | Silence on voice. Not a K4 result | A same-device additional factor is a class the 2021 text says regulated entities may consider. The locked proof channel is the banking app | The sentence does not name voice and does not accept this design |
| E-MKT-002, adoption of SMS OTP, and the moat note's reading that no specific factor was mandated | Status quo competitor | The adopted factor is a named incumbent. On the moat note's reading, the directions do not mandate that one factor as the only factor | Neither reading accepts Audio Signature. K4 stays UNTESTED |
| E-MKT-022, Pindrop named beside an SMS one-time PIN | Graveyard transition off Amazon Connect Voice ID | A named alternative remains in the category. The moat note states that the notice does not empty the category | Pindrop's price is unpublished. That price is not VM-PRICE |
| E-MKT-027, $420,000 a year | CPI-05 and Scenario C only | A budget-shaped annual figure exists in inbound authentication. Willingness to pay on that axis is 3. Confidence 0.64 | Different product. Flagged ASSUMPTION if reused. Per-call rate unpublished. Not divided by 12 million calls. Not CPI-01. Not ARPA |
| E-MKT-051, ₹1.20 per wireless subscriber per month | Scenario B revenue-mix share | A VAS mix line is printed for FY 2025-26, equal to 0.64% of per-subscriber revenue excluding GST. The comparative cell is ₹1.26 | Not this product's price. Not a gross margin. Subscriber count unpublished. Not multiplied |
| Company gross margins in E-MKT-040 through E-MKT-050 | Kept at company level, outside the model | Those reporting entities state company-level gross profit or revenue | E-MKT-059 withholds the contract margin. No multiple is applied. Not a valuation of this product |

The graveyard is part of the strongest case, on the narrow reading the record already uses. Amazon Connect Voice ID stopped new customers on 20 May 2025, and support ends 20 May 2026, with the named transitions Pindrop or an SMS one-time PIN (E-MKT-022). Microsoft Speech SDK 1.47 removed speaker-recognition samples and support because of the service retirement (E-MKT-079). An HSBC Hong Kong customer notice says phone-banking Voice ID login ended, replaced by a PIN reset with an ATM PIN plus SMS OTP or at an HSBC ATM in Hong Kong (E-MKT-026). The feasibility graveyard marks "does the cause apply to us?" as UNTESTED on those rows. OpenAI's 29 March 2024 post encouraged phasing out voice-based authentication for bank accounts. The ledger states that this is a recommendation, not evidence that banks stopped paying (E-MKT-038, confidence 0.39). C-MKT-02, whether Nuance Gatekeeper is still on sale, stays OPEN. A category with dated exits and a named continuing alternative is a category that has already been sold and already been left by some vendors. It is not a category the record has measured as unsellable for this design.

What this scenario-set wins on, that a PMF total cannot see, because no total was computed:

- The three offers are different objects. A is the locked Phase-1 use case. B is a declared A2P catalogue outside that proof channel. C drops the Audio Signature claim and keeps a per-call structure whose rate is unpublished. The feasibility assessment states that they do not differ by a demonstrated price order of magnitude, because every price point is unpublished. Optionality among them is a process fact. It is not a network effect. Network effects are UNPUBLISHED in the moat note.
- Defensibility is untested on capital, distribution, data, switching cost, technical path, and brand-for-us. The moat note leaves all seven powers UNPUBLISHED and assigns no integer. An unpublished power is not a score of 0. The moat note says a zero on counter-positioning would assert that cannibalization was measured and found absent. It was not measured.
- The 1 April 2026 date is already past. The feasibility assessment refuses two descriptions: an unopened window, and a mandate for voice. Both refusals hold. A past compliance date is evidence that the two-factor rule is already in force on the printed calendar. It is not evidence that SMS OTP is the only factor a later text could sit beside, and it is not evidence that this signature is that factor.

### What the scoring model misses

The PMF block was not filled. Pain acuteness, pain breadth, workaround weakness, willingness to pay, and timing are NOT COMPUTED for A, for B, and for C. The miss is the collapse a reader can still perform: treating NOT COMPUTED as a low score. The feasibility assessment already blocks that collapse. This pass repeats the block. Absence of a printed CPI is not a CPI below 20. Absence of a price is not a willingness-to-pay of zero. Absence of a retail OTP price leaves workaround quality UNTESTED (E-MKT-071). The inter-operator ceiling of up to Rs 0.05 is a charge between access providers (E-MKT-070, E-MKT-039). It is not the retail price a bank pays per OTP.

CPI-05's willingness-to-pay input is 3 out of 5. Mapping that single input to 60 points and weighting it by 20% would produce a partial 12 and would hide three unscored terms. The feasibility assessment refuses that partial. This pass agrees. The only non-T4 money signal in the packet is not the strongest PMF, because there is no PMF total, and it is not the price of Audio Signature.

The model also has nowhere to put a moat integer. The feasibility barriers table leaves capital, distribution, data, switching cost, and technical path UNTESTED on both sides. It prints a regulatory pair of 4 against and 2 for, and it says the 2 is a reading of the absence of an exclusive right, not a moat. The moat note, which that section does not use, prints every power as UNPUBLISHED. The investment memo uses the moat note as an absence record and assigns no integer. No Helmer integer is available to the PMF total. This pass does not supply one.

T4 forum quotes and synthetic interviews stay out of CPI and out of prices (constraint 18, `ledger/CPI.md`). India customer quotes on voice authentication in the voice-of-customer set: 0. Caller-tune charge quotes dated on or after 2024-11-24: 0. That count is an empty T4 set. It is not a census of Indian banks or of phone-banking users. Reachable-account counts are unpublished.

### The 3-year winning version

A winning version with customers, revenue, retention, or a moat integer is not in the ledger. This pass does not draw one.

The only winning shape the locked constraints can describe, if the user later selects the Phase-1 use case, is the use case itself: phone-banking acts inside the bank's own app, authorized by an enrolled live voiceprint, with the clone off that path. Production transfer authorization stays blocked while K2 is UNTESTED. No rupee cap is stated (constraint 6). Year-3 price, year-3 account count, year-3 margin, and year-3 cash are the unpublished lines in the investment memo's DCF assumption set. They are unpublished in every year.

### Where this case runs out

The case runs out at capital. The underwriting model is blank. Product price, four-component COGS, and the four Van Westendorp points are unpublished, so ARPA, gross margin, customers-to-breakeven, a revenue multiple, and a DCF are unpublished. All seven powers are unpublished. No scenario is selected.

The case also runs out at the bars the opened pages miss, without those misses becoming kills. The best joint point the constraints record under a replay condition is FAR 5.62% and FRR 72.59% (E-ACA-060). SASV 2022 prints FAR = FRR = 0.13% on TTS and voice conversion, without replay (E-ACA-001). That 0.13% figure is not the 0.001% bar. K2 stays UNTESTED. No Phase-1 speech-to-speech p95 is in the record. K3 stays UNTESTED. The four-component per-minute total is unpublished (E-OSS-055). K1 stays UNTESTED. The opened banking texts do not contain a sentence that accepts or refuses this design. K4 stays UNTESTED.

Company gross margins, OneMeta's USD 0.30 to USD 0.36 per minute, the partial ASR and TTS figures, the ₹1.20 mix, and the $420,000 composite fee are printed in the record and stay outside the model. They do not extend the case into a number.

---

## Pessimist audit

The G2 pessimist file was not read. The rows below are skeptical claims already printed in the G2 record this pass did open. They are audited as claims in that record. They are not attributed to the unread pass. No row below is a reply to that pass.

| Claim | Evidence | Tier | Verdict |
| :--- | :--- | :--- | :--- |
| No CPI can be printed. The anchor value proposition has no CPI. | `ledger/CPI.md`. CPI-01 through CPI-04 UNTESTED on every axis. CPI-05 WTP = 3 only, from E-MKT-027. Workaround quality blocked because the retail OTP price is unpublished (E-MKT-071) | E-MKT-027 is T2, confidence 0.64. E-MKT-071 is T1, confidence 0.77. The other CPI-01 axes are UNTESTED | The skepticism is evidenced as a missing score. It is not evidenced as a pain frequency of zero or a willingness to pay of zero |
| The underwriting model is blank, so no capital is committed | Investment memo Sections 1, 4, 7, and 10. VM-PRICE, COGS-TOTAL, and the four Van Westendorp points unpublished. E-MKT-057: the 1.5× buffer has no payback input | E-MKT-057 is T1, confidence 1.00. E-OSS-055 is carried as T2, confidence 0.90, for the absence of the four-component total. E-USER-001 is T1, confidence 0.90 | Evidenced. The blank is the result of the test. The same memo states that unpublished is not a pass of K1 or K5 and not a trip of K1 or K5. A blank model is not a valuation. A blank price is not proof the offer cannot be sold |
| Voice-ID products have already been left, and the adopted additional factor is SMS OTP | E-MKT-022, E-MKT-079, E-MKT-080, E-MKT-026, E-MKT-081, E-MKT-038, E-MKT-002 | Investment memo labels E-MKT-022 as T3, confidence 0.61. E-MKT-038 is confidence 0.39 in the feasibility graveyard. E-MKT-024 is confidence 0.47 and is not applied | The exits and the adoption sentence are evidenced. The feasibility graveyard marks the cause as UNTESTED for this design. E-MKT-038 is a recommendation, not evidence that banks stopped paying. Using those exits as proof that this offer cannot be sold would be over-broad. The documents do not take that step |
| The ledger does not show an asymmetric advantage against a fast-follower announcement of this feature | Moat note, fast-follower section. Public results, public licenses, statutes that do not reserve the design, and exits whose named replacements include SMS OTP | The moat note assigns no tier and no integer. It states that it does not predict that the announcement will happen and does not predict that it will fail | The absence of a recorded advantage is evidenced. A further claim that Microsoft, Google, Salesforce, or Apple will respond well, or that the announcement will commoditize the design, is not the sentence the moat note prints. That further claim would be incumbent omniscience. It is not adopted here |
| Regulatory pressure against entry is real | E-MKT-010 Article 9(1), E-MKT-001, E-MKT-002, E-MKT-013. Feasibility prints 4 against and 2 for | The feasibility file calls these ratings judgments. The 2 is described there as a reading of absent exclusivity, not a moat. The moat note prints no integer and says statute silence is not a regulatory moat | The statutes are evidenced. The integers are judgments. This pass does not convert 4 or 2 into a Helmer score, and it does not convert UNPUBLISHED into 0. K4 and K6 stay UNTESTED |
| Brand and trust weigh against this product | Feasibility brand/trust row: 4 against, carried by E-MKT-022, with E-MKT-038 at confidence 0.39 not carrying the rating. For-us cell UNTESTED | E-MKT-022 as labeled in the investment memo: T3, 0.61 | The dated end of Voice ID support is evidenced. No trust asset for this product is in the ledger. The integer 4 is a judgment about an unbuilt product. Moat Branding is UNPUBLISHED. Both of those limits stand |
| Demand risk is high impact and high probability because CPI-01 is unprinted | Feasibility Section 11. The cell says impact and probability are judgments and do not change K1–K6 | The missing CPI is the evidenced state. No frequency in the ledger is the probability | The evidence gap is real. A probability that demand fails is not a measured frequency. The section's own mitigation is to keep CPI-01 unprinted until the axes exist |
| General B2B SaaS margins, a "about 12 months" sentence, or one commissioned payback govern this contract | E-MKT-054, E-MKT-082, E-MKT-057 | E-MKT-054 is T2, 0.64, and is a different category. Median payback months are unpublished in its text layer. E-MKT-082 is T2, confidence 0.38, one commissioned customer, and is not a K5 input | The documents already refuse the misapplication. This pass agrees. Those figures do not enter CAC, payback, or the DCF |

### Unevidenced skepticism flagged

- **Unevidenced doubt, if WATCH is read as a failed sale or as a value of zero.** The investment memo computes no valuation. It states that unpublished is not a trip of K1 or K5. Absence of a price is not proof the offer cannot be sold, and it is not a valuation.
- **Unevidenced doubt, if an unpublished power is read as 0.** The moat note withholds the integer because the power was not measured. Counter-positioning is the explicit case: a zero would assert a measurement that was not made.
- **Over-broad survivorship.** The graveyard's "does the cause apply to us?" column is UNTESTED. The commercial reason for the Voice ID stop is not stated beyond the stop and the end date. HSBC Hong Kong's notice is not an RBI decision. A Philippines circular that lists voice recognition is not the applicable control (E-MKT-066).
- **Incumbent-omniscience, if added on top of the moat note.** The note records specific withdrawals and statute silence. It does not record that a named platform will ship this feature and win.
- **Base-rate misapplication, already refused in the memo.** Pavilion medians, the "common wisdom often says about 12 months" sentence, pure-software 75–85% bands, and AI-heavy 60–70% bands are not this product's floor. Constraint 8 leaves the 12-month window and the 50% gross-margin floor unfrozen. This pass does not apply them.
- **Materiality inflation.** This pass does not open a further round, does not reclassify an unpublished cell as a kill, and does not spend a G1 round 3. Constraint 18 records that the judge loop stopped because the round-2 coverage gain was 0.01, below 0.03. The five gap clusters stay open as gaps.

---

## What would have to be true

The investment memo's verdict is WATCH. Watch, in that memo, commits no capital, marks no kill, and selects no scenario. The notch it names next is Diligence, which is the notch at which the model can be filled. The memo does not reach Conviction. It does not say that a filled model is a commitment of capital.

A later packet can commit capital only on a model that can be computed for a scenario the user has selected. The rows below are that precondition, taken from the memo's load-bearing list and from the further blanks the same memo leaves unpublished. They are not a capital commitment. None of them is already true. This pass does not move WATCH.

| # | Must be true | Currently | Evidence needed | Gate that can test it | Cheapest test | Cost/time |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | The user has selected Scenario A, Scenario B, or Scenario C | Unselected. Feasibility recommends A and states that the selection is not made. The investment memo selects none | The user's selection at the G2 packet. A recommendation is not that selection | G2 packet. The selection is a user decision | The user names A, B, or C, or names none | UNPUBLISHED |
| 2 | The selected offer has a disclosed price that can be entered as ARPA. Another product's annual fee is not that price | VM-PRICE UNPUBLISHED for A, B, and C. $420,000, ₹1.20, the ceiling, OneMeta's USD 0.30–0.36, and every T4 card stay outside ARPA | A T1 or T2 row that states the price of the selected offer | G2 model. The current memo already ran and left the price unpublished. That result is not a failed sale and not a valuation. A later packet can enter the price when the row exists | A filing, a tariff, or a contract that states that price. Constraint 18: the four denied searches stay denied unless the user says RE-SCOUT | UNPUBLISHED |
| 3 | A four-component per-minute total exists, with the arithmetic and the hardware, and is set beside both ceiling readings. The readings stay unconverted | COGS-TOTAL UNPUBLISHED (E-OSS-055). Partials in E-OSS-006 and E-OSS-019 are excluded from any sum. ₹0.30 per minute and 30 pence are both printed (E-USER-001). C-00 stays OPEN. K1 stays UNTESTED | A sourced sum of streaming ASR + LLM/SLM + voice-clone TTS + SIP/WebRTC. A sum that omits a component is not a measurement | K1. G2 is the model test. G4 is the measured path. G4 is not open. The G2 model result is unpublished, which is not a clear and not a trip | The four-component sum, beside both readings, with no currency conversion | UNPUBLISHED |
| 4 | A CAC in currency and a new-customer ARR exist, so the locked 1.5× buffer has an input | Both missing (E-MKT-057). CAC_raw and buffered CAC are UNPUBLISHED. K5 stays UNTESTED. The 12-month window and the 50% floor are not applied (constraint 8) | Contract-level CAC in currency and new-customer ARR for a banking voice-agent contract or a telecom VAS contract, matching the selected offer | K5. G2. The current memo leaves the status UNTESTED. A later G2 packet can test K5 when the inputs exist. This pass does not freeze the assumption window or the assumption floor | A filing that states both missing terms. Five9's and NICE's sales-and-marketing dollars are not this CAC | UNPUBLISHED |
| 5 | The selected scenario has a CPI printed from four axes, each with a ledger id. Willingness to pay on that CPI does not rest on T4 alone | No CPI is printed. CPI-05's axis of 3 does not print a CPI and does not price Audio Signature | T1 or T2 evidence for frequency, severity, a workaround price, and willingness to pay for the selected offer. The retail OTP price is not the inter-operator Rs 0.05 ceiling | G2 market feasibility and `ledger/CPI.md`. This is not a kill criterion. The feasibility file states what a later printed CPI would do to the recommendation. Those conditions are not met, because no CPI is printed | Score the four axes from ledger ids, or leave the CPI unprinted | UNPUBLISHED |
| 6 | If the selected offer authenticates a payment, the applicable banking control's text is in the ledger | The opened RBI texts are silent on voice biometrics replacing SMS OTP (E-MKT-001, E-MKT-002, E-MKT-003). Silence is not that text. K4 stays UNTESTED. E-MKT-066 is a Philippines circular, not an RBI acceptance | A text of the applicable control that accepts this design, or a text that refuses it | K4. G1 and G2. Both have been used. Absence of the text is not a pass. This pass does not mark K4. A later G2 reading can test K4 when the text is opened | Open that control text. An assertion is not a measurement | UNPUBLISHED |
| 7 | Fixed monthly cost is stated on team, infra, tooling, and overhead, so customers-to-breakeven can be computed after ARPA and gross margin exist | All four parts unpublished. Contribution unpublished. Customers, months, and cash to breakeven unpublished at slow, base, and fast, for A, B, and C. No rate is selected | A sourced or user-frozen bill for each part, plus the price and the cost that make contribution computable | G2 model. The memo calls customers, timing, and cash the single most important number, and states that the number is unpublished | A costed operating bill for this product. Company operating costs of other issuers are not this bill | UNPUBLISHED |
| 8 | If the DCF the brief asks for is to be computed, a discount rate has a ledger id or is a frozen user assumption. Terminal growth or an exit multiple likewise has a source. Neither terminal method is selected in this packet | E-USER-006 asks for a DCF and states no rate. No venture discount rate, no perpetuity growth rate, and no revenue or ARR multiple is in the inputs. No public-market WACC is substituted | A ledger row or a frozen user assumption for the rate, and a sourced terminal input if a terminal value is computed | G2 model. The current memo selects neither terminal method and invents no rate | The user freezes a rate, or a sourced rate is opened. This pass invents neither | UNPUBLISHED |
| 9 | The four Van Westendorp points are stated, if a later packet treats them as part of the price record | VW-CHEAP, VW-BARGAIN, VW-EXPENSIVE, and VW-TOO-EXPENSIVE are UNPUBLISHED. CPI willingness to pay does not supply them | A ledger row for each point | G2 pricing. The Diligence list names a T1 or T2 price. It does not say the four points substitute for that price. Missing points are not proof the offer cannot be sold | A priced buyer study that states the four points, or the cells stay unpublished | UNPUBLISHED |

One of rows 1 through 4, without the others, leaves ARPA, gross margin, customers-to-breakeven, the multiple, or the DCF unpublished. That is the investment memo's own limit on moving from Watch to Diligence. Rows 5 and 6 are the memo's further load-bearing conditions. Rows 7 through 9 are blanks the same memo prints and does not fill. None of the nine is already true.

These items are untested and are not in the Diligence list. They are recorded so they are not silently marked, and so they are not silently promoted into extra capital hurdles.

| Item | Currently | Gate | This pass |
| :--- | :--- | :--- | :--- |
| K1, full-pipeline COGS strictly under the ceiling | UNTESTED. The G2 model has no sum | G2 model and G4 measured path. G4 is not open | Not marked |
| K2, FAR < 0.001% and FRR < 1.0% together under replay, generative deepfake, and voice conversion | UNTESTED. Opened points miss the bars. Production transfer authorization stays blocked while K2 is unmeasured (constraint 6) | G1 literature has been used. G4 is the chosen path. G4 is not open | Not marked. 0.13% is not cited as 0.001% |
| K3, speech-to-speech p95 < 800 ms on the banking-app channel | UNTESTED | G4 | Not marked |
| K6, a prohibition on a subscriber voice clone placing or conducting calls as that subscriber | UNTESTED. The clone stays off the transaction path (constraint 4). The opened offence sections do not contain the sentence. The 10 February 2026 gazette was not opened | G1 and G2 | Not marked. Silence is not a pass |

C-00 is not a row that evidence closes. The working ceiling is ₹0.30 per minute, and the brief also says 30 pence. A later packet that cites a cost prints both readings and does not convert them. The user closes C-00, or C-00 stays OPEN. This pass does not close it.

---

## Conflicts for user adjudication

**Do the feasibility recommendation and the investment WATCH verdict disagree on a material fact?** No.

Both documents state the same material facts: no scenario is selected, no CPI is printed, every product price point is unpublished, the model inputs for ARPA and COGS are unpublished, K1–K6 stay UNTESTED, and C-00 stays OPEN. The feasibility verdict is PROCEED WITH CONDITIONS, and the recommendation is Scenario A, because that scenario stays inside the locked Phase-1 use case. The same document states that the selection is not made. The investment verdict is WATCH. The memo records the recommendation and does not adopt it as an underwriting case. WATCH commits no capital. The difference is which decision each document is allowed to make. It is not a contradiction of a printed price, a printed CPI, a printed kill, or a printed selection. Absence of a price is not, on either document, proof the offer cannot be sold, and the blank model is not a valuation.

The G2 pessimist pass was not read, so no conflict below is a split against that pass. The conflicts the user must still see are the posture above, the register descriptions, the open register, and the integer-versus-unpublished powers. This pass resolves none of them.

### CONFLICT-1: Recommendation of Scenario A, and WATCH

**Feasibility position:** PROCEED WITH CONDITIONS. The recommendation is Scenario A. The selection is not made. The because-clause is the locked Phase-1 use case (E-USER-005, constraint 5). PMF is NOT COMPUTED. The change-mind conditions are a later printed CPI-01 below 20, or a later printed CPI-05 of at least 35 while CPI-01 stays unprintable, or an opened control text that refuses the design. None of those is in the ledger now.
**Investment position:** WATCH. No capital is committed. The recommendation is not adopted as an underwriting case. No scenario is selected (investment memo Section 10). The model is blank (VM-PRICE, COGS-TOTAL, E-MKT-057).
**What separates them:** A scope question and a capital question. Feasibility answers which scenario matches the locked use case. Investment answers whether a blank model can carry capital. They do not give different answers to either question.
**Cheapest resolution:** The user selects A, B, or C at the G2 packet, or selects none. This pass does not select.
**If unresolved, this blocks:** A later packet that treats the recommendation as an underwriting case, or that treats WATCH as a finding that the offer cannot be sold.

### CONFLICT-2: What the contradiction register contains

**Feasibility position:** `ledger/CONTRADICTIONS.md` contains adjudication language, prices, and a component stack. The assessment does not adopt that language. G4 is not open. No architecture is selected (feasibility Section 13).
**Pricing-note position:** `ledger/CONTRADICTIONS.md` records C1–C6 as resolved and attaches rupee amounts to those rows. Those amounts have no Evidence Ledger ID. The note leaves them unused. C-00, C-MKT-01, and C-MKT-03 stay OPEN (pricing note, opening).
**Register, as opened for this pass:** Status OPEN. G3 has not started. No contradiction in the register is resolved. The register states that rupee amounts on a claim of resolved C1–C6 have no Evidence Ledger ID and are not an adjudication.
**What separates them:** Whether the register itself contains a resolution, prices, and a stack, or whether it disclaims that material and stays OPEN. This pass does not open any other contradiction file and does not use any rupee amount from a resolved-C1–C6 claim.
**Cheapest resolution:** The user says which description binds. Until then, every contradiction named in the register stays OPEN, and no rupee amount from a resolved claim enters a price, a COGS, or a CPI.
**If unresolved, this blocks:** Any later use of a resolved stack, a resolved kill, a pipeline cost, or a CPI taken from that claim. Constraint 19 states that those claims are not in the evidence ledger. This pass does not use them.

### CONFLICT-3: Barrier integers and unpublished powers

**Feasibility position:** Regulatory is 4 against and 2 for. The 2 is a reading of absent exclusivity, not a moat. Brand/trust is 4 against, carried by E-MKT-022, and UNTESTED for this product. Other barrier types are UNTESTED. The section states that it does not use the moat note and that the note is not evidence.
**Moat note and investment position:** All seven powers are UNPUBLISHED. No integer is assigned. The investment memo says the feasibility file described the notes as pending, and that both notes are on disk as absence records. It uses the absences. It adds no source and no power score.
**What separates them:** A judgment integer in one instrument, and a refused integer in the other. They agree there is no demonstrated franchise and no Helmer score for this product.
**Cheapest resolution:** Leave both instruments visible. Do not average 4, 2, and UNPUBLISHED into a moat score.
**If unresolved, this blocks:** A defensibility rating that pretends the packet contains one agreed integer.

### Open register the user must still see

None of these is resolved in this pass.

| ID | Conflict, as the register states it | Status |
| :--- | :--- | :--- |
| C-00 | The brief's ceiling is written as under 30p per minute and also as 30 pence. Working unit is ₹0.30 per minute. Neither reading is converted | OPEN |
| C-MKT-01 | A Twilio card states $0.095 per second. A Google card states $0.001 per second. The opened filings do not contain either voice price. Alphabet's $0.001 in the 10-K is stock par value | OPEN |
| C-MKT-02 | Whether Nuance Gatekeeper is still on sale. Classified incidental in G1. Not decided | OPEN |
| C-MKT-03 | The TRAI Rs 0.05 transactional-SMS ceiling, unnamed 2024 estimates, a vendor OTP card, and a Jio consumer plan are different objects. Retail OTP and inbound voice prices are unpublished | OPEN |
| C-MKT-04 | OnMobile growth figures disagree. Classified incidental in G1. Not decided | OPEN |
| C-ACA-01 | Watermark false-alarm figures near 1%, and a much smaller figure under additive noise, are not a speaker false-accept rate under 0.001% | OPEN |
| C-ACA-02 | Moshi's 160 ms and 200 ms frame claims, a 737 ms p95 with no turn count, and a longer mean are different clocks | OPEN |
| Verification baseline | The brief uses that phrase for a generative clone. The locked signature is a live voiceprint, a dynamic challenge, and an app watermark. The phrase was not reconciled | OPEN |

Also still open, and not a contradiction id: the five G1 gap clusters in feasibility Section 13 (accuracy pair, pipeline cost, India tariffs and vendor cards, Phase-1 latency, clone sentence), each at 1 of 2 retries, and the 53 Q2 rows. They are gaps. They are not passes and they are not kills.

---

## Honest assessment

The investment memo is right about capital. A blank model cannot be asked to commit money. WATCH is the verdict that matches the inputs that were actually opened. This pass agrees with it. The agreement stops at the blank. WATCH is not a valuation, and it is not a finding that a bank, an operator, or a contact center will refuse a price that no row has stated.

The feasibility assessment is right that no CPI can be printed, that PMF is not a number, and that recommending Scenario A is not the same act as selecting it. This pass agrees. The recommendation's because-clause is the locked use case. That is a constraint. It is not a willingness to pay. A later printed CPI-01 below 20 would drop that recommendation, on the feasibility file's own change-mind line, and no such CPI exists to apply today.

The graveyard is real. A scaled vendor has dated the end of a voice-ID product and has named an SMS one-time PIN as a way off it. A bank notice in Hong Kong has named a PIN plus SMS OTP as a replacement. Those facts limit any claim that voice authentication for phone banking is an empty field waiting for this design. They do not, on the opened pages, state a false-accept rate for the withdrawal, and they do not state an RBI refusal. K4 stays UNTESTED. The cause-applies cell stays UNTESTED.

The moat note is right that no asymmetric advantage is recorded and that silence is not a moat. This pass agrees, and it does not add a prediction that a platform announcement will fail. All seven powers stay unpublished. The feasibility integers 4 and 2 stay judgments in that file. They are not adopted here as a score.

K1 through K6 stay UNTESTED. This pass marks none of them. The 12-month window and the 50% floor stay unfrozen. The 1.5× CAC buffer stays locked and unused. C-00 stays OPEN. No architecture is selected. G4 stays closed.

The optimistic case is the experiment queue in the table above. None of those rows is already true. Until a later packet has a selected scenario, a price for that scenario, a four-component cost, and a CAC with new-customer ARR, there is nothing in this record to underwrite. That queue is the whole of the case that survives contact with the ledger.
