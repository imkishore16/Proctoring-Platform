import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class QuestionModel(Base):
    __tablename__ = "Questions"

    id = Column(Integer, primary_key=True)
    question = Column(String(20000), nullable=False)
    answer = Column(Integer, nullable=False)
    a = Column(String(3000), nullable=False)
    b = Column(String(3000), nullable=False)
    c = Column(String(3000), nullable=True)
    d = Column(String(3000), nullable=True)

# Replace 'sqlite:///test.db' with your actual database connection string
engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)
session = Session(engine)

def scrape_geeksforgeeks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    questions = soup.find_all('div', class_='question-block')

    for idx, question in enumerate(questions, start=1):
        question_text = question.find('div', class_='question').text.strip()
        choices = question.find_all('div', class_='option')
        choices_text = [choice.text.strip()[2:] for choice in choices]  # Removing the choice number

        # Extracting correct answer index (assuming it's the first letter of the correct choice)
        correct_choice = question.find('div', class_='correct-option').text.strip()
        answer = ord(correct_choice) - ord('A') + 1

        # Create a QuestionModel instance and add it to the database
        question_instance = QuestionModel(
            question=question_text,
            answer=answer,
            a=choices_text[0],
            b=choices_text[1],
            c=choices_text[2] if len(choices_text) > 2 else None,
            d=choices_text[3] if len(choices_text) > 3 else None
        )
        session.add(question_instance)

    session.commit()

if __name__ == "__main__":
    url = "https://www.geeksforgeeks.org/top-50-data-structures-mcqs-with-answers/"
    scrape_geeksforgeeks(url)
