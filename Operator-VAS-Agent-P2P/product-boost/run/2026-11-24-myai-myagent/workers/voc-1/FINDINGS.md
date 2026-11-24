# Voice of customer — RQ-6

**Run:** 2026-11-24-myai-myagent
**Worker:** voice-of-customer-1
**Retrieved:** 2026-11-24
**Question:** What do retail banking customers say, in their own words, about IVR transfers, SMS OTP failure or fraud, and voice authentication?
**Metric:** count of independent verbatims per theme. One independent verbatim is one author. India and other markets both count. The market is tagged on each quote.
**IDs used:** E-VOC-001 through E-VOC-019, each once.
**Not done:** no CPI score, no kill-criterion mark, no willingness-to-pay number. Carrier IVR and caller tunes are voc-2's question and are not in this file. `workers/prior-contaminated/` was not used.

Every quote below was read on a page fetched on 2026-11-24. Forum text, Reddit comments, Trustpilot free text, and MoneySavingExpert forum posts are T4. A T4 row can support a directional reading only when at least three independent T4 authors agree. It cannot support a material claim, a price, or a WTP axis by itself.

## Verbatim count by theme

| Theme | Independent authors | Ledger IDs | Markets in the set |
|---|---:|---|---|
| Bank IVR, including failure to reach a person and transfers between a menu, an agent, or a department | 7 | E-VOC-001 to E-VOC-007 | India 4, Canada 1, United Kingdom 1, United States 1 |
| SMS OTP failure (not delivered, or delivered only after repeated requests) | 4 | E-VOC-008 to E-VOC-011 | India bank / New Zealand resident 1, India bank / United States 1, India 2 |
| SMS OTP fraud (OTP shared with a caller, or a debit the customer says they did not authorise with an OTP) | 3 | E-VOC-012 to E-VOC-014 | India 3 |
| SMS OTP failure or fraud, combined | 7 | E-VOC-008 to E-VOC-014 | India plus the two NRI residencies above |
| Voice authentication | 5 | E-VOC-015 to E-VOC-019 | United Kingdom 2, Australia 1, Canada 2 |
| Voice authentication, India customers only | 0 | — | No customer verbatim opened |

Authors who share a thread are still different people. The pairs are E-VOC-001 with E-VOC-002, E-VOC-003 with E-VOC-004, E-VOC-005 with E-VOC-019, and E-VOC-008 with E-VOC-009. The fraud rows are three different URLs.

Of the 7 IVR authors, 3 use the word transfer or describe a department handoff: E-VOC-002, E-VOC-005, E-VOC-007. The other 4 describe a bank voice menu that will not connect them to a person.

## Quadrants

| Quadrant | Count | IDs |
|---|---:|---|
| Feature Gaps | 2 | E-VOC-001, E-VOC-003 |
| Workflow Friction / UX Pain | 5 | E-VOC-002, E-VOC-004, E-VOC-005, E-VOC-006, E-VOC-007 |
| Reliability & Performance | 11 | E-VOC-008 to E-VOC-018 |
| Pricing & Contract Hostility | 0 | — |
| Counterexample, not a pain quadrant | 1 | E-VOC-019 |

E-VOC-019 is praise: a TD customer in Canada said voice recognition made the call easy. It is ledgered so the set is not only complaints.

## Proposed VoC multiplier: 1.0

The count behind 1.0 is the 19 authors above.

- 12 authors describe friction, a failed OTP, or a hack they are still using (lost-card menu, pressing 0, resending the OTP, emailing the branch, a dispute). IDs: E-VOC-001, E-VOC-002, E-VOC-003, E-VOC-004, E-VOC-005, E-VOC-007, E-VOC-008, E-VOC-009, E-VOC-010, E-VOC-011, E-VOC-012, E-VOC-013.
- 4 authors use exit language, and all 4 are conditional, planned, or hypothetical. None records a completed switch to a named bank. E-VOC-006: "If they don't improve fast im moving to another bank." E-VOC-014: "We also planned to close both her CC." E-VOC-017: the accounts "would be shut down" if the amounts were frequent or time critical. E-VOC-018: "Was almost enough to switch everything over to another bank."
- 2 authors opted out of voice ID and stayed with questions or a PIN path. E-VOC-015, E-VOC-016.
- 1 author described voice recognition as easy. E-VOC-019.
- 0 authors state a price, a budget, or an amount they would pay for a replacement.

