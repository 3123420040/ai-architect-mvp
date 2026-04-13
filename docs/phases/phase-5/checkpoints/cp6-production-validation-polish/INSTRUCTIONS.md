# CP6 — Production Validation and Polish

**Objective:** Validate the finished Phase 5 candidate in production and close remaining UX or sequence defects.
**Requires:** CP5 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp6-production-validation-polish/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP6 — Production Validation and Polish",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Deploy candidate

Use the standard project deploy path.

Read first:

- `implementation/phase-5/04-phase-5-option-generation-deep-dive.md`
- `implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md`

Expected:

- web deployed,
- api deployed,
- health checks pass.

## Step 2 — Validate against production truth

Run at least:

- one intake validation on a real project,
- one Designs validation on a real project with generated options,
- one audit of the system sequence in logs or DB state.

The Designs validation must explicitly answer:

- do the generated options feel materially different,
- do titles and descriptions still feel placeholder-like,
- does the page now explain why one option differs from another,
- and would an end user read the output as professional,
- do strategy titles, fit reasons, strengths, and caveats feel credible and usable.

Save screenshots to `output/playwright/`.

## Step 3 — Fix final defects

Only fix issues that:

- directly violate the Phase 5 contract,
- or materially reduce the production UX quality.

For the generation lane, that includes:

- generic option naming,
- weak rationale copy,
- missing decision metadata,
- shallow or duplicated strategy profiles,
- and sequence mismatches between actual state and visible state.

Do not reopen scope into review/export/3D redesign.

## Step 4 — Record completion

Create `docs/phases/phase-5/checkpoints/cp6-production-validation-polish/result.json`.

```json
{
  "cp": "cp6-production-validation-polish",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Phase 5 candidate is deployed, production-validated, and polished.",
  "artifacts": [
    {"file": "artifacts/production-checks/", "action": "updated"},
    {"file": "output/playwright/", "action": "updated"},
    {"file": "implementation/phase-5/03-phase-5-checkpoint-execution-plan.md", "action": "updated"}
  ],
  "issues": [],
  "notes": "Production truth is the final acceptance gate for this phase, including the perceived quality of generated options and the credibility of strategy and decision metadata."
}
```

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp6-production-validation-polish \
  --role implementer \
  --status READY \
  --summary "Phase 5 candidate is deployed, production-validated, and polished." \
  --result-file docs/phases/phase-5/checkpoints/cp6-production-validation-polish/result.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp6-production-validation-polish/result.json
```
