# CP8 — Video Lane

**Code:** `cp8-phase6-video-lane`  
**Order:** 8  
**Depends On:** `cp7-phase6-still-render-lane`  
**Estimated Effort:** 1.5 days

## Objective

Generate `walkthrough.mp4` from the planned walkthrough sequence and register it as a required Phase 6 artifact with duration controls.

## Locked Slices

1. path planner read
2. frame render
3. FFmpeg encode
4. duration validation
5. asset ingest

## Interfaces and States Touched

- walkthrough sequence
- `video/walkthrough.mp4`
- `duration_seconds`
- render preset for video lane
- bundle asset list

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| gpu | `../ai-architect-gpu/pipelines/video_render.py` | created | Walkthrough frame and MP4 pipeline |
| gpu | `../ai-architect-gpu/tests/test_presentation_video.py` | created | Duration and contract tests |
| api | `../ai-architect-api/app/services/presentation_3d/orchestrator.py` | updated | Video ingest path |
| api | `../ai-architect-api/tests/test_presentation_3d_assets.py` | updated | Video metadata ingest tests |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp8-phase6-video-lane/result.json` | created | Implementation result |
| `artifacts/phase6/cp8-phase6-video-lane/notes.md` | created | Video lane notes |
| `artifacts/phase6/cp8-phase6-video-lane/video-tests.log` | created | Video test output |
| `artifacts/phase6/cp8-phase6-video-lane/video-runtime.log` | created | One recorded video-render example |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | `walkthrough.mp4` is generated and ingested as a required bundle asset | ✓ |
| CHECK-02 | Duration metadata is captured and validated against the `45–90 seconds` launch window | ✓ |
| CHECK-03 | The first implementation uses deterministic camera path playback and FFmpeg encode | ✓ |
| CHECK-04 | Video lane does not introduce cinematic-edit scope beyond Program A | ✓ |
