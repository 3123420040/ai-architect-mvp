# Program B Technical Design Detailed

## 1. Purpose

This document translates the locked Program B Release 1 scope into an implementation-facing technical design.

It assumes Program B Release 1 is locked to:

**Coordination-ready architectural handoff**

## 2. As-Is Technical Reality

The current product already has:

- canonical design versioning,
- package export baseline,
- DXF and IFC attachment paths,
- delivery workspace infrastructure,
- and review or approval patterns.

The current product does **not** yet have:

- a first-class semantic coordination model,
- stable semantic element identity for handoff workflows,
- schedule snapshots with verification state,
- first-class coordination issue records,
- or a dedicated handoff bundle architecture for Program B.

## 3. Target Technical Outcome

Program B Release 1 target flow:

`approved version -> semantic coordination model -> quantity snapshots -> coordination IFC -> handoff bundle -> QA/review -> release`

The system must truthfully produce:

- `coordination_model.json`
- `architectural_coordination.ifc`
- required schedule files
- `issue_register.json`
- `coordination_manifest.json`
- `readiness_summary.json`

## 4. System Decomposition

Program B Release 1 should be implemented as seven cooperating subsystems.

### 4.1 Eligibility and Trigger Layer

Owned by API.

Responsibilities:

- verify source version eligibility
- verify typology support
- create handoff bundle and job records
- enqueue execution

Primary modules:

- `app/api/v1/coordination.py`
- `app/services/coordination/eligibility.py`
- `app/services/coordination/orchestrator.py`

### 4.2 Semantic Coordination Model Builder

Owned by app-side service and worker.

Responsibilities:

- normalize approved geometry into architectural semantics
- assign persistent semantic ids
- create queryable relationships
- persist `coordination_model.json`

Primary modules:

- `app/services/coordination/semantic_model_builder.py`
- `app/services/coordination/semantic_ids.py`
- `app/services/coordination/relationships.py`

### 4.3 Quantity and Schedule Extraction Layer

Owned by app-side worker.

Responsibilities:

- derive schedule snapshots
- assign confidence and verification flags
- persist schedule artifacts and structured rows

Primary modules:

- `app/services/coordination/quantity_extractor.py`
- `app/services/coordination/schedule_serializer.py`

### 4.4 Coordination Issue Layer

Owned by API and web app.

Responsibilities:

- store issue records
- link issues to bundle, version, room, and element ids
- expose issue lifecycle APIs

Primary modules:

- `app/services/coordination/issues.py`
- `app/api/v1/coordination.py`

### 4.5 IFC Export Layer

Owned by worker-side export service.

Responsibilities:

- map semantic model to coordination-grade architectural IFC
- attach selected property sets
- persist validation metadata

Primary modules:

- `app/services/coordination/ifc_exporter.py`
- `app/services/coordination/ifc_validation.py`

### 4.6 Manifest and Readiness Layer

Owned by API or worker.

Responsibilities:

- compose released handoff package
- generate `coordination_manifest.json`
- generate `readiness_summary.json`
- enforce release rules

Primary modules:

- `app/services/coordination/manifest.py`
- `app/services/coordination/readiness.py`

### 4.7 Delivery Workspace Consumption Layer

Owned by web app.

Responsibilities:

- show readiness state
- show schedules and issues
- expose download actions
- expose release controls

Primary modules:

- `src/components/delivery-client.tsx`
- `src/components/coordination-handoff.tsx`
- `src/lib/coordination.ts`

## 5. Data Model Design

## 5.1 Design Principle

Do not overload `design_versions` to carry Program B runtime state directly.

`DesignVersion` remains the source design object.

Program B introduces dedicated persistence for:

- semantic coordination model,
- schedules,
- issues,
- handoff bundle,
- and job lifecycle.

## 5.2 Proposed New Tables

### A. `coordination_model_versions`

Purpose:

- one semantic coordination model per source version and bundle generation

Suggested columns:

- `id`
- `project_id`
- `version_id`
- `typology`
- `status`
- `schema_version`
- `verification_status`
- `model_url`
- `created_by`
- `created_at`
- `updated_at`

### B. `coordination_elements`

Purpose:

- store normalized semantic elements

Suggested columns:

- `id`
- `coordination_model_id`
- `stable_key`
- `element_type`
- `parent_element_id`
- `level_key`
- `source_geometry_ref`
- `classification_code`
- `properties_json`
- `verification_status`
- `created_at`
- `updated_at`

### C. `coordination_element_relationships`

Purpose:

- store semantic relationships between elements

Suggested columns:

- `id`
- `coordination_model_id`
- `from_element_id`
- `relationship_type`
- `to_element_id`
- `metadata_json`

