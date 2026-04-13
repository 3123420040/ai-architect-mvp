# CP2 — API Contracts and Serializers

**Code:** `cp2-phase6-api-contracts-and-serializers`  
**Order:** 2  
**Depends On:** `cp1-phase6-persistence-and-migrations`  
**Estimated Effort:** 1.5 days

## Objective

Expose the Phase 6 bundle-first API contract and typed frontend consumption layer without relying on the legacy `model_url + render_urls` shape.

## Locked Slices

1. endpoint skeletons
2. request and response schemas
3. eligibility errors
4. legacy-route deprecation behavior
5. typed frontend fetch contract

## Interfaces and States Touched

- all seven public Phase 6 endpoints
- bundle summary shape
- bundle detail shape
- job detail shape
- delivery-state and approval-state serialization

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| api | `../ai-architect-api/app/api/v1/presentation_3d.py` | created | New bundle-first router |
| api | `../ai-architect-api/app/api/v1/router.py` | updated | Route registration |
| api | `../ai-architect-api/app/schemas.py` | updated | Serializer types if centralized |
| api | `../ai-architect-api/tests/test_presentation_3d_api.py` | created | API contract tests |
| web | `../ai-architect-web/src/lib/presentation-3d.ts` | created | Typed fetch adapter |
| web | `../ai-architect-web/src/lib/api-types.generated.ts` | updated | Generated types if required |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp2-phase6-api-contracts-and-serializers/result.json` | created | Implementation result |
| `artifacts/phase6/cp2-phase6-api-contracts-and-serializers/notes.md` | created | Contract notes and deprecation behavior |
| `artifacts/phase6/cp2-phase6-api-contracts-and-serializers/api-tests.log` | created | API test output |
| `artifacts/phase6/cp2-phase6-api-contracts-and-serializers/openapi-snapshot.json` | created | Captured API surface |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | All seven locked endpoints exist and serialize bundle-first payloads | ✓ |
| CHECK-02 | Latest bundle fetch no longer requires legacy `model_url` or `render_urls` reads | ✓ |
| CHECK-03 | Invalid eligibility paths return explicit `409` or `422` behavior | ✓ |
| CHECK-04 | Frontend has a typed fetch adapter for the new contract | ✓ |
