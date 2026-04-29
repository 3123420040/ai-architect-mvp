# C2DQ0 Prompt - Bootstrap/Worktrees

Copy everything below into a new Codex session after the integrator confirms the pushed baseline is available on `origin/main`.

```text
You are the C2DQ0 Bootstrap/Worktrees Agent for AI Architect Concept 2D Market Quality V2.

Main project path:
/Users/nguyenquocthong/project/ai-architect

Repos:
- API: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- Web: /Users/nguyenquocthong/project/ai-architect/ai-architect-web
- Docs: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/context-and-acceptance-contract.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/operating-model.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/ledger.md

Primary objective:
Create and verify the dedicated C2DQ worktrees from current local `main`.

Required worktrees:
- C2DQ1 Docs rubric:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
  - branch: codex/concept-2d-market-rubric
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/.worktrees/concept-2d-market-rubric
- C2DQ2 API spatial planning:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
  - branch: codex/concept-2d-market-spatial
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-spatial
- C2DQ3 API drawing craft:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
  - branch: codex/concept-2d-market-craft
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-craft
- C2DQ4 API style/facade:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
  - branch: codex/concept-2d-market-style
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-style
- C2DQ5 API revision loop:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
  - branch: codex/concept-2d-market-revision
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-revision
- C2DQ5 optional Web UI companion:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-web
  - branch: codex/concept-2d-market-review-ui
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/concept-2d-market-review-ui
- C2DQ6 API closeout:
  - repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
  - branch: codex/concept-2d-market-closeout
  - path: /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-closeout

Hard constraints:
- Do not modify /Users/nguyenquocthong/project/quickchat or QuickChat repos.
- Do not push.
- Do not create PRs.
- Do not implement product changes.
- Do not run heavy generation in this bootstrap session.

Preconditions:
1. Confirm each repo is on `main`.
2. Confirm each repo is clean or report the dirty files.
3. Fetch `origin main`.
4. If any repo diverges from origin, stop and report:
   - Decision: BLOCKED
   - Known issues: BLOCKED_BY_REMOTE_DIVERGENCE

Tasks:
1. Inspect current worktrees and prune stale registrations if needed.
2. Create the required worktrees from local `main`.
3. Verify each worktree starts clean.
4. Verify each worktree can read this workflow folder.
5. Return the exact branch/path mapping.

Return status marker:
C2DQ_WORKTREES_READY

Final report format:
Decision: PASS | BLOCKED

Scope:
- Session: C2DQ0 Bootstrap/Worktrees
- Repos inspected:
- Worktrees created:
- Shared files changed:

Verification:
- Commands run:
- API main status:
- Web main status:
- Docs main status:
- Worktree cleanliness:

Residual risk:
- Flakes:
- Known gaps:

Known issues:
-
```
