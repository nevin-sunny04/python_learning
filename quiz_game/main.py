from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_object = Question(question['text'], question['answer'])
    question_bank.append(question_object)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    score = quiz_brain.next_question()

print(f"Total Score: {score}")