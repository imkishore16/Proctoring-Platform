from db import db

import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, Session
from Models.question import QuestionModel
Base = declarative_base()

# class QuestionModel(Base):
#     __tablename__ = "Questions"

#     id = Column(Integer, primary_key=True)
#     question = Column(String(20000), nullable=False)
#     answer = Column(Integer, nullable=False)
#     a = Column(String(3000), nullable=False)
#     b = Column(String(3000), nullable=False)
#     c = Column(String(3000), nullable=True)
#     d = Column(String(3000), nullable=True)

# # Replace 'sqlite:///test.db' with your actual database connection string
# engine = create_engine('sqlite:///test.db')
# Base.metadata.create_all(engine)
# session = Session(engine)

def scrape_geeksforgeeks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(1)
    questions = soup.find_all('div', class_='mtq_question_text')
    print(2)
    print(questions)
    for idx, question in enumerate(questions, start=1):
        print(33)
        question_text = question.find('div', class_='question').text.strip()
        choices = question.find_all('div', class_='option')
        choices_text = [choice.text.strip()[2:] for choice in choices]  # Removing the choice number

        # Extracting correct answer index (assuming it's the first letter of the correct choice)
        correct_choice = question.find('div', class_='mtq_correct_marker').text.strip()
        answer = ord(correct_choice) - ord('A') + 1
        print(3)
        print(
            question=question_text,
            answer=answer,
            a=choices_text[0],
            b=choices_text[1],
            c=choices_text[2] if len(choices_text) > 2 else None,
            d=choices_text[3] if len(choices_text) > 3 else None
        )
        # Create a QuestionModel instance and add it to the database
        # question_instance = QuestionModel(
        #     question=question_text,
        #     answer=answer,
        #     a=choices_text[0],
        #     b=choices_text[1],
        #     c=choices_text[2] if len(choices_text) > 2 else None,
        #     d=choices_text[3] if len(choices_text) > 3 else None
        # )
        # db.session.add(question_instance)

    # db.session.commit()

if __name__ == "__main__":
    url = "https://www.geeksforgeeks.org/top-50-data-structures-mcqs-with-answers/"
    print("start")
    scrape_geeksforgeeks(url)
    print("end")

[<div class="mtq_question_text" id="mtq_question_text-1-1">Which one of the following is an application of Stack Data Structure?</div>, <div class="mtq_question_text" id="mtq_question_text-2-1">
<p>Which one of the following is an application of Queue Data Structure?</p>
</div>, <div class="mtq_question_text" id="mtq_question_text-3-1">
<p>Which of the following sorting algorithms can be used to sort a random linked list with minimum time complexity?</p>
</div>, <div class="mtq_question_text" id="mtq_question_text-4-1">Which of the following is true about linked list implementation of stack?</div>, <div class="mtq_question_text" id="mtq_question_text-5-1">Which of the 
following is an advantage of adjacency list representation over adjacency matrix representation of a graph?</div>, <div class="mtq_question_text" id="mtq_question_text-6-1">
<p>Suppose a circular queue of capacity (n – 1) elements is implemented with an array of n elements. Assume that the insertion and deletion operation are carried out using REAR and FRONT as array index variables, respectively. Initially, REAR = FRONT = 0. The conditions to detect queue full and queue empty are</p>
</div>, <div class="mtq_question_text" id="mtq_question_text-7-1">
<p>A hash table of length 10 uses open addressing with hash function h(k)=k mod 10, and linear probing. After inserting 6 values into an empty hash table, the table is as shown below. </p>
<div class="wp-caption alignnone" style="width: 810px"><img src="https://www.geeksforgeeks.org/wp-content/uploads/gate2010_1.GIF"/><p class="wp-caption-text"> </p></div>
<p>Which one of the following choices gives a possible order in which the key values could have been inserted in the table?</p>
</div>, <div class="mtq_question_text" id="mtq_question_text-8-1">
<p>A program P reads in 500 integers in the range [0..100] representing the scores of 500 students. It then prints the frequency of each score above 50. What would be the best way for P to store the frequencies?<br/> </p>
</div>, <div class="mtq_question_text" id="mtq_question_text-9-1">
<p>The keys 12, 18, 13, 2, 3, 23, 5 and 15 are inserted into an initially empty hash table of length 10 using open addressing with hash function h(k) = k mod 10 and linear probing. What is the resultant hash table?</p><div class="wp-caption alignnone" style="width: 810px"><img sizes="100vw" src="https://media.geeksforgeeks.org/wp-content/uploads/20230414215402/gate_2009_hash-_3_.jpg" srcset="https://media.geeksforgeeks.org/wp-content/uploads/20230414215402/gate_2009_hash-_3_.jpg 542w, https://media.geeksforgeeks.org/wp-content/uploads/20230414215402/gate_2009_hash-_3_-100.jpg 100w, https://media.geeksforgeeks.org/wp-content/uploads/20230414215402/gate_2009_hash-_3_-200.jpg 200w, https://media.geeksforgeeks.org/wp-content/uploads/20230414215402/gate_2009_hash-_3_-300.jpg 300w, " width="542"/><p class="wp-caption-text"> </p></div></div>, <div class="mtq_question_text" id="mtq_question_text-10-1">Suppose the numbers 7, 5, 1, 8, 3, 6, 0, 9, 4, 2 are inserted in that order into an initially empty binary search tree. The binary search tree uses the usual ordering on natural numbers. What is the in-order traversal sequence of the resultant tree?</div>]


