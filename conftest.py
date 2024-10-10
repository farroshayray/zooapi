import pytest
from main import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.testing = True
    client = app.test_client()

    yield client
    
@pytest.fixture
def mock_supabase_table():
    with patch('modules.db.supabase.table') as mock_table:
        yield mock_table
