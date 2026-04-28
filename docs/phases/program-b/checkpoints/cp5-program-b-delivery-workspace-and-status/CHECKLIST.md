# CP5 Validation Checklist — Delivery Workspace and Status

**For:** Validator
**Read first:** `artifacts/program-b/cp5-program-b-delivery-workspace-and-status/result.json`
**Goal:** Confirm Program B value is visible in the delivery workspace and not hidden behind file downloads only.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp5-program-b-delivery-workspace-and-status/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP5 — Program B delivery workspace and status",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Program B frontend files exist

```bash
test -f ../ai-architect-web/src/components/coordination-handoff.tsx && \
test -f ../ai-architect-web/src/lib/coordination.ts
```

**Expected:** Program B frontend files exist.
**Fail if:** Any required file is missing.

### CHECK-02: UI includes readiness, schedule, and issue concepts

```bash
rg -n "readiness|schedule|issue|release|coordination" \
  ../ai-architect-web/src/components/coordination-handoff.tsx \
  ../ai-architect-web/src/components/delivery-client.tsx
```

**Expected:** UI concepts are represented explicitly.
**Fail if:** Program B is still only raw asset links.

### CHECK-03: User-facing copy avoids misleading authoring claims

```bash
rg -n "authoring|editable BIM|construction-ready|Revit" \
  ../ai-architect-web/src/components/coordination-handoff.tsx \
  artifacts/program-b/cp5-program-b-delivery-workspace-and-status/ui-notes.md
```

**Expected:** Either no misleading terms appear, or notes explicitly explain safe wording.
**Fail if:** Copy overclaims Program B capability.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp5-program-b-delivery-workspace-and-status \
  --role validator \
  --status PASS \
  --summary "CP5 passed. Program B delivery workspace and status UX are validated." \
  --result-file artifacts/program-b/cp5-program-b-delivery-workspace-and-status/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp5-program-b-delivery-workspace-and-status/validation.json
```
