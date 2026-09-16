-- ==============================================================================
-- 07_quality.sql
-- Automated Data Quality & Anomaly Detection Audit Log
-- Flags, documents, and quantifies every data integrity condition
-- ==============================================================================

DROP TABLE IF EXISTS audit_data_quality;

CREATE TABLE audit_data_quality AS

-- 1. Missing Values in Ad Campaign Data
SELECT 
    'Dataset A (Ads)' AS dataset,
    'Missing Critical Values' AS check_name,
    COUNT(*) AS flagged_records,
    'Rows with NULL in ad_id, campaign_id, impressions, clicks, or spent' AS description,
    CASE WHEN COUNT(*) = 0 THEN 'PASSED' ELSE 'FAILED' END AS status
FROM stg_ad_campaigns
WHERE ad_id IS NULL OR xyz_campaign_id IS NULL OR impressions IS NULL OR clicks IS NULL OR spent IS NULL

UNION ALL

-- 2. Duplicate Ad IDs
SELECT 
    'Dataset A (Ads)' AS dataset,
    'Duplicate Ad IDs' AS check_name,
    COUNT(*) - COUNT(DISTINCT ad_id) AS flagged_records,
    'Duplicate primary key ad_id occurrences' AS description,
    CASE WHEN COUNT(*) = COUNT(DISTINCT ad_id) THEN 'PASSED' ELSE 'FAILED' END AS status
FROM stg_ad_campaigns

UNION ALL

-- 3. Negative Numeric Values
SELECT 
    'Dataset A (Ads)' AS dataset,
    'Negative Numeric Values' AS check_name,
    COUNT(*) AS flagged_records,
    'Rows with impressions < 0, clicks < 0, or spent < 0' AS description,
    CASE WHEN COUNT(*) = 0 THEN 'PASSED' ELSE 'FAILED' END AS status
FROM stg_ad_campaigns
WHERE impressions < 0 OR clicks < 0 OR spent < 0

UNION ALL

-- 4. Funnel Logic Violation: Clicks > Impressions
SELECT 
    'Dataset A (Ads)' AS dataset,
    'Clicks Exceed Impressions' AS check_name,
    COUNT(*) AS flagged_records,
    'Impossible physical event: Clicks recorded without impressions' AS description,
    CASE WHEN COUNT(*) = 0 THEN 'PASSED' ELSE 'FAILED' END AS status
FROM stg_ad_campaigns
WHERE clicks > impressions

UNION ALL

-- 5. Conversion Logic Violation: Approved > Total Conversions
SELECT 
    'Dataset A (Ads)' AS dataset,
    'Approved Exceeds Total Conversion' AS check_name,
    COUNT(*) AS flagged_records,
    'Logically invalid state: Approved subset is larger than total enquiry set' AS description,
    CASE WHEN COUNT(*) = 0 THEN 'PASSED' ELSE 'FAILED' END AS status
FROM stg_ad_campaigns
WHERE approved_conversion > total_conversion

UNION ALL

-- 6. Zero Clicks with Positive Spend (Ad Budget Waste / Tracking Lag)
SELECT 
    'Dataset A (Ads)' AS dataset,
    'Zero-Click Spend Ads' AS check_name,
    COUNT(*) AS flagged_records,
    'Ads that consumed budget without generating any clicks' AS description,
    CASE WHEN COUNT(*) = 0 THEN 'PASSED' ELSE 'WARNING (Informational)' END AS status
FROM stg_ad_campaigns
WHERE clicks = 0 AND spent > 0

UNION ALL

-- 7. Low Sample Rows (< 10 Clicks)
SELECT 
    'Dataset A (Ads)' AS dataset,
    'Low-Sample Records (< 10 Clicks)' AS check_name,
    COUNT(*) AS flagged_records,
    'Ad records with insufficient sample for standalone rate evaluation' AS description,
    CASE WHEN COUNT(*) > 0 THEN 'FLAGGED (Sample Protection Active)' ELSE 'PASSED' END AS status
FROM stg_ad_campaigns
WHERE clicks < 10

UNION ALL

-- 8. Missing Values in Consumer Behavior Data (Dataset B)
SELECT 
    'Dataset B (UCI Sessions)' AS dataset,
    'Missing Conversion Labels' AS check_name,
    COUNT(*) AS flagged_records,
    'Sessions with NULL Revenue outcome in raw file' AS description,
    CASE WHEN COUNT(*) > 0 THEN 'FLAGGED (Cleaned via View)' ELSE 'PASSED' END AS status
FROM stg_consumer_behavior
WHERE revenue IS NULL;

-- Display Quality Report
SELECT * FROM audit_data_quality;
