import sqlite3
import random
from datetime import datetime, timedelta

def create_database():
    """Creates a local SQLite database and populates it with messy support ticket data."""
    print("Initializing database connection...")
    conn = sqlite3.connect('../data/analytics_practice.db')
    cursor = conn.cursor()

    # Create Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS raw_tickets (
        ticket_id INTEGER PRIMARY KEY,
        created_date TEXT,
        resolved_date TEXT,
        customer_tier TEXT,
        agent_id INTEGER
    )
    ''')
    
    # Clear existing data for clean run
    cursor.execute('DELETE FROM raw_tickets')

    print("Generating raw support ticket records...")
    tiers = ['VIP', 'vip', 'Standard', 'standard', '  VIP  '] # Deliberately messy data
    
    # Generate 200 mock tickets
    for i in range(1, 201):
        # Randomize creation date within the last 30 days
        days_ago = random.randint(1, 30)
        created = datetime.now() - timedelta(days=days_ago, hours=random.randint(1, 24))
        
        # Determine if resolved (leave some unresolved/null)
        is_resolved = random.choice([True, True, True, False])
        
        if is_resolved:
            # VIPs generally get resolved faster (1-30 hours), Standards (12-72 hours)
            tier = random.choice(tiers)
            if 'vip' in tier.lower():
                resolve_time = timedelta(hours=random.randint(1, 30))
            else:
                resolve_time = timedelta(hours=random.randint(12, 72))
            resolved = (created + resolve_time).strftime('%Y-%m-%d %H:%M:%S')
        else:
            resolved = None

        created_str = created.strftime('%Y-%m-%d %H:%M:%S')
        agent = random.randint(101, 110)
        
        cursor.execute('''
        INSERT INTO raw_tickets (created_date, resolved_date, customer_tier, agent_id)
        VALUES (?, ?, ?, ?)
        ''', (created_str, resolved, random.choice(tiers), agent))

    conn.commit()
    conn.close()
    print("Database initialization complete. Data saved to data/analytics_practice.db")

if __name__ == "__main__":
    create_database()