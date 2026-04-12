# CP3 — Frontend Shell + Auth

**Code:** cp3-frontend-shell-auth
**Order:** 3
**Depends On:** cp2-data-auth-permissions
**Estimated Effort:** 1 ngay

## Muc tieu

Dung app shell, auth pages, design tokens, query client va socket client skeleton cho frontend theo `implementation/02-tech-stack-decisions.md` va `implementation/04-implementation-directives.md`.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-web/src/app/(auth)/login/page.tsx` | created | Login page |
| `../ai-architect-web/src/app/(auth)/register/page.tsx` | created | Register page |
| `../ai-architect-web/src/components/layout/app-shell.tsx` | created | Shell chung |
| `../ai-architect-web/src/lib/api-client.ts` | created | Typed API client skeleton |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Frontend `pnpm build` pass | ✓ |
| CHECK-02 | Component tests cho `StatusBadge` va auth pages pass | ✓ |
| CHECK-03 | Auth E2E flow `Register -> Login -> Dashboard` pass | ✓ |
