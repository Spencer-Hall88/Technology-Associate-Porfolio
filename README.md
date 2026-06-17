# enterprise-automation-portfolio

Welcome to my technical portfolio. This repository contains functional prototypes and architectural models demonstrating my ability to build automated workflows, configure AI agents, and manage data pipelines using modern low-code and Python-based ecosystems.

**Core Competencies Demonstrated**

AI Agent Orchestration: Copilot prompting frameworks, LLM integrations, and autonomous agent tool-calling.

Workflow Automation: Webhook-driven pipelines, automated data entry, and API integrations.

Data Engineering & Analytics: SQL aggregations, Python (Pandas) ETL pipelines, and BI data modeling.

Lightweight App Development: Streamlit and SQL-backed internal tools for rapid operational solutions.

**Project 01: Intelligent Document Automation (M365 Copilot Simulation)**

Objective: Automate the generation of formatted executive reports from unstructured chat and log data.

Tech Stack: Python, python-docx, LLM API (OpenAI/Local).

Architecture: Ingests raw .txt chat transcripts, applies Microsoft's Goal-Context-Source-Expectation prompting framework via API to extract key insights, and automatically generates a formatted .docx Incident Report.

Business Value: Eliminates manual data synthesis and standardizes documentation formatting, replicating the core functionality of M365 Copilot document automation.

**Project 02: Autonomous Data Agent (n8n & LLM Orchestration)**

Objective: Build an autonomous AI agent capable of routing requests and querying databases.

Tech Stack: n8n (Node-based automation), Python, Webhooks, LLMs.

Architecture: Configured an n8n webhook trigger to receive data payloads. Integrated an AI Agent node with Window Buffer Memory and custom tools (Calculator, Code Executor) to simulate a dynamic "think-act-observe" loop, completely bypassing rigid deterministic workflows.

Business Value: Demonstrates advanced agent orchestration equivalent to Copilot Studio, proving the ability to build AI that safely interacts with internal enterprise data.

**Project 03: Support Analytics Data Pipeline (SQL & Python ETL)**

Objective: Process raw operational data into a clean, BI-ready semantic model.

Tech Stack: SQLite, Python (Pandas), Advanced Excel/BI concepts.

Architecture: Constructed a local SQLite database to house raw ticketing data. Wrote SQL aggregations to calculate Average Resolution Time (ART) and SLA compliance. Utilized Pandas for ETL cleanup (handling nulls, standardizing formats) and exported a pristine dataset modeled for Star Schema ingestion.

Business Value: Showcases a complete understanding of the data lifecycle—from backend relational databases to semantic layers used in Power BI and executive dashboards.

**Project 04: AI-Assisted Lightweight App (Streamlit Asset Tracker)**

Objective: Rapidly prototype an internal operational tool using AI-assisted development.

Tech Stack: Python, Streamlit, SQLite, LLM Code Generation.

Architecture: Leveraged an AI-assisted development environment to generate boilerplate code for a full-stack internal tool. The application features a dual-tab frontend UI mapped directly to local SQL INSERT and SELECT statements.

Business Value: Demonstrates "speed-to-value" development. Proves architectural understanding of how low-code frontends (like Power Apps) securely bind to relational databases (like Dataverse).

Prepared for technical review and interview discussion.
