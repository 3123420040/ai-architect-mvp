---
title: UI E2E Professional Deliverables Retro Action Plan
phase: 2
status: needs-fix
date: 2026-04-27
owner: Codex Coordinator
source_project_id: 3b00f863-3144-4223-b04d-dec825c894d8
---

# UI E2E Professional Deliverables Retro Action Plan

This document records the concrete follow-up work after inspecting the local product flow for project `3b00f863-3144-4223-b04d-dec825c894d8`.

The earlier local sign-off proved that a happy-path project can produce a Phase 2 professional deliverables bundle. This retro shows that the broader product surface is not yet acceptable for customer use. The issues are systemic across asset serving, version selection, job orchestration, share links, 3D viewing, and UI state design.

## Current Decision

Decision: `NEEDS_FIX`

Reason: the tested project has broken visual assets, failed professional deliverables jobs, no registered downloadable assets, a broken share page, a disconnected 3D viewer, and a brittle non-LLM intake parser.

## Evidence Checked

- Web routes:
  - `http://localhost:3000/projects/3b00f863-3144-4223-b04d-dec825c894d8/intake`
  - `http://localhost:3000/projects/3b00f863-3144-4223-b04d-dec825c894d8/designs`
  - `http://localhost:3000/projects/3b00f863-3144-4223-b04d-dec825c894d8/review`
  - `http://localhost:3000/projects/3b00f863-3144-4223-b04d-dec825c894d8/delivery`
  - `http://localhost:3000/projects/3b00f863-3144-4223-b04d-dec825c894d8/viewer`
  - `http://localhost:3000/share/k2GgHmvg6UG2SOEXdrP_C687`
- API endpoints:
  - `GET /api/v1/versions/{version_id}/professional-deliverables`
  - `GET /api/v1/share/{token}`
  - `GET /api/v1/versions/{version_id}/presentation-3d`
- Data stores:
  - Postgres project, version, professional deliverable bundle/job/asset rows.
  - Local professional deliverables storage under `/app/storage/professional-deliverables/projects/...`.
  - MinIO direct object URLs for generated SVG floor plans.
- Logs:
  - `professional-worker` Celery task logs.
  - Browser failed requests and DOM image state via Playwright.
- Intake parser test:
  - Isolated project `dc759def-c7e7-4075-8bec-18a8a3baaa5e`.
  - Tested natural language Vietnamese brief with `7*25m` and `hướng Tây Nam`.

## Confirmed Root Causes

### RC-01 - Generated Images Are Not Publicly Readable

Symptom:

- Floor plan images fail on Designs, Review, and Delivery.
- Browser image elements are complete but have `naturalWidth = 0`.
- Direct MinIO object URL returns `403 AccessDenied`.

Root cause:

- `app/services/storage.py` returns direct MinIO URLs such as `http://localhost:19000/ai-architect-assets/...`.
- Stored objects or bucket policy are not public.
- The UI receives URLs that the browser cannot read.

Primary files:

- API: `app/services/storage.py`
- API: object upload sites that store `floor_plan_urls`
- Web: image rendering components in Designs, Review, Delivery

Required fix:

- Choose one explicit asset access model:
  - Preferred local-first option: expose an authenticated/public API asset proxy under `/api/v1/assets/...`.
  - Alternative: generate presigned URLs for browser reads.
  - Alternative only for local dev: make the MinIO bucket public in compose bootstrap.
- Ensure generated project/version image URLs are browser-readable from the Web container and from the host browser.
- Add visible broken-image fallback in UI instead of collapsed empty boxes.

Acceptance criteria:

- Every generated floor plan image for project `3b00f863-3144-4223-b04d-dec825c894d8` loads in Designs, Review, and Delivery.
- `img.naturalWidth > 0` for all displayed design/floor-plan images.
- Direct user-facing image URLs do not return MinIO `AccessDenied`.
- If an asset is missing, UI shows a clear state such as `Image unavailable`, not a broken placeholder.

