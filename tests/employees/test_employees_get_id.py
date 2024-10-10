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