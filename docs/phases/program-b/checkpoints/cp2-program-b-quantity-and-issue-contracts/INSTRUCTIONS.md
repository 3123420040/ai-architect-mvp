# CP2 — Quantity and Issue Contracts

**Objective:** Add required schedules and issue registry resources.
**Requires:** CP1 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp2-program-b-quantity-and-issue-contracts/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP2 — Program B quantity and issue contracts",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement schedule extraction

Create:

- `../ai-architect-api/app/services/coordination/quantity_extractor.py`
- `../ai-architect-api/app/services/coordination/schedule_serializer.py`

Launch-required schedules:

- room schedule
- door/window schedule
- area schedule

Each row must carry:

- bundle linkage
- source element linkage where available
- confidence or verification state

## Step 2 — Implement issue registry

Create:

- `../ai-architect-api/app/services/coordination/issues.py`

Add fields for:

- issue code
- severity
- status
- source discipline
- owner
- linked room or element ids
- resolution note

## Step 3 — Expose API contracts

Extend `coordination.py` with:

- schedule read endpoints
- issue list endpoint
- issue create endpoint
- issue resolve endpoint

## Step 4 — Add tests

Suggested command:

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest -q tests/coordination
```

## Step 5 — Record completion artifacts

Create:

- `artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/result.json`
- `artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/notes.md`
- `artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/schedule-contract-notes.md`

## Step 6 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp2-program-b-quantity-and-issue-contracts \
  --role implementer \
  --status READY \
  --summary "CP2 complete. Program B schedules and issue registry contracts are implemented." \
  --result-file artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/result.json
```
