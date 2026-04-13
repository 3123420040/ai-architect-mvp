# CP6 — GLB Export Runtime

**Objective:** Replace placeholder 3D model output with a real GLB runtime contract.  
**Requires:** `cp5-phase6-storage-and-asset-registry` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp6-phase6-glb-export-runtime/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP6 — GLB Export Runtime",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement the runtime contract

Update:

- `../ai-architect-gpu/api/server.py`

The runtime request must accept:

- `bundle_id`
- `scene_spec_url` or equivalent payload
- render preset
- requested outputs
- output storage target

The runtime response must return artifact metadata suitable for app-side ingest.

## Step 2 — Implement scene assembly and GLB export

Create:

- `../ai-architect-gpu/pipelines/scene_builder.py`
- `../ai-architect-gpu/pipelines/blender_export.py`

Do not add approval logic, QA logic, or delivery-release logic to the GPU runtime.

## Step 3 — Wire app-side dispatch and ingest

Update:

- `../ai-architect-api/app/services/presentation_3d/orchestrator.py`

Ensure GLB export results become registered `presentation_3d_asset` rows and update job progression.

## Step 4 — Add tests

Create:

- `../ai-architect-gpu/tests/test_presentation_runtime.py`

Cover:

- runtime request validation
- scene-spec parsing
- GLB export metadata return
- placeholder output rejection

## Step 5 — Run required commands

```bash
cd ../ai-architect-gpu && python3 -m pytest tests/test_presentation_runtime.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp6-phase6-glb-export-runtime/runtime-tests.log
```

Record one representative GLB export flow in:

- `artifacts/phase6/cp6-phase6-glb-export-runtime/glb-export.log`

## Step 6 — Record completion and notify

Create:

- `artifacts/phase6/cp6-phase6-glb-export-runtime/result.json`
- `artifacts/phase6/cp6-phase6-glb-export-runtime/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp6-phase6-glb-export-runtime \
  --role implementer \
  --status READY \
  --summary "CP6 complete. GLB export runtime is ready and placeholder output is retired from the main path." \
  --result-file artifacts/phase6/cp6-phase6-glb-export-runtime/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp6-phase6-glb-export-runtime/result.json
```
