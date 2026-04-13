# CP7 Validation Checklist — Still Render Lane

**For:** Validator  
**Read first:** `artifacts/phase6/cp7-phase6-still-render-lane/result.json`  
**Goal:** Confirm required still coverage is deterministic and complete enough for downstream QA.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7-phase6-still-render-lane/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP7 — Still Render Lane",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Still render pipeline and tests exist

```bash
test -f ../ai-architect-gpu/pipelines/still_render.py && \
test -f ../ai-architect-gpu/tests/test_presentation_stills.py && \
test -f ../ai-architect-api/tests/test_presentation_3d_assets.py
```

**Expected:** Still-render implementation and both test modules exist.  
**Fail if:** The pipeline or either test file is missing.

### CHECK-02: Locked shot IDs are present in runtime or ingest code

```bash
rg -n "exterior_hero_day|exterior_entry|living_room|kitchen_dining|master_bedroom" \
  ../ai-architect-gpu/pipelines/still_render.py \
  ../ai-architect-api/app/services/presentation_3d/orchestrator.py
```

**Expected:** The required launch shot IDs are encoded in the implementation path.  
**Fail if:** Required shots are not explicitly represented.

### CHECK-03: Still tests pass

```bash
cd ../ai-architect-gpu && python3 -m pytest tests/test_presentation_stills.py -q && \
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_assets.py -q
```

**Expected:** Shot completeness and asset-ingest tests are green.  
**Fail if:** Any still-related test fails.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp7-phase6-still-render-lane \
  --role validator \
  --status PASS \
  --summary "CP7 passed. Required still render coverage is ready for video and QA." \
  --result-file artifacts/phase6/cp7-phase6-still-render-lane/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp7-phase6-still-render-lane/validation.json
```
