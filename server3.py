from flask import Flask


# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/')
def get_info_bro():

	# Returning an api for showing in reactjs
	return {
		'Name':"Conrad", 
		"Age":"24",
		"programming":"python, but sometimes JavaScript ;)"
		}


# Running app
# if __name__ == '__main__':
# 	app.run(debug=True)
