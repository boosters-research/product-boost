# Moat audit — ledger synthesis

**Run:** 2026-11-24-myai-myagent
**Worker:** moat-auditor
**When:** G2 is open. G4 is not open.
**Inputs:** `ledger/EVIDENCE.md`, `ledger/CONSTRAINTS.md`, `KILL-CRITERIA.md`. No new sources.
**Scope:** Phase 1 is phone banking in the mobile app with Audio Signature (`E-USER-005`). A generative voice clone is off the transaction path (constraint 4). No architecture is selected (constraint 10).

This file is the moat-auditor synthesis for later use in market feasibility. It does not edit `deliverables/01-MARKET-FEASIBILITY.md`, the ledger, or the kill file. It does not mark K1–K6. It does not assign a PAVR score.

Hamilton Helmer’s scale is 0 (non-existent) to 5 (formidable). A power is **UNPUBLISHED** when the opened ledger does not measure that power. An unpublished power has no integer.

## Seven Powers

| Power | Score | Ledger basis | Why there is no integer |
|---|---|---|---|
| Scale Economies | UNPUBLISHED | `E-OSS-055`, `E-MKT-059`, `E-USER-001` | The four-component per-minute cost is unpublished. Company gross margins are not a unit-cost curve. |
| Network Effects | UNPUBLISHED | `E-USER-005` | No row measures value changing as users or nodes are added. |
| Counter-Positioning | UNPUBLISHED | `E-MKT-022`, `E-MKT-026`, `E-MKT-079` | The opened voice-ID notices do not state that a copy would cannibalize an incumbent’s core revenue. |
| Switching Costs | UNPUBLISHED | `E-USER-005`, `E-MKT-026` | No row measures embedded data, workflow, or integration for this product. |
| Branding | UNPUBLISHED | `E-VOC-015`, `E-VOC-016`, `E-VOC-017`, `E-VOC-018`, `E-VOC-019` | No row measures a price premium or trust asset for this product. |
| Cornered Resource | UNPUBLISHED | `E-ACA-001`, `E-OSS-034`, `E-OSS-011`, `E-OSS-013` | No row assigns an exclusive right. Opened error rates and public licenses are not that right. |
| Process Power | UNPUBLISHED | `E-OSS-055` | No architecture is selected, and no proprietary operating process is measured. |

### Scale Economies — UNPUBLISHED

Scale economies require unit cost to fall as volume rises. `E-OSS-055` states that a per-minute currency total covering streaming ASR, an SLM or LLM, voice-clone or TTS, and SIP or WebRTC, with the arithmetic and the hardware, is unpublished in the sources opened on 2026-11-24. OneMeta’s USD 0.30 to 0.36 per minute in that row is a wholesale interpretation price, not this pipeline. Partial ASR and TTS figures stay unadded (constraint 17). `E-USER-001` prints both ₹0.30 per minute and 30 pence. Those are the user’s ceiling readings. They are not a measured cost curve. C-00 stays open. This file does not convert one reading into the other.

`E-MKT-059` states that no filing, regulator report, or named-methodology survey opened on 2026-11-24 gives the gross margin of one telecom VAS contract or one banking voice-agent contract. The percents in `E-MKT-040` through `E-MKT-050` are company-level, an undefined product-margin KPI, or a derived residual. Company gross margin is not a moat and is not this score. The 12-month payback window and the 50% gross-margin floor remain unfrozen (constraint 16). `E-MKT-052`, `E-MKT-053`, and `E-MKT-057` leave CAC payback months unpublished for the contract classes those rows name, so the 1.5× CAC buffer has no payback input here.

`E-MKT-037` is one Indian CPaaS list card with volume bands. It is not this product’s unit cost.

### Network Effects — UNPUBLISHED

