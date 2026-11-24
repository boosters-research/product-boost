# Ledger rows — voice-of-customer-2 — RQ-9

**Agent:** voice-of-customer-2
**Retrieved:** 2026-11-24
**IDs:** E-VOC-020–E-VOC-039 only. Do not append these to the shared ledger from this file; the orchestrator copies them.

Tier is T4 for every row (Reddit). Confidence = 0.3 × recency × corroboration, capped at 1.0, rounded to 2 d.p.

Recency against retrieved 2026-11-24: ≤12 months = 1.0; 12–24 months = 0.85; 24–48 months = 0.7; >48 months = 0.5.

Corroboration: the factor is 1.2 when the row’s theme already has at least three independent accounts in this file, 1.1 when it has two, 1.0 when the specific claim has one rowed account. E-VOC-037 is the single “cannot set HelloTune” row, so its factor is 1.0. E-VOC-038 and E-VOC-039 are the only other-market static-VAS rows, so their factor is 1.1.

Quadrants are the skill’s four: Feature Gaps; Workflow Friction / UX Pain; Reliability & Performance; Pricing & Contract Hostility.

---

### E-VOC-020

| Field | Value |
|---|---|
| id | E-VOC-020 |
| claim | On 2026-10-05 a self-described Airtel subscriber wrote that Airtel had no in-app option to call a human agent. |
| tier | T4 |
| source | https://www.reddit.com/r/Airtel/comments/1wy515n.json |
| permalink | https://www.reddit.com/r/Airtel/comments/1wy515n/i_have_an_issue_with_airtels_bot_customer_support/ |
| retrieved | 2026-11-24 |
| as_of | 2026-10-05 |
| agent | voice-of-customer-2 |
| confidence | 0.36 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/Airtel |
| role | Reddit user ROO2918, self-described Airtel subscriber for over a decade |
| market | India |
| theme | carrier-ivr |
| quadrant | Feature Gaps |
| notes | 0.3 × 1.0 × 1.2 = 0.36. Corroboration is the India IVR set E-VOC-020, E-VOC-021, E-VOC-022, E-VOC-023, E-VOC-024, E-VOC-028. |

Verbatim:

> I have been an Airtel user for over a decade. Recently, whenever I have an issue with their service im unable to get in touch with proper human customer support. im really losing it with all compani3s switching to AI chatbots for customer support. I even sent a complaint email to TRAI , I dont think they will do anything either. But the government should do something about the right to get proper customer support for a monthly paying customer. I dont want bots only customer support, it's good for quick answers but there should be a clear option in the app where it's an option to call a human agent.

---

### E-VOC-021

| Field | Value |
|---|---|
| id | E-VOC-021 |
| claim | On 2026-05-19 a self-described Airtel subscriber wrote that 121, 198, and 9810012345 reached only IVR and that no option reached a human. |
| tier | T4 |
| source | https://www.reddit.com/r/Airtel/comments/1thbq12.json |
| permalink | https://www.reddit.com/r/Airtel/comments/1thbq12/speak_with_live_human/ |
| retrieved | 2026-11-24 |
| as_of | 2026-05-19 |
| agent | voice-of-customer-2 |
| confidence | 0.36 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/Airtel |
| role | Reddit user Ok_Bank6835, self-described Airtel customer calling 121/198 |
| market | India |
| theme | carrier-ivr |
| quadrant | Workflow Friction / UX Pain |
| notes | 0.3 × 1.0 × 1.2 = 0.36. Same India IVR set as E-VOC-020. |

Verbatim:

> How does one connect with live human on Airtel customer care numbers (121/198/9810012345)?
>
> I get IVR all the time and tried all options in IVR for prepaid, new service, postpaid. None of the option led to human. Even for new services, I was told by IVR that request is registered and they will get back to you. Any help?

---

### E-VOC-022

| Field | Value |
|---|---|
| id | E-VOC-022 |
| claim | On 2026-01-06 a self-described Jio subscriber wrote that 199 and 198 would not connect a person and that an AI repeated four sentences. |
| tier | T4 |
| source | https://www.reddit.com/r/Jio/comments/1q5l3fq.json |
| permalink | https://www.reddit.com/r/Jio/comments/1q5l3fq/how_do_i_talk_to_a_real_representative_instead_of/ |
| retrieved | 2026-11-24 |
| as_of | 2026-01-06 |
| agent | voice-of-customer-2 |
| confidence | 0.36 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/Jio |
| role | Reddit user internetfreak130, self-described Jio 5G/LTE subscriber |
| market | India |
| theme | carrier-ivr |
| quadrant | Workflow Friction / UX Pain |
| notes | 0.3 × 1.0 × 1.2 = 0.36. |

