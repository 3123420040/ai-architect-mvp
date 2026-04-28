# CP4 — Handoff Package and Manifest

**Objective:** Package Program B into a releaseable handoff bundle.
**Requires:** CP3 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp4-program-b-handoff-package-and-manifest/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP4 — Program B handoff package and manifest",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement manifest and readiness builders

Create:

- `../ai-architect-api/app/services/coordination/manifest.py`
- `../ai-architect-api/app/services/coordination/readiness.py`

Manifest must include:

- bundle identity
- source version identity
- released artifact list
- issue and schedule references
- release and limitation metadata

Readiness summary must include:

- current release state
- verified vs review-required data summary
- open issue counts
- limitation notes

## Step 2 — Register bundle assets

Update Program B orchestration so bundle packaging registers:

- semantic model
- IFC
- schedules
- issue register
- manifest
- readiness summary

Use object storage keys matching Program B checkpoint root README.

## Step 3 — Add tests

Suggested command:

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest -q tests/coordination
```

## Step 4 — Record completion artifacts

Create:

- `artifacts/program-b/cp4-program-b-handoff-package-and-manifest/result.json`
- `artifacts/program-b/cp4-program-b-handoff-package-and-manifest/notes.md`
- `artifacts/program-b/cp4-program-b-handoff-package-and-manifest/bundle-contract-notes.md`

## Step 5 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp4-program-b-handoff-package-and-manifest \
  --role implementer \
  --status READY \
  --summary "CP4 complete. Program B bundle manifest and readiness summary are implemented." \
  --result-file artifacts/program-b/cp4-program-b-handoff-package-and-manifest/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp4-program-b-handoff-package-and-manifest/result.json
```
