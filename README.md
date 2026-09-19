# Khatabook Growth Intelligence Platform

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests Passing](https://img.shields.io/badge/tests-34+-brightgreen.svg)](tests/)
[![Live Web Dashboard](https://img.shields.io/badge/live%20dashboard-Vercel%20Ready-teal.svg)](web/)
[![Free Backend](https://img.shields.io/badge/backend%20API-Render%20Free-purple.svg)](backend/)

## The Problem
Why does scaling paid spend cause unit economics to collapse? This is the central growth diagnostic challenge. When an acquisition campaign scales from $2k to $55k, the cost per approved merchant conversion often surges 4x, destroying LTV:CAC ratios. The instinct is often to blame expensive ad inventory (CPM), but the math usually points deeper into the funnel. This platform investigates exactly where and why growth fails at scale, and provides a structured pipeline for fixing it.

## What This Platform Demonstrates
This project is an artifact of analytical thinking, data integrity, and experimentation discipline.
- **Analytical Thinking:** Decomposing complex metrics (e.g., Cost per Approved Conversion) into a 3-factor waterfall (CPM, CTR, Post-Click Conversion) to isolate the exact step causing failure.
- **Data Integrity:** Explicitly acknowledging what data we have and what we don't. We do not invent fake revenue or ROAS numbers when the dataset doesn't support it.
- **Market Research:** Synthesizing public data (RBI reports, Play Store reviews, competitor moves) into actionable strategic hypotheses.
- **Funnel Reasoning:** Analyzing consumer behavior datasets to uncover drop-offs between high-intent returning users and actual transaction completion.
- **Growth Hypothesis Generation:** Using a disciplined 5-stage Growth OS (Observe → Diagnose → Hypothesize → Experiment → Learn) rather than throwing spaghetti at the wall.

## Live Platform
- **Vercel Dashboard URL:** [https://growth-campaign-funnel-intelligence-lab.vercel.app](https://growth-campaign-funnel-intelligence-lab.vercel.app)
- **Render API URL:** [https://khatabook-growth-api.onrender.com](https://khatabook-growth-api.onrender.com)

## Analytical Methods
1. **3-Factor Efficiency Decomposition:**
   $$\text{Cost per Approved} = \left(\frac{\text{CPM}}{1000}\right) \times \left(\frac{1}{\text{CTR}}\right) \times \left(\frac{1}{\text{Click-to-Approved Rate}}\right)$$
2. **Simpson's Paradox Adjustment:** Applying mix-adjusted cost calculations to isolate true metric changes from demographic shifts.
3. **Statistical Power Analysis:** Calculating minimum detectable effect (MDE) and sample sizes required for statistically significant A/B tests.

## Data Integrity
This project relies strictly on 100% public datasets (Kaggle KAG_conversion_data, UCI Online Shoppers).
**What we compute:** Valid unit economics (Cost per Approved Conversion, CTR, CPM, Click-to-Approved Rate) backed by mathematical proofs.
**What we explicitly refuse to compute:**
- CAC (Customer Acquisition Cost): The dataset lacks downstream install, retention, and exact LTV data.
- ROAS (Return on Ad Spend): No transaction revenue exists in the ad dataset.
- Khatabook internal metrics: Everything here is derived from public proxies.

## JD Skills Evidence Map
| Skill | Evidence in Project |
|---|---|
| Analytical Problem Solving | `src/statistics.py` - 3-factor decomposition |
| Experimentation & A/B Testing | `docs/growth_os_framework.md` & `/api/hypothesis-pipeline` |
| Market & Competitor Intelligence | `docs/market_intelligence.md` & Market Intelligence Tab |
| Funnel Diagnostics | Conversion Waterfall Tab |
| Data-Driven Communication | Metric Dictionary Tab |

## Project Architecture
```text
├── backend/            # FastAPI endpoints (Market Intel, Growth OS)
├── data/               # Processed dashboard JSON and raw public data
├── docs/               # Research methodology (Market Intel, Growth OS)
├── scripts/            # Build scripts, test runners, data exporters
├── src/                # Core analytical engine (Experiment, Stats)
├── tests/              # Pytest suite
└── web/                # Vercel-ready frontend (HTML/JS)
```

## Run Locally
```bash
git clone https://github.com/sailwalpranjal/Growth-Campaign-Funnel-Intelligence-Lab.git
cd Growth-Campaign-Funnel-Intelligence-Lab
pip install -r requirements.txt
python -m pytest -q
python scripts/run_analysis.py
python backend/main.py
```

## What Would Change in Production
In a real Khatabook data infrastructure:
- Data would stream from a Snowflake/BigQuery warehouse rather than static CSVs.
- Real-time events would be ingested via Segment or Snowplow.
- We would have complete SDK attribution (AppsFlyer/Branch) linking an ad click to a specific mobile app install, allowing calculation of true CAC and LTV rather than stopping at web 'approved conversions'.
- The Growth OS pipeline would be integrated into a tool like LaunchDarkly or Optimizely for automated rollout management.
