#selenium server class 
from selenium import webdriver
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import base64


class Selenium_Instance:
	def __init__(self, app):
		self.display = Display(visible=0, size=(1024, 768))
		self.display.start()
		self.driver = webdriver.PhantomJS()
		self.app = app
		self.app_location = "/get_div/"
		return

	def back(self):
		if self.driver is None:
			self.driver = webdriver.PhantomJS()
		self.driver.back()
		return
	
	def forward(self):
		if self.driver is None:
			self.driver = webdriver.PhantomJS()
		self.driver.forward()
		return

	def refresh(self):
		if self.driver is None:
			self.driver = webdriver.PhantomJS()
		self.driver.refresh()
		return

	def populate_form(self, data):
		self.app.logger.debug(data['bast_name'])
		form = self.driver.find_element_by_name(data['bast_name']);
		for key in data.keys():
			self.app.logger.debug(key)
			if key != "bast_name" and data[key] != "":
				self.app.logger.debug("form: " + form.get_attribute("name") + "\n  key: " + key)
				element = form.find_element_by_name(key)

				if element.is_displayed():
					element.clear()
					element.send_keys(data[key])
		form.submit()
		return

	def get_page(self, url):
		if self.driver is None:
			self.driver = webdriver.PhantomJS()
		self.driver.get(url)
		return

	def get_elements_by_xpath(self, path):
		if self.driver is None:
			self.driver = webdriver.PhantomJS()
		elements = self.driver.find_elements_by_xpath(path)
		parsed = []
		for element in elements:
			if element.is_displayed():
				attributes = {'id': element.get_attribute("id")}
				attributes['name'] = element.get_attribute("name")
				attributes['class'] = element.get_attribute("class")
				attributes['text'] = element.text
				attributes['x'] = element.location['x']
				attributes['y'] = element.location['y']
				attributes['height'] = element.size['height']
				attributes['width'] = element.size['width']
				attributes['tag'] = element.tag_name
				attributes['src'] = element.get_attribute("src")
				attributes['href'] = self.app_location + base64.urlsafe_b64encode(str(element.get_attribute("href")))
				attributes['action'] = element.get_attribute("action")
				parsed.append(attributes)
				self.app.logger.debug("New element added %s", ' '.join([str(item) for item in attributes]))
		return parsed

	def parse_current_page(self):
		content = []
		content = content + self.get_elements_by_xpath("//form")
		content = content + self.get_elements_by_xpath("//h1")
		content = content + self.get_elements_by_xpath("//h2")
		content = content + self.get_elements_by_xpath("//h3")
		content = content + self.get_elements_by_xpath("//p")
		content = content + self.get_elements_by_xpath("//a")
		content = content + self.get_elements_by_xpath("//input")
		content = content + self.get_elements_by_xpath("//img")
		content = content + self.get_elements_by_xpath("//button")
		content = content + self.get_elements_by_xpath("//li")
		return content

	def take_screenshot(self):
		if self.driver is None:
			self.driver = webdriver.PhantomJS()
		self.driver.get_screenshot_as_file("static/screenshot.png")
		return

	def fix_href(self, link):
		#relative link?
		if not(link.split('/')[0] == "http:" or link.split('/')[0] == "https:" or link[:2] == '//'):
			link = self.driver.current_url + link
		if link[:2] == '//':
			link = "http:" + link
		#parse it!
		self.app.logger.debug("\thref: %s", link)
		return link


	#					#
	#  HELPER FINDERS  	#
	#					#

	#helper finder for form events
		#note that this might disable some form debugging output for the user
	def handle_form_media_events(self, tag):
		form_events = set(["onload", "onblur", "oncontextmenu", "onchange", "onfocus", "onformchange", "onforminput", "oninput", "oninvalid", "onreset", "onselect", "onsubmit"])
		media_events = set(["onabort", "oncanplay", "oncanplaythrough", "ondurationchange", "onemptied", "onended", "onerror", "onloadeddata", "onloadedmetadata", "onloadstart", "onpause", "onplay", "onplaying", "onprogress", "onratechange", "onreadystatechange", "onseeked", "onseeking", "onstalled", "onsuspend", "ontimeupdate", "onvolumechange", "onwaiting"])
		events = form_events.union(media_events) #have to disable all of them
		attributes = tag.attrs # get attributes for tag as dict
		intersect = events.intersection(attributes) #set intersections O(min(len(attributes), len(events)))
		for event in intersect:
			tag[event] = "console.log(event + ' caught and nullified');"
		return len(intersect) > 0


	#helper finder for onclick tags
	def handle_onclick(self, tag):
		if tag.has_attr("onclick"):
			tag["onclick"]='console.log("onclick caught");'
			return True
		return False



	#handle images with viewport
	def handle_images(self, body):
		imgs_driver = self.driver.find_elements_by_xpath("//img")
		imgs_bs = body("img")
		souper = BeautifulSoup()
		for i in range(len(imgs_bs)):
			wrapper = souper.new_tag("div")
			wrapper["class"] = ["viewport"]
			imgs_bs[i].wrap(wrapper) # wrap in viewport
			imgs_bs[i]["class"] = ["clipped"]
			imgs_bs[i]["src"] = "/static/screenshot.png"
			imgs_bs[i]["onload"] = "setViewport(this," + str(imgs_driver[i].location['x']) + ", " + str(imgs_driver[i].location['y']) + ", " +  str(imgs_driver[i].size['width']) + ", " +  str(imgs_driver[i].size['height']) + ");"

		return body

	#get page source and strip of naughtiness 
	def get_page_source(self):
		# source = self.driver.execute_script("return document.getElementsByTagName('body')[0].innerHTML;")
		source = self.driver.page_source

		##note: thread this out!!!! ##
		#take_screenshot() # take screenshot for later use
	

		# self.app.logger.debug("IMPORTANT %s", source)
		soup = BeautifulSoup(source)
		body = soup.body.extract()
		
		# first remove any remaining scripts
		for script in body("script"):
			script.decompose()

		#find all form event objects and remove scripting
		body.find_all(self.handle_form_media_events)

		#find all onclick objects and handle
		body.find_all(self.handle_onclick)


		#handle links
		for link in body("a"):
			if link.has_attr('href'):
				proc_href = self.fix_href(link['href'])
				link['href'] = "/src/" + base64.urlsafe_b64encode(proc_href)
		#handle images
		body = self.handle_images(body)
		self.take_screenshot()
		# for image in body("img"):
		# 	src = image['src']
		# 	if not(src.split('/')[0] == "http:" or src.split('/')[0] == "https:" or src[:2] == '//'):
		# 		#relational image
		# 		image['src'] = "http://" + self.driver.execute_script("return window.document.domain") + src
		#handle style elements
		for style in soup("style"):
			body.insert(0, style)

		#handle videos? NOTE: not done yet
		return body

	def pg_src_image(image, self):
		#get image location
		x,y = self.driver.execute_script("...")
		#get dimensions
		width, height = self.driver.execute_script("...")
		#cutout with dimensions from screenshot
		return 

	def get_css_sheets(self):
		self.app.logger.debug("getting css links now")
		css = self.driver.find_elements_by_xpath("//link[@rel='stylesheet']")
		style_links = []
		for c in css:
			l = c.get_attribute("href")
			if not(l.split('/')[0] == "http:" or l.split('/')[0] == "https:"):
				l = "http://" + self.driver.execute_script("return window.document.domain") + l
			style_links.append(l)
		self.app.logger.debug("Style sheet urls: %s", style_links)
		return style_links

	def shutdown(self):
		if self.driver:
			self.driver.close()
		if self.display:
			self.display.stop()
		return

