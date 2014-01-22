#flask based web server 
from flask import Flask 
from flask import render_template

import base64

from seleniumserver import *

#declare app 
app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to Bastion'

@app.route('/hello/<name>')
def hi(name=None):
	n = name
	return render_template("hello.html", data=n)

@app.route('/get_sspng/<url>')
def get_request(url):
	decoded_url = base64.urlsafe_b64decode(str(url))
	app.logger.debug("user requested screenshot %s", decoded_url)
	serve = Selenium_Instance(app)
	#load site
	serve.get_page(decoded_url)
	#take screenshot
	serve.take_screenshot()
	#serve screenshot
	#clean up
	serve.shutdown()
	return render_template("screenshot-page.html")

@app.route('/src/<url>')
def source_request(url):
	decoded_url = base64.urlsafe_b64decode(str(url))
	app.logger.debug("user requested pagesource %s", decoded_url)
	serve = Selenium_Instance(app)
	#load
	serve.get_page(decoded_url)
	src = serve.get_page_source()
	app.logger.debug(src)
	serve.shutdown()
	return render_template("raw.html", src=src)

@app.route('/get_div/<url>')
def div_request(url):
	decoded_url = base64.urlsafe_b64decode(str(url))
	app.logger.debug("user requested web-elements %s", decoded_url)
	serve = Selenium_Instance(app)
	serve.get_page(decoded_url)
	everything = serve.parse_current_page()
	app.logger.debug(str(everything))
	serve.shutdown()
	return render_template("floating-div.html", title='Bastion', content=everything, url=decoded_url)

@app.after_request
def add_header(response):
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response

if __name__ == '__main__':
	app.debug = True #True allows for arbitrary code execution!
	app.run()