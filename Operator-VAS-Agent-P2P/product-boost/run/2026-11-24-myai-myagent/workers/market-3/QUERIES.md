# Queries — market-scout-3 — RQ-8

**Run:** 2026-11-24-myai-myagent
**Retrieved:** 2026-11-24
**Question:** Gross margin percent and CAC payback months for telecom VAS or banking voice-agent contracts, with sample and year.
**Rule:** Three framings. Dead ends are listed so a retry does not repeat them. A retry must use a different string.

## Framing 1 — insider (filer and regulator language)

| Query | Opened | Result |
|---|---|---|
| OnMobile Global annual report gross margin FY2025 OR FY2026 VAS | https://nsearchives.nseindia.com/corporate/ONMOBILE_18052026233709_Investor_Presentation_Q4FY26.pdf ; https://www.onmobile.com/sites/default/files/FY-2026-Annual-Report.pdf ; https://www.onmobile.com/sites/default/files/Q4%20FY2026%20Consolidated%20Financial%20Results.pdf | Produced E-MKT-040, E-MKT-041, E-MKT-042, E-MKT-043. Presentation states 52.7%. Audit does not label a gross margin. Letter states undefined product margins of 11% and 21%. |
| Tanla Platforms gross profit margin annual report FY2025 FY2026 | https://www.bseindia.com/xml-data/corpfiling/AttachHis/41802ade-a3b7-4826-866f-187e7e79c6bf.pdf | Produced E-MKT-044 and E-MKT-045. Stated gross margin 26.6%. No payback string in the letter. |
| Five9 gross margin 10-K 2025 contact center | https://www.sec.gov/Archives/edgar/data/1288847/000128884726000023/fivn-20251231.htm ; https://investors.five9.com/news-releases/news-release-details/five9-reports-record-full-year-2025-revenue-11-billion/ | Produced E-MKT-047. GAAP 55% in the 10-K, 55.1% in the release. No payback string in the 10-K. |
| NICE Ltd 2025 annual report gross margin GAAP cloud 20-F | https://www.sec.gov/Archives/edgar/data/1003935/000100393526000010/nice-20251231.htm | Produced E-MKT-048. Stated 66.4% total and 65.6% cloud. No payback string. |
| SoundHound AI 10-K 2025 gross margin Amelia voice | https://investors.soundhound.com/static-files/265b3ec8-c438-441e-96c0-4044d3654cdf ; https://www.sec.gov/Archives/edgar/data/1840856/000184085626000002/soun-20260226ex991earnings.htm | Produced E-MKT-049. GAAP 42% in the 10-K. No payback string. |
| Sinch AB annual report 2025 gross margin percent messaging | https://www.group.sinch.com/files/Main/22250/4338347/sinch-annual-report-2025.pdf | Produced E-MKT-046. 34.8%. No CAC or payback string. "Acquisition costs" means a business combination. |
| LivePerson 10-K 2025 gross margin GAAP year ended December 31 2025 | https://www.sec.gov/Archives/edgar/data/1102993/000110299326000014/lpsn-20251231.htm | Produced E-MKT-050. No labeled gross-margin percent and no payback months. |
| TRAI performance indicator report VAS revenue gross margin unpublished value added services 2025 2026 | https://trai.gov.in/sites/default/files/2026-10/YIR_05102026.pdf | Produced E-MKT-051. No gross margin. VAS appears as ₹1.20 per subscriber per month inside the ARPU composition, 0.64% of that mix. |

## Framing 2 — buyer (payback, contract, what a bank or telco would call it)

| Query | Opened | Result |
|---|---|---|
| "CAC payback" OR "payback period" months "voice agent" OR "voice bot" OR "conversational AI" bank OR telecom | Search hits included https://indiaml.com/reports/voice-ai-industry-report/financial-benchmarks , https://pulserevops.com/go-to-market-playbooks/gp0102 , https://aitrustedadvisors.com/blog/2026-09-29-what-is-the-average-payback-period-for-a-voice-ai-deployment , and https://www.backbase.com/blog/the-business-case-for-voice-ai-in-banking | IndiaML was opened and rejected as E-MKT-055. The other three were not fetched in full and were not used. PulseRevOps states a 3–12 month target, not a sample. The AI Trusted Advisors snippet is an illustrative buyer-ROI example, which is not vendor CAC. The Backbase snippet says the page gives no per-call benchmark and that payback has to be built from the bank's own inputs. |
| Benchmarkit 2025 SaaS metrics report CAC payback months median sample size | https://5242563.fs1.hubspotusercontent-na1.net/hubfs/5242563/Pavilion%20Benchmarkit%202025%20SaaS%20Performance%20Benchmarks.pdf | Produced E-MKT-054. Named method, wrong population. Median payback months is not in the text. Secondary pages that say the median is 18 months or 16 months were not used, because they disagree and the chart number was not read from the report. |
| PolyAI OR Replicant OR "Skit.ai" OR Gnani "gross margin" OR "payback period" OR "CAC" voice bank | https://indiafintech.substack.com/p/the-hundred-buyer-problem-the-complete | Produced E-MKT-056, a claim without a filing. No PolyAI, Replicant, or Skit.ai filing with a gross margin or a payback was found. Skit.ai price language in a vendor comparison was not recorded; price points belong to market-2. |

## Framing 3 — skeptic (compression, unpublished, failed unit economics)

| Query | Opened | Result |
|---|---|---|
| telecom VAS "gross margin" "revenue share" operator contract margin compression OnMobile OR Comviva OR "value added services" | https://investorrelations.digispice.com/files/S%20Mobility%20Investor%20Comm_Quarter%20ended%20Sep%202013.pdf | Produced E-MKT-058. Quarter dated September 2013. No current Comviva gross-margin filing came back. Do not repeat this string expecting a 2025 Comviva margin. |
| indiaml.com voice AI financial benchmarks page, opened from the payback query | https://indiaml.com/reports/voice-ai-industry-report/financial-benchmarks | Rejected. No sample, no method. Public-company cells conflict with E-MKT-047 and E-MKT-048. |
| OnMobile FY26 annual report, string search for payback and for the USD 1.06 trillion MVAS citation | https://www.onmobile.com/sites/default/files/FY-2026-Annual-Report.pdf | No payback months. The report cites Research and Markets for a USD 1.06 trillion 2025 MVAS market and a USD 1.89 trillion 2029 figure. Not used. No multiplication was shown, so no TAM was published. |

## Dead ends — do not repeat these strings for the same gap

- `telecom VAS "gross margin" "revenue share" operator contract margin compression OnMobile OR Comviva` returned a 2013 DigiSpice deck, not a current contract margin and not a Comviva filing.
- `"CAC payback" voice agent bank` returned unsourced blogs and one unnamed-method page. It did not return a filing.
- Secondary retellings of Benchmarkit that state a median of 18 months or 16 months. The report text that was opened does not contain the chart's median. A retry should seek a different named survey with a telecom or banking-voice cut, not another blog summary of Benchmarkit.
- Buyer-ROI pages that model a bank's savings payback. That metric is not vendor CAC payback. The Backbase and AI Trusted Advisors URLs above were not adopted.
- Top-down MVAS dollar totals, including the Research and Markets figure cited by OnMobile. A retry that only restates a trillion-dollar market does not answer RQ-8.

## Not searched, so not claimed

Route Mobile, Comviva standalone accounts, PolyAI audited accounts, and Replicant audited accounts were not opened as primary documents. Their gross margins and payback months stay UNPUBLISHED rather than estimated. Price pages were left to market-2. Statutes were left to market-1.
