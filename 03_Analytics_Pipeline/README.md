# Support Operations Analytics Pipeline

## Objective
Design and execute a local ETL (Extract, Transform, Load) data pipeline that processes raw, unstructured customer support logs and transforms them into an analytics-ready dataset for Business Intelligence reporting.

## Architecture & Tech Stack
* **Data Storage (Backend):** SQLite (Local relational database)
* **Data Extraction & Logic:** SQL (Date arithmetic, backend aggregations)
* **Data Transformation (ETL):** Python (Pandas library)
* **Business Intelligence (Presentation):** Google Sheets / Looker Studio / Power BI

## Methodology: The ETL Framework

**1. Data Ingestion (Extract)**
A Python script generates a localized SQLite database, simulating a raw production environment. It seeds the database with support ticket logs containing deliberate anomalies (missing resolution dates, inconsistent text casing) to mirror real-world dirty data.

**2. Data Transformation (Transform)**
The pipeline utilizes Python's Pandas library to query the SQLite database and perform critical data hygiene:
* Standardizing categorical text fields and dropping null/blank records to ensure BI dashboard integrity.
* Handling NULL values for unresolved tickets.
* Applying dynamic, multi-tier boolean logic to flag SLA compliance (VIP tickets = 24 hours, Standard tickets = 48 hours).

**3. Data Visualization (Load)**
The cleaned dataset is exported as a structured CSV. A dual-axis analytical model was built to track Ticket Volume (Workload) against SLA Adherence (Success Rate) by Customer Tier. This visualization successfully exposed an operational bottleneck: while average resolution hours remained stable, the sheer volume of VIP tickets caused a massive drop in SLA compliance compared to the Standard tier.

## Repository Structure

```text
03_Analytics_Pipeline/
├── assets/
│   └── analytics_dashboard.png    # Dual-axis BI visualization
├── sql/
│   └── kpi_metrics.sql            # Raw SQL logic for backend aggregation
├── src/
│   ├── 01_generate_data.py        # Python script to initialize database
│   └── 02_etl_process.py          # Python script executing Pandas ETL
├── DEPLOYMENT_PLAYBOOK.md         # Standard Operating Procedure for execution
└── README.md                      # Project documentation

## Visual Architecture

**Business Intelligence Dashboard: Ticket Volume vs. SLA Compliance**
![Analytics Dashboard](assets/analytics_dashboard.png)
