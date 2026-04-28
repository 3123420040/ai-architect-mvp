# CP7 Validation Checklist — Release Readiness and Launch Gate

**For:** Validator
**Read first:** `artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/result.json`
**Goal:** Confirm Program B launch readiness is evidence-based and does not overclaim capability.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7-program-b-release-readiness-and-launch-gate/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP7 — Program B release readiness and launch gate",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Launch readiness artifacts exist

```bash
test -f artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/launch-readiness.json && \
test -f artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/closeout.md
```

**Expected:** Final launch artifacts are present.
**Fail if:** Any required artifact is missing.

### CHECK-02: Launch thresholds are explicit and reviewable

```bash
rg -n "PASS|FAIL|PASS_WITH_LIMITATION|semantic|schedule|IFC|issue|readiness" \
  artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/launch-readiness.json
```

**Expected:** Threshold outcomes are explicit.
**Fail if:** Launch decision is vague.

### CHECK-03: Closeout notes preserve Release 1 scope integrity

```bash
rg -n "native BIM|Revit|APS|connector|MEP|structural|out of scope|deferred" \
  artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/closeout.md
```

**Expected:** Deferred items and scope integrity are explicit.
**Fail if:** Closeout reopens deferred scope.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp7-program-b-release-readiness-and-launch-gate \
  --role validator \
  --status PASS \
  --summary "CP7 passed. Program B launch readiness is frozen with explicit evidence and honest scope." \
  --result-file artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/validation.json
```
