# Query Ledger

**Run:** 2026-11-24-myai-myagent
**Protocol:** P1 §6. Log every query string and its outcome. Retries must use a different string and a different source class.

Prior `SUCCESS` rows were quarantined. They recorded no URL and are not reusable hits.

| Query ID | Research target | Query string | Agent | Outcome | Status |
|---|---|---|---|---|---|
| Q-G0-PESS-01 | Order of magnitude between ₹0.30 and £0.30. Not a K1 input. | Bank of England spot exchange rate GBP INR 24 November 2026 | judge-pessimist | Bank of England database URL was not opened (timeout, then HTTP 404 on a CSV form). A republisher page, https://bankfxapi.com/bank/7 , was opened. It is not T1. It is not copied into the evidence ledger or the scope. C-00 stays open. | NOT-T1 |

Source: workers\academic-2\QUERIES.md
| Query ID | Query string | Outcome |
|---|---|---|
| Q-ACA2-01 | `"speech-to-speech" latency p95 OR "95th" streaming ASR TTS LLM arxiv pdf` | Opened FireRedChat Table 4 (P95 2.407–4.649 s, first audio chunk). Also surfaced Twilio. E-ACA-020, E-ACA-034. |
| Q-ACA2-02 | `Moshi speech-to-speech "theoretical latency" OR "160 ms" OR "200 ms" Kyutai arxiv pdf` | Opened Moshi arXiv HTML and PDF. Theoretical 160 ms; abstract “200 ms in practice.” No percentile. E-ACA-030. |
| Q-ACA2-03 | `LLaMA-Omni "latency" 226ms OR "response latency" speech arxiv pdf Freeze-Omni latency milliseconds` | Opened LLaMA-Omni PDF (226.13 ms at chunk 10, not a percentile) and Full-Duplex-Bench HTML (means 1.18–2.25 s). E-ACA-027, E-ACA-031. |
| Q-ACA2-04 | `Qwen2.5-Omni "first packet" OR "latency" milliseconds technical report pdf GLM-4-Voice latency` | Opened Qwen2.5-Omni PDF (no wall-clock ms), VocalNet-M2 DOI page (first-chunk means), GLM-4-Voice PDF (b = 0.8 s). E-ACA-028, E-ACA-029, E-ACA-036. |
| Q-ACA2-05 | `Freeze-Omni "latency" milliseconds OR "response delay" arxiv pdf 2411.00774 speech-to-speech` | Opened Freeze-Omni abs HTML, Table 4 p90 1,020 ms to first PCM. Opened FD-Bench PDF, medians on H20. E-ACA-032, E-ACA-033. |
| Query ID | Query string | Outcome |
|---|---|---|
| Q-ACA2-06 | `voice agent "end-to-end latency" milliseconds p95 streaming ASR TTS production benchmark 2025 pdf` | Opened arXiv:2508.04721 (H100, mean TTFA 0.678 s, no percentile) and the PAVO OpenReview PDF (E2E P95 1,449–1,651 ms). E-ACA-021, E-ACA-022. Twilio already opened. |
| Q-ACA2-07 | `"p95" TTFAB OR "time to first audio" phone call voice agent ElevenLabs Retell benchmark milliseconds` | Opened https://openbenchmarks.com/voice-agent-latency . Phone-call TTFAB p95 1,768–2,259 ms. Not labeled VoLTE. E-ACA-035. |
| Query ID | Query string | Outcome |
|---|---|---|
| Q-ACA2-08 | `"time to first audio" OR "first packet" OR TTFA cascaded ASR LLM TTS "not" full speech-to-speech latency pdf` | Opened the Salesforce tutorial PDF (measured TTFA 755 ms, not a p95), Voice-Light PDF (median 758 ms, authors refuse a p95), and the on-device cascade PDF (p95 11.92 s). E-ACA-023, E-ACA-024, E-ACA-025, E-ACA-026. |
| Q-ACA2-09 | `VoLTE OR cellular "speech-to-speech" OR "voice agent" latency p95 milliseconds ASR LLM TTS pdf` | No paper with a VoLTE air-interface p95 of ASR + SLM + TTS. Hits were the H100 telecom-titled lab paper, the phone-call board, and vendor budgets. |
| Q-ACA2-10 | `"VoLTE" "speech-to-speech" OR "voice agent" OR "ASR" LLM TTS latency milliseconds p95 measurement pdf` | Opened Exotel 2026-09-02. VoLTE appears only inside an unsourced 40–150 ms one-way carrier range. E-ACA-037. Caller Digital and TestMu pages were opened and rejected (no sample, no hardware, no table). Cekura docs define percentiles and publish no pipeline number. |
| Query or URL | Why it is a dead end |
|---|---|
| `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2410.00037` and the same API for 2509.06502, 2508.04721, and 2412.02612 | HTTP 429 on 2026-11-24. Citation counts for Moshi, FireRedChat, the H100 telecom paper, and GLM-4-Voice were not retrieved and were not filled in. |
| `https://api.openalex.org/works/https://doi.org/10.48550/arxiv.2409.06666` | HTTP 403. |
| `https://api.semanticscholar.org/graph/v1/paper/batch` | HTTP 404. |
| `https://github.com/kyutai-labs/moshi` | Page body was an empty stub (0 stars). The L4 sentence is from the raw README only. |
| `https://caller.digital/blog/openai-realtime-api-vs-voice-ai-platforms-india-2026` | Asserts 900 ms–1.4 s p50 and 2 s+ p95 on Indian PSTN legs, and mentions Jio VoLTE-to-2G handoffs, with no n, no hardware, and no table. Not a ledger row. |
| `https://www.testmuai.com/blog/voice-quality-testing/` | States a P50 of 1.4–1.7 s and a P95 target of 3–5 s with no dataset. Not a ledger row. |
| `https://docs.cekura.ai/documentation/key-concepts/metrics/pre-defined-metrics` | Method only. No measured pipeline percentile. |
| Deepgram, Ortavox, and Pazau URLs that appeared in search snippets | Not opened. Any p95 in those snippets is unused. |
| Q-ACA2-09 and Q-ACA2-10 | No measured p95 of streaming ASR + a small language model + streaming TTS on a VoLTE or cellular air interface. |
Source: workers\oss-1\QUERIES.md
| Query | Result used |
|---|---|
| `open weight streaming ASR github moonshine parakeet sherpa faster-whisper license 2026` | Named Moonshine, Parakeet, sherpa-onnx, faster-whisper. Led to license files opened in the fetch log. |
| `"cost per minute" OR "per audio minute" OR "$ per minute" self-hosted whisper OR moonshine OR parakeet ASR GPU benchmark` | InferenceBench states $0.00007 USD/min (ledgered). hireagentic.dev states estimated USD per audio hour, not a measured per-minute figure (not ledgered). Kernwerk states joules and seconds per sentence, not currency (not ledgered). |
| `open source streaming TTS few-shot voice clone github CosyVoice F5-TTS Kokoro Chatterbox license` | Named CosyVoice, F5-TTS, Qwen3-TTS, Chatterbox, VoXtream. Kokoro is not a clone and was not scored. |
| Query | Result used |
|---|---|
| `open source alternative to Deepgram streaming ASR github self-hosted` | Named WhisperLiveKit, whisper.api, Coro, OASR as servers in front of Whisper, Parakeet, or Nemotron. Those servers were not scored. The models behind them were. |
| `open source alternative to ElevenLabs streaming voice clone TTS github` | Named Qwen3-TTS, Pocket TTS, Tontaube, a Chatterbox streaming fork. Qwen3-TTS was opened. Pocket TTS and Tontaube were not primary-read and are not scored. |
| `Phi-4-mini-instruct license MIT Llama-3.2-3B community license Qwen2.5-3B Apache gemma-3 license` | Pointed at the license files. The Qwen2.5 "Apache" description in a third-party dataset LICENSES.md is contradicted by the model LICENSE opened here (Qwen Research License). The third-party table was not used. |
| Query | Result used |
|---|---|
| `faster-whisper limitations problems production hallucination streaming` | Issue https://github.com/SYSTRAN/faster-whisper/issues/1179 (batched pipeline quality). Production notes at https://gods.dev/blog/faster-whisper-in-prod/ and https://www.spheron.network/blog/faster-whisper-gpu-cloud-production-deployment-guide/. Those blogs are not cost sources. |
| `CosyVoice OR Qwen3-TTS OR F5-TTS problems production license non-commercial complaints` | F5-TTS weights CC-BY-NC confirmed on the README. A 2026-06 Mac write-up describes a CosyVoice 3 Japanese-frontend bug: https://zenn.dev/mohhh_ok/articles/2026-06-cosyvoice-qwen3-tts-apache2-mac. A voice-agent hosting note describes Qwen3-TTS concurrency and says vLLM streaming serving was still maturing: https://softcery.com/lab/self-hosting-tts-for-voice-agents. Neither page states a project-published currency cost per minute. |
| `ChatTTS AGPL OR "SSPL" OR "AGPL-3.0" TTS OR "speech recognition" github license` | ChatTTS AGPL confirmed on the LICENSE file after the search. |
| `SSPL TTS OR ASR OR whisper OR "text-to-speech" license github -elasticsearch` | Hit niradler/vocal, SSPL-1.0. LICENSE and README opened. No other SSPL speech project was opened. |
| `Fish Speech license OR "Coqui Public Model License" XTTS OR OpenVoice MIT commercial restriction` | Led to the XTTS CPML file, which was opened. Fish Speech and OpenVoice license files were not opened, so those projects are not scored. |
| `"per minute" GPU cost TTS OR "voice clone" OR "small language model" open source inference dollars OR USD benchmark` | Stork.AI states about 1.4 and about 0.8 US cents per minute (ledgered). NexGPU derives a USD-per-audio-hour figure for CosyVoice from an L20 RTF and a different GPU price (not ledgered). gpuvault and a Ming 3.0 personal test were not used. |
| Query or page | Why it is not a per-minute cost |
|---|---|
| https://hireagentic.dev/tools/self-hosted-speech-to-text-cost-calculator | Publishes estimated USD per audio hour. Non-A100 RTFx is marked as a bandwidth estimate. This worker did not divide by 60. |
| https://www.assemblyai.com/blog/open-source-speech-to-text-cost | Competitor marketing page. Not used as a model cost. |
| https://nexgpu.net/en/models/cosyvoice/ | Derives about $0.030 per audio-hour by applying an L20 RTF to a different GPU's rental price. Not a per-minute figure and not the project's own price. |
| https://gpuvault.io/model/kokoro-82m/ | Host marketing page. Kokoro is not a voice-clone model. Not scored. |
| https://softreviewed.com/ming-3-tts-free-voice-cloning/ | One person's Modal arithmetic, including cold start. Not used. |
| https://kernwerk.org/blog/speech-to-text-edge-jetson/ | Joules and seconds per sentence. No currency per minute. |
| `SSPL` search | Only Vocal's SSPL-1.0 file was opened. No second SSPL ASR or TTS license file was found and opened. |
| Fish Speech, OpenVoice, Pocket TTS, Tontaube, Kyutai STT, Vosk, FunASR, Piper | Named in search. License files not opened. Not scored. |
| nvidia/parakeet_realtime_eou_120m-v1 and nemotron streaming checkpoints | A third-party license table named NVIDIA Open Model License and OpenMDW 1.1. Those model cards were not opened. E-OSS-003 does not cover them. |
| Gemma 4 license link on https://gemma.ai/resources/terms/ | Not opened. E-OSS-018 is Gemma 3 only. |
| ZONOS3-Mini upstream license file | Not opened. E-OSS-019 quotes the benchmark's license sentence only. |
| GitHub API burst after the first seven repositories | `You have triggered an abuse detection mechanism` and then `API rate limit exceeded`. Retries of that burst will fail until the limit resets. Use raw README, LICENSE, and `commits/*.atom` instead. |
Source: workers\oss-2\QUERIES.md
| # | Framing | Query or fetch | Result used |
|---|---|---|---|
| 1 | Insider | `open source speaker verification anti-spoofing FAR FRR github license evaluation` | SASV2 baseline README (EER tables, MIT), SASV 2022 baseline repo, RawGAT-ST README (min t-DCF and EER, MIT), SpoofSV (plots spoof rate vs FRR; anti-spoof section of that repo says it is incomplete). |
| 2 | Buyer | `open source alternative Nuance voice biometrics speaker verification anti-spoof github Apache` | 3D-Speaker README EER table and Apache-2.0; WeSpeaker Apache-2.0; VoiceGuard README (EER only, and a held-out detection rate that is not FAR/FRR at the K2 point); RawGAT-ST MIT. |
| 3 | Skeptic | `SpeechBrain OR WeSpeaker OR NeMo OR AASIST speaker verification production problems limitations CVE security advisory` | CASE `docs/findings.md` playback EERs; NVD text for CVE-2026-10036; GitHub advisory GHSA-F54R-JQHG-Q7VG; NVIDIA NeMo Speech bulletin, September 2026. |
| 4 | Insider | `ASVspoof evaluation plan false acceptance false rejection rate OR FAR FRR pdf 2019 2021 2024` | ASVspoof 2019, 2021, and 5 plans. They define miss and false-alarm rates inside t-DCF, DCF, and a-DCF. The ranking metrics on those plans are the costs and EER, not a measured FAR < 0.001% at FRR < 1.0%. |
| 5 | Insider | `"false acceptance rate" "false rejection rate" speaker verification ECAPA OR x-vector OR wespeaker OR speechbrain github` | Brydinskyi et al. 2024 PDF, Table 3 FAR/FRR. SpeechBrain `metric_stats` can compute FAR and FRR; the published VoxCeleb table does not. |
| 6 | Insider | `wespeaker NIST SRE16 EER minDCF results github Pmiss Pfa` | WeSpeaker SRE16 commit: metric column is EER. `score_metrics.py` computes Pmiss and Pfa in order to derive EER and minDCF. NIST SRE16 plan defines Cdet from PMiss and PFalseAlarm. The WeSpeaker results table that was opened prints EER. |
| 7 | Skeptic | `AASIST anti-spoofing production failure OR "does not generalize" CVE OR advisory kaldi pyannote 3D-Speaker` | VoiceWukong arXiv HTML, Table 3 FAR/FRR on replay and EER on the full sets. Müller et al. generalization gaps are EER gaps. No CVE for AASIST on this query. |
| 8 | Skeptic | `"FRR" "FAR" speaker verification replay OR "voice conversion" OR TTS open source ECAPA OR "x-vector" pdf` | SASV 2022 PDF (primary metric SASV-EER). voice_match README says it has a FAR/FRR evaluator and that anti-spoof weights are disabled; it does not publish a measured pair. |
| 9 | Insider | `AASIST OR RawNet2 OR "XLS-R" ASVspoof "FAR" OR "false acceptance" OR APCER BPCER github license` | VoiceWukong FAR/FRR table confirmed. W2V2-AASIST Hugging Face card, EER by dataset. |
| 10 | Skeptic | `"false rejection rate" OR "FRR" "0.001%" OR "10^-5" OR "1e-5" speaker verification anti-spoof open source` | No open-source toolkit page returned a measured FRR or FAR at 0.001% or 1e-5. SASV 2022’s lowest listed figure on this query path is 0.13% SASV-EER. |
| 11 | Insider | `ASVspoof 2019 x-vector "Pfa" OR "false alarm" ASV EER logical access pdf Todisco` | arXiv 1911.01601 Tables 6, 7, and 8. Metric printed for the ASV baseline is EER. |
| 12 | Buyer | `NVIDIA NeMo TitaNet speaker verification EER VoxCeleb results documentation` | TitaNet paper Table 2 (EER and MinDCF). Hugging Face card 0.66 EER%. `voxceleb_eval.py` prints EER only. |
| 13 | Skeptic | `CVE kaldi-asr OR wespeaker OR pyannote OR AASIST OR "3D-Speaker" security advisory 2024 OR 2025 OR 2026` | No CVE record for those five names. The hit that did load was sherpa-onnx issue 3253 (heap-use-after-free report involving a pyannote segmentation model and a 3D-Speaker CAM++ ONNX file). GPT-SoVITS CVE coverage in the same results was not used; TTS licensing belongs to oss-1. |
| 14 | Skeptic | `speechbrain 1.1.1 release changelog CVE-2026-10036 site:github.com` | SpeechBrain releases page: v1.1.1 security note, v1.1.2 dated 14 Oct on that page. Advisory and the safeloader commit 22a6166. |
| Query or fetch | What happened |
|---|---|
| `https://nvd.nist.gov/vuln/detail/CVE-2026-10036` fetched twice | Timed out both times. The record text had already come back through search and through the GitHub advisory. A retry should use a different NVD URL form or the VulnCheck advisory linked from the GitHub advisory: `https://www.vulncheck.com/advisories/speechbrain-arbitrary-code-execution-via-ckpt-yaml-parsing`. |
| `https://api.github.com/repos/.../commits?since=2026-08-24` and `.../releases` for the candidate repos | HTTP 403 rate limit after the per-repo metadata calls. Bus-factor org counts are therefore taken from release notes and READMEs, not from the contributor graph. A retry needs a different access path, not the same unauthenticated loop. |
| WebFetch of `https://github.com/speechbrain/speechbrain/blob/develop/recipes/VoxCeleb/SpeakerRec/README.md`, `https://github.com/clovaai/aasist`, `https://github.com/wenet-e2e/wespeaker`, `https://github.com/modelscope/3D-Speaker`, and `https://github.com/gittb/case-benchmark/blob/master/docs/findings.md` | HTML shells came back empty. The same documents loaded from `raw.githubusercontent.com`. |
| `https://github.com/LuiShek/gmm-ubm-speaker-verification` | Page shell only. The search snippet mentioned 0.98% EER and an incomplete anti-spoof note. The numeric claim was not in the fetched body, so it is not a ledger row. |
| `"false rejection rate" OR "FRR" "0.001%" OR "10^-5" OR "1e-5" speaker verification anti-spoof open source` | No page with an open-source FAR below 0.001% at FRR below 1.0%. |
| `CVE kaldi-asr OR wespeaker OR pyannote OR AASIST OR "3D-Speaker" security advisory 2024 OR 2025 OR 2026` | No advisory for those project names. Do not rerun the same OR-string; split by repository if a later scout needs a per-project NVD search. |
Source: workers\market-1\QUERIES.md
| Framing | Query | Result |
|---|---|---|
| Insider | `Reserve Bank of India Authentication mechanisms for digital payment transactions Directions site:rbi.org.in pdf` | Hit the RBI master-directions index and the 25 September 2025 directions. Opened https://www.rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=12898. Produced E-MKT-001, E-MKT-002, E-MKT-004, E-MKT-005. |
| Buyer | `RBI Master Direction Digital Payment Security Controls SMS OTP voice biometric authentication February 2021 pdf` | Hit the official HTML of the 18 February 2021 direction: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12032. Produced E-MKT-003 and E-MKT-006. A separate rbidocs PDF of this direction was not in the results. NOT OPENED. |
| Skeptic | `RBI additional factor of authentication SMS OTP still mandatory voice biometrics cannot replace OTP 2025 2026` | Reuters, Business Standard, Mint, and a law-firm page. Those pages are not the instrument. They were not used for the rule. The official directions already opened do not say voice biometrics may replace SMS OTP, and they do not say SMS OTP remains the only additional factor. |
| Follow-up, primary PDF | `RBI/2025-26/79 Authentication mechanisms for digital payment transactions Directions 2025 pdf rbidocs.rbi.org.in` | Opened https://rbidocs.rbi.org.in/rdocs/notification/PDFs/NT79258FF36ECA8F4886B3B01F55D166C2B2.PDF. Paragraphs 5(f) and 6 match the HTML. |
| Framing | Query | Result |
|---|---|---|
| Insider | `Department of Telecommunications AI generated calls spoofing CLI voice cloning circular 2024 2025 site:dot.gov.in pdf` | Opened the 18 February 2025 DoT advisory on CLI spoofing: https://www.dot.gov.in/static/uploads/2025/07/b5617f94aa59eba08adcccb9f2bebd31.pdf. Produced E-MKT-019. The advisory does not mention a voice clone. Also returned PIB press-release PDFs that describe AI voice cloning as a fraud threat in a speech. Those releases are not a prohibition and were not used as a rule. |
| Buyer | `Telecommunications Act 2023 Section 42 tampering telecommunication identification official pdf site:indiacode.nic.in OR site:egazette.gov.in` | Opened the Act: https://egazette.gov.in/WriteReadData/2023/250880.pdf. Produced E-MKT-011. Also opened the Telecom Cyber Security Rules on India Code. Produced E-MKT-012. India Code bitstream URL for the Act itself returned an error page. That bitstream URL is a dead end. |
| Skeptic | `"voice clone" OR "voice cloning" prohibited OR illegal call subscriber Telecommunications Act OR DPDP OR GDPR OR TRAI` | Hit the TRAI Third Amendment of 18 September 2026, which was then opened: https://www.trai.gov.in/sites/default/files/2026-09/Regulation_18092026.pdf. Produced E-MKT-013. Also hit artintele.ai, Legal 500, and LiveLaw. Those secondary pages were not used as the rule. The LiveLaw page names Bharatiya Nyaya Sanhita section 319. That section was NOT OPENED. The artintele page names Information Technology intermediary rules on synthetically generated information. That gazette was NOT OPENED. |
| Framing | Query | Result |
|---|---|---|
| Insider | `Digital Personal Data Protection Act 2023 official text section 8 erasure retention pdf site:meity.gov.in OR site:indiacode.nic.in` | Opened https://www.meity.gov.in/static/uploads/2025/02/07b7d737f483714eacde37d1a259a6c8.pdf. Section 8(7) and 8(8) state no number for transactional SMS or call transcripts. Produced E-MKT-007 and E-MKT-008. Two other MeitY PDF URLs of the same Act were returned and match the same section 8 text. The India Code handle page was a catalogue record, not the section text. |
| Buyer | `GDPR Regulation 2016/679 official storage limitation Article 5 EUR-Lex call recording retention` | Opened https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng and the consolidated text https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02016R0679-20160504. Article 5(1)(e) states no number. Produced E-MKT-009 and E-MKT-010. ICO, European Commission guidance, and a vendor blog were in the results and were not used as the rule. |
| Skeptic / prescribed period | `Digital Personal Data Protection Rules 2025 official pdf retention period erase personal data MeitY gazette` | The first hits included https://www.dpdpa.in/dpdpa_rules_2025/dpdpa_rules_english_2.pdf. That site is not the Gazette. It was not used. A later query, `G.S.R. 843(E) Digital Personal Data Protection Rules 2025 egazette.gov.in WriteReadData pdf`, separated the commencement notification from the rules. Opened the rules at https://egazette.gov.in/WriteReadData/2025/267650.pdf and the commencement notification at https://egazette.gov.in/WriteReadData/2025/267647.pdf. Produced E-MKT-014, E-MKT-015, E-MKT-016, E-MKT-017. |
| Follow-up | `EUR-Lex GDPR Article 5(1)(e) "no longer than is necessary" call recording OR SMS no specific period site:eur-lex.europa.eu` | Returned Court of Justice judgments applying Article 5(1)(e) to other facts, plus the consolidated regulation. No judgment in the results states a number of days for transactional SMS or call transcripts. The regulation text remains the measurement. |
| Follow-up | `G.S.R. 892(E) corrigendum Digital Personal Data Protection Rules 2025 egazette.gov.in WriteReadData pdf` | Opened https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf. Produced E-MKT-018. The corrigendum does not replace the one-year sentences quoted from rules 6(1)(e) and 8(3). |
Source: workers\market-2\QUERIES.md
| Query | Result |
|---|---|
| `voice biometrics pricing per subscriber bank telco 2024 2025` | Hit the Forrester/TransUnion TEI page, plus vendor cards (AuraSign, VeridVox, Vosco, VoiceVantage). No per-subscriber telco contract. AuraSign, VeridVox, and Vosco were not fetched and are not ledgered. |
| `"Amazon Connect Voice ID" "$0.025" OR "0.025 per" transaction pricing` | Confirmed the $0.025 figure lives on the current AWS pricing appendix, with the 20 May 2026 end-of-support notice on the same page. |
| `Forrester TEI voice biometrics cost per call TransUnion contact center cost per minute Gartner` | Opened the December 2024 TEI. $420,000 per year and $1 per minute are composite assumptions. No separate Gartner price was opened. |
| `site:pindrop.com pricing OR "$" per minute OR per seat OR per authentication` | **Dead end.** No results. Homepage https://www.pindrop.com/ was fetched and contains no unit price. |
| Query | Result |
|---|---|
| `contact center voice AI agent price per minute OR per seat bank OR telco 2025 2026` | Secondary roundups (Plivo, Thunderphone, Denebly, Retell, DialerBee). Those roundups were not used as prices. Official Genesys, Five9, Google, and Twilio pages were fetched instead. |
| `Genesys Cloud CX pricing per user month official Five9 pricing Dialogflow CX voice per minute` | Opened https://www.genesys.com/pricing, https://www.five9.com/pricing, https://cloud.google.com/products/conversational-agents/pricing, and the Genesys BYOT rate table. |
| `IVR cost per minute contact center agent cost SMS OTP price 2024 2025` | Opened ETTelecom (7 May 2024) and https://2factor.in/v4/pricing.html. NESARK was in the result list and was not fetched. |
| `BLS customer service representatives median hourly wage 2025 Twilio SMS pricing official` | Opened the BLS Occupational Outlook Handbook (May 2025) and Twilio US SMS pricing (current as of November 2026). |
| `TRAI tariff order commercial SMS charge paise per SMS enterprise voice minute site:trai.gov.in` | Opened the 3 November 2021 consultation paper quoting TCCCPR 2018 regulation 35 (up to ₹0.05 per promotional or service SMS, inter-operator). **Dead end for a retail bank OTP price and for a voice-agent price.** 2025–2026 comment PDFs on the same site propose or dispute A2P voice charges; those proposals are not ledgered as prices in force. |
| Query | Result |
|---|---|
| `"voice biometrics" (shutdown OR sunset OR discontinued OR "shut down" OR failed) bank OR telco` | AWS Voice ID end of support, Azure Speaker Recognition retirement, CXToday on Google and Nuance, Auraya press release, Voxmind funding note. |
| `HSBC "Voice ID" discontinued OR retired OR "no longer" 2024 OR 2025 OR 2026` | Opened HSBC Hong Kong important notices: Voice ID unsupported from 18 August 2024. No UK closure page was opened. |
| `Azure AI Speaker Recognition retirement September 2025 site:learn.microsoft.com OR site:azure.microsoft.com` | Opened the Microsoft Q&A thread stating retirement on 30 September 2025. Speech SDK release notes mention removal of speaker-recognition samples and were not used for the date. |
| `Nuance Gatekeeper "end of sale" OR "end-of-sale" OR Skit.ai shutdown OR layoffs voice AI` | No Microsoft end-of-sale bulletin. CXToday/Smallman says off official sale since July 2024 with no EOL. Auraya’s press release says end-of-sale. Logged as a contradiction. |
| `OpenAI "phasing out voice-based authentication" Voice Engine 2024 Pindrop pricing` | Opened the 29 March 2024 OpenAI post. Pindrop’s Voice Engine article was in the results and was not used, because it is a vendor accuracy claim and states no price. |
Source: workers\market-3\QUERIES.md
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
| Query | Opened | Result |
|---|---|---|
| "CAC payback" OR "payback period" months "voice agent" OR "voice bot" OR "conversational AI" bank OR telecom | Search hits included https://indiaml.com/reports/voice-ai-industry-report/financial-benchmarks , https://pulserevops.com/go-to-market-playbooks/gp0102 , https://aitrustedadvisors.com/blog/2026-09-29-what-is-the-average-payback-period-for-a-voice-ai-deployment , and https://www.backbase.com/blog/the-business-case-for-voice-ai-in-banking | IndiaML was opened and rejected as E-MKT-055. The other three were not fetched in full and were not used. PulseRevOps states a 3–12 month target, not a sample. The AI Trusted Advisors snippet is an illustrative buyer-ROI example, which is not vendor CAC. The Backbase snippet says the page gives no per-call benchmark and that payback has to be built from the bank's own inputs. |
| Benchmarkit 2025 SaaS metrics report CAC payback months median sample size | https://5242563.fs1.hubspotusercontent-na1.net/hubfs/5242563/Pavilion%20Benchmarkit%202025%20SaaS%20Performance%20Benchmarks.pdf | Produced E-MKT-054. Named method, wrong population. Median payback months is not in the text. Secondary pages that say the median is 18 months or 16 months were not used, because they disagree and the chart number was not read from the report. |
| PolyAI OR Replicant OR "Skit.ai" OR Gnani "gross margin" OR "payback period" OR "CAC" voice bank | https://indiafintech.substack.com/p/the-hundred-buyer-problem-the-complete | Produced E-MKT-056, a claim without a filing. No PolyAI, Replicant, or Skit.ai filing with a gross margin or a payback was found. Skit.ai price language in a vendor comparison was not recorded; price points belong to market-2. |
| Query | Opened | Result |
|---|---|---|
| telecom VAS "gross margin" "revenue share" operator contract margin compression OnMobile OR Comviva OR "value added services" | https://investorrelations.digispice.com/files/S%20Mobility%20Investor%20Comm_Quarter%20ended%20Sep%202013.pdf | Produced E-MKT-058. Quarter dated September 2013. No current Comviva gross-margin filing came back. Do not repeat this string expecting a 2025 Comviva margin. |
| indiaml.com voice AI financial benchmarks page, opened from the payback query | https://indiaml.com/reports/voice-ai-industry-report/financial-benchmarks | Rejected. No sample, no method. Public-company cells conflict with E-MKT-047 and E-MKT-048. |
| OnMobile FY26 annual report, string search for payback and for the USD 1.06 trillion MVAS citation | https://www.onmobile.com/sites/default/files/FY-2026-Annual-Report.pdf | No payback months. The report cites Research and Markets for a USD 1.06 trillion 2025 MVAS market and a USD 1.89 trillion 2029 figure. Not used. No multiplication was shown, so no TAM was published. |
workers\persona-1\QUERIES.md: SYNTHETIC: no web queries; synthetic