Verification:

```bash
curl -I "<floor_plan_url>"
```

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Manual:

- Open Designs, Review, Delivery.
- Confirm all visible version/floor-plan images render.

### RC-02 - Product Has No Reliable Current Version Selection

Symptom:

- Designs shows multiple locked/approved versions without a clear active version.
- Review defaults to V2, although V4 is the newer locked/approved version.
- Delivery falls back to V6, a superseded version, then shows empty/404 deliverables.
- Viewer selects a different version than Delivery.

Root cause:

- Each page has its own version selection logic.
- `review-client.tsx` selects the first locked version.
- `delivery-client.tsx` ignores locked versions in the active selection path and falls back to the last version.
- There is no shared product definition of `current version`.

Primary files:

- Web: `src/components/review-client.tsx`
- Web: `src/components/delivery-client.tsx`
- Web: `src/components/viewer-client.tsx`
- Web: new shared helper, for example `src/lib/version-selection.ts`
- API: optionally expose `current_version_id` explicitly on project detail

Required fix:

- Define a single current-version rule.
- Recommended rule:
  1. Use `project.current_professional_bundle_id` only for bundle lookup, not for version selection.
  2. Prefer the latest approved `locked` version by `version_number` or `created_at`.
  3. Then `handoff_ready`.
  4. Then `delivered`.
  5. Then latest non-superseded generated version.
  6. Never select `superseded` by default unless it is the only available version and clearly label it.
- Implement shared helper and use it in Designs, Review, Delivery, and Viewer.
- Add visual label: `Current approved version`.

Acceptance criteria:

- Review, Delivery, and Viewer open the same current version for the same project.
- Superseded versions are visually de-emphasized and never silently selected.
- If there are multiple locked versions, the latest locked version is selected and older locked versions are marked as historical.

Verification:

- Open all project pages and confirm selected version id is the same.
- Add a focused Web unit test for the selection helper if the test setup supports it.

### RC-03 - Professional Deliverables Job Runs Forbidden Sprint 4 Scope

Symptom:

- Job stages include `derive_reel` and `build_manifest`.
- Storage contains Sprint 4 artifacts such as reel, hero still, GIF preview, manifest, and Sprint 4 gate summaries.
- Delivery UI also lists these Sprint 4 artifacts.

Root cause:

- The Option B implementation calls Sprint 4 derivative generation from the Phase 2 professional deliverables task.
- Required product artifact list includes forbidden Sprint 4 outputs.

Primary files:

- API: `app/tasks/professional_deliverables.py`
- API: `app/services/professional_deliverables/video_derivatives.py`
- Web: `src/components/delivery-client.tsx`
- Web: `src/lib/professional-deliverables.ts`

Required fix:

- Remove Sprint 4 derivative generation from the Option B first slice.
- Remove Sprint 4 artifact requirements from the product job validator.
- Remove Sprint 4 artifact labels from Delivery for this phase.
- Preserve Sprint 3 golden commands and any standalone Sprint 4 code if it exists, but do not call it from the Phase 2 UI E2E path.

Acceptance criteria:

- New job progress uses only the approved stages:
  - `queued 0`
  - `adapter 10`
  - `export_2d 25`
  - `export_3d 50`
  - `export_usdz 65`
  - `render_video 85`
  - `validate 95`
  - `ready 100`
  - `failed` preserves last progress
- New project/version output does not include Sprint 4 final manifest, reel, hero still, or GIF.
- Delivery does not show Sprint 4 artifact slots.

