# CP1 — Intake Chat-Only Workspace

**Code:** cp1-intake-chat-only-workspace
**Order:** 1
**Depends On:** cp0-phase5-scope-truth
**Estimated Effort:** 1 day

## Objective

Simplify the intake experience so the AI conversation becomes the single primary workspace and external suggestion clutter is removed.

## Expected Artifacts

| File/Path | Action | Description |
|-----------|--------|-------------|
| `../ai-architect-web/src/components/intake-client.tsx` | updated | Remove external suggestion-heavy surfaces and refocus layout on the chat |
| `../ai-architect-web/src/components/app-shell.tsx` | updated | Support a cleaner workspace header if needed |
| `../ai-architect-web/src/components/status-badge.tsx` | updated | Keep compact supporting status language |

## Checklist Validator

| ID | Description | Blocker |
|----|-------------|---------|
| CHECK-01 | Intake no longer shows large suggestion blocks outside the chat thread | ✓ |
| CHECK-02 | Header and support chrome are compact and do not compete with the conversation | ✓ |
| CHECK-03 | Web build passes after the layout simplification | ✓ |
