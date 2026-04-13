# CP5 Validation Checklist — Storage and Asset Registry

**For:** Validator  
**Read first:** `artifacts/phase6/cp5-phase6-storage-and-asset-registry/result.json`  
**Goal:** Confirm durable storage and asset registration are stable before runtime outputs expand.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp5-phase6-storage-and-asset-registry/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP5 — Storage and Asset Registry",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Storage helper and asset registry exist

```bash
test -f ../ai-architect-api/app/services/presentation_3d/asset_registry.py && \
rg -n "signed|checksum|storage_key|duration_seconds|public_url" \
  ../ai-architect-api/app/services/storage.py \
  ../ai-architect-api/app/services/presentation_3d/asset_registry.py
```

**Expected:** Centralized storage helpers and asset registry logic exist.  
**Fail if:** Asset metadata logic is missing or duplicated ad hoc.

### CHECK-02: Storage test file exists and passes

```bash
test -f ../ai-architect-api/tests/test_presentation_3d_storage.py && \
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_storage.py -q
```

**Expected:** Storage and asset tests are present and green.  
**Fail if:** The test file is missing or failing.

### CHECK-03: Sample asset registry uses the locked object-key structure

```bash
test -f artifacts/phase6/cp5-phase6-storage-and-asset-registry/storage-sample.json && \
rg -n "projects/.+/versions/.+/3d/.+/(scene|renders|video|manifest|qa)/" \
  artifacts/phase6/cp5-phase6-storage-and-asset-registry/storage-sample.json
```

**Expected:** Asset storage keys follow the locked prefix structure.  
**Fail if:** Sample output uses ad hoc or local-only path schemes.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp5-phase6-storage-and-asset-registry \
  --role validator \
  --status PASS \
  --summary "CP5 passed. Durable storage and asset registry are stable." \
  --result-file artifacts/phase6/cp5-phase6-storage-and-asset-registry/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp5-phase6-storage-and-asset-registry/validation.json
```
