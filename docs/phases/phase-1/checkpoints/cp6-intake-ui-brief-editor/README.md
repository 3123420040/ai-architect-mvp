# CP6 — Intake UI + Brief Editor

**Code:** cp6-intake-ui-brief-editor
**Order:** 6
**Depends On:** cp5-intake-brief-backend
**Estimated Effort:** 1 ngay

## Muc tieu

Hoan tat intake UX gom chat interface, form wizard, brief editor va brief summary card de user/KTS co the hoan thanh brief tren UI.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-web/src/components/chat/chat-interface.tsx` | created | Chat UI |
| `../ai-architect-web/src/components/forms/intake-form.tsx` | created | Multi-step form |
| `../ai-architect-web/src/components/brief/brief-editor.tsx` | created | Inline brief editor |
| `../ai-architect-web/src/app/projects/[id]/intake/page.tsx` | created | Intake page |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Component tests cho chat, form va brief editor pass | ✓ |
| CHECK-02 | Intake E2E flow pass | ✓ |
| CHECK-03 | Mode switcher `Chat/Form` va brief summary hoat dong dung | ✓ |
