# CP14 — Integrated Concept Package

**Mục tiêu:** Verify the full AI concept 2D workflow on realistic customer scenarios.
**Requires:** CP13 PASS.

## Steps

1. Add at least three sparse homeowner scenarios:
   - 7x25, 3 floors, 4 bedrooms, modern tropical, garage;
   - 5x20, 3 floors, minimal warm, low maintenance;
   - apartment renovation, indochine soft, small family.
2. Run each through understanding, style inference, concept model, layout/defaults, drawing package, render QA.
3. Run at least one revision loop.
4. Write an acceptance report with paths, evidence, gaps, and next recommended phase.

## Verification

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_ai_concept_2d_e2e.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables tests/test_foundation.py tests/test_flows.py
```
