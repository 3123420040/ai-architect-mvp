# CP10 — Approval Gate and Manifest

**Code:** `cp10-phase6-approval-gate-and-manifest`  
**Order:** 10  
**Depends On:** `cp9-phase6-qa-validator-and-degraded-policy`  
**Estimated Effort:** 1.5 days

## Objective

Make manifest generation and architect approval the release contract for all Phase 6 client delivery behavior.

## Locked Slices

1. manifest builder
2. approval endpoints
3. approval notes persistence
4. release-state transition
5. download entitlement rules

## Interfaces and States Touched

- `presentation_manifest.json`
- bundle `approval_status`
- bundle `delivery_status`
- approval notes
- approval and rejection endpoints

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| api | `../ai-architect-api/app/services/presentation_3d/manifest.py` | created | Manifest-first release contract |
| api | `../ai-architect-api/app/api/v1/presentation_3d.py` | updated | Approve and reject endpoints |
| api | `../ai-architect-api/tests/test_presentation_3d_delivery.py` | created | Approval and release gating tests |
| web | `../ai-architect-web/src/lib/presentation-3d.ts` | updated | Manifest and approval payload consumption |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp10-phase6-approval-gate-and-manifest/result.json` | created | Implementation result |
| `artifacts/phase6/cp10-phase6-approval-gate-and-manifest/notes.md` | created | Manifest and release notes |
| `artifacts/phase6/cp10-phase6-approval-gate-and-manifest/delivery-tests.log` | created | Approval/delivery test output |
| `artifacts/phase6/cp10-phase6-approval-gate-and-manifest/sample-manifest.json` | created | Representative manifest |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Approval is impossible when QA is `fail` or required assets are missing | ✓ |
| CHECK-02 | Release is impossible before explicit architect approval | ✓ |
| CHECK-03 | Manifest contains approval, QA, delivery, asset, branding, and disclaimer sections | ✓ |
| CHECK-04 | Viewer and delivery code can read release truth from manifest-first data | ✓ |
