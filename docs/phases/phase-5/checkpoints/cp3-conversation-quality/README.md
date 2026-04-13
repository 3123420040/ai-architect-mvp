# CP3 — Conversation Quality Hardening

**Code:** cp3-conversation-quality
**Order:** 3
**Depends On:** cp2-brief-lock-contract
**Estimated Effort:** 1 day

## Objective

Make AI clarification turns feel more tactful, better prioritized, and cleaner to read.

## Expected Artifacts

| File/Path | Action | Description |
|-----------|--------|-------------|
| `../ai-architect-api/app/services/briefing.py` | updated | Better assistant payload and follow-up prioritization |
| `../ai-architect-api/app/services/llm.py` | updated | Safer conversation turn generation and formatting |
| `../ai-architect-web/src/components/intake-client.tsx` | updated | Better chat rendering and quick-reply placement |
| `../ai-architect-api/tests/test_briefing.py` | updated | Add tricky transcript cases |

## Checklist Validator

| ID | Description | Blocker |
|----|-------------|---------|
| CHECK-01 | Assistant turns prioritize one or two high-value follow-up asks instead of broad generic prompts | ✓ |
| CHECK-02 | Chat formatting is structured and easy to scan | ✓ |
| CHECK-03 | Transcript fixtures cover conflict, context switch, and incomplete-budget cases | ✓ |
