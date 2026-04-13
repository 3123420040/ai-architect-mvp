# CP5 Validation Checklist — Designs Decision Workspace

**For:** Validator Agent
**Read first:** `docs/phases/phase-5/checkpoints/cp5-designs-decision-workspace/result.json`
**Goal:** Confirm that the Designs page now supports comparison and decision-making instead of acting like a simple gallery.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp5-designs-decision-workspace/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP5 — Designs Decision Workspace",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Option cards contain decision-support content

```bash
rg -n "strength|caveat|compare|metric|review" ../ai-architect-web/src/components/designs-client.tsx
```

**Expected:** The page includes decision-support content and actions.
**Fail if:** Cards still show only image, title, and a single select button.

### CHECK-01B: Placeholder-style option copy is removed

```bash
rg -n "Phuong an .* cho|Option A|Option B|Option C" ../ai-architect-web/src/components/designs-client.tsx ../ai-architect-api/app/api/v1/generation.py ../ai-architect-api/app/api/v1/projects.py
```

**Expected:** End-user-facing option copy is no longer generic placeholder output.
**Fail if:** Raw technical placeholder labels remain the dominant user-facing copy.

### CHECK-02: Build passes

```bash
cd ../ai-architect-web && pnpm build
```

**Expected:** Build succeeds.
**Fail if:** The workspace redesign breaks the app build.

### CHECK-03: Backend payload changes are wired

```bash
rg -n "option_description|generation_metadata|geometry_summary|strategy|strength|caveat|versions" ../ai-architect-api/app/api/v1/projects.py ../ai-architect-api/app/api/v1/generation.py
```

**Expected:** The backend exposes enough metadata to drive the workspace.
**Fail if:** The frontend depends on data that the API does not supply.

### CHECK-03B: Strategy and decision metadata are explicitly referenced

```bash
rg -n "option_strategy|fit_reasons|strengths|caveats|metrics|option_title_vi|option_summary_vi" \
  ../ai-architect-web/src/components/designs-client.tsx \
  ../ai-architect-api/app/api/v1/projects.py \
  ../ai-architect-api/app/api/v1/generation.py
```

**Expected:** The decision workspace consumes structured strategy and decision metadata fields directly.
**Fail if:** The page still depends mainly on placeholder label and description fields.

## Record Validation

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp5-designs-decision-workspace \
  --role validator \
  --status PASS \
  --summary "Designs now behaves like a decision workspace instead of a raw gallery." \
  --result-file docs/phases/phase-5/checkpoints/cp5-designs-decision-workspace/validation.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp5-designs-decision-workspace/validation.json
```
