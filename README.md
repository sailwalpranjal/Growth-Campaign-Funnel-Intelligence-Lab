# Khatabook Growth Intelligence Platform

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests Passing](https://img.shields.io/badge/tests-44%20passed-brightgreen.svg)](tests/)
[![Data Integrity](https://img.shields.io/badge/data%20provenance-100%25%20real%20public-orange.svg)](data/)
[![Live Dashboard](https://img.shields.io/badge/live%20dashboard-Vercel-teal.svg)](https://growth-campaign-funnel-intelligence-lab.vercel.app)
[![API](https://img.shields.io/badge/backend%20API-Render%20Free-purple.svg)](https://growth-intelligence-api.onrender.com)

---

## The Problem

When an acquisition campaign scales 19x in spend, why does cost per approved conversion sometimes surge 4x — even as CPM actually improves? The instinct is to blame expensive ad inventory. But a 3-factor mathematical decomposition points elsewhere: the CPM lever improved, the CTR lever partially degraded, and the post-click conversion rate collapsed by 73.8%. That single lever accounts for 98.1% of the entire cost explosion.

This is a real diagnostic question every growth team faces. This platform investigates exactly where and why growth fails at scale, and provides a structured evidence-to-hypothesis-to-experiment pipeline for fixing it — using 100% real public data, no synthetic metrics, and no fabricated Khatabook internal numbers.

**Live Platform:** [growth-campaign-funnel-intelligence-lab.vercel.app](https://growth-campaign-funnel-intelligence-lab.vercel.app)  
**API Docs:** [growth-intelligence-api.onrender.com/docs](https://growth-intelligence-api.onrender.com/docs)

---

## What This Platform Demonstrates

This is not a feature showcase. Every component exists because it answers a question a Growth Manager would actually ask.

| Capability | What the platform does | Why it matters |
|:---|:---|:---|
| **Numerical reasoning** | 3-factor sequential substitution bridge decomposing a $48.02 cost gap into CPM (-$3.74), CTR (+$4.66), and conversion effect (+$47.10) with zero reconciliation residual | Shows ability to isolate causation, not just correlation |
| **Funnel analysis** | Multi-stage funnel (Impression → Click → Enquiry → Approved) with stage-level conversion rates and 92.6% post-click drop-off identified | Precisely locates where the acquisition funnel breaks |
| **Audience segmentation** | Interest-group analysis with sensitivity classification at 10, 25, and 50-click thresholds — distinguishing stable segments from sample-fragile noise | Prevents budget misallocation to statistically unreliable segments |
| **Mix-adjusted analysis** | Direct standardization comparing raw vs. benchmark-weighted campaign performance to isolate demographic confounding from true efficiency gaps | Controls for the audience composition effect that creates apparent-but-false campaign performance differences |
| **Experimentation thinking** | 5-experiment ICE-prioritized backlog derived directly from real empirical findings — not generic ideas | Demonstrates ability to translate data anomalies into structured, testable hypotheses |
| **Statistical rigor** | Two-proportion z-test with two-tailed p-values, 95% CIs, sample size planning, and a disciplined decision matrix that distinguishes statistical from practical significance | Shows understanding that p < 0.05 does not automatically mean "ship the variant" |
| **Market research** | Competitor matrix (Khatabook vs Vyapar vs OkCredit vs BharatPe vs PhonePe), MSME landscape sourced from public reports, app store signal analysis | Demonstrates ability to frame analytical findings in broader business context |
| **Data quality** | 11-check automated audit flagging missing values, zero-click spend anomalies, funnel logic violations, and sample reliability | Shows attention to data hygiene before any analysis is run |
| **Growth OS pipeline** | 5-stage workflow (Observe → Diagnose → Hypothesize → Experiment → Learn) mapping each experiment across its full lifecycle | Demonstrates structured growth thinking, not ad hoc decision-making |
| **Analytical transparency** | Every metric shows formula, data source, confidence level, and honest limitation — via info panels and a searchable Metric Dictionary | Proves understanding of what the data can and cannot prove |

---

## Data Integrity Statement

### What we compute (with legitimate basis)

- **CTR** = SUM(Clicks) / SUM(Impressions) — ratio-of-sums, not row-averaging
- **CPM** = (SUM(Spent) / SUM(Impressions)) × 1000
- **CPC** = SUM(Spent) / SUM(Clicks)
- **Cost per Approved Conversion** = SUM(Spent) / SUM(Approved_Conversion)
- **Click-to-Approved Rate** = SUM(Approved_Conversion) / SUM(Clicks)
- All efficiency decomposition, mix adjustment, and segment stability metrics derived from the above

### What we explicitly refuse to compute and why

| Metric | Why we don't compute it |
|:---|:---|
| **CAC (Customer Acquisition Cost)** | Requires full blended spend (including organic, agency fees), downstream install attribution, and post-activation retention data. This dataset ends at approved conversion. |
| **ROAS (Return on Ad Spend)** | No transaction revenue exists in this ad dataset. Creating synthetic revenue numbers would be fabrication, not analysis. |
| **Mobile installs / DAU** | This is a web conversion dataset. No SDK-level mobile attribution exists. |
| **Real Khatabook internal metrics** | This platform uses 100% public datasets. No confidential company data is implied, inferred, or fabricated. |

---

## Analytical Methods

### 1. Three-Factor Efficiency Decomposition Bridge

$$\text{Cost per Approved} = \underbrace{\frac{\text{Spend}}{\text{Impressions}}}_{L_1: \text{CPM}/1000} \times \underbrace{\frac{\text{Impressions}}{\text{Clicks}}}_{L_2: 1/\text{CTR}} \times \underbrace{\frac{\text{Clicks}}{\text{Approved}}}_{L_3: 1/\text{Conv Rate}}$$

Sequential substitution attribution ensures every dollar of cost gap is mathematically accounted for with zero residual. See [`src/diagnostics.py`](src/diagnostics.py) and [`docs/methodology.md`](docs/methodology.md) for full derivation.

### 2. Direct Standardization (Audience Mix Adjustment)

$$\text{AdjCost}_c = \sum_{s \in S} w_s \cdot \text{Cost}_{c, s}, \quad w_s = \frac{\sum_{c} \text{Clicks}_{c,s}}{\sum_{c} \text{Clicks}_c}$$

Answers: "If both campaigns faced identical audience weights, would the efficiency gap persist?" It does — ruling out demographic composition as the confound. See [`src/diagnostics.py`](src/diagnostics.py).

### 3. Two-Proportion Z-Test with Disciplined Decision Matrix

$$z = \frac{p_2 - p_1}{SE_\text{pool}}, \quad SE_\text{pool} = \sqrt{p_\text{pool}(1-p_\text{pool})\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}$$

The decision matrix distinguishes: Run longer (underpowered) / Do not conclude (null) / Investigate (wide CI) / Promote cautiously (significant + practical + CI > 0). See [`src/statistics.py`](src/statistics.py).

### 4. Ratio-of-Sums Aggregation

All conversion rates use SUM(numerator) / SUM(denominator) across rows — never the average of row-level rates. This prevents row-averaging bias and Simpson's paradox. See [`src/metrics.py`](src/metrics.py).

### 5. ICE Prioritization

$$\text{ICE Score} = \frac{\text{Impact} + \text{Evidence} + \text{Ease}}{3}, \quad \text{each } \in [1, 10]$$

Used to rank experiment proposals derived from real data findings. Impact is opportunity size, Evidence is empirical support quality, Ease is implementation effort (inverted). See [`src/experiment_engine.py`](src/experiment_engine.py).

---

## JD Skills Evidence Map

| Khatabook JD Requirement | How it is demonstrated | Key file |
|:---|:---|:---|
| Campaign performance & spend analysis | Ratio-of-sums scorecard: impressions, clicks, spend, CTR, CPC, CPM across 3 campaigns | [`src/metrics.py`](src/metrics.py) / [`sql/03_metrics.sql`](sql/03_metrics.sql) |
| Investigate why a metric changed | 3-factor waterfall bridge isolating CPM, CTR, and conversion rate contributions | [`src/diagnostics.py`](src/diagnostics.py) / Waterfall tab |
| Acquisition funnel & drop-off analysis | Multi-stage funnel (Impression→Click→Enquiry→Approved) with stage conversion rates | [`sql/06_funnel.sql`](sql/06_funnel.sql) / Funnel tab |
| Audience segmentation & stability | Age, gender, interest breakdown with 10/25/50-click threshold sensitivity classification | [`sql/04_audience.sql`](sql/04_audience.sql) / Audience Matrix tab |
| Audience mix adjustment | Direct standardization isolating composition effect from rate effect | [`sql/05_mix_analysis.sql`](sql/05_mix_analysis.sql) / Mix tab |
| Growth experimentation & hypothesis | Evidence-to-hypothesis pipeline with ICE scoring, control/variant, KPIs, guardrails | [`src/experiment_engine.py`](src/experiment_engine.py) / Growth OS tab |
| A/B testing & sample-size planning | Two-proportion z-test with p-values, 95% CIs, power-based sample sizing | [`src/statistics.py`](src/statistics.py) / A/B Lab tab |
| Dashboard & reporting | Interactive dark-mode Growth Intelligence Platform on Vercel | [`web/index.html`](web/index.html) / [`web/js/dashboard.js`](web/js/dashboard.js) |
| Data quality & attention to detail | 11-check automated audit: missing values, zero-click spend, funnel logic violations, sample reliability | [`src/validation.py`](src/validation.py) / Audit Daemon tab |
| Consumer behavior analysis | UCI session diagnostic (visitor type, traffic channel, bounce/exit rates, engagement tiers) | [`src/diagnostics.py`](src/diagnostics.py) / Consumer Sessions tab |
| Competitor & market research | Competitor matrix (5 companies), MSME landscape, growth loops, app store signals | [`docs/market_intelligence.md`](docs/market_intelligence.md) / Market Intel tab |
| Google Sheets / Excel deliverable | Formatted multi-tab Excel model with KPI cards, scorecard, charts | [`sheets/growth_dashboard.xlsx`](sheets/growth_dashboard.xlsx) |
| Cross-functional communication | Experiment briefs with business context, guardrail metrics, and learning objectives | [`docs/experiment_brief.md`](docs/experiment_brief.md) / Growth OS tab |
| Analytical transparency | Metric Dictionary tab (14 metrics with formulas, confidence, limitations), per-KPI info panels | Metrics tab / Overview info panels |

---

## Real Public Data Sources

| Dataset | Source | Records | Analytical role |
|:---|:---|:---|:---|
| **KAG_conversion_data.csv** | Kaggle — Sales Conversion Optimization | 1,143 ad sets, 3 campaigns | Campaign scorecard, decomposition, audience analysis, funnel |
| **online_shoppers_intention.csv** | UCI Machine Learning Repository | 12,330 sessions | Consumer behavior diagnostics, engagement tiers, visitor type analysis |

Both datasets are 100% real public data. No rows have been modified, filtered for convenience, or supplemented with synthetic values.

---

## Project Architecture

```text
e:\Growth Campaign & Funnel Intelligence Lab\
├── index.html                   # Root: Vercel entry point (auto-synced from web/)
├── js/dashboard.js              # Root: Vercel JS asset (auto-synced from web/)
├── data/dashboard_data.json     # Root: Vercel data asset (auto-synced)
├── vercel.json                  # Vercel deploy config (cleanUrls, CORS headers)
├── render.yaml                  # Render Blueprint: pip install + uvicorn
│
├── web/                         # Source of truth for frontend
│   ├── index.html               # 1800+ line dark-mode analytics UI (16 interactive tabs)
│   ├── js/dashboard.js          # 2400+ line Chart.js + Canvas controller (interactive HUDs, radar, donut, modal)
│   └── data/dashboard_data.json # 15-key analytical payload with 21-field Experiment OS
│
├── backend/
│   ├── main.py                  # FastAPI: 8 endpoints (scorecard, decomposition,
│   │                            #   ab-test, sample-size, experiments, market-intel,
│   │                            #   hypothesis-pipeline, metric-dictionary)
│   └── requirements.txt
│
├── src/                         # Python analytical engine
│   ├── data_loader.py           # Dataset loading and schema validation
│   ├── metrics.py               # Ratio-of-sums KPI engine
│   ├── diagnostics.py           # 3-factor bridge, mix adjustment, segment stability
│   ├── statistics.py            # Z-test, confidence intervals, sample size
│   ├── experiment_engine.py     # ICE backlog, hypothesis pipeline stages, data provenance
│   ├── validation.py            # 11-check data quality audit
│   └── report_generator.py     # Markdown and CSV exports
│
├── sql/                         # Analytical SQL transformations
│   ├── 01_staging.sql
│   ├── 02_clean.sql
│   ├── 03_metrics.sql           # CTR, CPC, CPM, conversion rates
│   ├── 04_audience.sql          # Age, gender, interest segmentation
│   ├── 05_mix_analysis.sql      # Direct standardization
│   ├── 06_funnel.sql            # Stage conversion and drop-off rates
│   └── 07_quality.sql           # Data quality checks
│
├── docs/                        # Strategy and methodology documentation
│   ├── methodology.md           # Mathematical derivations and proofs
│   ├── market_intelligence.md   # Competitor analysis, MSME landscape
│   ├── growth_os_framework.md   # Growth OS methodology
│   ├── growth_playbook.md       # Executive strategy briefing
│   ├── experiment_brief.md      # Cross-functional experiment template
│   ├── metric_definitions.md    # Metric availability and boundary table
│   ├── analytical_dossier.md    # Mathematical proofs and code traceability
│   ├── limitations.md           # Honest capability boundaries
│   └── khatabook_growth_strategy.md  # Khatabook product & growth analysis
│
├── tests/                       # 44 automated tests
│   ├── test_metrics.py          # Ratio-of-sums, safe_divide, scorecard
│   ├── test_diagnostics.py      # Decomposition bridge, mix adjustment
│   ├── test_statistics.py       # Z-test, CI, sample size
│   ├── test_funnel.py           # Funnel stage calculations
│   ├── test_quality.py          # Data quality audit checks
│   ├── test_backend.py          # FastAPI endpoint integration (10 endpoints)
│   ├── test_experiment_engine.py # ICE scoring, hypothesis pipeline
│   └── test_market_data.py      # Market intelligence data structure
│
├── scripts/
│   ├── download_data.py         # Fetch raw datasets with SHA-256 validation
│   ├── prepare_data.py          # Clean, schema-validate, persist to Parquet/SQLite
│   ├── run_analysis.py          # Execute full analytical pipeline
│   ├── export_reports.py        # Generate Markdown + CSV exports
│   └── export_web_data.py       # Build dashboard_data.json payload
│
├── exports/                     # 9 CSV exports (scorecard, funnel, segments, etc.)
├── reports/                     # 4 Markdown analytical reports
└── sheets/growth_dashboard.xlsx # Formatted Excel model (10 tabs)
```

---

## Run Locally

```bash
git clone https://github.com/sailwalpranjal/Growth-Campaign-Funnel-Intelligence-Lab.git
cd Growth-Campaign-Funnel-Intelligence-Lab

pip install -r requirements.txt

# Download and validate real public datasets
python scripts/download_data.py

# Build analytical pipeline (clean, transform, compute)
python scripts/prepare_data.py
python scripts/run_analysis.py

# Export analytical reports and web data payload
python scripts/export_reports.py
python scripts/export_web_data.py

# Run full test suite (44 tests)
python -m pytest -q

# Start backend API
uvicorn backend.main:app --reload --port 8000
# API docs: http://localhost:8000/docs

# Serve frontend locally (any static server)
cd web && python -m http.server 3000
# Open http://localhost:3000
```

---

## Cloud Deployment

### Vercel (Frontend — zero config)
1. Fork repository to your GitHub account
2. Connect to Vercel at [vercel.com](https://vercel.com)
3. Import the repository — no build settings needed
4. Deploy. `index.html` at root is the entry point.

### Render (Backend API — free tier)
1. Connect repository at [render.com](https://render.com)
2. Create a new **Web Service**
3. Build command: `pip install -r backend/requirements.txt`
4. Start command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5. Or use the included `render.yaml` Blueprint for one-click deploy.

---

## What Would Change in Production

This platform uses static public datasets and a pre-built JSON payload. In a real Khatabook data infrastructure:

| Component | Portfolio version | Production version |
|:---|:---|:---|
| **Data source** | Static CSV files (Kaggle, UCI) | Snowflake / BigQuery warehouse fed by event streams |
| **Event collection** | Not applicable | Segment or Snowplow SDK on mobile app |
| **Mobile attribution** | Not available | AppsFlyer or Branch linking ad click → install → activation |
| **Funnel stages** | Impression → Click → Enquiry → Approved | Full: Click → Install → OTP → Login → First Entry → D7 Active → QR payment → Loan application |
| **A/B testing** | Statistical calculator (user-entered data) | Integrated with LaunchDarkly or Statsig for automated assignment and real-time tracking |
| **CRM signals** | Observational from UCI dataset | Real merchant event stream: last_entry_date, reminder_sent_count, feature_adoption |
| **Competitor intel** | Manually sourced public data | Automated monitoring via public APIs (App Store ratings, LinkedIn job signals) |
| **Refresh** | Static payload, manual re-run | Scheduled dbt runs → API cache invalidation → frontend auto-refresh |

The analytical architecture (3-factor decomposition, mix adjustment, ICE prioritization, z-test engine) translates directly to production — only the data sources change.
