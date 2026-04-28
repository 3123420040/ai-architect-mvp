# CP10 — Concept Model Contract

**Mục tiêu:** Create a renderer-safe concept architecture model with decision provenance.
**Requires:** CP9 PASS.

## Steps

1. Define `DecisionValue` or equivalent provenance wrapper.
2. Define `ArchitecturalConceptModel` sections: site, buildable area, levels, rooms, walls, openings, stairs, fixtures, style, facade, section lines, assumptions.
3. Add validation rules for critical fields and safe assumptions.
4. Add conversion stubs from `CustomerUnderstanding` + style inference to concept model seed.
5. Add focused contract tests.

## Verification

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_model_contract.py
```
