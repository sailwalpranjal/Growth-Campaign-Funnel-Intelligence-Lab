# Analytical & Methodological Audit Dossier

This dossier establishes the exact mathematical proofs, data lineage, statistical formulas, and verification methods implemented across the **Growth Campaign & Funnel Intelligence Platform**.

---

## 1. Mathematical Proofs & Variance Identities

### Proof 1.1: Exact Three-Factor Efficiency Decomposition
Cost per Approved Conversion is expressed as the product of three distinct commercial levers:

$$\text{Cost per Approved} = \left(\frac{\text{Spend}}{\text{Impressions}}\right) \times \left(\frac{\text{Impressions}}{\text{Clicks}}\right) \times \left(\frac{\text{Clicks}}{\text{Approved}}\right) = \left(\frac{\text{CPM}}{1000}\right) \times \left(\frac{1}{\text{CTR}}\right) \times \left(\frac{1}{\text{ConvRate}}\right)$$

Let $C_0$ be baseline unit cost (Campaign 936) and $C_1$ be scaled unit cost (Campaign 1178). Under sequential substitution:
1. $\text{Step}_1 = \left(\frac{\text{CPM}_1}{1000}\right) \times \left(\frac{1}{\text{CTR}_0}\right) \times \left(\frac{1}{\text{ConvRate}_0}\right)$
   $$\text{Lever}_1 (\text{CPM Effect}) = \text{Step}_1 - C_0 = \$12.072 - \$15.811 = -\$3.739$$
2. $\text{Step}_2 = \left(\frac{\text{CPM}_1}{1000}\right) \times \left(\frac{1}{\text{CTR}_1}\right) \times \left(\frac{1}{\text{ConvRate}_0}\right)$
   $$\text{Lever}_2 (\text{CTR Effect}) = \text{Step}_2 - \text{Step}_1 = \$16.732 - \$12.072 = +\$4.660$$
3. $\text{Step}_3 = \left(\frac{\text{CPM}_1}{1000}\right) \times \left(\frac{1}{\text{CTR}_1}\right) \times \left(\frac{1}{\text{ConvRate}_1}\right) = C_1$
   $$\text{Lever}_3 (\text{Conversion Effect}) = \text{Step}_3 - \text{Step}_2 = \$63.833 - \$16.732 = +\$47.101$$

$$\text{Total Explained Variance} = (-\$3.739) + (+\$4.660) + (+\$47.101) = +\$48.022$$
$$\text{Reconciliation Residual} = |\Delta C - (\text{Lever}_1 + \text{Lever}_2 + \text{Lever}_3)| = \$0.00000000$$

* **Code Implementation**: [`src/diagnostics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/src/diagnostics.py#L19-L85)
* **SQL Pipeline**: [`sql/03_metrics.sql`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/sql/03_metrics.sql#L31-L36)
* **Unit Test**: [`tests/test_diagnostics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/tests/test_diagnostics.py#L12-L28) (passes within $10^{-6}$ precision).

---

### Proof 1.2: Direct Standardization & Confounding Adjustment
To adjust for demographic composition, we compute the pooled benchmark click distribution across all 4 age categories:

$$w_i = \frac{\sum_{c} \text{Clicks}_{c, i}}{\sum_{c} \sum_{i} \text{Clicks}_{c, i}}$$

For each campaign $c$, the standardized unit cost is:

$$\text{Cost}_{\text{adj}, c} = \sum_{i} w_i \times \text{Cost per Approved}_{c, i}$$

$$\text{Cost}_{\text{adj}, 936} = \$23.69 \quad \text{vs} \quad \text{Cost}_{\text{adj}, 1178} = \$78.16$$

* **Code Implementation**: [`src/diagnostics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/src/diagnostics.py#L140-L205)
* **SQL Pipeline**: [`sql/05_mix_analysis.sql`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/sql/05_mix_analysis.sql#L10-L65)
* **Unit Test**: [`tests/test_diagnostics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/tests/test_diagnostics.py#L42-L55)

---

### Proof 1.3: Two-Proportion Hypothesis Testing & Normal Approximation
For test evaluation, pooled proportion under the null hypothesis $H_0: p_1 = p_2$:

$$\hat{p} = \frac{x_1 + x_2}{n_1 + n_2}$$
$$\text{SE}_{\text{pooled}} = \sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$$
$$z = \frac{\hat{p}_1 - \hat{p}_2}{\text{SE}_{\text{pooled}}}$$
$$p\text{-value} = 2 \times \left(1 - \Phi(|z|)\right)$$

The 95% Confidence Interval for the difference $p_1 - p_2$ is:

$$\text{CI}_{95\%} = (\hat{p}_1 - \hat{p}_2) \pm 1.96 \times \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$$

* **Code Implementation**: [`src/statistics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/src/statistics.py#L15-L85)
* **Unit Test**: [`tests/test_statistics.py`](file:///e:/Growth%20Campaign%20&%20Funnel%20Intelligence%20Lab/tests/test_statistics.py#L12-L40)

---

## 2. Code, Metric & File Traceability Matrix

| Analytical Dimension | Source Code Implementation | SQL Pipeline File | Primary Export Deliverable | Verification Test |
| :--- | :--- | :--- | :--- | :--- |
| **Ratio-of-Sums Scorecard** | `src/metrics.py` | `sql/03_metrics.sql` | `exports/campaign_scorecard.csv` | `tests/test_metrics.py` |
| **Efficiency Waterfall** | `src/diagnostics.py` | `sql/03_metrics.sql` | `reports/campaign_diagnostic.md` | `tests/test_diagnostics.py` |
| **4-Stage Funnel Drop-off** | `src/diagnostics.py` | `sql/06_funnel.sql` | `exports/funnel_analysis.csv` | `tests/test_funnel.py` |
| **Segment Stability ($\ge 10, 25, 50$)**| `src/diagnostics.py` | `sql/04_audience.sql` | `exports/segment_stability.csv` | `tests/test_diagnostics.py` |
| **Direct Standardization** | `src/diagnostics.py` | `sql/05_mix_analysis.sql`| `exports/mix_analysis.csv` | `tests/test_diagnostics.py` |
| **A/B Testing & Sizing Engine** | `src/statistics.py` | — | Embedded in API & Dashboard | `tests/test_statistics.py` |
| **11-Rule Data Quality Audit** | `src/validation.py` | `sql/07_quality.sql` | `exports/data_quality.csv` | `tests/test_quality.py` |
| **Consumer Session Intent** | `src/data_loader.py` | `sql/02_clean.sql` | `exports/consumer_behavior.csv` | `tests/test_metrics.py` |
| **FastAPI REST Endpoints** | `backend/main.py` | — | OpenAPI Swagger `/docs` | `tests/test_backend.py` |
| **Web Visualizer Platform** | `web/index.html`, `js/` | — | Vercel Live Deployment | Local Server Test (HTTP 200) |
