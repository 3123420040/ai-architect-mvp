# CP11 — Layout Technical Defaults

**Mục tiêu:** Fill the concept model with useful layout geometry and style-aware technical defaults.
**Requires:** CP10 PASS.

## Steps

1. Build a room program planner from family/program/site facts.
2. Add deterministic first-pass layout generation for rectangular lots and common townhouse/villa patterns.
3. Resolve wall thicknesses, openings, stairs, fixtures, furniture, and level heights from style/profile defaults.
4. Add geometry validators: no room overlap, access exists, doors/windows attach to walls, stair footprint fits.
5. Add tests for at least one 7x25 modern tropical scenario and one minimal warm scenario.

## Verification

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_layout_generator.py
```
