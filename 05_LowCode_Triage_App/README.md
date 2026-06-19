## Low-Code IT Support Triage Application

**Objective**

This project demonstrates the ability to identify "Swivel Chair" workflow inefficiencies and rapidly deploy a low-code operational solution. It serves as an architectural equivalent to a Microsoft Power Apps + Dataverse environment, utilizing Retool to build a unified frontend interface connected to a relational database backend with automated action triggers.

**Methodology: The "Process Detective" Framework**

This application was built to solve a specific enterprise bottleneck by identifying workflows that meet three criteria:

High Volume: Tasks occurring dozens or hundreds of times daily (e.g., tier-one ticket triage).

Rule-Based: Strict logical routing without the need for complex human judgment.

Data-Heavy: Moving structured data from an inbox or queue into a CRM or Database.

By replacing manual ticket triage with a centralized low-code app, this solution eliminates manual data entry errors and standardizes the workflow pipeline.

**Tech Stack & Architecture Mapping**

Frontend UI (Retool Canvas): Acts as the architectural equivalent to Microsoft Power Apps, providing a drag-and-drop component library to build user interfaces without raw HTML/CSS.

Backend Database (PostgreSQL): Acts as the architectural equivalent to Microsoft Dataverse, providing a secure, relational backend data layer.

Automation Logic (Event Handlers): Acts as the architectural equivalent to Power Automate, binding custom SQL UPDATE statements to UI actions to eliminate manual status changes.

**Application Workflow**

Data Ingestion: The application interfaces securely with a backend database containing incoming IT support requests.

Interactive UI: A real-time data table surfaces the tickets to the agent without requiring them to write SQL queries.

Automated Escalate Action: A button click triggers an automated UPDATE query, instantly changing the ticket status to "Escalated" based on the exact row selected in the UI.

Instant UI Refresh: The frontend automatically re-syncs with the database upon successful execution to show the updated ticket queue.

**Repository Structure**

/assets - Visual documentation, including screenshots of the Retool UI dashboard and the backend database schema.

EXECUTION_GUIDE.md - Step-by-step documentation detailing how the application logic and database were configured.

## Visual Architecture

**Frontend Interface (Power Apps Alternative)**
![App Dashboard](assets/app_dashboard_view.png)

**Backend Database (Dataverse Alternative)**
![Database Schema](assets/database_schema.png)
