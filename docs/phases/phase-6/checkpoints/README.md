# Phase 6 Checkpoints

This folder is the execution control pack for **Phase 6 — Program A: Presentation-grade 3D**.

It converts the Phase 6 technical design into checkpoint folders that a delivery team can execute and validate without reopening scope decisions.

## Locked Source Documents

Phase 6 execution is locked to:

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
- `implementation/phase-6/13-phase-6-technical-design-detailed.md`
- `implementation/phase-6/14-phase-6-detailed-checkpoint-breakdown.md`

Future-program research only:

- `implementation/phase-6/04-independent-research-requirements-for-bim-and-premium-cgi.md`

## Hard Execution Rules

1. No team starts `CP(n+1)` until `CP(n)` has a green validator result.
2. Every checkpoint must write:
   - `artifacts/phase6/<cp-code>/result.json`
   - `artifacts/phase6/<cp-code>/notes.md`
3. Every validation pass must write:
   - `artifacts/phase6/<cp-code>/validation.json`
4. `CP3` and all later checkpoints must use the locked fixture pack under:
   - `implementation/phase-6/mock-inputs/`
5. `Program B` and `Program C` requirements are explicitly out of scope.
6. Final client release is blocked unless:
   - source version is approved,
   - QA blocking checks pass,
   - architect approval is recorded,
   - manifest references the released asset set.

## Locked Shared Interfaces

### Public resources

- `presentation_3d_bundle`
- `presentation_3d_job`
- `presentation_3d_asset`
- `presentation_3d_approval`

### Backend enums

- `bundle.status = queued | running | awaiting_approval | released | failed`
- `bundle.qa_status = pending | pass | warning | fail`
- `bundle.approval_status = not_requested | awaiting_approval | approved | rejected`
- `bundle.delivery_status = preview_only | blocked | released`
- `job.status = queued | running | succeeded | failed`
- `job.stage = scene_spec | runtime_dispatch | runtime_render | output_ingest | qa | manifest | approval_ready`

### Public endpoints

- `POST /versions/{version_id}/presentation-3d/jobs`
- `GET /versions/{version_id}/presentation-3d`
- `GET /presentation-3d/bundles/{bundle_id}`
- `GET /presentation-3d/jobs/{job_id}`
- `POST /presentation-3d/jobs/{job_id}/retry`
- `POST /presentation-3d/bundles/{bundle_id}/approve`
- `POST /presentation-3d/bundles/{bundle_id}/reject`

### Minimum release artifacts

- `scene.glb`
- `renders/exterior_hero_day.png`
- `renders/exterior_entry.png`
- `renders/living_room.png`
- `renders/kitchen_dining.png`
- `renders/master_bedroom.png`
- `video/walkthrough.mp4`
- `manifest/presentation_manifest.json`
- `qa/qa_report.json`

### Asset storage convention

- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/scene/scene.glb`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/scene/scene_spec.json`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/renders/{shot_id}.png`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/video/walkthrough.mp4`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/manifest/presentation_manifest.json`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/qa/qa_report.json`

### Frontend states

- `idle`
- `queued`
- `running`
- `preview_degraded`
- `awaiting_approval`
- `released`
- `failed`

## Common Tooling

Use these helper files from this folder:

- `config.example.json`
- `notify.py`
- `post-status.py`

Recommended local setup:

1. Copy `config.example.json` to `config.json`.
2. Fill `project_slug`, `dashboard_url`, and `ntfy_topic`.
3. Use the helper scripts in each CP instruction file.

## Common Result File Schema

`artifacts/phase6/<cp-code>/result.json`

```json
{
  "cp": "cp0-phase6-scope-lock-and-baseline-audit",
  "role": "implementer",
  "status": "READY",
  "timestamp": "2026-04-13T17:00:00+07:00",
  "summary": "Checkpoint goal is complete and ready for validation.",
  "artifacts": [],
  "issues": [],
  "notes": "",
  "executed_commands": []
}
```

`artifacts/phase6/<cp-code>/validation.json`

```json
{
  "cp": "cp0-phase6-scope-lock-and-baseline-audit",
  "role": "validator",
  "status": "PASS",
  "timestamp": "2026-04-13T18:00:00+07:00",
  "summary": "Checkpoint checks passed.",
  "checks": [],
  "issues": [],
  "ready_for_next_cp": true,
  "next_cp": "cp1-phase6-persistence-and-migrations"
}
```

## Common Validation Commands

Backend:

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest -q
```

Frontend:

```bash
cd ../ai-architect-web && pnpm build
```

GPU:

```bash
cd ../ai-architect-gpu && python3 -m pytest -q
```

Phase 6 mock baseline:

```bash
python3 scripts/phase6_3d_mock_demo.py
```

## Checkpoint Sequence

| Order | Code | Checkpoint | Depends On | Main target |
|---|---|---|---|---|
| 0 | `cp0-phase6-scope-lock-and-baseline-audit` | Scope Lock and Baseline Audit | — | Freeze scope, fixtures, render expectations, and validation plan |
| 1 | `cp1-phase6-persistence-and-migrations` | Persistence and Migrations | `cp0-phase6-scope-lock-and-baseline-audit` | Add Phase 6 DB backbone and enum model |
| 2 | `cp2-phase6-api-contracts-and-serializers` | API Contracts and Serializers | `cp1-phase6-persistence-and-migrations` | Expose bundle-first API and typed frontend consumption |
| 3 | `cp3-phase6-scene-spec-builder` | Scene Spec Builder | `cp2-phase6-api-contracts-and-serializers` | Generate deterministic scene spec from approved version truth |
| 4 | `cp4-phase6-job-orchestration-and-state-machine` | Job Orchestration and State Machine | `cp3-phase6-scene-spec-builder` | Replace sync derive with tracked async execution |
| 5 | `cp5-phase6-storage-and-asset-registry` | Storage and Asset Registry | `cp4-phase6-job-orchestration-and-state-machine` | Separate scratch vs durable storage and register assets |
| 6 | `cp6-phase6-glb-export-runtime` | GLB Export Runtime | `cp5-phase6-storage-and-asset-registry` | Produce non-placeholder GLB via runtime contract |
| 7 | `cp7-phase6-still-render-lane` | Still Render Lane | `cp6-phase6-glb-export-runtime` | Produce required curated still set |
| 8 | `cp8-phase6-video-lane` | Video Lane | `cp7-phase6-still-render-lane` | Produce walkthrough MP4 with locked duration rules |
| 9 | `cp9-phase6-qa-validator-and-degraded-policy` | QA Validator and Degraded Policy | `cp8-phase6-video-lane` | Validate completeness and enforce preview-only degraded mode |
| 10 | `cp10-phase6-approval-gate-and-manifest` | Approval Gate and Manifest | `cp9-phase6-qa-validator-and-degraded-policy` | Release control and manifest-first contract |
| 11 | `cp11-phase6-viewer-and-delivery-experience` | Viewer and Delivery Experience | `cp10-phase6-approval-gate-and-manifest` | Replace debug viewer with presentation workspace |
| 12 | `cp12-phase6-e2e-release-and-production-validation` | E2E Release and Production Validation | `cp11-phase6-viewer-and-delivery-experience` | Validate full client-ready package on real flow |

## Notes

- Phase 6 is the execution phase for `Program A: Presentation-grade 3D` only.
- The first locked still set is:
  - `exterior_hero_day`
  - `exterior_entry`
  - `living_room`
  - `kitchen_dining`
  - `master_bedroom`
- The first locked walkthrough target is `45–90 seconds`, `1080p minimum`, `30 fps`.
- The first locked presentation mode is `client_presentation`.
