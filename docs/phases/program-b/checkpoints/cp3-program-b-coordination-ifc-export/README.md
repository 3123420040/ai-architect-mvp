# CP3 — Coordination IFC Export

**Code:** `cp3-program-b-coordination-ifc-export`
**Order:** 3
**Depends On:** `cp2-program-b-quantity-and-issue-contracts`
**Estimated Effort:** 1 day

## Objective

Generate `architectural_coordination.ifc` from the semantic coordination model and persist export validation metadata.

## Locked Slices

1. architectural-only IFC
2. selected launch property sets
3. validation metadata
4. no authoring-grade claims

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `../ai-architect-api/app/services/coordination/ifc_exporter.py` | created | Program B IFC exporter |
| `../ai-architect-api/app/services/coordination/ifc_validation.py` | created | Export validation metadata |
| `artifacts/program-b/cp3-program-b-coordination-ifc-export/result.json` | created | CP completion record |
| `artifacts/program-b/cp3-program-b-coordination-ifc-export/ifc-export-notes.md` | created | IFC mapping and limits summary |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | `architectural_coordination.ifc` can be generated from the semantic coordination model | ✓ |
| CHECK-02 | Launch entities and selected property sets are mapped intentionally | ✓ |
| CHECK-03 | Validation metadata is persisted with the bundle or export result | ✓ |
| CHECK-04 | Export contract clearly avoids authoring-grade round-trip claims | ✓ |
