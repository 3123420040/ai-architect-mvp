# CP2 Validation Checklist — Quantity and Issue Contracts

**For:** Validator
**Read first:** `artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/result.json`
**Goal:** Confirm Program B can generate schedule resources and store coordination issues before IFC packaging begins.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp2-program-b-quantity-and-issue-contracts/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP2 — Program B quantity and issue contracts",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Quantity and issue service files exist

```bash
test -f ../ai-architect-api/app/services/coordination/quantity_extractor.py && \
test -f ../ai-architect-api/app/services/coordination/issues.py && \
test -f ../ai-architect-api/app/services/coordination/schedule_serializer.py
```

**Expected:** Core schedule and issue files exist.
**Fail if:** Any required file is missing.

### CHECK-02: Confidence and verification states are explicit

```bash
rg -n "confidence|verification|system_derived|review_required|verified" \
  ../ai-architect-api/app/services/coordination/quantity_extractor.py \
  ../ai-architect-api/app/api/v1/coordination.py
```

**Expected:** Verification markers are modeled explicitly.
**Fail if:** Schedule outputs have no confidence semantics.

### CHECK-03: Issue linkage is version-aware and element-aware

```bash
rg -n "bundle|version|element|room|severity|status|resolve" \
  ../ai-architect-api/app/services/coordination/issues.py \
  ../ai-architect-api/app/api/v1/coordination.py
```

**Expected:** Issue lifecycle and linkage fields are present.
**Fail if:** Issues are too shallow for coordination workflows.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp2-program-b-quantity-and-issue-contracts \
  --role validator \
  --status PASS \
  --summary "CP2 passed. Program B schedule and issue contracts are validated." \
  --result-file artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/validation.json
```
