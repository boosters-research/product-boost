# Protocol P6 — Compliance, Regulatory & AI Safety Matrix

**Binding on:** compliance-risk, ai-systems-architect, tech-path-agent, reconciliation, orchestrator.
**File:** `run/<run-id>/ledger/COMPLIANCE-AUDIT.md`

Every product research run must audit regulatory exposure, data privacy constraints, and AI safety risks before engineering feasibility is signed off.

---

## 1. Regulatory Jurisdictions & Standards Checklist

| Area | Scope & Triggers | Assessment Standards | Compliance Burden & Cost Tier |
|---|---|---|:---:|
| **EU AI Act** | Use of AI models, high-risk categorization, transparency rules | Prohibited vs High-Risk vs General Purpose AI (GPAI) | 🟡 Medium to 🔴 High |
| **Data Privacy (GDPR / CCPA / CPRA)** | Handling personal identifiable data (PII), telemetry, user inputs | Right to be forgotten, data residency, sub-processor audit | 🟡 Medium |
| **Healthcare (HIPAA / HITECH)** | Processing protected health information (PHI) | BAA requirements, audit logging, end-to-end encryption | 🔴 High |
| **Enterprise Security (SOC 2 Type II / ISO 27001)** | Enterprise B2B SaaS buyer procurement gating | Role-based access (RBAC), continuous compliance auditing | 🟡 Medium ($15k–$40k/yr) |
| **Financial / Payment (PCI-DSS / GLBA)** | Cardholder data or financial transaction analytics | Tokenized payment gateways (Stripe/Adyen), PCI compliance | 🟡 Medium |
| **Copyright & Model IP Liability** | Training, fine-tuning, or scraping copyrighted content | License provenance (MIT/Apache vs GPL/AGPL), RAG liability | 🔴 High |

---

## 2. AI Safety & Operational Risk Tiers

| Risk Tier | Trigger Conditions | Mandatory Safeguards |
|:---:|---|---|
| **Tier 1: Mission-Critical / Autonomous Action** | AI executes real-world trades, deletes database records, writes code to production, or dispenses clinical advice. | Human-in-the-loop confirmation, hard execution sandbox, deterministic sanity checks. |
| **Tier 2: Enterprise Copilot / Content Generation** | AI drafts external customer emails, generates financial summaries, or queries internal data stores. | Guardrail classifiers (toxicity, PII redaction, prompt injection defense), citation grounding. |
| **Tier 3: Internal Analytics / Creative Search** | Read-only summarization, semantic search, brainstorming. | Basic rate-limiting, output token filtering. |

---

## 3. The 4-Question Compliance Gate (Required at G3 & G4)

1. **Data Residency:** Where does customer data live during processing and at rest? Does it cross sovereign borders?
2. **Third-Party Model Retention:** Do upstream LLM APIs (OpenAI, Anthropic, Google) retain prompt data for model training? (Zero-data retention agreements required for B2B).
3. **Auditability:** Can every AI-driven action or recommendation be traced back to underlying sources?
4. **License Compatibility:** Does any embedded OSS library force reciprocal open-sourcing (e.g., AGPLv3 viral license)?
