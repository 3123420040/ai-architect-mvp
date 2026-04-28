---
title: UI E2E Professional Deliverables Remediation Implementation Contract
phase: 2
status: ready-for-fix-implementation
date: 2026-04-27
owner: Codex Coordinator
related_retro: 09-retro-action-plan.md
source_project_id: 3b00f863-3144-4223-b04d-dec825c894d8
---

# UI E2E Professional Deliverables Remediation Implementation Contract

This document is the implementation handoff for fixing the full set of issues found during the local retro for project `3b00f863-3144-4223-b04d-dec825c894d8`.

Use this as the source of truth for remediation work. The goal is not to redefine the product. The goal is to make the existing Phase 2 UI E2E professional deliverables flow usable, observable, and honest for a real local customer journey.

## Inputs To Read First

Read these files before changing code:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/03-adr-001-standards-combo.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/04-deferred-roadmap.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/05-prd-deliverables.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/07-local-git-verification-protocol.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/00-context.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/01-requirements.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/02-system-analysis.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/03-implementation-contract.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/09-retro-action-plan.md`
- This file.

## Repos

- API repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- Web repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-web`
- Docs/compose repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`

## Product Objective

Fix the local product E2E flow so that a customer can:

1. Enter a natural Vietnamese brief and see correctly extracted critical requirements or clear follow-up questions.
2. Generate design versions and see working floor-plan images.
3. Understand which design version is current and approved.
4. Trigger professional deliverables from Review.
5. Watch truthful job progress.
6. See useful failure, partial, or ready state.
7. Download Phase 2 professional deliverables from Delivery.
8. Open a working 3D viewer for the generated professional GLB when available.
9. Open a working share link.

## Non-goals

Do not add new product scope while fixing this:

- No remote push.
- No PR unless explicitly requested later.
- No ADR-001 changes.
- No PRD-05 acceptance relaxation.
- No Sprint 4 product outputs in the Phase 2 UI E2E path.
- No IFC.
- No Pascal Editor integration.
- No ISO 19650 process compliance.
- No TCVN/QCVN implementation.
- No Specular-Glossiness.
- No procedural materials.
- No external model upload/import.
- Do not replace or weaken the golden fixture pipeline.
- Do not run heavy generation synchronously inside a FastAPI request.
- Do not remove existing legacy export, handoff, or presentation 3D UI.

## Required End State

The same current version must be selected by Designs, Review, Delivery, and Viewer.

For the current version:

- Images load.
- Review can create or retry a professional deliverables job.
- Progress follows the approved Phase 2 stages.
- Delivery shows the real professional bundle state.
- Generated artifacts are shown only when they exist and are readable.
- Failed states are customer-readable and include expandable technical details.
- Viewer uses the professional GLB when it exists.
- Share links load through the correct API path.

## PM Decisions Locked For Remediation

The following decisions are approved and should be treated as implementation requirements:

- Asset access: use API proxy or presigned URL helper. Do not depend on raw private MinIO URLs. Do not make public MinIO bucket access the product default.
- Partial artifacts: allow users/devs to download valid generated artifacts from failed or partial bundles, but label them clearly as `Partial / not final`.
- Viewer: allow the Viewer to render a professional deliverables GLB from a failed or partial bundle if the GLB asset itself is valid, with a visible warning.
- Current version: latest `locked` version is the source of truth for the current approved version.
- Intake: fix deterministic parser failures first. Real structured LLM extraction is not required in this remediation.

## Regression Fixtures

Preserve and use these local fixtures during debugging:

- Project under investigation:
  - `3b00f863-3144-4223-b04d-dec825c894d8`
- Problem versions:
  - V2 `e888ad98-597c-4d52-872f-7b5f3106499c`
  - V4 `b0f39796-d4ba-43f8-92e8-058004ce64d6`
- V2 known failure:
  - invalid `master_4k.mp4`
  - ffprobe error: `moov atom not found`
- V4 known failure:
  - valid 4K MP4
  - validation failure: `Camera collision sanity - Bep va an at 28.0s intersects wall-f1-07`
- Intake parser test project:
  - `dc759def-c7e7-4075-8bec-18a8a3baaa5e`
- Share token:
  - `k2GgHmvg6UG2SOEXdrP_C687`

## Implementation Order

Fix in this order. Do not start with the UI redesign before the backend state and asset foundations are correct.

1. Asset access and image loading.
2. Shared current-version selection.
3. Share link API path.
4. Remove Sprint 4 from the Phase 2 UI E2E path.
5. Professional deliverables job state, partial artifacts, and failure behavior.
6. Invalid MP4 handling.
7. Camera collision regression.
8. Professional worker `usd-core`.
9. Delivery and Review UX cleanup.
10. Viewer integration with professional GLB.
11. Designs lifecycle cleanup.
12. Intake parser improvements.
13. Full verification.

## Workstream A - Asset Access And Image Loading

### Problem

Generated floor plan images use direct MinIO URLs, but MinIO denies browser access with `403 AccessDenied`.

### Target Behavior

All user-facing asset URLs returned to the browser must be readable by the browser.

For local Phase 2, choose one explicit strategy:

- Preferred: return short-lived presigned URLs for object storage assets in API responses.
- Acceptable local-first fallback: configure MinIO bucket read policy for generated design assets.
- Acceptable app-level option: create a browser-readable API asset route that does not require an Authorization header for public/share-safe assets and validates access by signed token or opaque asset id.

Do not leave the UI using raw private MinIO URLs.

### Suggested API Design

Introduce a single asset URL resolution helper, for example:

- `resolve_public_asset_url(stored_url_or_key: str) -> str`
- `resolve_asset_key(stored_url_or_key: str) -> AssetRef`

Use it whenever returning:

- `DesignVersion.floor_plan_urls`
- professional deliverable asset URLs
- share page images
- delivery artifacts

If presigned URLs are used:

- Do not persist presigned URLs as permanent DB state.
- Persist bucket/key or canonical object reference.
- Generate browser-readable URLs at response time.

### Files To Inspect

- API: `app/services/storage.py`
- API: `app/models.py`
- API: project/version serializers or schemas
- API: `app/api/v1/share.py`
- API: `app/api/v1/professional_deliverables.py`
- Web: image rendering in Designs, Review, Delivery, Share

### Required UI Behavior

- Images must have stable containers.
- Broken image state must show a visible fallback.
- Empty image areas must not collapse.

### Acceptance Criteria

- Designs page image elements for the regression project have `naturalWidth > 0`.
- Review page current floor plan image has `naturalWidth > 0`.
- Delivery page version image has `naturalWidth > 0`.
- Share page images load when the token is valid.
- A missing asset shows a clear fallback state.

## Workstream B - Shared Current-Version Selection

### Problem

Different pages select different versions. Delivery can select a superseded version and hide real failed jobs.

### Target Behavior

All pages must use the same current-version rule.

### Required Rule

Implement a shared helper in Web, and optionally expose current version metadata from API.

Recommended rule:

1. Prefer latest `locked` and approved version by `version_number` or `created_at`.
2. Then latest `handoff_ready`.
3. Then latest `delivered`.
4. Then latest generated non-superseded candidate.
5. Only select `superseded` if it is the only version available, and label it clearly.

Do not select an older locked version just because it appears first in the list.

### Files To Change

- Web: `src/lib/version-selection.ts` or equivalent new shared helper.
- Web: `src/components/review-client.tsx`
- Web: `src/components/delivery-client.tsx`
- Web: `src/components/viewer-client.tsx`
- Web: Designs page/client component.

### Required UI Labels

Add consistent labels:

- `Current approved version`
- `Selected version`
- `Historical version`
- `Superseded`
- `Needs generation`

### Acceptance Criteria

- Designs, Review, Delivery, and Viewer select the same version for the regression project.
- Superseded versions are not selected by default.
- If multiple locked versions exist, the newest locked version is selected.

## Workstream C - Share Link API Path

### Problem

The share page calls `http://localhost:18000/share/{token}`. The backend route is mounted at `/api/v1/share/{token}`.

