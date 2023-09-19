
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number != len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            answer = input(f"{self.question_number}. {current_question.text} (true/false): ").lower().replace(' ', '')
            if answer == 'true' or answer == 'false':
                break
            print("Type either 'True' or 'False'")
        actual_answer = current_question.answer
        if self.check_answer(answer, actual_answer):
            self.score += 1
        print(f"The correct answer was: {actual_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer.lower():
            print('You got it correct!')
            return True
        else:
            print('You got it wrong!')
            return False
