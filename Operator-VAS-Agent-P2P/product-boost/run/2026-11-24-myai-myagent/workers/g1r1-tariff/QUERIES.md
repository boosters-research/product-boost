# Queries — g1r1-tariff

**Run:** 2026-11-24-myai-myagent
**Date searched:** 2026-11-24
**Agent:** g1r1-tariff
**Rule:** different query strings from the exhausted pages. Dead ends are listed so a later retry does not repeat them.

Exhausted before this pass, and not used as sources: the Microsoft Q&A answer, the HSBC Hong Kong important-notices index, the Twilio US Voice pricing page, the Google Cloud conversational-agents pricing page, the Genesys Cloud pricing hub, the 7 May 2024 ETTelecom article, the 2Factor pricing page, the IndiaML financial-benchmarks page, and the 6 October 2026 India Fintech newsletter.

## Framing 1 — insider term

| Query | Result |
|---|---|
| `TRAI TCCCPR regulation 35 transactional SMS Rs 0.05 tariff order pdf site:trai.gov.in 2024 2025` | Opened https://www.trai.gov.in/sites/default/files/2025-02/Regulation_12022025.pdf . Produced E-MKT-070 and E-MKT-071. The 3 November 2021 consultation paper and the FACE comment PDF also appeared. The comment PDF is a stakeholder submission, not a tariff in force, and was not ledgered. |
| `Twilio Form 10-K 2025 "Conversation Relay" OR "0.095" OR Dialogflow site:sec.gov` | Opened the year-ended 31 December 2025 Form 10-K and the 2025 annual report. Produced E-MKT-073 and E-MKT-074. The two prices are absent. |
| `Alphabet Form 10-K Dialogflow "per second" OR "conversational agents" pricing 2025 site:sec.gov` | Opened the 2025 and 2024 Form 10-Ks. Produced E-MKT-075 and E-MKT-076. |
| `site:sec.gov Genesys ("bring your own" OR BYOT OR "0.02 per minute" OR "Dialogflow Voice") 10-K OR "S-1" OR "credit agreement"` | Hit Genesys S.A. conferencing filings and Genasys Inc. Produced E-MKT-077. Those issuers are not Genesys Cloud. |
| EDGAR full-text `Genesys Cloud Services` limited to S-1, 10-K, 10-Q, 8-K | 176 hits. Registrant aggregation does not include Genesys Cloud Services. Produced E-MKT-078. |
| `"Genesys Cloud Services, Inc." ("Form S-1" OR "registration statement" OR "order form") "per minute" 2021 OR 2022` | No public Genesys Cloud registration statement in the results. A secondary article asserting a confidential draft was not used as a filing. No customer contract was opened. |

## Framing 2 — buyer term

| Query | Result |
|---|---|
| `"per SMS" OR "per message" (OTP OR transactional) (Jio OR Airtel OR "Vodafone Idea" OR BSNL) tariff "Rs" OR "₹" enterprise 2025 OR 2026 filetype:pdf` | Opened the Jio postpaid file and produced E-MKT-072. Airtel postpaid terms were opened and not ledgered: after 100 SMS a day the personal plan prints 10 paise per home local and STD SMS, calls are described as unlimited, and the terms say personal and non-commercial use. That is not an enterprise OTP price and not an inbound voice price per minute. The BSNL Calcutta tariff PDF was in the results and was not extracted, so it is not ledgered. |
| `Gupshup SMS Pricing India 2026` via the operator-tariff query | Codingclave blog. The page says the OTP figures are not on Gupshup's site. Not a licensed-operator tariff. Not ledgered. |
| `"Speaker Recognition" retired OR retirement "September 30, 2025" site:learn.microsoft.com/en-us/azure -questions` | Opened the Speech service release notes. Produced E-MKT-079. |
| `site:azure.microsoft.com/en-us/updates Speaker Recognition retirement September 30 2025` | The updates index did not render a retirement notice. Fetched the speaker-recognition overview URL and the updates id `azure-ai-speaker-recognition-retirement`. Produced E-MKT-080. |
| Azure Speech pricing details page | Fetched https://azure.microsoft.com/en-us/pricing/details/speech/ . The extracted category tables do not name Speaker Recognition. Dollar amounts in the extract were placeholders, so no transaction price was read off that page and none is ledgered. |
| `HSBC Hong Kong "Voice ID" "18 August 2024" OR "no longer support" phone banking notice pdf` | The important-notices index is the exhausted page and was not reused. An HSBC Malaysia notice about authentication for Voice ID enrolment is a different market and was not ledgered. |
| `site:hkma.gov.hk HSBC "Voice ID" OR "voice identification" OR "voice biometric" discontinued OR ceased` | Opened four account-opening releases. Produced E-MKT-081. |
| `"Voice ID" "18 August 2024" HSBC (pdf OR "phone banking" OR HKMA OR circular) -"important-notices"` | No separate HSBC PDF and no regulator circular. Dead end for a PDF notice. |

## Framing 3 — skeptic term

