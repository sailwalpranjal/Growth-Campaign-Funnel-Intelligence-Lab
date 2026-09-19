# CRM Experiment Planning Framework

This document outlines a standardized, production-ready framework for lifecycle and CRM experimentation across **WhatsApp, SMS, Push Notifications, and In-App Channels**.

*Methodological Guardrail: This framework demonstrates lifecycle growth strategy, trigger mechanics, and measurement architecture. In compliance with project data ethics, it does NOT simulate fake delivery metrics or fabricate mock campaign telemetry.*

---

## 1. CRM Lifecycle Funnel Stage Mapping

In a fintech/bookkeeping ecosystem like Khatabook, the CRM lifecycle spans four distinct user transition phases:

```text
[Signup / Lead Submitted]
       │  (Trigger: 0-10 min)
       ▼
[Onboarding & Activation] ──▶ Add First Customer / Record 1st Transaction
       │  (Trigger: Days 1-3)
       ▼
[Habit Formation / Daily Use] ──▶ Send Daily WhatsApp Payment Reminder / View Balance
       │  (Trigger: Days 7-14)
       ▼
[Monetization & Retention] ──▶ QR Soundbox, Digital Invoicing, Merchant Credit
```

---

## 2. Reusable CRM Experiment Template

```markdown
### CRM Experiment Specification Sheet

* **Experiment ID**: CRM-EXP-[NUM]
* **Lifecycle Stage**: [Activation / Re-engagement / Retention / Cross-Sell]
* **Target Segment**: [Exact behavioral trigger criteria and exclusion filters]
* **Behavioral Barrier**: [Why users currently drop off at this lifecycle milestone]
* **Message Hypothesis**: [If we communicate X via Channel Y at Time Z, then users will do A because B]

#### Channel & Dispatch Mechanics
* **Channel**: [WhatsApp / SMS / Push Notification / In-App Message]
* **Trigger Condition**: [Event-based real-time trigger or scheduled batch]
* **Delivery Window**: [Local merchant time window, e.g. 09:30 AM - 11:00 AM or 08:00 PM - 09:30 PM]
* **Frequency Cap**: [Maximum message count per merchant per 7-day period]

#### Message Variants
* **Control (50%)**: [Standard transactional/operational notification]
* **Variant A (50%)**: [Personalized behavioral nudge with localized vernacular copy]

#### Measurement & Guardrails
* **Primary KPI**: [Action completion rate within 24 hours of dispatch]
* **Secondary KPI**: [7-day repeat feature usage rate]
* **Guardrail Metric**: [Unsubscribe / App uninstallation rate / Notification opt-out rate]
* **Statistical Plan**: [Minimum sample required, 14-day holdout evaluation, two-proportion z-test]
```

---

## 3. Production CRM Experiment Scenarios for Khatabook

### Scenario 1: Onboarding Drop-off — Zero First Transaction
* **Experiment ID**: `CRM-EXP-001`
* **Target Segment**: Newly approved merchants who registered 24 hours ago but have added 0 customer entries (`first_transaction_logged = False`).
* **Behavioral Barrier**: Local shop owners get busy with customers and forget to transfer their paper records to the app.
* **Hypothesis**: Sending a personalized WhatsApp message showing an example Kirana ledger entry with a 1-tap link to add a customer will trigger immediate activation.
* **Channel**: WhatsApp Business API (High open rate in India).
* **Timing**: Evening store closing window (08:30 PM - 09:15 PM local time when the merchant balances cash registers).
* **Control**: Standard SMS notification: *"Thank you for registering on Khatabook. Open the app to start adding your customers."*
* **Variant**: Vernacular WhatsApp message with interactive quick-reply button:  
  *"Namaste Ramesh ji! 🏪 Aaj dukaandaari ka hisaab khatam? Bas 1 minute mein pehle customer ka udhaar likhein aur chinta-mukt ho jaayein. [Button: Pehla Hisaab Likhein]"*
* **Primary KPI**: D1 Customer Entry Rate (`% of merchants adding >= 1 customer within 24 hours of message`).
* **Secondary KPI**: D7 Active Ledger Days.
* **Guardrail**: WhatsApp block/report rate must remain below 0.1%.
* **Measurement Plan**: 50/50 split via customer segment ID hash; evaluate 48-hour event attribution using backend transaction logs.

---

### Scenario 2: Active Ledger Users — Payment Reminder Adoption
* **Experiment ID**: `CRM-EXP-002`
* **Target Segment**: Merchants with active customer balances > ₹5,000 who have never used the "Automated WhatsApp Reminder" feature.
* **Behavioral Barrier**: Merchants fear offending neighborhood customers by sending automated reminders.
* **Hypothesis**: Educating merchants on the polite, customizable tone of Khatabook's reminder templates will overcome social embarrassment and drive reminder feature adoption.
* **Channel**: In-App Full-Screen Modal on 3rd app open.
* **Timing**: Immediately upon opening the customer credit balance tab.
* **Control**: Standard blue banner: *"Send automated WhatsApp payment reminders to collect money faster."*
* **Variant**: Social-proof testimonial modal:  
  *"92% dukaandaar kehte hain: Khatabook ke polite WhatsApp reminder se dosti bhi bani rehti hai aur udhaar 3x tez vasool hota hai. [Preview Sample Polite Message] [Button: Bhej kar dekhein]"*
* **Primary KPI**: First-Time Reminder Dispatch Rate (% of targeted merchants sending >= 1 reminder).
* **Secondary KPI**: 14-Day Payment Collection Volume (₹).
* **Guardrail**: App session drop-off (modal dismiss rate).
* **Measurement Plan**: Client-side feature flag split; tracked via mixpanel/in-app analytics event stream.
