#flask based web server 
from flask import Flask 
from flask import render_template

from seleniumserver import *

#declare app 
app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to Bastion'

@app.route('/get/<url>')
def get_request(url):
	app.logger.debug("user requested %s", url)
	serve = Selenium_Instance()
	#load site
	serve.get_page("http://" + url)
	#take screenshot
	serve.take_screenshot()
	#serve screenshot
	#clean up
	serve.shutdown()
	return render_template("bastion.html")



if __name__ == '__main__':
	app.debug = True #True allows for arbitrary code execution!
	app.run()