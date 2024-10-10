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