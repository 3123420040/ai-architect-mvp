# CP6 — Intake UI + Brief Editor

**Muc tieu:** Chot duoc full intake UX tren frontend
**Requires:** CP5 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp6-intake-ui-brief-editor/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP6 — Intake UI + Brief Editor",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Dung intake UI

Can cu:

- `implementation/05-checkpoints.md` muc `CP2`
- `implementation/04-implementation-directives.md` muc `2.2`, `2.3`

Implement:

- `ChatInterface`
- `IntakeForm`
- `BriefEditor`
- `BriefSummaryCard`
- mode switcher `Chat / Form`

## Buoc 2 — Test component va E2E

```bash
cd ../ai-architect-web
pnpm test src/components/chat/__tests__/chat-interface.test.tsx
pnpm test src/components/forms/__tests__/intake-form.test.tsx
pnpm test src/components/brief/__tests__/brief-editor.test.tsx
pnpm exec playwright test e2e/intake-flow.spec.ts
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp6-intake-ui-brief-editor/result.json`.

```json
{
  "cp": "cp6-intake-ui-brief-editor",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Intake chat/form UI va brief editor da san sang.",
  "artifacts": [
    {"file": "../ai-architect-web/src/components/chat/chat-interface.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/components/forms/intake-form.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/components/brief/brief-editor.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/app/projects/[id]/intake/page.tsx", "action": "created"}
  ],
  "issues": [],
  "notes": "Khong fetch data trong useEffect; dung query hooks."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp6-intake-ui-brief-editor \
  --role implementer \
  --status READY \
  --summary "Intake UI va brief editor da xong." \
  --result-file docs/phases/phase-1/checkpoints/cp6-intake-ui-brief-editor/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp6-intake-ui-brief-editor/result.json
```
