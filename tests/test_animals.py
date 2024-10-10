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

def test_get_single_animal(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = {
        "id": 1,
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "specialRequirements": "None"
    }

    response = client.get('/animals/1')
    assert response.status_code == 200
    assert b"Lion" in response.data
    
def test_get_single_animal_notfound(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = None

    response = client.get('/animals/3')
    
    assert response.status_code == 404
    assert b"not found" in response.data


def test_update_animal(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = {
        "id": 1,
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "specialRequirements": "None"
    }
    mock_supabase_table.return_value.update.return_value.eq.return_value.execute.return_value.data = {
        "id": 1,
        "species": "Lion",
        "age": 6,
        "gender": "Male",
        "specialRequirements": "None"
    }

    response = client.put('/animals/1', json={
        "age": 6
    })
    assert response.status_code == 200
    assert b"Animal updated successfully!" in response.data

def test_put_single_animal_notfound(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = None

    response = client.put('/animals/3')
    
    assert response.status_code == 404
    assert b"not found" in response.data
    
def test_delete_animal(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = {
        "id": 1,
        "species": "Lion",
        "age": 5,
        "gender": "Male",
        "specialRequirements": "None"
    }
    mock_supabase_table.return_value.delete.return_value.eq.return_value.execute.return_value.data = None

    response = client.delete('/animals/1')
    assert response.status_code == 200
    assert b"Animal deleted successfully!" in response.data

def test_delete_single_animal_notfound(client, mock_supabase_table):
    mock_supabase_table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = None

    response = client.delete('/animals/3')
    
    assert response.status_code == 404
    assert b"not found" in response.data