Verbatim:

> I am getting terrible speeds (200 Kbps to 2Mbps max) on unlimited 5G and LTE. I am on iPhone 17 and the speed are worst it has ever been. When I am calling customer care, it’s not letting me talk to a real human instead AI is just repeating those 4 sentences.
> I am calling at 199 and 198.

---

### E-VOC-023

| Field | Value |
|---|---|
| id | E-VOC-023 |
| claim | On 2026-04-17 a self-described Jio AirFiber subscriber wrote that six Jio helplines played one automated outage message and then dropped the call, and that the app bot and the WhatsApp bot referred to each other. |
| tier | T4 |
| source | https://www.reddit.com/r/Jio/comments/1snwagw.json |
| permalink | https://www.reddit.com/r/Jio/comments/1snwagw/jio_customer_service_is_pathetic_think_twice/ |
| retrieved | 2026-11-24 |
| as_of | 2026-04-17 |
| agent | voice-of-customer-2 |
| confidence | 0.36 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/Jio |
| role | Reddit user Navyoki, self-described Jio AirFiber subscriber |
| market | India |
| theme | carrier-ivr |
| quadrant | Reliability & Performance |
| notes | 0.3 × 1.0 × 1.2 = 0.36. The post also describes a forced set-top box. That sentence is not a caller-tune row. |

Verbatim:

> I have never been this frustrated with any company before.
>
> I took Jio AirFiber thinking I would get good speed in my village. But they forced a Set Top Box (STB) on me even though I clearly said I don't want TV or OTT, I only want internet. Sales guy said it's mandatory, no choice. Now that useless STB is sitting in my house like extra e-waste. Reliance is pushing unwanted hardware and making e-waste worse.
>
> The real nightmare starts when you try to cancel.
>
> I tried every single number possible:
>
> - 199
> - 198
> - 1800 896 9999
> - 1800 889 9999
> - 1800 890 8900
> - 1991
>
> etc...
>
> Every time it's the same automated message: “We are experiencing ongoing service issues in your area and we apologise for the inconvenience, beep 😞” and the call just drops. No option to leave a message, no way to talk to a real person.
>
> The Jio app chatbot is even worse. It tells me to go to WhatsApp, then the WhatsApp bot sends me back to the app. I was asking for help and they kept rotating me in circles. What the hell is wrong with this system?
>
> And now they have launched a new voice agent. Obviously not helpful. Gali dene se ruk nahi paoge itna ghatiya hai.
>
> Current status (as of 17 April 2026):
>
> My connection is still active.
>
> I am still unable to cancel my Jio AirFiber. I will update here the exact method which worked for me.
>
> I pray someone will make a lawsuit for this (seems like not a big deal, we have more concerning issues in daily life but still it will be great if this happens with reliance. I pray.)
>
> They are delivering not more than 40% of what they claimed speeds and forced me to take what I never wanted.
>
> If you are thinking of taking Jio AirFiber or any Jio service, especially in a village, THINK TWICE. Once you get stuck, getting out feels almost impossible.
>
> Jio, if your team is reading this; shame on Reliance Industries. This is not the way to make money.
>
> I will update the post the moment cancellation happens.
>
> Stay away if you value your time and sanity.
>
> EDIT: I have put a solution in the comments which worked for me

---

### E-VOC-024

| Field | Value |
|---|---|
| id | E-VOC-024 |
| claim | On 2025-09-24 a self-described Jio subscriber wrote that calling 199 announced a press-9 path to customer care and that the digit 9 was not offered. |
| tier | T4 |
| source | https://www.reddit.com/r/Jio/comments/1npe19r.json |
| permalink | https://www.reddit.com/r/Jio/comments/1npe19r/customer_care_blocked_me/ |
| retrieved | 2026-11-24 |
| as_of | 2025-09-24 |
| agent | voice-of-customer-2 |
| confidence | 0.31 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/Jio |
| role | Reddit user Hefty_Antelope7469, self-described caller of Jio 199 |
| market | India |
| theme | carrier-ivr |
| quadrant | Feature Gaps |
| notes | as_of is 14 months before retrieval. 0.3 × 0.85 × 1.2 = 0.306, rounded to 0.31. |

Verbatim:

> So the things whenever we call 199.
> 1.They tell ivs options number 1-8.
> 2. I clicked on option 2.
> 3. It says another 6 option also it says to back to main menu press 7 for last menu 8 to call customer care press 9.
> 4 . Whenever I call them there is no option for clicking 9

