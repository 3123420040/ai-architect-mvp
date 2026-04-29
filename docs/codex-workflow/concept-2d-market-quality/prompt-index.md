# AI Concept 2D Market-Quality Hardening Development Session Prompts

Status: ready

## Prompt Set

| Session | Launch lane | Branch/worktree | Canonical Prompt File |
|---|---|---|---|
| C2D0 | Bootstrap | docs main at `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp` | `session-prompts/c2d0-bootstrap-worktrees.prompt.md` |
| C2D1 | Parallel worker | `codex/concept-2d-input-style` at `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-input-style` | `session-prompts/c2d1-input-style-contract.prompt.md` |
| C2D2 | Parallel worker | `codex/concept-2d-layout-quality` at `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-layout-quality` | `session-prompts/c2d2-spatial-layout-quality.prompt.md` |
| C2D3 | Parallel worker | `codex/concept-2d-render-qa` at `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-render-qa` | `session-prompts/c2d3-drawing-craft-render-qa.prompt.md` |
| C2D4 | Parallel worker | `codex/concept-2d-review-loop` at `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-review-loop` | `session-prompts/c2d4-client-review-revision-loop.prompt.md` |
| C2D5 | Serialized closeout | `codex/concept-2d-closeout`; gate runs from API `main` | `session-prompts/c2d5-closeout-acceptance.prompt.md` |

## Workflow Root

```text
docs/codex-workflow/concept-2d-market-quality/
```

## Rework Prompt Artifacts

Rework prompts are written under:

```text
docs/codex-workflow/concept-2d-market-quality/rework-prompts/
```

Naming:

```text
c2d<N>-rework-YYYYMMDD-<short-reason>.prompt.md
```

The integrator creates these prompts after reading a final report and deciding
that the branch needs correction before merge.
