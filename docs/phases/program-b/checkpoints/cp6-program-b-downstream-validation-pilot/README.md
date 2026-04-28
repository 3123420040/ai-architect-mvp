# CP6 — Downstream Validation Pilot

**Code:** `cp6-program-b-downstream-validation-pilot`
**Order:** 6
**Depends On:** `cp5-program-b-delivery-workspace-and-status`
**Estimated Effort:** 1 day

## Objective

Validate Program B on benchmark townhouse and villa cases and capture real continuation feedback before launch.

## Locked Slices

1. benchmark bundle generation
2. downstream review evidence
3. launch-blocking defect triage
4. no launch without evidence

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/program-b/cp6-program-b-downstream-validation-pilot/result.json` | created | CP completion record |
| `artifacts/program-b/cp6-program-b-downstream-validation-pilot/benchmark-matrix.md` | created | Townhouse and villa benchmark evidence |
| `artifacts/program-b/cp6-program-b-downstream-validation-pilot/pilot-feedback.md` | created | Downstream continuation feedback |
| `artifacts/program-b/cp6-program-b-downstream-validation-pilot/blocker-list.json` | created | Launch-blocking issues list |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Benchmark townhouse and villa bundles are generated and reviewed | ✓ |
| CHECK-02 | Real downstream continuation feedback is recorded, not guessed | ✓ |
| CHECK-03 | Launch-blocking gaps are identified and ranked | ✓ |
| CHECK-04 | Team can state clearly whether Program B reduces ambiguity in practice | ✓ |
