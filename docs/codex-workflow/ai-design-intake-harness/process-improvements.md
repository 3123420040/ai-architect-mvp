# AI Design Intake Harness Process Improvements

Status: tailored

## Why This Workflow Exists

The product is moving from deterministic/one-shot LLM intake to a harnessed AI module. This affects API contracts, UI behavior, traceability, and downstream generation inputs. Worktree isolation and closeout evidence are required.

## Rules For Better Outcomes

1. **Trace before autonomy**
   - H1 must land before harness behavior becomes more powerful.

2. **Server validates before persistence**
   - LLM output is never trusted directly.

3. **Preserve old API shape**
   - Existing Web screens and tests should keep working during migration.

4. **Assumptions must be visible**
   - Inferred/defaulted design choices must be exposed with source, confidence, and confirmation status.

5. **No hidden construction claims**
   - Concept input and user-facing text must keep `construction_ready=false`.

6. **Worker evidence is not final**
   - H7 reruns on integrated local `main`.

7. **Prompt changes are versioned**
   - Every prompt ID must be explicit, for example `design_intake_harness_v1`.

8. **Debug artifacts are sanitized**
   - Store model, prompt id, byte counts, parsed JSON, validation gates.
   - Do not store API keys, Authorization headers, or raw secret-like values.

## Rework Routing

Use rework prompts when:

- a worker changes response shape unexpectedly;
- trace evidence leaks secrets;
- UI labels assumptions as facts;
- concept input emits despite missing critical fields;
- unsafe scope claims pass validation;
- integrated tests fail after merge.

## Evidence Rules

Every worker final report must include:

- branch/worktree;
- commit hash;
- owned/shared files changed;
- commands run;
- focused test results;
- compatibility notes;
- known gaps;
- scope compliance.

H7 must additionally include:

- integrated API commit;
- integrated Web commit;
- integrated Docs commit;
- browser/manual flow results;
- pass/needs_review/blocked decision.
