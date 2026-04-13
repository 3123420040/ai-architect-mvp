# Phase 6 Technical Design Detailed

## 1. Purpose

This document translates the locked Phase 6 scope into a concrete technical design that engineering can implement and then break into execution checkpoints.

It is intentionally implementation-facing.

It does not re-argue product scope.

It assumes the following are already locked:

- [00-README.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/00-README.md:1)
- [05-phase-6-scope-lock.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/05-phase-6-scope-lock.md:1)
- [06-phase-6-implementation-detailed.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/06-phase-6-implementation-detailed.md:1)
- [07-phase-6-api-job-and-storage-contracts.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/07-phase-6-api-job-and-storage-contracts.md:1)
- [08-phase-6-frontend-viewer-and-delivery-workflows.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/08-phase-6-frontend-viewer-and-delivery-workflows.md:1)

## 2. As-Is Technical Reality

The current system has a 3D lane, but it is still the pre-Phase-6 placeholder implementation.

Current backend behavior:

- `POST /versions/{version_id}/derive-3d` is synchronous
- it checks locked version state
- it calls the GPU boundary directly
- it persists `model_url` and `render_urls` on `design_versions`

Reference:

- [app/api/v1/derivation.py](/Users/nguyenquocthong/project/ai-architect-api/app/api/v1/derivation.py:23)

Current GPU behavior:

- returns placeholder `model_gltf`
- returns SVG render placeholders
- reports `gpu_available` based on `nvidia-smi`, but production currently runs in non-GPU mode

Reference:

- [ai-architect-gpu/api/server.py](/Users/nguyenquocthong/project/ai-architect-gpu/api/server.py:41)
- [ai-architect-gpu/api/server.py](/Users/nguyenquocthong/project/ai-architect-gpu/api/server.py:211)

Current viewer behavior:

- reads `model_url`
- fetches raw model text
- shows render previews
- acts as a technical verification page, not a delivery workspace

Reference:

- [src/components/viewer-client.tsx](/Users/nguyenquocthong/project/ai-architect-web/src/components/viewer-client.tsx:23)

Current persistence reality:

- `DesignVersion` only has `render_urls`, `model_url`, and generic `generation_metadata`
- there is no first-class 3D bundle/job/asset/QA/approval persistence yet

Reference:

- [app/models.py](/Users/nguyenquocthong/project/ai-architect-api/app/models.py:74)

## 3. Target Technical Outcome

The Phase 6 target is not "better placeholder renders".

It is a bundle-oriented architecture that can truthfully produce:

- `scene.glb`
- required still renders
- `walkthrough.mp4`
- `presentation_manifest.json`
- `qa_report.json`
- architect approval state

This must run through:

`approved version -> scene spec -> async jobs -> artifacts -> QA -> approval -> release`

## 4. System Decomposition

Phase 6 should be implemented as seven cooperating subsystems.

### 4.1 3D Eligibility and Trigger Layer

Owned by API.

Responsibilities:

- verify source version eligibility
- reject draft or unstable sources
- create bundle/job records
- enqueue execution

Primary modules:

- `app/api/v1/presentation_3d.py`
- `app/services/presentation_3d/eligibility.py`
- `app/services/presentation_3d/orchestrator.py`

### 4.2 Scene Spec Builder

Owned by app-side worker/service.

Responsibilities:

- read approved version truth
- normalize geometry references
- normalize room semantics
- bind visual rules
- generate deterministic `presentation_scene_spec`

Primary modules:

- `app/services/presentation_3d/scene_spec_builder.py`
- `app/services/presentation_3d/material_mapping.py`
- `app/services/presentation_3d/shot_planner.py`

### 4.3 Async Job Scheduler

Owned by worker and Redis broker.

Responsibilities:

- schedule bundle execution
- track job stage and progress
- retry eligible failures
- separate app orchestration from render execution

Primary modules:

- `app/tasks/presentation_3d.py`
- `app/services/presentation_3d/job_tracker.py`

### 4.4 GPU Render Runtime

Owned by dedicated GPU runtime.

Responsibilities:

- assemble render scene
- export `scene.glb`
- render stills
- render video frames and assemble MP4

Primary modules in GPU repo:

- `ai-architect-gpu/api/server.py`
- `ai-architect-gpu/pipelines/scene_builder.py`
- `ai-architect-gpu/pipelines/blender_export.py`
- `ai-architect-gpu/pipelines/still_render.py`
- `ai-architect-gpu/pipelines/video_render.py`

