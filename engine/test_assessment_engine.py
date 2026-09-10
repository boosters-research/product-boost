#!/usr/bin/env python3
"""
Unit Tests for Product Assessment Engine
"""

import unittest
import os
import sys

# Add engine directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from assessment_engine import ProductAssessmentEngine, EvidenceEntry, CPIScore

class TestProductAssessmentEngine(unittest.TestCase):

    def test_cpi_calculation_boundaries(self):
        # Max inputs: Freq=5, Sev=5, WQ=1 (invert 6-1=5), WTP=5, VoC=1.2 -> 5*5*5*5*1.2 = 750 / 7.5 = 100.0
        cpi_max = ProductAssessmentEngine.calculate_cpi_2(5, 5, 1, 5, 1.2)
        self.assertEqual(cpi_max, 100.0)

        # Min inputs: Freq=1, Sev=1, WQ=5 (invert 6-5=1), WTP=1, VoC=0.8 -> 1*1*1*1*0.8 = 0.8 / 7.5 = 0.1
        cpi_min = ProductAssessmentEngine.calculate_cpi_2(1, 1, 5, 1, 0.8)
        self.assertEqual(cpi_min, 0.1)

        # Standard Acute Case: Freq=5, Sev=4, WQ=2 (6-2=4), WTP=4, VoC=1.0 -> 5*4*4*4*1 = 320 / 7.5 = 42.7
        cpi_std = ProductAssessmentEngine.calculate_cpi_2(5, 4, 2, 4, 1.0)
        self.assertEqual(cpi_std, 42.7)

    def test_parse_evidence_ledger(self):
        sample_md = """
| E-MKT-001 | B2B churn rate median is 4.2% across mid-market | T2 | https://gartner.com/report | 0.85 |
| E-TECH-002 | RAG vector search latency p95 is 45ms on Milvus | T1 | https://arxiv.org/abs/2301.000 | 0.95 |
        """
        entries = ProductAssessmentEngine.parse_evidence_ledger(sample_md)
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0].entry_id, "E-MKT-001")
        self.assertEqual(entries[0].tier, "T2")
        self.assertEqual(entries[0].confidence, 0.85)
        self.assertEqual(entries[1].entry_id, "E-TECH-002")
        self.assertEqual(entries[1].tier, "T1")

    def test_scan_banned_buzzwords(self):
        sample_text = "Our intuitive and revolutionary platform provides seamless integration and scalable speed."
        banned = ProductAssessmentEngine.scan_banned_buzzwords(sample_text)
        self.assertIn("intuitive", banned)
        self.assertIn("revolutionary", banned)
        self.assertIn("seamless", banned)
        self.assertIn("scalable", banned)

    def test_evaluate_document(self):
        sample_doc = """
# Product Research: CloudOps AI Agent
Target Persona: Senior DevOps Engineer and SRE lead.
Problem Urgency: Daily deployment failures cost $5,000/incident. Workaround is brittle shell scripts.
Market Size: TAM is $12B, growing at 22% CAGR.
Value Proposition: Automated root-cause remediation in under 60 seconds.
Unit Economics: ARPU is $500/mo. CAC is $1,200 with 1.5x CAC buffer included ($1,800 total). Payback is 3.6 months.
Technical Stack: Open-source LangGraph + Vector DB with named fallback to rule-based triage.
AI Economics: Token cost is $0.04 per remediation session.
Compliance: GDPR compliant with zero-retention LLM endpoints. SOC 2 Type II audit planned.
Kill Criteria:
1. Payback exceeds 12 months.
2. Latency p95 exceeds 5 seconds.
3. No customer willing to pay >$300/mo.
        """
        report = ProductAssessmentEngine.evaluate_document(sample_doc, product_name="CloudOps AI Agent")
        self.assertGreaterEqual(report.overall_score, 75.0)
        self.assertEqual(len(report.scores), 10)
        self.assertTrue("Greenlight" in report.classification or "Conditional" in report.classification)

    def test_generate_tech_specification(self):
        sample_doc = "# Sample AI Tool\nARPU: $30/mo"
        report = ProductAssessmentEngine.evaluate_document(sample_doc, product_name="Sample AI Tool")
        tech_spec = ProductAssessmentEngine.generate_tech_specification(report, sample_doc)
        self.assertIn("# Technical Specification: Sample AI Tool", tech_spec)
        self.assertIn("## 1. System Architecture & Topology", tech_spec)
        self.assertIn("## 2. Component & Subsystem Breakdown", tech_spec)
        self.assertIn("## 4. AI & Compute Unit Economics", tech_spec)

if __name__ == "__main__":
    unittest.main()
