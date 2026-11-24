# QUERIES — voice-of-customer-1

**Run:** 2026-11-24-myai-myagent
**Retrieved:** 2026-11-24
**Question:** RQ-6, retail banking customers, in their own words, on IVR transfers, SMS OTP failure or fraud, and voice authentication.
**Rule:** three framings per theme (insider, buyer, skeptic). Dead ends are listed so a retry uses a different string. Carrier IVR and caller tunes were not queried for quotation. Those belong to voc-2.

## Queries that produced a ledgered quote

| Framing | Query | What was opened and kept |
|---|---|---|
| Buyer, IVR | `bank IVR transferred phone banking reddit hate hold queue "I"` | Pointed at the RBC thread. The HTML thread was not used. The JSON was opened and kept as E-VOC-005 and E-VOC-019. |
| Insider, IVR | `"phone banking" IVR "transferred" OR "hold" site:reddit.com` | ICICI r/india and IndusInd r/CreditCardsIndia. JSON opened. Kept as E-VOC-001 through E-VOC-004. |
| Skeptic, IVR | `"transferred me" OR "kept transferring" bank IVR OR "phone banking" "another department" customer` | Trustpilot Chase page 7 opened. Kept as E-VOC-007. RBS page 9 was opened from the voice-ID Trustpilot search below and kept as E-VOC-006. |
| Buyer, OTP | `SMS OTP not received bank India reddit "OTP" fraud OR failed` | Pointed at the phishing thread and at delivery-failure threads. The phishing JSON was opened later and kept as E-VOC-014. |
| Insider, OTP failure | `"OTP" "not received" OR "didn't receive" OR "not getting OTP" bank HDFC OR SBI OR ICICI site:reddit.com` | HDFC card thread, SBI NRO thread, SBI YONO thread. JSON opened. Kept as E-VOC-008, E-VOC-009, E-VOC-010, E-VOC-011. |
| Skeptic, OTP fraud | `"OTP" "never came" OR "did not receive" OR "gave the OTP" bank fraud reddit India customer` | HDFC debit-fraud thread and the HDFC credit-card thread. JSON opened. Kept as E-VOC-012 and E-VOC-013. |
| Insider, voice | `"voice ID" OR "voice recognition" bank "doesn't recognize" OR "couldn't verify" OR "locked out" reddit` | Scotiabank thread opened as JSON. Kept as E-VOC-018. |
| Buyer, voice | `"voice ID" OR voiceprint bank review "I" Trustpilot OR Mouthshut OR productreview.com.au` | Trustpilot RBS page 9 opened. Aaron W kept as E-VOC-006. |
| Skeptic, voice | `"Voice ID" "failed" OR "wouldn't recognise" OR "did not recognise" bank customer review Trustpilot OR reddit` | MoneySavingExpert threads opened. Kept as E-VOC-015 and E-VOC-016. ANZ thread JSON opened from an earlier result of this cluster and kept as E-VOC-017. |

## Dead ends

These strings, or these page opens, did not yield a quote that is in the ledger. A retry should not repeat them.

