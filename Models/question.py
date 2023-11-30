from db import db
import json

class QuestionModel(db.model):
    __tablename__="Questions"
    
    id=db.Column(db.Integer,primary_key=True)
    question=db.Column(db.String(20000),nullable=False)
    
    # add image column 
    answer = db.Column(db.Integer, nullable=False)
    
    a=db.Column(db.String(3000),nullable=False)
    b=db.Column(db.String(3000),nullable=False)
    c=db.Column(db.String(3000),nullable=True)
    d=db.Column(db.String(3000),nullable=True)
    
    
    #relation between a question and its test
    tests = db.relationship("TestModel",back_populates="questions",secondary="tests_questions")

    #relation between a question and its tags  --> many to many
    tags =db.relationship("TagModel",backpopulates="question",secondary="questions_tags")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    # def set_answer(self, answer_list):
    #     self.answer = json.dumps(answer_list)

    # def get_answer(self):
    #     return json.loads(self.answer) if self.answer else []
    
    
""" 
# Example usage:
# Create a Questions object
question_instance = Questions(question="What is your favorite color?")
# Set the answer using a list
question_instance.set_answer(["Blue", "Green", "Red"])
# Add the instance to the session and commit to the database
db.session.add(question_instance)
db.session.commit()

# Retrieve the instance and get the answer as a list
retrieved_question = Questions.query.filter_by(id=1).first()
answer_list = retrieved_question.get_answer()
print(answer_list)
    
    """