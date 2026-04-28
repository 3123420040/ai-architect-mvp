# CP3 — Coordination IFC Export

**Objective:** Implement Program B architectural IFC export.
**Requires:** CP2 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp3-program-b-coordination-ifc-export/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP3 — Program B coordination IFC export",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement IFC exporter

Create:

- `../ai-architect-api/app/services/coordination/ifc_exporter.py`
- `../ai-architect-api/app/services/coordination/ifc_validation.py`

Exporter must:

- read the semantic coordination model
- map launch architectural elements
- write `architectural_coordination.ifc`
- persist validation metadata

## Step 2 — Register export in bundle flow

Update orchestration so Program B bundle generation includes:

- semantic model
- schedules
- IFC export
- validation metadata registration

## Step 3 — Add tests

Suggested command:

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest -q tests/coordination
```

## Step 4 — Record completion artifacts

Create:

- `artifacts/program-b/cp3-program-b-coordination-ifc-export/result.json`
- `artifacts/program-b/cp3-program-b-coordination-ifc-export/notes.md`
- `artifacts/program-b/cp3-program-b-coordination-ifc-export/ifc-export-notes.md`

## Step 5 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp3-program-b-coordination-ifc-export \
  --role implementer \
  --status READY \
  --summary "CP3 complete. Program B coordination IFC export is implemented." \
  --result-file artifacts/program-b/cp3-program-b-coordination-ifc-export/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp3-program-b-coordination-ifc-export/result.json
```
