# CP0 — Scope Lock and Semantic Baseline

**Objective:** Freeze Program B Release 1 boundaries before implementation starts.
**Requires:** None.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp0-program-b-scope-lock-and-semantic-baseline/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP0 — Program B scope lock and semantic baseline",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Review the locked Program B docs

Read and reconcile:

- `implementation/program-b/01-program-b-scope-lock.md`
- `implementation/program-b/02-program-b-requirements-detailed.md`
- `implementation/program-b/03-program-b-technical-design-detailed.md`
- `implementation/program-b/04-program-b-implementation-detailed.md`
- `implementation/program-b/06-program-b-detailed-checkpoint-breakdown.md`

Lock these decisions into `decision-freeze.json`:

- release name: `Program B Release 1`
- scope: `coordination-ready architectural handoff`
- launch typologies: `townhouse`, `villa`
- required outputs:
  - `coordination_model.json`
  - `architectural_coordination.ifc`
  - `room_schedule.csv`
  - `door_window_schedule.csv`
  - `area_schedule.csv`
  - `issue_register.json`
  - `coordination_manifest.json`
  - `readiness_summary.json`
- required semantic entity minimum
- pilot thresholds and launch thresholds

## Step 2 — Audit current baseline

Inspect:

- `../ai-architect-api/app/services/exporter.py`
- `../ai-architect-api/app/models.py`
- `../ai-architect-web/src/components/delivery-client.tsx`

Record in `semantic-baseline.md`:

- what current DXF and IFC exports actually prove
- what current data model does not yet support
- what current delivery workspace shows and hides
- which gaps are launch-blocking for Program B

Helpful commands:

```bash
rg -n "ifc|dxf|schedule|export_urls|bundle|delivery" ../ai-architect-api/app ../ai-architect-web/src
```

## Step 3 — Record completion artifacts

Create:

- `artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/result.json`
- `artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/notes.md`
- `artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/decision-freeze.json`
- `artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/semantic-baseline.md`

The result must include:

- final scope and out-of-scope items
- launch typologies
- launch thresholds
- remaining non-blocking notes

## Step 4 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp0-program-b-scope-lock-and-semantic-baseline \
  --role implementer \
  --status READY \
  --summary "CP0 complete. Program B scope, semantic minimum, and launch thresholds are locked." \
  --result-file artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/result.json
```
