from flask import Flask, jsonify, render_template
from modules.db import supabase  # Import supabase client from db.py
from modules.employees import employees_bp
from modules.animals import animals_bp

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(employees_bp, url_prefix='/employees')
app.register_blueprint(animals_bp, url_prefix='/animals')

@app.route('/')
def home():
    return render_template("welcome.html")
# jsonify({"message": "Welcome to Zoo Management API!"})

# @app.route('/test-supabase')
# def test_supabase():
#     try:
#         response = supabase.table('Employees').select('*').limit(1).execute()
#         return jsonify({"message": "Connected to Supabase", "data": response.data}), 200
#     except Exception as e:
#         return jsonify({"message": f"Failed to connect to Supabase: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
