#selenium server class 
from selenium import webdriver
from pyvirtualdisplay import Display

class Selenium_Instance:
	def __init__(self):
		self.display = Display(visible=0, size=(1024, 768))
		self.display.start()
		self.driver = webdriver.Firefox()
		return

	def get_page(self, url):
		if self.driver is None:
			self.driver = webdriver.Firefox()
		self.driver.get(url)
		return

	def take_screenshot(self):
		if self.driver is None:
			self.driver = webdriver.Firefox()
		self.driver.get_screenshot_as_file("static/screenshot.png")
		return

	def shutdown(self):
		if self.driver:
			self.driver.close()
		if self.display:
			self.display.stop()
		return

