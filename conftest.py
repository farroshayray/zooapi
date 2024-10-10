import pytest

def client():
    from main import app
    
    app.config["Testing"] = True
    with app.test_client() as client:
        yield client