from flask import Blueprint, request, jsonify
import json

staff_blueprint = Blueprint('staff', __name__)

with open('db.json', 'r') as db:
    database = json.load(db)

@staff_blueprint.route("/", methods=["POST", "GET"])
def get_staff():
    if request.method == "POST":
        data = request.json
        staff_name = data.get("name")
        staff_email = data.get("email")
        staff_phone_number = data.get("phone_number")
        staff_roles = data.get("roles")
        staff_schedules = data.get("schedules")
        
        staff_list = database.get("employees", [])
        
        for staff in staff_list:
            if staff["name"] == staff_name:
                return jsonify({"message": "Staff already exists"}), 400
        
        new_id = max([staff["id"] for staff in staff_list], default=0) + 1
        new_staff = {
            "id": new_id,
            "name": staff_name,
            "email": staff_email,
            "phone_number": staff_phone_number,
            "roles": staff_roles,
            "schedules": staff_schedules
        }
        staff_list.append(new_staff)
        
        with open('db.json', 'w') as db:
            json.dump(database, db, indent=4)
            
        return jsonify(new_staff), 200
        
    elif request.method == "GET":
        staff_list = database.get("employees", [])
        return jsonify(staff_list)

@staff_blueprint.route("/<int:staff_id>", methods=["GET", "PUT", "DELETE"])
def get_staff_by_id(staff_id):
    staff_list = database.get("employees", [])
    
    for index, staff in enumerate(staff_list):
        if staff["id"] == staff_id:
            if request.method == "GET":
                return jsonify(staff), 200
            elif request.method == "PUT":
                data = request.json
                staff["name"] = data.get("name", staff["name"])
                staff["email"] = data.get("email", staff["email"])
                staff["phone_number"] = data.get("phone_number", staff["phone_number"])
                staff["roles"] = data.get("roles", staff["roles"])
                staff["schedules"] = data.get("schedules", staff["schedules"])
                
                with open('db.json', 'w') as db:
                    json.dump(database, db, indent=4)
                    
                return jsonify(staff), 200
            elif request.method == "DELETE":
                staff_list.pop(index)
                
                with open('db.json', 'w') as db:
                    json.dump(database, db, indent=4)
                    
                return jsonify({"message": "Staff deleted"}), 200
    
    return jsonify({"message": "Staff not found"}), 404