Verification:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
make sprint3-ci-linux
```

Manual:

- Trigger a new professional deliverables job from Review.
- Confirm observed stages match the approved contract.

### RC-04 - Failed Jobs Do Not Register Partial Evidence Or Customer-Readable Failure State

Symptom:

- For this project, `professional_deliverable_assets` has zero rows.
- V2 has PDF, GLB, FBX, USDZ, and an invalid MP4 on disk, but no registered assets.
- V4 has a valid 4K MP4 and other files on disk, but no registered assets because validation failed.
- Delivery shows no useful artifact state.

Root cause:

- Asset registration appears to happen only after all validation passes.
- A single failed gate prevents DB asset records from being created.
- UI has no distinction between:
  - not started
  - running
  - failed before artifact generation
  - failed after partial artifacts
  - ready with warnings

Primary files:

- API: `app/tasks/professional_deliverables.py`
- API: `app/api/v1/professional_deliverables.py`
- API: `app/models.py`
- API: `app/schemas.py`
- Web: `src/components/review-client.tsx`
- Web: `src/components/delivery-client.tsx`

Required fix:

- Persist job evidence throughout the pipeline, not only at final success.
- Register generated artifacts after each successful phase or persist them as `partial` assets.
- If validation fails after core outputs are created, bundle status should expose:
  - final status `failed` or `needs_fix`
  - `quality_status`
  - generated assets
  - failed gates
  - retry eligibility
- UI must show partial generated outputs separately from final approved deliverables.

Acceptance criteria:

- When video render fails, Review and Delivery show `Video render failed` with a short customer-readable message and a technical details expand/copy area.
- When validation fails after artifacts exist, Delivery lists generated artifacts with a warning state.
- Failed bundle API response includes enough structured data for the UI to show what happened without scraping raw error strings.

Verification:

- Re-run a failing job.
- Confirm DB has bundle/job rows and generated asset rows for completed phases.
- Confirm Delivery shows partial artifacts and failed gate summary.

### RC-05 - Video Pipeline Allows Invalid MP4 To Continue Into Later Steps

Symptom:

- V2 `master_4k.mp4` is only 48 bytes.
- ffprobe reports `moov atom not found`.
- Pipeline then fails later at `derive_reel 90%`.

Root cause:

- Sprint 3 render records gate failure but returns enough control to continue into derivative generation.
- Later derivative generation probes an invalid MP4 and fails with raw ffprobe text.

Primary files:

- API: `app/services/professional_deliverables/sprint3_demo.py`
- API: `app/services/professional_deliverables/video_renderer.py`
- API: `app/services/professional_deliverables/video_derivatives.py`
- API: `app/tasks/professional_deliverables.py`

Required fix:

- Treat failed master MP4 render as a terminal failure for this Option B job.
- Delete or quarantine invalid MP4 outputs before exposing them.
- Capture ffmpeg stderr/stdout into a structured error payload.
- Do not run any derivative step when master MP4 validation fails.

Acceptance criteria:

- An invalid `master_4k.mp4` cannot appear as a downloadable artifact.
- Job fails at `render_video` or `validate`, not at a later forbidden derivative stage.
- Error payload includes:
  - `error_code`
  - short user message
  - technical command/stderr detail
  - output path

Verification:

```bash
ffprobe -v error -show_format -show_streams "<master_4k.mp4>"
```

### RC-06 - Camera Collision Gate Fails On A Real Generated Version

Symptom:

- V4 generates a valid 4K video, but job fails at validation:
  - `Camera collision sanity - Bếp và ăn at 28.0s intersects wall-f1-07`

Root cause:

- Generated camera path can intersect derived walls for real project geometry.
- The camera planner and collision validator are not robust enough for this generated layout.

Primary files:

- API: `app/services/professional_deliverables/video_renderer.py`
- API: camera path or validation helpers under `app/services/professional_deliverables/`
- API: geometry adapter if room/wall bounds are over-constrained

Required fix:

- Inspect the generated DrawingProject for V4.
- Adjust camera path generation to keep a safe offset from walls.
- Add a fallback path strategy when a room path fails collision checks.
- Add a regression test using the project/version geometry that caused the failure.

Acceptance criteria:

- V4 or an equivalent fixture passes camera collision sanity.
- If a path cannot be generated safely, job fails before expensive video render with a clear reason.

Verification:

- Re-run professional deliverables job for the same V4 geometry.
- Confirm camera collision gate passes before final ready state.

### RC-07 - Share Link Frontend Calls The Wrong API Path

Symptom:

- `http://localhost:3000/share/k2GgHmvg6UG2SOEXdrP_C687` renders `{"detail":"Not Found"}`.
- Browser calls `http://localhost:18000/share/{token}`.
- Correct API endpoint is `http://localhost:18000/api/v1/share/{token}` and returns 200.