### 4.5 QA Validator

Owned by app-side worker/service.

Responsibilities:

- verify required artifact completeness
- validate basic geometry and metadata integrity
- produce `qa_report.json`
- assign `pass | warning | fail`

Primary modules:

- `app/services/presentation_3d/qa.py`

### 4.6 Manifest and Release Layer

Owned by API/service.

Responsibilities:

- generate `presentation_manifest.json`
- store release metadata
- enforce approval gate
- expose signed URLs

Primary modules:

- `app/services/presentation_3d/manifest.py`
- `app/api/v1/presentation_3d.py`

### 4.7 Viewer and Delivery Consumption Layer

Owned by web app.

Responsibilities:

- show progress state
- show preview vs released state
- show still gallery, video, and model action
- expose architect approval actions

Primary modules:

- `src/components/viewer-client.tsx`
- `src/components/delivery-client.tsx`
- new `src/lib/presentation-3d.ts` or equivalent fetch adapter

## 5. Data Model Design

## 5.1 Design principle

Do not overload `design_versions` further than necessary.

`DesignVersion` should remain the source design object.

Phase 6 should introduce dedicated persistence for generated 3D presentation bundles.

## 5.2 Proposed new tables

### A. `presentation_3d_bundles`

Purpose:

- one row per generated 3D presentation bundle

Suggested columns:

- `id`
- `project_id`
- `version_id`
- `scene_spec_revision`
- `status`
- `qa_status`
- `approval_status`
- `delivery_status`
- `is_degraded`
- `degraded_reasons_json`
- `scene_spec_url`
- `manifest_url`
- `qa_report_url`
- `created_by`
- `approved_by`
- `approved_at`
- `created_at`
- `updated_at`

### B. `presentation_3d_jobs`

Purpose:

- track async execution and retries

Suggested columns:

- `id`
- `bundle_id`
- `job_type`
- `status`
- `stage`
- `progress_percent`
- `attempt_count`
- `error_code`
- `error_message`
- `runtime_metadata_json`
- `started_at`
- `finished_at`
- `created_at`
- `updated_at`

### C. `presentation_3d_assets`

Purpose:

- record every generated artifact

Suggested columns:

- `id`
- `bundle_id`
- `asset_type`
- `asset_role`
- `storage_key`
- `public_url`
- `content_type`
- `byte_size`
- `checksum`
- `width`
- `height`
- `duration_seconds`
- `metadata_json`
- `created_at`

### D. `presentation_3d_approvals`

Purpose:

- keep explicit review decisions rather than burying them inside the bundle row only

Suggested columns:

- `id`
- `bundle_id`
- `decision`
- `notes`
- `reviewed_by`
- `reviewed_at`

## 5.3 Relationship to current models

`DesignVersion` should gain only minimal linkage:

- optional `current_presentation_3d_bundle_id`

`Project` does not need denormalized 3D fields in Phase 6 unless proven necessary for dashboard performance.

## 5.4 Migration strategy

Use additive migrations only:

1. create new Phase 6 tables
2. backfill nothing initially
3. keep legacy `model_url` and `render_urls` readable during transition
4. migrate viewer and APIs to bundle-first reads

## 6. API Design

## 6.1 New router

Add a dedicated router rather than expanding the old derivation route:

- `app/api/v1/presentation_3d.py`

Reason:

- Phase 6 is bundle-oriented, async, approval-gated, and stateful
- the old route shape is too narrow and too misleading

## 6.2 Required endpoints

### A. Create bundle job

`POST /versions/{version_id}/presentation-3d/jobs`

Responsibilities:

- validate eligibility
- create bundle row if needed
- create job row
- dispatch worker

### B. Get latest bundle

`GET /versions/{version_id}/presentation-3d`

Responsibilities:

- return current bundle shape for frontend
- act as primary viewer fetch contract

### C. Get bundle detail

`GET /presentation-3d/bundles/{bundle_id}`

Responsibilities:

- return full internal detail for approval and support tooling

### D. Get job detail

`GET /presentation-3d/jobs/{job_id}`

Responsibilities:

- return status, stage, progress, error fields

### E. Retry job

`POST /presentation-3d/jobs/{job_id}/retry`

Responsibilities:

- allow controlled retry when status permits

### F. Approve bundle

`POST /presentation-3d/bundles/{bundle_id}/approve`

Responsibilities:

