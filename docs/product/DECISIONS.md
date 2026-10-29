# Decision log

Decisions I can see in the code and docs. I did not date them at the time, so I do not date them now.

## 1. Ratio-of-sums instead of averaging row-level rates

**Context.** Each row is an ad set with very different impressions. Averaging 1,143 row-level CTRs gives every tiny ad set the same weight as the biggest.
**Options.** Mean of row rates; ratio of sums; weighted mean.
**Decision.** Ratio of sums everywhere (`src/metrics.py`).
**Consequences.** Overall CTR is 0.0179% by ratio of sums and 0.0164% by row average, an 8.2% understatement. The cost is that rates cannot be recomputed from other rates alone; the sums have to be carried.

## 2. A decision matrix for the A/B calculator, not just a p-value

**Context.** A p-value under 0.05 does not mean "ship".
**Options.** Report p only; report p with a CI; map results to an action.
**Decision.** The calculator maps results to run longer, do not conclude, investigate, or promote cautiously (`src/statistics.py`).
**Consequences.** Users see an action, not just a number. The matrix thresholds are my choices and are not validated against anything.

## 3. Refuse to compute CAC and ROAS

**Context.** The ad data ends at approved conversion and has no revenue.
**Options.** Invent revenue per conversion; leave the metrics out; compute them with stated assumptions.
**Decision.** Leave them out and say so in the README and `docs/limitations.md`.
**Consequences.** A reader looking for ROAS will not find it. In exchange, nothing on the dashboard is fabricated.

## 4. Sequential substitution for the cost bridge

**Context.** Cost per approved conversion is a product of three factors, and I needed the gap split into three dollar amounts that sum to the gap.
**Options.** Sequential substitution; log-mean (LMDI) decomposition; Shapley averaging over orderings.
**Decision.** Sequential substitution in the order CPM, CTR, conversion (`src/diagnostics.py`).
**Consequences.** Zero residual and easy to explain. It is order-dependent: across all six orders the post-click share ranges from 70.8% to 128.5%, and a Shapley split gives 96.8% (`tests/test_headline_numbers.py`). This is the reason I later started `decision-pack`.

## 5. A precomputed JSON payload for the dashboard, with the API optional

**Context.** The dashboard has to load fast on a free host.
**Options.** Query the API per tab; precompute one JSON file; ship a database to the browser.
**Decision.** Precompute `data/dashboard_data.json`; the FastAPI backend serves the same data.
**Consequences.** Fast and cheap. Some blocks (`growth_os`, market intelligence) are preserved across exports instead of rebuilt, and one of them drifted out of date. Replacing that is on the roadmap.