### Target Behavior

The share page must load the shared project through the correct API base path.

### Files To Change

- Web: `src/lib/api.ts`
- Web: `src/components/share-client.tsx`
- API: `app/api/v1/share.py` only if the contract needs clarification.

### Required Fix

- Fix public API URL composition.
- Avoid stripping `/api/v1` for API calls that need the API prefix.
- Normalize share read and feedback calls.

### Acceptance Criteria

- `http://localhost:3000/share/k2GgHmvg6UG2SOEXdrP_C687` renders shared project content.
- Browser no longer requests `http://localhost:18000/share/{token}`.
- Invalid token still shows a polished not-found/expired state.

## Workstream D - Remove Sprint 4 From Phase 2 Product Path

### Problem

The Phase 2 UI E2E path is creating or expecting Sprint 4 artifacts:

- `reel_9x16_1080p.mp4`
- `hero_still_4k.png`
- `preview.gif`
- `manifest.json`
- `sprint4_gate_summary.*`

These were explicitly forbidden for the Option B first slice.

### Target Behavior

The product path must generate only Phase 2 required deliverables:

- PDF
- DXF
- DWG only when ODA is configured, otherwise explicit skip
- GLB
- FBX
- USDZ
- `master_4k.mp4`
- gate summary JSON
- gate summary MD

