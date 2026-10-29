# Generate the Growth OS block instead of preserving it

**Labels:** type:chore, priority:P1, area:data

## Problem

`scripts/export_web_data.py` copies `growth_os`, market intelligence and the metric dictionary from the previous JSON file instead of rebuilding them. The `growth_os` text for EXP-003, 004 and 005 therefore kept old numbers after the generator was corrected, and the dashboard showed them.

## Acceptance criteria

- [ ] `growth_os` is built from `src/experiment_engine.py` on every export.
- [ ] Re-running `scripts/export_web_data.py` on a clean checkout produces an identical `growth_os` block (no manual edits needed).
- [ ] `tests/test_headline_numbers.py` has a test that fails if `growth_os` text contains a number that does not appear in the recomputed data.
