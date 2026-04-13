# CP2 Validation Checklist — API Contracts and Serializers

**For:** Validator  
**Read first:** `artifacts/phase6/cp2-phase6-api-contracts-and-serializers/result.json`  
**Goal:** Confirm the API contract is bundle-first and stable enough for downstream implementation.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp2-phase6-api-contracts-and-serializers/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP2 — API Contracts and Serializers",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: All locked endpoints are present in the new router

```bash
rg -n "presentation-3d/jobs|presentation-3d$|bundles/\\{bundle_id\\}|jobs/\\{job_id\\}|retry|approve|reject" \
  ../ai-architect-api/app/api/v1/presentation_3d.py
```

**Expected:** The new router exposes all locked endpoints.  
**Fail if:** One or more endpoints are missing or implemented on the legacy route only.

### CHECK-02: Bundle-first contract is implemented and frontend adapter exists

```bash
test -f ../ai-architect-web/src/lib/presentation-3d.ts && \
rg -n "bundle_id|qa_status|approval_status|delivery_status|scene_glb|walkthrough_video|manifest" \
  ../ai-architect-api/app/api/v1/presentation_3d.py \
  ../ai-architect-web/src/lib/presentation-3d.ts
```

**Expected:** New payload fields exist in both API and frontend adapter.  
**Fail if:** The frontend still depends on legacy `model_url` or `render_urls`.

### CHECK-03: API contract tests pass

```bash
test -f ../ai-architect-api/tests/test_presentation_3d_api.py && \
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_api.py -q
```

**Expected:** Contract tests are present and green.  
**Fail if:** The test file is missing or failing.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp2-phase6-api-contracts-and-serializers \
  --role validator \
  --status PASS \
  --summary "CP2 passed. Bundle-first API contracts are stable for downstream lanes." \
  --result-file artifacts/phase6/cp2-phase6-api-contracts-and-serializers/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp2-phase6-api-contracts-and-serializers/validation.json
```
