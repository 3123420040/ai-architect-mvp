# CP1 Validation Checklist — Intake Chat-Only Workspace

**For:** Validator Agent
**Read first:** `docs/phases/phase-5/checkpoints/cp1-intake-chat-only-workspace/result.json`
**Goal:** Confirm that intake is now conversation-first and no longer split across duplicated suggestion surfaces.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp1-intake-chat-only-workspace/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP1 — Intake Chat-Only Workspace",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Removed suggestion surfaces are no longer present in the intake component

```bash
rg -n "Mức độ sẵn sàng của brief|Việc cần chốt tiếp|Định hướng đã ghi nhận" ../ai-architect-web/src/components/intake-client.tsx
```

**Expected:** Removed large side/support sections are absent or converted into minimal inline/chat-first forms.
**Fail if:** The old large support sections still exist as primary page blocks.

### CHECK-02: Web build passes

```bash
cd ../ai-architect-web && pnpm build
```

**Expected:** Build succeeds.
**Fail if:** The layout refactor breaks the app build.

### CHECK-03: Intake remains functionally usable

```bash
cd ../ai-architect-web && rg -n "sendMessage|saveBrief|assistant_payload" src/components/intake-client.tsx
```

**Expected:** The main chat and brief actions still exist after the simplification.
**Fail if:** The refactor removed key interaction paths.

## Record Validation

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp1-intake-chat-only-workspace \
  --role validator \
  --status PASS \
  --summary "Intake is now chat-first and no longer split by duplicated suggestion surfaces." \
  --result-file docs/phases/phase-5/checkpoints/cp1-intake-chat-only-workspace/validation.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp1-intake-chat-only-workspace/validation.json
```
