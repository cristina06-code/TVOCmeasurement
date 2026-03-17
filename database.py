'''A module for handling database operations'''
import sqlite3

# Creating the connection and database


def create_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect("measurements.db")
    conn.row_factory = sqlite3.Row  # Enable dictionary-like access to rows
    return conn


def create_database():
    """Creates the database and the table if they don't exist"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS entries (
    id             INTEGER      PRIMARY KEY  AUTOINCREMENT,
    TVOC         INTEGER      NOT NULL,
    eCO2        INTEGER      NOT NULL,
    timestamp      DATETIME     NOT NULL
    )
    """
    )

    conn.commit()
    conn.close()
    print("Database and table are ready!")


if __name__ == "__main__":
    create_database()


def insert_measurement(TVOC, eCO2, timestamp):
    """Insert a new measurement entry into the database"""
    try:
        conn = create_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO entries (TVOC, eCO2, timestamp) VALUES (?,?,?)",
            (TVOC, eCO2, timestamp)
        )
        # stringTime = f"{timestamp}"
        # newFormatTime = stringTime.replace("T", " ")
        # newFormatTime = newFormatTime[:-7]
        # cur.execute(
        #     "UPDATE entries SET timestamp = ? WHERE id = ?", (
        #         newFormatTime, cur.lastrowid)
        # )
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Failed to insert measurement: {e}")
        return False


def get_statistics():
    """Return last, min, and max measurements"""
    conn = create_connection()
    cur = conn.cursor()

    stats = {}

    # Last measurement
    cur.execute("SELECT * FROM entries ORDER BY timestamp DESC LIMIT 1")
    stats["last"] = cur.fetchone()

    # Highest TVOC
    cur.execute("SELECT * FROM entries ORDER BY TVOC DESC LIMIT 1")
    stats["max_TVOC"] = cur.fetchone()

    # Lowest TVOC
    cur.execute("SELECT * FROM entries ORDER BY TVOC ASC LIMIT 1")
    stats["min_TVOC"] = cur.fetchone()

    # Highest eCO2
    cur.execute("SELECT * FROM entries ORDER BY eCO2 DESC LIMIT 1")
    stats["max_eCO2"] = cur.fetchone()

    # Lowest eCO2
    cur.execute("SELECT * FROM entries ORDER BY eCO2 ASC LIMIT 1")
    stats["min_eCO2"] = cur.fetchone()

    conn.close()
    return stats


def get_all_measurements():
    """Get all measurement entries"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM entries ORDER BY timestamp DESC')
    measurements = cur.fetchall()
    conn.close()
    return measurements


def get_measurements_paginated(limit=20, offset=0):
    """Get paginated measurements"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute(
        'SELECT * FROM entries ORDER BY timestamp DESC LIMIT ? OFFSET ?',
        (limit, offset)
    )
    rows = cur.fetchall()

    conn.close()
    return rows


def get_measurements_count():
    """Get total number of measurements"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) as count FROM entries")
    count = cur.fetchone()["count"]

    conn.close()
    return count
