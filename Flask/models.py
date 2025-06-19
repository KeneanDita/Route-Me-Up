from datetime import datetime, timezone
from app import db

class Todo(db.Model):
    __tablename__ = 'todo'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Task {self.id}>'
