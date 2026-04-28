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
| 7 | `cp7-pascal-editor-integration` | Pascal Editor Integration | `cp1-geometry-layer2`, `cp6-integration-qa` (soft) | Vendor Pascal editor, adapter geometry Layer 2 ↔ scene, replace 3D viewer, mo KTS edit mode |
| 8 | `cp8-style-knowledge-base` | Style Knowledge Base | `cp6-integration-qa` + output quality baseline | Structured style profiles, avoid rules, drawing rules, and seed pattern memory |
| 9 | `cp9-conversation-style-inference` | Conversation Style Inference | `cp8-style-knowledge-base` | Sparse Vietnamese chat/reference-image signals → customer understanding and style candidates |
| 10 | `cp10-concept-model-contract` | Concept Model Contract | `cp9-conversation-style-inference` | Renderer-safe ArchitecturalConceptModel with provenance and assumptions |
| 11 | `cp11-layout-technical-defaults` | Layout Technical Defaults | `cp10-concept-model-contract` | Program planner, first-pass layout, and style-aware technical defaults |
| 12 | `cp12-concept-2d-render-qa` | Concept 2D Render QA | `cp11-layout-technical-defaults` | DrawingPackageModel, PDF/DXF concept render, semantic and visual QA |
| 13 | `cp13-client-review-revision-loop` | Client Review Revision Loop | `cp12-concept-2d-render-qa` | Chat/annotation feedback → structured revision operations and child versions |
| 14 | `cp14-integrated-concept-package` | Integrated Concept Package | `cp13-client-review-revision-loop` | End-to-end sparse homeowner scenarios and final concept package acceptance |

## Notes

- The source of truth for deliverable scope remains [implementation/11-phase2-layer2-full-deliverable.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/11-phase2-layer2-full-deliverable.md:1).
- The market-standard analysis baseline for downstream teams is [00-market-standard-2d-output-requirements.md](/Users/nguyenquocthong/project/ai-architect-mvp/docs/phases/phase-2/00-market-standard-2d-output-requirements.md:1).
- The AI concept 2D style intelligence workflow is [19-ai-concept-2d-style-intelligence-workflow.md](/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/19-ai-concept-2d-style-intelligence-workflow.md:1).
- `CP0` is added as a readiness gate to preserve the checkpoint contract used across this workspace.
- Every checkpoint folder contains `README.md`, `INSTRUCTIONS.md`, and `CHECKLIST.md` so implementation and validation can be run independently.
