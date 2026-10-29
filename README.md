# Growth Campaign & Funnel Intelligence Lab

[![tests](https://github.com/sailwalpranjal/Growth-Campaign-Funnel-Intelligence-Lab/actions/workflows/ci.yml/badge.svg)](https://github.com/sailwalpranjal/Growth-Campaign-Funnel-Intelligence-Lab/actions/workflows/ci.yml)
[![licence: MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)

A funnel analysis of a public ad dataset that answers one question: why did one campaign cost 4.04x more per approved conversion than another, and what should a growth team test next?

**Live dashboard:** [growth-campaign-funnel-intelligence.vercel.app](https://growth-campaign-funnel-intelligence.vercel.app) · **API docs:** [growth-intelligence-api.onrender.com/docs](https://growth-intelligence-api.onrender.com/docs)

## Who this is for, and the problem

It is for a growth analyst or product manager who has two campaigns, one number that got much worse, and a marketing lead asking why. Campaign 1178 spent $55,662.15, 19.2 times campaign 936's $2,893.37. Its cost per approved conversion went from $15.81 to $63.83. The obvious suspect is pricier ad inventory, but CPM actually fell, from $0.36 to $0.27. So where did the money go?

I built this to find out, and to turn the answer into experiments someone could run. It uses only public data. I have no access to any company's internal numbers, and nothing here should be read as describing one.

## Demo

The live dashboard has 16 tabs. The three worth opening first are Waterfall (the cost bridge), Funnel (where people drop out) and Growth OS (the experiment backlog).

> Screenshot placeholder. To capture: open the live dashboard at 1440x900, select the Waterfall tab, wait for the chart animation to finish, then save as `docs/img/waterfall.png`. For a GIF, record the tab switching Overview -> Waterfall -> Funnel -> Growth OS (about 10 seconds) with ScreenToGif at 12 fps.

## Quick start

```bash
git clone https://github.com/sailwalpranjal/Growth-Campaign-Funnel-Intelligence-Lab.git
cd Growth-Campaign-Funnel-Intelligence-Lab
pip install -r requirements.txt -r backend/requirements.txt pytest httpx

python scripts/export_reports.py      # rebuild exports/ and reports/ from the raw CSVs
python scripts/export_web_data.py     # rebuild the dashboard payload
python -m pytest -q                   # 63 tests

uvicorn backend.main:app --reload --port 8000   # API docs at /docs
python -m http.server 3000                      # dashboard at localhost:3000
```

The raw data is committed (`data/raw/`, with SHA-256 checksums in `data/raw/provenance_metadata.json`), so there is nothing to download.

## How it works

```
 raw CSV (Kaggle ad sets, UCI sessions)
        |
   SQL staging + cleaning (sql/01 .. 07)         src/data_loader.py
        |
   metrics, funnel, bridge, stability, mix       src/metrics.py, src/diagnostics.py
        |
   experiment backlog (ICE scored)               src/experiment_engine.py
        |
   exports/ + reports/ + dashboard_data.json  -> static dashboard (Vercel)
                                              -> FastAPI (Render)
```

Every rate is a ratio of sums, never an average of row-level rates. Across all 1,143 ad sets, CTR is 0.0179% (38,165 clicks over 213,434,828 impressions); averaging the rows gives 0.0164%, an 8.2% understatement.

## What it found

| Finding | Number | How it was checked |
|---|---|---|
| Cost per approved conversion, campaign 936 vs 1178 | $15.81 vs $63.83 (4.04x) | recomputed from the raw CSV in `tests/test_headline_numbers.py` |
| Share of the $48.02 gap that opens after the click | 98.1% by the sequential bridge, 96.8% by a Shapley split | same test file |
| Clicks in campaign 1178 that never became an enquiry | 92.6% | funnel tab, `exports/funnel_analysis.csv` |
| Female vs male cost per approved conversion | $69.70 vs $41.44, while female CTR is higher (0.0208% vs 0.0145%) | same test file |
| New vs returning visitors (UCI sessions) | 24.91% vs 13.93% purchase rate | same test file |

All of this is observational. I describe patterns and propose tests; I do not claim causes.

## Limits and known gaps

- **Not an A/B test.** The three campaigns did not run as a concurrent split against one audience. Campaign 1178 may simply be a later, broader phase.
- **The bridge depends on the order of substitution.** The sequential split (CPM -$3.74, CTR +$4.66, conversion +$47.10) uses the order CPM, CTR, conversion. Across all six orders the conversion share ranges from 70.8% to 128.5%. A Shapley split, which averages over orders, gives CPM -$11.08, CTR +$12.62, conversion +$46.48. Conversion is the largest driver under every ordering that I tried, but the exact percentage is not unique. Roadmap item: show both.
- **No CAC, no ROAS.** The dataset ends at an approved conversion and has no revenue. I chose not to invent any.
- **The experiment backlog is a set of proposals.** None has been run.
- **An earlier version quoted numbers that failed recomputation** (returning visitors described as converting better than new ones when the opposite is true, a gender cost gap that was off by about $1.50 on each side, and a count of "small" interests that the data does not support). They are fixed, and `tests/test_headline_numbers.py` now checks published text against the raw data.
- `docs/khatabook_growth_strategy.md` and `docs/market_intelligence.md` are background research from public sources written for a job application. I have not independently re-verified every figure in them, and the project is not affiliated with that company.

## Product thinking

How I would run this as a product, written down after the fact:

- [PRD](docs/product/PRD.md): problem, user, goals, non-goals, acceptance criteria, risks
- [Roadmap](docs/product/ROADMAP.md): Now / Next / Later with RICE and ICE arithmetic
- [Decision log](docs/product/DECISIONS.md): five decisions visible in the code
- [Metrics plan](docs/product/METRICS.md): events and queries I would add
- [Changelog](CHANGELOG.md), [project board setup](docs/project-board.md), [issue drafts](docs/issues/)

## Data sources

| Dataset | Source | Rows | Used for |
|---|---|---|---|
| `KAG_conversion_data.csv` | Kaggle, Sales Conversion Optimization | 1,143 ad sets, 3 campaigns | scorecard, bridge, audience, funnel |
| `online_shoppers_intention.csv` | UCI Machine Learning Repository, Online Shoppers Purchasing Intention | 12,330 labelled sessions | visitor and engagement diagnostics |

Licence terms are recorded in [data/README.md](data/README.md). I have not independently confirmed the Kaggle dataset's licence; check it before reusing the data.

## Deploying

The root `index.html` is the Vercel entry point and needs no build step. The API deploys to Render with the included `render.yaml`.

## Licence

MIT, see [LICENSE](LICENSE).
