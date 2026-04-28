# CP10 — Concept Model Contract

**Code:** cp10-concept-model-contract
**Order:** 10
**Depends On:** cp9-conversation-style-inference
**Estimated Effort:** 1 day

## Mục tiêu

Define the `ArchitecturalConceptModel` with provenance so AI-filled design decisions can become renderer-safe technical inputs.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/design_intelligence/concept_model.py` | created | Concept model dataclasses/schemas |
| `../ai-architect-api/app/services/design_intelligence/provenance.py` | created | Source/confidence/assumption tracking |
| `../ai-architect-api/tests/test_concept_model_contract.py` | created | Contract validation tests |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | Concept model represents site, levels, rooms, walls, openings, stairs, fixtures, facade, and assumptions | ✓ |
| CHECK-02 | Every AI-filled value can carry source, confidence, assumption, and explanation | ✓ |
| CHECK-03 | Missing critical site data blocks or marks assumptions explicitly | ✓ |
