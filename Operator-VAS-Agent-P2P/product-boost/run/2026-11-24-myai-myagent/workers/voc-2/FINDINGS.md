# VoC-2 findings — RQ-9

**Run:** 2026-11-24-myai-myagent
**Agent:** voice-of-customer-2
**Question:** What do telecom subscribers say, in their own words, about carrier IVR, hold-queue transfers between departments, and caller tunes or other static VAS?
**Retrieved:** 2026-11-24
**IDs used:** E-VOC-020 through E-VOC-039 (20 rows). No CPI score.

Retail banking IVR, SMS OTP, and voice authentication were left to voice-of-customer-1. None of those topics are in this set.

Every quote below is forum text. Tier is T4. A T4 cluster can support a direction when at least three independent accounts agree. It cannot support a material or financial claim by itself.

## Verbatim count by theme

One row is one Reddit account. Two rows are tagged to two themes (E-VOC-027, E-VOC-028). The unique account count is 20. The theme counts below add to 22 because of those two dual tags.

| Theme | India | Other markets | Independent accounts | Quadrant that holds most of the rows |
|---|---:|---:|---:|---|
| Carrier IVR (phone menu, voice bot, or automated line that blocks a person) | 6 | 3 | 9 | Workflow Friction / UX Pain |
| Hold-queue and department transfer (re-verify, blind transfer, supervisor hold, callback that does not come) | 3 | 4 | 7 | Workflow Friction / UX Pain |
| Caller tune or other static VAS | 4 | 2 | 6 | Pricing & Contract Hostility |

Market split inside those themes:

| Slice | IDs | n |
|---|---|---:|
| India carrier IVR | E-VOC-020, E-VOC-021, E-VOC-022, E-VOC-023, E-VOC-024, E-VOC-028 | 6 |
| Other-market carrier IVR | E-VOC-025 Canada (Rogers), E-VOC-026 United States (AT&T), E-VOC-027 United States (AT&T) | 3 |
| India hold / department handoff | E-VOC-028 Airtel senior transfer never happens, E-VOC-029 Airtel postpaid-department transfer, E-VOC-030 Jio supervisor hold | 3 |
| Other-market hold / department handoff | E-VOC-027 AT&T, E-VOC-031 AT&T, E-VOC-032 Verizon, E-VOC-033 T-Mobile | 4 |
| India caller tune or HelloTune | E-VOC-034, E-VOC-035, E-VOC-036 (unwanted charge), E-VOC-037 (cannot set the tune) | 4 |
| Other-market static VAS, not a caller tune | E-VOC-038 Zong, E-VOC-039 Jazz, both Pakistan, one thread | 2 |

India IVR carriers named in the subscriber’s own post: Airtel (020, 021, 028) and Jio (022, 023, 024). Other-market carriers: Rogers, AT&T, Verizon, T-Mobile.

## Proposed VoC multiplier

**1.0**

Count behind it: **20** independent subscriber accounts, of which **5** use leave, port, or “ending my business” language.

| ID | Market | as_of | Switch language in the verbatim |
|---|---|---|---|
| E-VOC-026 | United States | 2026-03-18 | “if this keeps up I’m transferring back” |
| E-VOC-032 | United States | 2023-02-22 | “I’m transferring it to AT&T” |
| E-VOC-033 | United States | 2026-08-08 | “im very close to ending my business with them” |
| E-VOC-034 | India | 2021-08-16 | “Thinking of porting to Jio.” |
| E-VOC-036 | India | 2022-03-07 | “Is porting the only option?” |

Five of twenty is a minority. Two of those five are dated 2026 (E-VOC-026, E-VOC-033). The three India or older lines are a question or a thought, not a completed switch in the post. The 2025–2026 India IVR rows describe a keypad or bot workaround (press 9, survive the menu, mail instead). That is the skill’s moderate-friction band: common annoyance tolerated with a hack. It is not the 1.2 band (people leaving the carrier today over this pain) and it is not the 0.8 band (a passive preference). 

This multiplier is T4-only. CPI 2.0 does not allow the VoC multiplier axis to rest on T4 alone. The number above is the sentiment proposal. It is not a CPI score.

## Themes with fewer than 3 independent quotes

1. **Caller tunes outside India: 0.** No opened subscriber post from a non-India market uses “caller tune,” “hello tune,” “HelloTune,” or CRBT.
2. **Other static VAS outside India: 2.** E-VOC-038 and E-VOC-039. Both are 2024-08-20 comments on one r/PakistaniTech thread (Zong magazine-style pack; Jazz ad-activated pack). Two accounts, one thread, so this slice does not clear the three-source bar.
3. **HelloTune that the subscriber still wants but cannot set: 1.** E-VOC-037 only (Airtel Thanks, 2025-03-20). Same-thread replies were opened and not given IDs, so they are not in the count.
4. **Unwanted caller-tune charge with `as_of` on or after 2024-11-24: 0.** The three charge quotes are 2021-08-16, 2022-03-07, and 2023-06-03. The theme has three India accounts. None of them are inside 24 months of this retrieval.

## What the words cluster into

**Feature gaps.** E-VOC-020 wants a visible in-app control that calls a human. E-VOC-024 says the Jio menu describes “press 9” and then does not offer 9. E-VOC-037 says the HelloTune control does not appear after the song plays.

**Workflow friction.** This is the main cluster. India subscribers describe 121/198/199 as a tree that ends in a bot, a registered request, or a dropped call (E-VOC-021, E-VOC-022, E-VOC-023, E-VOC-028). US subscribers describe a voice assistant that lands in the wrong department and a fresh verification at every hop (E-VOC-027, E-VOC-031). Verizon and T-Mobile rows are long holds and a callback that does not arrive (E-VOC-032, E-VOC-033). E-VOC-029 is the India department case: the executive transfers the call to postpaid, the IVR rejects the number because it is no longer postpaid, and a promised “different department” is the same IVR.

**Reliability.** E-VOC-023: the Jio automated line plays an outage apology and drops the call, and the app bot and WhatsApp bot send the subscriber to each other. E-VOC-026: after a hold, the AT&T line disconnects. E-VOC-030: the Jio hold for a supervisor ends with “unable to connect” or a cut call, up to a dozen times.

**Pricing hostility.** E-VOC-034, E-VOC-035, and E-VOC-036 say a caller tune was billed without a request they recognise. E-VOC-038 and E-VOC-039 say a Pakistan pack was subscribed from a PIN or an ad the subscriber says they did not choose, and that unsubscribe does not stick. Amounts the subscribers state: Vi/Vodafone balance deductions with no rupee figure in E-VOC-034; E-VOC-035 describes the charge as a line item that was later reversed, with no rupee figure; E-VOC-038 states Rs 22 per week.

## Same-thread pairs

These are different accounts. They are not different venues.

- E-VOC-027 and E-VOC-031 are both on the 2026-03-02 AT&T thread.
- E-VOC-038 and E-VOC-039 are both on the 2024-08-20 Jazz thread.

## Not used

- Deleted or removed post bodies were opened and not quoted: r/Airtel/1vipvc9, r/bsnl/1amgfgy, r/verizon/1fza2jn, and the Jazz original post (comments on that thread were kept).
- A 2018 news paraphrase of a Delhi consumer complaint was opened and not quoted. It is not the subscriber’s words.
- TRAI press text was opened and not quoted. It is the regulator, not a subscriber.
- `workers/prior-contaminated/` was not used.
