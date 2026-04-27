---
title: UI E2E Professional Deliverables Handoff - Implementation Contract
phase: 2
status: approved-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# Implementation Contract

## Scope

Implement the first product E2E slice for Phase 2 professional deliverables:

```text
generated DesignVersion -> Review page trigger -> async job -> canonical professional bundle -> UI artifact links
```

## Allowed Changes

API repo:

- `app/models.py`
- `app/schemas.py`
- `app/api/v1/router.py`
- new `app/api/v1/professional_deliverables.py`
- new `app/services/professional_deliverables/geometry_adapter.py`
- new or updated `app/services/professional_deliverables/*orchestrator*.py`
- existing Sprint 1-3 generator modules, only to generalize golden-only functions while preserving current wrappers
- `app/tasks/professional_deliverables.py`
- Alembic migration under `alembic/versions/`
- tests under `tests/`
- `Makefile` only for new local verification commands
- Dockerfile/tooling under `tools/sprint3/` or a clearly named professional worker Dockerfile

Web repo:

- `src/components/review-client.tsx`
- `src/components/delivery-client.tsx`
- new `src/lib/professional-deliverables.ts`
- minimal shared UI helper/component if needed

Docs/compose repo:

- `docker-compose.local.yml`
- this handoff folder if opencode needs to append notes
- optional local runbook docs under `docs/phase-2/`

## Forbidden Changes

- No remote push.
- No PR creation.
- No ADR-001 changes.
- No PRD-05 acceptance relaxation.
- No Sprint 4 outputs: final `manifest.json`, reel, hero still, GIF.
- No IFC export.
- No Pascal Editor integration.
- No ISO 19650 process compliance.
- No TCVN/QCVN compliance implementation.
- No Specular-Glossiness workflow.
- No procedural material generation.
- No external model import/upload support.
- Do not replace the accepted golden fixture pipeline.
- Do not run heavy render/generation synchronously in a FastAPI request.
- Do not put Blender/KTX/FFmpeg into the main API container.

## API Contract

Add a new professional deliverables namespace:

```http
POST /api/v1/versions/{version_id}/professional-deliverables/jobs
GET  /api/v1/versions/{version_id}/professional-deliverables
GET  /api/v1/professional-deliverables/jobs/{job_id}
POST /api/v1/professional-deliverables/jobs/{job_id}/retry
```

Use `architect` and `admin` role protection, consistent with existing export/presentation routes.

Version eligibility:

- `locked`, `handoff_ready`, and `delivered` are eligible.
- `generated` and `under_review` are not eligible.
- Missing or unsupported `geometry_json` must return a clear 409/422 style error, not a silent fallback to golden fixture.

## Database Contract

Add dedicated records rather than overloading legacy `ExportPackage` or `Presentation3DBundle`.

Recommended model names:

- `ProfessionalDeliverableBundle`
- `ProfessionalDeliverableJob`
- `ProfessionalDeliverableAsset`

Minimum fields:

Bundle:

- `id`
- `project_id`
- `version_id`
- `status`: `queued | running | ready | failed`
- `quality_status`: `pending | pass | partial | fail`
- `is_degraded`
- `degraded_reasons_json`
- `gate_summary_url`
- `runtime_metadata_json`
- `created_by`
- timestamps

Job:

- `id`
- `bundle_id`
- `job_type`: `generate_professional_bundle`
- `status`: `queued | running | succeeded | failed`
- `stage`
- `progress_percent`
- `attempt_count`
- `error_code`
- `error_message`
- `started_at`
- `finished_at`
- timestamps

Asset:

- `id`
- `bundle_id`
- `asset_type`
- `asset_role`
- `storage_key`
- `public_url`
- `content_type`
- `byte_size`
- `checksum`
- optional width/height/duration
- `metadata_json`
- `created_at`

Add Alembic migration and keep `Base.metadata.create_all` tests passing.

## Geometry Adapter Contract

Create:

```text
app/services/professional_deliverables/geometry_adapter.py
```

Required function shape:

```python
def geometry_to_drawing_project(
    *,
    project_id: str,
    project_name: str,
    brief_json: dict | None,
    geometry_json: dict | None,
    issue_date: date | None = None,
) -> DrawingProject:
    ...
```

Rules:

