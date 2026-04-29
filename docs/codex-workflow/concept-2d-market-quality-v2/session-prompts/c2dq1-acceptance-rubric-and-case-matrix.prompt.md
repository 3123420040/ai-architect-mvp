# C2DQ1 Prompt - Acceptance Rubric And Case Matrix

Copy everything below into a new Codex session only after C2DQ0 reports `C2DQ_WORKTREES_READY`.

```text
You are the C2DQ1 Acceptance Rubric And Case Matrix Agent for AI Architect Concept 2D Market Quality V2.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/.worktrees/concept-2d-market-rubric

Main project path, read-only except local git merge from main:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

API repo reference, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Required docs to read first:
- docs/codex-workflow/concept-2d-market-quality-v2/README.md
- docs/codex-workflow/concept-2d-market-quality-v2/context-and-acceptance-contract.md
- docs/codex-workflow/concept-2d-market-quality-v2/plan.md
- docs/codex-workflow/concept-2d-market-quality-v2/operating-model.md
- docs/codex-workflow/concept-2d-live-integration/fresh-full-flow-acceptance.md
- docs/codex-workflow/concept-2d-live-integration/closeout-report.md
- output/concept-2d-acceptance-audit/10-loop-findings.md, if present

Primary objective:
Turn the audit findings and product goal into a concrete market-quality acceptance rubric, a 20-case fixture matrix, and evidence templates for downstream implementation sessions.

Owned files:
- docs/codex-workflow/concept-2d-market-quality-v2/**

Read-only:
- API/Web product code.

Hard constraints:
- Do not implement product code.
- Do not weaken technical gates.
- Do not redefine the phase into construction documentation.
- Do not claim permit/code/MEP/structural/legal readiness.
- Do not push or create PRs.

Tasks:
1. Merge current local main into the worktree.
2. Read the latest audit and acceptance evidence.
3. Write a detailed market-quality rubric at:
   - docs/codex-workflow/concept-2d-market-quality-v2/market-quality-rubric.md
4. Write the 20-case matrix at:
   - docs/codex-workflow/concept-2d-market-quality-v2/20-case-matrix.md
5. Write an artifact evidence template at:
   - docs/codex-workflow/concept-2d-market-quality-v2/evidence-template.md
6. Update the ledger status for C2DQ1.
7. Commit locally:
   - Suggested message: docs(concept-2d): define market quality rubric

Acceptance criteria:
- Rubric separates homeowner readability, architect plausibility, spatial planning, drawing craft, style expression, revision usefulness, and safety.
- Case matrix covers townhouse, apartment, narrow lots, larger lots, low-communication briefs, explicit dislikes, reference descriptors, and revision cases.
- Each case has expected inputs, expected outputs, and failure signals.
- C2DQ2-C2DQ6 can execute from these docs without relying on chat history.

Verification:
- `git diff --check`
- Manual read-through of all generated docs.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DQ1 Acceptance Rubric And Case Matrix
- Branch/worktree:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Verification:
- Commands run:
- Rubric coverage:
- Case matrix coverage:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No product code changes:
- No unsafe readiness claims:
- Any NEEDS_ARCHITECT_DECISION:

Known issues:
-
```
