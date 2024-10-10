from flask import Blueprint, jsonify, request
from modules.db import supabase  # Import supabase client from db.py

animals_bp = Blueprint('animals', __name__)

@animals_bp.route('/', methods=['GET', 'POST'])
def manage_animals():
    if request.method == 'POST':
        data = request.get_json()

        existing_animal = supabase.table('Animals').select('*').eq('species', data['species']).execute()
        if existing_animal.data:
            return jsonify({"message": "Animal already exists!"}), 400

        response = supabase.table('Animals').insert({
            'species': data['species'],
            'age': data['age'],
            'gender': data['gender'],
            'specialRequirements': data['specialRequirements']
        }).execute()
        return jsonify({"message": "Animal added successfully!", "data": response.data}), 201

    if request.method == 'GET':
        animals = supabase.table('Animals').select('*').execute()
        return jsonify(animals.data), 200


@animals_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def update_delete_animal(id):
    try:
        animal = supabase.table('Animals').select('*').eq('id', id).single().execute()

        if animal.data is None:
            return jsonify({"message": "Animal not found"}), 404

        if request.method == 'GET':
            return jsonify(animal.data), 200

        if request.method == 'PUT':
            data = request.get_json()
            updated_animal = {
                'species': data.get('species', animal.data['species']),
                'age': data.get('age', animal.data['age']),
                'gender': data.get('gender', animal.data['gender']),
                'specialRequirements': data.get('specialRequirements', animal.data['specialRequirements']),
            }

            response = supabase.table('Animals').update(updated_animal).eq('id', id).execute()

            return jsonify({"message": "Animal updated successfully!", "data": response.data}), 200

        if request.method == 'DELETE':
            response = supabase.table('Animals').delete().eq('id', id).execute()

            return jsonify({"message": "Animal deleted successfully!"}), 200

    except Exception as e:
        if e.code ==  "PGRST116":
            return jsonify({"message": "Animal not found"}), 404
        return jsonify({"message": f"Error: {str(e)}"}), 500
