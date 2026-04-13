# CP0 Validation Checklist — Scope Lock and Production Truth

**For:** Validator Agent
**Read first:** `docs/phases/phase-5/checkpoints/cp0-phase5-scope-truth/result.json`
**Goal:** Confirm that Phase 5 has a clear, production-backed contract before implementation starts.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp0-phase5-scope-truth/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP0 — Scope Lock and Production Truth",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Phase docs exist and are internally consistent

```bash
test -f implementation/phase-5/00-README.md && \
test -f implementation/phase-5/01-phase-5-analysis-brief.md && \
test -f implementation/phase-5/02-phase-5-implementation-detailed.md && \
test -f implementation/phase-5/03-phase-5-checkpoint-execution-plan.md && \
test -f docs/phases/phase-5/checkpoints/README.md
```

**Expected:** All phase-level files exist.
**Fail if:** Any required document is missing.

### CHECK-02: The analysis explicitly references the four production gaps

```bash
rg -n "chat|brief lock|sequence|Designs" implementation/phase-5/01-phase-5-analysis-brief.md
```

**Expected:** The analysis covers intake clutter, brief lock, sequence, and Designs UX.
**Fail if:** One or more of the four gaps are missing.

### CHECK-03: Execution plan maps one checkpoint to one deliverable boundary

```bash
rg -n "CP-5\\.[0-6]" implementation/phase-5/03-phase-5-checkpoint-execution-plan.md
```

**Expected:** CP0 through CP6 are present with distinct goals.
**Fail if:** The plan is missing checkpoints or mixes multiple milestones without boundaries.

## Record Validation

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp0-phase5-scope-truth \
  --role validator \
  --status PASS \
  --summary "Phase 5 scope is locked and grounded in production evidence." \
  --result-file docs/phases/phase-5/checkpoints/cp0-phase5-scope-truth/validation.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp0-phase5-scope-truth/validation.json
```
