import unittest
from flask import Flask
from main import app
from unittest import mock

class HomeRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        
        assert response.status_code == 200
        assert b'Welcome Animal Lovers!' in response.data

    # def test_main_run(self):
    #     with mock.patch('main.app.run') as mock_run:
    #         app.run(debug=True)

    #         assert mock_run.called, "Expected app.run to be called but it was not"
    #         args, kwargs = mock_run.call_args
    #         assert kwargs.get('debug') == True, "Expected app.run to be called with debug=True"

# if __name__ == '__main__':
#     unittest.main()
