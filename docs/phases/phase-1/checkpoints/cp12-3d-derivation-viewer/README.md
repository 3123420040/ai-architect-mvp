# CP12 — 3D Derivation + Viewer

**Code:** cp12-3d-derivation-viewer
**Order:** 12
**Depends On:** cp11-export-bundle-readiness
**Estimated Effort:** 1 ngay

## Muc tieu

Noi locked canonical version voi 3D derivation, static renders va viewer 3D co feature flag de khong block core P0 flow.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-api/app/api/v1/derivation.py` | created | 3D derivation endpoints |
| `../ai-architect-gpu/pipelines/blender_3d_pipeline.py` | created | Blender headless pipeline |
| `../ai-architect-web/src/components/viewer/viewer-3d.tsx` | created | Three.js viewer |
| `../ai-architect-web/src/app/projects/[id]/viewer/page.tsx` | created | Viewer page |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Derivation chi cho phep tren locked version va integration tests pass | ✓ |
| CHECK-02 | GPU smoke test tao duoc model_url/render_urls | ✓ |
| CHECK-03 | Viewer page load duoc GLTF khi feature flag bat | ✓ |
