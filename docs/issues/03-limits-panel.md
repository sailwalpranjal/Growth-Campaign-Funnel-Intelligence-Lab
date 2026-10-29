# Add a "what this cannot tell you" panel to the Overview tab

**Labels:** type:feature, priority:P1, area:dashboard

## Problem

The limits are real and written down (`docs/limitations.md`), but a person looking at the dashboard never opens that file. The three most important ones are: the campaigns were not a concurrent split test, the bridge depends on substitution order, and CAC and ROAS are not computed.

## Acceptance criteria

- [ ] The Overview tab shows a panel with those three limits in plain language, above the fold on a 1280px-wide screen.
- [ ] Each limit links to the relevant section of `docs/limitations.md`.
- [ ] The panel does not use the words "causal" or "proves" except to say the data does not.
- [ ] The panel renders on a 375px-wide screen without horizontal scrolling.
