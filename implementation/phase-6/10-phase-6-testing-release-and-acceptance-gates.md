# Phase 6 Testing, Release, and Acceptance Gates

## 1. Purpose

This document defines the required verification stack for Phase 6 so the team does not mistake partial artifact generation for a successful release.

## 2. Test Layers

### 2.1 Unit tests

Must cover:

- scene spec validation
- bundle state transitions
- QA rule evaluation
- approval gate rules
- manifest assembly

### 2.2 Integration tests

Must cover:

- create bundle job
- progress state progression
- asset registration
- storage URL generation
- delivery-state transitions

### 2.3 Fixture and golden tests

Must cover:

- representative typology fixtures
- expected scene spec shape
- expected manifest shape
- expected QA rule outcomes

### 2.4 Frontend tests

Must cover:

- viewer status states
- progress UI
- degraded badge display
- approval action availability
- delivery workspace bundle visibility

## 3. Non-Negotiable Acceptance Checks

Phase 6 cannot be accepted unless all of the following are true for at least one real production-like case.

### Check 1: Source gating works

- bundle generation is blocked for ineligible source versions

### Check 2: Async generation works

- bundle job is queued and progresses through expected stages

### Check 3: Output set is complete

- `scene.glb` exists
- still pack exists
- `walkthrough.mp4` exists
- `presentation_manifest.json` exists
- `qa_report.json` exists

### Check 4: QA gate works

- a failing or incomplete bundle is marked degraded or failed
- client release is blocked

### Check 5: Approval gate works

- architect approval is required before release

### Check 6: Viewer reflects truth

- viewer shows bundle state correctly
- viewer does not present degraded preview as issued output

### Check 7: Delivery integration works

- released bundle is visible from delivery workspace with correct state

## 4. Release Gates

### Gate A: Pre-merge

Required:

- tests pass locally or in CI
- schema migrations reviewed
- no unresolved P0 contract gaps

### Gate B: Pre-deploy

Required:

- render runtime available
- object storage configured
- signed URL path verified
- environment variables set

### Gate C: Post-deploy smoke

Required:

- API health passes
- new bundle endpoints respond
- queue and worker path operate
- GPU runtime is reachable

### Gate D: End-to-end production truth

Required:

- one real generation flow from approved version to released 3D bundle succeeds
- screenshots or artifacts are recorded
- QA and approval history are auditable

## 5. Failure Conditions

Phase 6 must be treated as failed if any of these remain in the live path:

- sync placeholder derive remains the main 3D flow
- final bundle lacks walkthrough MP4
- final bundle lacks manifest
- approval gate is bypassable
- degraded preview can be issued as released client output
- viewer still behaves like a debug JSON page

## 6. Final Acceptance Statement

Phase 6 is accepted only when the product can truthfully say:

`From an approved design version, the system can generate a presentation-grade 3D bundle with GLB, still renders, walkthrough video, manifest, QA result, and architect-gated release.`