- record approval
- release bundle when QA allows

### G. Reject bundle

`POST /presentation-3d/bundles/{bundle_id}/reject`

Responsibilities:

- preserve preview
- block release
- record notes

## 6.3 Legacy endpoint handling

The old derivation route should not stay as the primary path.

Preferred approach:

- mark `POST /versions/{version_id}/derive-3d` as legacy
- internally forward or explicitly deprecate it
- move UI off that route

## 7. Scene Spec Builder Design

## 7.1 Inputs

The builder should read:

- `Project`
- source `DesignVersion`
- approved geometry JSON
- room summaries
- selected/derived material mapping
- render request preset

## 7.2 Builder pipeline

Suggested internal steps:

1. `load_source_version`
2. `validate_geometry_minimums`
3. `extract_room_semantics`
4. `derive_facade_and_orientation`
5. `apply_material_mapping`
6. `build_staging_rules`
7. `plan_still_shots`
8. `plan_walkthrough_sequence`
9. `emit_scene_spec`

## 7.3 Output file

Persist `scene_spec.json` as first-class artifact, even if it is also stored in DB metadata.

Reason:

- GPU runtime should consume a stable file or signed URL
- support debugging and replay

## 7.4 Deterministic scope

Phase 6 builder does not need to solve perfect geometry reconstruction from arbitrary drawings.

It needs to deterministically package already-approved geometry into a presentation-scene contract.

## 8. Worker and Job Design

## 8.1 App-side orchestration job

Suggested Celery task chain:

1. `build_scene_spec_task(bundle_id)`
2. `dispatch_render_runtime_task(bundle_id)`
3. `ingest_render_outputs_task(bundle_id)`
4. `run_qa_task(bundle_id)`
5. `build_manifest_task(bundle_id)`
6. `mark_bundle_awaiting_approval_task(bundle_id)`

## 8.2 Why chain the work

This makes failure recovery clearer:

- scene spec failures stay app-side
- runtime failures stay runtime-side
- QA failures do not erase generated assets

## 8.3 Retry policy

Recommended retry rules:

- scene spec build: retry 0-1 times only
- object storage upload: retry 2-3 times
- GPU runtime call: retry 1-2 times
- QA task: retry 0 times unless due to storage read issue

## 8.4 Progress update design

Progress should be written to DB and optionally emitted to WS/SSE.

The frontend should not rely solely on long-lived websocket continuity.

Preferred truth source:

- DB status first
- WS/SSE as enhancement

## 9. GPU Runtime Design

## 9.1 Runtime boundary

The GPU runtime should be treated as a render execution service, not as product orchestration.

It should not decide:

- whether the source version is allowed
- whether the result is releasable
- whether approval passes

## 9.2 GPU request contract

Input:

- `bundle_id`
- `scene_spec_url` or payload
- render preset
- requested outputs
- output storage target

Output:

- artifact metadata list
- runtime metadata
- success or failure payload

## 9.3 Blender pipeline responsibility

The Blender-side scripts should handle:

- scene graph assembly
- material binding
- camera placement from shot definitions
- GLB export
- still render export
- video frame output

## 9.4 Video design

Recommended simple first implementation:

- render image sequence from planned camera path
- encode to MP4 with FFmpeg

Do not overcomplicate first release with:

- path editing UI
- sound
- narration
- advanced edit transitions

## 9.5 Runtime image requirements

The GPU image should include:

- Blender headless
- FFmpeg
- Python runtime
- NVIDIA runtime support
- fonts and minimal material asset pack

## 10. Storage Design

## 10.1 Scratch vs durable storage

Separate clearly:

- local scratch during render
- durable object storage for final assets

## 10.2 Required object prefixes

Use stable paths:

- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/scene/scene.glb`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/scene/scene_spec.json`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/renders/{shot_id}.png`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/video/walkthrough.mp4`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/manifest/presentation_manifest.json`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/qa/qa_report.json`

## 10.3 Storage adapter

Do not let GPU runtime or frontend reimplement storage logic.

Prefer one adapter layer in API repo:

- `app/services/storage.py`

Extend it with:

- signed URL generation for Phase 6 assets
- checksum capture
- media metadata helpers

## 11. QA Validator Design

## 11.1 Phase 6 QA focus

QA in this phase is not BIM-grade geometric proof.

It is release-safety QA for presentation bundles.

## 11.2 Required checks

Minimum checks:

