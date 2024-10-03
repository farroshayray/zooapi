from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)
with open('db.json', 'r') as db:
    database = json.load(db)

@app.route("/")
def welcome():
    return render_template("welcome.html")
@app.route("/animals", methods=["POST","GET"])
def get_animals():

    if request.method == "POST":
        data = request.json
        species = data.get("species")
        age = data.get("age")
        gender = data.get("gender")
        specialRequirements = data.get("specialRequirements")
        
        animal_list = database.get("animals", [])
        
        for animal in animal_list:
            if animal["species"] == species:
                return jsonify({"message": "Animal already exists"}), 400
        
        new_id = max([animal["id"] for animal in animal_list], default=0) + 1
        new_animal = {
            "id": new_id,
            "species": species,
            "age": age,
            "gender": gender,
            "specialRequirements": specialRequirements
        }
        animal_list.append(new_animal)
        
        with open('db.json', 'w') as db:
            json.dump(database, db, indent=4)
            
        return jsonify(new_animal), 200
        
    elif request.method == "GET":
        animal_list = database.get("animals", [])
        print(animal_list)
        return jsonify(animal_list)
        
@app.route("/animals/<int:animal_id>", methods=["GET", "PUT", "DELETE"])
def get_animal_by_id(animal_id):
    animal_list = database.get("animals", [])
    
    for index, animal in enumerate (animal_list):
        if animal["id"] == animal_id:
            if request.method == "GET":
                return jsonify(animal), 200
            elif request.method == "PUT":
                data = request.json
                animal["species"] = data.get("species", animal["species"])
                animal["age"] = data.get("age", animal["age"])
                animal["gender"] = data.get("gender", animal["gender"])
                animal["specialRequirements"] = data.get("specialRequirements", animal["specialRequirements"])
                
                with open('db.json', 'w') as db:
                    json.dump(database, db, indent=4)
                    
                return jsonify(animal), 200
            elif request.method == "DELETE":
                animal_list.pop(index)
                
                with open('db.json', 'w') as db:
                    json.dump(database, db, indent=4)
                    
                return jsonify({"message": "animal deleted"}), 200
    
    return jsonify({"message": "animal not found"}), 404

#employees

@app.route("/staff", methods=["POST","GET"])
def get_staff():
    if request.method == "POST":
        data = request.json
        staff_name = data.get("name")
        staff_age = data.get("age")
        staff_gender = data.get("gender")
        staff_roles = data.get("roles")
        staff_schedules = data.get("schedules")
        
        staff_list = database.get("employees", [])
        
        for staff in staff_list:
            if staff["name"] == staff_name:
                return jsonify({"message": "staff already exists"}), 400
        
        new_id = max([staff["id"] for staff in staff_list], default=0) + 1
        new_staff = {
            "id": new_id,
            "name": staff_name,
            "age": staff_age,
            "gender": staff_gender,
            "roles": staff_roles,
            "schedules": staff_schedules
        }
        staff_list.append(new_staff)
        
        with open('db.json', 'w') as db:
            json.dump(database, db, indent=4)
            
        return jsonify(new_staff), 200
        
    elif request.method == "GET":
        staff_list = database.get("employees", [])
        print(staff_list)
        return jsonify(staff_list)
    
@app.route("/staff/<int:staff_id>", methods=["GET", "PUT", "DELETE"])
def get_staff_by_id(staff_id):
    staff_list = database.get("employees", [])
    
    for index, staff in enumerate (staff_list):
        if staff["id"] == staff_id:
            if request.method == "GET":
                return jsonify(staff), 200
            elif request.method == "PUT":
                data = request.json
                staff["name"] = data.get("name", staff["name"])
                staff["age"] = data.get("age", staff["age"])
                staff["gender"] = data.get("gender", staff["gender"])
                staff["roles"] = data.get("roles", staff["roles"])
                staff["schedules"] = data.get("schedules", staff["schedules"])
                
                with open('db.json', 'w') as db:
                    json.dump(database, db, indent=4)
                    
                return jsonify(staff), 200
            elif request.method == "DELETE":
                staff_list.pop(index)
                
                with open('db.json', 'w') as db:
                    json.dump(database, db, indent=4)
                    
                return jsonify({"message": "staff deleted"}), 200
    
    return jsonify({"message": "staff not found"}), 404