### Files To Change

- API: `app/tasks/professional_deliverables.py`
- API: any product-path validators that require Sprint 4 outputs.
- Web: `src/lib/professional-deliverables.ts`
- Web: `src/components/delivery-client.tsx`

### Required Progress Contract

Use these stages only:

- `queued`: 0
- `adapter`: 10
- `export_2d`: 25
- `export_3d`: 50
- `export_usdz`: 65
- `render_video`: 85
- `validate`: 95
- `ready`: 100
- `failed`: preserve last progress and record error fields

### Acceptance Criteria

- New jobs do not run `derive_reel`.
- New jobs do not run `build_manifest`.
- New output roots do not contain Sprint 4 artifacts.
- Delivery page does not list Sprint 4 artifact slots.

## Workstream E - Job State, Partial Artifacts, And Failure Behavior

### Problem

Generated files can exist on disk, but no DB asset rows are registered when a later gate fails. Delivery then shows no useful links or state.

### Target Behavior

The API must truthfully expose:

- no job created
- queued
- running
- failed before artifacts
- failed after partial artifacts
- ready with warnings
- ready

### Required Backend Behavior

- Persist job stage and progress before each long-running step.
- Register generated assets after each successful generation phase, or persist them as partial assets.
- Store gate summaries even when final validation fails.
- Preserve failed job progress and error fields.
- Keep retry endpoint limited to failed jobs.
- Do not silently delete useful evidence after failure.

### Suggested Data Shape

Bundle response should include:

- `status`
- `quality_status`
- `current_job`
- `assets`
- `missing_artifacts`
- `failed_gates`
- `warnings`
- `retryable`
- `user_message`
- `technical_details`

Asset response should include:

- `kind`
- `status`: `ready`, `partial`, `failed`, `skipped`
- `url`
- `path`
- `skip_reason`
- `validation_error`

### Files To Change

- API: `app/models.py`
- API: `app/schemas.py`
- API: `app/api/v1/professional_deliverables.py`
- API: `app/tasks/professional_deliverables.py`
- API: Alembic migration if schema changes are needed.
- Web: `src/lib/professional-deliverables.ts`
- Web: `src/components/review-client.tsx`
- Web: `src/components/delivery-client.tsx`

### Acceptance Criteria

- If PDF/DXF/GLB/FBX/USDZ exist but video fails, Delivery shows those as partial artifacts.
- If video succeeds but camera validation fails, Delivery shows generated artifacts with a warning/failure state.
- Gate summary JSON/MD are available for failed jobs if they were generated.
- UI does not show raw ffmpeg/ffprobe output as the main message.

## Workstream F - Invalid MP4 Handling

### Problem

An invalid 48-byte `master_4k.mp4` was allowed to continue into later processing and failed with `moov atom not found`.

### Target Behavior

Invalid MP4 output must stop the job at `render_video` or `validate` with a structured error.

### Required Backend Behavior

- After ffmpeg returns, verify the MP4 with ffprobe before continuing.
- If ffprobe fails:
  - mark job failed
  - do not register MP4 as ready
  - do not run derivatives
  - preserve stderr/stdout
  - optionally move invalid file to a diagnostic path
- Store a stable error code such as `VIDEO_MASTER_INVALID`.

### Files To Change

- API: `app/services/professional_deliverables/video_renderer.py`
- API: `app/services/professional_deliverables/sprint3_demo.py`
- API: `app/tasks/professional_deliverables.py`
- API tests under `tests/professional_deliverables`

### Acceptance Criteria

