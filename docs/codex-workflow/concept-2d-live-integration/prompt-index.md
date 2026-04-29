# Concept 2D Live Product Integration Development Session Prompts

Status: ready for integrator launch

## Prompt Set

| Session | Purpose | Canonical Prompt File |
|---|---|---|
| C2DL0 | Bootstrap/Worktrees | `session-prompts/c2dl0-bootstrap-worktrees.prompt.md` |
| C2DL1 | Product Contract Adapter | `session-prompts/c2dl1-product-contract-adapter.prompt.md` |
| C2DL2 | Professional Deliverables Wiring | `session-prompts/c2dl2-professional-deliverables-wiring.prompt.md` |
| C2DL3 | Review and Delivery UI Exposure | `session-prompts/c2dl3-review-and-delivery-ui-exposure.prompt.md` |
| C2DL4 | Evidence and Backward Compatibility | `session-prompts/c2dl4-evidence-and-backward-compatibility.prompt.md` |
| C2DL5 | Closeout Acceptance | `session-prompts/c2dl5-closeout-acceptance.prompt.md` |

## Workflow Root

```text
docs/codex-workflow/concept-2d-live-integration/
```

## Launch Rule

Start with `C2DL0`. Do not launch `C2DL2` or `C2DL3` until `C2DL1` has been
reviewed, accepted, and merged into API `main`.

## Rework Prompt Naming

If a slice needs rework, create the prompt under:

```text
docs/codex-workflow/concept-2d-live-integration/rework-prompts/
```

Use this naming pattern:

```text
c2dl<N>-rework-<short-reason>.prompt.md
```
