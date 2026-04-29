# Concept 2D Live Product Integration Process Improvements

Status: ready for integrator launch

Keep and tailor these rules:

1. Sync with local `main` before declaring a precondition blocker.
2. Worktree evidence is advisory; the integrator reruns on integrated `main`.
3. Keep one integrator thread and paste every final report back there.
4. Use rework prompts as artifacts, not only chat corrections.
5. Separate local-env blockers from product blockers.
6. Keep any live/noisy execution lane serialized.

Additional controls for this phase:

7. Preserve selected-version geometry. A live product bundle must not silently
   regenerate a different layout from the brief.
8. Treat `Project.brief_json` and `DesignVersion.generation_metadata` as context,
   not as authority over the selected `geometry_json`.
9. Concept 2D output may be concept/schematic only. It must not claim permit,
   construction, structural, MEP, geotech, legal, or code compliance readiness.
10. Existing legacy 2D professional deliverables remain supported for geometry
    that cannot satisfy the new concept package contract.
11. UI should expose readiness truth and links; it should not mask partial,
    degraded, skipped, or failed artifacts as ready.
12. Rework prompts must name the exact failed evidence: missing sheet, wrong
    page count, stale dimension, broken link, bad readiness semantics, or
    unsupported source geometry.
