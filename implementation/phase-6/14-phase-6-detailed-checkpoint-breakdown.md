# Phase 6 Detailed Checkpoint Breakdown

## 1. Purpose

This document breaks the Phase 6 technical design into execution checkpoints detailed enough for the development team to implement and test without reopening the architecture.

This is a planning artifact only.

It does **not** execute development or testing.

It assumes the team will implement only:

**Program A: Presentation-grade 3D**

## 2. Source Documents

This breakdown is derived from:

- [05-phase-6-scope-lock.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/05-phase-6-scope-lock.md:1)
- [06-phase-6-implementation-detailed.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/06-phase-6-implementation-detailed.md:1)
- [07-phase-6-api-job-and-storage-contracts.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/07-phase-6-api-job-and-storage-contracts.md:1)
- [08-phase-6-frontend-viewer-and-delivery-workflows.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/08-phase-6-frontend-viewer-and-delivery-workflows.md:1)
- [09-phase-6-checkpoint-execution-plan.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/09-phase-6-checkpoint-execution-plan.md:1)
- [10-phase-6-testing-release-and-acceptance-gates.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/10-phase-6-testing-release-and-acceptance-gates.md:1)
- [13-phase-6-technical-design-detailed.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/13-phase-6-technical-design-detailed.md:1)

## 3. Execution Principles

Every Phase 6 checkpoint must obey these rules:

1. do not mix Program B or Program C requirements into implementation
2. keep bundle-oriented APIs as the target contract
3. keep rendering async
4. keep release blocked until QA and architect approval pass
5. keep final artifacts in object storage, not only local volume paths

## 4. Team Lane Model

The checkpoints below assume four engineering lanes.

### Lane A — Backend Contract and Persistence

Owns:

- DB migration
- ORM models
- API schemas
- API routes
- bundle/job/asset/approval persistence

### Lane B — Scene Spec and Runtime Orchestration

Owns:

- eligibility validation
- scene spec generation
- Celery or worker orchestration
- storage handoff
- runtime dispatch and retries

### Lane C — GPU Render Runtime

Owns:

- render service contract
- Blender or render runtime integration
- GLB export
- still renders
- walkthrough MP4 generation

### Lane D — Frontend, QA, and Delivery UX

Owns:

- progress UI
- presentation viewer
- delivery integration
- approval panel
- QA visibility and degraded handling

## 5. Checkpoint Overview

| Order | Code | Checkpoint | Main target |
|---|---|---|---|
| 0 | `cp0-phase6-scope-contract-freeze` | Scope and Contract Freeze | Freeze implementation boundaries and unresolved choices |
| 1 | `cp1-phase6-bundle-persistence-api` | Bundle Persistence and API Backbone | Add persistence and bundle-first API contract |
| 2 | `cp2-phase6-scene-spec-builder` | Scene Spec Builder | Generate deterministic `presentation_scene_spec` |
| 3 | `cp3-phase6-async-job-orchestration` | Async Job Orchestration | Replace sync derive path with tracked async jobs |
| 4 | `cp4-phase6-storage-runtime-adapter` | Storage and Runtime Adapter | Wire object storage and runtime handoff |
| 5 | `cp5-phase6-glb-and-still-render-lane` | GLB and Still Render Lane | Generate non-placeholder GLB and required stills |
| 6 | `cp6-phase6-video-qa-and-degraded` | Video, QA, and Degraded Policy | Generate MP4, run QA, assign degraded state |
| 7 | `cp7-phase6-approval-manifest-delivery` | Approval, Manifest, and Delivery | Release control and manifest contract |
| 8 | `cp8-phase6-viewer-production-validation` | Viewer and Production Validation | Final UX integration and production truth validation |

## 6. Detailed Checkpoints

## CP0 — Scope and Contract Freeze

### Goal

Freeze all decisions that would otherwise cause rework during implementation.

### Dependencies

- existing Phase 6 docs completed

### Required closure items

- confirm launch typologies for Phase 6
- confirm required still shot set
- confirm first video duration target
- confirm initial render preset names
- confirm object storage target
- confirm dedicated GPU runtime path

### Lane tasks

Lane A:

- review bundle/job/entity design
- flag any migration conflicts with current schema

Lane B:

- review scene spec minimum fields
- review orchestration assumptions

