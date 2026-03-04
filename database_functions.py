from database import create_connection
# from datetime import datetime
import sqlite3

# Basic functions for the website


def get_entries():
    """Get all entries and order them chronologically"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM entries ORDER BY timestamp DESC')
    entries = cur.fetchall()
    conn.close()
    return entries


def submit_entry(TVOC, eCO2, timestamp):
    """Submit a new entry to the database"""
    try:
        conn = create_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO entries (TVOC, eCO2, timestamp) VALUES (?,?,?)",
            (TVOC.strip(), eCO2.strip(), timestamp)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Failed to submit entry: {e}")
        return False
