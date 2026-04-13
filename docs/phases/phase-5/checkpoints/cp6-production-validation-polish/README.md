# CP6 — Production Validation and Polish

**Code:** cp6-production-validation-polish
**Order:** 6
**Depends On:** cp5-designs-decision-workspace
**Estimated Effort:** 1 day

## Objective

Deploy the Phase 5 candidate, validate it against real production behavior, and close the last mile issues before acceptance.
This includes validating not only layout and stability, but also whether generated options feel more intentional and professional to an end user.

## Expected Artifacts

| File/Path | Action | Description |
|-----------|--------|-------------|
| `artifacts/production-checks/` | updated | Store Phase 5 validation outputs |
| `output/playwright/` | updated | Store production screenshots for intake and designs states |
| `implementation/phase-5/03-phase-5-checkpoint-execution-plan.md` | updated | Record any scope-neutral polish decisions if needed |
| `implementation/phase-5/04-phase-5-option-generation-deep-dive.md` | referenced | Final production validation must evaluate against this target |
| `implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md` | referenced | Final production validation must evaluate strategy and metadata quality against this slice |

## Checklist Validator

| ID | Description | Blocker |
|----|-------------|---------|
| CHECK-01 | Production deploy succeeds and health checks pass | ✓ |
| CHECK-02 | One real intake project and one real designs project are validated against the new UX | ✓ |
| CHECK-03 | Screenshot evidence and audit notes are saved for closure | ✓ |
| CHECK-04 | Production notes explicitly evaluate generation quality against the deep-dive target | ✓ |
| CHECK-05 | Production notes explicitly evaluate strategy profile and decision metadata quality | ✓ |
