# H6 Prompt - UI Assumption Preview Flow

Copy everything below into a new Codex chat session only after H4 is accepted and merged into API `main`.

```text
You are the UI Assumption Preview Flow Agent for AI Architect.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/ai-harness-ui

Main Web repo, read-only except local git merge from main:
/Users/nguyenquocthong/project/ai-architect/ai-architect-web

API repo, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Docs repo, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/output/ai-harness-design/02-solution-design-current-code-agentic-os.md

API contract to inspect:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/schemas.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/api/v1/chat.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/api/v1/ai_harness.py if present

Precondition:
1. Merge current local Web main: `git merge --no-edit main`.
2. Confirm API H4 contract fields are known.
3. If H4 is absent, stop and report BLOCKED_BY_PENDING_H4_CONCEPT_INPUT_CONTRACT.

Primary objective:
Improve the Web intake flow so homeowners can see AI assumptions, readiness, and next-step CTA without changing backend modules.

Owned files:
- src/components/intake-client.tsx
- src/lib/api.ts only if new helper typing is needed
- src/lib/*harness*.ts if adding a small parser/helper
- route page files only if needed

Read-only:
- API code
- auth code
- generation/review backend
- professional deliverables backend

Hard constraints:
- No API changes.
- No auth changes.
- No broad UI redesign outside intake/harness exposure.
- Do not label assumptions as confirmed facts.
- Do not expose raw prompt/provider debug to homeowner UI.
- No push/PR.

Tasks:
1. Extend Web types to tolerate optional `harness` fields from `/chat` and/or harness state endpoint.
2. In Intake UI, expose:
   - readiness status;
   - critical missing fields;
   - proposed assumptions;
   - confirmations;
   - concept input availability;
   - safe next CTA.
3. Improve CTA behavior:
   - if brief/harness is not ready, guide back to the one or two highest-value inputs;
   - if ready for confirmation, show confirm/lock CTA;
   - if concept input is ready, make next action to preview/generate clear.
4. Keep homeowner language friendly and nontechnical.
5. Keep existing technical JSON textarea under details/dev style, not primary path.
6. Add graceful fallback when API has no harness field.
7. Verify responsive layout and no text overlap.

Acceptance criteria:
- Existing intake flow still works with old response shape.
- Harness-aware response shows assumptions/readiness clearly.
- CTA after readiness moves user toward Designs/preview, not a dead end.
- No customer-facing unsafe claims.

Verification:
- `pnpm lint`
- `pnpm build`
- If local app is running, use browser/manual check on at least one project intake URL.
- `git diff --check`

Commit locally:
- Suggested message: `feat(ai-harness): expose intake assumptions in ui`

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: H6 UI Assumption Preview Flow
- Branch/worktree:
- Commit:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

UI coverage:
- Readiness:
- Assumptions:
- Confirmation:
- CTA:
- Fallback old API:
- Mobile/responsive:

Verification:
- Commands run:
- Lint/build:
- Browser/manual notes:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No API changes:
- No auth changes:
- No unsafe customer-facing claims:
- No push/PR:

Known issues:
-
```
