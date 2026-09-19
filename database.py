import sqlite3

connection = sqlite3.connect("music.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    file_path TEXT NOT NULL
)
""")

connection.commit()
connection.close()

print("Database Created Successfully")