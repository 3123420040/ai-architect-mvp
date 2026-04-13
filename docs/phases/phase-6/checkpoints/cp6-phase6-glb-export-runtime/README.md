# CP6 — GLB Export Runtime

**Code:** `cp6-phase6-glb-export-runtime`  
**Order:** 6  
**Depends On:** `cp5-phase6-storage-and-asset-registry`  
**Estimated Effort:** 2 days

## Objective

Implement the first real runtime output lane so Phase 6 can export `scene.glb` from `scene_spec.json` instead of returning placeholder model data.

## Locked Slices

1. scene-spec reader
2. runtime request contract
3. Blender or headless scene assembly
4. GLB export
5. artifact metadata return

## Interfaces and States Touched

- runtime request payload
- runtime response payload
- `scene.glb` asset registration
- bundle `status`
- job `stage = runtime_render`

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| gpu | `../ai-architect-gpu/api/server.py` | updated | Runtime API boundary |
| gpu | `../ai-architect-gpu/pipelines/scene_builder.py` | created | Scene assembly from spec |
| gpu | `../ai-architect-gpu/pipelines/blender_export.py` | created | GLB export implementation |
| gpu | `../ai-architect-gpu/tests/test_presentation_runtime.py` | created | Runtime contract tests |
| api | `../ai-architect-api/app/services/presentation_3d/orchestrator.py` | updated | Runtime dispatch and ingest |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp6-phase6-glb-export-runtime/result.json` | created | Implementation result |
| `artifacts/phase6/cp6-phase6-glb-export-runtime/notes.md` | created | Runtime and GLB notes |
| `artifacts/phase6/cp6-phase6-glb-export-runtime/runtime-tests.log` | created | GPU/runtime test output |
| `artifacts/phase6/cp6-phase6-glb-export-runtime/glb-export.log` | created | One recorded runtime execution |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Runtime no longer returns placeholder glTF as the accepted Phase 6 output path | ✓ |
| CHECK-02 | `scene.glb` can be generated from `scene_spec.json` and registered through the app ingest path | ✓ |
| CHECK-03 | Runtime request and response shapes are explicit and stable | ✓ |
| CHECK-04 | GPU/runtime responsibility stays limited to render execution, not business approval logic | ✓ |