Network effects require the product to become more valuable as more users or nodes join. No ledger row measures that change. `E-USER-005` states the anchor use case as phone banking in a mobile app, with transaction authorization by Audio Signature and no SMS OTP, plus a requirement to integrate with telco IMS/SIP, VoLTE/5G media servers, and banking core APIs. That sentence is user-asserted. It is not a measurement that one additional subscriber raises value for another. External P2P and the general life-KB stay in Phase 2 until CPI is scored from evidence (constraint 5). This file does not treat that later phase as a network.

### Counter-Positioning — UNPUBLISHED

Counter-positioning requires that an incumbent’s copy would cannibalize the incumbent’s own core revenue model. The voice-ID withdrawals quoted in the fast-follower section are exits and replacements. `E-MKT-022` names Pindrop or an SMS one-time PIN as Amazon’s transition. `E-MKT-026` names a phone-banking PIN reset with an ATM PIN plus SMS OTP, or an HSBC ATM in Hong Kong, as HSBC Hong Kong’s replacement. `E-MKT-079` records removal of speaker recognition “due to the service retirement” and states no revenue effect. None of those sentences states damage to a core revenue line from continuing or copying the feature. A zero would assert that cannibalization was measured and found absent. It was not measured. The score stays unpublished. The withdrawal facts themselves are in the fast-follower section and are not discarded.

### Switching Costs — UNPUBLISHED

Switching costs require data, workflow, or integration to be deeply embedded in customer operations. No row measures that depth for this product. Constraint 7 locks the Phase 1 proof channel as the banking app. IMS/SIP and VoLTE/5G stay later tests of the same 800 ms line. `E-USER-005` names those integrations as a requirement. A requirement is not an embedded switching cost.

`E-MKT-026` records that HSBC Hong Kong stopped supporting phone-banking Voice ID and replaced that login. That notice shows one bank’s customer communication about a method change. It does not measure the cost, for this unbuilt product, of leaving an Audio Signature workflow. It is reported below and is not converted into an integer.

`E-SIM-001` through `E-SIM-019` are synthetic. Constraint 18 keeps synthetic interviews out of CPI and out of prices. Each of those rows states that T4 alone cannot support a material claim. They are not a switching-cost score.

### Branding — UNPUBLISHED

Branding requires a brand that commands pricing power and organic trust. No row names a brand for this product, a price premium, or a trust asset. Constraint 12 records India customer quotes on voice authentication in the voc-1 set as 0. The voice-authentication quotes that were rowed are outside India: a UK Voice ID failure and an opt-out request (`E-VOC-015`), a UK removal of First Direct voice ID back to security questions (`E-VOC-016`), an Australia ANZ Voice ID failure (`E-VOC-017`), a Canada Scotiabank voice-recognition lockout (`E-VOC-018`), and a Canada TD voice-recognition account that calls the calls easy (`E-VOC-019`). Those rows are T4. They are not a brand score.

### Cornered Resource — UNPUBLISHED

A cornered resource is exclusive IP, talent, a proprietary dataset, or an exclusive license possessed by this product. No ledger row assigns any of those.

Opened equal-error rates are public evaluation results. They are not a cornered resource, and they are not given a number on this scale:

- `E-ACA-001`: at the SASV 2022 threshold, FAR = FRR = 0.13% on ASVspoof 2019 logical-access TTS, voice conversion, and hybrid TTS-VC. Replay is not in that protocol. 0.13% is 130 times the FAR line of 0.001%. It is not 0.001%.
- `E-OSS-034`: the same challenge’s top listed submission, IDVoice, is SASV-EER 0.13%. The paper’s open-source links are the ECAPA, AASIST, and SASV baseline repositories. Constraint 13: the 0.13% figure is not an open-source toolkit FAR/FRR result.
- `E-ACA-010`: VLSP 2025, the opened protocol that includes voice conversion, replay, and TTS together, reports SASV-EER 20.79% on the public test and 17.78% on the private test.
- `E-OSS-020` and `E-OSS-021`: ECAPA FAR 1.73% and FRR 1.68% on zero-effort YouTube pairs. The experiment describes no replay, TTS, or voice conversion.
- `E-OSS-022` and `E-ACA-060`: on the VoiceWukong English replay subset, AASIST2 is FAR 5.62% and FRR 72.59% at the equal-error point.

