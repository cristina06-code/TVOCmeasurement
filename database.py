import sqlite3

# Creating the connection and database


def create_connection():
    """Create and return a database connection"""
    return sqlite3.connect("measurements.db")


def create_database():
    """Creates the database and the table if they don't exist"""
    conn = create_connection()
    cur = conn.cursor()

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS entries (
    id             INTEGER      PRIMARY KEY  AUTOINCREMENT,
    TVOC         TEXT         NOT NULL,
    eCO2        TEXT         NOT NULL,
    timestamp      DATETIME     NOT NULL
    )
    """
    )

    conn.commit()
    conn.close()
    print("Database and table are ready!")


if __name__ == "__main__":
    create_database()
