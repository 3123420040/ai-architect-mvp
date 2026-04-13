# CP1 Validation Checklist — Persistence and Migrations

**For:** Validator  
**Read first:** `artifacts/phase6/cp1-phase6-persistence-and-migrations/result.json`  
**Goal:** Confirm the persistence backbone is additive, exact, and safe.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp1-phase6-persistence-and-migrations/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP1 — Persistence and Migrations",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Migration and models reference all four Phase 6 entities

```bash
rg -n "presentation_3d_bundles|presentation_3d_jobs|presentation_3d_assets|presentation_3d_approvals|current_presentation_3d_bundle_id" \
  ../ai-architect-api/alembic/versions \
  ../ai-architect-api/app/models.py
```

**Expected:** All bundle/job/asset/approval entities are present.  
**Fail if:** Any entity or the `DesignVersion` linkage is missing.

### CHECK-02: Enum values match the locked Phase 6 contract exactly

```bash
rg -n "queued|running|awaiting_approval|released|failed|pending|pass|warning|fail|not_requested|approved|rejected|preview_only|blocked|succeeded|scene_spec|runtime_dispatch|runtime_render|output_ingest|qa|manifest|approval_ready" \
  ../ai-architect-api/app/models.py \
  ../ai-architect-api/app/schemas.py
```

**Expected:** Locked enums appear exactly once in canonical model/schema definitions.  
**Fail if:** Enums drift, are renamed, or are split inconsistently.

### CHECK-03: Persistence test file exists and passes

```bash
test -f ../ai-architect-api/tests/test_presentation_3d_persistence.py && \
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_persistence.py -q
```

**Expected:** Persistence tests are present and green.  
**Fail if:** The test file is missing or failing.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp1-phase6-persistence-and-migrations \
  --role validator \
  --status PASS \
  --summary "CP1 passed. Phase 6 persistence model is stable and migration-safe." \
  --result-file artifacts/phase6/cp1-phase6-persistence-and-migrations/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp1-phase6-persistence-and-migrations/validation.json
```
