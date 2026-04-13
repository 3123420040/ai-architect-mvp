# CP4 Validation Checklist — Designs Sequence and State Correction

**For:** Validator Agent
**Read first:** `docs/phases/phase-5/checkpoints/cp4-designs-sequence-state/result.json`
**Goal:** Confirm that generation, selection, and review states now reflect the real workflow.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp4-designs-sequence-state/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP4 — Designs Sequence and State Correction",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Sequence logic is updated in the generation backend

```bash
rg -n "options_generated|under_review|superseded|version.select|generation.complete" ../ai-architect-api/app/api/v1/generation.py ../ai-architect-api/app/services/state_machine.py
```

**Expected:** Sequence logic no longer treats generated options as already under review.
**Fail if:** Review still starts implicitly at generation completion.

### CHECK-02: Flow tests pass

```bash
cd ../ai-architect-api && ./.venv/bin/pytest tests/test_flows.py -q
```

**Expected:** Tests pass.
**Fail if:** Selection or state transition regressions remain.

### CHECK-03: Designs client no longer opens generation stream on mount

```bash
rg -n "new WebSocket|generate/stream" ../ai-architect-web/src/components/designs-client.tsx
```

**Expected:** Streaming is attached to explicit generate behavior, not passive page load.
**Fail if:** The page still opens a stream immediately on initial render.

## Record Validation

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp4-designs-sequence-state \
  --role validator \
  --status PASS \
  --summary "Design generation and review sequence is now semantically correct." \
  --result-file docs/phases/phase-5/checkpoints/cp4-designs-sequence-state/validation.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp4-designs-sequence-state/validation.json
```
