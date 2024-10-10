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
    
def test_get_single_employee(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = {
        "id": 1,
        "name": "John",
        "email": "abcd@example.com",
        "phone_number": "1234567890",
        "role": "Manager",
        "schedule": "Monday - Friday"
    }
    
    response = client.get('/employees/1')
    assert response.status_code == 200
    assert b"John" in response.data
    assert b"Manager" in response.data
    assert b"abcd@example.com" in response.data
    
def test_get_single_employee_notfound(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = None

    response = client.get('/employees/3')
    
    assert response.status_code == 404
    assert b"not found" in response.data
    
def test_update_employee(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = {
        "id": 1,
        "name": "John",
        "email": "qwerty@example.com",
        "phone_number": "1234567890",
        "role": "Manager",
        "schedule": "Monday - Friday"
    }
    mock_supabase_table.return_value.update.return_value.eq.return_value.execute.return_value.data = {
        "id": 1,
        "name": "William",
        "email": "abcd@example.com",
        "phone_number": "1234567890",
        "role": "Manager",
        "schedule": "Monday - Friday"
    }
    
    response = client.put('/employees/1', json={
        "name": "William",
        "email": "abcd@example.com"
    })
    assert response.status_code == 200
    assert b"Employee updated successfully!" in response.data
    assert b"William" in response.data
    
def test_put_single_employee_notfound(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = None

    response = client.put('/employees/3')
    
    assert response.status_code == 404
    assert b"not found" in response.data
    
def test_delete_employee(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = {
        "id": 1,
        "name": "John",
        "email": "abcd@example.com",
        "phone_number": "1234567890",
        "role": "Manager",
        "schedule": "Monday - Friday"
    }
    
    response = client.delete('/employees/1')
    assert response.status_code == 200
    assert b"Employee deleted successfully!" in response.data
    
def test_delete_single_employee_notfound(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = None

    response = client.delete('/employees/3')
    
    assert response.status_code == 404
    assert b"not found" in response.data