Root cause:

- `publicFetch()` strips `/api/v1` from `NEXT_PUBLIC_API_BASE_URL`.
- Share client uses `publicFetch("/share/...")`.

Primary files:

- Web: `src/lib/api.ts`
- Web: `src/components/share-client.tsx`
- API: `app/api/v1/share.py`

Required fix:

- Fix public API URL composition so share reads call `/api/v1/share/{token}`.
- Standardize feedback POST path as well.
- Add a browser-level smoke test for share token load.

Acceptance criteria:

- Existing share token page loads project/version content.
- Browser network tab has no 404 for `/share/{token}`.
- Invalid or expired token still shows a polished error state.

Verification:

```bash
curl -i http://localhost:18000/api/v1/share/k2GgHmvg6UG2SOEXdrP_C687
```

Manual:

- Open `http://localhost:3000/share/k2GgHmvg6UG2SOEXdrP_C687`.

### RC-08 - Viewer Uses Legacy Presentation3D Instead Of Professional Deliverables GLB

Symptom:

- Viewer page shows no 3D model.
- It calls `/api/v1/versions/{version_id}/presentation-3d` and receives 404.
- Professional deliverables GLB exists on disk for some failed jobs, but viewer does not use it.
- Create bundle action is disabled for locked versions.

Root cause:

- Viewer is wired to the legacy Presentation3D bundle pipeline.
- Option B professional deliverables GLB/FBX/USDZ outputs are not connected to the viewer.

Primary files:

- Web: `src/components/viewer-client.tsx`
- Web: `src/lib/professional-deliverables.ts`
- API: `app/api/v1/professional_deliverables.py`
- API: existing presentation 3D routes should be preserved

Required fix:

- Decide viewer behavior:
  - For Phase 2 delivery, viewer should prefer the professional deliverables GLB when available.
  - If no professional GLB exists, show an actionable state that links to Review/Delivery job creation.
  - Legacy Presentation3D should remain available but not block the professional deliverables viewer path.
- Ensure locked versions are eligible for viewing generated professional GLB assets.

Acceptance criteria:

- Viewer loads the professional GLB for the current version once the bundle has a GLB asset.
- If bundle failed after GLB generation, Viewer can show the GLB with warning.
- If no GLB exists, Viewer shows a clear empty state and next action.

Verification:

- Trigger or use an existing job with a GLB asset.
- Open Viewer and confirm a rendered 3D model appears.

### RC-09 - Delivery UX Shows The Wrong State And Forbidden Artifact Slots

Symptom:

- Delivery selects V6 `superseded`.
- Professional deliverables API returns 404 for that version.
- UI shows `Chưa tạo` even though V2/V4 have failed bundle jobs.
- It lists Sprint 4 artifact slots that are out of scope.

Root cause:

- Wrong active version selection.
- UI does not aggregate or surface existing failed jobs for the actual current version.
- Delivery artifact schema includes out-of-scope Sprint 4 artifacts.

Primary files:

- Web: `src/components/delivery-client.tsx`
- Web: `src/lib/professional-deliverables.ts`

Required fix:

- Use shared current-version helper.
- Remove Sprint 4 slots.
- Show professional bundle state as a first-class panel:
  - Not created
  - Queued/running with progress
  - Failed with reason and retry
  - Partial with warnings
  - Ready with artifact links
- Keep legacy export/handoff/presentation UI separate and clearly labeled.

Acceptance criteria:

