# Phase 6 Checkpoints

Phase 6 is locked to:

- `implementation/phase-6/01-3d-output-research-and-direction.md`
- `implementation/phase-6/02-3d-module-input-contracts.md`
- `implementation/phase-6/03-3d-presentation-architecture-and-hosting.md`
- `implementation/phase-6/05-phase-6-scope-lock.md`
- `implementation/phase-6/06-phase-6-implementation-detailed.md`
- `implementation/phase-6/07-phase-6-api-job-and-storage-contracts.md`
- `implementation/phase-6/08-phase-6-frontend-viewer-and-delivery-workflows.md`
- `implementation/phase-6/09-phase-6-checkpoint-execution-plan.md`
- `implementation/phase-6/10-phase-6-testing-release-and-acceptance-gates.md`
- `implementation/phase-6/11-phase-6-dev-readiness-checklist.md`

Future-program research only:

- `implementation/phase-6/04-independent-research-requirements-for-bim-and-premium-cgi.md`

## Sequence

| Order | Code | Checkpoint | Depends On | Target |
|---|---|---|---|---|
| 0 | `cp0-phase6-scope-lock` | Scope Lock and Contract Freeze | — | Freeze Program A scope, inputs, outputs, and out-of-scope lines |
| 1 | `cp1-persistence-bundle-backbone` | Persistence and Bundle Backbone | `cp0-phase6-scope-lock` | Add bundle/job/asset/QA/approval backbone and new API shape |
| 2 | `cp2-scene-spec-builder` | Scene Spec Builder | `cp1-persistence-bundle-backbone` | Generate deterministic `presentation_scene_spec` from approved version |
| 3 | `cp3-async-job-orchestration` | Async Job Orchestration | `cp2-scene-spec-builder` | Move 3D generation to queued jobs with visible progress |
| 4 | `cp4-gpu-runtime-artifact-generation` | GPU Runtime and Artifact Generation | `cp3-async-job-orchestration` | Produce real GLB, still renders, MP4, and object-storage-backed assets |
| 5 | `cp5-qa-degraded-policy` | QA Validator and Degraded Policy | `cp4-gpu-runtime-artifact-generation` | Validate bundle completeness and block degraded delivery |
| 6 | `cp6-approval-delivery-integration` | Approval Gate and Delivery Integration | `cp5-qa-degraded-policy` | Add architect approval, manifest, and delivery release control |
| 7 | `cp7-presentation-viewer-ux` | Presentation Viewer UX | `cp6-approval-delivery-integration` | Replace debug viewer with client-ready presentation workspace |
| 8 | `cp8-production-validation` | Production Deployment and Validation | `cp7-presentation-viewer-ux` | Validate full end-to-end truth on production |

## Notes

- Phase 6 is the execution phase for `Program A: Presentation-grade 3D` only.
- Program B and Program C are intentionally separated and must not be pulled into Phase 6 scope.
- Production truth remains the final acceptance gate.
