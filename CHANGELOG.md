# Changelog

All notable changes are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow semantic versioning. Versions below 1.0.0 mean numbers and interfaces may still change.

## [Unreleased]

## [0.2.0] - proposed tag `v0.2.0`

### Fixed
- The experiment backlog and dashboard text quoted figures that failed recomputation. New visitors convert at 24.91% against 13.93% for returning visitors (not "3.5x higher" for returning). Female CPA is $69.70 against $41.44 for male, not $68.20 and $42.10.
- Interest 27 is the highest-CPA interest among those with at least 50 approved conversions, not the highest overall. Another 13 interests have under 10 approved conversions and are too noisy to rank.
- README click total corrected from 38,181 to 38,165.
- Gender CTR in the limitations doc corrected to 0.0208% and 0.0145%.

### Added
- `tests/test_headline_numbers.py`, which recomputes the headline numbers and scans published files for stale claims.
- MIT licence, CI workflow, issue and pull request templates, contributing, security and conduct files.
- Product documents under `docs/product/`.

## [0.1.0] - proposed tag `v0.1.0`

First public version: SQL pipeline, three-factor cost bridge, funnel, audience stability, mix adjustment, A/B calculator, ICE backlog, 16-tab dashboard and FastAPI backend.
