import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# --- Database Setup (Dataverse Alternative) ---
def init_db():
    conn = sqlite3.connect('fleet_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS maintenance_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_name TEXT,
            category TEXT,
            issue_description TEXT,
            urgency TEXT,
            status TEXT,
            date_logged TEXT
        )
    ''')
    conn.commit()
    conn.close()

# --- Database Functions ---
def add_log(asset, category, issue, urgency):
    conn = sqlite3.connect('fleet_data.db')
    c = conn.cursor()
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute('INSERT INTO maintenance_logs (asset_name, category, issue_description, urgency, status, date_logged) VALUES (?, ?, ?, ?, ?, ?)', 
              (asset, category, issue, urgency, 'Open', date_now))
    conn.commit()
    conn.close()

def get_data():
    conn = sqlite3.connect('fleet_data.db')
    df = pd.read_sql_query("SELECT * FROM maintenance_logs WHERE status='Open'", conn)
    conn.close()
    return df

# --- Streamlit UI (Power Apps Alternative) ---
st.set_page_config(page_title="Fleet Maintenance Tracker", layout="centered")

st.title("Demo Fleet Maintenance Tracker")
st.markdown("Lightweight asset management interface mapping frontend forms to a relational database.")

init_db()

# Create Tabs
tab1, tab2 = st.tabs(["Log a Maintenance Issue", "View Active Issues"])

with tab1:
    st.header("Report Equipment Damage")
    with st.form("maintenance_form", clear_on_submit=True):
        asset_name = st.text_input("Asset ID / Name (e.g., Stumpjumper 15, Salomon QST 98 L47606800)")
        category = st.selectbox("Equipment Category", ["Mountain Bike", "Ski/Snowboard", "Electronics", "Other"])
        issue_description = st.text_area("Description of Issue (e.g., Bleed brakes, core shot on base)")
        urgency = st.selectbox("Urgency", ["Low", "Medium", "High - Grounded"])
        
        submitted = st.form_submit_button("Submit Ticket")
        if submitted:
            if asset_name and issue_description:
                add_log(asset_name, category, issue_description, urgency)
                st.success("Ticket successfully written to database!")
            else:
                st.error("Please fill out all required fields.")

with tab2:
    st.header("Active Maintenance Queue")
    data = get_data()
    
    if not data.empty:
        # Sort so high urgency is at the top
        urgency_order = {"High - Grounded": 1, "Medium": 2, "Low": 3}
        data['sort_val'] = data['urgency'].map(urgency_order)
        data = data.sort_values('sort_val').drop('sort_val', axis=1)
        
        st.dataframe(data, use_container_width=True, hide_index=True)
    else:
        st.info("No active maintenance issues. Fleet is 100% operational.")