- Delivery defaults to the same current version as Review.
- Delivery shows the failed professional deliverables job for the current version, not a false `not created` state.
- Delivery never shows unavailable links as normal anchors.

### RC-10 - Review UX Is Not A Usable Customer Workflow

Symptom:

- Review shows broken images, raw error logs, multiple disabled/enabled actions, and unclear next steps.
- User cannot easily understand what to do after selecting/approving a design.

Root cause:

- Review page exposes implementation actions without a state-driven workflow.
- Professional deliverables trigger was added without simplifying surrounding decision UI.

Primary files:

- Web: `src/components/review-client.tsx`

Required fix:

- Redesign Review around a small number of explicit states:
  1. Select a design version.
  2. Confirm/lock selected version.
  3. Generate professional deliverables.
  4. Track job progress.
  5. Resolve failure or continue to Delivery.
- Use one primary action at a time.
- Move technical details behind a disclosure.
- Add image fallback, selected/current labels, and consistent version badges.

Acceptance criteria:

- A user can tell which version is selected, whether it is approved, and what the next primary action is.
- Progress bar uses real backend job status.
- Raw ffmpeg/ffprobe text is not shown as the main customer-facing message.

### RC-11 - Designs UX Needs Lifecycle Cleanup

Symptom:

- Designs page remains generation-oriented after the project is locked.
- Superseded and locked versions compete visually.
- Broken images make cards unusable.

Root cause:

- Page is not organized around lifecycle state and current-version hierarchy.

Primary files:

- Web: designs page component and version card components

Required fix:

- Group versions:
  - Current approved version
  - Candidate versions
  - History/superseded
- Disable or de-emphasize generation actions after lock unless explicitly creating a revision.
- Add compare/review CTA from the current version.

Acceptance criteria:

- User can immediately identify the approved design.
- Superseded versions do not look equally selectable.
- Broken image fallback is visible and recoverable.

### RC-12 - Intake Parser Is Brittle For Natural Vietnamese Customer Language

Symptom:

- `7*25m` was not parsed as lot dimensions.
- `hướng Tây Nam` was parsed as `west`.
- The phrase `bắt buộc nhiều ánh sáng thông gió và tránh không gian bí` produced poor `must_haves`/`must_not_haves`.

Root cause:

- Intake extraction is deterministic regex/rules, not an LLM or robust NLU layer.
- Pattern order and separators are too narrow.

Primary files:

- API: `app/services/llm.py`
- API: `app/services/briefing.py`
- API tests for briefing/intake

Required fix:

- Short-term parser improvements:
  - Accept `*`, `x`, `×`, `by`, and Vietnamese variants for dimensions.
  - Match compound orientations before single-word orientations.
  - Improve Vietnamese negation and requirement splitting.
  - Add tests for realistic customer sentences.
- Product-level decision:
  - Either rename the feature as deterministic guided intake, or implement actual structured LLM extraction with deterministic validation fallback.

Acceptance criteria:

- The tested customer sentence extracts:
  - project type `villa`
  - mode `new_build`
  - lot `7m x 25m`
  - orientation `southwest`
  - 3 floors
  - 4 bedrooms
  - 3 bathrooms
  - garage
  - prayer room
  - 6 occupants
  - 7B VND budget
  - 8-month timeline
  - daylight and ventilation priorities
  - avoid cramped/dark spaces as a negative constraint
- The UI does not mark brief as ready if a critical field is parsed ambiguously.

