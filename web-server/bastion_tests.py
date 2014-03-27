# import os
import webserver_bastion
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        webserver_bastion.app.config['TESTING'] = True
        self.app = webserver_bastion.app.test_client()

    def tearDown(self):
    	pass

if __name__ == '__main__':
    unittest.main()