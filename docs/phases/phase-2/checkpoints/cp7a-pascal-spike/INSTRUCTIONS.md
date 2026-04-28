# CP7.A — Instructions

## Buoc 0 — Notify start

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7a-pascal-spike/status" \
  -H "Content-Type: application/json" \
  -d '{"role":"implementer","status":"IN_PROGRESS","summary":"CP7.A spike start","readyForNextTrigger":false}' || true
```

## Buoc 1 — Vendor Pascal

```bash
cd ../ai-architect-web
# Chon pin commit upstream moi nhat khi bat dau
export PASCAL_SHA=<SHA>

git submodule add https://github.com/pascalorg/editor packages/pascal-editor
cd packages/pascal-editor && git checkout $PASCAL_SHA && cd -

# Cap nhat pnpm-workspace.yaml neu chua declare packages/*
```

Neu Pascal la Next.js standalone app (khong phai library), chon 1 trong 2:

- Extract editor core sang folder `packages/pascal-editor/editor-core`, re-export (uu tien neu thoi gian cho phep)
- Hoac fork noi bo, xoa Next app shell, giu scene graph + components

Document lua chon vao spike report.

## Buoc 2 — Workspace wiring

- Cap nhat `ai-architect-web/package.json` them `"pascal-editor": "workspace:*"` neu can expose name.
- Build thu `pnpm install && pnpm build` — fix compat issue (peer deps React 19, three.js version).
- Neu co conflict React duplicated, set `peerDependencies` trong Pascal package.

## Buoc 3 — Lab route

Tao `src/app/lab/pascal/page.tsx`:

```tsx
// NOTE: Next.js 16 — doc node_modules/next/dist/docs/ de confirm App Router convention
import dynamic from "next/dynamic";

const PascalEditor = dynamic(
  () => import("pascal-editor").then((m) => m.Editor),
  { ssr: false }
);

export default function PascalLabPage() {
  return (
    <main className="h-screen">
      <PascalEditor />
    </main>
  );
}
```

Chay `pnpm dev`, mo `/lab/pascal`, xac nhan render.

## Buoc 4 — Browser matrix

Mo `/lab/pascal` tren 4 browser, ghi nhan:

| Browser | Version | WebGPU | Render? | Note |
|---------|---------|--------|---------|------|
| Chrome | stable | ✓/✗ | ✓/✗ | |
| Edge | stable | | | |
| Safari | 17+ | | | |
| Firefox | 120+ | | | |

Neu Safari/Firefox fail → document fallback strategy (se lam tai CP7.C).

## Buoc 5 — Bundle measurement

```bash
cd ../ai-architect-web && pnpm build
# Doc output .next/analyze hoac dung @next/bundle-analyzer
```

Ghi size route `/lab/pascal` vao spike report.

## Buoc 6 — Spike report

Tao `docs/phase-1/23-pascal-spike-report.md` voi sections:

1. Vendor strategy (submodule / fork / extract)
2. Build fix applied
3. Browser matrix (bang tren)
4. Bundle size + budget proposal
5. SSR pitfalls (dynamic import, WebGPU availability, zustand hydration)
6. Recommendation di tiep CP7.B hoac pivot

## Buoc 7 — NOTICE + LICENSE

```bash
# Giu LICENSE upstream tai packages/pascal-editor/LICENSE
test -f ../ai-architect-web/packages/pascal-editor/LICENSE || echo "Missing LICENSE"

# Them entry vao ../ai-architect-web/NOTICE
```

## Buoc 8 — Result

Tao `result.json`:

```json
{
  "cp": "cp7a-pascal-spike",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Pascal vendored, lab route mount OK, spike report hoan tat",
  "artifacts": [
    {"file":"../ai-architect-web/packages/pascal-editor","action":"submodule"},
    {"file":"../ai-architect-web/src/app/lab/pascal/page.tsx","action":"created"},
    {"file":"docs/phase-1/23-pascal-spike-report.md","action":"created"}
  ],
  "notes": "Xem recommendation o cuoi spike report truoc khi trigger CP7.B"
}
```

```bash
uv run python docs/phases/phase-2/checkpoints/notify.py \
  --cp cp7a-pascal-spike --role implementer --status READY \
  --summary "Spike done" \
  --result-file docs/phases/phase-2/checkpoints/cp7a-pascal-spike/result.json
```
