# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/')
# @app.route('/data')
def get_time():

	# Returning an api for showing in reactjs
	return {
		'Name':"Conrad", 
		"Age":"24",
		"Date":x, 
		"programming":"python, but sometimes JavaScript ;)"
		}

	
# Running app
# if __name__ == '__main__':
# 	app.run(debug=True)
