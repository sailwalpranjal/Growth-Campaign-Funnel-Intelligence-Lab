# Growth Analytics Methodology & Mathematical Formulations

This document provides complete mathematical derivations and procedural documentation for all analytical frameworks implemented in the **Growth Campaign & Funnel Intelligence Lab**.

---

## 1. Mathematical 3-Factor Efficiency Decomposition Bridge

The centerpiece of campaign diagnostics is decomposing unit conversion cost into three distinct, non-overlapping growth levers.

### The Identity:
$$\text{Cost per Approved Conversion} = \frac{\text{Spend}}{\text{Approved}} = \underbrace{\frac{\text{Spend}}{\text{Impressions}}}_{L_1} \times \underbrace{\frac{\text{Impressions}}{\text{Clicks}}}_{L_2} \times \underbrace{\frac{\text{Clicks}}{\text{Approved}}}_{L_3}$$

Where:
* **Lever 1 ($L_1$) — Inventory Cost Efficiency**:
  $$L_1 = \frac{\text{Spend}}{\text{Impressions}} = \frac{\text{CPM}}{1000}$$
  Reflects media buying auction dynamics, audience competition, and ad delivery efficiency.
* **Lever 2 ($L_2$) — Creative Appeal Friction**:
  $$L_2 = \frac{\text{Impressions}}{\text{Clicks}} = \frac{1}{\text{CTR}}$$
  Represents how many ad views are required to generate one click. Higher values indicate weaker creative resonance.
* **Lever 3 ($L_3$) — Downstream Qualification Resistance**:
  $$L_3 = \frac{\text{Clicks}}{\text{Approved}} = \frac{1}{\text{Click-to-Approved Rate}}$$
  Represents how many landing clicks are required to yield one approved conversion. Higher values indicate landing page friction, intent mismatch, or lead disqualification.

### Sequential Step Substitution (Exact Attribution)
To explain the dollar difference between Baseline Campaign $A$ (936) and Scaled Campaign $B$ (1178):
$$\Delta \text{Cost} = C_B - C_A = L_{1B} L_{2B} L_{3B} - L_{1A} L_{2A} L_{3A}$$

We decompose $\Delta \text{Cost}$ into a telescoping sum:
$$\Delta \text{Cost} = \underbrace{(L_{1B} - L_{1A}) L_{2A} L_{3A}}_{\text{CPM Effect } (\Delta_1)} + \underbrace{L_{1B} (L_{2B} - L_{2A}) L_{3A}}_{\text{CTR Effect } (\Delta_2)} + \underbrace{L_{1B} L_{2B} (L_{3B} - L_{3A})}_{\text{Post-Click Conversion Effect } (\Delta_3)}$$

**Mathematical Proof of Zero Residual:**
$$\Delta_1 + \Delta_2 + \Delta_3 = (L_{1B} L_{2A} L_{3A} - L_{1A} L_{2A} L_{3A}) + (L_{1B} L_{2B} L_{3A} - L_{1B} L_{2A} L_{3A}) + (L_{1B} L_{2B} L_{3B} - L_{1B} L_{2B} L_{3A})$$
Canceling intermediate terms leaves:
$$= L_{1B} L_{2B} L_{3B} - L_{1A} L_{2A} L_{3A} = C_B - C_A \equiv \Delta \text{Cost}$$
This proves that 100.000% of the cost variance is mathematically accounted for without arbitrary estimation error.

---

## 2. Direct Standardization & Audience Mix-Adjustment

When comparing two marketing campaigns, an observed cost advantage may reflect either:
1. **True Intra-Segment Efficiency**: Superior creative, bidding, or copy within the same audiences.
2. **Audience Composition Skew**: Targeting a demographic that is inherently cheaper or easier to convert.

To isolate these effects, we implement **Direct Standardization** (the epidemiological standard for confounding control).

### Standardization Math:
1. **Benchmark Audience Weights ($w_s$)**:
   Pooled share of audience clicks across both campaigns:
   $$w_s = \frac{\sum_{c \in \{936, 1178\}} \text{Clicks}_{c, s}}{\sum_{c \in \{936, 1178\}} \text{Clicks}_c}$$
   Where $\sum_s w_s = 1.0$.
2. **Segment-Specific Conversion Cost ($\text{Cost}_{c, s}$)**:
   $$\text{Cost}_{c, s} = \frac{\text{Spend}_{c, s}}{\text{Approved}_{c, s}}$$
3. **Mix-Adjusted Cost ($\text{AdjCost}_c$)**:
   $$\text{AdjCost}_c = \sum_{s \in S} w_s \cdot \text{Cost}_{c, s}$$
4. **Mix Effect Gap**:
   $$\text{Mix Effect} = \text{AdjCost}_c - \text{RawCost}_c$$

### Analytical Role:
This module answers: *"If Campaign 936 and Campaign 1178 had faced the exact same audience demographic proportions, would Campaign 936 still hold its cost advantage?"*

---

## 3. Segment Stability & Minimum-Sample Sensitivity

Small segments in digital ad accounts frequently display deceptively attractive conversion rates due to small-sample variance. To prevent budget misallocation:

### Sensitivity Thresholds Tested:
* **Threshold 1 (10 Clicks)**: Filters absolute noise where a single conversion yields artificial 10%+ rates.
* **Threshold 2 (25 Clicks)**: Minimum directional benchmark for paid social ad sets.
* **Threshold 3 (50 Clicks)**: Statistically defensible volume required for stable decision-making.

### Classification Taxonomy:
* **Stable**: Segment qualifies for Threshold 3 ($\ge 50$ clicks) and maintains consistent performance ranking.
* **Sample-Sensitive**: Segment qualifies at 25 clicks but drops out at 50 clicks; cost estimates are fragile.
* **Low-Sample**: $10 \le \text{Clicks} < 25$. Directional only; requires sample accumulation before scaling.
* **Unreliable**: $\text{Clicks} < 10$. Excluded from strategic optimization.

---

## 4. Statistical Testing Engine & Decision Matrix

### Two-Proportion Z-Test:
For testing conversion rates $p_1 = x_1 / n_1$ and $p_2 = x_2 / n_2$:
$$\text{Null Hypothesis } H_0: p_1 = p_2 \quad \text{vs} \quad H_1: p_1 \ne p_2$$

**Pooled Proportion & Standard Error:**
$$p_{\text{pool}} = \frac{x_1 + x_2}{n_1 + n_2}, \quad \text{SE}_{\text{pool}} = \sqrt{p_{\text{pool}}(1 - p_{\text{pool}})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$$
$$z = \frac{p_2 - p_1}{\text{SE}_{\text{pool}}}, \quad p\text{-value} = 2 \cdot (1 - \Phi(|z|))$$

### 95% Confidence Interval for Absolute Lift:
$$\text{SE}_{\text{unpooled}} = \sqrt{\frac{p_1(1 - p_1)}{n_1} + \frac{p_2(1 - p_2)}{n_2}}$$
$$\text{CI}_{95\%} = (p_2 - p_1) \pm 1.95996 \cdot \text{SE}_{\text{unpooled}}$$

### Sample Size Planning Formula:
Sample size required per variant for two-tailed test with significance $\alpha$ and power $1 - \beta$:
$$n = \frac{\left(Z_{\alpha/2} \sqrt{2 \bar{p}(1 - \bar{p})} + Z_{\beta} \sqrt{p_1(1 - p_1) + p_2(1 - p_2)}\right)^2}{(p_2 - p_1)^2}$$
Where $p_2 = p_1 (1 + \text{MDE})$.