---

### E-VOC-025

| Field | Value |
|---|---|
| id | E-VOC-025 |
| claim | On 2025-06-23 a self-described Rogers subscriber wrote that three days of calls and live chat produced only bots or holds. |
| tier | T4 |
| source | https://www.reddit.com/r/Rogers/comments/1lilfgh.json |
| permalink | https://www.reddit.com/r/Rogers/comments/1lilfgh/rogers_customer_service_still_impossible_to_reach/ |
| retrieved | 2026-11-24 |
| as_of | 2025-06-23 |
| agent | voice-of-customer-2 |
| confidence | 0.31 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/Rogers |
| role | Reddit user LoonyVibes, self-described Rogers customer with a billing error |
| market | Canada |
| theme | carrier-ivr |
| quadrant | Workflow Friction / UX Pain |
| notes | as_of is 17 months before retrieval. 0.3 × 0.85 × 1.2 = 0.306, rounded to 0.31. Other-market IVR set is E-VOC-025, E-VOC-026, E-VOC-027. |

Verbatim:

> Tried calling and using live chat for 3 days over a billing error, and all I get are bots or endless holds. Is there a real workaround to talk to a human at Rogers in 2025?

---

### E-VOC-026

| Field | Value |
|---|---|
| id | E-VOC-026 |
| claim | On 2026-03-18 a self-described new AT&T subscriber wrote that the phone robot had no matching option, that a hold ended in a disconnect, and that they would transfer back to Verizon if it continued. |
| tier | T4 |
| source | https://www.reddit.com/r/ATT/comments/1rizwil.json |
| permalink | https://www.reddit.com/r/ATT/comments/1rizwil/how_is_it_that_att_has_such_incredibly_atrocious/ob608eo/ |
| retrieved | 2026-11-24 |
| as_of | 2026-03-18 |
| agent | voice-of-customer-2 |
| confidence | 0.36 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/ATT |
| role | Reddit user FewCharge668, self-described new AT&T customer, former Verizon customer |
| market | United States |
| theme | carrier-ivr |
| quadrant | Reliability & Performance |
| notes | 0.3 × 1.0 × 1.2 = 0.36. Switch sentence is one of the five leave/port lines behind the 1.0 multiplier. |

Verbatim:

> Please tell me maplesurpy how you actually get a person to talk to. I’m a new customer trying to get an actual person to help me with my issue and it’s nothing the robot mentions for me to choose…it’s absolutely the worst! I should have never left Verizon. I had no problem at all getting someone with Verizon to answer the phone…if this keeps up I’m transferring back and I would suggest anyone wanting to go to ATT is to call the customer service number and try to get an actual person. I just went through the motion and chose new service and actually got a person but they couldn’t help me with my issues so they put me on hold and I said I need a person not a robot, so he said he would get me an actual person …while I just spent about five minutes on hold, only to be disconnected… so this is absolutely crazy!!!! The reason they get away with it, is because too many people put up with it…. This whole country is getting away from good customer service and it probably all started with the self checkout lines.

---

### E-VOC-027

| Field | Value |
|---|---|
| id | E-VOC-027 |
| claim | On 2026-03-02 a self-described AT&T subscriber wrote that a voice assistant routed them to the wrong department and that each later representative cost another 10 minutes plus a new verification. |
| tier | T4 |
| source | https://www.reddit.com/r/ATT/comments/1rizwil.json |
| permalink | https://www.reddit.com/r/ATT/comments/1rizwil/how_is_it_that_att_has_such_incredibly_atrocious/ |
| retrieved | 2026-11-24 |
| as_of | 2026-03-02 |
| agent | voice-of-customer-2 |
| confidence | 0.36 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/ATT |
| role | Reddit user Sun_Lizard, self-described AT&T customer |
| market | United States |
| theme | carrier-ivr; hold-transfer |
| quadrant | Workflow Friction / UX Pain |
| notes | 0.3 × 1.0 × 1.2 = 0.36. Dual theme. Same thread as E-VOC-026 and E-VOC-031, different account. Counted once. |

Verbatim:

