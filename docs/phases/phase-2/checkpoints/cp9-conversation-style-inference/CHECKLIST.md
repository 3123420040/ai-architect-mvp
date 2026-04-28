# CP9 Validation Checklist — Conversation Style Inference

## CHECK-01: Sparse Vietnamese Brief

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_design_intelligence_style_inference.py -q
```

**Expected:** Sparse homeowner prompts infer facts and ranked style candidates.

## CHECK-02: Confirmation Behavior

**Expected:** Low-confidence style inference produces a plain-language confirmation question.
**Fail if:** The system asks wall, CAD, MEP, or engineering questions.

## CHECK-03: Brief Parser Regression

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_briefing.py -q
```
