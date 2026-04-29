# C2DL2 Prompt - Professional Deliverables Wiring

Copy everything below into a new Codex chat session only after the integrator
accepts and merges C2DL1 into API `main`.

```text
You are the Professional Deliverables Wiring Agent for AI Architect Concept 2D Live Product Integration.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-deliverables

Main API path, read-only except local git merge from main:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Docs path, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/operating-model.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/ledger.md

Precondition:
- Merge current local API main first: `git merge --no-edit main`.
- Confirm C2DL1 adapter code is present on this worktree.
- If not present, stop with BLOCKED_BY_MISSING_C2DL1_CONTRACT.

Primary objective:
Route the live Professional Deliverables 2D export stage through the full Concept 2D package when the selected version can be adapted by the C2DL1 contract.

Current product gap to fix:
Project `56e4c77f-5f46-4506-af8c-df88362aad34`, version `5e6b84dd-5e4c-419d-a00a-b4f9b54918ee`, generated a 7-page old-style PDF. The live job must produce the full concept package sheets, including cover/index, schedules, and assumptions/style notes.

Likely owned files:
- app/tasks/professional_deliverables.py
- app/services/professional_deliverables/demo.py
- app/services/professional_deliverables/concept_pdf_generator.py
- app/services/professional_deliverables/concept_dxf_exporter.py
- app/services/professional_deliverables/artifact_quality_report.py
- app/services/professional_deliverables/orchestrator.py
- tests/professional_deliverables/test_product_concept_live_deliverables.py
- tests/professional_deliverables/test_output_quality_2d.py

Read-only unless required by compiler/test failures:
- app/services/design_intelligence/product_concept_adapter.py
- app/services/design_intelligence/drawing_package_model.py
- Web repo

Hard constraints:
- Do not modify Web.
- Do not push or create PRs.
- Preserve selected-version geometry.
- Preserve legacy fallback for unsupported geometry.
- Preserve Sprint 2/3 stage order: adapter -> export_2d -> export_3d -> export_usdz -> render_video -> validate.
- Do not reintroduce Sprint 4 outputs.
- Do not run heavy rendering synchronously inside a FastAPI request.
- Do not claim construction/permit/MEP/legal/code-ready output.

Tasks:
1. Inspect the current live path in `app/tasks/professional_deliverables.py`.
2. Replace only the 2D export source for eligible versions:
   - adapt selected version using the C2DL1 adapter;
   - render with the full concept sheet specs;
   - fall back to legacy `generate_project_2d_bundle` only with explicit reason.
3. Ensure generated PDF physically includes:
   - cover/index;
   - site plan;
   - one floor plan per floor;
   - elevations;
   - sections;
   - room/area schedule;
   - door/window schedule;
   - assumptions/style notes.
4. Ensure generated DXF output physically includes matching sheet files or explicit machine-readable unsupported reason for non-drawing sheets.
5. Register assets with enough metadata for UI:
   - sheet number;
   - sheet title;
   - sheet kind;
   - readiness/state;
   - source path/public URL.
6. Ensure `artifact_quality_report.json` and gate summary include concept package readiness and fallback reason if fallback was used.
7. Add tests proving:
   - live concept 2D route is selected for eligible geometry;
   - old 7-page-only output is no longer accepted for concept-eligible geometry;
   - fallback remains explicit for unsupported geometry;
   - asset registration contains sheet metadata;
   - existing 2D gates still pass.

Verification commands:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-deliverables
PYTHONPATH=. /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.venv/bin/python -m pytest tests/professional_deliverables/test_product_concept_live_deliverables.py -q
PYTHONPATH=. /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.venv/bin/python -m pytest tests/professional_deliverables/test_concept_2d_package.py tests/professional_deliverables/test_ai_concept_2d_e2e.py -q
PYTHONPATH=. /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.venv/bin/python -m pytest tests/professional_deliverables/test_output_quality_2d.py tests/professional_deliverables/test_dxf_pdf_gates.py -q

Optional local artifact evidence:
- Generate a temporary eligible 5x20 or 7x25 product bundle.
- Inspect PDF text for `A-000`, `A-601`, `A-602`, `A-901`, and selected lot dimensions.
- Inspect DXF file list for matching concept sheet files.

Commit locally if verification passes:
feat(concept-2d): wire concept package into live deliverables

Acceptance criteria:
- Eligible live professional-deliverables jobs use full Concept 2D package output.
- Legacy fallback is explicit and tested.
- No selected-version geometry regression.
- Existing professional deliverables tests remain green for touched scope.
- Worktree is clean after commit.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DL2 Professional Deliverables Wiring
- Branch/worktree:
- Commit:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Product path evidence:
- New 2D route:
- Fallback behavior:
- Registered asset metadata:
- Quality report/readiness:
- Stage order preserved:

Verification:
- Commands run:
- Focused tests:
- Manual/temp artifact evidence:

Integration notes:
- Expected UI fields:
- C2DL4 evidence needs:
- Merge risks:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No Web changes:
- No Sprint 4 outputs:
- No push/PR:
- No unsafe readiness claims:

Known issues:
-
```
