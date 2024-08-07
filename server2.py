# Sources: 
# [2]: https://treyhunner.com/2013/02/random-name-generator/
# [3]: https://www.w3schools.com/python/gloss_python_random_number.asp

import sqlite3 # [1]
# import names # [2]
import random # [3]


from flask import Flask


# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/')
def get_time():
	# CHQ: Connect to the database (or create a new one if it doesn't exist)
	conn = sqlite3.connect('example.db') 
	# CHQ: Create a cursor object to interact with the database  
	cursor = conn.cursor()
	
	# CHQ: Create a table called 'employees' with columns 'id', 'name', 'position', and 'salary'
	cursor.execute('''CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)''')
	conn.commit()
	
	# Step 5: Insert some new employees into the 'employees' table
	
	the_names = []
	the_fields = []
	the_salaries = []
	
	the_count = 20
	
	for x in range(the_count):
		curEmployee = "John Stevenson"
		# curEmployee = names.get_full_name()
		the_names.append(curEmployee)
	
	for x in range(the_count):
		curJob = "Software Engineer"
		# FIXME: figure out how to generate random job titles
		# curEmployee = names.get_full_name()
		the_fields.append(curJob)
	
	# for x in range(the_count):
	# 	the_salaries = 1000*random.randrange(44,85)
	# 	# print(the_salaries)
	# 	a = 5
	# 	a = str(5)
	# 	print(a)
	# 	the_salaries.append("str(the_salaries)")
	# 	# the_salaries.append(str(the_salaries))
	
	
	# for x in range(the_count):
	# 	cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (the_names[the_count], the_fields[the_count], the_salaries[the_count]))
	# 	conn.commit()
	  
	thisdict = {
		"Name": "Ford",
		"Age": "Mustang",
		"programming": "1964"
	}

	employee_list = []
	names_list = ['John Doe', 'Ford Mustang', 'Mike Johnson']

	for cur_name in names_list:
		cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (cur_name, 'Software Engineer', 80000))
		conn.commit()
		
		
	
	# cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", ('John Doe', 'Software Engineer', 80000))
	# conn.commit()
	
	# cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", ('Ford Mustang', 'Software Engineer', 78000))
	# conn.commit()
 
	# cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", ('Mike Johnson', 'Software Engineer', 62000))
	# conn.commit()
	
	# Step 6: Query data from the 'employees' table
	# cursor.execute("SELECT name FROM employees")
	cursor.execute("SELECT * FROM employees")
	rows2 = cursor.fetchall()
	for row in rows2:
		# names_list.append(row)
		employee_list.append({"name": row[1], "position": row[2], "salary": row[3]})
		# print(row)
	
	# # Step 7: Update the salary of the employee with id 1
	# cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (90000, 1))
	# conn.commit()
	
	# # Step 8: Delete the employee with id 1
	# cursor.execute("DELETE FROM employees WHERE id = ?", (1,))
	# conn.commit()
	
	# Step 9: Close the connection when you're done
	conn.close()
	# Returning an api for showing in reactjs
	
	# return thisdict
	return employee_list




