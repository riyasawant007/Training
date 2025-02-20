'''

import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",
    password="world123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        salary FLOAT
    )
""")
conn.commit()

# Insert data
cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", ("Bob", 60000))
conn.commit()

# Read data
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

# Close connection
cursor.close()
conn.close()
'''