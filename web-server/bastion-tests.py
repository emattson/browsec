# import os
import bastion_web_server_flask.py
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        bastion_web_server_flask.app.config['TESTING'] = True
        self.app = bastion_web_server_flask.app.test_client()

    def tearDown(self):
    	pass

if __name__ == '__main__':
    unittest.main()