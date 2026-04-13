# CP7 — Still Render Lane

**Code:** `cp7-phase6-still-render-lane`  
**Order:** 7  
**Depends On:** `cp6-phase6-glb-export-runtime`  
**Estimated Effort:** 1.5 days

## Objective

Produce the required curated still set from planned shot definitions and register them as first-class presentation assets.

## Locked Slices

1. camera mapping
2. render preset binding
3. still export
4. asset ingest
5. gallery ordering

## Interfaces and States Touched

- still shot definitions
- `renders/{shot_id}.png`
- hero still identification
- interior room shot completeness
- gallery ordering in bundle payload

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| gpu | `../ai-architect-gpu/pipelines/still_render.py` | created | Still render pipeline |
| gpu | `../ai-architect-gpu/tests/test_presentation_stills.py` | created | Shot completeness and metadata tests |
| api | `../ai-architect-api/app/services/presentation_3d/orchestrator.py` | updated | Still ingest and ordering |
| api | `../ai-architect-api/tests/test_presentation_3d_assets.py` | created | Still-asset ingest tests |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp7-phase6-still-render-lane/result.json` | created | Implementation result |
| `artifacts/phase6/cp7-phase6-still-render-lane/notes.md` | created | Shot coverage and preset notes |
| `artifacts/phase6/cp7-phase6-still-render-lane/still-runtime.log` | created | Still-render execution log |
| `artifacts/phase6/cp7-phase6-still-render-lane/still-tests.log` | created | Still-render test output |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Required shot IDs are produced and registered for every passing bundle | ✓ |
| CHECK-02 | Hero still is explicitly identified and interior shot roles are preserved | ✓ |
| CHECK-03 | Still preset binding is deterministic and not prompt-only | ✓ |
| CHECK-04 | Bundle gallery ordering is stable and frontend-consumable | ✓ |
