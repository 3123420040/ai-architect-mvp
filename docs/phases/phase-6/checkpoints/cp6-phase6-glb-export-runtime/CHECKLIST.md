# CP6 Validation Checklist — GLB Export Runtime

**For:** Validator  
**Read first:** `artifacts/phase6/cp6-phase6-glb-export-runtime/result.json`  
**Goal:** Confirm the runtime can now generate GLB from the locked scene contract.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp6-phase6-glb-export-runtime/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP6 — GLB Export Runtime",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Runtime pipeline files exist

```bash
test -f ../ai-architect-gpu/pipelines/scene_builder.py && \
test -f ../ai-architect-gpu/pipelines/blender_export.py
```

**Expected:** Runtime scene-builder and GLB export pipeline files exist.  
**Fail if:** Runtime still relies entirely on the old placeholder path.

### CHECK-02: Runtime no longer references placeholder-only output as success path

```bash
rg -n "scene_spec|scene.glb|artifact|storage" ../ai-architect-gpu/api/server.py ../ai-architect-gpu/pipelines/scene_builder.py ../ai-architect-gpu/pipelines/blender_export.py && \
! rg -n "placeholder|SVG render placeholder|model_gltf" ../ai-architect-gpu/pipelines/scene_builder.py ../ai-architect-gpu/pipelines/blender_export.py
```

**Expected:** Runtime code is centered on real scene-spec driven export.  
**Fail if:** Placeholder model generation remains the accepted success path.

### CHECK-03: Runtime tests pass

```bash
test -f ../ai-architect-gpu/tests/test_presentation_runtime.py && \
cd ../ai-architect-gpu && python3 -m pytest tests/test_presentation_runtime.py -q
```

**Expected:** Runtime contract tests are present and green.  
**Fail if:** The test file is missing or failing.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp6-phase6-glb-export-runtime \
  --role validator \
  --status PASS \
  --summary "CP6 passed. GLB runtime contract is ready for still and video lanes." \
  --result-file artifacts/phase6/cp6-phase6-glb-export-runtime/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp6-phase6-glb-export-runtime/validation.json
```
