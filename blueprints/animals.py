from flask import Blueprint, request, jsonify
import json

animals_blueprint = Blueprint('animals', __name__)

with open('db.json', 'r') as db:
    database = json.load(db)

@animals_blueprint.route("/", methods=["POST", "GET"])
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
        return jsonify(animal_list)

@animals_blueprint.route("/<int:animal_id>", methods=["GET", "PUT", "DELETE"])
def get_animal_by_id(animal_id):
    animal_list = database.get("animals", [])
    
    for index, animal in enumerate(animal_list):
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
                    
                return jsonify({"message": "Animal deleted"}), 200
    
    return jsonify({"message": "Animal not found"}), 404
