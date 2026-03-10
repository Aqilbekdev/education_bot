import sqlite3

DB_NAME = "education.db"


def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registrations(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        course TEXT,
        full_name TEXT,
        phone TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_registration(user_id, course, full_name, phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO registrations(user_id, course, full_name, phone)
    VALUES (?, ?, ?, ?)
    """, (user_id, course, full_name, phone))

    conn.commit()
    conn.close()

def check_duplicate(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM registrations WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()
    conn.close()

    return result is not None