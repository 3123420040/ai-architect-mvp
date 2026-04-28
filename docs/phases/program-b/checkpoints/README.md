# Program B Checkpoints

This folder is the execution control pack for **Program B Release 1 — Coordination-ready architectural handoff**.

It converts the Program B technical design into checkpoint folders that a delivery team can execute and validate without reopening scope decisions.

## Locked Source Documents

Program B execution is locked to:

- `implementation/program-b/01-program-b-scope-lock.md`
- `implementation/program-b/02-program-b-requirements-detailed.md`
- `implementation/program-b/03-program-b-technical-design-detailed.md`
- `implementation/program-b/04-program-b-implementation-detailed.md`
- `implementation/program-b/05-program-b-checkpoint-execution-plan.md`
- `implementation/program-b/06-program-b-detailed-checkpoint-breakdown.md`

Supporting context:

- `implementation/phase-6/program-b-bim-and-construction-research-report.md`
- `implementation/phase-6/04-independent-research-requirements-for-bim-and-premium-cgi.md`

## Hard Execution Rules

1. No team starts `CP(n+1)` until `CP(n)` has a green validator result.
2. Every checkpoint must write:
   - `artifacts/program-b/<cp-code>/result.json`
   - `artifacts/program-b/<cp-code>/notes.md`
3. Every validation pass must write:
   - `artifacts/program-b/<cp-code>/validation.json`
4. Launch scope is limited to:
   - `townhouse`
   - `villa`
5. Native BIM authoring, Revit connector work, and multi-discipline BIM are explicitly out of scope.
6. Final release is blocked unless:
   - source version is approved,
   - semantic model build succeeds,
   - required schedules exist,
   - coordination IFC exists,
   - architect review is recorded,
   - manifest references the released asset set.

## Locked Shared Interfaces

### Public resources

- `coordination_model`
- `coordination_schedule_snapshot`
- `coordination_issue`
- `coordination_handoff_bundle`
- `coordination_job`

### Backend enums

- `coordination_model.status = pending | built | verified | failed`
- `quantity_item.confidence_status = system_derived | review_required | verified`
- `issue.status = open | in_review | resolved | waived`
- `bundle.status = queued | running | awaiting_review | ready_for_release | released | failed`
- `bundle.delivery_status = internal_only | consultant_review | released | blocked`
- `job.status = queued | running | succeeded | failed`
- `job.stage = eligibility_check | semantic_model_build | quantity_extract | ifc_export | bundle_package | qa_validate | awaiting_review | released`

### Public endpoints

- `POST /versions/{version_id}/coordination-handoff/jobs`
- `GET /versions/{version_id}/coordination-handoff`
- `GET /coordination-handoff/bundles/{bundle_id}`
- `GET /coordination-handoff/jobs/{job_id}`
- `GET /coordination-handoff/bundles/{bundle_id}/schedules`
- `GET /coordination-handoff/bundles/{bundle_id}/issues`
- `POST /coordination-handoff/bundles/{bundle_id}/issues`
- `POST /coordination-issues/{issue_id}/resolve`
- `POST /coordination-handoff/bundles/{bundle_id}/release`

### Minimum release artifacts

- `model/coordination_model.json`
- `ifc/architectural_coordination.ifc`
- `schedules/room_schedule.csv`
- `schedules/door_window_schedule.csv`
- `schedules/area_schedule.csv`
- `issues/issue_register.json`
- `manifest/coordination_manifest.json`
- `reports/readiness_summary.json`

### Asset storage convention

- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/model/coordination_model.json`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/ifc/architectural_coordination.ifc`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/schedules/{schedule_name}.csv`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/issues/issue_register.json`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/manifest/coordination_manifest.json`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/reports/readiness_summary.json`

### Frontend states

- `idle`
- `queued`
- `running`
- `awaiting_review`
- `ready_for_release`
- `released`
- `blocked`
- `failed`

## Shared Tooling

Use the shared helper scripts already available in:

- `docs/phases/phase-6/checkpoints/notify.py`
- `docs/phases/phase-6/checkpoints/post-status.py`

## Checkpoint Sequence

| Order | Code | Checkpoint | Depends On | Main target |
|---|---|---|---|---|
| 0 | `cp0-program-b-scope-lock-and-semantic-baseline` | Scope Lock and Semantic Baseline | — | Freeze launch truth, validation thresholds, and semantic minimum |
| 1 | `cp1-program-b-semantic-model-and-persistence` | Semantic Model and Persistence | `cp0-program-b-scope-lock-and-semantic-baseline` | Add Program B DB backbone and semantic core |
| 2 | `cp2-program-b-quantity-and-issue-contracts` | Quantity and Issue Contracts | `cp1-program-b-semantic-model-and-persistence` | Generate schedules and issue registry resources |
| 3 | `cp3-program-b-coordination-ifc-export` | Coordination IFC Export | `cp2-program-b-quantity-and-issue-contracts` | Produce architectural coordination IFC |
| 4 | `cp4-program-b-handoff-package-and-manifest` | Handoff Package and Manifest | `cp3-program-b-coordination-ifc-export` | Freeze release artifact set and readiness summary |
| 5 | `cp5-program-b-delivery-workspace-and-status` | Delivery Workspace and Status | `cp4-program-b-handoff-package-and-manifest` | Surface Program B value in the product |
| 6 | `cp6-program-b-downstream-validation-pilot` | Downstream Validation Pilot | `cp5-program-b-delivery-workspace-and-status` | Validate real continuation value on benchmark cases |
| 7 | `cp7-program-b-release-readiness-and-launch-gate` | Release Readiness and Launch Gate | `cp6-program-b-downstream-validation-pilot` | Close blockers and freeze launch evidence |

## Notes

- Program B Release 1 is the execution scope for coordination-ready architectural handoff only.
- Launch typologies are `townhouse` and `villa`.
- Homeowner-facing value is readiness and transparency, not raw BIM tooling.
- If a requirement depends on native authoring or multi-discipline BIM, it belongs to a later Program B release.
