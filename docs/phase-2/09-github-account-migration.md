---
title: GitHub Account Migration
phase: 2
status: active-source-of-truth
date: 2026-04-27
owner: Codex Coordinator
---

# GitHub Account Migration

This document records the canonical GitHub account and remote policy for the AI Architect workspace after the 2026-04-27 migration.

## Decision

All agents working on this machine should use GitHub account:

```text
3123420040
```

The migrated repositories are public and live at:

- `https://github.com/3123420040/ai-architect-api`
- `https://github.com/3123420040/ai-architect-web`
- `https://github.com/3123420040/ai-architect-gpu`
- `https://github.com/3123420040/ai-architect-mvp`

## Local Git Configuration

Global git identity was set to:

```text
user.name=3123420040
user.email=261400952+3123420040@users.noreply.github.com
```

GitHub CLI active account was switched to:

```text
3123420040
```

## Remote Policy

For each local repo:

- `origin` points to the new `3123420040` GitHub repo.
- `old-origin` points to the previous `blackbirdzzzz365-gif` GitHub repo for reference only.

Agents should push/fetch from `origin` by default.

Agents must not push to `old-origin` unless the Product Owner explicitly requests it.

## Migration Scope

The migration pushed all committed local branches and tags from:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-web`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-gpu`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`

Default branch for all new GitHub repos is:

```text
main
```

## Important Caveat

GitHub only receives committed history.

Uncommitted local work-in-progress was intentionally left untouched and was not pushed during migration. Agents must inspect `git status` before making changes and must not revert unrelated dirty files.

Known local dirty work after migration includes:

- API Sprint 4 work-in-progress files.
- Web dirty files including existing unrelated `designs-client.tsx` and `status-badge.tsx`.
- Docs/implementation checkpoint files unrelated to the migration.

## Security Note

A quick obvious-secret scan before public migration found only placeholder/example values such as `.env.example`, `${OPENAI_COMPAT_API_KEY:-}`, and local MinIO defaults.

This was not a full historical secret audit. If the project later becomes externally sensitive, run a dedicated history scanner before broader distribution.

