# Cross-Functional Experiment Brief Template

This document provides an end-to-end experiment brief standardizing collaboration across **Growth, Creative, Analytics, Product, and CRM** teams for full-funnel growth initiatives.

---

## Experiment Brief: EXP-GROWTH-001 — Value Prop Qualification Alignment

### 1. Business Context & Objective
* **Business Question**: Why did scaling Campaign 1178 cause post-click approved conversion to collapse by 73.8% (from 9.22% to 2.42%), and can pre-qualifying ad messaging restore unit economics without choking click volume?
* **Objective**: Reduce Cost per Approved Conversion from \$63.83 to below \$35.00 at scale by replacing generic reach hooks with high-intent operational pain-point messaging.

---

### 2. Hypothesis & Behavioral Rationale
* **Hypothesis**: Generic ad copy (*"Grow your business with smart digital tools"*) attracts casual clickers who abandon the landing page when faced with business verification. Testing operational pain-point hooks (*"Stop losing ₹5,000/month to forgotten udhaar: 1-click WhatsApp ledger"*) will pre-qualify user intent on the ad unit itself, improving post-click conversion efficiency.
* **Target Audience**: Scaled acquisition audience (Ages 30-49, top 5 stable interest segments).

---

### 3. Test Design & Traffic Split
* **Test Architecture**: 50/50 randomized split-cell test on Meta / Google Ads network.
* **Sample Size Requirement**: 17,400 clicks per variant (calculated in `src/statistics.py` to detect a +20% relative lift with 80% power at $\alpha=0.05$).
* **Test Duration**: 14 calendar days (capturing full weekly merchant trading cycles).

| Cell | Name | Ad Creative Hook | Landing Page Experience |
| :--- | :--- | :--- | :--- |
| **Control (50%)** | Broad Reach Control | *"Smart Digital Tools for Local Merchants"* | Standard mobile landing page form. |
| **Variant A (50%)** | Operational Intent Hook | *"Recover Pending Udhaar 3x Faster via WhatsApp"* | Same landing page with pre-filled headline matching ad hook. |

---

### 4. Cross-Functional Deliverables & Responsibilities

#### A. Growth (Performance Marketing)
* Set up isolated 50/50 split-cell campaign structure with identical audience targeting and automated budget distribution.
* Enforce bid caps to ensure CPM parity between control and treatment variants.

#### B. Creative & Copywriting Team
* Produce 3 creative format variations (1:1 static card, 4:5 motion graphic, 9:16 vertical short) for Variant A highlighting customer ledger balance and WhatsApp reminder alert UI.
* Maintain consistent typography, brand colors, and vernacular copy in Hindi, Hinglish, and regional languages.

#### C. Product Experience Team
* Implement message matching: dynamically adapt the hero headline on the landing page based on UTM tag `utm_campaign=exp_001_variant` to reinforce the specific ad hook.
* Monitor mobile landing page load performance (< 1.5s on 4G connections).

#### D. Analytics Team
* Configure client-side event tracking (`view_landing_page`, `form_field_focused`, `form_submitted`, `lead_approved`).
* Maintain real-time tracking dashboard monitoring ratio-of-sums conversion rates, p-values, and guardrails.
* Cross-check daily data against backend CRM approval logs to eliminate attribution lag.

#### E. CRM & Lifecycle Marketing Team
* Set up automated follow-up WhatsApp/SMS welcome drip triggered within 60 seconds of form submission.
* Align CRM copy to reference the specific hook ("Here is your link to start tracking daily udhaar").

---

### 5. Metrics, Guardrails & Decision Matrix

* **Primary KPI**: Click-to-Approved Conversion Rate ($\frac{\sum \text{Approved}}{\sum \text{Clicks}}$). Target: $\ge 3.0\%$ (+24% relative lift).
* **Secondary KPI**: Cost per Approved Conversion ($\frac{\sum \text{Spend}}{\sum \text{Approved}}$). Target: $\le \$35.00$.
* **Guardrail Metric 1**: Click-Through Rate (CTR) must not drop below 0.014% (protect traffic volume from over-filtering).
* **Guardrail Metric 2**: Enquiry-to-Approved qualification rate must not decline (ensure lead quality is preserved).

### Decision Rules:
1. **Rollout Variant**: If $p < 0.05$, relative lift $\ge +15\%$, and both guardrails hold $\to$ Shift 100% of scaled campaign budget to Variant A.
2. **Iterate & Retest**: If $p < 0.05$ but CTR dropped below 0.014% $\to$ Soften headline copy to broaden appeal while preserving qualification.
3. **Terminate Variant**: If $p < 0.05$ with negative lift, or if lead approval rate collapses $\to$ Halt test immediately.
