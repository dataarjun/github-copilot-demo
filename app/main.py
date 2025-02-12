from flask import Flask
from app.database.db import init_db
from app.routes.product_routes import product_routes

def create_app():
    app = Flask(__name__)
    
    # Initialize the database
    init_db(app)
    
    # Register routes
    app.register_blueprint(product_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)