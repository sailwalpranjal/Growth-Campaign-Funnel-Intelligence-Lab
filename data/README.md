# Data Provenance & Evaluation

This directory contains the real public datasets used in the **Growth Campaign & Funnel Intelligence Lab**, along with their SHA-256 integrity checksums, variable dictionaries, and evaluation rationale.

---

## 1. Candidate Dataset Evaluation (3 Public Datasets Assessed)

Before building this project, three public datasets were evaluated against the core business question:
*"Why does one campaign acquire conversions more efficiently than another, which observable factors explain the difference, where are users dropping off, and what should the growth team test next?"*

| Candidate Dataset | Key Attributes Available | Strengths | Limitations | Decision |
| :--- | :--- | :--- | :--- | :--- |
| **1. Kaggle Sales Conversion Optimization (Clicks Conversion Tracking)** | `ad_id`, `xyz_campaign_id`, `fb_campaign_id`, `age`, `gender`, `interest`, `Impressions`, `Clicks`, `Spent`, `Total_Conversion`, `Approved_Conversion` (1,143 ads, 3 campaigns) | Multi-campaign spend, impression, click, and multi-tier conversion counts. Rich demographic (`age`, `gender`) and audience (`interest`) dimensions. Allows exact mathematical decomposition into CPM, CTR, and post-click conversion rate. | Anonymized ad campaign IDs; lacks creative text/image files; does not track downstream app events (`installs`, `logins`, `revenue`). | **Selected (Primary Acquisition Dataset)** |
| **2. UCI Online Shoppers Purchasing Intention** | `Administrative`, `Informational`, `ProductRelated`, durations, `BounceRates`, `ExitRates`, `PageValues`, `SpecialDay`, `Month`, `OperatingSystems`, `Browser`, `Region`, `TrafficType`, `VisitorType`, `Weekend`, `Revenue` (12,330 sessions) | Real granular session-level behavioral signals, engagement depth, bounce/exit rates, returning vs new visitor splits, and final transaction outcomes. | Session-level e-commerce data; lacks paid ad spend, impressions, or ad creative links. | **Selected (Secondary Consumer Behavior Diagnostic)** |
| **3. Criteo Attribution Modeling / Bank Marketing Datasets** | Criteo: Hashed categorical features `cat_1` to `cat_9`, timestamp, click, conversion.<br>Bank Marketing: Age, job, marital, education, contact duration, deposit. | Criteo offers massive scale (millions of touchpoints). Bank marketing has detailed demographics. | Criteo's hashed features prevent interpretable audience segmentation (`interest`, `gender`, `age`) essential for growth campaign diagnostics. Bank marketing reflects outbound telemarketing, not digital growth marketing funnels. | **Evaluated & Excluded** |

---

## 2. Selected Datasets & Provenance

### Dataset A: Primary Ad Campaign Acquisition Dataset
- **Filename**: `data/raw/KAG_conversion_data.csv`
- **Source**: Kaggle — Sales Conversion Optimization / Clicks Conversion Tracking
- **Publisher**: Kaggle / Anonymous Ad Network
- **Retrieval Date**: 2026-09-19
- **Size**: 60,522 bytes (1,143 records, 11 columns)
- **SHA-256 Checksum**: `2ee88488b5229562e8814b08e95e09e675aa939f69fc16f124eefe2bfdfa7cf8`
- **License**: Public Domain / CC0 Equivalent
- **Description**: Anonymized public social-media advertising dataset spanning three campaigns (`916`, `936`, `1178`).
- **Data Dictionary**:
  - `ad_id`: Unique identifier for each ad record (Integer).
  - `xyz_campaign_id`: Top-level marketing campaign ID (`916`, `936`, `1178`) (Integer).
  - `fb_campaign_id`: Ad network / Facebook platform campaign ID (Integer).
  - `age`: Age bracket of the targeted audience segment (`30-34`, `35-39`, `40-44`, `45-49`) (String).
  - `gender`: Gender of targeted audience (`M`, `F`) (String).
  - `interest`: Numeric code representing the audience interest category (Integer).
  - `Impressions`: Number of times the ad was shown (Integer).
  - `Clicks`: Number of clicks recorded on the ad (Integer).
  - `Spent`: Amount of advertising spend in currency units (Float).
  - `Total_Conversion`: Number of people who enquired or initiated action after clicking the ad (Integer).
  - `Approved_Conversion`: Number of people who successfully converted / bought a product or approved an offer (Integer).

