# CP5 — Storage and Asset Registry

**Code:** `cp5-phase6-storage-and-asset-registry`  
**Order:** 5  
**Depends On:** `cp4-phase6-job-orchestration-and-state-machine`  
**Estimated Effort:** 1.5 days

## Objective

Separate temporary render scratch space from durable object storage and register every final Phase 6 asset with stable metadata.

## Locked Slices

1. storage adapter extension
2. signed URL strategy
3. durable object key rules
4. asset checksum and media metadata
5. ingest pipeline

## Interfaces and States Touched

- `presentation_3d_asset`
- bundle asset references
- signed/public URL generation
- storage key naming convention
- output ingest handoff from runtime to app

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| api | `../ai-architect-api/app/services/storage.py` | updated | Signed URL and metadata helpers |
| api | `../ai-architect-api/app/services/presentation_3d/asset_registry.py` | created | Durable asset registration layer |
| api | `../ai-architect-api/app/services/presentation_3d/orchestrator.py` | updated | Output ingest path |
| api | `../ai-architect-api/tests/test_presentation_3d_storage.py` | created | Storage and registry tests |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp5-phase6-storage-and-asset-registry/result.json` | created | Implementation result |
| `artifacts/phase6/cp5-phase6-storage-and-asset-registry/notes.md` | created | Storage and URL policy notes |
| `artifacts/phase6/cp5-phase6-storage-and-asset-registry/storage-tests.log` | created | Registry/storage test output |
| `artifacts/phase6/cp5-phase6-storage-and-asset-registry/storage-sample.json` | created | Sample registered asset list |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Final assets resolve to stable object keys under the locked `projects/{project_id}/versions/{version_id}/3d/{bundle_id}/...` pattern | ✓ |
| CHECK-02 | Asset rows capture storage key, URL, checksum, media metadata, and role | ✓ |
| CHECK-03 | Runtime scratch and durable storage are explicitly separated | ✓ |
| CHECK-04 | Signed URL generation is centralized in app storage services, not duplicated in runtime or frontend | ✓ |
