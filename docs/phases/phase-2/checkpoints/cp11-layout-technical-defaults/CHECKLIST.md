# CP11 Validation Checklist — Layout Technical Defaults

## CHECK-01: Layout Scenario

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_layout_generator.py -q
```

**Expected:** Layout scenarios pass with valid geometry.

## CHECK-02: No Technical Survey Leakage

**Expected:** Defaults are rule/style-derived.
**Fail if:** The implementation requires homeowners to provide wall thickness, door height, sill height, CAD layers, or sheet scale.
