# C2DQ3 Prompt - Drawing Craft And Readability

Copy everything below into a new Codex session only after C2DQ1 is accepted and merged.

```text
You are the C2DQ3 Drawing Craft And Readability Agent for AI Architect Concept 2D Market Quality V2.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-craft

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/context-and-acceptance-contract.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/market-quality-rubric.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/20-case-matrix.md

Primary objective:
Improve PDF/DXF sheet readability and drawing craft so concept packages are easier for homeowners and architects to review.

Likely files:
- app/services/design_intelligence/drawing_package_model.py
- app/services/design_intelligence/concept_drawing_qa.py
- app/services/professional_deliverables/pdf_generator.py
- app/services/professional_deliverables/dxf_exporter.py
- app/services/professional_deliverables/concept_pdf_generator.py
- app/services/professional_deliverables/drawing_quality_gates.py
- tests/professional_deliverables/test_concept_2d_package.py
- tests/professional_deliverables/test_concept_2d_live_integration.py
- tests/professional_deliverables/test_output_quality_2d.py

In scope:
- viewport fit and whitespace control;
- line hierarchy and hatches;
- room label density and collision avoidance;
- dimension readability;
- title block/legend readability;
- schedules that are useful for review;
- PDF render QA and DXF openability gates.

Out of scope:
- changing planning heuristics unless a renderer contract requires a field;
- UI redesign;
- construction drawing conventions beyond concept-review clarity.

Requirements:
- Keep selected geometry truth and no stale labels.
- Keep concept-only warning.
- Do not mark market quality ready when visual QA fails.
- Add/strengthen tests for page render, text tokens, sheet titles, DXF sheet parity, and non-overlap signals.

Verification:
- `PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_concept_2d_package.py tests/professional_deliverables/test_concept_2d_live_integration.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_output_quality_2d.py tests/professional_deliverables/test_dxf_pdf_gates.py -q`
- Render sample PDFs locally if dependencies allow.
- `git diff --check`

Commit locally:
- Suggested message: feat(concept-2d): improve market drawing craft

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DQ3 Drawing Craft And Readability
- Branch/worktree:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Market-quality coverage:
- Viewport scale:
- Label collision:
- Dimensions:
- Line hierarchy:
- Schedules:
- PDF visual QA:
- DXF parity:

Verification:
- Commands run:
- Focused tests:
- Manual/render evidence:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No unsafe readiness claims:
- Any NEEDS_ARCHITECT_DECISION:

Known issues:
-
```
