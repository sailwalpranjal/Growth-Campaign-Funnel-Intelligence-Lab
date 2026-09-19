# Metric Definitions & Availability Boundary Framework

This document establishes the formal definitions, mathematical formulas, and data availability boundaries for all metrics used in the **Growth Campaign & Funnel Intelligence Lab**.

---

## 1. Metric Availability & Integrity Table

In performance marketing and growth analytics, disciplined reporting requires distinguishing between metrics that are **directly supported by observable data** versus metrics that require **unobserved upstream/downstream variables**.

| Metric Name | Available? | Formula / Aggregation Method | Data Source | Analytical Role & Operational Boundary |
| :--- | :--- | :--- | :--- | :--- |
| **Impressions** | **Yes** | $\sum \text{Impressions}$ | Ad Network Delivery Log | Top-of-funnel reach / ad display count. |
| **Clicks** | **Yes** | $\sum \text{Clicks}$ | Ad Network Interaction Log | Volume of user traffic navigating off-platform. |
| **Spend** | **Yes** | $\sum \text{Spent}$ | Paid Media Billing Ledger | Direct media dollar investment. |
| **CTR (Click-Through Rate)** | **Yes** | $\frac{\sum \text{Clicks}}{\sum \text{Impressions}}$ | Ratio-of-Sums Derived | Creative resonance and audience hook efficiency. |
| **CPC (Cost Per Click)** | **Yes** | $\frac{\sum \text{Spent}}{\sum \text{Clicks}}$ | Ratio-of-Sums Derived | Auction competitiveness and media buying efficiency. |
| **CPM (Cost Per Mille)** | **Yes** | $\frac{\sum \text{Spent}}{\sum \text{Impressions}} \times 1000$ | Ratio-of-Sums Derived | Baseline inventory pricing across audience targets. |
| **Total Conversions (Enquiries)** | **Yes** | $\sum \text{Total\_Conversion}$ | Landing Page Event Log | Top-of-funnel lead intent / form submission. |
| **Approved Conversions** | **Yes** | $\sum \text{Approved\_Conversion}$ | CRM / Backend Qualification | Verified lead, approved merchant, or completed order. |
| **Click-to-Approved Rate** | **Yes** | $\frac{\sum \text{Approved\_Conversion}}{\sum \text{Clicks}}$ | Ratio-of-Sums Derived | End-to-end post-click acquisition efficiency. |
| **Cost Per Approved Conversion** | **Yes** | $\frac{\sum \text{Spent}}{\sum \text{Approved\_Conversion}}$ | Ratio-of-Sums Derived | **Strictly labeled as Cost per Approved Conversion** (NOT CAC). |
| **CAC (Customer Acquisition Cost)** | **No (Unsupported)** | *N/A* | *Unobserved* | Requires fully loaded marketing costs, blended organic attribution, agency retainers, and net retention. |
| **ROAS (Return on Ad Spend)** | **No (Unsupported)** | *N/A* | *Unobserved* | Ad dataset records integer conversion counts, NOT monetary purchase amounts. Fabricating revenue violates analytical integrity. |
| **Mobile App Installs** | **No (Unavailable)** | *N/A* | *Unobserved* | Dataset tracks web conversion pixels, not mobile SDK attribution (e.g. AppsFlyer / Adjust). |
| **User Login / Onboarding** | **No (Unavailable)** | *N/A* | *Unobserved* | In-app user session and authentication logs do not exist in this public advertising dataset. |

---

## 2. Why "Spend / Approved Conversions" is NOT Customer Acquisition Cost (CAC)

A common mistake made by inexperienced analysts is equating direct ad spend divided by conversion counts with Customer Acquisition Cost (CAC). In this project, we deliberately and explicitly reject that label in favor of **Cost per Approved Conversion**.

### Key Differences Between Paid Unit Cost and True CAC:
1. **Exclusion of Non-Working Spend**: True CAC includes agency fees, creative production costs, analytics tooling (Adjust, Segment, Mixpanel), martech infrastructure, and growth team salaries. Direct ad spend represents only working media.
2. **Attribution & Blended Dynamics**: An ad click that results in an "Approved Conversion" may reflect brand search cannibalization or view-through re-engagement rather than net-new incremental merchant acquisition. True CAC evaluates blended paid + organic payback.
3. **Activation & Post-Install Drop-Off**: In SaaS and Fintech businesses like Khatabook, an approved signup or lead is not an acquired customer until they reach the **"Aha! Moment"** (e.g., adding their first customer, recording 3 transactions, or setting up a QR code). Labeling top-of-funnel form approvals as "CAC" artificially inflates perceived growth efficiency.

---

## 3. Why ROAS Cannot Be Calculated for This Dataset

Return on Ad Spend (ROAS) is defined as:
$$\text{ROAS} = \frac{\text{Attributed Revenue Generated}}{\text{Total Ad Media Spend}}$$

In the Kaggle Sales Conversion Tracking dataset:
* `Total_Conversion` reflects the number of people who enquired about the product.
* `Approved_Conversion` reflects the number of people who bought the product or were approved.
* **Critically, the transaction value (in dollars) is not provided.**

### Why Fabricating Revenue is Fatal to Analysis:
Assigning an arbitrary average order value (e.g. assuming every conversion is worth \$100) creates synthetic ROAS that reflects the analyst's hardcoded assumption rather than true commercial performance. Analytical discipline requires reporting what is observable:
* We know **Cost per Approved Conversion** in Campaign 936 was **\$15.81**.
* We know **Cost per Approved Conversion** in Campaign 1178 was **\$63.83**.
* Unless the average margin in Campaign 1178 was 400% higher than Campaign 936 (unlikely for identical products), Campaign 1178 represents substantial unit economic degradation.

---

## 4. Aggregation Methodology: Ratio-of-Sums vs. Row-Level Averaging

All aggregate rates in this lab are computed using **ratio-of-sums**, defined as:
$$\text{Metric}_{\text{agg}} = \frac{\sum_{i=1}^N \text{Numerator}_i}{\sum_{i=1}^N \text{Denominator}_i}$$

### Why Never Average Row-Level Ratios:
Averaging row-level rates $\frac{1}{N}\sum \frac{\text{Numerator}_i}{\text{Denominator}_i}$ assigns equal weight to an ad that received 10 impressions and an ad that received 1,000,000 impressions. This introduces severe **Simpson's Paradox** and distorts campaign comparisons.

**Proof with Real Data:**
* In Campaign 1178, true Ratio-of-Sums CTR is **0.0176%** ($\frac{36,068 \text{ clicks}}{204,823,716 \text{ impressions}}$).
* Unweighted row-averaged CTR across Campaign 1178 ad rows is **0.0162%** (understating true CTR by -7.9%).
* Across all 1,143 ads in the dataset, unweighted row-averaging yields **0.0164%** vs true ratio-of-sums **0.0179%** (-8.2% understated).
* Unweighted row-averaging violates aggregation integrity by assigning equal weight to micro-budget ad sets with minimal impressions and scaled ad sets with millions of impressions. Strict ratio-of-sums aggregation is mandatory for all executive reporting.