K2 stays untouched. An equal-error rate near 1%, and the 0.13% point, are not a pass of FAR < 0.001% and FRR < 1.0% together under all three attacks (constraint 3, constraint 13).

Public component licenses are other parties’ terms. `E-OSS-011` states ChatTTS code under AGPLv3+ and the model under CC BY-NC 4.0. `E-OSS-013` states Vocal under SSPL-1.0, with a service-source condition for offering it as a managed service. Constraint 17: those are license flags, not a stack choice. They are not an exclusive right held for this product. This file does not select either component.

### Process Power — UNPUBLISHED

Process power requires proprietary operational complexity that yields a measured speed or quality advantage. Constraint 10: no technical architecture is selected. `E-OSS-055` leaves the full-pipeline cost unpublished. Opened latency rows are not a proprietary process and are not used to pick a path. G4 is not open, so this file contains no path measurement against the 800 ms line.

## Big Tech fast-follower test

**Question.** What happens when Microsoft, Google, Salesforce, or Apple announces this exact feature at their next developer conference?

**Answer from the opened ledger.** The ledger does not show an asymmetric advantage that would stop that announcement from commoditizing Audio Signature. It shows specific voice-ID withdrawals, and it shows silence in named statutes. Silence is not a moat and not a ban.

### What the ledger shows about incumbent voice-ID withdrawals

**Amazon Connect Voice ID.** `E-MKT-022` (AWS documentation): new customers stopped on 20 May 2025, support ends on 20 May 2026, and the named transition options are Pindrop or an SMS one-time PIN. No Pindrop price is on that page. `E-MKT-021` (the Connect pricing appendix): Voice ID at $0.025 per transaction, counting enrollment, identity verification, and fraud check separately, discontinued effective 20 May 2026, with new-customer access no longer available. The $0.025 row is a vendor rate card. `E-MKT-025` (Auraya press release) also states that AWS Voice ID is at announced end-of-support. The named next step in the AWS documentation includes SMS one-time PIN, which is the factor Phase 1 proposes to drop (`E-USER-005`).

**Microsoft speaker recognition.** `E-MKT-023` (a Microsoft external-staff answer on Microsoft Q&A): Speaker Recognition was retired on 30 September 2025 and is no longer available. That page is not a separate retirement bulletin, and it states no Azure speaker-recognition price. `E-MKT-079` (Speech service release notes): Speech SDK 1.47, the November 2025 release, removed speaker recognition samples and removed speaker recognition support due to the service retirement, and those notes do not state 30 September 2025. `E-MKT-080`: the page fetched at the speaker-recognition overview URL on 2026-11-24 does not contain the words Speaker Recognition or that date, and the Azure Updates page for id `azure-ai-speaker-recognition-retirement` returned an empty update list that does not contain that date. The retirement clause is in the SDK notes and the Q&A answer. The calendar date is in the Q&A answer.

**Nuance Gatekeeper, as two conflicting secondary accounts.** `E-MKT-024` (CXToday, 14 August 2025, quoting SymNex founder Matt Smallman): Gatekeeper has not been officially on sale since July 2024, is still being bought, and has no end-of-life date. `E-MKT-025` (Auraya, 17 July 2025): Microsoft’s Nuance Gatekeeper is at end-of-sale. The ledger marks those rows as conflicting on whether Gatekeeper has a formal end-of-sale. This file does not resolve that conflict. The “80–90 percent” share line in the CXToday article is the consultant’s, not a filing, and it is not used.

