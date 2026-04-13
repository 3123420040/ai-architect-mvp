# Phase 6 API, Job, and Storage Contracts

## 1. Purpose

This document freezes the backend contract needed to implement Phase 6 without ambiguity across API, worker, GPU runtime, storage, and frontend consumption.

## 2. New Core Entities

### 2.1 `three_d_bundle`

Represents one generated presentation bundle for a specific version.

Required fields:

- `id`
- `project_id`
- `version_id`
- `scene_spec_revision`
- `status`
- `qa_status`
- `approval_status`
- `delivery_status`
- `is_degraded`
- `degraded_reasons`
- `created_at`
- `updated_at`

### 2.2 `three_d_job`

Represents an async generation job tied to a bundle.

Required fields:

- `id`
- `bundle_id`
- `job_type`
- `status`
- `stage`
- `progress_percent`
- `attempt_count`
- `error_code`
- `error_message`
- `started_at`
- `finished_at`

### 2.3 `three_d_asset`

Represents each generated artifact in the bundle.

Required fields:

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

### 2.4 `three_d_qa_report`

Represents rule-based validation results.

Required fields:

- `id`
- `bundle_id`
- `status`
- `summary`
- `checks_json`
- `blocking_reasons`
- `warnings`
- `generated_at`

### 2.5 `three_d_approval`

Represents architect review and release decision.

Required fields:

- `id`
- `bundle_id`
- `reviewed_by`
- `decision`
- `notes`
- `reviewed_at`

## 3. Required State Model

### 3.1 Bundle states

Required `three_d_bundle.status` values:

- `not_started`
- `queued`
- `building`
- `generated`
- `qa_failed`
- `awaiting_approval`
- `approved`
- `delivery_ready`
- `failed`

### 3.2 QA states

Required `qa_status` values:

- `pending`
- `pass`
- `warning`
- `fail`

### 3.3 Approval states

Required `approval_status` values:

- `not_requested`
- `pending`
- `approved`
- `rejected`

### 3.4 Delivery states

Required `delivery_status` values:

- `internal_preview`
- `blocked`
- `released`

## 4. API Surface

### 4.1 Create or restart a 3D bundle job

`POST /versions/{version_id}/presentation-3d/jobs`

Request:

```json
{
  "target_rooms": ["living_room", "kitchen", "master_bedroom"],
  "outputs": {
    "glb": true,
    "stills": true,
    "video": true
  },
  "presentation_mode": "client_presentation",
  "priority": "standard"
}
```

Response `202`:

```json
{
  "bundle_id": "uuid",
  "job_id": "uuid",
  "status": "queued",
  "stage": "queued",
  "progress_percent": 0
}
```

Blocking responses:

- `409` when source version is not eligible
- `422` when required upstream inputs are missing

### 4.2 Get the latest 3D bundle for a version

`GET /versions/{version_id}/presentation-3d`

Response `200`:

```json
{
  "bundle_id": "uuid",
  "status": "generated",
  "qa_status": "warning",
  "approval_status": "pending",
  "delivery_status": "internal_preview",
  "is_degraded": true,
  "degraded_reasons": ["video_missing"],
  "assets": {
    "scene_glb": {"url": "https://...", "checksum": "sha256:..."},
    "stills": [
      {"shot_id": "hero-exterior-day", "url": "https://..."},
      {"shot_id": "living-room-main", "url": "https://..."}
    ],
    "walkthrough_video": {"url": "https://...", "duration_seconds": 62},
    "manifest": {"url": "https://..."},
    "qa_report": {"url": "https://..."}
  },
  "scene_spec_revision": "v1",
  "updated_at": "2026-04-13T15:00:00Z"
}
```

### 4.3 Get job detail

`GET /presentation-3d/jobs/{job_id}`

Response `200`:

```json
{
  "job_id": "uuid",
  "bundle_id": "uuid",
  "status": "running",
  "stage": "video_rendering",
  "progress_percent": 78,
  "attempt_count": 1,
  "error_code": null,
  "error_message": null
}
```

### 4.4 Retry a failed job

`POST /presentation-3d/jobs/{job_id}/retry`

Allowed only when:

- job is `failed`
- bundle is not already approved and released

### 4.5 Approve bundle

`POST /presentation-3d/bundles/{bundle_id}/approve`

Request:

```json
{
  "decision": "approved",
  "notes": "Render pack and walkthrough match the approved version."
}
```

Required behavior:

- reject approval if QA is `fail`
- switch bundle to `approved`
- set `delivery_status` to `released` only if all required assets exist

### 4.6 Reject bundle

`POST /presentation-3d/bundles/{bundle_id}/reject`

Required behavior:

- preserve assets
- keep delivery blocked
- record review notes

## 5. Worker and GPU Activity Contract

### 5.1 App worker stages

The app worker must own:

- eligibility validation
- scene spec persistence
- job dispatch
- asset registration
- QA execution
- manifest generation
- approval gate transitions

### 5.2 GPU runtime request

The GPU runtime should receive:

- `bundle_id`
- `scene_spec_url` or scene spec payload reference
- requested outputs
- render preset
- output target metadata

The GPU runtime should return:

- structured artifact metadata
- stage completion signals
- error payload on failure

## 6. Event and Progress Contract

The system must expose progress updates for the frontend.

Minimum event payload:

```json
{
  "job_id": "uuid",
  "bundle_id": "uuid",
  "status": "running",
  "stage": "still_rendering",
  "progress_percent": 56,
  "message": "Dang render bo hinh khong gian chinh"
}
```

Minimum completion payload:

```json
{
  "job_id": "uuid",
  "bundle_id": "uuid",
  "status": "completed",
  "qa_status": "warning",
  "approval_status": "pending",
  "delivery_status": "internal_preview"
}
```

## 7. Storage Contract

### 7.1 Storage prefixes

Use stable object-storage prefixes:

- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/scene/scene.glb`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/renders/{shot_id}.png`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/video/walkthrough.mp4`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/manifest/presentation_manifest.json`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/qa/qa_report.json`
- `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/scene/scene_spec.json`

### 7.2 Storage metadata

Every stored asset must preserve:

- immutable storage key
- checksum
- byte size
- media metadata when applicable
- source bundle id

### 7.3 Delivery URLs

Frontend should consume signed URLs or CDN URLs generated by the API. It should not build local file paths itself.

## 8. Manifest Contract

`presentation_manifest.json` must include:

- manifest version
- bundle id
- project id
- version id
- source package revision
- approval state
- degraded state
- required asset registry
- disclaimer policy
- branding policy
- generation metadata
- QA summary

## 9. Backward Compatibility Rules

During rollout:

- legacy `model_url` and `render_urls` may coexist temporarily
- new UI must prefer bundle-based contracts
- final release cannot rely on legacy-only shape

## 10. Explicit Implementation Requirement

No backend slice is complete until:

- persistence exists for bundle/job/asset/QA/approval
- API responses match the new bundle-oriented contract
- storage keys are stable
- and frontend can consume the new contract without reading raw debug payloads
