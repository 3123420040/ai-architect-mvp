# CP9 — QA Validator and Degraded Policy

**Objective:** Enforce release-safety checks and degraded-preview behavior.  
**Requires:** `cp8-phase6-video-lane` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp9-phase6-qa-validator-and-degraded-policy/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP9 — QA Validator and Degraded Policy",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement the QA validator

Create:

- `../ai-architect-api/app/services/presentation_3d/qa.py`

At minimum, enforce checks for:

- approved source version
- scene spec presence
- GLB existence and readability
- required still count and required room shots
- walkthrough video presence and duration window
- manifest reference integrity
- asset URL readability

## Step 2 — Implement degraded handling

Update the orchestration path so bundles can be:

- `pass`
- `warning`
- `fail`

and degraded behavior sets:

- `is_degraded`
- `degraded_reasons_json`
- `delivery_status`

without deleting existing assets.

## Step 3 — Add tests

Create:

- `../ai-architect-api/tests/test_presentation_3d_qa.py`

Cover:

- missing GLB
- missing still shot
- missing video
- invalid URL reference
- degraded-but-previewable bundle

## Step 4 — Run required commands

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_qa.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/qa-tests.log
```

Save one representative QA output to:

- `artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/sample-qa-report.json`

## Step 5 — Record completion and notify

Create:

- `artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/result.json`
- `artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp9-phase6-qa-validator-and-degraded-policy \
  --role implementer \
  --status READY \
  --summary "CP9 complete. QA validator and degraded policy are ready." \
  --result-file artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/result.json
```
