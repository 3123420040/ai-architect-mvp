# C2DL0 Prompt - Bootstrap/Worktrees

Copy everything below into a new Codex chat session after the integrator
confirms this session may start.

```text
You are the Bootstrap/Worktrees Agent for AI Architect Concept 2D Live Product Integration.

Main paths:
- Docs repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
- API repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- Web repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-web

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/operating-model.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/ledger.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/21-ai-concept-2d-acceptance-report.md

Primary objective:
Create and verify the dedicated API/Web worktrees for the Concept 2D Live Product Integration phase. Do not implement product code in this session.

Required worktrees:
- C2DL1 Product Contract Adapter:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
  - branch: codex/concept-2d-live-contract
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-contract
- C2DL2 Professional Deliverables Wiring:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
  - branch: codex/concept-2d-live-deliverables
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-deliverables
- C2DL3 Review and Delivery UI Exposure:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-web
  - branch: codex/concept-2d-live-ui
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/concept-2d-live-ui
- C2DL4 Evidence and Backward Compatibility:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
  - branch: codex/concept-2d-live-evidence
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-evidence
- C2DL5 Closeout Acceptance:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
  - branch: codex/concept-2d-live-closeout
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-closeout

Hard constraints:
- Do not modify /Users/nguyenquocthong/project/ai-architect/quickchat or any unrelated repo.
- Do not push.
- Do not create PRs.
- Do not implement API/Web product code.
- Do not delete branches unless they are stale C2DL worktree registrations and the corresponding worktree path is absent or unusable.
- If API, Web, or Docs has uncommitted product changes, stop and report CURRENT_SLICE_NOT_CLEAN.

Tasks:
1. Verify API, Web, and Docs are git repos on local main.
2. Capture clean/dirty state for all three repos.
3. Prune stale git worktree registrations if needed.
4. Create all required C2DL worktrees from current local main.
5. Verify each worktree is readable and starts clean.
6. Verify each worktree can read this workflow folder.
7. Return exact branch/path mapping and launch order.

Acceptance criteria:
- All required worktrees exist.
- All required worktrees are clean.
- API/Web main remain unchanged.
- Docs workflow files remain readable.
- Final report returns CONCEPT_2D_LIVE_WORKTREES_READY only if all checks pass.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Status marker:
- CONCEPT_2D_LIVE_WORKTREES_READY | WORKTREE_NOT_READY | CURRENT_SLICE_NOT_CLEAN

Scope:
- Session: C2DL0 Bootstrap/Worktrees
- Branch/worktree:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Worktrees:
- C2DL1:
- C2DL2:
- C2DL3:
- C2DL4:
- C2DL5:

Verification:
- Commands run:
- API repo status:
- Web repo status:
- Docs repo status:
- Worktree cleanliness:

Launch order:
1.
2.
3.

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No product code changes:
- No push/PR:
- Any NEEDS_ARCHITECT_DECISION:

Known issues:
-
```
