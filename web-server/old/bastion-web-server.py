#Simple web server
from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from cgi import parse_header
from cgi import parse_multipart
from urlparse import parse_qs

from seleniumserver import *

#constants
PORT = 8080

class Handler(BaseHTTPRequestHandler):

    def do_GET(self) :
        path = self.path[1:]
        print path
        # self.send_error(404, path)
        process_request(path)

        try:
            f = open("screenshot.png")
            self.send_response(200)
            self.send_header('Content-type','image/png')
            self.end_headers()

            self.wfile.write(f.read())
            f.close()
            return
        except IOError:
            self.send_error(404, "url failed to load")



#spin up selenium instance
def spin_up_instance():
    return Selenium_Instance()

#Recieves request for website.  
def process_request(request):
    serve = spin_up_instance()
    #load site
    serve.get_page(request)
    #take screenshot
    serve.take_screenshot()
    #serve screenshot
    #clean up
    serve.shutdown()


#init webserver
httpd = HTTPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()