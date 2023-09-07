'''' Get quiz question from api and display on gui '''
import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

PARAMETERS = {
    "amount": 10,
    "type": "boolean",
    "timeout": 10,
}

URL = "https://opentdb.com/api.php"

def get_quiz_question():
    ''' return data from api in json format '''
    response = requests.get(URL, params=PARAMETERS)
    response.raise_for_status()
    data = response.json()
    return data

quiz_data = get_quiz_question()

question_bank = []

for question in quiz_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz)
