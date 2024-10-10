from flask import Blueprint, jsonify, request
from modules.db import supabase  # Import supabase client from db.py

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/', methods=['GET', 'POST'])
def manage_employees():
    if request.method == 'POST':
        data = request.get_json()

        existing_employee = supabase.table('Employees').select('*').eq('name', data['name']).execute()
        if existing_employee.data:
            return jsonify({"message": "Employee already exists!"}), 400

        response = supabase.table('Employees').insert({
            'name': data['name'],
            'email': data['email'],
            'phone_number': data['phone_number'],
            'role': data['role'],
            'schedule': data['schedule']
        }).execute()
        return jsonify({"message": "Employee added successfully!", "data": response.data}), 201

    if request.method == 'GET':
        employees = supabase.table('Employees').select('*').execute()
        return jsonify(employees.data), 200


@employees_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def update_delete_employee(id):
    try:
        employee = supabase.table('Employees').select('*').eq('id', id).single().execute()

        if employee.data is None:
            return jsonify({"message": "Employee not found"}), 404

        if request.method == 'GET':
            return jsonify(employee.data), 200

        if request.method == 'PUT':
            data = request.get_json()
            updated_employee = {
                'name': data.get('name', employee.data['name']),
                'email': data.get('email', employee.data['email']),
                'phone_number': data.get('phone_number', employee.data['phone_number']),
                'role': data.get('role', employee.data['role']),
                'schedule': data.get('schedule', employee.data['schedule']),
            }

            response = supabase.table('Employees').update(updated_employee).eq('id', id).execute()

            return jsonify({"message": "Employee updated successfully!", "data": response.data}), 200

        if request.method == 'DELETE':
            response = supabase.table('Employees').delete().eq('id', id).execute()

            return jsonify({"message": "Employee deleted successfully!"}), 200

    except Exception as e:
        if e.code ==  "PGRST116":
            return jsonify({"message": "Employee not found"}), 404
        return jsonify({"message": f"Error: {str(e)}"}), 500
