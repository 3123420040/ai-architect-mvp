# Concept 2D Market Quality V2 Operating Model

Status: ready for bootstrap

## Core Principle

Worker sessions may prove local slice behavior, but only the integrator can accept market-quality truth after rerunning from integrated `main`.

## Branch And Worktree Map

C2DQ0 should create these from current local `main`.

| Session | Repo | Branch | Worktree |
|---|---|---|---|
| C2DQ1 | Docs | `codex/concept-2d-market-rubric` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/.worktrees/concept-2d-market-rubric` |
| C2DQ2 | API | `codex/concept-2d-market-spatial` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-spatial` |
| C2DQ3 | API | `codex/concept-2d-market-craft` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-craft` |
| C2DQ4 | API | `codex/concept-2d-market-style` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-style` |
| C2DQ5 | API | `codex/concept-2d-market-revision` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-revision` |
| C2DQ5 UI companion, only if needed | Web | `codex/concept-2d-market-review-ui` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/concept-2d-market-review-ui` |
| C2DQ6 | API | `codex/concept-2d-market-closeout` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-closeout` |

## Launch Order

1. Start `C2DQ0`.
2. Start `C2DQ1`.
3. Merge accepted `C2DQ1` into Docs `main`.
4. Start `C2DQ2`, `C2DQ3`, and `C2DQ4` in parallel.
5. Integrator reviews and merges accepted API slices in this order:
   - `C2DQ2`
   - `C2DQ3`
   - `C2DQ4`
6. Start `C2DQ5` after API slices land.
7. Start `C2DQ6` only after accepted `C2DQ1`-`C2DQ5` are integrated.

## Ownership Boundaries

- C2DQ1 owns rubric/case-matrix docs and optional evidence templates only.
- C2DQ2 owns spatial model, layout, program planning, and layout tests.
- C2DQ3 owns drawing package model, PDF/DXF rendering, drawing QA, and artifact tests.
- C2DQ4 owns style profiles, style inference/defaults, facade/elevation expression, and style tests.
- C2DQ5 owns revision interpretation/application and optional review UI exposure.
- C2DQ6 owns integrated closeout evidence only; no product code changes unless the integrator explicitly decides a blocker is a closeout bug.

## Merge Model

- No worker self-certifies integrated success.
- Every worker final report is pasted into the integrator thread.
- Integrator may reject a PASS worker report if artifacts are technically passing but not review-useful.
- Rework is captured as a new prompt file, not vague chat instructions.
- Remote push is allowed only after accepted commits are clean and no divergence exists.

## Serialized Lanes

- Fresh browser full-flow acceptance is serialized.
- Heavy Docker rebuild/full artifact generation is serialized.
- Manual architect/customer visual review evidence is serialized and belongs to C2DQ6 unless explicitly delegated.
