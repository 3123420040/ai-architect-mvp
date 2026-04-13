# Phase 5 Analysis Brief

## Problem Statement

Production evidence shows four concrete gaps:

1. the intake screen still spreads attention across side suggestions, progress blocks, and duplicated summaries outside the chat,
2. the product does not express a true `brief locked` state even when the brief has been confirmed,
3. the system sequence for generated options is misleading because a project appears to enter review before an option is actually selected,
4. and the `Designs` page is still a technical option gallery with weak decision support and inconsistent UX language quality.

## Decision

Phase 5 will solve this by locking one focused product contract:

1. chat becomes the single primary clarification workspace,
2. brief lock becomes an explicit state contract across backend and frontend,
3. generation and review sequence become semantically correct,
4. and the `Designs` page becomes a decision workspace with clearer rationale, compareability, and next-step actions.

## In Scope

- remove non-essential suggestion surfaces around the intake chat,
- refine the assistant response contract so key follow-up prompts live inside the chat thread,
- add a separate brief contract state beyond `readiness`,
- expose `brief locked` explicitly in APIs and UI,
- correct project/version state transitions around generation and review,
- redesign the `Designs` page information architecture and language,
- validate the final UX against production truth and screenshots.

## Out of Scope

- new design-board capability expansion,
- image-reference ingestion,
- full review workspace redesign,
- export package redesign,
- 3D viewer redesign,
- and permit/compliance automation.

## Success Criteria

- the intake workspace no longer distracts the user with duplicated suggestion content outside the chat,
- the user can clearly distinguish `still clarifying`, `ready to lock`, and `brief locked`,
- project sequence reflects reality: generated options are not treated as under review until one is selected,
- the `Designs` page helps the user compare and choose, not just browse,
- and production validation confirms the new UX matches the intended sequence.
