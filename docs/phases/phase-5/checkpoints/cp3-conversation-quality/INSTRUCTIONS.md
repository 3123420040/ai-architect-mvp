# CP3 — Conversation Quality Hardening

**Objective:** Improve the quality of AI clarification turns without re-expanding the intake page around the chat.
**Requires:** CP2 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp3-conversation-quality/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP3 — Conversation Quality Hardening",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Refine follow-up strategy

Update the assistant contract so that each turn:

- confirms what changed,
- asks at most one or two priority follow-ups,
- keeps quick replies tightly connected to those asks,
- avoids dumping broad lists when a narrower next step is possible.

Primary files:

- `../ai-architect-api/app/services/briefing.py`
- `../ai-architect-api/app/services/llm.py`

## Step 2 — Improve readable formatting

Update chat rendering in `../ai-architect-web/src/components/intake-client.tsx` so that:

- message hierarchy is obvious,
- sections are not visually noisy,
- quick reply actions sit close to the related AI ask.

## Step 3 — Add transcript coverage

Add or update transcript-oriented tests for:

- context switch,
- budget still missing,
- brief almost complete,
- conflict warning,
- apartment renovation path.

```bash
cd ../ai-architect-api && ./.venv/bin/pytest tests/test_briefing.py tests/test_flows.py -q
```

## Step 4 — Record completion

Create `docs/phases/phase-5/checkpoints/cp3-conversation-quality/result.json`.

```json
{
  "cp": "cp3-conversation-quality",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "AI clarification turns are more focused, readable, and tactful.",
  "artifacts": [
    {"file": "../ai-architect-api/app/services/briefing.py", "action": "updated"},
    {"file": "../ai-architect-api/app/services/llm.py", "action": "updated"},
    {"file": "../ai-architect-web/src/components/intake-client.tsx", "action": "updated"},
    {"file": "../ai-architect-api/tests/test_briefing.py", "action": "updated"}
  ],
  "issues": [],
  "notes": "The AI should prefer the highest-value next question instead of broad generic prompt dumps."
}
```

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp3-conversation-quality \
  --role implementer \
  --status READY \
  --summary "AI clarification turns are more focused, readable, and tactful." \
  --result-file docs/phases/phase-5/checkpoints/cp3-conversation-quality/result.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp3-conversation-quality/result.json
```
