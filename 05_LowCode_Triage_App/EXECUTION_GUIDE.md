## Click-by-Click Execution Guide: Building the Retool App

Follow these exact steps to build the application. You do not need any prior experience with Retool to execute this.

**Phase 1: Spin up Retool & Seed the Database (The Dataverse Alternative)**

Retool Database is a free, built-in PostgreSQL database. We will use their visual builder, which perfectly mimics Microsoft Dataverse.

Create Account: Go to Retool.com and sign up for a free account.

Navigate to Database: On your Retool dashboard, look at the top navigation bar and click Database.

Create the Table:

Click the + Create button (usually near the top right) and select Blank Table.

Name the table: support_tickets

Configure the Columns:

Retool gives you an id column and a created_at column by default. Leave those alone.

Click the + icon next to the column headers to add a new field. Name it customer_name (Type: Text).

Click + to add another field. Name it issue_description (Type: Long Text / Text).

Click + to add another field. Name it status (Type: Text).

Seed the Data:

Just like an Excel spreadsheet, click directly into the empty rows on the screen and type in a few fake tickets to populate your database.

Row 1: Alice Smith | Cannot access AWS | New

Row 2: Bob Jones | Monitor won't turn on | New

Row 3: Charlie Brown | Need SAP password reset | New

**Phase 2: Build the Low-Code UI (The Power Apps Alternative)**

Create the App (Important Step):

Click the Apps tab in the top navigation bar.

Click Create new -> App.

Crucial: If it asks for a template, ensure you select Blank App or Web App (Do NOT select Chat or AI). Name it "IT Ticket Triage".

Connect the Data:

Look at the Left Sidebar. You should see a little icon that looks like </> (Code). Click it to open the Code panel.

Click the + button in that Code panel.

Select Resource query.

Select Retool Database as your resource.

Write this SQL query in the text box: SELECT * FROM support_tickets ORDER BY id ASC;

Click the Save & Run button (usually a blue triangle or play button).

Name this query getTickets at the top of its settings.

Build the Table:

Still on the left-hand side, click the + Add icon (Components library) right above or below the code icon.

Drag a Table component onto the middle of your blank canvas.

Click on the table. On the right-hand Inspector panel, look for Data Source.

Change it from the demo data to {{ getTickets.data }}. You will instantly see your database rows appear in the UI.

**Phase 3: Wire the Automation (The Power Automate Alternative)**

Add the Action Button:

Drag a Button component from the left panel and drop it below your table.

On the right-hand Inspector panel, change the button text to "Escalate Selected Ticket".

Change the button color to Red to indicate an escalation action.

Create the Update Logic:

Go back to the left sidebar and click the </> (Code) icon again.

Click + -> Resource query.

Select Retool Database again.

Name this query escalateTicket.

Crucial Step: Choose GUI mode instead of SQL mode (to show off low-code skills).

Action type: Choose Update an existing record.

Table: Select support_tickets.

Filter by: id = {{ table1.selectedRow.id }} (This tells it to target whatever row you clicked on in the UI).

Changeset: Column status = Escalated.

Click Save.

Tie the Button to the Logic:

Click your red button on the canvas.

On the right panel, find Event Handlers. Click + Add.

Set it to: Action -> Control query -> Query -> escalateTicket.

Close the Loop (Refresh the UI):

Go back to your escalateTicket query in the code panel.

Look for the Event Handlers section inside the query settings.

Add a new handler: On Success -> Trigger query -> getTickets.

(This ensures that when you escalate a ticket, the table instantly refreshes to show the new status!)
