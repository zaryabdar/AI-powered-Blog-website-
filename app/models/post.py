from app.Extensions import db
from datetime import datetime

class Post(db.Model):
    __tablename__ ="posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    summary = db.Column(db.String(300), nullable=False)
    content = db.Column(db.Text, nullable=False)
    cover_img = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)