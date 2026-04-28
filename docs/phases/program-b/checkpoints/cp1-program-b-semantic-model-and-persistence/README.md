# CP1 — Semantic Model and Persistence

**Code:** `cp1-program-b-semantic-model-and-persistence`
**Order:** 1
**Depends On:** `cp0-program-b-scope-lock-and-semantic-baseline`
**Estimated Effort:** 1 day

## Objective

Add the Program B persistence backbone and implement the first durable semantic coordination model for launch-supported typologies.

## Locked Slices

1. Program B tables and enums
2. semantic model builder
3. stable semantic ids
4. eligibility and typology blocking

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `../ai-architect-api/app/services/coordination/semantic_model_builder.py` | created | Semantic coordination model builder |
| `../ai-architect-api/app/services/coordination/semantic_ids.py` | created | Stable semantic id strategy |
| `../ai-architect-api/app/api/v1/coordination.py` | updated | Program B router backbone |
| `artifacts/program-b/cp1-program-b-semantic-model-and-persistence/result.json` | created | CP completion record |
| `artifacts/program-b/cp1-program-b-semantic-model-and-persistence/schema-notes.md` | created | Schema and model notes |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Program B tables and enums exist in migration or schema layer | ✓ |
| CHECK-02 | Semantic model builder can produce durable model data for `townhouse` and `villa` fixtures | ✓ |
| CHECK-03 | Unsupported typologies are blocked from launch flow | ✓ |
| CHECK-04 | Semantic ids are deterministic enough for downstream linkage tests | ✓ |
