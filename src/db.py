# src/db.py

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="pfs_database",
    user="admin",
    password="password"
)

# Function to add a new citizen record
def add_citizen(name, age, address):
    try:
        # Validate age (positive integer)
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer")
        
        # Create a cursor
        cur = conn.cursor()

        # SQL query to insert a new citizen record
        sql = "INSERT INTO citizens (name, age, address) VALUES (%s, %s, %s)"
        
        # Execute the SQL query with the provided values
        cur.execute(sql, (name, age, address))

        # Commit the transaction
        conn.commit()
        
        print("Citizen record added successfully!")

    except (Exception, psycopg2.DatabaseError, ValueError) as error:
        print("Error:", error)

    finally:
        # Close the cursor
        cur.close()

# Function to retrieve all citizen records
def get_all_citizens():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM citizens")
        rows = cur.fetchall()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
    finally:
        cur.close()

# Function to update a citizen record
def update_citizen(citizen_id, name, age, address):
    try:
        cur = conn.cursor()
        sql = "UPDATE citizens SET name = %s, age = %s, address = %s WHERE id = %s"
        cur.execute(sql, (name, age, address, citizen_id))
        conn.commit()
        print("Citizen record updated successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
    finally:
        cur.close()

# Function to delete a citizen record
def delete_citizen(citizen_id):
    try:
        cur = conn.cursor()
        sql = "DELETE FROM citizens WHERE id = %s"
        cur.execute(sql, (citizen_id,))
        conn.commit()
        print("Citizen record deleted successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
    finally:
        cur.close()
