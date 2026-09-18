# Campaign Diagnostic & 3-Factor Efficiency Decomposition

## 1. Ratio-of-Sums Campaign Scorecard

| Campaign ID | Total Ads | Impressions | Clicks | Spend ($) | Total Conv | Approved Conv | CTR (%) | CPC ($) | CPM ($) | Click-to-Approved (%) | Cost / Approved ($) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **916** | 54 | 482,925 | 113 | $149.71 | 58 | 24 | 0.0234% | $1.32 | $0.310 | 21.24% | **$6.24** |
| **936** | 464 | 8,128,187 | 1,984 | $2,893.37 | 537 | 183 | 0.0244% | $1.46 | $0.356 | 9.22% | **$15.81** |
| **1178** | 625 | 204,823,716 | 36,068 | $55,662.15 | 2,669 | 872 | 0.0176% | $1.54 | $0.272 | 2.42% | **$63.83** |

---

## 2. Mathematical 3-Factor Efficiency Decomposition Bridge

To diagnose why **Campaign 1178** cost **$63.83** per approved conversion compared to **$15.81** for **Campaign 936** (a gap of **$48.02**), we express unit cost as the exact product of three independent levers:

$$\text{Cost per Approved} = \underbrace{\frac{\text{Spend}}{\text{Impressions}}}_{L_1: \text{CPM} / 1000} \times \underbrace{\frac{\text{Impressions}}{\text{Clicks}}}_{L_2: 1 / \text{CTR}} \times \underbrace{\frac{\text{Clicks}}{\text{Approved}}}_{L_3: 1 / \text{Conversion Rate}}$$

### Sequential Waterfall Attribution

| Lever | Metric Definition | Campaign 936 Value | Campaign 1178 Value | Dollar Impact on Cost Difference | Relative Contribution (%) | Directional Implication |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Lever 1 (CPM Effect)** | Cost per Impression | $0.000356 | $0.000272 | **-$3.74** | -7.8% | **Advantage Campaign 1178**: Cheaper inventory at scale. |
| **Lever 2 (CTR Effect)** | Impressions per Click | 4096.9 | 5678.8 | **+$4.66** | +9.7% | **Disadvantage Campaign 1178**: 27.9% creative CTR decay. |
| **Lever 3 (Post-Click Conv)** | Clicks per Approved | 10.8 | 41.4 | **+$47.10** | **+98.1%** | **Primary Leakage**: Post-click conversion dropped by 73.8%. |
| **Total Reconciled Gap** | Sum of Levers | $15.81 | $63.83 | **+$48.02** | **100.0%** | **Mathematically Exact Identity** (Error: $0.00000000) |

### Growth Analyst Takeaway
Scaling ad budget 19.2x unlocked media buying efficiencies (lower CPM), but generated low-intent clicks that failed downstream. Growth optimization must prioritize post-click relevance and creative qualification over auction bidding optimizations.
