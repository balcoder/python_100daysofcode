'''' Get quiz question from api '''
import requests
from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain

PARAMETERS = {
    "amount": 10,
    "type": "boolean",
    "timeout": 10,
}

URL = "https://opentdb.com/api.php"

def get_quiz_question():
    response = requests.get(URL, params=PARAMETERS)
    response.raise_for_status()
    data = response.json()
    return data

quiz_data = get_quiz_question()
print(quiz_data["results"])

question_bank = []


for question in quiz_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
