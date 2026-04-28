# CP1 Validation Checklist — Semantic Model and Persistence

**For:** Validator
**Read first:** `artifacts/program-b/cp1-program-b-semantic-model-and-persistence/result.json`
**Goal:** Confirm Program B has a durable semantic backbone before schedules or IFC export are attempted.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp1-program-b-semantic-model-and-persistence/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP1 — Program B semantic model and persistence",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Core Program B semantic files exist

```bash
test -f ../ai-architect-api/app/services/coordination/semantic_model_builder.py && \
test -f ../ai-architect-api/app/services/coordination/semantic_ids.py && \
test -f artifacts/program-b/cp1-program-b-semantic-model-and-persistence/result.json
```

**Expected:** Core semantic files and CP artifact exist.
**Fail if:** Any required file is missing.

### CHECK-02: Semantic model builder and typology blocking are wired

```bash
rg -n "semantic|stable|typology|townhouse|villa|unsupported" \
  ../ai-architect-api/app/services/coordination/semantic_model_builder.py \
  ../ai-architect-api/app/api/v1/coordination.py \
  ../ai-architect-api/app/services/coordination/eligibility.py
```

**Expected:** Semantic model generation and typology checks are present.
**Fail if:** Logic is absent or generic.

### CHECK-03: Targeted coordination tests exist

```bash
find ../ai-architect-api/tests -type f | rg "coordination|semantic"
```

**Expected:** Program B semantic tests exist.
**Fail if:** No targeted tests are added.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp1-program-b-semantic-model-and-persistence \
  --role validator \
  --status PASS \
  --summary "CP1 passed. Program B semantic persistence backbone is validated." \
  --result-file artifacts/program-b/cp1-program-b-semantic-model-and-persistence/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp1-program-b-semantic-model-and-persistence/validation.json
```
