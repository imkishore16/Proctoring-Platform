from db import db


class TestQuestions(db.model):
    __tablename__ = "tests_questions"
    
    id=db.Column(db.Integer,primary_key=True )
    #link to test
    test_id=db.Column(db.Integer,db.Foreignkey("test.id"))
    #link to questions
    question_id=db.Column(db.Integer,db.Foreignkey("question.id"))
    