1.2 is the band for customers actively seeking an alternative today. Four conditional lines out of 19 are not that pattern. 0.8 is the band for a passive preference. An hour in a bank menu, a payment blocked because the SMS never arrived, and a debit the customer says arrived while they were asleep are not a passive preference. 1.0 is the band that matches this set: repeated complaint, usually with a hack.

This multiplier is an input. It is not a CPI score. CPI is not calculated here.

## Willingness to pay

No willingness-to-pay figure is stated. No quote names a price the customer would pay. Wanting a fraudulent debit returned is a restitution request, not a price. Exit language in this set is T4 only, so it cannot carry the WTP axis.

## Themes with fewer than 3 independent quotes

The three named themes, with India and other markets counted together, are each at or above 3: IVR 7, SMS OTP failure 4, SMS OTP fraud 3, voice authentication 5.

These slices are under 3:

- India retail-customer voice authentication: 0. The India search returned bank announcements and an annual-report description of voice biometrics. It did not return a customer sentence. See QUERIES.md.
- Pricing & Contract Hostility: 0 quotes in this set.
- Feature Gaps: 2 authors.

## Quotes

### E-VOC-001 — IVR — Feature Gaps — India

Platform: Reddit, r/india. Author on the fetched JSON: `[deleted]`. The post body was still on the page. Date: 2023-05-24. Role: retail customer calling ICICI customer care.

> I tried calling customer care and they introduced some garbage voice assistant. I can tell it agent, but then it wants to know if I want to ask about bank account, credit card or loan. I'm not looking for information on any of those, it's a completely different query that this stupid bot doesn't know how to handle.
>
> But it just won't get me to an actual human. Keeps insisting on trying to handle the queries itself.
>
> Useless IVRS shit needs to die.

URL opened: https://www.reddit.com/r/india/comments/13qgebc/fuck_icici_banks_voice_assistant_bullshit.json

### E-VOC-002 — IVR transfer — Workflow Friction — India

Platform: Reddit, r/india, same thread as E-VOC-001, different author. Author: gpahul. Date: 2023-05-24. Role: retail customer describing the ICICI path.

> Just go to the report scam/ATM lost, it will connect to cc and ask them to transfer the call to the relevant department without involving IVR.

URL opened: https://www.reddit.com/r/india/comments/13qgebc/fuck_icici_banks_voice_assistant_bullshit.json

### E-VOC-003 — IVR — Feature Gaps — India

Platform: Reddit, r/CreditCardsIndia. Author: memebanao007. Date: 2025-03-26. Role: IndusInd credit-card customer.

> I'm unable to connect to IndusInd Bank's customer care agent no matter what I try. I've called 3-4 different numbers, but every time, it's just an endless IVR loop with no option to speak to a real person. It’s frustrating! Does anyone know how to connect with a customer care executive? Any help would be appreciated

URL opened: https://www.reddit.com/r/CreditCardsIndia/comments/1jke3pp/stuck_in_indusind_banks_ivr_maze_need_a_way_to.json

### E-VOC-004 — IVR — Workflow Friction — India

Platform: Reddit, r/CreditCardsIndia, same thread as E-VOC-003, different author. Author: COHillur. Date: 2025-07-26. Role: IndusInd credit-card customer.

> I found the way after going through the maze for about an hour.
>
> NOTE: You should remember that a looping IVR message saying, "For better services use Indie, .....", will keep on coming, I thought it was a stuck message, but waited. And finally got to talk to the Phone banker.

URL opened: https://www.reddit.com/r/CreditCardsIndia/comments/1jke3pp/stuck_in_indusind_banks_ivr_maze_need_a_way_to.json

### E-VOC-005 — IVR transfer — Workflow Friction — Canada

Platform: Reddit, r/PersonalFinanceCanada. Author: tazmoffatt. Date: 2023-12-05. Role: retail customer calling Canadian banks.

> I usually just hit 1 or 0 until they transfer for a human. But once or twice it was an infinite loop and wouldn’t transfer so I had to deal with it lol

URL opened: https://www.reddit.com/r/PersonalFinanceCanada/comments/18bj1i1/tip_bypass_voice_assistant_on_some_banks_by.json

### E-VOC-006 — IVR — Workflow Friction — United Kingdom