> You call, get routed through a 'voice assistant' to the incorrect department. Asking for a representative will takes a full 3-5 minutes to 'verify' your account. At this point your 'representative' takes your information only to tell you you've been routed to the wrong department. They *may* connect you directly or give you a number to call - also AT&T so you can do all of this again.
>
> Each representative you speak to will cost you 10 minutes of wait time *AND* re-verification.
>
> AT&T is a telecommunications company ... if they can't transfer you with your information pre-verified and not waste 5 minutes, who the heck can?
>
> AT&T is supposed to be one of the best in the Industry? Is how long customer support keeps you on the line some sort of of metric they are using to gauge their customer service reps support?
>
> US telecoms have become some of the worst in the world.

---

### E-VOC-028

| Field | Value |
|---|---|
| id | E-VOC-028 |
| claim | On 2026-09-14 a self-described Airtel subscriber wrote that toll-free menus had no “Customer Service” choice and that repeated requests for a senior person never produced a transfer. |
| tier | T4 |
| source | https://www.reddit.com/r/Airtel/comments/1wgfua7.json |
| permalink | https://www.reddit.com/r/Airtel/comments/1wgfua7/airtel_customer_service_rant/ |
| retrieved | 2026-11-24 |
| as_of | 2026-09-14 |
| agent | voice-of-customer-2 |
| confidence | 0.36 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/Airtel |
| role | Reddit user chaipilofrans, self-described Airtel subscriber with a billing issue open for 1.5 months |
| market | India |
| theme | carrier-ivr; hold-transfer |
| quadrant | Workflow Friction / UX Pain |
| notes | 0.3 × 1.0 × 1.2 = 0.36. Dual theme. The post states three store visits and no senior transfer. |

Verbatim:

> Y'all, WTF?
> I have genuinely never been this frustrated with a SIM provider before, and I actually used to love Airtel.
>
> I’ve had a billing issue that’s been messy from the beginning, but it has now been 1.5 months and it still hasn’t been sorted out.
>
> But the billing issue isn’t even what frustrated me the most. It’s how ridiculously difficult Airtel makes it to reach an actual human being who can understand the problem and fix it.
>
> I’ve been to 3 different Airtel stores. Every single time, I’m basically told that it’s a “backend” issue and there’s nothing they can do.
>
> Fine. So I tried the chatbot.
>
> The chatbot is basically preloaded with a handful of answers, sends you around in a circle of the same options, and then ends the chat when it decides it has done its job. There doesn’t seem to be any meaningful way to explain a complicated issue to an actual person.
>
> Then I tried the toll-free numbers. Same story. Automated menus, automated responses, and seemingly no straightforward option to just select "Customer Service"
>
> And when Airtel does call me from some random number, it’s usually a junior person who can only tell me what they’re allowed to say based on whatever script or information they have in front of them.
>
> Honestly, I feel bad getting frustrated with them because I can literally hear them getting nervous when I push for answers. They’re clearly not the people who created the problem. But despite repeatedly asking to speak to someone senior who can actually investigate the issue, I’ve never actually been transferred to anyone who can do that.
>
> And then there are the email responses.
>
> I’ll send a detailed explanation of the problem and get back what feels like an extremely generic, one-line response that barely addresses what I wrote. At this point, it honestly makes me wonder whether anyone is actually reading these emails properly, or whether there’s some automated system summarising the issue for the reader.
>
> I mean, it should be illegal for them to even call these "Contact options"
>
> Is this just my experience with Airtel, or has customer support genuinely become this bad?

---

### E-VOC-029

| Field | Value |
|---|---|
| id | E-VOC-029 |
| claim | On 2025-07-01 a self-described Airtel subscriber wrote that a transfer to the postpaid department ended in an IVR that rejected the number, and that a promised different department was the same IVR, three further times. |
| tier | T4 |
| source | https://www.reddit.com/r/Airtel/comments/1loxfut.json |
| permalink | https://www.reddit.com/r/Airtel/comments/1loxfut/update_airtel_scammed_me_for_859_heres_what_i/ |
| retrieved | 2026-11-24 |
| as_of | 2025-07-01 |
| agent | voice-of-customer-2 |
| confidence | 0.31 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/Airtel |
| role | Reddit user Inevitable3000, writing about their mother’s Airtel number |
| market | India |
| theme | hold-transfer |
| quadrant | Workflow Friction / UX Pain |
| notes | as_of is 16 months before retrieval. 0.3 × 0.85 × 1.2 = 0.306, rounded to 0.31. The ₹859 figure is the subscriber’s statement about a discarded recharge, not a VAS tariff study. India handoff set is E-VOC-028, E-VOC-029, E-VOC-030. |

Verbatim:

