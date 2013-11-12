#selenium server class 
from selenium import webdriver

class Selenium_Instance:
	def __init__(self):
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
		self.driver.get_screenshot_as_file("screenshot.png")
		return

	def shutdown(self):
		if self.driver:
			self.driver.close()
		return

