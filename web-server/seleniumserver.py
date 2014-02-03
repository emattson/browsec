#selenium server class 
from selenium import webdriver
from pyvirtualdisplay import Display
import base64

class Selenium_Instance:
	def __init__(self, app):
		self.display = Display(visible=0, size=(1024, 768))
		self.display.start()
		self.driver = webdriver.PhantomJS()
		self.app = app
		self.app_location = "/get_div/"
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
	def get_page_source(self):
		source = self.driver.execute_script("return document.getElementsByTagName('body')[0].innerHTML;");
		self.app.logger.debug("IMPORTANT %s", source)
		return source

	def get_css_sheets(self):
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

