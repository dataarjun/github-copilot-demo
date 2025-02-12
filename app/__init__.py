from flask import Flask
from .database.db import init_db
from .routes.product_routes import product_routes

def create_app():
    app = Flask(__name__)
    
    # Initialize the database
    init_db(app)
    
    # Register routes
    app.register_blueprint(product_routes)
    
    return app