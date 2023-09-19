from data import question_data
from quiz_brain import Quizbrain, Question

question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz = Quizbrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print(f'Your final score was {quiz.score}/{quiz.question_number}!')
