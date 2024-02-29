import sqlite3

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create a table in the database
def create_table(conn):
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS contacts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Cell TEXT NOT NULL,
            Email TEXT
        );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table 'contacts' created successfully")
    except sqlite3.Error as e:
        print(e)

# Function to insert data into the database
def insert_data(conn, data):
    sql = """
        INSERT INTO contacts (Name, Cell, Email)
        VALUES (?, ?, ?)
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Data inserted successfully")
    except sqlite3.Error as e:
        print(e)

# Function to fetch and display all data from the database
def fetch_all_data(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()
        print("\nContact Book:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def main():
    database = "phone_contacts.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        
        # Inserting sample data
        data = [
            ("John Doe", "123-456-7890", "john@example.com"),
            ("Alice Smith", "987-654-3210", "alice@example.com"),
            ("Bob Johnson", "555-555-5555", None),
            ("Emily Brown", "111-222-3333", "emily@example.com"),
            ("Michael Davis", "444-444-4444", None)
        ]
        for contact in data:
            insert_data(conn, contact)
        
        # Fetching and displaying all data
        fetch_all_data(conn)
        
        conn.close()
    else:
        print("Error! Cannot establish connection to the database.")

if __name__ == "__main__":
    main()
