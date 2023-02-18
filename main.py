from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUI
import requests

params = {
    "amount": "10", # change this value for number of questions, max is 50
    "type":"boolean"
}

response = requests.get(url= "https://opentdb.com/api.php", params=params)
question_data = response.json()["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_UI = QuizUI(quiz)
