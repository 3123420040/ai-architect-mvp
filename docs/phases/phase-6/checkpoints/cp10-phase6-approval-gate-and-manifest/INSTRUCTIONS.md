# CP10 — Approval Gate and Manifest

**Objective:** Make release a manifest-first, architect-approved action instead of an implicit artifact side effect.  
**Requires:** `cp9-phase6-qa-validator-and-degraded-policy` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp10-phase6-approval-gate-and-manifest/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP10 — Approval Gate and Manifest",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement manifest generation

Create:

- `../ai-architect-api/app/services/presentation_3d/manifest.py`

The manifest must include at minimum:

- `manifest_version`
- `bundle_identity`
- `source_identity`
- `approval`
- `qa_summary`
- `delivery_state`
- `assets`
- `branding`
- `disclaimer`
- `generation_metadata`

## Step 2 — Implement approval and rejection flow

Update `../ai-architect-api/app/api/v1/presentation_3d.py` so:

- approval is blocked when QA is `fail`
- approval notes are persisted
- rejection preserves preview but blocks release
- release state changes only after approval and required assets are present

## Step 3 — Add tests

Create:

- `../ai-architect-api/tests/test_presentation_3d_delivery.py`

Cover:

- approval blocked on QA fail
- reject path
- release transition
- manifest integrity

## Step 4 — Run required commands

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_delivery.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp10-phase6-approval-gate-and-manifest/delivery-tests.log
```

Save one representative manifest to:

- `artifacts/phase6/cp10-phase6-approval-gate-and-manifest/sample-manifest.json`

## Step 5 — Record completion and notify

Create:

- `artifacts/phase6/cp10-phase6-approval-gate-and-manifest/result.json`
- `artifacts/phase6/cp10-phase6-approval-gate-and-manifest/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp10-phase6-approval-gate-and-manifest \
  --role implementer \
  --status READY \
  --summary "CP10 complete. Approval gate and manifest-first release contract are ready." \
  --result-file artifacts/phase6/cp10-phase6-approval-gate-and-manifest/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp10-phase6-approval-gate-and-manifest/result.json
```
