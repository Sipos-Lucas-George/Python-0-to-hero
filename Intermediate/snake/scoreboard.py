from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roboto Mono", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.__score = 0
        self.__high_score = self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()

    @staticmethod
    def get_high_score():
        with open("data.txt", "r") as file:
            return int(file.read())

    def update_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.__high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.__score} - High Score: {self.__high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.__score > self.__high_score:
            self.__high_score = self.__score
            self.update_high_score()
        self.__score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.__score += 1
        self.update_scoreboard()
