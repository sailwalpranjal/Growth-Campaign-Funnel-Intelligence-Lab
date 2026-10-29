# Metrics

Nobody but me uses this yet, so this document is a plan for how I would know it was useful. Nothing below has been measured.

## What I would want to know

1. Do visitors reach the Waterfall and Growth OS tabs, or leave from the first screen?
2. Are the downloads (CSV exports, Excel model) used?
3. Does the page change what someone decides? This one needs a conversation, not a log.

## Events I would add

The dashboard is a static page, so a privacy-friendly analytics script (Plausible or Umami, for example) plus a few custom events:

| Event | Properties | Question it answers |
|---|---|---|
| `tab_view` | `tab` | Which tabs get read |
| `info_panel_open` | `metric` | Whether people check how a number is built |
| `export_download` | `file` | Whether the data gets used |
| `ab_calculator_run` | `result_state` | Whether the calculator is used and what it concludes |

For the API: one log line per request with route, status and latency, and a daily count per `/api/*` route.

## Queries

```sql
-- tab reach, last 30 days
SELECT tab, COUNT(DISTINCT session_id) AS sessions
FROM events
WHERE name = 'tab_view' AND ts >= date('now', '-30 day')
GROUP BY tab
ORDER BY sessions DESC;
```

## The guardrail that exists today

`tests/test_headline_numbers.py` recomputes each quoted number from the raw CSVs and scans the published text for known stale phrases. It runs in CI on every push.
