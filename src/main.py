# src/main.py

from db import add_citizen, get_all_citizens, update_citizen, delete_citizen

# Add a new citizen record
add_citizen("John Doe", 30, "123 Main Street")

# Retrieve all citizen records
print("All Citizens:")
print(get_all_citizens())

# Update a citizen record
update_citizen(1, "John Doe", 35, "456 Oak Avenue")

# Delete a citizen record
delete_citizen(1)
