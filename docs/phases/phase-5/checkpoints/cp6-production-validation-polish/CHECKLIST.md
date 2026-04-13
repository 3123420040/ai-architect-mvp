# CP6 Validation Checklist — Production Validation and Polish

**For:** Validator Agent
**Read first:** `docs/phases/phase-5/checkpoints/cp6-production-validation-polish/result.json`
**Goal:** Confirm that the Phase 5 release candidate is validated by production truth and properly documented.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp6-production-validation-polish/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP6 — Production Validation and Polish",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Production health checks are green

```bash
curl -fsS https://kts.blackbirdzzzz.art/backend-health
```

**Expected:** Health endpoint returns success.
**Fail if:** Production is unhealthy or unreachable.

### CHECK-02: Validation artifacts exist

```bash
test -d artifacts/production-checks && test -d output/playwright
```

**Expected:** Validation artifact directories exist and contain Phase 5 evidence.
**Fail if:** Production validation is claimed but artifacts are missing.

### CHECK-03: Closure notes reference both intake and Designs validation

```bash
rg -n "intake|Designs|production" implementation/phase-5/03-phase-5-checkpoint-execution-plan.md docs/phases/phase-5/checkpoints/cp6-production-validation-polish/result.json
```

**Expected:** Final notes mention both key UX moments and production truth.
**Fail if:** Closure is asserted without evidence from both lanes.

### CHECK-04: Closure notes explicitly evaluate generation quality

```bash
rg -n "placeholder|strategy|rationale|generation quality|option quality|professional" implementation/phase-5/04-phase-5-option-generation-deep-dive.md docs/phases/phase-5/checkpoints/cp6-production-validation-polish/result.json docs/phases/phase-5/checkpoints/cp6-production-validation-polish/validation.json
```

**Expected:** Final production validation explicitly comments on generation quality against the deep-dive target.
**Fail if:** Production closure only covers deploy success and screenshots without judging option quality.

### CHECK-05: Closure notes explicitly evaluate strategy and decision metadata quality

```bash
rg -n "strategy profile|decision metadata|fit reasons|strengths|caveats|compare axes" \
  implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md \
  docs/phases/phase-5/checkpoints/cp6-production-validation-polish/result.json \
  docs/phases/phase-5/checkpoints/cp6-production-validation-polish/validation.json
```

**Expected:** Final validation notes explicitly assess whether strategy profile and decision metadata quality reached the Phase 5 target.
**Fail if:** Closure ignores the quality of explanation and only checks page stability or deploy success.

## Record Validation

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp6-production-validation-polish \
  --role validator \
  --status PASS \
  --summary "Phase 5 is production-validated and ready for closeout." \
  --result-file docs/phases/phase-5/checkpoints/cp6-production-validation-polish/validation.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp6-production-validation-polish/validation.json
```
