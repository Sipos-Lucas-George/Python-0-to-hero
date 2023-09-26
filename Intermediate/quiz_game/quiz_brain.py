class QuizBrain:
    def __init__(self, question_list: list):
        self.__question_number = 0
        self.__question_list = question_list
        self.__score = 0

    def get_question_number(self) -> int:
        return self.__question_number

    def get_question(self) -> str:
        self.__question_number += 1
        return self.__question_list[self.__question_number - 1].get_text()

    def get_question_answer(self, number: int) -> str:
        return self.__question_list[number].get_answer()

    def get_score(self) -> int:
        return self.__score

    def still_has_questions(self) -> bool:
        return self.__question_number < len(self.__question_list)

    def check_answer(self, answer: str) -> bool:
        if self.__question_list[self.__question_number - 1].get_answer().lower() == answer.lower():
            self.__score += 1
            return True
        return False
