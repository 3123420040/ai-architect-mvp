# CP4 — Job Orchestration and State Machine

**Objective:** Move Phase 6 from sync derive to observable async execution.  
**Requires:** `cp3-phase6-scene-spec-builder` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp4-phase6-job-orchestration-and-state-machine/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP4 — Job Orchestration and State Machine",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement orchestration services

Create:

- `../ai-architect-api/app/services/presentation_3d/orchestrator.py`
- `../ai-architect-api/app/services/presentation_3d/job_tracker.py`
- `../ai-architect-api/app/tasks/presentation_3d.py`

The task chain must be able to progress through:

- `scene_spec`
- `runtime_dispatch`
- `runtime_render`
- `output_ingest`
- `qa`
- `manifest`
- `approval_ready`

## Step 2 — Persist state and retry behavior

Persist:

- bundle `status`
- job `status`
- job `stage`
- `progress_percent`
- `attempt_count`
- error code and message

Define retry rules that preserve traceability and do not silently overwrite approved/released assets.

## Step 3 — Update legacy derive behavior

Update `../ai-architect-api/app/api/v1/derivation.py` so the old route is no longer the primary path. It may:

- forward internally to the new orchestration path, or
- return a clear deprecation contract

but it must not remain the main product contract.

## Step 4 — Add state-machine tests

Create:

- `../ai-architect-api/tests/test_presentation_3d_jobs.py`

Cover:

- job creation
- stage transitions
- failure path
- retry path
- prohibited transitions

## Step 5 — Run required commands

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_jobs.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/job-tests.log
```

Record one representative job lifecycle in:

- `artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/job-flow.log`

## Step 6 — Record completion and notify

Create:

- `artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/result.json`
- `artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp4-phase6-job-orchestration-and-state-machine \
  --role implementer \
  --status READY \
  --summary "CP4 complete. Phase 6 async orchestration and state machine are ready." \
  --result-file artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/result.json
```