- No invalid MP4 is shown as a downloadable artifact.
- Failure stage is `render_video` or `validate`, not `derive_reel`.
- Error has a short user message and technical details.

## Workstream G - Camera Collision Regression

### Problem

V4 produced a valid master video but failed camera collision validation.

### Target Behavior

Camera path generation must avoid wall collisions for current generated geometry, or fail early with a clear reason before expensive render.

### Required Backend Behavior

- Reproduce the V4 geometry collision locally.
- Add a fixture or regression test using equivalent geometry.
- Adjust path generation to maintain safe offsets from walls.
- Add fallback camera positions when the preferred path intersects walls.
- Run collision sanity before final render when possible.

### Files To Inspect

- API: `app/services/professional_deliverables/video_renderer.py`
- API: camera path helpers under `app/services/professional_deliverables/`
- API: geometry adapter if wall bounds are inflated or mislabeled.

### Acceptance Criteria

- The V4 fixture or equivalent layout passes camera collision sanity.
- If no safe path exists, job fails before rendering with `CAMERA_PATH_UNSAFE`.

## Workstream H - Professional Worker Toolchain

### Problem

The professional worker is missing `usd-core==26.5` even though it was required.

### Target Behavior

The worker image must contain all required heavy tools without bloating the main API image.

### Files To Change

- API: `Dockerfile.professional-worker`
- Docs/compose: `docker-compose.local.yml` only if command or environment changes are needed.

### Acceptance Criteria

Inside `professional-worker`:

```bash
blender --version
ktx --version
ffmpeg -version
ffprobe -version
node --version
python --version
python -m pip show usd-core
python -c "from pxr import Usd; print('ok')"
```

Required versions:

- Blender 4.5.1
- KTX 4.4.2
- FFmpeg/ffprobe installed
- Node 22
- Python 3.12
- `usd-core==26.5`

## Workstream I - Review UX Redesign

### Problem

Review is currently a confusing mix of version review, approval, export, share, and professional deliverables actions.

### Target Behavior

Review should guide the user through one clear workflow:

1. Inspect selected/current version.
2. Confirm selected version status.
3. Trigger professional deliverables.
4. Watch job progress.
5. Continue to Delivery or retry on failure.

### Required UI Behavior

- One primary action at a time.
- A clear current version badge.
- A clear selected version state.
- Floor-plan image fallback.
- Professional deliverables card with:
  - status
  - progress
  - current stage
  - short message
  - retry button when failed
  - link to Delivery when ready or partial
- Technical logs behind a disclosure.

### Files To Change

- Web: `src/components/review-client.tsx`
- Web: shared status/progress component if useful.
- Web: `src/lib/professional-deliverables.ts`

### Acceptance Criteria

- User can tell what version is selected.
- User can tell whether professional deliverables are not started, running, failed, partial, or ready.
- User can retry a failed job from Review.
- Raw ffmpeg text is not the main page message.

## Workstream J - Delivery UX Redesign

### Problem

Delivery selects the wrong version, hides failed jobs, lists forbidden artifact slots, and shows unavailable links.

### Target Behavior

Delivery is the artifact readiness and download workspace.

### Required UI Behavior

Professional deliverables panel must show:

- selected/current version
- bundle status
- quality status
- latest job status
- progress if running
- failed gates if failed
- generated artifacts
- skipped artifacts with reason
- retry action if eligible

Artifact slots for Phase 2 only:

- PDF
- DXF
- DWG
- GLB
- FBX
- USDZ
- MP4
- gate summary JSON
- gate summary MD

No Sprint 4 slots.

### Files To Change

- Web: `src/components/delivery-client.tsx`
- Web: `src/lib/professional-deliverables.ts`
- Web: shared artifact card/status component if useful.

### Acceptance Criteria

- Delivery uses the same current version as Review.
- Delivery shows existing failed bundle state for the current version.
- Delivery does not render anchors without usable `href`.
- DWG skip is explicit when ODA is unavailable.

## Workstream K - Viewer Integration With Professional GLB

### Problem

Viewer is tied to legacy Presentation3D and does not load professional deliverables GLB.

### Target Behavior

Viewer should prefer professional deliverables GLB for the current version when available, while preserving the legacy Presentation3D flow.

### Required UI Behavior

Viewer source priority:

1. Professional deliverables GLB asset for current version.
2. Legacy Presentation3D bundle if available.
3. Empty state with action to generate professional deliverables.

