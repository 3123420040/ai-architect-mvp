# CP9 Validation Checklist — QA Validator and Degraded Policy

**For:** Validator  
**Read first:** `artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/result.json`  
**Goal:** Confirm QA and degraded-state handling are strong enough to protect release quality.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp9-phase6-qa-validator-and-degraded-policy/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP9 — QA Validator and Degraded Policy",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: QA service and tests exist

```bash
test -f ../ai-architect-api/app/services/presentation_3d/qa.py && \
test -f ../ai-architect-api/tests/test_presentation_3d_qa.py
```

**Expected:** QA service and test module exist.  
**Fail if:** Either file is missing.

### CHECK-02: QA logic explicitly references required artifact gates and degraded fields

```bash
rg -n "scene.glb|walkthrough|manifest|qa_status|is_degraded|degraded_reasons|delivery_status|warning|fail" \
  ../ai-architect-api/app/services/presentation_3d/qa.py \
  ../ai-architect-api/app/services/presentation_3d/orchestrator.py
```

**Expected:** Blocking artifact checks and degraded policy are explicit in code.  
**Fail if:** The code cannot clearly explain when a bundle becomes degraded or blocked.

### CHECK-03: QA tests pass

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_qa.py -q
```

**Expected:** QA and degraded tests are green.  
**Fail if:** The validator cannot prove blocked vs preview-only behavior.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp9-phase6-qa-validator-and-degraded-policy \
  --role validator \
  --status PASS \
  --summary "CP9 passed. QA and degraded handling now protect release quality." \
  --result-file artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/validation.json
```
