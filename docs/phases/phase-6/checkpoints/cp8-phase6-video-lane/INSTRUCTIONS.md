# CP8 — Video Lane

**Objective:** Produce the first locked walkthrough MP4 package for Phase 6.  
**Requires:** `cp7-phase6-still-render-lane` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp8-phase6-video-lane/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP8 — Video Lane",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement video-render pipeline

Create:

- `../ai-architect-gpu/pipelines/video_render.py`

The first implementation must:

- read the walkthrough sequence from scene spec
- render frames deterministically
- encode MP4 with FFmpeg
- target `1080p minimum`, `30 fps`, `45–90 seconds`

## Step 2 — Bind video output to app ingest

Update app-side ingest to capture:

- video asset role
- `duration_seconds`
- output URL
- checksum

Ensure video remains a required asset in the release package.

## Step 3 — Add tests

Create:

- `../ai-architect-gpu/tests/test_presentation_video.py`

Update:

- `../ai-architect-api/tests/test_presentation_3d_assets.py`

Cover:

- duration window
- missing-video failure behavior
- video metadata ingest

## Step 4 — Run required commands

```bash
cd ../ai-architect-gpu && python3 -m pytest tests/test_presentation_video.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp8-phase6-video-lane/video-tests.log
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_assets.py -q >> ../ai-architect-mvp/artifacts/phase6/cp8-phase6-video-lane/video-tests.log
```

Record one representative video-render execution in:

- `artifacts/phase6/cp8-phase6-video-lane/video-runtime.log`

## Step 5 — Record completion and notify

Create:

- `artifacts/phase6/cp8-phase6-video-lane/result.json`
- `artifacts/phase6/cp8-phase6-video-lane/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp8-phase6-video-lane \
  --role implementer \
  --status READY \
  --summary "CP8 complete. Walkthrough video lane is generating MP4 with duration metadata." \
  --result-file artifacts/phase6/cp8-phase6-video-lane/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp8-phase6-video-lane/result.json
```
