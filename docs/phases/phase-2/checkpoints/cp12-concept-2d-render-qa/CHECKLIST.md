# CP12 Validation Checklist — Concept 2D Render QA

## CHECK-01: Concept Package Render

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_concept_2d_package.py -q
```

**Expected:** Concept package renders and QA passes.

## CHECK-02: No Stale Golden Data

**Expected:** PDF/DXF values match scenario geometry.
**Fail if:** Output contains stale 5x15 or other fixture dimensions not present in source input.
