# CP5 — Storage and Asset Registry

**Objective:** Make all final Phase 6 assets durable, addressable, and metadata-rich.  
**Requires:** `cp4-phase6-job-orchestration-and-state-machine` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp5-phase6-storage-and-asset-registry/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP5 — Storage and Asset Registry",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Extend the app storage adapter

Update `../ai-architect-api/app/services/storage.py` to support:

- signed URL generation for Phase 6 assets
- checksum capture
- media metadata capture
- stable object key helpers for `scene`, `renders`, `video`, `manifest`, and `qa`

## Step 2 — Implement the registry and ingest path

Create:

- `../ai-architect-api/app/services/presentation_3d/asset_registry.py`

Wire runtime output ingestion so every durable asset becomes a `presentation_3d_asset` row with:

- `asset_type`
- `asset_role`
- `storage_key`
- `public_url`
- `checksum`
- `width`, `height`, `duration_seconds` where relevant

## Step 3 — Add tests

Create:

- `../ai-architect-api/tests/test_presentation_3d_storage.py`

Cover:

- stable object key generation
- signed URL behavior
- asset metadata ingestion
- separation of scratch vs durable paths

## Step 4 — Run required commands

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_storage.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp5-phase6-storage-and-asset-registry/storage-tests.log
```

Save one representative asset registry payload to:

- `artifacts/phase6/cp5-phase6-storage-and-asset-registry/storage-sample.json`

## Step 5 — Record completion and notify

Create:

- `artifacts/phase6/cp5-phase6-storage-and-asset-registry/result.json`
- `artifacts/phase6/cp5-phase6-storage-and-asset-registry/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp5-phase6-storage-and-asset-registry \
  --role implementer \
  --status READY \
  --summary "CP5 complete. Storage and asset registry are ready for runtime outputs." \
  --result-file artifacts/phase6/cp5-phase6-storage-and-asset-registry/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp5-phase6-storage-and-asset-registry/result.json
```