### D. `coordination_quantity_snapshots`

Purpose:

- persist schedule extraction runs

Suggested columns:

- `id`
- `coordination_model_id`
- `version_id`
- `snapshot_type`
- `status`
- `summary_json`
- `generated_at`

### E. `coordination_quantity_items`

Purpose:

- persist schedule rows

Suggested columns:

- `id`
- `snapshot_id`
- `item_type`
- `item_key`
- `label`
- `unit`
- `value_numeric`
- `source_element_ids`
- `confidence_status`
- `review_note`

### F. `coordination_issues`

Purpose:

- first-class issue registry

Suggested columns:

- `id`
- `project_id`
- `version_id`
- `bundle_id`
- `issue_code`
- `issue_type`
- `severity`
- `status`
- `source_discipline`
- `assigned_to`
- `title`
- `description`
- `linked_element_ids`
- `linked_room_ids`
- `linked_sheet_ids`
- `viewpoint_asset_id`
- `resolution_note`
- `created_by`
- `created_at`
- `updated_at`
- `resolved_at`

### G. `coordination_handoff_bundles`

Purpose:

- one row per generated handoff bundle

Suggested columns:

- `id`
- `project_id`
- `version_id`
- `coordination_model_id`
- `status`
- `qa_status`
- `delivery_status`
- `manifest_url`
- `readiness_summary_url`
- `created_by`
- `released_by`
- `released_at`
- `created_at`
- `updated_at`

### H. `coordination_bundle_assets`

Purpose:

- register released artifacts

Suggested columns:

- `id`
- `bundle_id`
- `asset_type`
- `storage_key`
- `file_name`
- `mime_type`
- `checksum`
- `metadata_json`
- `created_at`

### I. `coordination_jobs`

Purpose:

- track async generation lifecycle

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
- `created_at`
- `updated_at`

## 6. Public API Design

### 6.1 Core endpoints

- `POST /versions/{version_id}/coordination-handoff/jobs`
- `GET /versions/{version_id}/coordination-handoff`
- `GET /coordination-handoff/bundles/{bundle_id}`
- `GET /coordination-handoff/jobs/{job_id}`
- `GET /coordination-handoff/bundles/{bundle_id}/schedules`
- `GET /coordination-handoff/bundles/{bundle_id}/issues`
- `POST /coordination-handoff/bundles/{bundle_id}/issues`
- `POST /coordination-issues/{issue_id}/resolve`
- `POST /coordination-handoff/bundles/{bundle_id}/release`

### 6.2 Minimum response resources

- `coordination_model`
- `coordination_schedule_snapshot`
- `coordination_issue`
- `coordination_handoff_bundle`
- `coordination_job`

## 7. State Model

### 7.1 Coordination model status

- `pending`
- `built`
- `verified`
- `failed`

### 7.2 Quantity confidence state

- `system_derived`
- `review_required`
- `verified`

### 7.3 Issue state

- `open`
- `in_review`
- `resolved`
- `waived`

### 7.4 Bundle status

- `queued`
- `running`
- `awaiting_review`
- `ready_for_release`
- `released`
- `failed`

### 7.5 Delivery status

- `internal_only`
- `consultant_review`
- `released`
- `blocked`

## 8. Async Job Stages

Minimum stages:

1. `eligibility_check`
2. `semantic_model_build`
3. `quantity_extract`
4. `ifc_export`
5. `bundle_package`
6. `qa_validate`
7. `awaiting_review`
8. `released`
9. `failed`

## 9. Storage Convention

- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/model/coordination_model.json`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/ifc/architectural_coordination.ifc`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/schedules/room_schedule.csv`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/schedules/door_window_schedule.csv`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/schedules/area_schedule.csv`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/issues/issue_register.json`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/manifest/coordination_manifest.json`
- `projects/{project_id}/versions/{version_id}/coordination/{bundle_id}/reports/readiness_summary.json`

## 10. Frontend State Contract

Required user-facing states:

- `Chưa tạo gói coordination`
- `Đang chuẩn bị gói coordination`
- `Cần KTS rà soát`
- `Sẵn sàng phát hành`
- `Đã phát hành`
- `Bị chặn`

## 11. Runtime Responsibility Split

### App host owns

- source truth reads
- semantic model generation
- schedule extraction
- issue persistence
- manifest generation
- release policy
- signed URL issuance

### Worker owns

- async orchestration
- IFC export
- artifact packaging
- QA execution

## 12. Explicit Technical Exclusions

Program B Release 1 must not spend implementation time on:

- Revit plugin development
- APS automation integration
- Speckle-first canonical storage
- multi-discipline clash engine
- browser-native BIM editing
