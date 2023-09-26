class Question:
    def __init__(self, text: str, answer: str):
        self.__text = text
        self.__answer = answer

    def get_text(self):
        return self.__text

    def get_answer(self):
        return self.__answer