Lane C:

- review runtime contract feasibility
- confirm first implementation path for GLB/stills/video

Lane D:

- review viewer states and approval UX labels

### Test focus

- no runtime test
- document review only

### DoD

- no open P0 ambiguity remains
- all CP1-CP8 assumptions can proceed without waiting on product clarification

## CP1 — Bundle Persistence and API Backbone

### Goal

Introduce first-class 3D bundle persistence and the new API contract.

### Dependencies

- CP0 pass

### Lane tasks

Lane A:

- create Alembic migration for:
  - `presentation_3d_bundles`
  - `presentation_3d_jobs`
  - `presentation_3d_assets`
  - `presentation_3d_approvals`
- update ORM models
- add Pydantic schemas for bundle/job/asset/approval
- create new router `app/api/v1/presentation_3d.py`
- add endpoints:
  - create job
  - get latest bundle
  - get bundle detail
  - get job detail

Lane B:

- add service skeletons:
  - `eligibility.py`
  - `orchestrator.py`
  - `job_tracker.py`

Lane D:

- add typed client fetch layer for new endpoints

### Test focus

- migration applies cleanly
- API schema serialization
- eligibility blocking for invalid source version

### DoD

- new tables exist
- API returns bundle-first shape
- legacy derive route is no longer the only supported contract

## CP2 — Scene Spec Builder

### Goal

Produce deterministic `presentation_scene_spec` from an approved version.

### Dependencies

- CP1 pass

### Lane tasks

Lane B:

- implement `scene_spec_builder.py`
- implement `material_mapping.py`
- implement `shot_planner.py`
- persist `scene_spec.json`
- validate minimum geometry completeness

Lane A:

- add scene spec metadata fields to bundle rows if needed
- expose scene spec reference in bundle detail endpoint

Lane C:

- review scene spec contract and confirm runtime readability

### Test focus

- fixture-based tests for scene spec generation
- deterministic output shape for same source input
- missing geometry validation failures

### DoD

- scene spec exists as durable artifact or persisted JSON reference
- runtime can consume the scene spec without custom one-off logic

## CP3 — Async Job Orchestration

### Goal

Move the 3D lane from synchronous derivation to tracked async execution.

### Dependencies

- CP2 pass

### Lane tasks

Lane B:

- create worker task chain:
  - build scene spec
  - dispatch runtime
  - ingest outputs
  - run QA
  - build manifest
  - set approval-ready state
- persist stage and progress updates
- implement retry rules

Lane A:

- wire API endpoint to create jobs
- wire job status retrieval
- persist stage/progress fields

Lane D:

- connect progress polling or status refresh

### Test focus

- enqueue path works
- stage transitions are persisted
- failed job records remain inspectable

### DoD

- API no longer blocks on full render execution
- users can observe real job state

## CP4 — Storage and Runtime Adapter

### Goal

Introduce the durable artifact path and the runtime adapter layer before real rendering is finalized.

### Dependencies

- CP3 pass

### Lane tasks

Lane A:

- extend storage adapter for Phase 6 prefixes
- add signed URL generation for 3D assets
- register checksums and media metadata

Lane B:

- implement runtime dispatch client
- define payload contract to GPU runtime

Lane C:

- implement Phase 6 runtime endpoint shape
- return structured artifact metadata, not ad hoc fields

Lane D:

- consume signed/public asset URLs from bundle payload

### Test focus

- storage key generation
- artifact registration integrity
- runtime call success and failure parsing

### DoD

- bundle artifacts can be stored outside local-only paths
- runtime adapter is stable enough for GLB/still/video work

## CP5 — GLB and Still Render Lane

### Goal

Deliver the first real presentation artifact set: `scene.glb` and required still renders.

### Dependencies

- CP4 pass

### Lane tasks

Lane C:

- implement scene assembly in runtime
- export `scene.glb`
- render mandatory still pack
- emit artifact metadata for each still

Lane B:

- ingest returned assets into bundle registry
- set correct bundle/job states

Lane A:

- expose stills and GLB in bundle detail payload

Lane D:

- show hero still and still gallery from bundle API

### Test focus

- GLB artifact exists and is non-empty
- required shot IDs are present
- storage references are valid

### DoD

- one approved source version can generate a stable GLB and still pack
- placeholder-only SVG path is no longer the accepted result

