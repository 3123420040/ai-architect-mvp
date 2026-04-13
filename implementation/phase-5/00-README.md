# Phase 5: Brief Lock, Chat-Only Clarification, and Decision Workspace Hardening

---

## Context

Phase 5 starts from the production findings gathered after the Phase 4 intake revamp.

The product already has:

- an upgraded AI clarification baseline,
- a richer `clarification_state`,
- a Vietnamese-first intake workspace,
- and the downstream Phase 3 package/export baseline.

But production truth shows a new problem set:

- the intake page still competes with itself outside the chat box,
- the system does not express a true `brief locked` state,
- the generation lane exposes the wrong project-level sequence,
- and the `Designs` page still behaves like a technical gallery instead of a decision workspace.

## Read Order

1. `implementation/phase-3/06-status-audit-20260412.md`
2. `implementation/phase-4/01-phase-4-analysis-brief.md`
3. `implementation/phase-4/02-phase-4-implementation-detailed.md`
4. `00-README.md`
5. `01-phase-5-analysis-brief.md`
6. `02-phase-5-implementation-detailed.md`
7. `03-phase-5-checkpoint-execution-plan.md`
8. `04-phase-5-option-generation-deep-dive.md`
9. `05-phase-5-option-strategy-decision-metadata-slice.md`
10. `06-phase-5-option-strategy-technical-task-breakdown.md`
11. `docs/phases/phase-5/checkpoints/README.md`

## Core Decision

Phase 5 will not expand scope sideways.

It will harden two specific product moments:

1. the AI clarification moment, where the user should focus only on the conversation and brief lock,
2. the option decision moment, where the user should compare and choose a direction instead of browsing a gallery.

## Boundary with Earlier Phases

Phase 3 remains the package/export and issue baseline.

Phase 4 remains the baseline for:

- AI-assisted intake,
- clarification data contracts,
- and design-direction capture.

Phase 5 does not replace those foundations.

Phase 5 hardens the user-facing workflow around them:

- simplify the intake workspace into chat-first behavior,
- add a real brief-lock contract,
- correct the generation/review state machine,
- turn `Designs` into a decision workspace,
- and improve the option-generation architecture so generated options feel more intentional, differentiated, and professionally presented.
