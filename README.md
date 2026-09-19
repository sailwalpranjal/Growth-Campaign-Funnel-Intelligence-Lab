# Growth Campaign & Funnel Intelligence Lab

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests Passing](https://img.shields.io/badge/tests-25%20passed-brightgreen.svg)](tests/)
[![Data Integrity](https://img.shields.io/badge/data%20provenance-100%25%20real%20public-orange.svg)](data/)
[![Excel Deliverable](https://img.shields.io/badge/deliverable-Google%20Sheets%20%2F%20Excel-success.svg)](sheets/)
[![Live Web Dashboard](https://img.shields.io/badge/live%20dashboard-Vercel%20Ready-teal.svg)](web/)
[![Free Backend](https://img.shields.io/badge/backend%20API-Render%20Free-purple.svg)](backend/)

> **Production-grade growth analytics platform engineered for Khatabook growth marketing, product growth, and merchant acquisition leadership.**  
> *Core Focus: Numerical reasoning, 3-factor campaign efficiency decomposition, multi-stage funnel drop-off diagnostics, observational audience mix-adjustment, and merchant unit economics using 100% verified public data.*  
> **Live Visual Dashboard**: Includes an ultra-modern dark-mode executive dashboard deployable to **Vercel** with zero cold starts, interactive Gaussian A/B testing simulator, and mobile app unit economics modeling.

---

## Executive Summary in 60 Seconds

```text
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ CORE BUSINESS QUESTION:                                                                 │
│ "Why did scaling ad spend from Campaign 936 ($2.9k) to Campaign 1178 ($55.7k) cause      │
│  Cost per Approved Conversion to surge from $15.81 to $63.83 (+303.7%), and what should │
│  the growth team test next to recover unit economics?"                                   │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

| Dimension | Mid-Scale Baseline (Camp 936) | Scaled Campaign (Camp 1178) | Observed Delta / Variance | Growth Diagnosis |
| :--- | :--- | :--- | :--- | :--- |
| **Media Spend** | \$2,893.37 | \$55,662.15 | **+\$52,768.78 (19.2x)** | Aggressive scale across 625 ad sets. |
| **Approved Conversions**| 183 | 872 | **+689 (+376.5%)** | Sub-linear volume scaling. |
| **Cost / Approved** | **\$15.81** | **\$63.83** | **+\$48.02 (+303.7%)** | **4.0x Unit Cost Degradation.** |
| **CPM (Inventory Cost)**| \$0.356 | \$0.272 | **-\$0.084 (-23.6%)** | *Advantage Scaled*: Cheaper media pricing at scale. |
| **CTR (Creative Hook)** | 0.0244% | 0.0176% | **-0.0068% (-27.9%)** | *Friction*: Creative fatigue and broader audience reach. |
| **Post-Click Conv Rate**| **9.22%** | **2.42%** | **-6.80% (-73.8%)** | **PRIMARY LEAKAGE**: 92.6% drop-off post-click. |

### The 3-Factor Efficiency Bridge (Sequential Waterfall Attribution)
$$\text{Cost per Approved} = \underbrace{\frac{\text{Spend}}{\text{Impressions}}}_{L_1: \text{CPM}/1000} \times \underbrace{\frac{\text{Impressions}}{\text{Clicks}}}_{L_2: 1/\text{CTR}} \times \underbrace{\frac{\text{Clicks}}{\text{Approved}}}_{L_3: 1/\text{Conv Rate}}$$

* **Lever 1 (CPM Effect)**: **-\$3.74** *(Favorable: Scale buying unlocked cheaper impressions)*.
* **Lever 2 (CTR Effect)**: **+\$4.66** *(Unfavorable: Creative hook resonance decayed)*.
* **Lever 3 (Post-Click Conversion Effect)**: **+\$47.10** *(**Primary Culprit: 98.1% of cost surge occurred after the click**)*.
* **Total Reconciled Gap**: **+\$48.02** (100.000% mathematical identity match; zero residual).

---

## Why This Project?

Most early-career portfolios build toy machine learning models on synthetic data or build web applications that look like software engineering demos. 

**This lab takes the opposite approach:**
1. **Prioritizes Commercial Thinking Over Technology**: Focuses on the core metric levers a Growth Manager cares about: spends, CTR, CPM, CPC, conversion rates, funnel drop-offs, and unit economics.
2. **Rejects Mock Data**: Employs real public datasets (1,143 Facebook ad records across 3 campaigns and 12,330 UCI e-commerce sessions).
3. **Observational Rigor**: Treats data with intellectual honesty—refusing to label top-of-funnel lead approvals as "CAC", refusing to fabricate mock revenue for synthetic "ROAS", and applying direct standardization to control for audience confounding.

---

## JD-Relevant Skills Demonstrated (Mapped to Khatabook Requirements)

| Khatabook JD Requirement | How It Is Implemented in This Repository | Key File Reference |
| :--- | :--- | :--- |
| **Campaign Performance & Spend Analysis** | Ratio-of-sums campaign scorecard tracking impressions, clicks, spend, CTR, CPC, and CPM. | [`sql/03_metrics.sql`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/sql/03_metrics.sql) / [`src/metrics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/src/metrics.py) |
| **Investigate Why a Metric Changed** | Three-factor efficiency bridge mathematically isolating CPM, CTR, and conversion rate contributions. | [`src/diagnostics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/src/diagnostics.py) / [`reports/campaign_diagnostic.md`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/reports/campaign_diagnostic.md) |
| **Acquisition Funnel & Drop-Off Analysis** | Multi-stage funnel modeling (Impression $\to$ Click $\to$ Enquiry $\to$ Approved) isolating the 92.6% click-to-lead bottleneck. | [`sql/06_funnel.sql`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/sql/06_funnel.sql) / [`reports/funnel_analysis.md`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/reports/funnel_analysis.md) |
| **Audience Segmentation & Stability** | Demographics (Age, Gender, Interest) with sensitivity checks at 10, 25, 50 clicks to filter volatile noise. | [`sql/04_audience.sql`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/sql/04_audience.sql) / [`exports/segment_stability.csv`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/exports/segment_stability.csv) |
| **Audience Mix Adjustment** | Direct standardization comparing raw vs benchmark-adjusted performance to rule out demographic skew. | [`sql/05_mix_analysis.sql`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/sql/05_mix_analysis.sql) / [`exports/mix_analysis.csv`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/exports/mix_analysis.csv) |
| **Growth Experimentation & Backlog** | Evidence-to-hypothesis pipeline with ICE scoring, control/variants, primary KPIs, and guardrail metrics. | [`src/experiment_engine.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/src/experiment_engine.py) / [`reports/experiment_backlog.md`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/reports/experiment_backlog.md) |
| **A/B Testing & Sample-Size Planning** | Two-proportion z-test calculator with two-tailed p-values, 95% CIs, and power-based sample size sizing. | [`src/statistics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/src/statistics.py) / [`tests/test_statistics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/tests/test_statistics.py) |
| **Google Sheets & Reporting** | Formatted executive dashboard with KPI cards, tables, conditional formatting, and charts. | [`sheets/growth_dashboard.xlsx`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/sheets/growth_dashboard.xlsx) |
| **Attention to Detail & Data Quality** | Automated 11-check audit flagging missing labels, zero-click ad spend, and impossible event states. | [`src/validation.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/src/validation.py) / [`sql/07_quality.sql`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/sql/07_quality.sql) |
| **Consumer Behavior & Competitor Research**| UCI session diagnostic & public market study of Khatabook, OkCredit, Vyapar, and PhonePe for Business. | [`docs/research.md`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/docs/research.md) / [`exports/consumer_behavior.csv`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/exports/consumer_behavior.csv) |

---

## Real Public Data Sources & Separation

To preserve methodological integrity, datasets are maintained as distinct modules without artificial joins:

1. **Primary Acquisition Dataset (Dataset A)**:
   * **Source**: Kaggle — Sales Conversion Optimization / Clicks Conversion Tracking (`KAG_conversion_data.csv`).
   * **Scope**: 1,143 ad sets across 3 social advertising campaigns (`916`, `936`, `1178`).
   * **SHA-256**: `2ee88488b5229562e8814b08e95e09e675aa939f69fc16f124eefe2bfdfa7cf8`
   * **Role**: Top-of-funnel acquisition, spend efficiency, CTR, CPM, CPC, and efficiency decomposition.
2. **Consumer Behavior Dataset (Dataset B)**:
   * **Source**: UCI Machine Learning Repository (`online_shoppers_intention.csv`).
   * **Scope**: 12,330 e-commerce sessions with page duration, bounce/exit rates, and purchase outcomes.
   * **SHA-256**: `16c44b48955125b2adc0b37c526f3e190d0689a3193a41e65da9b210cc5d7af1`
   * **Role**: On-site session diagnostics, returning vs. new visitor dynamics, and engagement propensity.

---

## Real vs. Derived vs. Hypothesis Taxonomy

* **Real Public Data**: Unedited observations present in the source files (e.g. `Clicks = 36,068`, `Spend = $55,662.15`).
* **Derived Metrics**: Pure mathematical ratio-of-sums calculations (e.g. $\text{CTR} = 0.0176\%$, $\text{CPM} = \$0.272$, $\text{Cost/Approved} = \$63.83$).
* **Analyst Interpretation**: Observational inferences drawn from quantitative patterns (e.g. Campaign 1178 experienced post-click expectation misalignment at scale).
* **Hypothesis**: Behavioral theories formulated to explain gaps (e.g. generic broad ad hooks attracted low-intent browsers).
* **Proposed Experiment**: Unexecuted growth test designs with controls, variants, primary KPIs, and guardrails.

---

## Key Analytical Findings

### 1. The 92.6% Post-Click Bottleneck
Multi-stage funnel mapping revealed that once an enquiry is submitted, qualification rates are virtually identical between Campaign 936 (34.1%) and Campaign 1178 (32.7%). **The failure happens entirely between the click and form submission**, where 92.6% of traffic in Campaign 1178 bounced without submitting an enquiry.

### 2. Audience Mix Standardization
Applying direct standardization across age demographics proved that if Campaign 1178 were evaluated under Campaign 936's exact demographic distribution, its cost per approved conversion would actually increase slightly to **\$78.16**. This definitively rules out demographic skew as the root cause of underperformance.

### 3. Segment Stability & Budget Concentration
Sensitivity analysis at 10, 25, and 50 clicks revealed that 12 of 28 interest segments had <10 clicks, creating noisy and misleading cost metrics. Conversely, top interest segments (IDs 16 and 27) consistently maintained approved conversion costs below \$25 across 50+ click thresholds, indicating an immediate opportunity to prune volatile ad sets.

### 4. Consumer Behavior: Intent Divergence
Analysis of 12,330 sessions demonstrated that New Visitors converted at 24.9% with an average page value of \$10.77, while Returning Visitors converted at 13.9% with longer browsing durations (1,289s) and higher bounce rates (0.0248), identifying a prime opportunity for personalized cart re-engagement.

---

## Top Prioritized Growth Experiments (ICE Framework)

| Priority | ID | Title | Target Audience | Primary KPI | Guardrail | ICE Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P0** | `EXP-GROWTH-001` | **Value Prop Pre-Qualification Hook** | Broad Acquisition | Click-to-Approved Rate ($\ge 3.0\%$) | CTR $\ge 0.012\%$ | **8.67** |
| **P0** | `EXP-GROWTH-003` | **Budget Concentration in Stable Interests**| Campaign Allocation | Blended Cost / Approved ($\le \$35$) | Impressions $\ge 85\%$ | **8.67** |
| **P0** | `EXP-GROWTH-002` | **2-Step Progressive Micro-Commitment Form**| All Post-Click Traffic | Click-to-Enquiry Rate ($\ge 12\%$) | Lead Quality $\ge 30\%$ | **8.00** |
| **P1** | `EXP-GROWTH-004` | **Returning Visitor Contextual Nudge** | Returning Sessions | Session-to-Purchase Rate | Bounce Rate $\le +2\%$ | **7.00** |
| **P1** | `EXP-GROWTH-005` | **Demographic Landing Page Framing** | Female SMB Cohort | Post-Click Approved Rate | CPC $\le +10\%$ | **7.00** |

---

## Deliverables & Repository Structure

```text
growth-campaign-funnel-intelligence/
├── README.md                           # Executive showcase and growth memo
├── requirements.txt                    # Minimal reproducible dependencies
├── pytest.ini                          # Test runner configuration
├── data/
│   ├── README.md                       # Data provenance, evaluation of 3 public datasets
│   ├── raw/                            # Original unedited CSVs with SHA-256 metadata
│   └── processed/                      # Clean parquet snapshots and SQLite database
├── sql/
│   ├── 01_staging.sql                  # Staging tables DDL
│   ├── 02_clean.sql                    # Data cleaning views & anomaly filters
│   ├── 03_metrics.sql                  # Ratio-of-sums scorecard & decomposition
│   ├── 04_audience.sql                 # Demographics & interest segment performance
│   ├── 05_mix_analysis.sql            # Direct standardization & common audience mix
│   ├── 06_funnel.sql                   # Multi-stage funnel drop-off analysis
│   └── 07_quality.sql                  # Data hygiene, duplicates & negative value checks
├── src/
│   ├── data_loader.py                  # Automated download, checksum & caching
│   ├── validation.py                   # Data quality rules & anomaly detection
│   ├── metrics.py                      # Ratio-of-sums aggregations & safe denominators
│   ├── diagnostics.py                  # Efficiency bridge & direct standardization
│   ├── statistics.py                   # Two-proportion z-test & sample size planner
│   ├── experiment_engine.py            # ICE prioritization & test proposals
│   └── report_generator.py             # Openpyxl Excel workbook & markdown builder
├── scripts/
│   ├── download_data.py                # Automated data acquisition with SHA-256 validation
│   ├── prepare_data.py                 # Cleaning, staging & SQLite pipeline execution
│   ├── run_analysis.py                 # Core analytical pipeline execution
│   └── export_reports.py               # Generates CSVs, Excel dashboard & executive memos
├── reports/
│   ├── executive_summary.md            # One-page executive growth memo
│   ├── campaign_diagnostic.md          # 3-factor efficiency decomposition report
│   ├── funnel_analysis.md              # Multi-stage drop-off diagnostic
│   └── experiment_backlog.md           # Prioritized growth backlog with ICE scores
├── exports/
│   ├── campaign_scorecard.csv          # Campaign scorecard CSV
│   ├── audience_analysis.csv           # Age, gender & interest breakdown CSV
│   ├── segment_stability.csv           # Sensitivity checks across 10, 25, 50 clicks
│   ├── mix_analysis.csv                # Raw vs mix-adjusted campaign comparison CSV
│   ├── funnel_analysis.csv             # Multi-stage drop-off rates CSV
│   ├── consumer_behavior.csv           # UCI session diagnostic CSV
│   ├── experiment_backlog.csv          # Structured test proposals CSV
│   └── data_quality.csv                # Integrity audit log CSV
├── sheets/
│   └── growth_dashboard.xlsx           # Interactive multi-tab Excel workbook with KPI cards & charts
├── docs/
│   ├── metric_definitions.md           # Metric availability table & CAC/ROAS boundaries
│   ├── methodology.md                  # Ratio-of-sums, decomposition & mix standardization math
│   ├── limitations.md                  # Observational vs causal boundaries & unobserved factors
│   ├── research.md                     # Khatabook & Indian SMB competitor landscape analysis
│   ├── khatabook_growth_strategy.md    # 2026 Khatabook fintech ecosystem, growth loops & app funnel
│   ├── experiment_brief.md             # Cross-functional brief (Growth, Creative, Analytics, Product, CRM)
│   ├── crm_template.md                 # CRM experiment planning framework
│   ├── analytical_dossier.md           # Methodological proofs, variance identities & metric lineage
│   └── growth_playbook.md              # Executive Growth Operations & Strategy Playbook
├── web/
│   ├── index.html                      # 10-tab interactive executive dashboard (Chart.js, Tailwind CDN)
│   ├── js/
│   │   └── dashboard.js                # State management, waterfall charts, live A/B lab & simulator
│   └── data/
│       └── dashboard_data.json         # Static standalone analytical payload (zero cold start)
├── backend/
│   ├── main.py                         # FastAPI analytical microservice with CORS & live calculations
│   └── requirements.txt                # Lightweight backend dependencies (uvicorn, fastapi, scipy)
├── vercel.json                         # Vercel single-click deployment & URL routing configuration
├── render.yaml                         # Render free-tier Blueprint configuration for FastAPI backend
└── tests/
    ├── test_metrics.py                 # Ratio-of-sums, CTR, CPC, CPM, zero denominators
    ├── test_diagnostics.py             # Three-factor efficiency decomposition math identity
    ├── test_funnel.py                  # Drop-off calculations & stage rates
    ├── test_statistics.py              # Z-score, p-value, 95% CI & sample size formulas
    ├── test_quality.py                 # Anomaly detection & boundary constraints
    └── test_backend.py                 # FastAPI test suite (scorecard, decomposition, A/B test endpoints)
```

---

## Executive Growth Briefing & Walkthrough Protocol

Executive leaders and VP/Heads of Growth evaluate whether an analytical platform delivers **commercial clarity, actionable funnel levers, customer unit economics, and testable hypotheses**.

Here is the structured 3-minute briefing protocol:

### 1. The 30-Second Commercial Hook
> *"When scaling paid social acquisition by 19x (from \$2.9k to \$55.7k), why did cost per approved conversion surge from \$15.81 to \$63.83 (+303.7%)?*  
> *Rather than guessing or blaming ad algorithms, this platform decomposes unit cost into exact mathematical levers. The data revealed that media buying was actually 24% cheaper at scale (lower CPMs). Demographics didn't explain the gap either. The core problem was post-click conversion collapse: 92.6% of clicks bounced before submitting an enquiry. We translated this into prioritized growth tests, modeled Khatabook's merchant unit economics, and built an interactive executive dashboard deployed on Vercel."*

### 2. The 3-Minute Live Dashboard Walkthrough
1. **Executive Overview & KPI Cards (Tab 1)**: Review blended metrics aggregated via strict ratio-of-sums to eliminate Simpson's Paradox.
2. **The Efficiency Bridge Waterfall (Tab 2)**: Walk through the 3-factor waterfall chart. Show how Lever 1 (CPM effect) saved -\$3.74, Lever 2 (CTR decay) cost +\$4.66, and Lever 3 (Post-Click Conversion) surged by +\$47.10 (accounting for 98.1% of the cost explosion).
3. **Khatabook Mobile App Funnel & LTV/CAC Simulator (Tab 4)**: Demonstrate the dual live charts (Funnel Projection and 12-Month LTV/CAC Payback Curve). Adjust $D_1$ activation and Soundbox attachment sliders to show how product onboarding improvements drop merchant CAC by 28% without increasing ad budget.
4. **Live Statistical A/B Testing Lab with Bell Curves (Tab 7)**: Show the canvas-rendered Gaussian Normal Distribution curves, two-tailed z-score ($p < 0.001$), 95% confidence intervals, and automated decision badges (*"Ship & Scale"*, *"Inconclusive"*, *"Kill Variant"*).

### 3. Commercial Growth Principles
* **"Growth is an Integrated System"**: Scaled campaigns fail when top-of-funnel ad promises do not align with post-click product onboarding.
* **"Data Integrity Over Vanity"**: Never label direct ad spend as 'CAC' because true CAC includes organic attribution and retention. Never fabricate mock revenue for 'ROAS'.
* **"Analysis Must Fuel Hypotheses"**: Pinpointing a funnel leakage is only complete once it is translated into an ICE-prioritized experiment backlog with cross-functional briefs.

---

## Free Cloud Deployment Guide (Vercel & Render)

This repository is architected with a **dual-mode deployment model**:
1. **Static Vercel Dashboard (Primary / Recommended)**: Instant load, zero server cold starts, 100% free forever on Vercel's global CDN. Includes all visualizations, interactive sliders, client-side statistical engine, and direct file downloads.
2. **FastAPI Backend on Render (Optional)**: A lightweight Python microservice for dynamic REST API endpoints (`/api/scorecard`, `/api/decomposition`, `/api/ab-test`, `/api/sample-size`).

### Option A: 1-Click Deployment to Vercel (Recommended)

1. **Push your repository to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "feat: initial Growth Campaign & Funnel Intelligence Lab commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/growth-campaign-funnel-intelligence.git
   git push -u origin main
   ```
2. **Log into Vercel** ([vercel.com](https://vercel.com)):
   * Click **"Add New..."** $\to$ **"Project"**.
   * Import your `growth-campaign-funnel-intelligence` GitHub repository.
3. **Configure Project Settings**:
   * **Framework Preset**: Select `Other` (or None).
   * **Root Directory**: Leave as `./` (the included [`vercel.json`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/vercel.json) automatically maps root requests to `/web/index.html` and routes assets).
   * **Build & Output Settings**: Leave completely blank (no build step needed).
4. **Click Deploy**:
   * In 15 seconds, your dashboard will be live at `https://your-project-name.vercel.app`!
   * Verify tabs, interactive charts, and Excel dashboard download button.

### Option B: Deploy Backend REST API to Render (Free)

1. **Log into Render** ([render.com](https://render.com)):
   * Click **"New +"** $\to$ **"Blueprint"** (or "Web Service").
   * Connect your GitHub repository.
   * Render will automatically read the included [`render.yaml`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/render.yaml) file:
     * **Runtime**: Python 3.11+
     * **Build Command**: `pip install -r backend/requirements.txt`
     * **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
     * **Instance Type**: Free
2. **Access Swagger Interactive API**:
   * Once deployed, your API is available at `https://growth-intelligence-api.onrender.com`.
   * Explore interactive documentation at `https://growth-intelligence-api.onrender.com/docs`.
   * Test live endpoints:
     * `GET /api/scorecard`: Full campaign performance metrics.
     * `GET /api/decomposition?base=936&target=1178`: Exact mathematical efficiency waterfall.
     * `POST /api/ab-test`: Live two-proportion hypothesis testing.
     * `POST /api/sample-size`: Minimum detectable effect and sample size calculation.

---

## Khatabook Growth & Product Strategy Alignment

This project is directly mapped to Khatabook's 2026 fintech ecosystem ([Read the full 15-page strategy breakdown](docs/khatabook_growth_strategy.md)):

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           KHATABOOK ECOSYSTEM (2026)                             │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 1. Core Digital Bahi Khata (App)  ──> Free Merchant Bookkeeping & Ledger         │
│ 2. Smart Soundbox & Dynamic QR    ──> Audio UPI confirmation hardware (Hardware) │
│ 3. Biz Analyst by Khatabook       ──> Tally desktop integration for mid-tier SMBs│
│ 4. Merchant Financial Services    ──> Credit score, short-term MSME working cap  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### The 3 Core Growth Loops
1. **Organic WhatsApp Payment Reminder Loop ($K$-Factor Engine)**:
   * Merchant records a debit credit ($Udhar$) $\to$ Sends automated WhatsApp reminder with UPI pay link $\to$ Customer receives message with *"Powered by Khatabook"* $\to$ Customer happens to be a retail merchant $\to$ Installs Khatabook.
2. **Paid Acquisition Loop (Meta/Google $\to$ Regional Onboarding)**:
   * Targeted ads in 11 regional languages (Hindi, Gujarati, Tamil, Hinglish) $\to$ Lightweight Play Store install $\to$ OTP verification $\to$ First customer credit added within 48 hours ($D_1$ Activation).
3. **Monetization & Expansion Loop**:
   * Active ledger history $\to$ Proprietary merchant credit assessment $\to$ Pre-approved collateral-free working capital loan $\to$ Net interest margin + Soundbox monthly subscription recurring SaaS fee.

---

## Reproducibility & Quickstart

Clone the repository and run the end-to-end pipeline in under 2 minutes:

```powershell
# 1. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # On Windows (or source .venv/bin/activate on Linux/Mac)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download verified public datasets with SHA-256 checks
python scripts/download_data.py

# 4. Initialize SQL database, run staging views, and execute quality audit
python scripts/prepare_data.py

# 5. Run full growth analytics pipeline
python scripts/run_analysis.py

# 6. Export all CSVs, Excel dashboard, and markdown executive reports
python scripts/export_reports.py

# 7. Run automated test suite (Unit, Integration, Analytics & API)
pytest -q
```

**All 25 test cases pass cleanly with zero warnings or errors.**

---

## Local Web Visualizer Preview

To preview the interactive web dashboard locally:

```powershell
# Start local Python HTTP server
python -m http.server 8000 --directory web

# Open in browser
# http://localhost:8000
```

---

## Cloud Deployment Guide (Vercel + Render)

### 1. Vercel Global CDN (Frontend Web Platform - 100% Free, Zero Cold Starts)
The web platform is pre-configured with `vercel.json` with clean URL rewrites:
1. Navigate to [Vercel](https://vercel.com) and log in with your GitHub account.
2. Click **"Add New..."** $\to$ **"Project"**.
3. Select and import **`sailwalpranjal/Growth-Campaign-Funnel-Intelligence-Lab`**.
4. In **Project Settings**:
   * **Framework Preset**: `Other`
   * **Root Directory**: `./`
   * **Build & Output Settings**: Default (no build step needed for pure static assets)
5. Click **Deploy**. The platform deploys globally in under 20 seconds with sub-30ms TTFB.

### 2. Render Free Web Service (FastAPI REST Backend)
The API service is pre-configured with `render.yaml` Infrastructure-as-Code:
1. Navigate to [Render](https://dashboard.render.com) and log in with your GitHub account.
2. Click **"New +"** $\to$ **"Blueprint"**.
3. Select repository **`sailwalpranjal/Growth-Campaign-Funnel-Intelligence-Lab`**.
4. Render automatically reads `render.yaml` (`pip install -r backend/requirements.txt`, `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`, Free Plan).
5. Click **Apply**. The backend API and interactive `/docs` Swagger UI deploy in ~2 minutes.
