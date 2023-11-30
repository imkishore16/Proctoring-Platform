from db import db  
from datetime import datetime

class TestModel(db.Model):
    __tablename__='test'
    
    id = db.Column(db.BigInteger, primary_key=True)#test id
    password = db.Column(db.String(100), nullable=False)
    
    #basic impormation
    test_type = db.Column(db.String(75), nullable=False)#objective
    start = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    end = db.Column(db.TIMESTAMP, nullable=False, default=datetime(1, 1, 1, 0, 0))
    duration = db.Column(db.Integer, nullable=False)
    # show_ans = db.Column(db.Integer, nullable=False)
    recruiting_role=db.Column(db.String(100), nullable=True)
    subject = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    neg_marks = db.Column(db.Integer, nullable=False)
    proctoring_type = db.Column(db.SmallInteger, nullable=False, default=0)
    
    
    
    #relation between test and its questions
    questions = db.relationship("QuestionModel",back_populates="tests",secondary="tests_questions") 
    
