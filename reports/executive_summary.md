# Executive Growth Memo — Campaign & Funnel Intelligence Lab

**To:** VP of Growth / Growth Hiring Team  
**From:** Growth Analytics & Performance Team  
**Date:** September 2026  
**Subject:** Growth Diagnostic: Root-Cause Analysis of 4.0x Cost Surge in Scaled Acquisition and Next Test Backlog  

---

### Executive Summary in 60 Seconds
When scaling ad acquisition from **Campaign 936** ($2,893 spend, 183 approved conversions) to **Campaign 1178** ($55,662 spend, 872 approved conversions), our cost per approved conversion increased dramatically from **$15.81** to **$63.83** (+303.7% cost inflation).

Through rigorous **three-factor efficiency decomposition**, direct audience-mix standardization, and multi-stage funnel diagnostics on 1,143 ad records, we uncovered that this cost explosion was **NOT** caused by media auction competition (CPM actually decreased from $0.356 to $0.272) nor by demographic audience skew. Rather, it was driven almost entirely by **post-click conversion collapse**: click-to-approved conversion plummeted from **9.22%** to **2.42%**, leaking 92.6% of clicks before form completion.

---

### 1. What Happened?
Across three distinct campaigns in our public social acquisition dataset:
* **Campaign 916 (Early Pilot)**: Spent $149.71, generated 24 approved conversions at **$6.24** per approved conversion.
* **Campaign 936 (Mid-Scale Focused)**: Spent $2,893.37, generated 183 approved conversions at **$15.81** per approved conversion.
* **Campaign 1178 (Broad Scaled)**: Spent $55,662.15, generated 872 approved conversions at **$63.83** per approved conversion.

### 2. Which Campaign Performed Differently?
**Campaign 1178** absorbed 94.8% of total budget but exhibited severe unit economic degradation, costing **$48.02 more per approved conversion** than Campaign 936.

### 3. Why Does the Data Suggest the Difference Happened? (Efficiency Bridge)
Decomposing unit cost into three underlying levers reveals the exact sequential attribution:
* **CPM Lever Contribution**: **-$3.74** (Favorable effect — Campaign 1178 purchased media 23.6% cheaper).
* **CTR Lever Contribution**: **+$4.66** (Unfavorable — CTR dropped from 0.0244% to 0.0176%).
* **Post-Click Conversion Lever Contribution**: **+$47.10** (**Primary Culprit — 98% of total cost degradation**).

* **Demographic Sensitivity**: Female segments demonstrated higher engagement (0.0208% CTR vs 0.0145% for Males, +43.4% higher), but experienced a higher cost per approved conversion ($69.70 vs $41.44) due to severe post-click drop-off (2.07% vs 4.09% conversion rate).
* **Interest Efficiency Dispersion**: Segment analysis across all 40 interest categories reveals significant CPA dispersion: Interest 27 carries the highest CPA at $95.85 (54 conversions on $5,176.17 spend across 3,409 clicks), whereas top efficient scaled clusters like ID 16 ($57.34 CPA) and ID 10 ($55.89 CPA) maintain strong efficiency at scale.

### 5. Where Is the Funnel Leaking?
The primary point of leakage is **Stage 2 -> Stage 3 (Click to Enquiry)**:
* In Campaign 936, 27.1% of clicks submitted an enquiry.
* In Campaign 1178, only 7.40% submitted an enquiry — an astonishing **92.6% drop-off** immediately following the click.
* In contrast, Stage 3 -> Stage 4 (Enquiry to Approved Conversion) remained relatively stable (34.1% in 936 vs 32.7% in 1178). The bottleneck is landing-page qualification and expectation alignment.

### 6. What Is Uncertain? (Known Limitations)
* **Unobserved Creative Text/Visuals**: Dataset lacks ad copy and creative video/image assets; creative fatigue is an inferred hypothesis based on CTR and conversion decay.
* **Post-Conversion Lifetime Value**: The dataset records approved conversions, not downstream revenue, merchant retention, or LTV.
* **Observational Confounding**: Campaigns were not run concurrently as split-cell A/B tests; macro seasonality or bidding strategy shifts cannot be ruled out.

### 7. What Should We Test Next? (Top 3 Prioritized Experiments)
1. **EXP-GROWTH-001 (P0, ICE: 8.67)**: Replace generic scaled ad copy with high-intent operational pain-point messaging to pre-qualify clicks.
2. **EXP-GROWTH-003 (P0, ICE: 8.67)**: Reallocate 30% of budget from long-tail volatile interest targets (<10 clicks) into proven stable interest clusters.
3. **EXP-GROWTH-002 (P0, ICE: 8.00)**: Convert the single-page enquiry form into a 2-step progressive micro-commitment flow to reduce 92.6% post-click drop-off.

### 8. What Should NOT Be Concluded?
* Do **NOT** conclude that Campaign 1178 was poorly managed by performance marketers; aggressive budget scaling naturally reaches saturation without audience segmentation.
* Do **NOT** conclude that Campaign 1178 has a higher CAC; "Cost per approved conversion" is not CAC because it excludes blended organic acquisition, agency fees, and churn.
* Do **NOT** conclude that older audiences are unprofitable; older segments have higher CPCs but require LTV tracking to determine true economic viability.
