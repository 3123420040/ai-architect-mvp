# CP7 — Still Render Lane

**Objective:** Produce and register the locked curated still set.  
**Requires:** `cp6-phase6-glb-export-runtime` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7-phase6-still-render-lane/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP7 — Still Render Lane",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement still-render pipeline

Create:

- `../ai-architect-gpu/pipelines/still_render.py`

The first locked still set is:

- `exterior_hero_day`
- `exterior_entry`
- `living_room`
- `kitchen_dining`
- `master_bedroom`

## Step 2 — Bind still outputs to app ingest

Update app-side ingest so still outputs become `presentation_3d_asset` rows with:

- shot id
- asset role
- width and height
- gallery order
- hero flag or equivalent role marker

## Step 3 — Add tests

Create:

- `../ai-architect-gpu/tests/test_presentation_stills.py`
- `../ai-architect-api/tests/test_presentation_3d_assets.py`

Cover:

- required shot completeness
- hero still identification
- missing-room or missing-shot failure behavior
- deterministic gallery ordering

## Step 4 — Run required commands

```bash
cd ../ai-architect-gpu && python3 -m pytest tests/test_presentation_stills.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp7-phase6-still-render-lane/still-tests.log
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_assets.py -q >> ../ai-architect-mvp/artifacts/phase6/cp7-phase6-still-render-lane/still-tests.log
```

Record one still-render example in:

- `artifacts/phase6/cp7-phase6-still-render-lane/still-runtime.log`

## Step 5 — Record completion and notify

Create:

- `artifacts/phase6/cp7-phase6-still-render-lane/result.json`
- `artifacts/phase6/cp7-phase6-still-render-lane/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp7-phase6-still-render-lane \
  --role implementer \
  --status READY \
  --summary "CP7 complete. Required still render lane and gallery ordering are ready." \
  --result-file artifacts/phase6/cp7-phase6-still-render-lane/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp7-phase6-still-render-lane/result.json
```
