### Deployment Playbook (`DEPLOYMENT_PLAYBOOK.md`)

```markdown
# Standard Operating Procedure: Analytics Pipeline Deployment

## Document Purpose
This runbook details the local execution of the Support Operations Data Pipeline. It provides step-by-step instructions for an engineer to initialize the local database, execute the Python-based ETL scripts, and connect the transformed data to a Business Intelligence platform.

## Phase 1: Environment Setup

**1. Directory Initialization**
Ensure the local environment mirrors the repository structure. You must manually create a `data/` directory within the `03_Analytics_Pipeline` folder before running scripts.

**2. Python Dependencies**
Ensure the host machine has Python installed along with the `pandas` library.
* Command: `pip install pandas`
* Note: `sqlite3` is part of the Python standard library and requires no external installation.

## Phase 2: Database Initialization (Extract)

**1. Execute Data Generator**
* Navigate to the `src/` directory in your terminal.
* Execute the initialization script: `python 01_generate_data.py`
* **Validation:** Verify that `analytics_practice.db` has been successfully generated inside the `data/` directory. This file contains raw, unstructured ticket data.

## Phase 3: Data Transformation (ETL)

**1. Execute Pipeline Script**
* Remain in the `src/` directory.
* Execute the ETL script: `python 02_etl_process.py`
* **System Action:** The script establishes a connection to the SQLite database, standardizes text casing via Pandas, drops blank/invalid rows, calculates multi-tier SLA compliance (24hr VIP / 48hr Standard), and handles null values.
* **Validation:** Verify that `kpi_summary.csv` has been successfully generated inside the `data/` directory.

## Phase 4: Business Intelligence Integration (Load)

**1. BI Tool Ingestion**
* Open a BI tool of choice (Google Sheets, Looker Studio, Power BI, Excel).
* Import the `data/kpi_summary.csv` dataset.

**2. Dashboard Configuration (Dual-Axis Chart)**
* Create a Pivot Table summarizing data by `customer_tier`.
* Calculate the `COUNTA` of `ticket_id` (representing Volume).
* Calculate the `AVERAGE` of `sla_compliant` (representing Success Rate percentage).
* Generate a Combo Chart plotting Volume as Columns (Left Axis) and SLA Compliance as a Line/Floating Column (Right Axis).
