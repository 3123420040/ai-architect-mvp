# CP0 — Scope Lock and Baseline Audit

**Objective:** Freeze Phase 6 execution boundaries before implementation starts.  
**Requires:** None.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp0-phase6-scope-lock-and-baseline-audit/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP0 — Scope Lock and Baseline Audit",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Review the locked Phase 6 docs

Read and reconcile:

- `implementation/phase-6/05-phase-6-scope-lock.md`
- `implementation/phase-6/06-phase-6-implementation-detailed.md`
- `implementation/phase-6/07-phase-6-api-job-and-storage-contracts.md`
- `implementation/phase-6/13-phase-6-technical-design-detailed.md`
- `implementation/phase-6/14-phase-6-detailed-checkpoint-breakdown.md`

Lock these decisions into `decision-freeze.json`:

- presentation mode: `client_presentation`
- minimum still set:
  - `exterior_hero_day`
  - `exterior_entry`
  - `living_room`
  - `kitchen_dining`
  - `master_bedroom`
- minimum video target: `45–90 seconds`, `1080p minimum`, `30 fps`
- public resources, enums, endpoints, and frontend states from the checkpoint root README

## Step 2 — Audit current runtime baseline

Inspect:

- `../ai-architect-api/app/api/v1/derivation.py`
- `../ai-architect-web/src/components/viewer-client.tsx`
- `../ai-architect-gpu/api/server.py`

Record in `notes.md`:

- what current sync derive returns
- what current viewer can and cannot show
- what current GPU runtime still stubs or placeholders
- what must be preserved temporarily during migration

## Step 3 — Run the mock baseline demo

```bash
python3 scripts/phase6_3d_mock_demo.py | tee artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/mock-demo.log
```

Use the output to confirm the current production baseline and note the current gap versus the Phase 6 target package.

## Step 4 — Record completion artifacts

Create:

- `artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/result.json`
- `artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/notes.md`
- `artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/decision-freeze.json`

The result must include:

- locked output set
- locked status model
- locked API endpoints
- explicit out-of-scope items
- any unresolved non-blocking notes

## Step 5 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp0-phase6-scope-lock-and-baseline-audit \
  --role implementer \
  --status READY \
  --summary "CP0 complete. Phase 6 scope, asset naming, state model, and baseline gap are locked." \
  --result-file artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/result.json
```
