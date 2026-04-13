# CP4 — Designs Sequence and State Correction

**Code:** cp4-designs-sequence-state
**Order:** 4
**Depends On:** cp3-conversation-quality
**Estimated Effort:** 1 day

## Objective

Correct the system sequence so generated options are not misrepresented as under review before a user actually selects one.
This checkpoint also prepares the option-generation contract so richer strategy and rationale metadata can flow downstream into the decision workspace.

## Expected Artifacts

| File/Path | Action | Description |
|-----------|--------|-------------|
| `../ai-architect-api/app/api/v1/generation.py` | updated | Correct project and version transitions |
| `../ai-architect-api/app/services/state_machine.py` | updated | Add or refine the correct sequence |
| `../ai-architect-api/app/api/v1/projects.py` | updated | Expose the corrected project state |
| `../ai-architect-web/src/components/designs-client.tsx` | updated | Remove eager generation stream behavior and render the corrected states |
| `../ai-architect-api/tests/test_flows.py` | updated | Cover generation-to-selection sequence |
| `../implementation/phase-5/04-phase-5-option-generation-deep-dive.md` | referenced | Generation sequence and metadata contract that CP4 must implement against |
| `../implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md` | referenced | Lane-specific contract for strategy payload shape and persistence |

## Checklist Validator

| ID | Description | Blocker |
|----|-------------|---------|
| CHECK-01 | Project stays in generated-options state until a version is selected | ✓ |
| CHECK-02 | Selecting an option transitions that version into review and siblings into superseded | ✓ |
| CHECK-03 | The Designs page does not open a generation stream eagerly on initial load | ✓ |
| CHECK-04 | Version payload is ready to carry richer generation metadata for CP5 | ✓ |
| CHECK-05 | Version payload shape is compatible with strategy profile and decision metadata serialization | ✓ |
