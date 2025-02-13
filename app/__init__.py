from flask import Flask
from app.database.db import init_db
from app.routes.product_routes import product_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database
    init_db(app)
    
    # Register routes
    app.register_blueprint(product_routes)
    
    return app