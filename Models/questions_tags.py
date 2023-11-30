from db import db

# this table is called the association table
#this is a secondary table used for many to many relationship between a question and its tags
class ItemTags(db.model):
    __tablename__ = "question_tags"
    
    id=db.Column(db.Integer,primary_key=True )
    #link to questions
    question_id=db.Column(db.Integer,db.Foreignkey("question.id"))
    #link to tags
    tag_id=db.Column(db.Integer,db.Foreignkey("tags.id"))
    