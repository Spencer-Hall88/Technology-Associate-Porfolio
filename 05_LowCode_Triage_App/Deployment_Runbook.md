# Standard Operating Procedure: IT Triage Dashboard Deployment

## Document Purpose

This runbook details the deployment steps and architectural configuration for the Low-Code IT Support Triage application. It provides the necessary specifications for an engineer to replicate the database schema, frontend UI bindings, and event-driven automation logic.

## Phase 1: Database Initialization

*This phase provisions the PostgreSQL backend, acting as the relational data layer (architectural equivalent to Microsoft Dataverse).*

**1. Schema Creation**

* Initialize a new PostgreSQL database environment via the Retool Database interface.

* Configure the database schema by establishing the `support_tickets` table with the following parameters:

  * `id` (Integer, Primary Key, Auto-Increment)

  * `customer_name` (Text)

  * `issue_description` (Text)

  * `status` (Text)

  * `created_at` (Timestamp/Date)

**2. Data Seeding**

* Populate the table with initial mock data representing incoming tier-one support requests to validate downstream UI rendering.

## Phase 2: Frontend Dashboard Configuration

*This phase constructs the presentation layer, bridging the database to a user-friendly interface (architectural equivalent to Microsoft Power Apps).*

**1. Data Retrieval Query (`getTickets`)**

* Initialize a new blank web application.

* Within the application scope, configure a new Resource Query targeting the PostgreSQL database.

* **Query String:** `SELECT * FROM support_tickets ORDER BY id ASC;`

* **Purpose:** This query establishes the initial data payload that will populate the frontend application state.

**2. UI Data Binding**

* Deploy a **Table** component to the application canvas.

* Map the Table's Data Source parameter to evaluate the application state: `{{ getTickets.data }}`.

* **Strategic Benefit:** Binding the component directly to the query object ensures the UI remains synced with the backend data layer without requiring manual state management.

## Phase 3: Event-Driven Automation Logic

*This phase configures the action triggers and database mutations (architectural equivalent to Microsoft Power Automate).*

**1. Action Query Configuration (`escalateTicket`)**

* Initialize a new Resource Query configured for Page-level scope (ensure the query is nested under the specific page utilizing the Table component).

* **Action Type:** Update an existing record.

* **Target Table:** `support_tickets`

* **Filter Condition:** `id` = `{{ table1.selectedRow.id }}`

* **Changeset:** `status` = `Escalated`

* **Strategic Benefit:** Scoping the filter dynamically to the `selectedRow.id` ensures the query targets strictly the exact record highlighted by the user, preventing blanket database updates.

**2. Event Handler Orchestration**

* Deploy a **Button** component labeled "Escalate Ticket".

* Bind an Event Handler to the Button's `Click` action to trigger the `escalateTicket` query.

* Navigate to the `escalateTicket` query settings and bind an `On Success` Event Handler to trigger the `getTickets` query.

* **Strategic Benefit:** This orchestration loop (Action -> Database Mutation -> Auto-Refresh) eliminates the need for the user to manually refresh the browser, providing a seamless "zero-touch" UI experience upon escalation.
