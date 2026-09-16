-- ==============================================================================
-- 01_staging.sql
-- Ingestion DDL for raw advertising and consumer behavior datasets
-- Compatible with PostgreSQL and SQLite
-- ==============================================================================

-- Staging table for Ad Campaign Conversion Tracking (Dataset A)
DROP TABLE IF EXISTS stg_ad_campaigns;

CREATE TABLE stg_ad_campaigns (
    ad_id               BIGINT PRIMARY KEY,
    xyz_campaign_id     INTEGER NOT NULL,
    fb_campaign_id      BIGINT NOT NULL,
    age                 VARCHAR(20) NOT NULL,
    gender              VARCHAR(5) NOT NULL,
    interest            INTEGER NOT NULL,
    impressions         BIGINT NOT NULL,
    clicks              BIGINT NOT NULL,
    spent               NUMERIC(12, 4) NOT NULL,
    total_conversion    BIGINT NOT NULL,
    approved_conversion BIGINT NOT NULL
);

-- Staging table for Consumer Behavior & On-site Sessions (Dataset B)
DROP TABLE IF EXISTS stg_consumer_behavior;

CREATE TABLE stg_consumer_behavior (
    session_id                  INTEGER PRIMARY KEY,
    administrative              INTEGER NOT NULL,
    administrative_duration     NUMERIC(10, 4) NOT NULL,
    informational               INTEGER NOT NULL,
    informational_duration      NUMERIC(10, 4) NOT NULL,
    product_related             INTEGER NOT NULL,
    product_related_duration    NUMERIC(12, 4) NOT NULL,
    bounce_rates                NUMERIC(8, 6) NOT NULL,
    exit_rates                  NUMERIC(8, 6) NOT NULL,
    page_values                 NUMERIC(10, 4) NOT NULL,
    special_day                 NUMERIC(4, 2) NOT NULL,
    month                       VARCHAR(10) NOT NULL,
    operating_systems           INTEGER NOT NULL,
    browser                     INTEGER NOT NULL,
    region                      INTEGER NOT NULL,
    traffic_type                INTEGER NOT NULL,
    visitor_type                VARCHAR(30) NOT NULL,
    weekend                     BOOLEAN NOT NULL,
    revenue                     BOOLEAN -- Can be NULL in raw data (data quality audit target)
);
