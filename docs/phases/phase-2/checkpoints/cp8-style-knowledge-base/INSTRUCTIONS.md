# CP8 — Style Knowledge Base

**Mục tiêu:** Build the structured style and pattern data foundation for concept 2D generation.
**Requires:** Current professional deliverables tests pass.

## Steps

1. Add a style profile schema with fields for aliases, customer language signals, visual signals, spatial rules, room defaults, opening rules, facade rules, material palette, drawing rules, avoid rules, and validation rules.
2. Add initial profiles for `modern_tropical`, `minimal_warm`, and `indochine_soft`.
3. Add seed pattern memory for common Vietnamese concept scenarios: 5x20 townhouse, 7x25 townhouse/villa, 10x20 villa, apartment renovation, corner lot.
4. Add tests that load profiles, validate required fields, and retrieve at least one pattern from sparse facts.
5. Preserve existing golden and professional deliverables tests.

## Verification

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_style_knowledge.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
```

## Result

Write a short result summary listing added profiles, seed patterns, and validation commands.