1. `https://old.reddit.com/...` for the IndusInd, HDFC OTP, LifeProTips, Scotiabank, and SBI NRO threads. Each returned a login wall. Replacement: the same thread with `.json` appended.
2. `"voice ID" OR "voice biometric" OR "voice password" OR "voice recognition" HDFC OR SBI OR ICICI OR Axis customer reddit OR mouthshut`. Results were an ICICI annual-report page, an ICICI 2015 press release, a 2015 Business Standard article, a 2018 Times of India article about SBI, and a 2018 ET CIO commentary. No customer sentence. This is why the India voice-authentication count is 0.
3. `https://www.productreview.com.au/listings/anz-online` was opened. The body returned on 2026-11-24 did not contain the Voice ID sentence that a search snippet had attributed to that listing. That snippet was not quoted.
4. `https://www.trustpilot.com/review/www.santander.co.uk?page=2` and `page=4` were opened. David Fury's review is cut at "The Cha... See more". The unfinished sentence was not quoted. Query that found it: `"use my voice as my password" Santander Trustpilot David Fury`.
5. `https://uk.trustpilot.com/review/www.mbna.co.uk?page=3` was opened. The voice-recognition sentence in the search snippet was not on the page returned. Not quoted.
6. `https://www.reddit.com/r/CreditCardsIndia/comments/1iqa9ww/credit_card_fraud.json` — the original post body is `[removed]`. Only later comments by AmbassadorNo1503 were quoted (E-VOC-012).
7. `https://www.reddit.com/r/CreditCardsIndia/comments/1nmk255/not_receiving_any_otps_for_hdfc_cards.json` — the original post body is `[deleted]`. Only visualartist47's comments were quoted (E-VOC-010).
8. `https://www.reddit.com/r/AusFinance/comments/1e1dsjf/anz_cybersecurity_is_making_me_want_to_switch.json` — the original post is `[removed]`. The voice-ID comment is present and its author is `[deleted]`. That comment is E-VOC-017. The search snippet's username was not on the fetched JSON and was not used.
9. `https://www.reddit.com/r/LifeProTips/comments/131fg0h/lpt_opt_out_of_voice_authentication_from_your.json` was opened. A search snippet named hipsiguy and a branch-reset story. That author was not in the JSON returned. Not quoted. A comment by NotARealPerson6969 describes authenticating clients, which is a worker's account, not a retail customer. Not quoted.
10. LifeProTips, generic "press 0 to reach a human" threads, and the Institutional Investor phone-menu table are not bank-customer verbatims about a named banking IVR. Not quoted.
11. Beyond Bank's Voice ID marketing page, the Kerala Police cyber-fraud notice, the Axis Bank fraud-awareness PDF, the LiveLaw report of a High Court order, and the Guardian Centrelink voiceprint article are not retail-banking customers speaking in a review or forum. Not quoted.
12. Airtel subreddit SMS-OTP thread (`r/Airtel`, "Sms otp issue") is a carrier handset thread. Left for voc-2's side of the line. Not quoted here.
13. `https://www.customerservicescoreboard.com/Bank+of+America/t/answer-phone`, the HSBC UK app-review page, the Westpac ProductReview page, and the Barclays Smart Money People page appeared in search. They were not used. The BofA text that was spilled is dated 2013 in the snippet, and the others were not lifted into a complete on-theme quote after the pages that were fully read.

## Pages opened on 2026-11-24 that the ledger cites

- https://www.reddit.com/r/india/comments/13qgebc/fuck_icici_banks_voice_assistant_bullshit.json
- https://www.reddit.com/r/CreditCardsIndia/comments/1jke3pp/stuck_in_indusind_banks_ivr_maze_need_a_way_to.json
- https://www.reddit.com/r/PersonalFinanceCanada/comments/18bj1i1/tip_bypass_voice_assistant_on_some_banks_by.json
- https://www.trustpilot.com/review/personal.rbs.co.uk?page=9
- https://ca.trustpilot.com/review/jpmorganchase.com?page=7
- https://www.reddit.com/r/nri/comments/1n063eb/sms_otp_stopped_being_received_on_registered.json
- https://www.reddit.com/r/CreditCardsIndia/comments/1nmk255/not_receiving_any_otps_for_hdfc_cards.json
- https://www.reddit.com/r/nri/comments/1v6w7lq/is_anyone_getting_otps_from_sbi.json
- https://www.reddit.com/r/CreditCardsIndia/comments/1iqa9ww/credit_card_fraud.json
- https://www.reddit.com/r/LegalAdviceIndia/comments/1nvw7rj/hdfc_debit_card_fraud_234_lakh_wiped_out_without.json
- https://www.reddit.com/r/LegalAdviceIndia/comments/1o2eavq/please_help_my_wife_got_scammed_by_clicking_the.json
- https://forums.moneysavingexpert.com/discussion/5937560/voice-id-is-not-reliable
- https://forums.moneysavingexpert.com/discussion/6654061/secure-use-of-voice-recognition-for-access
- https://www.nationaltradingstandards.uk/news/phone-scams-take-sinister-twist-as-victims-voices-cloned/
- https://www.reddit.com/r/AusFinance/comments/1e1dsjf/anz_cybersecurity_is_making_me_want_to_switch.json
- https://www.reddit.com/r/Scotiabank/comments/1dgwa55/bank_needs_to_update_voice_recognition_when.json
