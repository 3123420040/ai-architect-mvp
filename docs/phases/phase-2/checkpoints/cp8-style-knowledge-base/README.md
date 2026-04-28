# CP8 — Style Knowledge Base

**Code:** cp8-style-knowledge-base
**Order:** 8
**Depends On:** cp6-integration-qa, output-quality uplift baseline
**Estimated Effort:** 1 day

## Mục tiêu

Create a versioned structured style knowledge base and seed project-pattern memory so AI can infer and apply architectural style without asking homeowners technical questions.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/professional_deliverables/style_knowledge.py` | created | Style profile schema, resolver, and default catalog |
| `../ai-architect-api/app/services/professional_deliverables/style_profiles/*.json` | created | Initial profiles: modern tropical, minimal warm, indochine soft |
| `../ai-architect-api/app/services/professional_deliverables/pattern_memory.py` | created | Pattern retrieval contract and seed patterns |
| `../ai-architect-api/tests/professional_deliverables/test_style_knowledge.py` | created | Schema, retrieval, and style-rule tests |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | Style profiles load from structured data and validate required fields | ✓ |
| CHECK-02 | Initial three styles include aliases, spatial rules, opening rules, material palette, avoid rules, and drawing rules | ✓ |
| CHECK-03 | Pattern memory can retrieve a townhouse 7x25 modern tropical pattern from sparse facts | ✓ |
| CHECK-04 | No style profile makes construction/legal/compliance claims | ✓ |
