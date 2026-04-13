# CP4 Validation Checklist — Job Orchestration and State Machine

**For:** Validator  
**Read first:** `artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/result.json`  
**Goal:** Confirm async orchestration is explicit, traceable, and safe to build on.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp4-phase6-job-orchestration-and-state-machine/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP4 — Job Orchestration and State Machine",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Orchestration modules exist and mention all locked job stages

```bash
test -f ../ai-architect-api/app/services/presentation_3d/orchestrator.py && \
test -f ../ai-architect-api/app/services/presentation_3d/job_tracker.py && \
test -f ../ai-architect-api/app/tasks/presentation_3d.py && \
rg -n "scene_spec|runtime_dispatch|runtime_render|output_ingest|qa|manifest|approval_ready" \
  ../ai-architect-api/app/services/presentation_3d/orchestrator.py \
  ../ai-architect-api/app/services/presentation_3d/job_tracker.py \
  ../ai-architect-api/app/tasks/presentation_3d.py
```

**Expected:** All orchestration modules exist and use the locked stage vocabulary.  
**Fail if:** Stages are missing, renamed, or spread inconsistently.

### CHECK-02: State-machine tests pass

```bash
test -f ../ai-architect-api/tests/test_presentation_3d_jobs.py && \
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_jobs.py -q
```

**Expected:** Job/state tests are present and green.  
**Fail if:** The test file is missing or failing.

### CHECK-03: Legacy route no longer represents the only supported path

```bash
rg -n "deprecated|presentation-3d|forward|legacy" \
  ../ai-architect-api/app/api/v1/derivation.py \
  ../ai-architect-api/app/api/v1/presentation_3d.py
```

**Expected:** The new bundle-first path is authoritative and the old route is explicitly legacy.  
**Fail if:** `derive-3d` still appears to be the primary Phase 6 contract.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp4-phase6-job-orchestration-and-state-machine \
  --role validator \
  --status PASS \
  --summary "CP4 passed. Async orchestration and state transitions are ready for storage/runtime work." \
  --result-file artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp4-phase6-job-orchestration-and-state-machine/validation.json
```
