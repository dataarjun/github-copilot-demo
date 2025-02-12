from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy database instance
db = SQLAlchemy()

def init_db(app):
    """Initialize the database with the given Flask app."""
    db.init_app(app)

    with app.app_context():
        # Create all tables
        db.create_all()