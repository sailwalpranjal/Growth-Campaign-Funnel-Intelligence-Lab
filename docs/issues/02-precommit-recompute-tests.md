# Run the headline-number tests before every commit

**Labels:** type:chore, priority:P0, area:data

## Problem

Stale numbers reached the exported backlog and the live dashboard because the generator was fixed but the committed exports were not regenerated. CI now catches that after a push. It should also be caught before the commit exists.

## Acceptance criteria

- [ ] A `.pre-commit-config.yaml` hook runs `python -m pytest -q tests/test_headline_numbers.py`.
- [ ] `CONTRIBUTING.md` explains how to install the hook.
- [ ] The hook fails if `exports/` and `web/exports/` differ.
- [ ] The hook completes in under 15 seconds on a normal laptop (current full suite: about 5 seconds).
