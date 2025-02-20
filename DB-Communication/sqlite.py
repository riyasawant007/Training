#Create a simple SQLite database and perform CRUD operations

import sqlite3

# Connect to database (creates if it doesn’t exist)
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Create table
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)""")

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()

# Read data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Close connection
conn.close()
