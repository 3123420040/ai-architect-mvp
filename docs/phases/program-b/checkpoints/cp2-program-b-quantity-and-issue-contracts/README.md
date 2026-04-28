# CP2 — Quantity and Issue Contracts

**Code:** `cp2-program-b-quantity-and-issue-contracts`
**Order:** 2
**Depends On:** `cp1-program-b-semantic-model-and-persistence`
**Estimated Effort:** 1 day

## Objective

Generate required schedule snapshots and introduce a first-class coordination issue registry with API contracts.

## Locked Slices

1. required schedule set
2. confidence and verification markers
3. issue persistence
4. schedule and issue endpoints

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `../ai-architect-api/app/services/coordination/quantity_extractor.py` | created | Schedule extraction service |
| `../ai-architect-api/app/services/coordination/issues.py` | created | Issue registry service |
| `../ai-architect-api/app/services/coordination/schedule_serializer.py` | created | Schedule artifact serializer |
| `artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/result.json` | created | CP completion record |
| `artifacts/program-b/cp2-program-b-quantity-and-issue-contracts/schedule-contract-notes.md` | created | Required schedule contract summary |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | Required schedules are generated as first-class structured resources | ✓ |
| CHECK-02 | Every schedule row exposes verification or confidence state | ✓ |
| CHECK-03 | Coordination issues are persisted and linked to version, bundle, room, or element references | ✓ |
| CHECK-04 | API can return schedule and issue resources without relying on raw file parsing only | ✓ |
