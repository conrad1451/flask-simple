# This is an SQLite demo originally found on this medium article
# Source: https://medium.com/nishkoder/using-sqlite-database-in-python-projects-73b4d827f1c4

import sqlite3

# Step 1: Import the SQLite library
# Step 2: Connect to the database (or create a new one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Step 3: Create a cursor object to interact with the database
cursor = conn.cursor()

# Step 4: Create a table called 'employees' with columns 'id', 'name', 'position', and 'salary'
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)''')
conn.commit()

# Step 5: Insert a new employee into the 'employees' table
cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", ('John Doe', 'Software Engineer', 80000))
conn.commit()

# Step 6: Query data from the 'employees' table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Step 7: Update the salary of the employee with id 1
cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (90000, 1))
conn.commit()

# Step 8: Delete the employee with id 1
cursor.execute("DELETE FROM employees WHERE id = ?", (1,))
conn.commit()

# Step 9: Close the connection when you're done
conn.close()
