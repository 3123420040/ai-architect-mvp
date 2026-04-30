# AI Design Intake Harness Product Update

Status: tailored workflow scaffold

This workflow implements the product update described in:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/output/ai-harness-design/01-design-intake-ai-harness.md`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/output/ai-harness-design/02-solution-design-current-code-agentic-os.md`

## Phase Goal

At the end of this phase, AI Architect should have a harnessed AI intake module that can talk naturally with low-communication homeowners, propose and confirm design assumptions, persist sanitized LLM traces, and emit validated `concept_design_input_v1` JSON for downstream concept/generation workflows without weakening the existing backend modules.

## Product Principle

The AI chat must not be a single prompt wrapper.

Target shape:

```text
conversation -> harness state -> server tools -> validator/verifier -> safe brief patch
             -> assumptions/readiness -> optional concept_design_input_v1
             -> preview/generation/revision flow
```

LLM proposes. Server validates, compiles, persists, and triggers.

## Repos

- Docs: `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`
- API: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- Web: `/Users/nguyenquocthong/project/ai-architect/ai-architect-web`

## Required Precondition Before H0

API/Web/Docs local `main` should be committed or intentionally clean enough to fork worktrees from. If API or Web have uncommitted product code, H0 must stop and report:

```text
Decision: BLOCKED
Known issues: BASELINE_DIRTY_BEFORE_WORKTREES
```

Reason: worker worktrees are created from local `main`; uncommitted implementation state would be silently excluded.

## Sessions

| Session | Title | Repo | Purpose |
|---|---|---|---|
| H0 | Bootstrap/Worktrees | Docs + API/Web git metadata | Create and verify dedicated worktrees |
| H1 | LLM Trace Observability | API | Add sanitized prompt/request/response/gate trace to current intake without behavior changes |
| H2 | Harness Core Wrapper | API | Introduce `DesignIntakeHarnessLoop` while preserving existing chat API response shape |
| H3 | Readiness And Assumptions | API | Add field-level readiness matrix and homeowner-visible design assumptions |
| H4 | Concept Input Contract | API | Add `concept_design_input_v1` compiler, validator, and snapshot handoff |
| H5 | Style Pattern Tools | API | Integrate style knowledge, pattern memory, dislikes, and reference descriptors into harness tools |
| H6 | UI Assumption Preview Flow | Web | Expose harness state, assumptions, concept input readiness, and preview CTA |
| H7 | Evidence And Closeout | Docs + integrated API/Web main | Rerun integrated acceptance and close the phase |

## Launch Order

1. Run H0 only after API/Web/Docs baseline is clean or intentionally checkpointed.
2. Run H1 first.
3. Merge H1 into API `main`.
4. Run H2.
5. Merge H2 into API `main`.
6. Run H3 and H5 in parallel if H2 is accepted.
7. Merge H3 then H5 into API `main`.
8. Run H4 after H3/H5 are integrated.
9. Merge H4 into API `main`.
10. Run H6 after H4 API contract is integrated.
11. Merge H6 into Web `main`.
12. Run H7 closeout on integrated local `main`.

## Integrated-Main Rerun Gate

H7 must rerun from integrated local `main`, not from worker evidence:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_llm_intake.py tests/test_flows.py -q
PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_model_contract.py tests/test_concept_layout_generator.py tests/test_product_concept_adapter.py -q
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_ai_concept_2d_e2e.py tests/professional_deliverables/test_concept_2d_live_integration.py -q

cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Manual/browser evidence must include:

- low-communication townhouse brief;
- fuller townhouse brief with style/dislikes;
- apartment renovation brief;
- unsafe construction/permit request;
- at least one flow that emits or blocks `concept_design_input_v1` correctly.

## Output Contract

The phase returns PASS only if:

- current chat behavior remains backward-compatible;
- every LLM turn has sanitized trace evidence;
- field-level readiness and assumptions are visible in API responses;
- `concept_design_input_v1` is validated and provenance-tagged before any downstream use;
- unsafe construction/legal/MEP/geotech/code claims are blocked;
- Web exposes the harness state without requiring homeowner technical knowledge;
- integrated API/Web tests and manual product evidence pass.
