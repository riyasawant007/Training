import psycopg2

# Database connection parameters
DB_PARAMS = {
    "dbname": "testdb",
    "user": "postgres",
    "password": "world123",
    "host": "localhost",
    "port": 5433,
}

def connect_to_db():
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        print("✅ Connected to the database")
        return conn
    except psycopg2.Error as e:
        print(f"❌ Error connecting to DB: {e}")
        return None

def create_table(conn):
    """Creates a 'users' table if it doesn't exist."""
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INT NOT NULL
    );
    """
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
        print("✅ Table 'users' created or already exists")

def insert_user(conn, name, age):
    """Inserts a new user into the database."""
    query = "INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;"
    with conn.cursor() as cursor:
        cursor.execute(query, (name, age))
        user_id = cursor.fetchone()[0]
        conn.commit()
        print(f"✅ User {name} (ID: {user_id}) inserted successfully")

def fetch_users(conn):
    """Fetches all users from the database."""
    query = "SELECT * FROM users;"
    with conn.cursor() as cursor:
        cursor.execute(query)
        users = cursor.fetchall()
        print("📌 Users in Database:")
        for user in users:
            print(user)

def main():
    """Main execution function."""
    conn = connect_to_db()
    if conn:
        create_table(conn)
        insert_user(conn, "Alice", 25)
        insert_user(conn, "Bob", 30)
        fetch_users(conn)
        conn.close()
        print("✅ Connection closed")

if __name__ == "__main__":
    main()
