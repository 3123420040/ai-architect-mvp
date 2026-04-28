# CP8 Validation Checklist — Style Knowledge Base

**Dành cho:** Validator Agent
**Mục tiêu:** Confirm the style KB is structured, deterministic, and safe for concept-only generation.

## CHECK-01: Profile Schema Loads

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_style_knowledge.py -q
```

**Expected:** Tests pass.
**Fail if:** Any profile is unstructured free text only.

## CHECK-02: Safe Scope

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
rg -n "issued for construction|permit approved|structural design|MEP design|code compliant" app/services/professional_deliverables/style_profiles app/services/professional_deliverables/style_knowledge.py
```

**Expected:** No unsafe construction/compliance claims.
**Fail if:** Style profiles claim professional/permit/construction readiness.

## CHECK-03: Existing Deliverables Tests

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q
```

**Expected:** Existing tests pass.
