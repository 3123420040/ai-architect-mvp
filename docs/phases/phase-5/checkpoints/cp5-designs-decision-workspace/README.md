# CP5 — Designs Decision Workspace

**Code:** cp5-designs-decision-workspace
**Order:** 5
**Depends On:** cp4-designs-sequence-state
**Estimated Effort:** 1.5 days

## Objective

Turn the `Designs` page from a technical gallery into a compare-and-choose decision workspace.
This checkpoint must also make generated options feel more intentional and professional by exposing stronger naming, rationale, and strategy metadata.

## Expected Artifacts

| File/Path | Action | Description |
|-----------|--------|-------------|
| `../ai-architect-web/src/components/designs-client.tsx` | updated | Redesign page IA and option cards |
| `../ai-architect-api/app/api/v1/projects.py` | updated | Expose any missing metadata needed by the workspace |
| `../ai-architect-api/app/api/v1/generation.py` | updated | Return improved option metadata if needed |
| `../ai-architect-web/src/components/status-badge.tsx` | updated | Align page badge language with the new workspace |
| `../implementation/phase-5/04-phase-5-option-generation-deep-dive.md` | referenced | Quality target for option strategy, rationale, and presentation |
| `../implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md` | referenced | Detailed contract for titles, rationale, strengths, caveats, and metrics |

## Checklist Validator

| ID | Description | Blocker |
|----|-------------|---------|
| CHECK-01 | Designs page presents decision-support metadata, not only image thumbnails | ✓ |
| CHECK-02 | Compare mode or compare state exists for at least two options | ✓ |
| CHECK-03 | Primary CTA clearly expresses moving a chosen option into review | ✓ |
| CHECK-04 | Option title and description no longer look like raw placeholder output | ✓ |
| CHECK-05 | Strategy profile and decision metadata are rendered as first-class content, not hidden JSON | ✓ |
