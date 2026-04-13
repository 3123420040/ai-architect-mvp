# CP10 Validation Checklist — Approval Gate and Manifest

**For:** Validator  
**Read first:** `artifacts/phase6/cp10-phase6-approval-gate-and-manifest/result.json`  
**Goal:** Confirm Phase 6 has a real release gate rather than a loose asset bundle.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp10-phase6-approval-gate-and-manifest/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP10 — Approval Gate and Manifest",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Manifest service exists and includes required sections

```bash
test -f ../ai-architect-api/app/services/presentation_3d/manifest.py && \
rg -n "manifest_version|bundle_identity|source_identity|approval|qa_summary|delivery_state|assets|branding|disclaimer|generation_metadata" \
  ../ai-architect-api/app/services/presentation_3d/manifest.py \
  artifacts/phase6/cp10-phase6-approval-gate-and-manifest/sample-manifest.json
```

**Expected:** Manifest generation and a representative output both include the locked sections.  
**Fail if:** Required manifest sections are missing.

### CHECK-02: Approval and rejection endpoints are explicit

```bash
rg -n "approve|reject|approval_status|delivery_status|qa_status" \
  ../ai-architect-api/app/api/v1/presentation_3d.py \
  ../ai-architect-api/app/services/presentation_3d/manifest.py
```

**Expected:** Approval and release logic is explicit in code.  
**Fail if:** Approval or release still happens as an implicit side effect.

### CHECK-03: Delivery tests pass

```bash
test -f ../ai-architect-api/tests/test_presentation_3d_delivery.py && \
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_delivery.py -q
```

**Expected:** Approval, rejection, and release-gating tests are green.  
**Fail if:** The test file is missing or failing.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp10-phase6-approval-gate-and-manifest \
  --role validator \
  --status PASS \
  --summary "CP10 passed. Manifest-first release and approval gating are functioning." \
  --result-file artifacts/phase6/cp10-phase6-approval-gate-and-manifest/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp10-phase6-approval-gate-and-manifest/validation.json
```
