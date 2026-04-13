# Phase 6 Dev Readiness Checklist

## 1. Purpose

This checklist is the final gate before implementation begins.

The phase is ready for dev only when every section below has a clear owner and no unresolved blocking ambiguity.

## 2. Must-Read Docs

- `implementation/phase-6/00-README.md`
- `implementation/phase-6/01-3d-output-research-and-direction.md`
- `implementation/phase-6/02-3d-module-input-contracts.md`
- `implementation/phase-6/03-3d-presentation-architecture-and-hosting.md`
- `implementation/phase-6/05-phase-6-scope-lock.md`
- `implementation/phase-6/06-phase-6-implementation-detailed.md`
- `implementation/phase-6/07-phase-6-api-job-and-storage-contracts.md`
- `implementation/phase-6/08-phase-6-frontend-viewer-and-delivery-workflows.md`
- `implementation/phase-6/09-phase-6-checkpoint-execution-plan.md`
- `implementation/phase-6/10-phase-6-testing-release-and-acceptance-gates.md`

## 3. Ownership Checklist

### Backend

- owner assigned for bundle/job persistence
- owner assigned for API contract changes
- owner assigned for QA and manifest services

### Frontend

- owner assigned for generation progress UX
- owner assigned for viewer redesign
- owner assigned for delivery integration and approval actions

### GPU and Runtime

- owner assigned for render runtime image
- owner assigned for GLB export lane
- owner assigned for still/video generation

### DevOps

- owner assigned for object storage setup
- owner assigned for GPU host deployment
- owner assigned for secrets and environment config

### QA

- owner assigned for fixture coverage
- owner assigned for production truth validation

## 4. Technical Preconditions

- canonical version contract is stable enough for scene spec derivation
- object storage decision is made
- render runtime strategy is chosen
- queue/worker path is confirmed
- artifact naming and storage prefix contract is approved

## 5. Explicit Open Questions That Must Be Closed Before Coding

- Which rooms are mandatory defaults for the first still-render pack?
- What is the first required video duration target?
- Which render preset names are supported at launch?
- Which exact bundle states and status labels are exposed in the UI?
- Which typologies are launch-supported for Phase 6 generation?

If any of these remain open, they must be resolved in writing before implementation starts.

## 6. Lane Breakdown

### Lane 1: Backend contract and persistence

Target:

- bundle/job/asset/QA/approval persistence
- endpoints and progress contracts
- manifest and signed URL generation

### Lane 2: Scene spec and render execution

Target:

- scene spec builder
- GPU render runtime
- GLB, stills, and MP4 outputs

### Lane 3: Frontend consumption and approval UX

Target:

- progress state UX
- presentation viewer
- approval gate and delivery integration

### Lane 4: Validation and release

Target:

- QA rules
- degraded handling
- production acceptance flow

## 7. Blockers That Must Not Be Ignored

- treating legacy `model_url` as sufficient
- assuming local Docker volumes are acceptable final delivery storage
- assuming a live GPU service is the same as a render-capable GPU runtime
- treating preview assets as if they are released deliverables

## 8. Ready-for-Dev Statement

Phase 6 is ready for dev only when:

- scope is locked to Program A,
- all required contracts are documented,
- ownership is assigned,
- storage and runtime decisions are made,
- and the team agrees that Program B and Program C remain outside execution scope.
