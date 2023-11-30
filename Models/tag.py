from db import db 

class TagModel(db.Model):
    __tablename__="tags"
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True,nullable=False)
    
    # # one to many between store and tags
    # question_id=db.Column(db.Integer,db.Foreignkey("question.id"),nullable=False)
    # store =db.relationship("Question",backpopulates="tags")
    
    
    # many to many between items and tags
    questions =db.relationship("QuestionModel",backpopulates="tags",secondary="questions_tags")
    
    

    