If a professional bundle failed after GLB was generated, the viewer may show the GLB with a warning.

### Files To Change

- Web: `src/components/viewer-client.tsx`
- Web: `src/lib/professional-deliverables.ts`
- API: `app/api/v1/professional_deliverables.py` if GLB URL is not exposed.

### Acceptance Criteria

- Viewer renders a GLB for the current version when the professional bundle has one.
- Viewer does not show a dead disabled action without explanation.
- If neither professional GLB nor legacy Presentation3D exists, empty state explains the next step.

## Workstream L - Designs UX Cleanup

### Problem

Designs shows multiple versions with unclear hierarchy and poor state handling.

### Target Behavior

Designs should communicate lifecycle and selection hierarchy.

### Required UI Behavior

Group or label versions as:

- Current approved version
- Candidate versions
- Historical/superseded versions

After a project is locked:

- Do not present generation as the main action.
- Provide an explicit revision action if supported.
- Provide a clear route to Review/Delivery.

### Files To Change

- Web: Designs page/client component.
- Web: shared version selection helper.

### Acceptance Criteria

- Current approved design is immediately visible.
- Superseded versions are visually de-emphasized.
- Broken or unavailable images have stable fallback states.

## Workstream M - Intake Parser Improvements

### Problem

The current intake extractor is deterministic and brittle for realistic Vietnamese customer language.

### Target Behavior

At minimum, deterministic parsing must handle common Vietnamese phrasing correctly. If the product claims AI-like intake, use structured LLM extraction with validation fallback.

### Short-Term Required Parser Fixes

- Dimension separators:
  - `7x25m`
  - `7 x 25m`
  - `7*25m`
  - `7 * 25 m`
  - `7 by 25`
- Compound orientations must match before simple orientations:
  - `Tay Nam` before `Tay`
  - `Dong Nam` before `Dong`
  - `Tay Bac` before `Tay`
  - `Dong Bac` before `Dong`
- Improve Vietnamese negation extraction:
  - `tranh khong gian bi`
  - `khong muon nha toi`
  - `han che phong toi`
- Do not mark the brief ready if a critical field was parsed ambiguously.

### Files To Change

- API: `app/services/briefing.py`
- API: `app/services/llm.py` only if enabling real LLM behavior.
- API tests for intake/brief parsing.
- Web: intake UI only if parsed-field confirmation needs visual changes.

### Regression Sentence

Use this sentence as a required parser test:

```text
Nha biet thu xay moi lo 7*25m huong Tay Nam, 3 tang, 4 phong ngu, 3 WC, gara 1 o to, phong tho, 6 nguoi o gom ong ba va 2 tre nho, phong cach hien dai am xanh gan gui tu nhien, ngan sach khoang 7 ty, muon hoan thanh trong 8 thang, bat buoc nhieu anh sang thong gio va tranh khong gian bi.
```

Expected extracted fields:

- `project_type`: villa
- `project_mode`: new build
- lot width: 7m
- lot depth: 25m
- lot area: 175m2
- orientation: southwest
- floors: 3
- bedrooms: 4
- bathrooms: 3
- garage: true
- prayer room: true
- occupants: 6
- budget: 7,000,000,000 VND
- timeline: 8 months
- priorities: daylight and ventilation
- negative constraint: avoid cramped/dark spaces

### Acceptance Criteria

- The regression sentence parses correctly in backend tests.
- UI shows extracted fields clearly before lock.
- Ambiguous critical fields require confirmation.

## API Contract Requirements

Professional deliverables endpoints must remain:

- `POST /api/v1/versions/{version_id}/professional-deliverables/jobs`
- `GET /api/v1/versions/{version_id}/professional-deliverables`
- `GET /api/v1/professional-deliverables/jobs/{job_id}`
- `POST /api/v1/professional-deliverables/jobs/{job_id}/retry`

Requirements:

- Use architect/admin auth for protected product routes.
- Share route can remain token-public.
- Eligible version statuses for job creation:
  - `locked`
  - `handoff_ready`
  - `delivered`
- Job creation must return quickly.
- Heavy work must run in Celery on the `professional_deliverables` queue.
- Failed jobs must preserve last progress.
- Retry must create or schedule a new attempt without overwriting useful failure evidence.

## Data Contract Requirements

