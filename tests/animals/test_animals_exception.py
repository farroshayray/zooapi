import unittest
from unittest import mock
from main import app

class CustomSupabaseError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

class AnimalExceptionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @mock.patch('modules.db.supabase.table') 
    def test_animal_not_found_exception(self, mock_supabase_table):
        mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.side_effect = \
            CustomSupabaseError("Animal not found", "PGRST116")

        response = self.app.get('/animals/999')

        assert response.status_code == 404
        assert b"Animal not found" in response.data

    @mock.patch('modules.db.supabase.table')
    def test_generic_exception(self, mock_supabase_table):
        mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.side_effect = \
            Exception("Generic error")

        response = self.app.get('/animals/999')

        assert response.status_code == 500
        assert b"Error: Generic error" in response.data

if __name__ == '__main__':
    unittest.main()
