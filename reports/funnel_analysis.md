# Acquisition Funnel & Drop-Off Intelligence

## 1. Observable Multi-Stage Acquisition Funnel

This analysis models only real observable stages in the advertising dataset:
`Impressions` $\to$ `Clicks` $\to$ `Total Conversions (Enquiries)` $\to$ `Approved Conversions`.

| Campaign ID | Stage 1: Impressions | Stage 2: Clicks | Stage 3: Total Enquiries | Stage 4: Approved Conversions | Step 1 $\to$ 2 (CTR) | Step 2 $\to$ 3 (Enquiry Rate) | Step 3 $\to$ 4 (Approval Rate) | Cumulative Conversion |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **916** | 482,925 | 113 | 58 | 24 | 0.0234% | 51.33% | 41.38% | 0.004970% |
| **936** | 8,128,187 | 1,984 | 537 | 183 | 0.0244% | 27.07% | 34.08% | 0.002251% |
| **1178** | 204,823,716 | 36,068 | 2,669 | 872 | 0.0176% | 7.40% | 32.67% | 0.000426% |

---

## 2. Drop-Off Diagnostic & Leakage Mapping

### Relative Drop-Off by Stage
1. **Impressions $\to$ Clicks**: 99.98% drop-off (Standard social display ad benchmark).
2. **Clicks $\to$ Total Conversions (Enquiries)**:
   * Campaign 916: 48.7% drop-off (51.3% conversion)
   * Campaign 936: 72.9% drop-off (27.1% conversion)
   * **Campaign 1178: 92.6% drop-off (7.4% conversion) — CRITICAL BOTTLENECK**
3. **Total Conversions $\to$ Approved Conversions**:
   * Campaign 916: 58.6% drop-off (41.4% approval)
   * Campaign 936: 65.9% drop-off (34.1% approval)
   * Campaign 1178: 67.3% drop-off (32.7% approval)

### Key Finding
The drop-off between Stage 3 (Enquiry) and Stage 4 (Approval) is remarkably consistent between Campaign 936 (34.1% approved) and Campaign 1178 (32.7% approved). This proves that **once a user initiates an enquiry, their qualification rate is virtually identical**. The failure occurs entirely between the ad click and the form submission.
