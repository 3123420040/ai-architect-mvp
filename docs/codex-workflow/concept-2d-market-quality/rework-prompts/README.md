# Rework Prompt Artifacts

The integrator writes rework prompts in this directory when a worker final
report, branch diff, or verification result is not acceptable for integration.

Naming pattern:

```text
c2d<N>-rework-YYYYMMDD-<short-reason>.prompt.md
```

Each rework prompt must include:

- source session and branch/worktree;
- accepted parts and rejected parts;
- exact requested changes;
- verification evidence required;
- final report format;
- whether the worker should continue on the same branch or create a follow-up branch.
