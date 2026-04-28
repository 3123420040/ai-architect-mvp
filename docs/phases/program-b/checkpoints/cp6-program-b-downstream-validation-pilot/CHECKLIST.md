# CP6 Validation Checklist — Downstream Validation Pilot

**For:** Validator
**Read first:** `artifacts/program-b/cp6-program-b-downstream-validation-pilot/result.json`
**Goal:** Confirm Program B launch evidence is grounded in benchmark and downstream continuation feedback.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp6-program-b-downstream-validation-pilot/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP6 — Program B downstream validation pilot",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Pilot evidence artifacts exist

```bash
test -f artifacts/program-b/cp6-program-b-downstream-validation-pilot/benchmark-matrix.md && \
test -f artifacts/program-b/cp6-program-b-downstream-validation-pilot/pilot-feedback.md && \
test -f artifacts/program-b/cp6-program-b-downstream-validation-pilot/blocker-list.json
```

**Expected:** All evidence artifacts are present.
**Fail if:** Any evidence file is missing.

### CHECK-02: Benchmark evidence covers both launch typologies

```bash
rg -n "townhouse|villa" artifacts/program-b/cp6-program-b-downstream-validation-pilot/benchmark-matrix.md
```

**Expected:** Both launch typologies are covered explicitly.
**Fail if:** Either benchmark typology is missing.

### CHECK-03: Pilot feedback includes practical continuation judgment

```bash
rg -n "continuation|ambiguity|schedule|IFC|issue|re-model|usable|not usable" \
  artifacts/program-b/cp6-program-b-downstream-validation-pilot/pilot-feedback.md
```

**Expected:** Feedback captures practical continuation value or lack of it.
**Fail if:** Feedback is generic or purely optimistic.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp6-program-b-downstream-validation-pilot \
  --role validator \
  --status PASS \
  --summary "CP6 passed. Program B downstream validation evidence is grounded and reviewable." \
  --result-file artifacts/program-b/cp6-program-b-downstream-validation-pilot/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp6-program-b-downstream-validation-pilot/validation.json
```
