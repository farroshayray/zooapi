def test_get_all_animals(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.execute.return_value.data = [
        {
            "id": 1,
            "species": "Lion",
            "age": 5,
            "gender": "Male",
            "specialRequirements": "None"
        }
    ]

    response = client.get('/animals/')
    assert response.status_code == 200
    assert b"Lion" in response.data
    assert b"Male" in response.data