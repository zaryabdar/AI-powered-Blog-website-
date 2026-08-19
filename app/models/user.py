from app.Extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    profile_img = db.Column(db.String(255), default="default.jpg")
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)

    posts = db.relationship("Post", backref="author", lazy=True)