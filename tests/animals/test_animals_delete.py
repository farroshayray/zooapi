 
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