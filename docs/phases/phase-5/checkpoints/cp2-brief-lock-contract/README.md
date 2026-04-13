# CP2 — Brief Lock Contract

**Code:** cp2-brief-lock-contract
**Order:** 2
**Depends On:** cp1-intake-chat-only-workspace
**Estimated Effort:** 1 day

## Objective

Introduce an explicit brief contract state so the product can clearly express `Draft`, `Ready to lock`, and `Brief locked`.

## Expected Artifacts

| File/Path | Action | Description |
|-----------|--------|-------------|
| `../ai-architect-api/app/services/briefing.py` | updated | Add explicit lock-state semantics beyond readiness |
| `../ai-architect-api/app/schemas.py` | updated | Expose the new brief contract state in API responses |
| `../ai-architect-api/app/api/v1/chat.py` | updated | Return unified clarification plus brief-state contract |
| `../ai-architect-api/app/api/v1/brief.py` | updated | Respect lock and reopen transitions |
| `../ai-architect-api/app/api/v1/projects.py` | updated | Expose lock state in project payloads |
| `../ai-architect-web/src/components/intake-client.tsx` | updated | Render the correct brief state labels and actions |
| `../ai-architect-api/tests/test_briefing.py` | updated | Cover lock-state behavior |

## Checklist Validator

| ID | Description | Blocker |
|----|-------------|---------|
| CHECK-01 | API exposes brief state separately from readiness | ✓ |
| CHECK-02 | Locked brief is only shown when required fields are complete and confirmed | ✓ |
| CHECK-03 | Reopen path is supported and tested | ✓ |