## CP6 — Video, QA, and Degraded Policy

### Goal

Add walkthrough MP4 generation, QA validation, and degraded handling.

### Dependencies

- CP5 pass

### Lane tasks

Lane C:

- implement walkthrough video generation
- encode MP4
- emit duration metadata

Lane B:

- implement `qa.py`
- run QA after artifacts land
- classify `pass`, `warning`, `fail`
- assign degraded state when blocking checks fail

Lane A:

- persist QA result and degraded reasons
- expose QA result through bundle API

Lane D:

- show degraded badge and top blocking reason
- show preview-only state when QA fails

### Test focus

- MP4 exists and is readable
- QA report shape is valid
- degraded bundles are blocked from release

### DoD

- bundle output set now includes video and QA result
- internal preview remains possible even when release is blocked

## CP7 — Approval, Manifest, and Delivery

### Goal

Complete the release-control layer so a 3D bundle can become an official deliverable.

### Dependencies

- CP6 pass

### Lane tasks

Lane A:

- implement manifest generator
- implement approval and rejection endpoints
- persist approval notes
- enforce release rules

Lane B:

- finalize bundle state transitions:
  - `generated`
  - `qa_failed`
  - `awaiting_approval`
  - `approved`
  - `delivery_ready`

Lane D:

- add approval panel in viewer or review surface
- expose release state in delivery workspace
- add manifest/download actions where allowed

### Test focus

- approval blocked when QA fails
- release allowed only after approval
- manifest references released assets correctly

### DoD

- bundle can be approved or rejected explicitly
- released state is distinguishable from internal preview

## CP8 — Viewer and Production Validation

### Goal

Replace the old debug viewer with the client-ready presentation viewer and validate the full live path.

### Dependencies

- CP7 pass

### Lane tasks

Lane D:

- replace raw JSON viewer behavior
- implement:
  - status card
  - hero visual
  - still gallery
  - video player
  - GLB action
  - approval state
  - degraded state

Lane A:

- ensure bundle payload supports all viewer needs

Lane B:

- support final observability and error visibility

Lane C:

- confirm runtime stability in live environment

### Test focus

- frontend component tests for states
- one real production-like bundle flow
- released bundle visible in delivery workspace

### DoD

- viewer reads as presentation workspace, not debug tool
- one end-to-end production truth case passes:
  - source version eligible
  - bundle generated
  - QA run
  - approval recorded
  - release state visible

## 7. Testing Breakdown by Checkpoint

| Checkpoint | Required tests |
|---|---|
| CP0 | document review only |
| CP1 | migration test, API schema test, eligibility blocking test |
| CP2 | scene spec fixture tests, deterministic output tests |
| CP3 | async job state tests, retry and failure-path tests |
| CP4 | storage adapter tests, runtime adapter integration tests |
| CP5 | GLB existence test, still shot completeness test |
| CP6 | MP4 generation test, QA rules test, degraded-policy test |
| CP7 | approval/rejection tests, manifest integrity test, release gating test |
| CP8 | frontend state tests, production smoke flow, viewer acceptance screenshots |

## 8. Recommended Parallelization

Parallelize only where contracts are already stable.

### Safe early parallel work

After CP1:

- Lane A can continue API/schema work
- Lane B can start scene spec builder
- Lane D can scaffold bundle-based frontend adapter

After CP4:

- Lane C can work on render runtime
- Lane D can work on viewer shell and status UX
- Lane B can work on QA scaffolding

### Unsafe parallel work

Do not fully parallelize before these are frozen:

- bundle schema
- scene spec schema
- runtime artifact metadata contract

## 9. Handoff Rules Between Checkpoints

Each checkpoint should hand off:

- code changes or docs
- explicit test evidence
- unresolved issues list
- contract deltas if any

No checkpoint should be marked complete if the next checkpoint would still need to guess:

- field names
- state transitions
- artifact paths
- approval semantics

## 10. Recommended Next Artifact

The next artifact after this file should be one of:

1. checkpoint folders under `docs/phases/phase-6/checkpoints/`
2. a lane-by-lane technical task breakdown:
   - backend and persistence
   - scene spec and orchestration
   - GPU render runtime
   - frontend and delivery

This document is the correct source to generate either of those.
