# C2DL3 Prompt - Review and Delivery UI Exposure

Copy everything below into a new Codex chat session only after the integrator
accepts C2DL1. Prefer starting after C2DL2 has published the final response
contract; if started in parallel, do not merge until C2DL2 is integrated.

```text
You are the Review and Delivery UI Exposure Agent for AI Architect Concept 2D Live Product Integration.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/concept-2d-live-ui

Main Web path, read-only except local git merge from main:
/Users/nguyenquocthong/project/ai-architect/ai-architect-web

API path, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Docs path, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/operating-model.md

Primary objective:
Expose the live Concept 2D package clearly in Review and Delivery UI: readiness, PDF link, DXF/sheet links, quality report links, and partial/degraded/skipped states.

Current UI gap:
`src/components/review-client.tsx` only shows a Professional Deliverables status card/progress. It does not expose the full concept package, sheet list, quality report links, or readiness details.

Likely owned files:
- src/lib/professional-deliverables.ts
- src/components/review-client.tsx
- src/components/delivery-client.tsx
- src/components/status-badge.tsx only if needed for existing statuses
- src/lib/api-types.generated.ts only if the local workflow regenerates it cleanly

Hard constraints:
- Do not modify API.
- Do not broad redesign the app.
- Do not change auth/session behavior.
- Do not mask `partial`, `failed`, `skipped`, or degraded states as ready.
- Keep UI utilitarian and review-focused.
- Do not push or create PRs.

Tasks:
1. Merge current local Web main first: `git merge --no-edit main`.
2. Inspect current Review and Delivery components.
3. Extend Professional Deliverables client types to understand:
   - concept/package readiness;
   - asset status;
   - quality report assets;
   - PDF bundle;
   - DXF/sheet assets and metadata where provided.
4. In Review UI:
   - show concept package status clearly;
   - provide direct link to PDF bundle;
   - provide links to DXF/sheet files when present;
   - provide links to quality JSON/MD;
   - show degraded/partial/skipped reasons without scary raw logs unless expanded.
5. In Delivery UI:
   - expose the same concept package readiness and artifact links for handoff review.
6. Keep the old “create Professional Deliverables” action behavior.
7. Add or update tests if the repo has component/unit patterns. If there are no UI tests, run lint/build and document manual checking.

Verification commands:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/concept-2d-live-ui
pnpm lint
pnpm build

Optional manual UI check:
- Open Review URL after C2DL2 is integrated and Docker is rebuilt.
- Confirm the card shows the concept package links/status.

Commit locally if verification passes:
feat(concept-2d): expose live concept package evidence

Acceptance criteria:
- Review UI exposes PDF, sheet/DXF links, and quality report links when available.
- Delivery UI exposes the same readiness truth.
- Partial/degraded/skipped semantics are visible and not mislabeled as fully ready.
- Web lint/build pass.
- Worktree is clean after commit.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DL3 Review and Delivery UI Exposure
- Branch/worktree:
- Commit:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

UI coverage:
- Review package status:
- PDF link:
- DXF/sheet links:
- Quality report links:
- Partial/degraded/skipped semantics:
- Delivery UI:

Verification:
- Commands run:
- Lint/build:
- Manual UI notes, if run:

Integration notes:
- Depends on API fields:
- C2DL4 evidence needs:
- Merge risks:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No API changes:
- No auth changes:
- No push/PR:
- No false readiness claims:

Known issues:
-
```
