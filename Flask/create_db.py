from app import create_app, db
from models import Todo  # Ensure model is registered

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created.")
