---
title: UI E2E Professional Deliverables Handoff - Review Checklist
phase: 2
status: approved-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# Review Checklist

Use this checklist when opencode reports back.

## Scope

- Implementation supports only system-generated `DesignVersion.geometry_json`.
- No external import/upload support was added.
- No Sprint 4 deliverables were added.
- No deferred roadmap item was implemented.
- No remote push or PR was created.

## Architecture

- Heavy work runs through Celery, not a synchronous FastAPI request.
- A dedicated `professional-worker` service exists.
- Main API image remains slim.
- Professional deliverables have their own API namespace and persistence model.
- Existing legacy export, handoff, and presentation 3D flows still exist.
- Golden fixture functions still work.

## Geometry Adapter

- Accepts only `ai-architect-geometry-v2`.
- Fails clearly on missing/unsupported geometry.
- Converts floors, rooms, walls, openings, fixtures, roof, north angle, and style.
- Labels visible in professional deliverables are Vietnamese where generated room labels are known.
- `validate_project_contract` is called before export.

## API

- Auth/role protection matches existing architect/admin routes.
- Eligible version statuses are enforced.
- Job create endpoint returns quickly.
- Status endpoints return stage/progress/errors/assets.
- Retry endpoint handles only failed jobs.
- Alembic migration exists for new tables/columns.

## UI

- Review page has trigger and progress bar.
- Progress bar uses real job progress.
- Failure state is visible.
- Delivery page shows professional deliverables separately from presentation 3D.
- Artifact links use `assetUrl`/media URL conventions.

## Outputs

- Output path is project/version scoped.
- PDF exists.
- DXF exists.
- GLB exists.
- FBX exists.
- USDZ exists.
- MP4 exists and is the real master video.
- Gate summary JSON/MD exists.
- DWG skip is explicit when ODA is unavailable.

## Tests

- Focused adapter/job tests pass.
- API foundation/flow tests pass.
- Alembic test passes.
- Sprint 3 local parity still passes.
- Web lint/build pass.
- Docker Compose local E2E is verified or a clear blocker is reported.

## Decision Outcomes

Return `ACCEPTED` only if all acceptance criteria are met.

Return `NEEDS_FIX` if implementation violates scope, breaks accepted pipeline, or misses required UI/API behavior.

Return `NEEDS_MORE_TESTS` if code appears correct but verification is insufficient.

Return `NEEDS_CLARIFICATION` if opencode hit a product decision not covered by this contract.

