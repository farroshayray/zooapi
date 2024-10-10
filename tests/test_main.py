import unittest
from flask import Flask
from main import app  # Asumsikan bahwa file utama Anda bernama main.py

class HomeRouteTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client untuk Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        # Simulasi request GET ke home route
        response = self.app.get('/')
        
        assert response.status_code == 200
        assert b'Welcome Animal Lovers!' in response.data

if __name__ == '__main__':
    unittest.main()
