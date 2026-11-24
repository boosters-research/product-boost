# Queries — voice-of-customer-2 — RQ-9

**Retrieved:** 2026-11-24
**Rule:** Web search only. Forum text is T4. A quote is used only from a URL opened on this date. Dead ends are listed so a retry does not repeat them.

## Framings that returned subscriber speech

Insider (carrier short codes, IVR, HelloTune):

- `site:reddit.com Airtel "customer care" IVR OR "on hold" OR transferred OR "press 1"`
- `site:reddit.com/r/Airtel "customer care" IVR OR "real person" OR "on hold" OR chatbot OR "press 9"`
- `site:reddit.com/r/india OR site:reddit.com/r/Airtel OR site:reddit.com/r/Jio "customer care" (IVR OR "on hold" OR transferred OR "press 1" OR 198 OR 199) 2024 OR 2025 OR 2026`
- `"caller tune" OR "hello tune" OR "hello tunes" (Airtel OR Jio OR Vi OR Vodafone) (charged OR deducted OR unsubscribe OR "without consent" OR activated) reddit`

Buyer (how a subscriber asks for a person, or for the tune to stop):

- `site:reddit.com "caller tune" OR "hello tunes" OR CRBT charged OR unsubscribe OR scam OR "auto activated"`
- `site:reddit.com "caller tune" OR "hello tune" OR "hello tunes" OR "callertune" (activated OR deducted OR charged OR unsubscribe) (2024 OR 2025 OR 2026)`
- `site:reddit.com/r/Airtel OR site:reddit.com/r/Jio OR site:reddit.com/r/india "transferred" (department OR billing OR "another team" OR "senior") ("customer care" OR 198 OR 199)`

Skeptic (hold, wrong department, non-India):

- `site:reddit.com Verizon OR "T-Mobile" OR AT&T "transferred" "on hold" department IVR "customer service"`
- `site:reddit.com/r/verizon OR site:reddit.com/r/ATT "transferred me" OR "wrong department" OR "on hold" IVR OR "voice assistant" 2025 OR 2026`
- `"value added service" OR VAS OR CRBT "caller tune" Airtel complaint "I did not" OR "without my permission" site:reddit.com`

## URLs opened on 2026-11-24 that supplied a row

Thread JSON was fetched. The quote is in that JSON. Comment permalinks are in LEDGER-ROWS.md.

- https://www.reddit.com/r/Airtel/comments/1wy515n.json
- https://www.reddit.com/r/Airtel/comments/1thbq12.json
- https://www.reddit.com/r/Jio/comments/1q5l3fq.json
- https://www.reddit.com/r/Jio/comments/1snwagw.json
- https://www.reddit.com/r/Jio/comments/1npe19r.json
- https://www.reddit.com/r/Airtel/comments/1wgfua7.json
- https://www.reddit.com/r/Airtel/comments/1loxfut.json
- https://www.reddit.com/r/Rogers/comments/1lilfgh.json
- https://www.reddit.com/r/ATT/comments/1rizwil.json
- https://www.reddit.com/r/verizon/comments/1198d0j.json
- https://www.reddit.com/r/tmobile/comments/1vj7gxn.json
- https://www.reddit.com/r/india/comments/p5dew3.json
- https://www.reddit.com/r/mumbai/comments/13zcmm1.json
- https://www.reddit.com/r/india/comments/t8i32m.json
- https://www.reddit.com/r/india/comments/x8vj2o.json
- https://www.reddit.com/r/Airtel/comments/1jfpxa9.json
- https://www.reddit.com/r/PakistaniTech/comments/1ewsn67.json

## Opened, no row (do not retry as if unread)

- https://old.reddit.com/r/Jio/comments/1oximxa/has_jio_replaced_all_human_support_with_ai/ and the same host for 1q5l3fq, 1snwagw, p5dew3, 13zcmm1, 1vipvc9. Result: login wall. Use `www.reddit.com/...json` instead.
- Direct HTTPS from this machine to `www.reddit.com/*.json` with a browser user-agent returned HTTP 403. The fetch tool returned the JSON. Do not retry the raw client.
- https://www.reddit.com/r/Airtel/comments/1ma00xv.json was opened. Same “stuck in Airtel IVR” pattern as E-VOC-021. No extra ID.
- https://www.reddit.com/r/Jio/comments/1oximxa.json was opened. Image post with an empty selftext. Commenters repeat the bot complaint already rowed. No extra ID.
- https://www.reddit.com/r/Airtel/comments/1vipvc9.json was opened. Original post body is `[deleted]`. Not quoted.
- https://www.reddit.com/r/bsnl/comments/1amgfgy.json was opened after a timeout on the first try. Original post body is `[removed]`. A surviving comment asks how to deactivate in the BSNL tune app and does not describe a charge. Not quoted.
- https://www.reddit.com/r/verizon/comments/1fza2jn.json was opened. Original post body is `[removed]`. A search snippet about a voice assistant was not used.
- https://www.reddit.com/r/verizon/comments/1q37z64.json was opened. Hold-time rant overlaps E-VOC-033. No extra ID. Store-employee replies were not used as subscriber speech.
- https://www.reddit.com/r/india/comments/89n5wr.json was opened. 2018 Vodafone pack complaints (DHNEWS, astrology, caller-tune popup). Older than the three caller-tune rows already kept. No extra ID.
- https://www.thehindubusinessline.com/info-tech/vodafone-to-pay-rs-5k-for-starting-hello-tune-without-consent/article23086461.ece was opened. Journalist paraphrase of a 2008–2012 complaint. Not the subscriber’s words.
- https://trai.gov.in/sites/default/files/2024-09/pr27apr09no39%20%281%29.pdf and https://pib.gov.in/newsite/PrintRelease.aspx?relid=73785 were opened from search. Regulator text, not subscriber speech.
- `"caller tune" OR "hello tune" "without my consent" OR "I never subscribed" Airtel OR Jio OR Vi complaint` returned carrier help pages and TRAI PDFs, not new subscriber quotes.

## Phrases that subscribers do not use

Searches for the product phrase “static VAS” do not return subscriber speech. The words in the posts are “caller tune,” “callertune,” “hello tune,” “hellotune,” and “VAS.”
