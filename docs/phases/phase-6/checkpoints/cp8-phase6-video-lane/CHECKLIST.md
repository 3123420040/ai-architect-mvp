# CP8 Validation Checklist — Video Lane

**For:** Validator  
**Read first:** `artifacts/phase6/cp8-phase6-video-lane/result.json`  
**Goal:** Confirm the walkthrough video lane is complete enough for QA gating.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp8-phase6-video-lane/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP8 — Video Lane",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Video render pipeline and tests exist

```bash
test -f ../ai-architect-gpu/pipelines/video_render.py && \
test -f ../ai-architect-gpu/tests/test_presentation_video.py
```

**Expected:** Video-render implementation and test module exist.  
**Fail if:** The pipeline or test file is missing.

### CHECK-02: Video duration and output identity are represented in code

```bash
rg -n "walkthrough|duration_seconds|ffmpeg|1080|30" \
  ../ai-architect-gpu/pipelines/video_render.py \
  ../ai-architect-api/app/services/presentation_3d/orchestrator.py
```

**Expected:** The implementation captures the locked video identity and metadata.  
**Fail if:** Duration or encode path is not explicit.

### CHECK-03: Video tests pass

```bash
cd ../ai-architect-gpu && python3 -m pytest tests/test_presentation_video.py -q && \
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_assets.py -q
```

**Expected:** Video and ingest tests are green.  
**Fail if:** Any video-related test fails.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp8-phase6-video-lane \
  --role validator \
  --status PASS \
  --summary "CP8 passed. Walkthrough video lane is ready for QA and release gating." \
  --result-file artifacts/phase6/cp8-phase6-video-lane/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp8-phase6-video-lane/validation.json
```
