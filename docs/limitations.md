# Methodological Limitations & Analytical Boundaries

A defining hallmark of a senior growth analyst is knowing **what data CANNOT tell you**. This document defines the methodological boundaries, unobserved variables, and causal limitations of the **Growth Campaign & Funnel Intelligence Lab**.

---

## 1. Observational vs. Causal Inference Boundaries

All findings derived in this repository are based on **observational data**, not randomized controlled split-cell experiments.

### Why We Cannot Claim Causal Attribution:
1. **Lack of Simultaneous A/B Split**: The three campaigns (`916`, `936`, `1178`) were not deployed as concurrent, randomly assigned split tests against the same audience pool. They may represent sequential growth phases where Campaign 916 was an early pilot, Campaign 936 was a targeted test, and Campaign 1178 was an aggressive budget scale.
2. **Uncontrolled Seasonality & Macro Trends**: If Campaign 1178 was run during a competitive holiday window or off-peak business season, external economic headwinds may explain part of the conversion decline.
3. **Audience Saturation / Frequency Fatigue**: Aggressive scaling to \$55,662 in a single campaign typically increases ad frequency, exhausting the immediate ready-to-convert audience pool. This is an observational pattern, not proof of creative failure.

> [!WARNING]
> **Core Growth Rule**: Never claim causality from observational ad reports. Formulate hypotheses and validate them through prospectively randomized A/B experiments.

---

## 2. Unobserved Variables in the Advertising Dataset

| Unobserved Variable | Operational Consequence for Growth Team | How We Address It in This Project |
| :--- | :--- | :--- |
| **Ad Creative Copy & Visuals** | We cannot visually verify whether Campaign 1178 used video vs. image, or different value propositions. | We treat creative misalignment as a **hypothesis framework** rather than an established fact. |
| **Bidding Strategy & Optimization Goal** | We do not know if Campaign 936 was bid on Cost Cap while Campaign 1178 used Lowest Cost / Maximum Volume. | We decompose CPM and CPC to observe auction price dynamics without assuming manual vs. automated bidding. |
| **Landing Page Versioning** | If the destination landing page changed between campaigns, post-click drop-off could be an engineering/UX bug rather than ad mismatch. | We propose structured A/B tests with identical landing environments to isolate the variable. |
| **Downstream Revenue & LTV** | We cannot observe customer lifetime value, retention rate, or average transaction size. | We refuse to calculate synthetic ROAS and strictly evaluate Cost per Approved Conversion. |

---

## 3. Consumer Behavior Dataset Boundaries (UCI Dataset)

The secondary analysis on 12,330 e-commerce sessions provides valuable behavioral diagnostics, but also carries strict observational constraints:

### Association vs. Causation in Web Analytics:
* **Page Values**: High page values correlate with high purchase conversion ($r > 0.45$). However, visiting high-value pages (such as the cart or checkout review) is an **indicator of high pre-existing purchase intent**, not a marketing lever that automatically causes a passive user to buy.
* **Product Duration**: Users who spend >600 seconds convert at 28.4% vs 4.8% for users spending <120 seconds. This does not imply that artificially lengthening the merchant onboarding flow will increase conversion; rather, engaged users voluntarily invest time.

---

## 4. Summary: What Must NOT Be Concluded

1. **Do NOT conclude that Campaign 1178 was a failure**: In high-growth startups, scaling spend from \$2,800 to \$55,000 often requires accepting higher unit costs to achieve market share and absolute conversion volume (872 vs 183 approvals).
2. **Do NOT conclude that older age brackets should be turned off**: Although users aged 45-49 have higher CPCs and higher cost per approved conversion, older business owners frequently exhibit lower churn and higher average balances. Without cohort retention data, turning off segments prematurely damages LTV.
3. **Do NOT conclude that female business owners are less qualified**: Female segments show higher CTR (0.024% vs 0.016%) but drop off on the landing page form. This points to vertical relevance issues in landing page imagery, not lower intrinsic merchant qualification.
