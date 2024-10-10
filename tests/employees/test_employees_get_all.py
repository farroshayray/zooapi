def test_get_all_employees(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.execute.return_value.data = [
        {
            "id": 1,
            "name": "John",
            "email": "zJt5x@example.com",
            "phone_number": "1234567890",
            "role": "Manager",
            "schedule": "Monday - Friday"
        }
    ]

    response = client.get('/employees/')
    assert response.status_code == 200
    assert b"John" in response.data
    assert b"Manager" in response.data