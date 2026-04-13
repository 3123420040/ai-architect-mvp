# CP4 — Designs Sequence and State Correction

**Objective:** Make the generation-to-review flow semantically correct across backend, audit trail, and UI.
**Requires:** CP3 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp4-designs-sequence-state/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP4 — Designs Sequence and State Correction",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Correct backend sequence

Read first:

- `implementation/phase-5/04-phase-5-option-generation-deep-dive.md`
- `implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md`

Update the generation lane so that:

- generation completion sets project state to something equivalent to `options_generated`,
- selecting a version is what starts review,
- audit logs reflect the real business sequence.
- version payload is ready to expose richer metadata needed by CP5.
- structured strategy profile and decision metadata can persist on each generated version.

Primary files:

- `../ai-architect-api/app/api/v1/generation.py`
- `../ai-architect-api/app/services/state_machine.py`
- `../ai-architect-api/app/api/v1/projects.py`

## Step 2 — Remove eager generation stream behavior

Update `../ai-architect-web/src/components/designs-client.tsx` so the websocket generation stream is created only when generation is actively triggered.

The page should load passively and only stream when necessary.

At the same time, make sure the frontend does not hard-code assumptions that only support `Option A/B/C` plus a single generic description.

## Step 3 — Add coverage

```bash
cd ../ai-architect-api && ./.venv/bin/pytest tests/test_flows.py -q
cd ../ai-architect-web && pnpm build
```

Coverage should explicitly verify:

- generation completion does not imply review,
- selected version is the only one moving into review,
- API payload retains enough metadata for the next checkpoint,
- strategy profile and decision metadata survive generation persistence and serialization.

## Step 4 — Record completion

Create `docs/phases/phase-5/checkpoints/cp4-designs-sequence-state/result.json`.

```json
{
  "cp": "cp4-designs-sequence-state",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Generation and review sequence now reflects real business flow.",
  "artifacts": [
    {"file": "../ai-architect-api/app/api/v1/generation.py", "action": "updated"},
    {"file": "../ai-architect-api/app/services/state_machine.py", "action": "updated"},
    {"file": "../ai-architect-api/app/api/v1/projects.py", "action": "updated"},
    {"file": "../ai-architect-web/src/components/designs-client.tsx", "action": "updated"},
    {"file": "../ai-architect-api/tests/test_flows.py", "action": "updated"}
  ],
  "issues": [],
  "notes": "Project status must not imply review until an option is explicitly selected, and the payload must stay ready for richer option-generation metadata, including strategy profile and decision metadata."
}
```

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp4-designs-sequence-state \
  --role implementer \
  --status READY \
  --summary "Generation and review sequence now reflects real business flow." \
  --result-file docs/phases/phase-5/checkpoints/cp4-designs-sequence-state/result.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp4-designs-sequence-state/result.json
```
