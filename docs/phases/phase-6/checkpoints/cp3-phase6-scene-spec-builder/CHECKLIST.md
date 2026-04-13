# CP3 Validation Checklist — Scene Spec Builder

**For:** Validator  
**Read first:** `artifacts/phase6/cp3-phase6-scene-spec-builder/result.json`  
**Goal:** Confirm the scene spec contract is deterministic, traceable, and ready for runtime use.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp3-phase6-scene-spec-builder/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP3 — Scene Spec Builder",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Scene-spec builder modules exist

```bash
test -f ../ai-architect-api/app/services/presentation_3d/scene_spec_builder.py && \
test -f ../ai-architect-api/app/services/presentation_3d/material_mapping.py && \
test -f ../ai-architect-api/app/services/presentation_3d/shot_planner.py
```

**Expected:** All three builder modules exist.  
**Fail if:** Any builder module is missing.

### CHECK-02: Scene spec output contains shot and walkthrough structure

```bash
test -f artifacts/phase6/cp3-phase6-scene-spec-builder/sample-scene-spec.json && \
rg -n "\"still_shots\"|\"walkthrough\"|\"scene_spec_version\"|\"material\"|\"room\"" \
  artifacts/phase6/cp3-phase6-scene-spec-builder/sample-scene-spec.json
```

**Expected:** The saved sample spec contains the required structural sections.  
**Fail if:** The sample output is missing key contract sections.

### CHECK-03: Fixture-based scene-spec tests pass

```bash
test -f ../ai-architect-api/tests/test_presentation_3d_scene_spec.py && \
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_scene_spec.py -q
```

**Expected:** Determinism and failure-mode tests are green.  
**Fail if:** The test file is missing or failing.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp3-phase6-scene-spec-builder \
  --role validator \
  --status PASS \
  --summary "CP3 passed. Scene spec contract is deterministic and runtime-ready." \
  --result-file artifacts/phase6/cp3-phase6-scene-spec-builder/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp3-phase6-scene-spec-builder/validation.json
```
