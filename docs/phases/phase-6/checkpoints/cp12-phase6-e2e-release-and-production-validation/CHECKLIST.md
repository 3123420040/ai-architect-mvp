# CP12 Validation Checklist — E2E Release and Production Validation

**For:** Validator  
**Read first:** `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/result.json`  
**Goal:** Confirm Phase 6 is proven end to end with artifact, gating, and production evidence.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp12-phase6-e2e-release-and-production-validation/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP12 — E2E Release and Production Validation",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Final evidence artifacts exist

```bash
test -f artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/mock-demo.log && \
test -f artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/production-smoke.json && \
test -f artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/closeout-report.md && \
test -d artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/screenshots
```

**Expected:** All final evidence files are present.  
**Fail if:** Any final artifact is missing.

### CHECK-02: Closeout report explicitly mentions the full Phase 6 package and approval gate

```bash
rg -n "scene\\.glb|walkthrough\\.mp4|presentation_manifest\\.json|qa_report\\.json|approval|released|preview" \
  artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/closeout-report.md
```

**Expected:** The report explicitly calls out the required package and gating behavior.  
**Fail if:** The report is vague or omits core release guarantees.

### CHECK-03: Production smoke report exists and is parseable JSON

```bash
python3 - <<'PY'
import json
from pathlib import Path
path = Path("artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/production-smoke.json")
data = json.loads(path.read_text())
assert isinstance(data, dict)
print("ok")
PY
```

**Expected:** Production smoke output is valid JSON.  
**Fail if:** The report file is missing or invalid.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp12-phase6-e2e-release-and-production-validation \
  --role validator \
  --status PASS \
  --summary "CP12 passed. Phase 6 has end-to-end and production-closeout evidence." \
  --result-file artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/validation.json
```
