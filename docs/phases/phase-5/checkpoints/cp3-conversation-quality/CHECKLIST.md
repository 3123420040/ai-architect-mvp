# CP3 Validation Checklist — Conversation Quality Hardening

**For:** Validator Agent
**Read first:** `docs/phases/phase-5/checkpoints/cp3-conversation-quality/result.json`
**Goal:** Confirm that assistant turns are better prioritized, easier to scan, and grounded in the new chat-first workspace.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp3-conversation-quality/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP3 — Conversation Quality Hardening",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Assistant payload no longer defaults to long generic prompt lists

```bash
rg -n "next_prompts|headline|captured_facts|closing" ../ai-architect-api/app/services/briefing.py
```

**Expected:** The payload contract still exists, but follow-up logic is more selective and turn-based.
**Fail if:** The implementation still sprays broad prompt bundles every turn.

### CHECK-02: Transcript tests pass

```bash
cd ../ai-architect-api && ./.venv/bin/pytest tests/test_briefing.py tests/test_flows.py -q
```

**Expected:** Tests pass.
**Fail if:** Context-switch or conflict behaviors regress.

### CHECK-03: Chat UI still renders structured assistant content

```bash
rg -n "AssistantMessageCard|PlainTextMessage|assistant_payload" ../ai-architect-web/src/components/intake-client.tsx
```

**Expected:** Structured rendering remains intact.
**Fail if:** The chat falls back to unreadable plain text as the primary path.

## Record Validation

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp3-conversation-quality \
  --role validator \
  --status PASS \
  --summary "Conversation quality is improved and remains structurally renderable." \
  --result-file docs/phases/phase-5/checkpoints/cp3-conversation-quality/validation.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp3-conversation-quality/validation.json
```
