# CP9 — Conversation Style Inference

**Code:** cp9-conversation-style-inference
**Order:** 9
**Depends On:** cp8-style-knowledge-base
**Estimated Effort:** 1 day

## Mục tiêu

Convert sparse Vietnamese homeowner conversation and optional reference-image descriptors into structured customer understanding and ranked style candidates.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/design_intelligence/customer_understanding.py` | created | CustomerUnderstanding schema and parser contract |
| `../ai-architect-api/app/services/design_intelligence/style_inference.py` | created | Style classifier over text signals and image descriptors |
| `../ai-architect-api/tests/test_design_intelligence_style_inference.py` | created | Natural-language and reference-image inference tests |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | Vietnamese sparse brief infers correct project facts and style candidates | ✓ |
| CHECK-02 | Reference-image descriptors affect style score without overriding explicit customer dislikes | ✓ |
| CHECK-03 | Low confidence returns a friendly confirmation question, not a technical survey | ✓ |
