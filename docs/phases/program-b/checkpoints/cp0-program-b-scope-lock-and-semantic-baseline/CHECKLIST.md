# CP0 Validation Checklist — Scope Lock and Semantic Baseline

**For:** Validator
**Read first:** `artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/result.json`
**Goal:** Confirm Program B starts from a frozen and reality-based execution contract.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp0-program-b-scope-lock-and-semantic-baseline/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP0 — Program B scope lock and semantic baseline",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Locked docs and CP0 artifacts exist

```bash
test -f implementation/program-b/01-program-b-scope-lock.md && \
test -f implementation/program-b/02-program-b-requirements-detailed.md && \
test -f implementation/program-b/03-program-b-technical-design-detailed.md && \
test -f implementation/program-b/04-program-b-implementation-detailed.md && \
test -f artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/result.json && \
test -f artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/decision-freeze.json && \
test -f artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/semantic-baseline.md
```

**Expected:** All source docs and CP0 artifacts are present.
**Fail if:** Any required file is missing.

### CHECK-02: Decision freeze locks Release 1 to architectural coordination only

```bash
rg -n "coordination-ready architectural handoff|townhouse|villa|native BIM|Revit|MEP|structural" \
  implementation/program-b/01-program-b-scope-lock.md \
  artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/decision-freeze.json
```

**Expected:** Scope and exclusions are explicit.
**Fail if:** The freeze does not clearly exclude authoring and non-launch scope.

### CHECK-03: Baseline audit is grounded in current export and delivery behavior

```bash
rg -n "IFC|DXF|delivery|semantic|gap|issue|schedule" \
  artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/semantic-baseline.md \
  artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/notes.md
```

**Expected:** Current-state limitations are explicitly recorded.
**Fail if:** The baseline is generic and not tied to current project reality.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp0-program-b-scope-lock-and-semantic-baseline \
  --role validator \
  --status PASS \
  --summary "CP0 passed. Program B scope and semantic baseline are locked." \
  --result-file artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/validation.json
```