**Google Speaker ID references.** `E-MKT-024` reports that Google removed Speaker ID references about two months after May 2025. The same row states that no Google retirement notice was opened. `E-MKT-032` still lists Google Cloud Conversational Agents voice Flows at $0.001 per second and voice Playbooks at $0.002 per second. That is a voice-agent list price. It is not a speaker-ID withdrawal, and it is not evidence that Google will or will not add biometrics. `E-MKT-075` and `E-MKT-076` leave a Dialogflow voice price unpublished in the Alphabet 10-Ks that were opened. C-MKT-01 stays open. No winner is chosen between `E-MKT-031` and `E-MKT-032`.

**HSBC Hong Kong phone-banking Voice ID.** `E-MKT-026` (HSBC Hong Kong customer notice): from 18 August 2024 the bank no longer supports phone-banking authentication via Voice ID. The replacement login is a 6-digit Phone Banking PIN, reset with an ATM PIN plus SMS OTP or at an HSBC ATM in Hong Kong. The row states that this scout did not open a UK Voice ID closure. `E-MKT-081`: four HSBC account-opening releases hosted on hkma.gov.hk do not state that 18 August 2024 ending, and no HKMA regulator notice of that ending and no separate HSBC PDF of that ending were opened. The customer notice remains the opened statement of the change. The HKMA-hosted set does not corroborate it.

**OpenAI’s recommendation.** `E-MKT-038`: on 29 March 2024 OpenAI said it was previewing and not widely releasing Voice Engine, and it encouraged phasing out voice-based authentication as a security measure for bank accounts and other sensitive information. The ledger states that this is a recommendation, not evidence that banks stopped paying for voice biometrics.

**What those withdrawals are.** They are exits from named voice-ID features, with replacements that the notices actually name: an SMS one-time PIN or Pindrop (`E-MKT-022`), and a PIN plus SMS OTP (`E-MKT-026`). An exit is not a finding that Microsoft, Google, Salesforce, or Apple would damage a core revenue line by announcing Audio Signature. Pindrop remains a named alternative, and its price is unpublished (`E-MKT-022`), so the AWS notice does not empty the category.

**Apple and Salesforce in this ledger.** No row describes an Apple voice-ID product or an Apple withdrawal. No row describes a Salesforce voice-ID withdrawal. `E-ACA-024` is a Salesforce AI Research latency tutorial. It is not a product announcement and not a cannibalization statement. Voice-agent list prices that were opened for other vendors, including Twilio Conversation Relay at $0.07 per minute on the US Voice page (`E-MKT-031`), Genesys Cloud CX seat prices (`E-MKT-033`), and Five9 seat prices (`E-MKT-034`), are rate cards. They are not a moat for this product and not a forecast of a conference announcement.

### What the ledger shows about silence in the statutes

Silence is not a moat and not a ban. It is not a pass of K4 or K6 (constraint 11). This file does not mark either criterion.

**Voice biometrics in place of SMS OTP.** `E-MKT-002`: the Reserve Bank of India authentication directions of 25 September 2025 are silent on whether voice biometrics may replace SMS OTP. Paragraph 5(f) lists SMS-based OTP and “fingerprint, or any other form of biometrics (device native or Aadhaar based)” and does not name voice. The introduction says no specific factor was mandated and that the ecosystem has primarily adopted SMS-based OTP. `E-MKT-003`: the Digital Payment Security Controls directions of 18 February 2021 are silent on the same question. Paragraph 33 requires multi-factor authentication with at least one methodology generally dynamic or non-replicable, and gives OTP and biometric as examples. Paragraph 61 says regulated entities may consider alternatives to SMS-based OTP where the additional factor and the mobile application reside on the same device, and it does not name voice.

**A ban on a subscriber voice clone placing or conducting calls as that subscriber.** The opened texts contain no such clause:

- RBI authentication directions of 25 September 2025 (`E-MKT-005`).
- RBI Digital Payment Security Controls of 18 February 2021 (`E-MKT-006`).
- Digital Personal Data Protection Act, 2023 (`E-MKT-007`).
- Regulation (EU) 2016/679 (`E-MKT-010`).
- Telecommunications Act, 2023 (`E-MKT-011`).
- Telecommunications (Telecom Cyber Security) Rules, 2024 (`E-MKT-012`).
- Telecom Commercial Communications Customer Preference (Third Amendment) Regulations, 2026 (`E-MKT-013`).
- DoT advisory of 18 February 2025 (`E-MKT-019`), which addresses calling-line identification spoofing.
- Bharatiya Nyaya Sanhita section 319 (`E-MKT-061`). The row states that silence in this section is not a pass and not a breach.
- Information Technology Act section 66C (`E-MKT-063`) and section 66D (`E-MKT-065`). The same limit is stated on those rows.

`E-MKT-013` is silent on the subscriber-clone prohibition and, in the same instrument, defines an A2P call to include artificial voice technologies and treats a Sender’s undeclared A2P call as unsolicited commercial communication. That declaration rule is not an exclusive position and not a ban of a subscriber’s own-voice clone.

**What the silence does not remove.** `E-MKT-010`: GDPR Article 9(1) prohibits processing of biometric data for the purpose of uniquely identifying a natural person unless an Article 9(2) condition applies. Article 4(14) gives “facial images or dactyloscopic data” as examples and does not name a voice clone or a telephone call. Silence on the call prohibition leaves Article 9 in place. `E-MKT-060`, `E-MKT-062`, and `E-MKT-064` still state the personation and “unique identification feature of any other person” offences. Those offences are not, on the opened sentences, a prohibition of a subscriber using a clone of their own voice (`E-MKT-061`, `E-MKT-063`, `E-MKT-065`).

**Retention numbers are for other classes.** `E-MKT-008`: the DPDP Act states no numeric retention limit for transactional SMS or call transcripts. `E-MKT-009`: GDPR states no such number. `E-MKT-014` and `E-MKT-015` state a one-year minimum in the DPDP Rules for personal data, traffic data, and logs of processing, and those sentences do not name transactional SMS or call transcripts. `E-MKT-016` states “Three years” in the Third Schedule for classes whose cleanly extracted purposes concern access to a user account and access to a virtual token. Constraint 11: those rules do not state a number for transactional SMS or call transcripts.

**A different jurisdiction names voice recognition.** `E-MKT-066`: Bangko Sentral ng Pilipinas Circular No. 1213 lists voice recognition as an example of biometric authentication inside a set of strong authentication mechanisms for certain institutions. The opened circular contains no sentence that rejects voice authentication. The row states that this is a Philippines circular, not an RBI direction, and that K4 is not given a status. A foreign example list is not an exclusive license and not an RBI acceptance of this design.

### What a conference announcement meets

A Microsoft, Google, Salesforce, or Apple announcement of this feature meets public challenge results, public component licenses, statute texts that do not reserve voice biometrics for a new entrant, and incumbent exits whose named replacements include SMS OTP. None of those is an asymmetric advantage recorded in the ledger. This file does not predict that the announcement will happen, and it does not predict that it will fail.

## Data gravity and flywheel

Unpublished. No row shows customer usage producing a proprietary feedback set that improves accuracy or retention. `E-USER-004` requires a zero-retention LLM gateway. That is a user requirement, not a measured data asset. The public evaluation points in the cornered-resource section are challenge and paper results. They are not a feedback loop owned by this product. K2 is not marked.

## Bases refused as scores

- Company gross margins in `E-MKT-040` through `E-MKT-050`, and the contract-level gap in `E-MKT-059`, are not Scale Economies and not Process Power.
- `E-MKT-055` and `E-MKT-056` are not measurements. `E-MKT-083` and `E-MKT-084` leave the IndiaML benchmark table and a Gnani.ai gross margin above 80% unpublished as primary figures. They are not a moat.
- The equal-error rates listed under Cornered Resource are not a cornered resource.
- Statute silence is not a regulatory moat.
- `workers/prior-contaminated/` is not cited.

## Unpublished powers

All seven: Scale Economies, Network Effects, Counter-Positioning, Switching Costs, Branding, Cornered Resource, Process Power.
