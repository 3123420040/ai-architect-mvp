# CP2 Validation Checklist — Brief Lock Contract

**For:** Validator Agent
**Read first:** `docs/phases/phase-5/checkpoints/cp2-brief-lock-contract/result.json`
**Goal:** Confirm that `brief locked` is a real contract state instead of a UI approximation.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp2-brief-lock-contract/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP2 — Brief Lock Contract",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Backend contract exposes separate brief state

```bash
rg -n "brief_state|ready_to_lock|locked|reopened" ../ai-architect-api/app/services/briefing.py ../ai-architect-api/app/schemas.py ../ai-architect-api/app/api/v1
```

**Expected:** A separate brief-state contract exists.
**Fail if:** Only readiness labels are present.

### CHECK-02: Tests cover locked and reopened behavior

```bash
cd ../ai-architect-api && ./.venv/bin/pytest tests/test_briefing.py tests/test_flows.py -q
```

**Expected:** Tests pass.
**Fail if:** Lock-state regressions or missing test coverage cause failures.

### CHECK-03: Frontend labels are mapped to the new contract

```bash
rg -n "Ready to lock|Brief locked|Reopened|Đã chốt brief|Sẵn sàng chốt" ../ai-architect-web/src/components/intake-client.tsx
```

**Expected:** The UI uses the new state model.
**Fail if:** The UI still infers lock from completion ratio alone.

## Record Validation

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp2-brief-lock-contract \
  --role validator \
  --status PASS \
  --summary "Brief lock is now an explicit product contract." \
  --result-file docs/phases/phase-5/checkpoints/cp2-brief-lock-contract/validation.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp2-brief-lock-contract/validation.json
```
