"""
    Quiz Game
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_repository = []
for x in question_data:
    question_repository.append(Question(x["text"], x["answer"]))
translate_answer = {
    "t": "True",
    "f": "False",
}

quiz = QuizBrain(question_repository)
while quiz.still_has_questions():
    cmd = input(f"Q.{quiz.get_question_number() + 1}: {quiz.get_question()} (t/f): ").lower()
    print("You're wrong!" if not quiz.check_answer(translate_answer[cmd]) else "You're right!")
    print(f"The correct answer was {quiz.get_question_answer(quiz.get_question_number() - 1)}")
    print(f"Score: {quiz.get_score()}/{quiz.get_question_number()}\n")
print("You've completed the quiz!")
print(f"Your final score: {quiz.get_score()}/{quiz.get_question_number()}")
