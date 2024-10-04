from flask import Flask, render_template
from blueprints.animals import animals_blueprint
from blueprints.staff import staff_blueprint
import json

app = Flask(__name__)

# Load database
with open('db.json', 'r') as db:
    database = json.load(db)

# Register Blueprints
app.register_blueprint(animals_blueprint, url_prefix='/animals')
app.register_blueprint(staff_blueprint, url_prefix='/employees')

@app.route("/")
def welcome():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(debug=True)
