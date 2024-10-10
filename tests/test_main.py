import unittest
from flask import Flask
from main import app  # Assuming your main file is named app.py

class HomeRouteTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client for Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        # Simulate a GET request to the home route
        response = self.app.get('/')
        
        # Assert that the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)
        
        # Assert that the HTML page contains the expected content (assuming welcome.html has the word "Welcome")
        self.assertIn(b'Welcome', response.data)

if __name__ == '__main__':
    unittest.main()
