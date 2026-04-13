# CP9 — QA Validator and Degraded Policy

**Code:** `cp9-phase6-qa-validator-and-degraded-policy`  
**Order:** 9  
**Depends On:** `cp8-phase6-video-lane`  
**Estimated Effort:** 1.5 days

## Objective

Build the release-safety QA layer and degraded-preview policy so incomplete bundles remain visible internally but are blocked from delivery.

## Locked Slices

1. required artifact checks
2. URL integrity checks
3. video, still, and GLB completeness
4. degraded reason assignment
5. bundle QA state update

## Interfaces and States Touched

- `qa_report.json`
- bundle `qa_status`
- bundle `delivery_status`
- bundle `is_degraded`
- `degraded_reasons_json`

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| api | `../ai-architect-api/app/services/presentation_3d/qa.py` | created | Blocking and warning checks |
| api | `../ai-architect-api/app/services/presentation_3d/orchestrator.py` | updated | QA invocation and state update |
| api | `../ai-architect-api/tests/test_presentation_3d_qa.py` | created | QA and degraded tests |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/result.json` | created | Implementation result |
| `artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/notes.md` | created | QA policy notes |
| `artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/qa-tests.log` | created | QA test output |
| `artifacts/phase6/cp9-phase6-qa-validator-and-degraded-policy/sample-qa-report.json` | created | Representative QA report |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Missing blocking artifacts force `qa_status=fail` and `delivery_status=preview_only` or `blocked` | ✓ |
| CHECK-02 | Successful bundles produce deterministic `pass` or `warning` QA output with reason lists | ✓ |
| CHECK-03 | Degraded bundles remain internally visible but cannot be client-released | ✓ |
| CHECK-04 | QA checks are rule-based and explicit, not aesthetic guesswork | ✓ |
