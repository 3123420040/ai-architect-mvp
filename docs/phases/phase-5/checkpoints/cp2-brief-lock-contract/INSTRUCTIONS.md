# CP2 — Brief Lock Contract

**Objective:** Separate clarification readiness from brief contract state and make `Brief locked` explicit across the stack.
**Requires:** CP1 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp2-brief-lock-contract/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP2 — Brief Lock Contract",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Extend backend contract

Update backend logic so that:

- readiness remains about missing/conflicting clarification,
- brief state becomes a separate field,
- the brief state supports `draft`, `ready_to_lock`, `locked`, and `reopened`,
- `locked` requires required sections complete, no active conflicts, and explicit confirmation.

Files to update:

- `../ai-architect-api/app/services/briefing.py`
- `../ai-architect-api/app/schemas.py`
- `../ai-architect-api/app/api/v1/chat.py`
- `../ai-architect-api/app/api/v1/brief.py`
- `../ai-architect-api/app/api/v1/projects.py`

## Step 2 — Update frontend rendering

Update `../ai-architect-web/src/components/intake-client.tsx` so that the user sees a clean and consistent brief contract state:

- `Draft`
- `Ready to lock`
- `Brief locked`
- `Reopened`

Do not overload `completion_ratio` as the only visible source of truth.

## Step 3 — Add tests

At minimum, add or update tests for:

- ready-to-lock path,
- locked path,
- reopened path,
- conflict prevents locked path.

```bash
cd ../ai-architect-api && ./.venv/bin/pytest tests/test_briefing.py tests/test_flows.py -q
```

## Step 4 — Record completion

Create `docs/phases/phase-5/checkpoints/cp2-brief-lock-contract/result.json`.

```json
{
  "cp": "cp2-brief-lock-contract",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Brief lock state is now explicit and consistent across backend and frontend.",
  "artifacts": [
    {"file": "../ai-architect-api/app/services/briefing.py", "action": "updated"},
    {"file": "../ai-architect-api/app/schemas.py", "action": "updated"},
    {"file": "../ai-architect-api/app/api/v1/chat.py", "action": "updated"},
    {"file": "../ai-architect-api/app/api/v1/brief.py", "action": "updated"},
    {"file": "../ai-architect-api/app/api/v1/projects.py", "action": "updated"},
    {"file": "../ai-architect-web/src/components/intake-client.tsx", "action": "updated"},
    {"file": "../ai-architect-api/tests/test_briefing.py", "action": "updated"}
  ],
  "issues": [],
  "notes": "The UI must not imply a locked brief unless explicit confirmation has been recorded."
}
```

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp2-brief-lock-contract \
  --role implementer \
  --status READY \
  --summary "Brief lock state is now explicit and consistent across backend and frontend." \
  --result-file docs/phases/phase-5/checkpoints/cp2-brief-lock-contract/result.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp2-brief-lock-contract/result.json
```
