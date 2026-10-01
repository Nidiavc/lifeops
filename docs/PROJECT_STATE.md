# LifeOps - Project State

## Overview

LifeOps is a personal observability platform developed in Python.

The objective is to apply observability, analytics, data management and software engineering concepts to personal productivity, health and finance metrics.

The project stores information in SQLite and provides historical analysis, trend detection and metric insights.

---

# Current Version

LifeOps v0.6

---

# Architecture

```text
lifeops/

├── app
│   ├── database
│   │   └── storage.py
│   │
│   ├── models
│   │   ├── area.py
│   │   ├── metric.py
│   │   ├── metric_entry.py
│   │   ├── goal.py
│   │   └── event.py
│   │
│   ├── services
│   │   ├── dashboard.py
│   │   ├── lifeops_app.py
│   │   ├── metrics_service.py
│   │   ├── trend_service.py
│   │   ├── insights_service.py
│   │   ├── weekly_analytics_service.py
│   │   └── summary_dashboard.py
│   │
│   ├── lifeops.db
│   └── main.py
│
├── tests
│   ├── test_trend_service.py
│   ├── test_insights_service.py
│   └── test_weekly_analytics_service.py
│
├── docs
│   └── PROJECT_STATE.md
│
└── README.md
```

---

# Database

SQLite

Database file:

```text
lifeops.db
```

Current tables:

## metrics

```text
id
name
unit
```

Example:

```text
1 | Study Hours | Hours
2 | Sleep Hours | Hours
3 | Savings | CLP
```

---

## metric_entries

```text
id
metric_id
metric_name
value
entry_date
```

Example:

```text
1 | 1 | Study Hours | 3 | 2026-10-01
```

---

## goals

```text
id
title
progress
```

Example:

```text
1 | Get Power BI Certification | 35
```

---

# Metrics

Current metrics:

## Study Hours

Measures learning and certification effort.

Unit:

```text
Hours
```

---

## Sleep Hours

Measures rest and recovery.

Unit:

```text
Hours
```

---

## Savings

Measures personal savings evolution.

Unit:

```text
CLP
```

---

# Available Analytics

## Basic Statistics

Implemented through:

```python
metrics_service.py
```

Provides:

- Average

---

## SQL Statistics

Implemented through:

```python
storage.py
```

Provides:

- Average
- Min
- Max
- Count
- Latest Value

---

## Daily Analytics

Provides:

- Historical averages by day
- Latest value by date

---

## Trend Analysis

Implemented through:

```python
trend_service.py
```

Provides:

- Increasing
- Decreasing
- Stable
- Growth percentage
- Absolute variation

---

## Historical Insights

Implemented through:

```python
insights_service.py
```

Provides:

- Highest average day
- Lowest average day
- Historical average
- Days with records

---

## Weekly Analytics

Implemented through:

```python
weekly_analytics_service.py
```

Provides:

- Weekly averages
- Highest week
- Lowest week
- Weekly growth
- Weekly trend

---

# Quality Controls

## Source Control

Git

## Remote Repository

GitHub

## Unit Tests

Implemented:

```text
test_trend_service.py
test_insights_service.py
test_weekly_analytics_service.py
```

Current status:

```text
12 tests passing
```

---

# Current Limitations

The project currently works with:

```text
Console Output
```

No graphical dashboards are available yet.

Weekly analytics currently require data from multiple weeks.

---

# Planned Features

## v0.7

Monthly Analytics

Features:

- Monthly averages
- Monthly growth
- Monthly trends

---

## v0.8

Visualization

Features:

- Matplotlib charts
- Trend charts
- Weekly charts
- Monthly charts

---

## v0.9

Observability Reporting

Features:

- Health reports
- Productivity reports
- Finance reports

---

## v1.0

Personal Observability Platform

Features:

- Interactive dashboards
- Advanced analytics
- KPI tracking
- Goal monitoring
- Historical reporting

---

# Learning Objectives

This project is intended to demonstrate knowledge in:

- Python
- SQLite
- Git
- GitHub
- Unit Testing
- Analytics
- Data Persistence
- Observability Concepts
- Software Architecture
- Object-Oriented Programming