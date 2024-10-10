def test_create_employee(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.execute.return_value.data = []
    mock_supabase_table.return_value.insert.return_value.execute.return_value.data = {
        "id": 1,
        "name": "John",
        "email": "zJt5x@example.com",
        "phone_number": "1234567890",
        "role": "Manager",
        "schedule": "Monday - Friday"
    }
    
    response = client.post('/employees/', json={
        "name": "John",
        "email": "zJt5x@example.com",
        "phone_number": "1234567890",
        "role": "Manager",
        "schedule": "Monday - Friday"
    })
    
    assert response.status_code == 201
    assert b"Employee added successfully!" in response.data
    
def test_create_employee_already_exist(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.execute.return_value.data = {
        "id": 1,
        "name": "John",
        "email": "zJt5x@example.com",
        "phone_number": "1234567890",
        "role": "Manager",
        "schedule": "Monday - Friday"
    }
    mock_supabase_table.return_value.insert.return_value.execute.return_value.data = {
        "id": 1,
        "name": "John",
        "email": "zJt5x@example.com",
        "phone_number": "1234567890",
        "role": "Manager",
        "schedule": "Monday - Friday"
    }
    
    response = client.post('/employees/', json={
        "name": "John",
        "email": "zJt5x@example.com",
        "phone_number": "1234567890",
        "role": "Manager",
        "schedule": "Monday - Friday"
    })
    
    assert response.status_code == 400
    assert b"Employee already exists!" in response.data