- Accept only schema `ai-architect-geometry-v2`.
- Derive lot dimensions from `geometry["site"]["boundary"]`.
- Derive floors from `levels` where `type == "floor"`.
- Map `L1 -> floor 1`, `L2 -> floor 2`, etc.
- Convert room polygons into `Room`.
- Convert wall start/end into `WallSegment`.
- Convert openings from wall-relative data into `Opening(start, end)`.
- Convert fixtures into `Fixture` with deterministic kind mapping.
- Use `geometry["roof"]` plus site/building boundary to produce a valid roof outline.
- Use `site.orientation_north_deg` for north angle.
- Use project/brief style where available.
- Translate common generated room names/types to Vietnamese for visible labels.
- Call `validate_project_contract` and raise a clear adapter error on failure.

Do not generate from scratch if geometry is missing. Fail clearly.

## Generator Contract

Preserve existing accepted functions:

- `generate_golden_bundle`
- `generate_golden_3d_bundle`
- `generate_golden_ar_video_bundle`

Add project-based functions that those wrappers can reuse:

```python
generate_project_2d_bundle(project: DrawingProject, output_root: Path, ...)
generate_project_3d_bundle(project: DrawingProject, output_root: Path, ...)
generate_project_ar_video_bundle(project: DrawingProject, output_root: Path, ...)
```

The project-based functions must write into:

```text
professional-deliverables/projects/{project_id}/versions/{version_id}/
```

or an equivalent project/version scoped layout documented in the report.

DWG behavior:

- Local product E2E may use `require_dwg=False` unless ODA is configured.
- Missing DWG must be represented as a skipped/partial gate with reason.
- PDF, DXF, GLB, FBX, USDZ, and MP4 are required.

Video behavior:

- Must generate actual `master_4k.mp4`.
- Must use async worker path.
- UI must not wait on the render request synchronously.

## Job Progress Contract

Use deterministic stage names and progress values:

```text
queued: 0
adapter: 10
export_2d: 25
export_3d: 50
export_usdz: 65
render_video: 85
validate: 95
ready: 100
failed: preserve last progress
```

The Review page progress bar must display:

- percentage
- current stage label
- failure message if failed

The UI should poll while status is `queued` or `running`.

## Docker Contract

Extend:

```text
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docker-compose.local.yml
```

Add:

```text
professional-worker
```

Requirements:

- Shares `DATABASE_URL`, `REDIS_URL`, storage volume, and app env with API.
- Uses a Dockerfile/toolchain containing Blender 4.5.1, KTX 4.4.2, FFmpeg/ffprobe, Node 22, Python 3.12, and `usd-core==26.5`.
- Runs Celery worker for professional deliverables jobs.
- Uses Docker Compose as the local deployment path.
- Does not require Docker-in-Docker.

Recommended command:

```bash
celery -A app.tasks.worker.celery_app worker --loglevel=info -Q professional_deliverables --uid=nobody --gid=nogroup
```

If existing Celery routing is not queue-aware, add explicit routing in Celery config or call `.apply_async(..., queue="professional_deliverables")`.

## UI Contract

Review page:

- Add button: `Tạo Phase 2 Professional Deliverables`.
- Enable only for eligible locked/handoff/delivered versions.
- On click, POST professional deliverables job.
- Show progress bar and stage.
- Show ready/failed state.
- Provide shortcut link to Delivery page.

Delivery page:

- Show latest professional deliverables bundle for the active version.
- Show quality status.
- Show artifact links by role:
  - PDF
  - DXF
  - DWG when available
  - GLB
  - FBX
  - USDZ
  - MP4
  - gate summary JSON
  - gate summary MD

Do not remove existing legacy handoff or presentation bundle UI. Add a separate professional deliverables panel.

## Verification Plan

API focused tests:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py
```

Full API tests if time permits:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
make test
```

Golden regression:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
make sprint3-ci-linux
```

Web verification:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Local product E2E:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
docker compose -f docker-compose.local.yml up --build
```

Then verify manually through the UI:

- create/generate/approve version
- click professional deliverables on Review page
- progress bar moves
- Delivery page exposes artifact links
- generated storage contains PDF, DXF, GLB, FBX, USDZ, MP4, gate summaries

## Completion Rule

Return `PASS` only if:

- code compiles/builds;
- focused API tests pass;
- web lint/build pass;
- local Docker Compose E2E is documented and either verified or blocked with exact reason;
- no forbidden scope is touched.

Return `BLOCKED` if Blender/KTX/FFmpeg worker build, local video render, or geometry adapter correctness prevents true E2E.