Verification:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests -k "brief or intake"
```

Manual:

- Create a fresh project and paste the same natural-language request.
- Confirm extracted brief fields before locking.

### RC-13 - Professional Worker Missing usd-core

Symptom:

- Worker has Blender, KTX, FFmpeg, Node, and Python.
- `python -m pip show usd-core` reports package not found.
- `import pxr` fails.

Root cause:

- Professional worker Dockerfile does not install `usd-core==26.5`.

Primary files:

- API: `Dockerfile.professional-worker`
- Compose: `docker-compose.local.yml`

Required fix:

- Install `usd-core==26.5` into the professional worker image.
- Add a worker startup or CI verification command for `python -c "from pxr import Usd"`.

Acceptance criteria:

- Inside `professional-worker`, `python -m pip show usd-core` shows version `26.5`.
- Inside `professional-worker`, `python -c "from pxr import Usd"` exits 0.

Verification:

```bash
docker exec kts-blackbirdzzzz-art-professional-worker python -m pip show usd-core
docker exec kts-blackbirdzzzz-art-professional-worker python -c "from pxr import Usd; print('ok')"
```

## Recommended Fix Sequence

### P0 - Restore Basic Product Trust

1. Fix asset serving for generated images.
2. Fix share link API path.
3. Implement shared current-version selection and use it on Review, Delivery, Viewer, and Designs.
4. Remove Sprint 4 outputs from the Option B product path.
5. Fix professional deliverables job status so failed/partial states are visible and honest.

Exit criteria:

- Designs, Review, Delivery images load.
- Share link loads.
- Review and Delivery point at the same current version.
- Delivery no longer shows false `not created` for an existing failed job.
- New professional deliverables jobs do not create Sprint 4 artifacts.

### P1 - Make Deliverables Reliable

1. Stop pipeline correctly on invalid MP4.
2. Fix camera path collision for real generated geometry.
3. Register phase-by-phase assets and failed gate summaries.
4. Install and verify `usd-core==26.5` in professional worker.

Exit criteria:

- A locked generated version can produce ready or partial-with-clear-warning professional deliverables.
- `master_4k.mp4` is always ffprobe-valid before exposure.
- Failed gates are actionable, not raw infrastructure logs.

### P2 - Rebuild UX Around Workflow State

1. Redesign Review as a guided decision and job progress page.
2. Redesign Delivery as an artifact readiness/download page.
3. Connect Viewer to professional GLB assets.
4. Clean up Designs page lifecycle hierarchy.
5. Add customer-readable failure and empty states.

Exit criteria:

- A non-technical customer can understand which version is approved, what is being generated, what failed, and what can be downloaded.
- The UI does not expose unavailable links or raw backend errors as primary content.

### P3 - Improve Intake Intelligence

1. Patch deterministic parser for known Vietnamese input failures.
2. Add regression tests for realistic natural language briefs.
3. Decide whether Phase 2 requires real structured LLM extraction or an explicitly guided deterministic form.

Exit criteria:

- The tested Vietnamese brief is parsed correctly.
- Ambiguous critical fields require confirmation instead of silently accepting wrong data.

## Verification Plan After Fixes

API:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py
make sprint3-ci-linux
```

Web:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Docker:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
docker compose -f docker-compose.local.yml up --build
```

Manual product E2E:

1. Create a fresh project with natural Vietnamese input.
2. Confirm extracted brief fields before locking.
3. Generate design versions.
4. Confirm all design images load.
5. Lock one version and confirm all pages select the same current version.
6. Trigger professional deliverables from Review.
7. Observe progress through approved stages.
8. Open Delivery and confirm artifact links for PDF, DXF, GLB, FBX, USDZ, MP4, gate JSON, and gate MD.
9. Confirm DWG skip is explicit if ODA is unavailable.
10. Open Viewer and confirm professional GLB renders.
11. Open share link and confirm the shared project loads.

## Regression Fixtures To Preserve

- Project under investigation:
  - `3b00f863-3144-4223-b04d-dec825c894d8`
- Problem versions:
  - V2 `e888ad98-597c-4d52-872f-7b5f3106499c`: invalid MP4, `moov atom not found`.
  - V4 `b0f39796-d4ba-43f8-92e8-058004ce64d6`: valid MP4 but camera collision gate fail.
- Intake parser test project:
  - `dc759def-c7e7-4075-8bec-18a8a3baaa5e`
- Share token:
  - `k2GgHmvg6UG2SOEXdrP_C687`

These should be used as local regression references while fixing the product flow.
