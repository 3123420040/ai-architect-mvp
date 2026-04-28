# CP0 — Scope Lock and Semantic Baseline

**Code:** `cp0-program-b-scope-lock-and-semantic-baseline`
**Order:** 0
**Depends On:** —
**Estimated Effort:** 0.5 day

## Objective

Freeze the exact execution contract for Program B Release 1 so the team builds a coordination-ready handoff lane instead of drifting into native BIM or generic export work.

## Locked Slices

1. launch scope
2. launch typologies
3. semantic minimum
4. release language
5. pilot thresholds

## Modules and Documents to Review

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| mvp | `implementation/program-b/01-program-b-scope-lock.md` | verify | Program B single source of truth |
| mvp | `implementation/program-b/02-program-b-requirements-detailed.md` | verify | Product contract |
| mvp | `implementation/program-b/03-program-b-technical-design-detailed.md` | verify | Technical contract |
| mvp | `implementation/program-b/04-program-b-implementation-detailed.md` | verify | Implementation slices |
| mvp | `implementation/phase-6/program-b-bim-and-construction-research-report.md` | inspect | Supporting rationale |
| api | `../ai-architect-api/app/services/exporter.py` | inspect | Current export baseline |
| api | `../ai-architect-api/app/models.py` | inspect | Current persistence baseline |
| web | `../ai-architect-web/src/components/delivery-client.tsx` | inspect | Current delivery workspace baseline |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/result.json` | created | Scope lock result record |
| `artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/notes.md` | created | Baseline findings and frozen decisions |
| `artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/decision-freeze.json` | created | Typologies, outputs, semantics, thresholds |
| `artifacts/program-b/cp0-program-b-scope-lock-and-semantic-baseline/semantic-baseline.md` | created | Current-state semantic and export gap audit |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Program B Release 1 scope is explicitly frozen to coordination-ready architectural handoff | ✓ |
| CHECK-02 | Launch typologies are explicitly frozen to `townhouse` and `villa` | ✓ |
| CHECK-03 | Required output set, semantic minimum, and release language are recorded in artifacts | ✓ |
| CHECK-04 | Pilot and launch thresholds are documented before CP1 starts | ✓ |
