# AI & Compute Architecture Specification

**Product / System:** <System Name>  
**Author:** AI Systems Architect  
**Status:** DRAFT / APPROVED  

---

## 1. System Topology & Model Selection

| Capability / Task | Model Candidate | Type (Frontier / OSS / SLM) | TTFT Target | Total Latency | Cost / 1M Tokens (In/Out) | Rationale |
|---|---|---|---|---|---|---|
| Core Reasoning | ... | ... | <500ms | <2000ms | $X / $Y | ... |
| Extraction / Filter | ... | ... | <200ms | <500ms | $X / $Y | ... |
| Embedding / Retrieval | ... | ... | <50ms | <100ms | $X / $Y | ... |

---

## 2. Token & Compute Unit Economics (Per Active User)

- **Average Input Tokens per Session:** `<number>`
- **Average Output Tokens per Session:** `<number>`
- **Sessions per Daily Active User (DAU):** `<number>`
- **Cost per User per Month:**
  $$\text{AI COGS/User/Month} = \text{Sessions/Mo} \times [(\text{Input} \times P_{in}) + (\text{Output} \times P_{out}) + \text{Search/Vector Overhead}]$$
  - Calculated Monthly AI COGS: `$<cost>`
  - ARPU: `$<arpu>`
  - AI COGS % of ARPU: `<xx>%` (Must be < 20%)

---

## 3. RAG, Context & Data Flow Strategy

- **Context Window Budget:** `<n> tokens total (<x> system, <y> retrieved chunks, <z> history)`
- **Chunking & Indexing Pipeline:** `<chunk size, overlap, embedding model, vector DB>`
- **Semantic Caching & Deduping:** `<cache hit rate expectation, TTL, storage>`
- **Deterministic Fallback Loop:** `<what happens if API 429, timeout, or validation fails>`

---

## 4. Evaluation & Quality Benchmarks (Eval Suite)

| Eval Dimension | Target Benchmark Metric | Evaluation Dataset | Automated Test Tool |
|---|---|---|---|
| Hallucination Rate | < 2.0% | Golden dataset (n=200) | ragas / DeepEval |
| Context Faithfulness | > 92.0% | Domain QA pairs | promptfoo |
| Latency P95 | < 2500ms | Synthetic load tests | Locust / k6 |
