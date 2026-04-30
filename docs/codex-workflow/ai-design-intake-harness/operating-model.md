# AI Design Intake Harness Operating Model

Status: tailored

## Integrator Rules

- One integrator thread receives every worker final report.
- Worker evidence is advisory until rerun on integrated local `main`.
- Rework requests must become prompt files, not loose chat instructions.
- Do not let workers self-certify phase completion.
- Do not fork worktrees from dirty API/Web baseline.

## Worktree Map

H0 should create these worktrees:

| Session | Repo | Branch | Path |
|---|---|---|---|
| H1 | API | `codex/ai-harness-trace` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-trace` |
| H2 | API | `codex/ai-harness-core` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-core` |
| H3 | API | `codex/ai-harness-readiness` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-readiness` |
| H4 | API | `codex/ai-harness-concept-input` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-concept-input` |
| H5 | API | `codex/ai-harness-style-tools` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-style-tools` |
| H6 | Web | `codex/ai-harness-ui` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/ai-harness-ui` |
| H7 | Docs | `codex/ai-harness-closeout` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/.worktrees/ai-harness-closeout` |

## Ownership Boundaries

### API workers

May edit:

- `app/services/design_harness/**`
- `app/services/llm.py`
- `app/api/v1/chat.py`
- `app/api/v1/router.py` only if adding harness endpoints
- `app/schemas.py`
- `app/models.py` and `alembic/versions/**` only in H4/H5 if snapshot tables are required
- focused API tests

Must not edit:

- professional deliverable renderers unless a harness contract test proves a required change
- generation algorithms except H4/H5 adapter boundary
- auth/security broadly
- Web files

### Web worker

May edit:

- `src/components/intake-client.tsx`
- small API typing/helper files under `src/lib/**`
- route pages only where needed for harness state/CTA

Must not edit:

- API files
- auth flow
- design renderer modules

### Docs/closeout

May edit:

- `docs/codex-workflow/ai-design-intake-harness/**`
- closeout/evidence docs

## Live/Noisy Lane Rules

- Do not run broad Docker rebuilds in worker sessions unless the prompt explicitly asks.
- H7 owns integrated Docker/browser acceptance if needed.
- LLM live provider calls are allowed only when explicitly part of a focused trace/evidence task.
- Never print or persist raw API keys.

## Integration Flow

1. Worker merges current local `main` before implementation.
2. Worker runs focused tests.
3. Worker commits locally in its worktree.
4. Integrator reviews diff and final report.
5. Integrator merges accepted branch into local `main`.
6. Rework gets a new prompt file if needed.
7. H7 reruns integrated evidence from `main`.

## Final Decision

H7 writes:

- `closeout-report.md`
- evidence summary with command results
- known gaps and product blockers
