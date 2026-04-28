# CP13 — Client Review Revision Loop

**Mục tiêu:** Support natural homeowner feedback after the first 2D concept render.
**Requires:** CP12 PASS.

## Steps

1. Define revision operations: resize room, move wall, switch kitchen open/closed, add bedroom, adjust greenery, change facade emphasis, update style parameter.
2. Parse Vietnamese feedback into operations with confidence and explanation.
3. Apply operations to the concept model and re-run validation.
4. Create child design version metadata and customer-facing changelog.
5. Add tests for common homeowner feedback scenarios.

## Verification

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_revision_loop.py
```
