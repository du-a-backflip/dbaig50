import sqlite3
from config import Config

def create_tables():
    connection = sqlite3.connect(Config.DATABASE)
    cursor = connection.cursor()

    # Drop existing tables if they exist
    cursor.execute("DROP TABLE IF EXISTS user")
    cursor.execute("DROP TABLE IF EXISTS blog")
    cursor.execute("DROP TABLE IF EXISTS entry")

    # Create user table
    cursor.execute("""
    CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    # Create blog table
    cursor.execute("""
    CREATE TABLE blog (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date_posted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user (id)
    )
    """)

    # Create entry table
    cursor.execute("""
    CREATE TABLE entry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        date_posted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        blog_id INTEGER NOT NULL,
        FOREIGN KEY (blog_id) REFERENCES blog (id)
    )
    """)

    # Commit changes and close connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")
