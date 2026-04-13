# Phase 6 Implementation Detailed

## 1. Product Contract

Phase 6 introduces six implementation contracts:

1. deterministic scene-spec generation from approved 2D truth,
2. async 3D job orchestration,
3. presentation bundle artifact model,
4. QA and degraded handling,
5. architect approval and client-delivery release,
6. presentation-grade viewer and delivery experience.

## 2. Entry Gate Contract

### 2.1 Required upstream state

The 3D lane may start only when:

- brief contract state is `locked`,
- selected version is approved and stable for derivation,
- package metadata exists for the source version,
- and required style/material directives are present.

### 2.2 Block conditions

Do not allow 3D bundle generation when:

- project is still clarifying,
- version is draft or under unresolved review,
- no target rooms or shot plan can be derived,
- or canonical geometry is missing required structural fields.

## 3. Scene Specification Contract

### 3.1 Role

`presentation_scene_spec` is the mandatory handoff object between product truth and render execution.

It must normalize:

- geometry references
- room semantics
- facade orientation
- material assignments
- shot list
- walkthrough path
- output targets

### 3.2 Required fields

At minimum the scene spec must contain:

- project and version identity
- scene revision label
- level list
- room list with room types
- opening references
- facade orientation metadata
- material rules by zone
- staging rules by room type
- still shot definitions
- walkthrough sequence
- output format and resolution targets

### 3.3 Determinism rule

Given the same approved version and the same render config, the scene spec must be stable enough to reproduce the same asset structure and named outputs.

## 4. Render Orchestration Contract

### 4.1 Async-first behavior

3D rendering must run as an async job, not as a synchronous request.

The API must:

- enqueue a render job,
- return a `job_id`,
- expose progress,
- and persist final job outcome.

### 4.2 Job stages

Minimum stages:

1. `queued`
2. `scene_spec_building`
3. `scene_assembling`
4. `glb_exporting`
5. `still_rendering`
6. `video_rendering`
7. `qa_validating`
8. `awaiting_approval`
9. `ready_for_delivery`
10. `failed`

### 4.3 Retry behavior

The system may retry failed render execution, but:

- retries must not silently overwrite approved assets,
- retry reason must be logged,
- and retry behavior must preserve version traceability.

## 5. Artifact Bundle Contract

### 5.1 Required artifact set

Every successful Phase 6 bundle must register:

- `scene.glb`
- still render set
- `walkthrough.mp4`
- `presentation_manifest.json`
- `qa_report.json`

### 5.2 Artifact identity

Each artifact must be tied to:

- project id
- version id
- 3D bundle id
- scene spec revision
- generation timestamp
- generator/runtime metadata

### 5.3 Storage rule

Final artifacts must live in object storage with stable paths and signed delivery URLs.

Local storage may be used for temporary scratch work only.

## 6. QA and Degraded Contract

### 6.1 QA scope

The QA validator must check:

- geometry completeness
- required room coverage
- required shot coverage
- GLB presence and readability
- MP4 presence and duration sanity
- manifest completeness
- asset naming and reference integrity

### 6.2 Output

QA must return:

- `pass`
- `warning`
- `fail`
- and a machine-readable reason list

### 6.3 Degraded rule

If the bundle is incomplete or materially weak:

- mark it `degraded`
- expose it only as internal preview
- block final client release

## 7. Approval and Delivery Contract

### 7.1 Approval gate

No 3D bundle becomes client-deliverable until:

- QA is acceptable,
- architect review is completed,
- approval note is recorded,
- and release state is switched explicitly.

### 7.2 Delivery manifest role

`presentation_manifest.json` must act as the release contract for downstream viewer and delivery behavior.

It must contain:

- bundle identity
- source version identity
- approved asset list
- approval state
- degraded state if any
- disclaimer and branding metadata
- immutable references to released assets

## 8. Viewer and Delivery Contract

### 8.1 Viewer role

The viewer must behave as a presentation workspace, not a debug tool.

It must support:

- hero preview
- still gallery
- video playback
- 3D model launch or embed
- approval/degraded status
- downloadable released assets where allowed

### 8.2 Status language

Required user-facing states:

- `Chưa tạo gói 3D`
- `Đang tạo gói 3D`
- `Bản xem trước`
- `Cần KTS duyệt`
- `Đã duyệt`
- `Bị chặn phát hành`

### 8.3 Release rule

If the bundle is only preview or degraded:

- viewer may allow internal inspection
- delivery surface must not present it as an official issued package

## 9. Runtime Responsibilities

### 9.1 App host responsibilities

The app host owns:

- source-of-truth reads
- scene-spec generation
- job orchestration
- QA
- manifest generation
- approval state
- signed URL issuance

### 9.2 GPU runtime responsibilities

The GPU runtime owns:

- scene assembly execution
- GLB export
- still rendering
- video rendering

It does not own:

- source-of-truth decisions
- approval logic
- delivery release policy

## 10. Explicit Out-of-Scope Engineering Work

The Phase 6 team must not spend implementation time on:

- IFC authoring upgrades
- native BIM editor integration
- BLEND/USD/FBX scene handoff
- premium CGI post-production tooling
- artist workflow management

Those belong outside this phase.

## 11. Quality Bar

Phase 6 is acceptable only if:

- placeholder 3D derivation behavior is replaced by bundle-oriented async flow,
- scene spec exists and is persisted,
- final artifact set includes GLB, stills, MP4, manifest, and QA report,
- viewer reads as client-ready presentation UX,
- degraded bundles are blocked from issue,
- and production validation proves the end-to-end path works on a real project.
