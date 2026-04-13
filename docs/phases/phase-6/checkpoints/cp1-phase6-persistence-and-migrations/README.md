# CP1 — Persistence and Migrations

**Code:** `cp1-phase6-persistence-and-migrations`  
**Order:** 1  
**Depends On:** `cp0-phase6-scope-lock-and-baseline-audit`  
**Estimated Effort:** 1.5 days

## Objective

Add the Phase 6 persistence backbone so 3D presentation is modeled as first-class bundle, job, asset, and approval entities.

## Locked Slices

1. additive Alembic migration
2. ORM model wiring
3. enum definitions
4. minimal `DesignVersion` linkage
5. downgrade path

## Interfaces and States Touched

- `presentation_3d_bundle`
- `presentation_3d_job`
- `presentation_3d_asset`
- `presentation_3d_approval`
- bundle state enums
- job state enums

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| api | `../ai-architect-api/alembic/versions/*phase6_presentation_3d*.py` | created | Additive migration only |
| api | `../ai-architect-api/app/models.py` | updated | New models and `DesignVersion` linkage |
| api | `../ai-architect-api/app/schemas.py` | updated | Base schema types if kept centralized |
| api | `../ai-architect-api/tests/test_presentation_3d_persistence.py` | created | Migration and ORM persistence tests |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp1-phase6-persistence-and-migrations/result.json` | created | Implementation result |
| `artifacts/phase6/cp1-phase6-persistence-and-migrations/notes.md` | created | Schema rationale and migration notes |
| `artifacts/phase6/cp1-phase6-persistence-and-migrations/migration-up.log` | created | Upgrade log |
| `artifacts/phase6/cp1-phase6-persistence-and-migrations/migration-down.log` | created | Downgrade log |
| `artifacts/phase6/cp1-phase6-persistence-and-migrations/persistence-tests.log` | created | Test output |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | New tables exist for bundles, jobs, assets, and approvals | ✓ |
| CHECK-02 | Bundle and job enums match the locked root contract exactly | ✓ |
| CHECK-03 | `DesignVersion` has only minimal linkage to current bundle | ✓ |
| CHECK-04 | Migration upgrade and downgrade both run cleanly | ✓ |