| Query | Result |
|---|---|
| `"3.8 months" OR "3.8 month" CAC payback voice AI gross margin 74% Replicant survey pdf` | Opened the April 2021 Forrester TEI PDF hosted at crmxchange. Produced E-MKT-082. The six benchmark figures are absent. |
| `"3.8 months" Replicant "gross margin" OR "CAC payback" -indiaml` | Calculator pages use 3.8 months as a worked example. They are not a voice-AI sample. Not ledgered. Produced the absence in E-MKT-083. |
| `"Gnani.ai" OR "Gnani AI" "gross margin" (filing OR "annual report" OR DRHP OR "AOC-4" OR MCA OR "financial statement") -substack` | Opened the free Tofler page and the 31 March 2026 BusinessToday article. Produced E-MKT-084. A paywalled market-report outline that lists a gross-margin table of contents without numbers was not used. |
| `Azure updates feed and /api/v2/updates?search=speaker recognition` | Feed redirect returned no speaker item to this client. The API URL returned a 404 HTML page. Dead end for a machine-readable lifecycle record. |
| `"Beginning on September 30, 2025, Azure AI Speaker Recognition will be retired"` | Third-party mirrors (azurelook, a blogspot reprint, Medium). Not Microsoft's lifecycle page. Not ledgered. |

## Fetched and used

- https://www.trai.gov.in/sites/default/files/2025-02/Regulation_12022025.pdf
- https://myjiostatic.cdn.jio.com/jio/plan/Postpaid-Plans-Sep-2025.pdf
- https://www.sec.gov/Archives/edgar/data/1447669/000144766926000021/twlo-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1447669/000114036126017449/ny20050676x3_ars.pdf
- https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1652044/000165204425000014/goog-20241231.htm
- https://www.sec.gov/Archives/edgar/data/1125276/000110465906035974/a06-11520_120f.htm
- https://www.sec.gov/Archives/edgar/data/924383/000119312525319294/gnss-20250930.htm
- https://efts.sec.gov/LATEST/search-index?q=%22Genesys%20Cloud%20Services%22&forms=S-1,10-K,10-Q,8-K
- https://learn.microsoft.com/en-us/azure/ai-services/speech-service/releasenotes
- https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speaker-recognition-overview
- https://azure.microsoft.com/en-us/updates?id=azure-ai-speaker-recognition-retirement
- https://www.hkma.gov.hk/media/eng/doc/other-information/ac-opening/20220713e1.pdf
- https://www.hkma.gov.hk/media/eng/doc/other-information/ac-opening/20181122e1.pdf
- https://www.hkma.gov.hk/media/eng/doc/other-information/ac-opening/20200113e1.pdf
- https://www.hkma.gov.hk/media/eng/doc/other-information/ac-opening/20200622e1.pdf
- https://www.crmxchange.com/uploadedFiles/Featured_White_Papers/PDF/Replicant%20_%20Forrester%20Total%20Economic%20Impact%E2%84%A2(TEI)%20Report%20.pdf
- https://www.tofler.in/gnani-innovations-private-limited/company/U72100KA2016PTC095111
- https://www.businesstoday.in/technology/story/gnaniai-raises-10-million-in-funding-from-aavishkaar-capital-to-scale-global-voice-ai-push-523218-2026-03-31

## Opened, not ledgered

- https://www.airtel.in/mobile/terms-conditions/postpaid — personal postpaid terms. Excess SMS after the daily allowance is printed as 10 paise. Calls are described as unlimited. The terms say the offers are for personal and non-commercial use. Not an OTP tariff and not an inbound enterprise minute.
- https://azure.microsoft.com/en-us/pricing/details/speech/ — extracted tables do not name Speaker Recognition, and the numeric cells did not survive extraction.
- https://codingclave.com/blog/gupshup-sms-pricing-india-2026 — agency account of quotes. The page says Gupshup's own site does not list the SMS rates.
- https://trai.gov.in/sites/default/files/2024-11/FACE_10102024_0.pdf — stakeholder comment on the consultation. Not a tariff in force.
- AzureLook, Blogspot, and Medium reprints of a Speaker Recognition retirement sentence. Not Microsoft's lifecycle page.
- CAC calculator pages that illustrate 3.8 months. Not a voice-AI sample.

## Not found

- A TRAI or licensed-operator retail tariff that states an India enterprise OTP SMS price.
- A TRAI or licensed-operator tariff that states an India enterprise inbound voice price per minute.
- $0.095 per second or $0.07 per minute in the Twilio filings opened.
- $0.001 per second as a voice price in the Alphabet filings opened.
- USD 0.02 per minute for bring-your-own voice in a Genesys Cloud filing or a customer contract.
- A Microsoft lifecycle page that printed 30 September 2025 in the text this pass received.
- An HKMA notice, or a separate HSBC PDF, that Voice ID ended on 18 August 2024.
- A primary table with a sample size for 60%, 70%, 74%, and CAC payback of 9, 5, and 3.8 months.
- A Gnani.ai filing that states gross margin above 80% and the year.
