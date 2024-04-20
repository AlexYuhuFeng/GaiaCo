# src/db.py

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="database_name",
    user="username",
    password="password"
)

# Function to add a new citizen record
def add_citizen(name, age, address):
    try:
        # Create a cursor
        cur = conn.cursor()

        # SQL query to insert a new citizen record
        sql = "INSERT INTO citizens (name, age, address) VALUES (%s, %s, %s)"
        
        # Execute the SQL query with the provided values
        cur.execute(sql, (name, age, address))

        # Commit the transaction
        conn.commit()
        
        print("Citizen record added successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        # Close the cursor
        cur.close()
