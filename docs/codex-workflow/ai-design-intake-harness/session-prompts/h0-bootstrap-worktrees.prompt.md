# H0 Prompt - Bootstrap/Worktrees

Copy everything below into a new Codex chat session after the Integrator confirms the current API/Web/Docs baseline is clean or intentionally checkpointed.

```text
You are the AI Design Intake Harness Bootstrap/Worktrees Agent.

Docs repo:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

API repo:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Web repo:
/Users/nguyenquocthong/project/ai-architect/ai-architect-web

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/operating-model.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/ledger.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/output/ai-harness-design/01-design-intake-ai-harness.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/output/ai-harness-design/02-solution-design-current-code-agentic-os.md

Primary objective:
Create and verify dedicated worktrees for H1-H7.

Required worktrees:
- H1:
  - repo: API
  - branch: codex/ai-harness-trace
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-trace
- H2:
  - repo: API
  - branch: codex/ai-harness-core
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-core
- H3:
  - repo: API
  - branch: codex/ai-harness-readiness
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-readiness
- H4:
  - repo: API
  - branch: codex/ai-harness-concept-input
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-concept-input
- H5:
  - repo: API
  - branch: codex/ai-harness-style-tools
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-style-tools
- H6:
  - repo: Web
  - branch: codex/ai-harness-ui
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/ai-harness-ui
- H7:
  - repo: Docs
  - branch: codex/ai-harness-closeout
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/.worktrees/ai-harness-closeout

Hard constraints:
- Do not push to remote.
- Do not create PRs.
- Do not implement product code in this session.
- Do not modify /Users/nguyenquocthong/project/quickchat or any QuickChat repo.
- If API or Web has uncommitted product changes on local main, stop and report BASELINE_DIRTY_BEFORE_WORKTREES.
- If Docs has only this workflow scaffold dirty, report it but do not block unless the Integrator asked for clean docs first.

Tasks:
1. Verify each repo is a git repo and record branch/status.
2. Confirm API and Web are on local main.
3. Confirm API and Web are clean before creating worktrees.
4. Run `git worktree prune --dry-run` in API/Web/Docs and report any stale registrations.
5. Create missing worktrees from local main with the exact branch/path map above.
6. Verify every worktree exists and can read this workflow folder.
7. Verify every created worktree starts clean.
8. Return launch order and blocking notes.

Acceptance criteria:
- All required worktrees exist.
- All required branches exist.
- Worktrees are readable and clean.
- No product code changed.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Status marker:
- AI_DESIGN_INTAKE_HARNESS_WORKTREES_READY only if all required worktrees exist and are clean.

Scope:
- Session: H0 Bootstrap/Worktrees
- Docs repo:
- API repo:
- Web repo:
- Owned files changed:
- Shared files changed:

Worktrees:
- H1:
- H2:
- H3:
- H4:
- H5:
- H6:
- H7:

Verification:
- Commands run:
- API baseline status:
- Web baseline status:
- Docs baseline status:
- Worktree cleanliness:

Launch order:
-

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
