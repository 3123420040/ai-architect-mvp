# C2DQ4 Prompt - Style And Facade Expression

Copy everything below into a new Codex session only after C2DQ1 is accepted and merged.

```text
You are the C2DQ4 Style And Facade Expression Agent for AI Architect Concept 2D Market Quality V2.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-style

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/context-and-acceptance-contract.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/market-quality-rubric.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/20-case-matrix.md

Primary objective:
Make style selection visibly affect Concept 2D outputs, especially facade/elevation rhythm, material notes, shading, opening language, assumptions, and client-readable explanation.

Likely files:
- app/services/professional_deliverables/style_knowledge.py
- app/services/professional_deliverables/style_profiles/*.json
- app/services/design_intelligence/style_inference.py
- app/services/design_intelligence/layout_generator.py
- app/services/design_intelligence/drawing_package_model.py
- app/services/professional_deliverables/pdf_generator.py
- tests/professional_deliverables/test_style_knowledge.py
- tests/test_design_intelligence_style_inference.py
- tests/professional_deliverables/test_concept_2d_package.py

In scope:
- richer style profiles;
- style-specific facade/elevation marks;
- material/palette notes as concept assumptions;
- dislike suppression;
- reference-image descriptors as structured style hints;
- tests for minimal warm, modern tropical, Indochine, and explicit dislikes.

Out of scope:
- real image analysis;
- procedural material rendering;
- construction material specifications;
- permit/code compliance.

Requirements:
- Keep all style-derived fields provenance-tagged.
- Do not treat reference images as measured drawings.
- Do not overwrite selected geometry.
- Do not introduce one-note style output where all styles look the same.

Verification:
- `PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_style_knowledge.py tests/test_design_intelligence_style_inference.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_concept_2d_package.py tests/professional_deliverables/test_ai_concept_2d_e2e.py -q`
- `git diff --check`

Commit locally:
- Suggested message: feat(concept-2d): enrich style facade expression

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DQ4 Style And Facade Expression
- Branch/worktree:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Market-quality coverage:
- Style profiles:
- Facade/elevation expression:
- Material notes:
- Dislike suppression:
- Reference descriptors:
- Provenance:

Verification:
- Commands run:
- Focused tests:
- Manual/render evidence, if any:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No real image analysis claim:
- No unsafe readiness claims:
- Any NEEDS_ARCHITECT_DECISION:

Known issues:
-
```
