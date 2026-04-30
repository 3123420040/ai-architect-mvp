# AI Design Intake Harness Prompt Index

Status: tailored

Use prompts in this order:

1. [H0 Bootstrap/Worktrees](session-prompts/h0-bootstrap-worktrees.prompt.md)
2. [H1 LLM Trace Observability](session-prompts/h1-llm-trace-observability.prompt.md)
3. [H2 Harness Core Wrapper](session-prompts/h2-harness-core-wrapper.prompt.md)
4. [H3 Readiness And Assumptions](session-prompts/h3-readiness-and-assumptions.prompt.md)
5. [H5 Style Pattern Tools](session-prompts/h5-style-pattern-tools.prompt.md)
6. [H4 Concept Input Contract](session-prompts/h4-concept-input-contract.prompt.md)
7. [H6 UI Assumption Preview Flow](session-prompts/h6-ui-assumption-preview-flow.prompt.md)
8. [H7 Evidence And Closeout](session-prompts/h7-evidence-and-closeout.prompt.md)

## Parallelism

- H1 is first and serialized.
- H2 depends on H1.
- H3 and H5 may run in parallel after H2 is accepted.
- H4 depends on H3/H5.
- H6 depends on H4 API fields.
- H7 depends on integrated H1-H6.

## Rework Prompt Naming

Use:

```text
session-prompts/h<N>-<topic>-rework-after-<decision>.prompt.md
```

Examples:

- `h1-llm-trace-rework-after-integrator-review.prompt.md`
- `h4-concept-input-rework-after-ui-contract.prompt.md`
