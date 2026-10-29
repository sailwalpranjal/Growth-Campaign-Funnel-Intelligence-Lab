# PRD: Funnel Intelligence Lab

**Status:** Retrospective PRD, written after the build. It records what the product is for and where it stops. It is not a record of requirements gathered before coding.

## Problem

Two campaigns in a public ad dataset cost very different amounts per approved conversion: $15.81 for campaign 936 and $63.83 for campaign 1178, a 4.04x gap. The first reaction to a gap like that is usually "the media got more expensive". The data says CPM fell. Someone who has to decide what to change needs to know which part of the funnel moved, and how sure we can be.

## Target user

Primary user: me, working as a growth or product analyst on one question, "why did this metric move, and what do we test next?". The nearest real-world equivalent is a growth analyst or PM who has an ad-platform export and has to explain a cost gap to a marketing lead. I have not interviewed anyone, so I make no claim about how real teams work.

## Jobs to be done

- When a cost metric jumps between two campaigns, I want to split the gap into media cost, click appeal and post-click conversion, so I can say where to look first.
- When I find a segment that looks bad, I want to know whether it has enough data to trust, so I do not move budget on noise.
- When I propose a test, I want a hypothesis, a control, a primary metric, a guardrail and a sample size written down, so the test can be run and judged later.

## Goals

1. Reproduce every headline number from the raw CSVs, with a test per number.
2. Locate the funnel stage where the gap opens.
3. Turn findings into a prioritised, runnable experiment backlog (ICE).
4. State what the data cannot show.

## Non-goals

- CAC, ROAS, LTV or retention. The ad dataset ends at "approved conversion" and has no revenue.
- Causal claims. The three campaigns did not run as a concurrent split test.
- Real company data. Everything is public.

## User stories and acceptance criteria

| Story | Acceptance criteria |
|---|---|
| As an analyst I can see the cost gap split into three drivers. | Drivers sum to the gap with zero residual; the numbers match `tests/test_headline_numbers.py`; the page states that the split depends on the order of substitution. |
| As an analyst I can see which interest groups have enough data. | Each interest is classified at 10, 25 and 50 click thresholds; the dashboard shows the classification. |
| As a PM I can read the experiment backlog and see why each item is ranked where it is. | Each item shows impact, evidence and ease scores and the resulting ICE value; the evidence text matches recomputed data. |
| As a reader I can tell what a number rests on. | The metric dictionary lists formula, source and limitation for each metric. |

## Success metrics

Nothing here has users yet, so these measure the build, not adoption.

- North star (proposed): time from "why did this move?" to a defensible, evidence-backed next step. Not measured today.
- Input metric that is measured: headline numbers covered by recomputation tests (`tests/test_headline_numbers.py`).
- Guardrail: no number in published text that fails recomputation. CI enforces it.

See [METRICS.md](METRICS.md) for how adoption would be measured.

## Risks and open questions

- **Wrong claims survive in exported text.** This happened: the exported backlog had figures that failed recomputation. Mitigation: the recompute tests now scan the published files for the stale phrases.
- **Bridge order dependence.** Reordering the substitution moves the post-click share between 70.8% and 128.5%. An order-independent split (Shapley) gives 96.8%. Open question: which should the dashboard show by default?
- **Observational data.** The campaigns may be different phases of one rollout. Open question: is any concurrent split data available?
