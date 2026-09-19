# Growth Experiment Backlog & Prioritization Matrix

All proposed experiments follow the **Evidence $\to$ Hypothesis $\to$ Test $\to$ Guardrail** growth framework.  
*Note: These are structured growth proposals derived from empirical patterns; they are not claimed to have been run in production.*

---

## Experiment Backlog Table (Ranked by ICE Score)

| Priority | ID | Experiment Title | Target Audience | Test Variable | Primary KPI | Guardrail | ICE Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P0 (Immediate Sprint)** | `EXP-GROWTH-001` | **Ad Creative Value Prop Realignment for Scaled Campaigns** | Scaled acquisition audience (broad demographic, ages 30-49, top interest categories). | Ad Creative Hook & Headline Messaging | Click-to-Approved Conversion Rate (%) | CTR must not drop below 0.012% (protect traffic volume) | **8.67** |
| **P0 (Immediate Sprint)** | `EXP-GROWTH-002` | **Post-Click Landing Form Friction Reduction & Micro-Commitment** | All post-click web traffic from paid campaigns. | Landing Page Form Architecture | Click-to-Total Conversion (Enquiry) Rate (%) | Total-to-Approved qualification rate must remain >= 30% (protect lead quality). | **8.00** |
| **P0 (Immediate Sprint)** | `EXP-GROWTH-003` | **Audience Concentration & Budget Reallocation to Stable Interest Segments** | Campaign budget allocation across interest categories. | Audience Targeting Concentration | Blended Cost per Approved Conversion ($) | Weekly impression delivery volume must not decline by more than 15%. | **8.67** |
| **P1 (Next Sprint)** | `EXP-GROWTH-004` | **Returning Visitor Personalized High-Intent Nudge (Consumer Behavior)** | Returning visitors on web/mobile sessions. | On-site Returning Visitor Modal / Top-Banner | Session-to-Purchase Conversion Rate (%) | Session bounce rate must not increase by > 2% absolute. | **7.00** |
| **P1 (Next Sprint)** | `EXP-GROWTH-005` | **Demographic Gender-Specific Creative Framing Test** | Female business owners aged 30-49. | Landing Page Merchant Vertical Imagery & Testimonials | Post-Click Approved Conversion Rate (%) | CPC must not increase by > 10%. | **7.00** |

---

## Detailed Experiment Design Cards

### `EXP-GROWTH-001`: Ad Creative Value Prop Realignment for Scaled Campaigns
* **Priority**: P0 (Immediate Sprint) (ICE: 8.67) — *Directly attacks the largest source of cost leakage ($48.02 cost-per-approved surge).*
* **Observed Evidence**: Campaign 1178 spent $55,662.15 (19.2x the budget of Campaign 936 at $2,893.37) and achieved lower CPM ($0.27 vs $0.36), but post-click approved conversion collapsed by 73.8% (from 9.22% in Camp 936 to 2.42% in Camp 1178), causing cost per approved conversion to inflate from $15.81 to $63.83 (+303.7%).
* **Hypothesis**: Broad-reach ad creatives in Campaign 1178 set generic or misaligned user expectations that fail to convert on the post-click enquiry form. Replacing generic reach hooks with high-intent SMB pain-point hooks (e.g., 'Track daily udhaar payments instantly') will filter low-intent clicks and improve post-click conversion.
* **Control**: Generic broad benefit creative: 'Grow your business with smart digital tools'
* **Variant**: High-intent operational pain-point creative: 'Stop losing money to forgotten credits: 1-click ledger tracking'
* **Primary KPI**: Click-to-Approved Conversion Rate (%)
* **Secondary KPI**: Cost per Approved Conversion ($)
* **Guardrail**: CTR must not drop below 0.012% (protect traffic volume)
* **Success Criteria**: >= +25% relative lift in click-to-approved conversion rate with p < 0.05 and no CAC degradation
* **Expected Learning**: Determines whether qualification-focused copy improves downstream unit economics at scale.
* **Data Requirements**: Impression, click, enquiry, and approved conversion tracking at creative level.

---
### `EXP-GROWTH-002`: Post-Click Landing Form Friction Reduction & Micro-Commitment
* **Priority**: P0 (Immediate Sprint) (ICE: 8.00) — *High leverage on 36,000+ clicks where 92.6% currently bounce without converting.*
* **Observed Evidence**: Funnel drop-off analysis reveals that 92.6% of users who click Campaign 1178 ads drop off before completing the initial enquiry form (Click-to-Enquiry is only 7.40% vs 27.07% in Campaign 936).
* **Hypothesis**: The current post-click enquiry form requires too many fields upfront. Replacing the single multi-field form with a 2-step micro-commitment form (Step 1: Business category selection, Step 2: Contact info) will reduce cognitive friction and increase completion rates.
* **Control**: Single-page static form with 5 mandatory fields (Name, Phone, City, Business Type, Revenue).
* **Variant**: Progressive 2-step form: Step 1 (1-tap business type chip), Step 2 (Phone number OTP autofill).
* **Primary KPI**: Click-to-Total Conversion (Enquiry) Rate (%)
* **Secondary KPI**: Form Initiation Rate (%)
* **Guardrail**: Total-to-Approved qualification rate must remain >= 30% (protect lead quality).
* **Success Criteria**: >= +20% lift in total conversion rate with p < 0.05 and no drop in approval rate.
* **Expected Learning**: Identifies whether top-of-funnel conversion leakage is caused by UX form fatigue.
* **Data Requirements**: Session-level form field analytics, step completion timestamps, and approval backend sync.

