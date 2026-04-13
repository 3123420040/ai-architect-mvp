# CP0 — Scope Lock and Baseline Audit

**Code:** `cp0-phase6-scope-lock-and-baseline-audit`  
**Order:** 0  
**Depends On:** —  
**Estimated Effort:** 0.5 day

## Objective

Freeze the exact execution contract for Phase 6 so the team builds against locked presentation-grade 3D requirements instead of assumptions.

## Locked Slices

1. baseline inventory
2. decision freeze
3. artifact naming
4. validation plan

## Interfaces and States Touched

- Release artifact set
- Frontend state labels
- Bundle and job enum model
- Object storage path convention
- Legacy coexistence rule for `derive-3d`

## Modules and Documents to Review

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| mvp | `implementation/phase-6/05-phase-6-scope-lock.md` | verify | Scope source of truth |
| mvp | `implementation/phase-6/06-phase-6-implementation-detailed.md` | verify | Product and runtime contract |
| mvp | `implementation/phase-6/07-phase-6-api-job-and-storage-contracts.md` | verify | API and storage contract |
| mvp | `implementation/phase-6/13-phase-6-technical-design-detailed.md` | verify | Technical source of truth |
| mvp | `implementation/phase-6/14-phase-6-detailed-checkpoint-breakdown.md` | verify | Sequencing baseline |
| api | `../ai-architect-api/app/api/v1/derivation.py` | inspect | Legacy sync derive behavior |
| web | `../ai-architect-web/src/components/viewer-client.tsx` | inspect | Current debug viewer baseline |
| gpu | `../ai-architect-gpu/api/server.py` | inspect | Placeholder runtime baseline |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/result.json` | created | Scope lock result record |
| `artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/notes.md` | created | Baseline findings and frozen decisions |
| `artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/mock-demo.log` | created | Output from `scripts/phase6_3d_mock_demo.py` |
| `artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/decision-freeze.json` | created | Locked shot set, video target, artifact names, state model |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Program A scope is explicitly frozen and Program B/C are explicitly excluded | ✓ |
| CHECK-02 | Required shot set, video duration, asset names, and state names are recorded in artifacts | ✓ |
| CHECK-03 | Legacy `derive-3d` coexistence policy is documented | ✓ |
| CHECK-04 | No P0 ambiguity remains for CP1 through CP12 | ✓ |
