# CP12 — E2E Release and Production Validation

**Code:** `cp12-phase6-e2e-release-and-production-validation`  
**Order:** 12  
**Depends On:** `cp11-phase6-viewer-and-delivery-experience`  
**Estimated Effort:** 1 day

## Objective

Validate the full Phase 6 chain from approved version to released 3D presentation bundle and capture production evidence for closeout.

## Locked Slices

1. fixture-driven local e2e
2. cross-repo integration
3. short production smoke
4. screenshot pack
5. closeout report

## Interfaces and States Touched

- full bundle lifecycle
- full artifact package
- approval gate
- released delivery state
- production smoke path

## Modules and Systems in Scope

| Repo/System | File/Path | Action | Notes |
|---|---|---|---|
| mvp | `scripts/phase6_3d_mock_demo.py` | run | Baseline and fixture-driven local proof |
| mvp | `scripts/production_check_loops.py` | run | Short production smoke |
| api | `../ai-architect-api` | verify | Full backend stack |
| web | `../ai-architect-web` | verify | Full frontend experience |
| gpu | `../ai-architect-gpu` | verify | Full runtime lane |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/result.json` | created | Implementation result |
| `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/notes.md` | created | Final execution notes |
| `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/mock-demo.log` | created | Local Phase 6 demo output |
| `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/production-smoke.json` | created | Production smoke report |
| `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/screenshots/` | created | Final evidence screenshots |
| `artifacts/phase6/cp12-phase6-e2e-release-and-production-validation/closeout-report.md` | created | Final Phase 6 closeout report |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | System can produce `scene.glb + curated renders + walkthrough.mp4 + presentation_manifest.json + qa_report.json` | ✓ |
| CHECK-02 | Approval gate works and release only occurs after QA pass and architect approval | ✓ |
| CHECK-03 | Production smoke evidence is captured and attached to artifacts | ✓ |
| CHECK-04 | Final closeout report names residual risks and non-goals explicitly | ✓ |
