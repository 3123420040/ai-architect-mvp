# CP10 Validation Checklist — Concept Model Contract

## CHECK-01: Contract Coverage

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_model_contract.py -q
```

**Expected:** Contract validates required concept model sections and provenance.

## CHECK-02: Assumption Safety

**Expected:** Assumed rectangles, default level heights, and AI-proposed style decisions are marked as assumptions.
**Fail if:** Assumed data is indistinguishable from user facts.
