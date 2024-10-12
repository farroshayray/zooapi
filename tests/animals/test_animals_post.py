def test_create_animal(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.execute.return_value.data = []
    mock_supabase_table.return_value.insert.return_value.execute.return_value.data = {
        "id": 1,
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "specialRequirements": "None"
    }

    response = client.post('/animals/', json={
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "specialRequirements": "None"
    })

    assert response.status_code == 201
    assert b"Animal added successfully!" in response.data


def test_create_animal_already_exist(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.execute.return_value.data = {
        "id": 1,
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "specialRequirements": "None"
    }
    mock_supabase_table.return_value.insert.return_value.execute.return_value.data = [{
        "id": 1,
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "specialRequirements": "None"
    }]

    response = client.post('/animals/', json={
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "specialRequirements": "None"
    })

    assert response.status_code == 400
    assert b"Animal already exists!" in response.data