#flask practice
from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world!'

@app.route('/get/<input>')
def get(input):
	return "<h1>you requested: " + input + "</h1>"

if __name__ == '__main__':
	app.debug = True # while true vulnerable to arbitrary code execution!
	app.run()