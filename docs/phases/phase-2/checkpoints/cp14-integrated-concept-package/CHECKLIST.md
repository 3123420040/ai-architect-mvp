# CP14 Validation Checklist — Integrated Concept Package

## CHECK-01: End-to-End Scenarios

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_ai_concept_2d_e2e.py -q
```

**Expected:** All acceptance scenarios pass.

## CHECK-02: Regression Suite

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables tests/test_foundation.py tests/test_flows.py -q
```

**Expected:** Existing suites pass.

## CHECK-03: Concept-Only Truthfulness

**Expected:** Acceptance report and generated output state that packages are concept/schematic and not construction documents.
**Fail if:** Any artifact claims permit/construction readiness without verified professional input.
