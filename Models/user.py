from db import db

class UserModel(db.Model):
    __tablename__ = "User"

    email = db.Column(db.String(30), unique=True, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    user_type = db.Column(db.String(30), nullable=False)
    image_data = db.Column(db.String(20000), nullable=False)