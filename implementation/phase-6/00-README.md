# Phase 6: Presentation-Grade 3D Delivery

## Context

Phase 6 starts after the current platform already has:

- intake and brief-lock foundations,
- canonical 2D design state,
- package-centric export and delivery baseline,
- and a placeholder 3D derivation lane.

Production truth and code review show the current 3D lane is still only a workflow stub.

It can prove:

- locked-version gating,
- asset persistence,
- and basic viewer wiring.

It cannot yet prove:

- design-faithful `scene.glb`,
- curated still renders,
- walkthrough video,
- presentation manifest,
- or architect-gated client delivery.

## Core Decision

Phase 6 is locked to:

**Program A: Presentation-grade 3D**

Target output:

- `scene.glb`
- curated still renders
- `walkthrough.mp4`
- `presentation_manifest.json`
- architect approval gate

## Boundary

Phase 6 does **not** include:

- BIM and construction authoring
- native BIM editing workflows
- full construction-model semantics
- premium CGI studio pipeline
- BLEND/USD/FBX artist-production lane

Those are intentionally separated into the independent research brief:

- `implementation/phase-6/04-independent-research-requirements-for-bim-and-premium-cgi.md`

## Read Order

1. `implementation/phase-6/00-README.md`
2. `implementation/phase-6/01-3d-output-research-and-direction.md`
3. `implementation/phase-6/02-3d-module-input-contracts.md`
4. `implementation/phase-6/03-3d-presentation-architecture-and-hosting.md`
5. `implementation/phase-6/05-phase-6-scope-lock.md`
6. `implementation/phase-6/06-phase-6-implementation-detailed.md`
7. `implementation/phase-6/07-phase-6-api-job-and-storage-contracts.md`
8. `implementation/phase-6/08-phase-6-frontend-viewer-and-delivery-workflows.md`
9. `implementation/phase-6/09-phase-6-checkpoint-execution-plan.md`
10. `implementation/phase-6/10-phase-6-testing-release-and-acceptance-gates.md`
11. `implementation/phase-6/11-phase-6-dev-readiness-checklist.md`
12. `docs/phases/phase-6/checkpoints/README.md`

Optional future-program reading only:

- `implementation/phase-6/04-independent-research-requirements-for-bim-and-premium-cgi.md`

## What “Ready for Dev” Means in This Phase

Phase 6 is only considered dev-ready if the team can start implementation without reopening:

- what the target output is,
- what data the 3D lane may consume,
- what modules belong on app host versus GPU host,
- what APIs and job states are required,
- what the viewer and delivery UI must show,
- what quality gates block release,
- and what is explicitly out of scope.

This doc set is intended to freeze exactly those decisions.
