# CP4 Validation Checklist — Handoff Package and Manifest

**For:** Validator
**Read first:** `artifacts/program-b/cp4-program-b-handoff-package-and-manifest/result.json`
**Goal:** Confirm Program B artifacts are packaged into a coherent release object with readable readiness output.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp4-program-b-handoff-package-and-manifest/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP4 — Program B handoff package and manifest",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Manifest and readiness service files exist

```bash
test -f ../ai-architect-api/app/services/coordination/manifest.py && \
test -f ../ai-architect-api/app/services/coordination/readiness.py
```

**Expected:** Required packaging services exist.
**Fail if:** Any required file is missing.

### CHECK-02: Manifest references released artifact semantics

```bash
rg -n "manifest|bundle|artifact|release|readiness|issue_register|room_schedule" \
  ../ai-architect-api/app/services/coordination/manifest.py \
  ../ai-architect-api/app/services/coordination/readiness.py
```

**Expected:** Manifest and readiness logic reference the required artifact set.
**Fail if:** Bundle semantics are incomplete.

### CHECK-03: Object storage registration is part of the bundle contract

```bash
rg -n "storage|object|signed|key|manifest_url|readiness_summary" \
  ../ai-architect-api/app/services/coordination/manifest.py \
  ../ai-architect-api/app/api/v1/coordination.py
```

**Expected:** Release assets are registered against durable storage references.
**Fail if:** Bundle relies on local-only path assumptions.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp4-program-b-handoff-package-and-manifest \
  --role validator \
  --status PASS \
  --summary "CP4 passed. Program B handoff bundle and manifest contract are validated." \
  --result-file artifacts/program-b/cp4-program-b-handoff-package-and-manifest/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp4-program-b-handoff-package-and-manifest/validation.json
```
