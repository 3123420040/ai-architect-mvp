# CP0 Validation Checklist — Scope Lock and Baseline Audit

**For:** Validator  
**Read first:** `artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/result.json`  
**Goal:** Confirm Phase 6 starts from a locked and production-grounded contract.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp0-phase6-scope-lock-and-baseline-audit/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP0 — Scope Lock and Baseline Audit",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Phase 6 docs and baseline artifacts exist

```bash
test -f implementation/phase-6/05-phase-6-scope-lock.md && \
test -f implementation/phase-6/06-phase-6-implementation-detailed.md && \
test -f implementation/phase-6/07-phase-6-api-job-and-storage-contracts.md && \
test -f implementation/phase-6/13-phase-6-technical-design-detailed.md && \
test -f implementation/phase-6/14-phase-6-detailed-checkpoint-breakdown.md && \
test -f artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/result.json && \
test -f artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/decision-freeze.json
```

**Expected:** All source docs and CP0 artifacts are present.  
**Fail if:** Any required file is missing.

### CHECK-02: Decision freeze explicitly locks Program A and excludes Program B/C

```bash
rg -n "Program A|Program B|Program C|client_presentation|walkthrough" \
  implementation/phase-6/05-phase-6-scope-lock.md \
  artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/decision-freeze.json
```

**Expected:** Scope and launch constraints are explicit.  
**Fail if:** The file does not clearly separate Program A from future programs.

### CHECK-03: Baseline audit references current sync derive, debug viewer, and GPU placeholder runtime

```bash
rg -n "derive-3d|viewer|placeholder|SVG|glTF|model_url|render_urls" \
  artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/notes.md \
  artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/mock-demo.log
```

**Expected:** Current-state limitations are recorded.  
**Fail if:** The baseline audit is generic and not grounded in current system behavior.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp0-phase6-scope-lock-and-baseline-audit \
  --role validator \
  --status PASS \
  --summary "CP0 passed. Phase 6 scope and baseline gap are locked." \
  --result-file artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/validation.json
```
