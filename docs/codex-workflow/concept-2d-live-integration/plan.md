# Concept 2D Live Product Integration Plan

Status: ready for integrator launch

## Decision

CP8-CP14 built a market-quality AI Concept 2D package, but the live Review
Workspace and Professional Deliverables job still render the older 2D drawing
bundle. This phase wires the new concept package into the product path without
regressing the existing selected-version geometry guarantees.

The core product rule is:

```text
Live review/professional-deliverables output must use the selected
DesignVersion.geometry_json and enrich it into the Concept 2D package. It must
not silently reseed a different layout from the brief.
```

## Goal

```text
At the end of this phase, a locked version opened from the Review Workspace can
generate a Professional Deliverables bundle whose 2D PDF/DXF physically contains
the full CP8-CP14 Concept 2D sheet set, readiness evidence, and sheet links,
while preserving selected-version geometry and legacy fallback behavior.
```

## Regression Evidence

Observed on local Docker after CP8-CP14 closeout:

- Project: `56e4c77f-5f46-4506-af8c-df88362aad34`
- Locked selected version: `5e6b84dd-5e4c-419d-a00a-b4f9b54918ee`
- Bundle: `3d21fd3d-775c-4b90-b8fb-25c863e067b3`
- Job result: succeeded, `status=ready`, `quality_status=partial`,
  `is_degraded=true`
- Actual PDF: `2d/bundle.pdf`, 7 pages
- Actual DXF: 7 sheets
- Actual old path: `geometry_to_drawing_project(...) ->
  generate_project_2d_bundle(...)`
- Missing expected CP8-CP14 physical sheets/tokens: `A-000`, `A-601`, `A-602`,
  `A-901`, `Professional Concept 2D Package`, schedules, assumptions, style
  notes.

What is already working and must be preserved:

- PDF/DXF use actual `5.00 m x 20.00 m` geometry for this project.
- Stale `Ranh đất 5 m x 15 m` is absent.
- Existing 2D semantic gates pass.
- DWG local skip remains explicit, not a false failure.

## Workstreams

- C2DL0 Bootstrap/Worktrees: create and verify API/Web worktrees only.
- C2DL1 Product Contract Adapter: add a deterministic adapter from live
  `Project.brief_json`, selected `DesignVersion.geometry_json`,
  `resolved_style_params`, and `generation_metadata` into the concept drawing
  source/package contract.
- C2DL2 Professional Deliverables Wiring: route the live
  professional-deliverables 2D stage through the concept package when eligible;
  preserve legacy fallback for geometry that cannot satisfy the concept package
  contract.
- C2DL3 Review and Delivery UI Exposure: expose concept 2D readiness, PDF/DXF
  sheet links, quality report links, and clear partial/degraded semantics in
  Review and Delivery.
- C2DL4 Evidence and Backward Compatibility: prove the regression project,
  legacy fallback, and existing golden/professional tests.
- C2DL5 Closeout Acceptance: merge accepted slices and rerun integrated local
  Docker evidence.

## Non-Goals

- Do not weaken selected-version geometry correctness.
- Do not replace live generated geometry with a newly seeded concept layout
  unless the product path explicitly asks for a new concept generation.
- Do not make construction, permit, structural, MEP, geotech, legal, or code
  compliance claims.
- Do not implement real image analysis in this phase.
- Do not push remote or create PRs.
- Do not make broad UI redesign outside Review/Delivery concept evidence.

## Exit Gate

PASS only if integrated local `main` proves:

- Review flow can generate Professional Deliverables for project
  `56e4c77f-5f46-4506-af8c-df88362aad34`.
- The generated `2d/bundle.pdf` physically contains the full concept package
  sheet set, including cover/index, site, floor plans, elevations, sections,
  room/area schedule, door/window schedule, and assumptions/style notes.
- Generated DXF outputs physically include matching concept package sheet files
  or an explicit machine-readable reason if a non-drawing sheet has no DXF form.
- PDF/DXF dimensions still match selected `DesignVersion.geometry_json`.
- Quality report JSON/MD exposes concept package readiness truthfully.
- Review and Delivery UI expose usable links/status for the concept package.
- Existing `tests/professional_deliverables`, `tests/test_foundation.py`,
  `tests/test_flows.py`, `make sprint3-ci-linux`, `pnpm lint`, and `pnpm build`
  pass.

Return NEEDS_REVIEW if the backend product path is correct but one non-critical
UI presentation detail remains.

Return BLOCKED if the live source geometry cannot be deterministically adapted
without losing selected-version correctness, or if local Docker cannot run the
required review/professional-deliverables evidence.
