#flask based web server 
from flask import Flask 
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import atexit

import base64
# import socket

from seleniumserver import *

#declare app 
app = Flask(__name__)
serve = None 

@app.route('/')
def index():
	return 'Welcome to Bastion'

@app.route('/hello/<name>')
def hi(name=None):
	n = name
	return render_template("hello.html", data=n)

@app.route('/get_sspng/<url>')
def get_request(url):
	global serve
	decoded_url = base64.urlsafe_b64decode(str(url))
	app.logger.debug("user requested screenshot %s", decoded_url)
	if serve is None:
		serve = Selenium_Instance(app)
	#load site
	serve.get_page(decoded_url)
	#take screenshot
	serve.take_screenshot()
	#serve screenshot
	#clean up
	# serve.shutdown()
	return render_template("screenshot-page.html")

@app.route('/src/<url>')
def source_request(url):
	global serve
	decoded_url = base64.urlsafe_b64decode(str(url))
	app.logger.debug("user requested pagesource %s", decoded_url)
	if serve is None:
		serve = Selenium_Instance(app)
	#load
	serve.get_page(decoded_url)
	src = serve.get_page_source()
	# app.logger.debug(src)
	sheets = serve.get_css_sheets()
	# serve.shutdown()
	return render_template("raw.html", src=src, sheets=sheets)

@app.route('/get_div/<url>')
def div_request(url):
	global serve
	decoded_url = base64.urlsafe_b64decode(str(url))
	app.logger.debug("user requested web-elements %s", decoded_url)
	if serve is None:
		serve = Selenium_Instance(app)
	serve.get_page(decoded_url)
	everything = serve.parse_current_page()
	app.logger.debug(str(everything))
	# serve.shutdown()
	return render_template("floating-div.html", title='Bastion', content=everything, url=decoded_url)

@app.route('/_form_get')
def form_get():
	global serve
	app.logger.debug("post worked")
	form_data = request.args.to_dict()
	app.logger.debug("form data: " + str(form_data))
	serve.populate_form(form_data)
	
	return ""

@app.route('/_back')
def browse_back():
	global serve
	app.logger.debug("browser back")
	serve.back()
	app.logger.debug(str(url_for('.reload')))
	return redirect('http://nimbus.seas.gwu.edu:8888/src_reload')

@app.route('/src_reload')
def reload():
	global serve
	#serve
	src = serve.get_page_source()
	app.logger.debug(src)
	sheets = serve.get_css_sheets()
	# serve.shutdown()
	return render_template("raw.html", src=src, sheets=sheets)

@app.after_request
def add_header(response):
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response

#kill phantom browser on shutdown
def cleanup():
	global serve
	if serve is None:
		return
	else:
		serve.shutdown()


if __name__ == '__main__':
	atexit.register(cleanup) # cleanup for a clean exit
	app.debug = True #True allows for arbitrary code execution!
	app.run(host='0.0.0.0', port=8887)
