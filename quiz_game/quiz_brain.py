#asking the question
#checking if its correct
#checking if we are end of the quiz

class QuizBrain:
    score = 0
    def __init__(self, q_list):
        self.question_number = 0
        self.questions = q_list

    def next_question(self):
        current_question = self.questions[self.question_number]
        answer = input(f"Q. {self.question_number + 1}: {current_question.question} (True/False): ")
        self.check_answer(current_question, answer)
        self.question_number += 1
        return self.score

    def check_answer(self,current_question, answer):
        if answer == current_question.correct_answer:
            self.score += 1
            print(f"You're right! Score {self.score}")
        else:
            print(f"You're wrong! Score {self.score}")

    def still_has_questions(self):
        return self.question_number < len(self.questions)