Platform: Trustpilot, Royal Bank of Scotland. Author: Aaron W, GB, 2 reviews. Review date shown: Apr 11, 2024. The page also prints "April 10, 2024 Unprompted review". Role: RBS customer of 22 years. On-theme span:

> Its inconvenient with no local branch but telephone banking was always an option but it is just a nightmare recently, its a Robot that you need to get past. I kept going round in circles as it cant answer my question, i only call when it something i need to talk to someone for as im familiar with using the app. I called, asked to talk to someone but then the next step it would direct me to the app or not understand. After 10mins of this im mad and highly irritated and if i happen to get an operator they always now way too keen to just direct you to the app again! Calling them is a highly frustrating experience now. If they don’t improve fast im moving to another bank.

The same review continues with a loan-charge complaint. That coda is not an IVR quote.

URL opened: https://www.trustpilot.com/review/personal.rbs.co.uk?page=9

### E-VOC-007 — IVR transfer — Workflow Friction — United States

Platform: Trustpilot, JPMorgan Chase. Display name is not shown on the fetched page. The byline that is shown is "US• 15 reviews" and "May 18, 2022". Role: Chase customer. The review text dates the calls 5/17/22 and 5/18/22.

> We received a notice in mail, Chase removed withdrew money $3500.00 form my account from a deposited check, with no explanation as to why. Call the customer service number provided to find out. 5/17/22 Four call to Chase, person picks up, asks for info, tells me they can't help me and needs to transfer me to someone else. Once I get transferred on hold for at least 10 minutes, hung up on. Call my branch, they can't help me I need to call 800 #, did that can't get info. Finally give up. Call today 5/18/22, same deal rep asks for info, can't help puts on hold for 5 min., the person she said could help can't, asks someone else, they can't help. Transfers me to supervisor, she can't help, puts me on hold tells me they can help. So 10 minutes later she says these people can't help, she need the people in the "back office"??? and that is a 50 minute hold. I don't have 50 additional minutes to wait, already been on hold for 41 minutes. So basically I have to wait for 2-3 days for someone to maybe call me back. My friends this is JPMorgan Chase customer service.

URL opened: https://ca.trustpilot.com/review/jpmorganchase.com?page=7

### E-VOC-008 — SMS OTP failure — Reliability — India bank, customer in New Zealand

Platform: Reddit, r/nri. Author: SubstantialEvent8124. Date: 2025-08-25. Role: SBI NRO account holder.

> I have a SBI NRO account for the last 10 years and have been receiving OTPs on my international number regularly till 18 Aug25. Suddenly I am not getting anymore OTPs from SBI. The branch manager was contacted and he gave me a list of SMS which they have sent and seem to have been delivered after that date . However these SMSes have not reached my phone and now I am stuck with making payments. My SMS from SBI originate from the number 3132 which I believe is an Airtel number and I live in Nz. [...] I am getting SMS from all other sources. I tried switching over to email OTP but that also is coming as transaction failed on SBI website despite verification using debit card option coming as a success.

URL opened: https://www.reddit.com/r/nri/comments/1n063eb/sms_otp_stopped_being_received_on_registered.json

### E-VOC-009 — SMS OTP failure — Reliability — India bank, customer in the United States

Platform: Reddit, r/nri, same thread as E-VOC-008, different author. Author: KindRefrigerator2052. Date: 2025-12-18. Role: SBI customer.

> Has this issue resolved? I am still not receiving OTP from SBI in USA. Please help

URL opened: https://www.reddit.com/r/nri/comments/1n063eb/sms_otp_stopped_being_received_on_registered.json

### E-VOC-010 — SMS OTP failure — Reliability — India

Platform: Reddit, r/CreditCardsIndia. Author: visualartist47. Date: 2025-09-21. Role: HDFC cardholder. The thread's original post body is `[deleted]` on the fetched JSON, so it is not quoted. These are the author's own comments.

> I checked with the HDFC Credit card support. They don't have any email OTP options unfortunately
>
> I have used Flipkart, Diners Black Smart Buy and other verified portals for transactions. Tried resending again multiple times. No OTPs came so far. So not sure what's the issue. I've also accounts in ICICI Bank and all our OTP transactions work fine. This problem happened after I got the new Diners Card two weeks back.
>
> I've not received any