- source version locked and approved
- scene spec exists
- GLB exists and non-empty
- required still count present
- required room shots present
- MP4 exists and duration in allowed range
- manifest exists and references all released assets
- no broken signed/public URL references

## 11.3 Output shape

Recommended check item schema:

```json
{
  "check_id": "video_present",
  "status": "pass",
  "severity": "blocking",
  "message": "Walkthrough video exists and is readable."
}
```

## 11.4 Degraded assignment

Assign degraded when:

- required output is missing
- output exists but fails blocking QA
- runtime had partial fallback path

Do not assign degraded merely because visuals are not artist-grade.

## 12. Manifest Design

## 12.1 Manifest purpose

The manifest is the release contract for viewer and delivery.

It is not just metadata decoration.

## 12.2 Required sections

Suggested manifest sections:

- `manifest_version`
- `bundle_identity`
- `source_identity`
- `approval`
- `qa_summary`
- `delivery_state`
- `assets`
- `branding`
- `disclaimer`
- `generation_metadata`

## 12.3 Why manifest-first matters

Without a manifest, viewer and delivery code will drift into reading ad hoc fields from multiple places.

Phase 6 should centralize release truth here.

## 13. Frontend Technical Design

## 13.1 Fetch model

The viewer should fetch:

1. bundle summary from API
2. signed/public asset URLs from bundle payload
3. no raw local file paths

## 13.2 State model

Suggested client state buckets:

- `idle`
- `queued`
- `running`
- `preview_degraded`
- `awaiting_approval`
- `released`
- `failed`

## 13.3 Component decomposition

Suggested components:

- `Presentation3DStatusCard`
- `Presentation3DProgressPanel`
- `Presentation3DHero`
- `Presentation3DGallery`
- `Presentation3DVideo`
- `Presentation3DApprovalPanel`
- `Presentation3DDownloadPanel`

## 13.4 Delivery integration

Update delivery workspace so it can render:

- latest bundle status
- release state
- view/download actions

without treating 3D as a side-link to a debug page.

## 14. Rollout Design

## 14.1 Migration-safe rollout

Recommended rollout sequence:

1. add tables and APIs behind feature flag
2. build bundle flow in parallel with legacy route
3. shift frontend to bundle APIs
4. deprecate legacy route

## 14.2 Production gating

Do not enable client-delivery release until:

- object storage is configured
- GPU runtime is reachable
- QA and approval gates are functioning

## 14.3 Legacy coexistence window

During migration:

- keep `model_url` and `render_urls` readable
- but stop expanding them as the long-term contract

## 15. Risks and Technical Trade-offs

## 15.1 Risk: overloading current app host

Mitigation:

- keep heavy rendering off the app host

## 15.2 Risk: scene spec too weak

Mitigation:

- validate geometry minimums early
- persist scene spec and test it with fixtures

## 15.3 Risk: GPU runtime drift

Mitigation:

- runtime should consume a strict scene-spec schema
- runtime should not improvise business logic

## 15.4 Risk: frontend built on unstable fields

Mitigation:

- bundle-first API
- manifest-first release contract

## 16. Checkpoint Break Anchors

This section is the bridge from technical design into checkpoint breakdown.

## 16.1 Backend contract and persistence anchor

Break into:

1. schema migration for Phase 6 tables
2. ORM models
3. API schemas
4. bundle creation endpoint
5. bundle/job detail endpoints

## 16.2 Scene spec and orchestration anchor

Break into:

1. eligibility validator
2. scene spec builder
3. job tracker
4. Celery tasks
5. progress persistence

## 16.3 GPU runtime anchor

Break into:

1. render runtime contract
2. scene assembly implementation
3. GLB export
4. still render pack
5. walkthrough video generation

## 16.4 QA and manifest anchor

Break into:

1. QA rules
2. degraded-state assignment
3. manifest schema
4. approval gate logic

## 16.5 Frontend anchor

Break into:

1. viewer data adapter
2. progress UI
3. released vs preview state handling
4. approval panel
5. delivery workspace integration

## 16.6 Release and validation anchor

Break into:

1. object storage config
2. GPU deployment config
3. fixture tests
4. production smoke flow
5. release checklist

## 17. Recommended Use

Use this document as the primary design reference when creating the next layer of execution artifacts:

- checkpoint folders
- lane-specific task breakdowns
- schema migrations
- API implementation slices
- frontend implementation slices

If a checkpoint proposal contradicts this document, the checkpoint should be corrected before implementation starts.
