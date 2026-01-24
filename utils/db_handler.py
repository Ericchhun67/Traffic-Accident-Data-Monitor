# utils/db_handler.py
"""
db_handler.py
------------------------------------
Handles all database operations for Traffic & Accident Data Monitor.

Includes:
    - Database initialization
    - User management
    - Traffic data
    - Accident data
"""



import sqlite3
from contextlib import closing
import os, sys

# -------------------------------------------------------------------
# DATABASE CONFIGURATION
# -------------------------------------------------------------------
DB_PATH = "database.db"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



# A function to initialize the database and create necessary tables
def init_db():
    """Initialize tables for traffic, accident, and users."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cursor = conn.cursor()

        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        """)

        # Traffic data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS traffic_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                traffic_level TEXT NOT NULL,
                accidents INTEGER,
                avg_speed INTEGER,
                accident_type TEXT,
                timestamp TEXT
            );
        """)

        # Accident data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accident_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                date TEXT NOT NULL,
                fatal INTEGER DEFAULT 0,
                type TEXT,
                description TEXT
            );
        """)

        conn.commit()
        print("[INFO] Database initialized successfully.")


# A function to insert multiple traffic records into the database
def insert_bulk_traffic_data(records):
    """Insert multiple traffic records into the database."""
    if not records:
        print("[WARN] No traffic data to insert.")
        return
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO traffic_data (city, traffic_level, accidents, avg_speed, accident_type, timestamp)
            VALUES (:city, :traffic_level, :accidents, :avg_speed, :accident_type, :timestamp)
        """, records)
        conn.commit()
        print(f"[INFO] Inserted {len(records)} traffic records.")

# A function to retrieve all traffic records from the database
def get_all_traffic_data():
    """Retrieve all traffic records."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM traffic_data ORDER BY id DESC;")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in rows]

# A function to retrieve traffic data for a specific city
def get_city_data(city_name):
    """Retrieve traffic data filtered by city."""
    # retrieve traffic data for the specified city from the database
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM traffic_data WHERE city = ? ORDER BY timestamp DESC;", (city_name,))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in rows]



def insert_bulk_accident_data(records):
    """Insert multiple accident records."""
    if not records:
        print("[WARN] No accident data to insert.")
        return
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO accident_data (city, date, fatal, type, description)
            VALUES (:city, :date, :fatal, :type, :description)
        """, records)
        conn.commit()
        print(f"[INFO] Inserted {len(records)} accident records.")


def get_accident_data(days=7):
    """Retrieve accident records from the past N days."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM accident_data
            WHERE date >= DATE('now', ?)
            ORDER BY date DESC;
        """, (f'-{days} day',))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in rows]



if __name__ == "__main__":
    from utils.data_fetcher import get_traffic_data

    init_db()
    print("[TEST] Generating mock traffic data...")
    data = get_traffic_data(use_mock=True, num_records=5)

    print("[TEST] Inserting mock traffic data...")
    insert_bulk_traffic_data(data)

    print("[TEST] Retrieving data...")
    results = get_all_traffic_data()
    for row in results:
        print(row)