URL opened: https://www.reddit.com/r/CreditCardsIndia/comments/1nmk255/not_receiving_any_otps_for_hdfc_cards.json

### E-VOC-011 — SMS OTP failure — Reliability — India (NRI, Australian number, writer in India)

Platform: Reddit, r/nri. Author: srikat. Date: 2026-07-26. Role: SBI account holder.

> SBI recently had a facelift called YONO. After this change, I no longer receive OTPs to my phone number (Australian) associated with my account, even after clicking Resend OTP. Therefore, I am unable to log in. Note that I am currently in India but can receive OTPs and incoming calls to my Australian phone number w/o any issues from everyone else.

URL opened: https://www.reddit.com/r/nri/comments/1v6w7lq/is_anyone_getting_otps_from_sbi.json

### E-VOC-012 — SMS OTP fraud — Reliability — India

Platform: Reddit, r/CreditCardsIndia. Author: AmbassadorNo1503. Date: 2025-02-15. Role: HDFC credit-card customer. The original post is `[removed]` on the fetched JSON, so it is not quoted. These comments by the same author remain.

> The process seemed so convincing, but now I do realise I could have just opted out just when I received the OTP mentioning AMOUNT amount. Funny part is that the OTP came from HDFC Bank itself.
>
> It looks foolish I know, but as I said, I have had good experiences only wrt issuance of cards, limit increase etc and they all asked for OTP.
>
> In my case the OTP message did not mention any amount that would be debited. I guess i am in the grey zone.

URL opened: https://www.reddit.com/r/CreditCardsIndia/comments/1iqa9ww/credit_card_fraud.json

### E-VOC-013 — SMS OTP fraud — Reliability — India

Platform: Reddit, r/LegalAdviceIndia. Author: LuckyAd2308. Date: 2025-10-02. Role: HDFC debit-card customer. The customer wrote "OPT" in the first sentence.

> On 25th Sept 2025 at around 4:30 AM, I received an SMS from HDFC Bank that my debit card limits were increased first — without my request or any OPT verification. Immediately after, I received an OTP for a transaction I never initiated (I was asleep at that time). Minutes later, ₹2.34 lakh was debited from my account to “Freecharge Payment Techno”.
>
> I want to make it clear:
> • I did not authorize this transaction.
> • I never shared OTP/PIN/Card details with anyone.

URL opened: https://www.reddit.com/r/LegalAdviceIndia/comments/1nvw7rj/hdfc_debit_card_fraud_234_lakh_wiped_out_without.json

### E-VOC-014 — SMS OTP fraud — Reliability — India

Platform: Reddit, r/LegalAdviceIndia. Author: bala2shaah. Date: 2025-10-09. Role: spouse of the cardholder, writing about her ICICI and Axis cards.

> To add, she did not got any OTP for icici transaction. For axis bank transaction, she called their customer support and informed them. They surprisingly do not have any assistance to offer and directed us to contact cybercrime. For axis transaction she did received a OTP.
>
> We also planned to close both her CC.

URL opened: https://www.reddit.com/r/LegalAdviceIndia/comments/1o2eavq/please_help_my_wife_got_scammed_by_clicking_the.json

### E-VOC-015 — Voice authentication — Reliability — United Kingdom

Platform: MoneySavingExpert forum, Budgeting & bank accounts. Author: jaybeetoo. Date shown: 12 December 2018 at 3:43PM. Role: telephone-banking customer. The bank is not named in this post.

> I have declined to let my bank use Voice ID to validate who I am for telephone banking. The technology is not reliable enough. My wife is on Voice ID. Today she has a cold so Voice ID does not recognise her! She's had to go through an extended set of questions (some a bit bizarre) in order to do a simple telephone banking task (which couldn't be done online or in the app). It took ages. What a pain! It is not just having a cold or sore throat that causes problems. Voice ID also does not work well if there is any background noise. She's now asked to be taken off Voice ID. I hope banks will not make Voice ID mandatory.

URL opened: https://forums.moneysavingexpert.com/discussion/5937560/voice-id-is-not-reliable

### E-VOC-016 — Voice authentication — Reliability — United Kingdom

Platform: MoneySavingExpert forum, Budgeting & bank accounts. Author: Grumpy_chap. The page prints "5 February" and does not print a year. A reply on 6 February in the same thread calls a National Trading Standards release "yesterday". That release, opened the same day, is dated 5 February 2026. as_of is therefore 2026-02-05. Role: First Direct customer.