> This is a follow-up to my earlier post (https://www.reddit.com/r/Airtel/comments/1lo49x1/airtel_prepaid_postpaid_scam/)
>
> After a lot of back-and-forth, I finally managed to connect with an Airtel customer care executive and here’s what happened next:
>
> I explained the whole situation to the executive. She checked the system and told me that there was a request to convert the number to postpaid (which my mother 100% did not initiate), and then later a request to switch back to prepaid (which we did request). Because the number was in postpaid mode for a brief period, the recharge we did — ₹859 — got discarded. No refund. No rollover. Nothing. Just gone.
>
> That’s not even the worst part.
>
> Apparently, if you receive a promotional call and press a button (like 7 or some random number), that counts as your consent to convert to postpaid. No OTP, no clear confirmation, nothing. I asked my mother again — she did not press any such button. Yet the conversion happened.
>
> I told the executive I wanted to raise a complaint about this. She said she’d transfer my call to the postpaid department, which handles such issues. I was transferred, IVR asked me to enter the mobile number — and guess what? It said “invalid number” because the number is no longer postpaid. So the call just ends.
>
> I tried 3 more times. Same experience. One executive even promised, “This time I’ll transfer you to a different department where you won’t need to enter a mobile number.” Total lie — it was the exact same IVR that again rejected the number.
>
> My mother also went to a local Airtel store, hoping someone could help in person. The store owner there told her — this has been happening to a lot of people. He was aware of the scam and said, “Yes, many customers have come with the same issue. Sadly, we can’t do anything about it.”
>
> So Airtel clearly knows this is going on — and they’re doing nothing. That means it’s not just a one-off mistake, it’s happening at scale. They're scamming a lot of people.
>
> At this point, I’m just fed up. Airtel’s system makes it impossible to file a proper complaint for this kind of shady behavior.

---

### E-VOC-030

| Field | Value |
|---|---|
| id | E-VOC-030 |
| claim | On 2022-09-08 a self-described Jio subscriber wrote that up to a dozen calls to 199 ended with a supervisor hold that failed to connect or with the call cut. |
| tier | T4 |
| source | https://www.reddit.com/r/india/comments/x8vj2o.json |
| permalink | https://www.reddit.com/r/india/comments/x8vj2o/i_had_an_unauthorized_autodebit_on_my_jio_autopay/ |
| retrieved | 2026-11-24 |
| as_of | 2022-09-08 |
| agent | voice-of-customer-2 |
| confidence | 0.18 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/india |
| role | Reddit user Heliumorchid, self-described Jio mobile subscriber |
| market | India |
| theme | hold-transfer |
| quadrant | Reliability & Performance |
| notes | as_of is 50 months before retrieval. 0.3 × 0.5 × 1.2 = 0.18. The debit amount in the post is a Jio plan charge, not a bank OTP. |

Verbatim (hold passage; the post also describes a ₹1559 Jio AutoPay debit):

> I tried using the "Live Chat" feature in the MyJio app but it is just a bot that tries to route you to the FAQ section for anything. There's no way to chat with a real person. So I call 199 and I've had upto a dozen calls to them, with each of them having me explain the situation, them understanding it and explaining to me that when a successful transaction is done, there is no way for them to refund or transfer the plan to someone else. To which I have to tell them that this was a mistake at their end and that they have to rectify it somehow. They ask me to wait while they try to connect with a supervisor and EVERY time so far, their hold ends with them saying that they're unable to connect and asking me to call back later. Either that or they just cut the call.

---

### E-VOC-031

| Field | Value |
|---|---|
| id | E-VOC-031 |
| claim | On 2026-08-22 a self-described AT&T subscriber wrote that a department transfer did not carry verification, and that one call required the same identity details for four representatives. |
| tier | T4 |
| source | https://www.reddit.com/r/ATT/comments/1rizwil.json |
| permalink | https://www.reddit.com/r/ATT/comments/1rizwil/how_is_it_that_att_has_such_incredibly_atrocious/p59oexo/ |
| retrieved | 2026-11-24 |
| as_of | 2026-08-22 |
| agent | voice-of-customer-2 |
| confidence | 0.36 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/ATT |
| role | Reddit user SkaneatelesMan, self-described AT&T customer |
| market | United States |
| theme | hold-transfer |
| quadrant | Workflow Friction / UX Pain |
| notes | 0.3 × 1.0 × 1.2 = 0.36. Same thread as E-VOC-027, different account. A second comment by this account the same day says a transfer landed in a closed department; that second comment is the same account and is not a separate row. |

Verbatim:

> My problem with their account verification process is that if a CSR transfers you to another department they don't carry the verification over to the other department, its like you are starting all over. You first spend 5 minutes getting verified, have to provide a social security number, address, phone, before asking for information about the problem. I found myself handing out this information 4 times in one phone call, to 4 different reps only to find I had been transferred to yet another person with no clue how to fix the problem.
>
> I feel sorry for whoever works in AT&T's CSR hell hole. The amount of background noise is incredible and I've frequently gotten people with faulty headsets who cannot be heard. And then the fact is that their CSRs are not speaking North American English. Their accents are so bad that they have to repeat themselves over and over, wasting my time and costing AT&T money too.

---

### E-VOC-032

| Field | Value |
|---|---|
| id | E-VOC-032 |
| claim | On 2023-02-22 a self-described Verizon subscriber wrote that one call included four blind transfers, that departments could not see each other’s notes, and that they would move the number to AT&T. |
| tier | T4 |
| source | https://www.reddit.com/r/verizon/comments/1198d0j.json |
| permalink | https://www.reddit.com/r/verizon/comments/1198d0j/verizon_customer_service_is_awful_bifurcated_and/ |
| retrieved | 2026-11-24 |
| as_of | 2023-02-22 |
| agent | voice-of-customer-2 |
| confidence | 0.25 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/verizon |
| role | Reddit user johnnybozzz, self-described Verizon customer moving a business number to a personal account |
| market | United States |
| theme | hold-transfer |
| quadrant | Workflow Friction / UX Pain |
| notes | as_of is 45 months before retrieval. 0.3 × 0.7 × 1.2 = 0.252, rounded to 0.25. Switch sentence is one of the five leave/port lines. The “4 hours” and “transferred 4x” figures are the subscriber’s counts, not a carrier report. |

Verbatim:

> **4 hours** on the phone with Verizon spanning multiple (I've lost track) calls to transfer a business number to a personal account. After 3 weeks of calls, issues are still not resolved.
>
> Here is the situation for context: I was laid off in the tech layoffs, went to get my phone number from my business line ported to a consumer account. NOBODY knows how to do this. They have told me to contact my company, yeah the one that laid me off. They told me it can't be done, then well it can but only if I get the account number from my company. Then it can be done, but it's blocked by another department. I've spoken to every department from Tech Support, to Business Tech Support, to sales, etc. PASSED THE BUCK. As soon as I get this number, I'm transferring it to AT&T... they can have my money for a while.
>
> Issues inline:
>
> - Agents make you explain the entire situation each time
> - Nobody understands what they are doing, so they just blind-transfer you around to explain the issues all over again (i.e. I was transferred 4x in the most recent call alone).
> - They make you explain the entire situation before they will transfer you, even when requesting the department by name.
> - So much time wasted sitting on hold while they "review the notes on the account"
> - Supervisors are just as useless, agent quote "Sir my supervisor is remote so we will have to wait for her to respond, please stay on hold"
> - Answers are guesses, they pass the buck back to you if you let them. "Sir, please contact your company and have them release the number and give you the account number." Ugh, I told you in the explanation this was done already.
> - Blind transfers (cont), I was literally transferred to the business sales department for tech support. The lady was fun to talk with but admitted she had no ability to help.
> - Business technical support has no access to large accounts, making transfers from major corporate accounts a disaster
> - One division can block another, but they can't talk to each other (5g blocked me from opening a new account, so I had to transfer and spend an hour on the phone with them)
> - The notes are separated by phone number not user, so I probably have about 5-8 accounts created by now (not joking)
> - Dropped calls... you are a freakin cell service provider and you are dropping calls to your customers and having to call them back??? Really?

---

### E-VOC-033

| Field | Value |
|---|---|
| id | E-VOC-033 |
| claim | On 2026-08-08 a self-described 20-year T-Mobile subscriber wrote that every call took an hour to reach a person and that they were close to ending the relationship. |
| tier | T4 |
| source | https://www.reddit.com/r/tmobile/comments/1vj7gxn.json |
| permalink | https://www.reddit.com/r/tmobile/comments/1vj7gxn/tmobile_customer_service_wait_time_is_insane/ |
| retrieved | 2026-11-24 |
| as_of | 2026-08-08 |
| agent | voice-of-customer-2 |
| confidence | 0.36 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/tmobile |
| role | Reddit user Head_Row2765, self-described T-Mobile subscriber for 20 years |
| market | United States |
| theme | hold-transfer |
| quadrant | Workflow Friction / UX Pain |
| notes | 0.3 × 1.0 × 1.2 = 0.36. “An hour” is the subscriber’s statement. Switch sentence is one of the five leave/port lines. |

Verbatim:

> Their ceo makes 35 million a year but they cant afford enough people to cover the phones. Absolutely sickening. Ive been with tmobile for 20 years and im very close to ending my business with them. Its taking an hour to get hold of anyone everytime I call. Who runs a corporation like this????

---

### E-VOC-034

| Field | Value |
|---|---|
| id | E-VOC-034 |
| claim | On 2021-08-16 a self-described Vodafone India subscriber wrote that the carrier was activating caller tunes and other VAS without a request they recognised, and that they were thinking of porting to Jio. |
| tier | T4 |
| source | https://www.reddit.com/r/india/comments/p5dew3.json |
| permalink | https://www.reddit.com/r/india/comments/p5dew3/vodafone_automatically_activating_vas_is_there_a/ |
| retrieved | 2026-11-24 |
| as_of | 2021-08-16 |
| agent | voice-of-customer-2 |
| confidence | 0.18 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/india |
| role | Reddit user python00078, self-described Vodafone subscriber |
| market | India |
| theme | caller-tune |
| quadrant | Pricing & Contract Hostility |
| notes | as_of is 63 months before retrieval. 0.3 × 0.5 × 1.2 = 0.18. India unwanted-charge caller-tune set is E-VOC-034, E-VOC-035, E-VOC-036. |

Verbatim:

> Vodafone has been activating caller tunes and other VAS left and right. I searched and found out they have been doing these for years. I am seeing complaints from 2017 and they are still doing it. There are complaints in consumer court as well but consumer court is a joke in our country. Thinking of porting to Jio.

---

### E-VOC-035

| Field | Value |
|---|---|
| id | E-VOC-035 |
| claim | On 2023-06-03 a self-described Vodafone subscriber in Mumbai wrote that a caller-tune VAS appeared on the bill without a request, and that customer care attributed it to a keypress during a call. |
| tier | T4 |
| source | https://www.reddit.com/r/mumbai/comments/13zcmm1.json |
| permalink | https://www.reddit.com/r/mumbai/comments/13zcmm1/vodafone_adding_vas_shady_practices/ |
| retrieved | 2026-11-24 |
| as_of | 2023-06-03 |
| agent | voice-of-customer-2 |
| confidence | 0.25 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/mumbai |
| role | Reddit user 3_scorpion, self-described Vodafone subscriber |
| market | India |
| theme | caller-tune |
| quadrant | Pricing & Contract Hostility |
| notes | as_of is 41 months before retrieval. 0.3 × 0.7 × 1.2 = 0.252, rounded to 0.25. The post says the charge was reversed. No rupee amount is stated. |

Verbatim:

> Hey folks,
>
> Last month I saw Value Added Service (VAS) caller tunes added to my bill. I never requested this VAS, when I had a chat with the customer care, he mentioned "We don't add VAS without users' consent". I told I never did this by choice, to which he mentioned "I might have pressed a button during a call which might have used a certain caller tune, and that got activated for me as well".
>
> What is surprising to me is, there is no confirmation required and it automatically accepted the request. It is very possible that any one could have accidently pressed a number key during a call. This leads me to believe that the system is designed purposely to deceive users ( I was not aware that this is one of the ways to activate a caller-tune service). I really feel this cheating by deceiving!
>
> Although the customer care guy reverted the charges, however many folks can easily miss this additional charges on the bill. More so when you have automatic payments enabled.
>
> Watchout folks!

---

### E-VOC-036

| Field | Value |
|---|---|
| id | E-VOC-036 |
| claim | On 2022-03-07 a self-described Vi subscriber wrote that a recharge was followed by a callertune activation message and a balance deduction, and asked whether porting was the only option. |
| tier | T4 |
| source | https://www.reddit.com/r/india/comments/t8i32m.json |
| permalink | https://www.reddit.com/r/india/comments/t8i32m/vi_keeps_activating_callertune_and_deducts_balance/ |
| retrieved | 2026-11-24 |
| as_of | 2022-03-07 |
| agent | voice-of-customer-2 |
| confidence | 0.18 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/india |
| role | Reddit user ofpiyush, self-described Vi subscriber with a secondary Jio number |
| market | India |
| theme | caller-tune |
| quadrant | Pricing & Contract Hostility |
| notes | as_of is 56 months before retrieval. 0.3 × 0.5 × 1.2 = 0.18. No rupee amount is stated. |

Verbatim:

> Whenever I recharge my number. I'll get a message in a few days saying my request to activate callertunes is being processed.
>
> Then money gets deducted from my balance. I send the SMS to deactivate and then cycle continues.
>
> I'd stopped recharging main balance altogether to avoid this BS. Recharged a couple of days ago and it's started again.
>
> Is it just me? If not, can we do something?
>
> Is porting the only option? Which providers are good alternative? (I already have a secondary JIO Number)

---

### E-VOC-037

| Field | Value |
|---|---|
| id | E-VOC-037 |
| claim | On 2025-03-20 a self-described Airtel subscriber wrote that after HelloTune moved from Wynk into the Airtel Thanks app, selecting a song played it and did not offer a control to set it. |
| tier | T4 |
| source | https://www.reddit.com/r/Airtel/comments/1jfpxa9.json |
| permalink | https://www.reddit.com/r/Airtel/comments/1jfpxa9/unable_to_set_hellotune_through_thanks_app/ |
| retrieved | 2026-11-24 |
| as_of | 2025-03-20 |
| agent | voice-of-customer-2 |
| confidence | 0.26 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/Airtel |
| role | Reddit user Sipbloodyhell, self-described Airtel HelloTune user |
| market | India |
| theme | caller-tune |
| quadrant | Feature Gaps |
| notes | as_of is 20 months before retrieval. This is the only rowed “cannot set the tune” account, so corroboration is 1.0. 0.3 × 0.85 × 1.0 = 0.255, rounded to 0.26. Same-thread replies were opened and not given IDs. |

Verbatim:

> Airtel Thanks app is such a pain to navigate and after hellotune migrating from Wynk to Thanks App I have not been able to change my hellotune. When clicking on a song it just plays it and doesn't show the option to set it as hellotune, does anyone else know any alternative because it's so much annoying

---

### E-VOC-038

| Field | Value |
|---|---|
| id | E-VOC-038 |
| claim | On 2024-08-20 a self-described Zong subscriber wrote that a pack they did not request was billed at Rs 22 per week on their number and on their mother’s number. |
| tier | T4 |
| source | https://www.reddit.com/r/PakistaniTech/comments/1ewsn67.json |
| permalink | https://www.reddit.com/r/PakistaniTech/comments/1ewsn67/is_jazz_scamming_us/lj199bp/ |
| retrieved | 2026-11-24 |
| as_of | 2024-08-20 |
| agent | voice-of-customer-2 |
| confidence | 0.23 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/PakistaniTech |
| role | Reddit user gamerkaka1, self-described Zong subscriber |
| market | Pakistan |
| theme | static-vas |
| quadrant | Pricing & Contract Hostility |
| notes | as_of is 27 months before retrieval. Only two other-market static-VAS accounts are rowed, so corroboration is 1.1. 0.3 × 0.7 × 1.1 = 0.231, rounded to 0.23. Same thread as E-VOC-039, different account. The original post body was [removed] when opened and is not quoted. Rs 22 per week is the subscriber’s figure. |

Verbatim:

> Bro zong did the same with me they subscribed me to some random ass service for 22 rs per week. First they send pin code that no one requested and then say u have been subscribed to make it seem like you actually did it. Checked my mum's number and she also was subscribed to some random zong magazine service for the same price.

---

### E-VOC-039

| Field | Value |
|---|---|
| id | E-VOC-039 |
| claim | On 2024-08-20 a self-described Jazz subscriber wrote that packs activated when an ad started, without consent, and that the app then required an OTP to deactivate. |
| tier | T4 |
| source | https://www.reddit.com/r/PakistaniTech/comments/1ewsn67.json |
| permalink | https://www.reddit.com/r/PakistaniTech/comments/1ewsn67/is_jazz_scamming_us/lj1i6gi/ |
| retrieved | 2026-11-24 |
| as_of | 2024-08-20 |
| agent | voice-of-customer-2 |
| confidence | 0.23 |
| contradicts | — |
| status | OPEN |
| platform | Reddit r/PakistaniTech |
| role | Reddit user Pro-fess-SirZeero, commenting as a Jazz subscriber on a Jazz charge thread |
| market | Pakistan |
| theme | static-vas |
| quadrant | Pricing & Contract Hostility |
| notes | 0.3 × 0.7 × 1.1 = 0.231, rounded to 0.23. Same thread as E-VOC-038. Not a caller tune. The quote does not name a rupee amount. |

Verbatim:

> Yes. These services are activated by watching ads on other platforms, even if you don't watch the ad. As soon as the ad starts, such services are activated without any consent, but when you go to their app to deactivate it, it requires an OTP, which means you can't deactivate it without consent, but it is always auto-activated.