---
### `EXP-GROWTH-003`: Audience Concentration & Budget Reallocation to Stable Interest Segments
* **Priority**: P0 (Immediate Sprint) (ICE: 8.67) — *Zero engineering required; actionable immediately within ad campaign budget settings.*
* **Observed Evidence**: Audience segment stability analysis across all 40 interest categories reveals that Interest 27 carries the highest cost per approved conversion at $95.85 (54 conversions on $5,176.17 spend across 3,409 clicks), whereas top efficient scaled interests like ID 16 ($57.34 CPA across 5,144 clicks) and ID 10 ($55.89 CPA across 3,317 clicks) demonstrate proven scale. Reallocating spend away from high-CPA clusters into high-intent stable clusters optimizes blended unit economics.
* **Hypothesis**: Reallocating 30% of media budget away from unstable, fragmented interest segments into the top 5 sample-stable segments will improve overall blended campaign efficiency by eliminating long-tail spend waste.
* **Control**: Fragmented broad targeting across all 40 interest codes.
* **Variant**: Concentrated tier-1 targeting strictly limited to stable interest clusters with >50 clicks history.
* **Primary KPI**: Blended Cost per Approved Conversion ($)
* **Secondary KPI**: Total Approved Conversions per Week
* **Guardrail**: Weekly impression delivery volume must not decline by more than 15%.
* **Success Criteria**: >= 15% reduction in blended cost per approved conversion without frequency spike.
* **Expected Learning**: Tests the tradeoff between demographic scale and segment conversion efficiency.
* **Data Requirements**: Campaign budget split, weekly ad spend, and segment-level approved conversions.

---
### `EXP-GROWTH-004`: Returning Visitor Personalized High-Intent Nudge (Consumer Behavior)
* **Priority**: P1 (Next Sprint) (ICE: 7.00) — *Capitalizes on high baseline intent with proven behavioral divergence.*
* **Observed Evidence**: UCI consumer diagnostics reveal that Returning Visitors convert at 13.93% (1,470/10,551) compared to 24.91% (422/1,694) for New Visitors—a 44.1% conversion deficit—with an average cart exit rate of 0.0465 and average page value of $5.01 vs $10.77 for New Visitors. Personalizing returning merchant sessions addresses the sharp drop-off observed post-initial visit.
* **Hypothesis**: Displaying a personalized re-engagement banner ('Continue where you left off + free merchant QR setup') to returning visitors within 5 seconds of session start will increase transaction completion.
* **Control**: Standard landing view with generic homepage promotions.
* **Variant**: Personalized sticky top-bar showing last viewed feature with 1-click resume CTA.
* **Primary KPI**: Session-to-Purchase Conversion Rate (%)
* **Secondary KPI**: Add-to-Cart / Feature Usage Initiation Rate (%)
* **Guardrail**: Session bounce rate must not increase by > 2% absolute.
* **Success Criteria**: >= +12% relative lift in transaction rate among returning cohort with p < 0.05.
* **Expected Learning**: Quantifies the conversion lift of context-aware personalization for high-intent users.
* **Data Requirements**: Cookie/session identity persistence, on-site event stream, transaction confirmation webhook.

---
### `EXP-GROWTH-005`: Demographic Gender-Specific Creative Framing Test
* **Priority**: P1 (Next Sprint) (ICE: 7.00) — *High initial click engagement indicates strong top-of-funnel resonance that is currently squandered.*
* **Observed Evidence**: Audience analysis reveals Female segments generate higher CTR (0.0208% vs 0.0145% for Males, +43.4% higher) but incur higher cost per approved conversion ($69.70 vs $41.44 for Males, +68.2% higher) due to post-click conversion friction (2.07% vs 4.09%).
* **Hypothesis**: Current creative hooks appeal to female SMB owners' visual interest but downstream product copy is tailored predominantly to male-dominated wholesale trade. Creating retail/apparel-specific merchant landing copy for female audiences will bridge the post-click intent gap.
* **Control**: General wholesale distribution merchant testimonials and imagery.
* **Variant**: Retail, boutique, and local apparel merchant testimonials and workflow screenshots.
* **Primary KPI**: Post-Click Approved Conversion Rate (%)
* **Secondary KPI**: Cost per Approved Conversion ($)
* **Guardrail**: CPC must not increase by > 10%.
* **Success Criteria**: >= 20% reduction in Cost per Approved Conversion for Female cohort.
* **Expected Learning**: Reveals whether demographic conversion gaps are structural or artifacts of vertical misrepresentation.
* **Data Requirements**: Gender-segmented ad sets, separate landing page URLs, conversion tracking.

---
