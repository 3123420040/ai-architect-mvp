# CP3 Validation Checklist — Coordination IFC Export

**For:** Validator
**Read first:** `artifacts/program-b/cp3-program-b-coordination-ifc-export/result.json`
**Goal:** Confirm Program B can export architectural coordination IFC before handoff packaging begins.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp3-program-b-coordination-ifc-export/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP3 — Program B coordination IFC export",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: IFC export files exist

```bash
test -f ../ai-architect-api/app/services/coordination/ifc_exporter.py && \
test -f ../ai-architect-api/app/services/coordination/ifc_validation.py
```

**Expected:** IFC exporter and validation files exist.
**Fail if:** Any required file is missing.

### CHECK-02: Export logic is explicitly architectural-only and coordination-focused

```bash
rg -n "Ifc|wall|slab|roof|opening|door|window|stair|coordination|authoring" \
  ../ai-architect-api/app/services/coordination/ifc_exporter.py \
  artifacts/program-b/cp3-program-b-coordination-ifc-export/ifc-export-notes.md
```

**Expected:** Mapping scope and limits are explicit.
**Fail if:** Export logic is vague or overclaims authoring quality.

### CHECK-03: Validation metadata is present in implementation notes or code

```bash
rg -n "validation|warning|fail|metadata|property set|property_set" \
  ../ai-architect-api/app/services/coordination/ifc_validation.py \
  ../ai-architect-api/app/services/coordination/ifc_exporter.py
```

**Expected:** Export validation is part of the contract.
**Fail if:** IFC generation exists without validation semantics.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp3-program-b-coordination-ifc-export \
  --role validator \
  --status PASS \
  --summary "CP3 passed. Program B coordination IFC export is validated." \
  --result-file artifacts/program-b/cp3-program-b-coordination-ifc-export/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp3-program-b-coordination-ifc-export/validation.json
```