> I previously had voice ID with First Direct.
>
> It worked as an additional layer on top of the regular ID process. So, when calling the bank, they would take me through the normal ID process (which I had to pass) and, at the same time, do the voice ID by analysis of my voice in the conversation to go through the normal ID process.
>
> With voice ID operating in that manner, the cloned voice alone would not be able to circumvent the security process.
>
> The problem I had was it became so frequent that I was denied access because of the voice ID (even though I was me using my natural voice) that I eventually asked for the voice ID to be removed and just reverted to the standard security questions in any case. The sort of issues I experienced was failure to pass voice ID if I had a cold, any back-ground noise (wind noise particularly), or just a slightly flaky phone signal.

URL opened: https://forums.moneysavingexpert.com/discussion/6654061/secure-use-of-voice-recognition-for-access

Year support URL, also opened 2026-11-24: https://www.nationaltradingstandards.uk/news/phone-scams-take-sinister-twist-as-victims-voices-cloned/

### E-VOC-017 — Voice authentication — Reliability — Australia

Platform: Reddit, r/AusFinance. Author on the fetched JSON: `[deleted]`. The comment body was still on the page. Date: 2024-07-12. Role: ANZ customer, describing a secondary business and trust relationship. The thread's original post is `[removed]` and is not quoted.

> In theory there is meant to be voice ID and the ANZ shield app for stopping unauthorised access. Unfortunately they don’t work reliably.
>
> Voice ID will often fail to recognise your voice from mobile. Just switch to your computer and it’s no longer required.
>
> ANZ shield regularly dies requiring sitting in a call centre queue to reactive. Not that it matters as you can just select SMS code instead which defeats the purpose.
>
> Thankfully ANZ is just my secondary bank for business and trust distributions. While the amounts can be large they’re not frequent or time critical. Otherwise the accounts would be shut down.

URL opened: https://www.reddit.com/r/AusFinance/comments/1e1dsjf/anz_cybersecurity_is_making_me_want_to_switch.json

### E-VOC-018 — Voice authentication — Reliability — Canada

Platform: Reddit, r/Scotiabank. Author: Willing-Reason-2312. Date: 2024-06-16. Role: Scotiabank personal and business customer of over 25 years, and a shareholder.

> Nothing worse than being locked out all personal and business accounts due to a glitch in their app two weeks ago. Got locked out of personal and business. Was made to go into the branch and from there took 45 minutes to reset passwords etc. Tried resetting password with head office and they ask the most silliest questions like what was the last transaction in account ending in 90? I have about 15 accounts… How is someone supposed to know that?! They couldn’t use voice recognition for some reason either… I’m a BNS shareholder and think it’s absolutely ridiculous we can spend all this money on commercials while the oilers play the panthers, yet we inconvenience our customers and costs BNS a ton of money in labour asking all these questions and still doesn’t authenticate… Hope the new CEO gets with it in 2025 or ill be voting him out. This cost me 1.45 minutes total along with 1.5 staff helping. The branch staff had to get permissions from head office to reset while being on hold… Other banks have a priority number… Just an absolute unbelievable experience…. Have had an account for over 25 years. Was almost enough to switch everything over to another bank. Time is money…

URL opened: https://www.reddit.com/r/Scotiabank/comments/1dgwa55/bank_needs_to_update_voice_recognition_when.json

### E-VOC-019 — Voice authentication — counterexample — Canada

Platform: Reddit, r/PersonalFinanceCanada, same thread as E-VOC-005, different author. Author: ikindalikekitkat. Date: 2023-12-06. Role: TD customer.

> I call TD through the app and have never waited more than 2-3 minutes each time. I’ve also been authenticated via voice recognition so everything’s very easy.

URL opened: https://www.reddit.com/r/PersonalFinanceCanada/comments/18bj1i1/tip_bypass_voice_assistant_on_some_banks_by.json

## What this set does not say

Customers in this set describe bank phone menus, missed or misused SMS OTPs, and voice ID that rejects the person or, in one case, lets them through. They do not state a price for a replacement. They do not, in any India quote opened here, describe a bank voice biometric in their own words. Two authors (E-VOC-001 and E-VOC-017) are `[deleted]` on the page that was fetched. Their sentences were still visible. Their earlier usernames were not on that page and are not used.
