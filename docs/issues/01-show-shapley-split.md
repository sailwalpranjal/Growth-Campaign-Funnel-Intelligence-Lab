# Show an order-independent split next to the sequential bridge

**Labels:** type:feature, priority:P0, area:dashboard

## Problem

The Waterfall tab shows one split of the $48.02 gap: CPM -$3.74, CTR +$4.66, conversion +$47.10. That split depends on the order the three factors are substituted. Across all six orders the conversion share runs from 70.8% to 128.5%. A reader who sees one clean number will assume it is the answer.

## Acceptance criteria

- [ ] The Waterfall tab shows the sequential split and the Shapley split (CPM -$11.08, CTR +$12.62, conversion +$46.48) side by side.
- [ ] Both columns sum to $48.02.
- [ ] A one-line note says why they differ and that the conclusion (post-click conversion is the main driver) holds in both.
- [ ] `src/diagnostics.py` exposes a function that returns the Shapley split, covered by a unit test.
- [ ] The headline test in `tests/test_headline_numbers.py` still passes.
