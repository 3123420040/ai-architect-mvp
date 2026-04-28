# CP12 — Concept 2D Render QA

**Mục tiêu:** Render a professional concept 2D package from DrawingPackageModel.
**Requires:** CP11 PASS.

## Steps

1. Add `DrawingPackageModel` with sheets, views, dimensions, labels, schedules, title blocks, notes, and QA bounds.
2. Compile `ArchitecturalConceptModel` into `DrawingPackageModel`.
3. Render PDF and DXF without stale golden values.
4. Add QA gates for sheet count, geometry match, labels, dimensions, nonblank pages, DXF units/layers, and explicit assumptions.
5. Keep output labeled concept-only unless later workflows verify construction data.

## Verification

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_concept_2d_package.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
```
