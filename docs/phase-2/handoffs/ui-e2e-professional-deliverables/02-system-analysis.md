---
title: UI E2E Professional Deliverables Handoff - System Analysis
phase: 2
status: approved-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# System Analysis

## Current Product Flow

The current UI can create projects, lock briefs, generate design versions, review versions, approve versions, export legacy packages, create handoff bundles, and create presentation 3D jobs.

Relevant files:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/models.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/api/v1/generation.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/api/v1/exports.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/api/v1/presentation_3d.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/src/components/review-client.tsx`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/src/components/delivery-client.tsx`

`DesignVersion.geometry_json` is the source geometry for generated versions. It uses schema `ai-architect-geometry-v2`.

## Current Professional Deliverables Flow

The accepted Phase 2 professional deliverables pipeline currently runs from hardcoded golden fixture wrappers:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/demo.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/sprint2_demo.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/sprint3_demo.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/golden_fixture.py`

The professional deliverables contract is:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/drawing_contract.py`

`DrawingProject` requires:

- project id/name
- lot dimensions
- storey count
- style
- issue date
- rooms
- walls
- openings
- fixtures
- roof outline
- north angle

## Gap

There is no adapter from:

```text
DesignVersion.geometry_json -> DrawingProject
```

There is also no product-facing API/job/UI for:

```text
version -> professional deliverables bundle
```

The existing `exports.py` route calls the older `app.services.exporter.export_phase2_package`, not the accepted Sprint 1-3 professional deliverables implementation.

The existing `presentation_3d.py` route creates a different 3D presentation bundle and should not be repurposed for Phase 2 professional deliverables.

## Existing Patterns to Reuse

Use the existing `presentation_3d` architecture as the closest async job pattern:

- API route creates bundle/job.
- Orchestrator serializes bundle/job.
- Celery task updates stage and progress.
- Web polls latest bundle/job and derives a state bucket.
- Assets are grouped and exposed as URLs.

Relevant files:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/presentation_3d/orchestrator.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/tasks/presentation_3d.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/src/lib/presentation-3d.ts`

Do not mix professional deliverables into `presentation_3d` tables or API names. The outputs, gates, and product meaning are different.

## Data Flow Target

```text
Review page click
  -> POST /api/v1/versions/{version_id}/professional-deliverables/jobs
  -> create ProfessionalDeliverableBundle + ProfessionalDeliverableJob
  -> queue Celery task on professional_deliverables queue
  -> load Project + DesignVersion
  -> geometry_to_drawing_project(...)
  -> generate 2D bundle
  -> generate 3D bundle
  -> generate USDZ + master_4k.mp4
  -> run/write gate summaries
  -> register artifacts
  -> job progress 100, bundle ready
  -> Review/Delivery UI polls and shows links
```

## Docker Analysis

`docker-compose.local.yml` currently builds `api` and `worker` from the slim API image. That image is not appropriate for Blender/KTX/FFmpeg rendering.

Add a separate `professional-worker` service using the Sprint 3 parity toolchain. This service must share:

- Redis broker.
- Postgres database.
- `api_storage` volume.

The main API container stays slim.

## Storage Path

Use a project/version scoped path to avoid overwriting the golden fixture:

```text
storage/professional-deliverables/projects/{project_id}/versions/{version_id}/
  2d/
  3d/
  textures/
  video/
  sprint3_gate_summary.json
  sprint3_gate_summary.md
```

Expose files through existing `/media` static mount.

## Risks

- The current generated geometry may contain English room labels. Professional deliverable labels should be Vietnamese where visible. Add a deterministic name translation map for common room names/types.
- Opening conversion requires deriving start/end coordinates from `wall_id`, `position_along_wall_m`, and `width_m`.
- Local 4K MP4 generation is intentionally slow. UI must show progress and not time out the request.
- ODA may not be installed locally. DWG can be skipped only with an explicit gate reason.
- Alembic migrations exist. Any new database tables or columns must include a migration and tests must still pass.

## Assumptions

- This slice only needs to support geometry generated by `build_geometry_v2` / `ensure_geometry_v2`.
- The accepted Sprint 1-3 CLI/parity commands remain the regression oracle.
- The first UI E2E implementation can provide a deterministic, minimal material mapping. Rich external material libraries remain out of scope.

