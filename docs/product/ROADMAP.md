# Roadmap

Scores are my own judgement, not measured. I use RICE for items that touch many viewers and ICE for small internal items, and I show the arithmetic.

RICE = Reach x Impact x Confidence / Effort. Reach is a guess at viewers on a 1-10 scale, Impact is 0.25 / 0.5 / 1 / 2 / 3, Confidence is a fraction, Effort is person-weeks. ICE = (Impact + Confidence + Ease) / 3, each out of 10.

## Now

| Item | Why | Score (my judgement) |
|---|---|---|
| Show the order-independent (Shapley) split next to the sequential one on the Waterfall tab | The 98.1% headline moves between 70.8% and 128.5% with order. Showing one number hides that | RICE: 6 x 2 x 0.8 / 1 = **9.6** |
| Run the recompute tests as a pre-commit hook as well as in CI | A stale number reached the live dashboard once | ICE: (7 + 9 + 8) / 3 = **8.0** |
| Add a "what this cannot tell you" panel to the Overview tab | Limits live in docs, not where people read the numbers | ICE: (6 + 8 + 9) / 3 = **7.7** |

## Next

| Item | Why | Score (my judgement) |
|---|---|---|
| Replace the hand-maintained `growth_os` block in the dashboard JSON with content built from the code | That block went stale because the export script preserves it rather than rebuilding it | RICE: 5 x 1 x 0.8 / 2 = **2.0** |
| Add a two-proportion test with Holm correction to the audience tab | Many segments are compared with no multiple-comparison control | RICE: 4 x 1 x 0.5 / 2 = **1.0** |

## Later

| Item | Why | Score (my judgement) |
|---|---|---|
| Run one backlog experiment (EXP-GROWTH-002, landing form friction) on a real funnel | Every backlog item is a proposal; none has been run | ICE: (9 + 6 + 3) / 3 = **6.0**, held back by needing real traffic |
| Add revenue data so ROAS can be computed honestly | Would remove the biggest non-goal | Blocked on finding a dataset with revenue |
