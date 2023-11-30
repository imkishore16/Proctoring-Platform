from db import db  
from datetime import datetime

class EmployerModel(db.Model):
    __tablename__ = 'Employer'

    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    test_id = db.Column(db.String(100), nullable=False)
    
    
