# C2DQ2 Prompt - Spatial Planning Quality

Copy everything below into a new Codex session only after C2DQ1 is accepted and merged.

```text
You are the C2DQ2 Spatial Planning Quality Agent for AI Architect Concept 2D Market Quality V2.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-spatial

Main API repo, read-only except local git merge from main:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Docs repo reference, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/context-and-acceptance-contract.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/market-quality-rubric.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/20-case-matrix.md

Primary objective:
Improve concept spatial planning so generated layouts are plausible enough for customer review and architect critique.

Likely files to inspect/change:
- app/services/design_intelligence/layout_generator.py
- app/services/design_intelligence/program_planner.py
- app/services/design_intelligence/concept_model.py
- app/services/design_intelligence/product_concept_adapter.py
- tests/test_concept_layout_generator.py
- tests/test_concept_model_contract.py
- tests/professional_deliverables/test_ai_concept_2d_e2e.py

In scope:
- room sizing heuristics;
- stair/wet core/storage placement;
- vertical stacking consistency;
- opening placement intent;
- furniture/fixture fit checks;
- low-communication defaults with provenance;
- tests covering matrix cases relevant to spatial planning.

Out of scope:
- PDF/DXF renderer craft except where model fields are required;
- facade graphic styling except where spatial model must expose data;
- UI changes;
- construction/permit/MEP/structural logic.

Requirements:
- Preserve selected-version lot geometry.
- Do not invent critical site facts as verified truth.
- Mark inferred design assumptions.
- Avoid layouts where rooms, labels, openings, and fixtures collide semantically.
- Improve at least the required matrix cases assigned by the rubric.

Verification:
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_layout_generator.py tests/test_concept_model_contract.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_ai_concept_2d_e2e.py -q`
- Add focused tests for new spatial cases.
- `git diff --check`

Commit locally:
- Suggested message: feat(concept-2d): improve market spatial planning

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DQ2 Spatial Planning Quality
- Branch/worktree:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Market-quality coverage:
- Room sizing:
- Circulation:
- Stair/wet core:
- Storage:
- Openings/furniture:
- Multi-floor logic:
- Provenance/assumptions:

Verification:
- Commands run:
- Focused tests:
- Generated artifacts, if any:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No unsafe readiness claims:
- No UI work:
- Any NEEDS_ARCHITECT_DECISION:

Known issues:
-
```
