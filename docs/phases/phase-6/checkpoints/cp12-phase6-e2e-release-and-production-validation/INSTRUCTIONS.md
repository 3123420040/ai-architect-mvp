# CP12 — E2E Release and Production Validation

**Objective:** Prove the full Phase 6 package works end to end and capture production truth.  
**Requires:** `cp11-phase6-viewer-and-delivery-experience` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp12-phase6-e2e-release-and-production-validation/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP12 — E2E Release and Production Validation",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Run local or staging-like proof with the Phase 6 demo script

```bash
python3 scripts/phase6_3d_mock_demo.py | tee artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/mock-demo.log
```

Confirm the artifact chain and note any mismatch between current runtime and target package.

## Step 2 — Run a short production smoke

```bash
python3 scripts/production_check_loops.py \
  --loops 1 \
  --base-url https://kts.blackbirdzzzz.art \
  --host-header '' \
  --report-path artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/production-smoke.json
```

## Step 3 — Capture final screenshots

Capture desktop and mobile screenshots for:

- in-progress state
- preview state
- awaiting approval state
- released state

Save them under:

- `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/screenshots/`

## Step 4 — Write the closeout report

Create:

- `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/closeout-report.md`

The report must state:

- which required artifacts are now proven
- whether approval gating is functioning
- whether release labels and manifest are functioning
- residual risks and non-goals

## Step 5 — Record completion and notify

Create:

- `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/result.json`
- `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp12-phase6-e2e-release-and-production-validation \
  --role implementer \
  --status READY \
  --summary "CP12 complete. Phase 6 end-to-end and production validation artifacts are recorded." \
  --result-file artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/result.json
```
