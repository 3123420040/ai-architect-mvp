# CP6 — Downstream Validation Pilot

**Objective:** Validate Program B with evidence before launch.
**Requires:** CP5 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp6-program-b-downstream-validation-pilot/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP6 — Program B downstream validation pilot",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Generate benchmark bundles

Use benchmark cases for:

- `townhouse`
- `villa`

Generate complete Program B bundles and record:

- generation success or failure
- semantic stability observations
- schedule completeness
- IFC export completeness
- readiness summary clarity

## Step 2 — Capture downstream review evidence

For each benchmark, record:

- whether external continuation appears easier than starting from concept package only
- whether issue and schedule data are actually usable
- what still forces re-interpretation

This evidence must go into `pilot-feedback.md`, not only chat or memory.

## Step 3 — Triage blockers

Create `blocker-list.json` with:

- blocker id
- severity
- impacted typology
- impacted artifact or workflow
- recommended fix owner

## Step 4 — Record completion artifacts

Create:

- `artifacts/program-b/cp6-program-b-downstream-validation-pilot/result.json`
- `artifacts/program-b/cp6-program-b-downstream-validation-pilot/benchmark-matrix.md`
- `artifacts/program-b/cp6-program-b-downstream-validation-pilot/pilot-feedback.md`
- `artifacts/program-b/cp6-program-b-downstream-validation-pilot/blocker-list.json`

## Step 5 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp6-program-b-downstream-validation-pilot \
  --role implementer \
  --status READY \
  --summary "CP6 complete. Program B downstream validation evidence and blockers are recorded." \
  --result-file artifacts/program-b/cp6-program-b-downstream-validation-pilot/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp6-program-b-downstream-validation-pilot/result.json
```
