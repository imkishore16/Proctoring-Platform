from db import db
from datetime import datetime
class UserModel(db.Model):
    __tablename__ = "User"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    register_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    user_type = db.Column(db.String(25), nullable=False)
    user_image = db.Column(db.Text, nullable=False)
    user_login = db.Column(db.SmallInteger, nullable=False)
