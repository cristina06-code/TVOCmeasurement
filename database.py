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
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Failed to insert measurement: {e}")
        return False


def get_last_measurement():
    """Get the last measurement entry"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM entries ORDER BY timestamp DESC LIMIT 1')
    last_measurement = cur.fetchone()
    conn.close()
    return last_measurement


def get_highest_TVOC_measurement():
    """Get the measurement with the highest TVOC value"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM entries ORDER BY TVOC DESC LIMIT 1')
    highest_TVOC_measurement = cur.fetchone()
    conn.close()
    return highest_TVOC_measurement


def get_highest_eCO2_measurement():
    """Get the measurement with the highest eCO2 value"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM entries ORDER BY eCO2 DESC LIMIT 1')
    highest_eCO2_measurement = cur.fetchone()
    conn.close()
    return highest_eCO2_measurement


def get_lowest_TVOC_measurement():
    """Get the measurement with the lowest TVOC value"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM entries ORDER BY TVOC ASC LIMIT 1')
    lowest_TVOC_measurement = cur.fetchone()
    conn.close()
    return lowest_TVOC_measurement


def get_lowest_eCO2_measurement():
    """Get the measurement with the lowest eCO2 value"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM entries ORDER BY eCO2 ASC LIMIT 1')
    lowest_eCO2_measurement = cur.fetchone()
    conn.close()
    return lowest_eCO2_measurement


def get_all_measurements():
    """Get all measurement entries"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM entries ORDER BY timestamp DESC')
    measurements = cur.fetchall()
    conn.close()
    return measurements


# conn = create_connection()
# cur = conn.cursor()

# cur.executemany('INSERT INTO entries (TVOC, eCO2, timestamp) VALUES (?,?,?)', [
#     (300, 400, '06.03.2026 12.23'), (500, 600, '05.03.2026 11.00'), (100, 200, '04.03.2026 10.00'), (50, 230, '03.03.2026 09.00')])
# conn.commit()
# cur.close()
