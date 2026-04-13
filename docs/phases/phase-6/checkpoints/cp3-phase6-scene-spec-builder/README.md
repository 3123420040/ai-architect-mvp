# CP3 — Scene Spec Builder

**Code:** `cp3-phase6-scene-spec-builder`  
**Order:** 3  
**Depends On:** `cp2-phase6-api-contracts-and-serializers`  
**Estimated Effort:** 1.5 days

## Objective

Build deterministic `scene_spec.json` generation from approved version truth so runtime execution never improvises product logic.

## Locked Slices

1. source loader
2. geometry minimum validation
3. room semantics extraction
4. material mapping
5. shot planning
6. scene spec persistence

## Interfaces and States Touched

- `presentation_scene_spec`
- bundle `scene_spec_revision`
- runtime request payload
- still shot definitions
- walkthrough sequence

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| api | `../ai-architect-api/app/services/presentation_3d/scene_spec_builder.py` | created | Deterministic builder |
| api | `../ai-architect-api/app/services/presentation_3d/material_mapping.py` | created | Material and staging rules |
| api | `../ai-architect-api/app/services/presentation_3d/shot_planner.py` | created | Still and walkthrough shot planning |
| api | `../ai-architect-api/tests/test_presentation_3d_scene_spec.py` | created | Determinism and validation tests |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp3-phase6-scene-spec-builder/result.json` | created | Implementation result |
| `artifacts/phase6/cp3-phase6-scene-spec-builder/notes.md` | created | Builder decisions and edge cases |
| `artifacts/phase6/cp3-phase6-scene-spec-builder/scene-spec-fixtures.log` | created | Fixture test output |
| `artifacts/phase6/cp3-phase6-scene-spec-builder/sample-scene-spec.json` | created | Representative output artifact |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Same approved input and same render config produce stable scene spec shape | ✓ |
| CHECK-02 | Missing geometry fails before runtime dispatch | ✓ |
| CHECK-03 | Shot list and walkthrough sequence are generated from locked rules, not ad hoc strings | ✓ |
| CHECK-04 | `scene_spec.json` is persisted as first-class artifact input to runtime | ✓ |
