# CP3 — Frontend Shell + Auth

**Muc tieu:** Dung shell frontend va auth flow de FE co the dev tiep tren nen on dinh
**Requires:** CP2 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp3-frontend-shell-auth/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP3 — Frontend Shell + Auth",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Dung frontend base

Can cu:

- `implementation/02-tech-stack-decisions.md` muc `2`
- `implementation/04-implementation-directives.md` muc `2.1` -> `2.6`

Bat buoc co:

- Next.js 14 + TypeScript
- Tailwind + shadcn/ui
- Design tokens trong `globals.css`
- `AppShell`, `StatusBadge`, auth pages
- `TanStack Query` va `socket.io-client`

## Buoc 2 — Test build va auth flow

```bash
cd ../ai-architect-web
pnpm install
pnpm build
pnpm test src/components/common/__tests__/status-badge.test.tsx
pnpm exec playwright test e2e/auth-flow.spec.ts
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp3-frontend-shell-auth/result.json`.

```json
{
  "cp": "cp3-frontend-shell-auth",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Frontend shell, auth flow va base query/socket setup da co.",
  "artifacts": [
    {"file": "../ai-architect-web/src/app/(auth)/login/page.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/app/(auth)/register/page.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/components/layout/app-shell.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/lib/api-client.ts", "action": "created"}
  ],
  "issues": [],
  "notes": "Theme va status colors phai map ve design tokens, khong hardcode."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp3-frontend-shell-auth \
  --role implementer \
  --status READY \
  --summary "Frontend shell va auth flow da san sang." \
  --result-file docs/phases/phase-1/checkpoints/cp3-frontend-shell-auth/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp3-frontend-shell-auth/result.json
```
