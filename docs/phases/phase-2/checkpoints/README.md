# Phase 2 Checkpoints

Phase 2 is locked to [implementation/11-phase2-layer2-full-deliverable.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/11-phase2-layer2-full-deliverable.md:1).

## Sequence

| Order | Code | Checkpoint | Depends On | Target |
|---|---|---|---|---|
| 0 | `cp0-phase2-readiness` | Phase 2 Readiness Gate | — | Confirm Layer 1.5 baseline, export contract, and repo/runtime prerequisites |
| 1 | `cp1-geometry-layer2` | Geometry Layer 2 | `cp0-phase2-readiness` | Canonical Layer 2 geometry, validation, backward-compatible migration path |
| 2 | `cp2-elevations-dimensions` | 4 Elevations + Enhanced Dimensions | `cp1-geometry-layer2` | 4 elevations, 2 sections, dimension engine, schedule marks |
| 3 | `cp3-schedules` | Schedules | `cp2-elevations-dimensions` | Door, window, room/area schedules plus CSV exports |
| 4 | `cp4-dxf-export` | DXF Export | `cp3-schedules` | Model space + paper space DXF package with title blocks and layers |
| 5 | `cp5-ifc-foundation` | IFC Foundation | `cp4-dxf-export` | Basic IFC handoff from the same canonical geometry |
| 6 | `cp6-integration-qa` | Integration + QA | `cp5-ifc-foundation` | Unified export package, production verification, loop validation |

## Notes

- The source of truth for deliverable scope remains [implementation/11-phase2-layer2-full-deliverable.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/11-phase2-layer2-full-deliverable.md:1).
- The market-standard analysis baseline for downstream teams is [00-market-standard-2d-output-requirements.md](/Users/nguyenquocthong/project/ai-architect-mvp/docs/phases/phase-2/00-market-standard-2d-output-requirements.md:1).
- `CP0` is added as a readiness gate to preserve the checkpoint contract used across this workspace.
- Every checkpoint folder contains `README.md`, `INSTRUCTIONS.md`, and `CHECKLIST.md` so implementation and validation can be run independently.
