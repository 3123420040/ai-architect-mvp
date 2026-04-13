# CP1 — Intake Chat-Only Workspace

**Objective:** Make the intake page chat-first and remove duplicated suggestion content outside the conversation.
**Requires:** CP0 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp1-intake-chat-only-workspace/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP1 — Intake Chat-Only Workspace",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Remove non-essential suggestion surfaces

Update the intake layout in `../ai-architect-web/src/components/intake-client.tsx` so that:

- the large readiness card is removed or collapsed into a compact chip,
- example brief blocks outside the chat are removed,
- duplicated summary blocks outside the chat are removed,
- the chat becomes the visual center of the page,
- any remaining summary support is compact and secondary.

## Step 2 — Keep support UI minimal

If support UI remains outside chat, it must be one of:

- compact brief state chip,
- compact lock action,
- compact technical summary drawer.

Do not keep multiple vertical sections that repeat the same information as the AI thread.

## Step 3 — Verify locally

```bash
cd ../ai-architect-web && pnpm build
```

If the repo has existing lint warnings, record them but do not block on unrelated legacy warnings.

## Step 4 — Record completion

Create `docs/phases/phase-5/checkpoints/cp1-intake-chat-only-workspace/result.json`.

```json
{
  "cp": "cp1-intake-chat-only-workspace",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Intake is simplified into a chat-first clarification workspace.",
  "artifacts": [
    {"file": "../ai-architect-web/src/components/intake-client.tsx", "action": "updated"},
    {"file": "../ai-architect-web/src/components/app-shell.tsx", "action": "updated"},
    {"file": "../ai-architect-web/src/components/status-badge.tsx", "action": "updated"}
  ],
  "issues": [],
  "notes": "Outside-chat support UI must stay compact and non-duplicative."
}
```

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp1-intake-chat-only-workspace \
  --role implementer \
  --status READY \
  --summary "Intake is simplified into a chat-first clarification workspace." \
  --result-file docs/phases/phase-5/checkpoints/cp1-intake-chat-only-workspace/result.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp1-intake-chat-only-workspace/result.json
```
