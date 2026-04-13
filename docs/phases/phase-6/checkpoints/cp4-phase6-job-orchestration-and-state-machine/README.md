# CP4 — Job Orchestration and State Machine

**Code:** `cp4-phase6-job-orchestration-and-state-machine`  
**Order:** 4  
**Depends On:** `cp3-phase6-scene-spec-builder`  
**Estimated Effort:** 2 days

## Objective

Replace the synchronous derive path with a tracked async task chain that persists progress, retry behavior, and failure state.

## Locked Slices

1. bundle create
2. job create
3. task chain
4. progress writes
5. retry policy
6. failure recording

## Interfaces and States Touched

- `presentation_3d_job`
- bundle `status`
- job `status`
- job `stage`
- retry eligibility
- legacy derive deprecation behavior

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| api | `../ai-architect-api/app/services/presentation_3d/orchestrator.py` | created | Bundle and task orchestration |
| api | `../ai-architect-api/app/services/presentation_3d/job_tracker.py` | created | DB-backed status progression |
| api | `../ai-architect-api/app/tasks/presentation_3d.py` | created | Async job chain |
| api | `../ai-architect-api/app/api/v1/derivation.py` | updated | Legacy handling or forwarding behavior |
| api | `../ai-architect-api/tests/test_presentation_3d_jobs.py` | created | State-machine and retry tests |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/result.json` | created | Implementation result |
| `artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/notes.md` | created | State machine notes |
| `artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/job-tests.log` | created | Async/state tests output |
| `artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/job-flow.log` | created | One recorded bundle/job flow example |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Async job chain exists and stage updates are persisted | ✓ |
| CHECK-02 | Bundle and job states move only through locked enum values | ✓ |
| CHECK-03 | Retryable failures do not corrupt previously written artifacts | ✓ |
| CHECK-04 | Legacy derive route is no longer the primary product path | ✓ |