### Dataset B: Consumer Behavior Diagnostic Dataset
- **Filename**: `data/raw/online_shoppers_intention.csv`
- **Source**: UCI Machine Learning Repository
- **Publisher**: C. Okan Sakar & Yomi Kastro
- **Retrieval Date**: 2026-09-19
- **Size**: 1,062,237 bytes (12,359 rows total; 12,330 complete records, 18 columns)
- **SHA-256 Checksum**: `16c44b48955125b2adc0b37c526f3e190d0689a3193a41e65da9b210cc5d7af1`
- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Description**: Session-level browsing attributes and purchase transactions over a 1-year period to diagnose on-site engagement and drop-off propensity.
- **Key Attributes**:
  - `Administrative`, `Informational`, `ProductRelated`: Number of pages visited of each type.
  - `Administrative_Duration`, `Informational_Duration`, `ProductRelated_Duration`: Total time spent (seconds) in each category.
  - `BounceRates`: Average bounce rate of pages visited by the visitor.
  - `ExitRates`: Average exit rate of pages visited by the visitor.
  - `PageValues`: Average page value of pages visited prior to transaction.
  - `SpecialDay`: Closeness of browsing date to a special day (e.g. Mother's Day, Valentine's Day).
  - `Month`: Calendar month of the session.
  - `OperatingSystems`, `Browser`, `Region`, `TrafficType`: Device and traffic categorical dimensions.
  - `VisitorType`: Visitor status (`Returning_Visitor`, `New_Visitor`, `Other`).
  - `Weekend`: Boolean flag indicating weekend session (`True`, `False`).
  - `Revenue`: Conversion outcome indicating whether the session generated a completed purchase (`True`, `False`).

---

## 3. Methodological Boundary & Separation

> [!IMPORTANT]
> **Strict Analytical Separation**
> - **Dataset A** and **Dataset B** originate from two completely distinct real public sources and **do NOT share a common entity key**.
> - **Do NOT join them**: Joining them artificially would fabricate a false data model.
> - **Do NOT combine revenue and spend**: Dataset B's transaction revenue is never divided by Dataset A's ad spend to create synthetic ROAS or fake unit economics.
> - **Distinct Analytical Roles**:
>   - **Dataset A** powers top-of-funnel acquisition analysis: ad efficiency decomposition, audience mix standardization, CTR, CPC, CPM, and cost per approved conversion.
>   - **Dataset B** powers on-site consumer behavior diagnostics: returning vs new visitor engagement, exit/bounce dynamics, traffic-type intent differences, and behavioral segment propensity.

---

## 4. Analytical Taxonomy: Real vs Derived vs Hypothesis

To maintain analytical integrity, every artifact in this repository classifies information into one of five categories:

1. **Real Public Data**: Raw, unedited observations directly present in the source files (e.g., `Impressions = 8,128,187`, `Clicks = 1,984`, `Spent = $2,893.37`).
2. **Derived Metrics**: Mathematical computations aggregated strictly using ratio-of-sums (e.g., $\text{CTR} = 0.0244\%$, $\text{CPM} = \$0.356$, $\text{Cost per Approved} = \$15.81$).
3. **Analyst Interpretation**: Observational inferences drawn from quantitative patterns (e.g., Campaign 1178 shows creative/audience fatigue at scale, diluting post-click conversion rates).
4. **Hypothesis**: Plausible behavioral explanations formulated to explain observed performance gaps (e.g., "The ad copy in Campaign 1178 may have set expectations not fulfilled by the post-click enquiry form").
5. **Proposed Experiment**: Structured, un-run growth tests designed with controls, variants, primary KPIs, and guardrails to validate hypotheses empirically.