If schema changes are needed, add Alembic migrations.

The data model must distinguish:

- bundle
- job
- asset
- skipped artifact
- failed artifact
- generated but not fully validated artifact

Do not overload `Presentation3DBundle`.

## UI State Contract

Use the same state vocabulary in Review and Delivery:

- `not_created`
- `queued`
- `running`
- `failed`
- `partial`
- `ready`
- `skipped`

Customer-facing copy should be short and clear.

Technical errors:

- Must be available for debugging.
- Must not be the primary customer message.
- Should be behind a details/expand control.

## Verification Commands

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

Docker local E2E:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
docker compose -f docker-compose.local.yml up --build
```

Worker toolchain:

```bash
docker exec kts-blackbirdzzzz-art-professional-worker blender --version
docker exec kts-blackbirdzzzz-art-professional-worker ktx --version
docker exec kts-blackbirdzzzz-art-professional-worker ffmpeg -version
docker exec kts-blackbirdzzzz-art-professional-worker ffprobe -version
docker exec kts-blackbirdzzzz-art-professional-worker node --version
docker exec kts-blackbirdzzzz-art-professional-worker python --version
docker exec kts-blackbirdzzzz-art-professional-worker python -m pip show usd-core
docker exec kts-blackbirdzzzz-art-professional-worker python -c "from pxr import Usd; print('ok')"
```

Manual browser verification:

1. Open the regression project Designs page.
2. Confirm all visible images load.
3. Open Review.
4. Confirm current version matches Designs.
5. Trigger or retry professional deliverables.
6. Confirm progress stages match the approved contract.
7. Open Delivery.
8. Confirm current version matches Review.
9. Confirm artifact links reflect actual generated files.
10. Open Viewer.
11. Confirm professional GLB renders if available.
12. Open share token URL.
13. Confirm shared project content loads.

## Required Report Format

After implementation, report using this format:

```text
Decision: PASS | BLOCKED | NEEDS_REVIEW

Repos:
- API repo:
- API branch:
- API dirty status:
- Web repo:
- Web branch:
- Web dirty status:
- Docs repo:
- Docs branch:
- Docs dirty status:

Summary:
- Fixed:
- Not fixed:
- Deferred:

Root-cause coverage:
- RC-01 asset access:
- RC-02 current version:
- RC-03 Sprint 4 removal:
- RC-04 partial/failure assets:
- RC-05 invalid MP4:
- RC-06 camera collision:
- RC-07 share link:
- RC-08 viewer GLB:
- RC-09 delivery UX:
- RC-10 review UX:
- RC-11 designs UX:
- RC-12 intake parser:
- RC-13 worker usd-core:

Files changed:
- API:
- Web:
- Docs/compose:

Commands run:
1.
2.
3.

Test results:
- API focused:
- API foundation/flows:
- Golden parity:
- Web lint:
- Web build:
- Docker Compose E2E:
- Worker toolchain:

Manual evidence:
- Project id:
- Version id:
- Job id:
- Bundle id:
- Current version selected consistently:
- Images load:
- Share link works:
- Viewer works:
- Delivery artifacts:

Known issues:
-

Scope compliance:
- No remote push:
- No PR:
- No Sprint 4 product outputs:
- No deferred roadmap items:
- No main API heavy toolchain:
- No synchronous render request:
```

## Pass/Fail Rules

Return `PASS` only if:

- Images load across Designs, Review, Delivery, and Share.
- Current version is consistent across product pages.
- Share link works.
- Review and Delivery show truthful professional deliverables state.
- New jobs do not run Sprint 4 stages or create Sprint 4 product outputs.
- Worker has `usd-core==26.5`.
- Web lint/build pass.
- API focused tests and Sprint 3 golden parity pass.
- Local product E2E produces or truthfully reports Phase 2 artifacts.

Return `NEEDS_REVIEW` if:

- A product decision is required, such as whether to use public MinIO, presigned URLs, or app-level asset proxy.
- Structured LLM extraction is required but credentials/config are unavailable.
- A non-critical UI cleanup remains but core E2E is correct.

Return `BLOCKED` if:

- Docker E2E cannot run.
- Professional worker cannot build.
- Required artifacts cannot be produced due to missing local toolchain.
- Database migration cannot be applied.

Do not mark the remediation complete if the UI merely hides errors without fixing the backend state or asset access contract.
