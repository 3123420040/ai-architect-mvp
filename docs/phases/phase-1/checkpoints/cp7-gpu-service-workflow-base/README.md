# CP7 — GPU Service + Workflow Base

**Code:** cp7-gpu-service-workflow-base
**Order:** 7
**Depends On:** cp6-intake-ui-brief-editor
**Estimated Effort:** 1 ngay

## Muc tieu

Dung duoc GPU wrapper, ComfyUI API mode, workflow JSON base, progress callback va fallback skeleton de chuan bi cho generation that.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-gpu/api/server.py` | created | FastAPI wrapper |
| `../ai-architect-gpu/comfyui/workflows/floor_plan_gen.json` | created | Workflow base |
| `../ai-architect-gpu/pipelines/floor_plan_pipeline.py` | created | Diffusers fallback |
| `../ai-architect-gpu/Dockerfile.gpu` | created | GPU image |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | GPU wrapper boot duoc va `/health` tra thong tin GPU/ComfyUI | ✓ |
| CHECK-02 | Workflow JSON validate duoc va generation API nhan request | ✓ |
| CHECK-03 | Progress callback va webhook skeleton hoat dong | ✓ |
