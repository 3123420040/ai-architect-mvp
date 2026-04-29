# C2DL1 Prompt - Product Contract Adapter

Copy everything below into a new Codex chat session only after C2DL0 reports
`CONCEPT_2D_LIVE_WORKTREES_READY`.

```text
You are the Product Contract Adapter Agent for AI Architect Concept 2D Live Product Integration.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-contract

Main API path, read-only except local git merge from main:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Docs path, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/operating-model.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/21-ai-concept-2d-acceptance-report.md

Primary objective:
Add a deterministic API contract that adapts a live selected DesignVersion into the Concept 2D package source without losing selected-version geometry.

Current product gap:
The live Professional Deliverables path adapts DesignVersion.geometry_json into DrawingProject and calls generate_project_2d_bundle. It does not currently produce the full CP8-CP14 Concept 2D package.

Hard product rule:
The adapter must use the selected DesignVersion.geometry_json as the geometry authority. Project.brief_json, resolved_style_params, and generation_metadata may enrich style, assumptions, and notes, but must not silently reseed a different layout.

Likely owned files:
- app/services/design_intelligence/product_concept_adapter.py
- app/services/design_intelligence/concept_model.py
- app/services/design_intelligence/drawing_package_model.py
- app/services/professional_deliverables/concept_pdf_generator.py
- app/services/professional_deliverables/drawing_contract.py
- tests/test_product_concept_adapter.py
- tests/professional_deliverables/test_concept_2d_package.py

Read-only unless a narrow contract change is required:
- app/tasks/professional_deliverables.py
- app/services/professional_deliverables/demo.py
- app/api/**
- Web repo

Hard constraints:
- Do not wire the live job in this session. C2DL2 owns production task wiring.
- Do not modify Web.
- Do not push or create PRs.
- Do not make permit/construction/structural/MEP/geotech/legal/code-compliance claims.
- Do not replace selected geometry with a new layout generated from the brief.
- Preserve existing concept tests.

Tasks:
1. Merge current local main into the worktree with `git merge --no-edit main`.
2. Inspect:
   - app/tasks/professional_deliverables.py
   - app/services/professional_deliverables/geometry_adapter.py
   - app/services/professional_deliverables/concept_pdf_generator.py
   - app/services/design_intelligence/concept_model.py
   - app/services/design_intelligence/drawing_package_model.py
3. Implement a product/live adapter from:
   - project_id
   - project_name
   - Project.brief_json
   - DesignVersion.geometry_json
   - DesignVersion.resolved_style_params if present
   - DesignVersion.generation_metadata if present
   into a concept-compatible model/package source.
4. Preserve or derive:
   - project/version metadata;
   - site boundary, width, depth, area, north/orientation;
   - all levels;
   - all rooms with labels, polygons, areas, floor mapping;
   - walls/openings/fixtures where available;
   - style id/name, style notes, facade intent, assumptions;
   - concept-only status.
5. Add clear failure semantics:
   - return unsupported/blocked for missing critical geometry;
   - never silently substitute golden geometry;
   - expose why fallback is needed.
6. Add focused tests proving:
   - the adapter preserves selected 5x20 geometry;
   - room/floor counts match input geometry;
   - style/assumptions come from live metadata without overriding geometry;
   - missing critical geometry fails or marks fallback explicitly;
   - drawing package includes full concept sheet roles.

Verification commands:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-contract
PYTHONPATH=. /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.venv/bin/python -m pytest tests/test_product_concept_adapter.py -q
PYTHONPATH=. /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.venv/bin/python -m pytest tests/test_concept_model_contract.py tests/professional_deliverables/test_concept_2d_package.py -q
PYTHONPATH=. /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.venv/bin/python -m pytest tests/professional_deliverables/test_output_quality_2d.py -q

Commit locally if all focused verification passes:
feat(concept-2d): adapt live versions to concept package contract

Acceptance criteria:
- A live generated geometry fixture can become a Concept 2D package source.
- The package preserves selected-version lot dimensions and room/floor counts.
- Adapter exposes fallback/blocker reasons for unsupported geometry.
- No production job wiring is changed.
- Worktree is clean after commit.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DL1 Product Contract Adapter
- Branch/worktree:
- Commit:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Contract coverage:
- Selected geometry preserved:
- Project/brief metadata:
- Style metadata:
- Levels/rooms/walls/openings/fixtures:
- Assumptions/provenance:
- Fallback/blocker behavior:

Verification:
- Commands run:
- Focused tests:
- Regression tests:

Integration notes:
- Required C2DL2 import/function:
- Required C2DL3 response fields, if any:
- Merge risks:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No production job wiring:
- No Web changes:
- No push/PR:
- No unsafe readiness claims:

Known issues:
-
```
